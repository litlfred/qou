#!/usr/bin/env python3
"""Assertions whose TOLERANCE is computed from the residual it is supposed to bound.

THE DEFECT.  `Assertion.passed` is `|computed - expected| <= tolerance`.  When the
tolerance expression is itself a function of that same residual, the inequality
holds for every input and the assertion cannot fail.  It is not a loose bound —
it is a tautology generator.

WORKED CASE (bean `qou-tol0`).  `computations/atom_mass_derived.py` at
`7f95ad5962^`:

    w.add_assertion(
        f"M({r.element})",
        computed=round(r.M_derived_MeV, 1),
        expected=round(r.M_observed_MeV, 1),
        tolerance=max(abs(r.delta_MeV) * 2, 50),      # <- delta_MeV IS the residual
    )

`delta_MeV = M_derived_MeV - M_observed_MeV`, so the check reads
`|delta| <= max(2|delta|, 50)` and is true for every element, every value, always.
Nine of the ten rows recorded `passed: true` with a computed atomic mass of zero
or negative against expected masses of thousands of MeV.  Fixed in `7f95ad5962`.

WHY THE EXISTING SIX AUDITS MISS IT
-----------------------------------
Checked against this file at `7f95ad5962^`; **zero hits from any of them**:

  * `self_fulfilling_assertion_audit`, `always_vacuous_assertion_scan`,
    `tautological-assertion-census` — all compare `computed` to `expected`.
    Here those two arguments are genuinely different quantities.  They differ
    correctly.  The vacuity is in the third argument, which none of the three
    reads.
  * `vacuous_pass_assertion_scan` — counter-vs-counter; neither side is a counter.
  * `assertion_on_literal_audit` — `computed` traces to a real computation, not
    to a literal.  It is measured; it is simply never tested.
  * `tolerance_below_arithmetic_floor_audit` — the MIRROR of this file.  It reads
    the tolerance argument, and asks whether it is too SMALL to be reachable.
    A tolerance that is too LARGE, and specifically one derived from the
    residual, is outside its question.

And the witness-level detector `witness_assertion_slack_audit` sees this only by
its consequence: it fires when the recorded `tolerance >= |expected|`, which
happens when the computed value collapses to ~0.  A tautological tolerance on a
producer whose numbers happen to be close records a small tolerance and is
invisible there.  Source is the only place the defect is always visible.

METHOD, AND WHAT EACH SIGNAL IS WORTH
-------------------------------------
AST over every `add_assertion(...)` call under `computations/`, `scripts/`,
`tools/`.  Three INDEPENDENT signals, reported separately rather than folded
into one verdict, because they have very different precision:

  SHARED-ROOT   `tolerance` and `computed` reach a common root identifier
                (`r` in the worked case: `r.M_derived_MeV` / `r.delta_MeV`).
                NECESSARY, nowhere near sufficient — a tolerance of
                `abs(expected) * 1e-8` shares a root and is a textbook relative
                tolerance.  Reported for context, never alone.

  RESIDUAL-NAME an identifier in the tolerance matches the residual vocabulary
                (delta/resid/err/diff/gap/dev/miss/sigma...).  A NAME, so it is
                evidence about what the author called the quantity, not about
                what it holds.

  DATAFLOW      the residual-named quantity is assigned, in the same file, from
                an expression mentioning leaves of BOTH `computed` and
                `expected`.  This is the one that distinguishes "named delta"
                from "is the residual", and it is what the worked case needs:
                `delta = M_derived - M_observed` two hundred lines above the
                call, reaching it as a dataclass field.

BLOCKING is SHARED-ROOT + RESIDUAL-NAME + DATAFLOW.  REVIEW is the first two
without the third.  Everything else is context.

NOT FLAGGED, deliberately:
  * a tolerance that is a bare literal, or reaches only module constants — the
    overwhelming majority, and correct.
  * a tolerance built from `expected` alone (`abs(expected) * 1e-8`).  That is a
    relative tolerance; it scales the bound to the SCALE of the quantity, not to
    the ERROR.  It can fail.  The two look similar and are opposites.
  * a comparison deliberately written into the assertion fields — the bean names
    `binding_energy_scale_probe.E0_improves_deuteron`, which asserts
    `computed=|err_e0|, expected=0, tolerance=|err_qb|`: "the E0 error is no
    worse than the Q_beta error".  That IS the claim, the tolerance is a
    DIFFERENT error from the one being bounded, and it can fail.  It lands in
    REVIEW, and the report says so rather than pretending the machine can tell.

Exit 1 on any BLOCKING hit, 0 otherwise.
"""
from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
ROOTS = ("computations", "scripts", "tools")

# Identifier fragments that name an error rather than a scale. Deliberately does
# NOT include "tol"/"eps"/"atol" — those name the bound itself, not the residual.
RESIDUAL_WORDS = (
    "delta", "resid", "err", "diff", "gap", "deviation", "dev_",
    "miss", "discrep", "offset_from", "shortfall",
)
# Names that look residual but are scales/settings, not errors.
RESIDUAL_EXEMPT = ("differ", "different", "difference_quotient", "deriv")

# Methods that change a container in place, so its initialiser is not its value.
_MUTATORS = {"append", "extend", "update", "add", "insert", "setdefault", "pop"}


def _is_residual_name(ident: str) -> bool:
    low = ident.lower()
    if any(x in low for x in RESIDUAL_EXEMPT):
        return False
    return any(w in low for w in RESIDUAL_WORDS)


def _roots(node: ast.AST) -> set[str]:
    """Base identifiers an expression reaches through attribute/subscript/call."""
    out: set[str] = set()
    for n in ast.walk(node):
        if isinstance(n, ast.Name):
            out.add(n.id)
    return out


def _idents(node: ast.AST) -> set[str]:
    """Every identifier mentioned: names, attribute suffixes, string subscripts."""
    out: set[str] = set()
    for n in ast.walk(node):
        if isinstance(n, ast.Name):
            out.add(n.id)
        elif isinstance(n, ast.Attribute):
            out.add(n.attr)
        elif isinstance(n, ast.Subscript) and isinstance(n.slice, ast.Constant):
            if isinstance(n.slice.value, str):
                out.add(n.slice.value)
    return out


# Wrappers and builtins that appear on both sides of almost every assertion.
# Left in, they make any two expressions "share" an identifier and the dataflow
# test degenerates to always-true.
_STOP = {
    "round", "abs", "float", "int", "str", "len", "min", "max", "sum", "sorted",
    "mp", "mpf", "mpmath", "Decimal", "Fraction", "np", "sp", "math",
    "nstr", "fmt", "format", "N", "self", "w", "wb", "builder",
}


def _closure(idents: set[str], index: "_AssignIndex", depth: int = 2) -> set[str]:
    """`idents` plus everything they reach through assignments, minus wrappers."""
    out = set(idents)
    for i in set(idents) - _STOP:
        out |= index.resolve(i, depth=depth)
    return out - _STOP


class _SingleAssign:
    """Names assigned exactly once at module level, mapped to their RHS.

    Substitution is only sound when the name has ONE definition, so a name
    assigned twice (or in a loop, or as a function parameter) is excluded
    rather than guessed at. Deliberately stricter than `_AssignIndex`, which
    is a reachability index and may over-connect on purpose.
    """

    def __init__(self, tree: ast.AST) -> None:
        counts: dict[str, int] = {}
        rhs: dict[str, ast.AST] = {}
        params: set[str] = set()
        for n in ast.walk(tree):
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
                for arg in [*n.args.args, *n.args.posonlyargs, *n.args.kwonlyargs]:
                    params.add(arg.arg)
            elif isinstance(n, (ast.For, ast.AsyncFor)):
                for t in ast.walk(n.target):
                    if isinstance(t, ast.Name):
                        params.add(t.id)
            elif isinstance(n, ast.Assign):
                if len(n.targets) == 1 and isinstance(n.targets[0], ast.Name):
                    nm = n.targets[0].id
                    counts[nm] = counts.get(nm, 0) + 1
                    rhs[nm] = n.value
                else:
                    for t in n.targets:
                        for x in ast.walk(t):
                            if isinstance(x, ast.Name):
                                counts[x.id] = counts.get(x.id, 0) + 2
            elif isinstance(n, ast.AugAssign):
                for x in ast.walk(n.target):
                    if isinstance(x, ast.Name):
                        counts[x.id] = counts.get(x.id, 0) + 2
            elif (isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
                    and n.func.attr in _MUTATORS
                    and isinstance(n.func.value, ast.Name)):
                # `wired = []` then `wired.append(...)`: assigned once, but the
                # initialiser is NOT the value. Substituting it made
                # `len(wired) == len(per_nucleus)` expand to `len([]) == len([])`
                # and report a real coverage check as a tautology. One
                # assignment is not one value when the object is mutable.
                params.add(n.func.value.id)
            elif isinstance(n, ast.Subscript) and isinstance(n.ctx, ast.Store):
                for x in ast.walk(n.value):
                    if isinstance(x, ast.Name):
                        params.add(x.id)
        self.map = {k: v for k, v in rhs.items()
                    if counts.get(k) == 1 and k not in params}

    def expand(self, node: ast.AST, depth: int = 4) -> ast.AST:
        """Substitute single-assignment names into `node`, bounded depth."""
        cur = node
        for _ in range(depth):
            try:
                nxt = _Substituter(self.map).visit(_copy(cur))
            except (SyntaxError, ValueError, RecursionError):
                return cur
            if ast.dump(nxt) == ast.dump(cur):
                return cur
            cur = nxt
        return cur


def _copy(node: ast.AST) -> ast.AST:
    return ast.parse(ast.unparse(node), mode="eval").body


class _Substituter(ast.NodeTransformer):
    """Substitute single-assignment names, in LOAD position only.

    The ctx check is load-bearing, not defensive: a comprehension target is a
    `Name` in STORE position, and rewriting it produces `for f(x) in ...`,
    which does not parse. One producer in this corpus (`min_eig_*`, a generator
    over a call) crashed the whole sweep on exactly that.
    """

    def __init__(self, mapping: dict[str, ast.AST]) -> None:
        self.map = mapping

    def visit_Name(self, node: ast.Name):  # noqa: N802
        if not isinstance(getattr(node, "ctx", None), ast.Load):
            return node
        repl = self.map.get(node.id)
        return _copy(repl) if repl is not None else node


def _strip_wrappers(node: ast.AST) -> ast.AST:
    """Peel display/precision wrappers that never change the value compared.

    `float`, `fmt`, `str`, `mp.nstr`, `round(x, n)` and friends are formatting.
    `abs` is NOT peeled — it changes the value and is load-bearing below.
    """
    peel = {"float", "fmt", "str", "nstr", "mpf", "mpmathify", "N", "Decimal"}
    cur = node
    while isinstance(cur, ast.Call) and cur.args:
        fn = cur.func
        name = fn.attr if isinstance(fn, ast.Attribute) else getattr(fn, "id", None)
        if name in peel or (name == "round" and len(cur.args) <= 2):
            cur = cur.args[0]
        else:
            break
    return cur


def _unary_minus(node: ast.AST) -> ast.AST:
    """Peel a leading unary minus."""
    while isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        node = node.operand
    return node


def _same(a: ast.AST | None, b: ast.AST | None, *, up_to_sign: bool = False) -> bool:
    if a is None or b is None:
        return False
    a, b = _strip_wrappers(a), _strip_wrappers(b)
    if up_to_sign:
        # Inside an `abs(...)`, sign is already discarded: `abs(G)` bounds
        # `expected = -G` exactly as well as it bounds `G`. Without this the
        # yekutieli case — computed=kappa, expected=-G,
        # tolerance=max(|kappa|,|G|)*2 — fails to match and lands in `context`
        # despite being unfalsifiable by the triangle inequality.
        a, b = _unary_minus(a), _unary_minus(b)
    return ast.dump(a) == ast.dump(b)


def _abs_of(node: ast.AST) -> ast.AST | None:
    """If `node` is `abs(x)`, return x."""
    if (isinstance(node, ast.Call) and getattr(node.func, "id", None) == "abs"
            and len(node.args) == 1):
        return node.args[0]
    return None


def _const(node: ast.AST) -> float | None:
    try:
        v = ast.literal_eval(node)
        return float(v) if isinstance(v, (int, float)) else None
    except (ValueError, TypeError, SyntaxError):
        return None


def _provable_bound(tol: ast.AST, comp: ast.AST, exp: ast.AST | None) -> str | None:
    """Return a proof sketch if `|comp - exp| <= tol` holds for ALL values.

    Three forms, each an instance of the triangle inequality and none of them a
    heuristic — the assertion is unfalsifiable as arithmetic, whatever the data:

        k * max(|c|, |e|)   with k >= 2   since |c-e| <= |c|+|e| <= 2max
        k * (|c| + |e|)     with k >= 1
        k * |c - e|         with k >= 1   the residual bounding itself

    `max(<form>, <literal>)` also qualifies: taking a max with anything only
    enlarges the bound, so it cannot rescue the check.
    """
    t = _strip_wrappers(tol)

    # max(<form>, literal) -> recurse on the non-literal arm
    if (isinstance(t, ast.Call) and getattr(t.func, "id", None) == "max"
            and len(t.args) == 2):
        for i in (0, 1):
            if _const(t.args[1 - i]) is not None:
                got = _provable_bound(t.args[i], comp, exp)
                if got:
                    return got + " (max with a literal only enlarges it)"

    k = 1.0
    body = t
    if isinstance(t, ast.BinOp) and isinstance(t.op, ast.Mult):
        for lit, other in ((t.left, t.right), (t.right, t.left)):
            c = _const(lit)
            if c is not None:
                k, body = c, other
                break
    body = _strip_wrappers(body)

    # k * |c - e|
    inner = _abs_of(body)
    if inner is not None and isinstance(inner, ast.BinOp) and isinstance(inner.op, ast.Sub):
        if ((_same(inner.left, comp) and _same(inner.right, exp))
                or (_same(inner.left, exp) and _same(inner.right, comp))):
            if k >= 1:
                return f"tolerance = {k:g}*|computed - expected|, k >= 1"

    # k * max(|c|, |e|)
    if (isinstance(body, ast.Call) and getattr(body.func, "id", None) == "max"
            and len(body.args) == 2):
        a0, a1 = _abs_of(_strip_wrappers(body.args[0])), _abs_of(_strip_wrappers(body.args[1]))
        if a0 is not None and a1 is not None:
            if ((_same(a0, comp, up_to_sign=True) and _same(a1, exp, up_to_sign=True))
                    or (_same(a0, exp, up_to_sign=True) and _same(a1, comp, up_to_sign=True))):
                if k >= 2:
                    return (f"tolerance = {k:g}*max(|computed|,|expected|), k >= 2; "
                            "|c-e| <= |c|+|e| <= 2max")

    # k * (|c| + |e|)
    if isinstance(body, ast.BinOp) and isinstance(body.op, ast.Add):
        a0, a1 = _abs_of(_strip_wrappers(body.left)), _abs_of(_strip_wrappers(body.right))
        if a0 is not None and a1 is not None:
            if ((_same(a0, comp, up_to_sign=True) and _same(a1, exp, up_to_sign=True))
                    or (_same(a0, exp, up_to_sign=True) and _same(a1, comp, up_to_sign=True))):
                if k >= 1:
                    return f"tolerance = {k:g}*(|computed|+|expected|), k >= 1"

    return None


def _is_constant_expr(node: ast.AST) -> bool:
    """True if the expression bottoms out in literals only (no names at all)."""
    return not _roots(node)


class _AssignIndex:
    """Every `<target> = <rhs>` and `<field>=<rhs>` keyword in one module.

    Attribute and dataclass-field assignment both matter here: the worked case
    reaches its residual as `r.delta_MeV`, whose only definition is the keyword
    `delta_MeV=delta` in a dataclass constructor call, and `delta` itself is a
    plain local two lines above that.  A scanner that indexed only plain
    `Name = ...` assignments would follow `r.delta_MeV` nowhere and report the
    known positive as REVIEW.
    """

    def __init__(self, tree: ast.AST) -> None:
        self.by_name: dict[str, list[ast.AST]] = {}
        for n in ast.walk(tree):
            if isinstance(n, ast.Assign):
                for t in n.targets:
                    for key in self._target_keys(t):
                        self.by_name.setdefault(key, []).append(n.value)
            elif isinstance(n, ast.AnnAssign) and n.value is not None:
                for key in self._target_keys(n.target):
                    self.by_name.setdefault(key, []).append(n.value)
            elif isinstance(n, ast.Call):
                for kw in n.keywords:
                    if kw.arg:
                        self.by_name.setdefault(kw.arg, []).append(kw.value)

    @staticmethod
    def _target_keys(t: ast.AST) -> list[str]:
        if isinstance(t, ast.Name):
            return [t.id]
        if isinstance(t, ast.Attribute):
            return [t.attr]
        if isinstance(t, (ast.Tuple, ast.List)):
            keys: list[str] = []
            for e in t.elts:
                keys.extend(_AssignIndex._target_keys(e))
            return keys
        return []

    def resolve(self, ident: str, depth: int = 3) -> set[str]:
        """Identifiers reachable from `ident` by following assignments."""
        seen: set[str] = set()
        frontier = {ident}
        for _ in range(depth):
            nxt: set[str] = set()
            for name in frontier:
                for rhs in self.by_name.get(name, []):
                    for got in _idents(rhs):
                        if got not in seen:
                            seen.add(got)
                            nxt.add(got)
            frontier = nxt
            if not frontier:
                break
        return seen


def _call_args(call: ast.Call) -> dict[str, ast.AST]:
    """Map add_assertion's positional+keyword arguments onto parameter names."""
    order = ["name", "computed", "expected", "tolerance", "unit", "source"]
    out: dict[str, ast.AST] = {}
    for i, a in enumerate(call.args):
        if i < len(order):
            out[order[i]] = a
    for kw in call.keywords:
        if kw.arg in order:
            out[kw.arg] = kw.value
    return out


def scan_file(path: Path) -> list[dict]:
    try:
        src = path.read_text(encoding="utf-8")
        tree = ast.parse(src)
    except (SyntaxError, UnicodeDecodeError):
        return []
    index = _AssignIndex(tree)
    single = _SingleAssign(tree)
    hits: list[dict] = []

    for node in ast.walk(tree):
        if not (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)):
            continue
        if node.func.attr != "add_assertion":
            continue
        args = _call_args(node)
        tol = args.get("tolerance")
        comp = args.get("computed")
        exp = args.get("expected")
        if comp is None:
            continue

        # ---- provable shape A: computed and expected are the SAME expression
        # once single-assignment names are substituted. The residual is
        # identically zero and the tolerance never enters. Syntactically the
        # two arguments differ, so the tautology census (which compares the
        # raw ASTs) cannot see it.
        # Raw-identical arguments are NOT this audit's finding: `computed=3,
        # expected=3` is already covered by `always_vacuous_assertion_scan`,
        # `self_fulfilling_assertion_audit` and the qou-26f2 census, all of
        # which compare the two ASTs directly. Reporting them here would
        # inflate this count with 200-odd hits someone else already owns.
        # What is new is only the case that needs an INDIRECTION to see.
        if exp is not None and ast.dump(comp) != ast.dump(exp):
            ce, ee = single.expand(_strip_wrappers(comp)), single.expand(_strip_wrappers(exp))
            if ast.dump(ce) == ast.dump(ee):
                hits.append(_hit("blocking", "identical-after-substitution", path, node,
                                 args, comp, exp, tol,
                                 proof=f"both sides expand to `{ast.unparse(ce)}`; "
                                       "residual is identically 0"))
                continue

        if tol is None:
            continue

        # ---- provable shape B: the tolerance is a triangle-inequality bound on
        # the very residual it gates, so the assertion holds for all values.
        proof = _provable_bound(tol, comp, exp)
        if proof:
            hits.append(_hit("blocking", "triangle-bound", path, node,
                             args, comp, exp, tol, proof=proof))
            continue

        if _is_constant_expr(tol):
            continue

        tol_roots, comp_roots = _roots(tol), _roots(comp)
        exp_roots = _roots(exp) if exp is not None else set()
        shared = tol_roots & comp_roots
        tol_idents = _idents(tol)
        residual_named = sorted(i for i in tol_idents if _is_residual_name(i))

        # A tolerance built ONLY from `expected` is a relative tolerance, not a
        # residual bound. Do not report it at all.
        if not shared and (tol_roots & exp_roots):
            continue
        if not shared and not residual_named:
            continue

        # DATAFLOW: does a residual-named identifier in the tolerance resolve,
        # through assignments, to something mentioning BOTH sides' quantities?
        #
        # Both sides must be CLOSED over assignments, not just read off the call.
        # The worked case is exactly why: the tolerance reaches `delta`, whose
        # definition is `delta = M_derived - M_obs`, while `computed` reads
        # `r.M_derived_MeV`. Those two names never meet — the link is the
        # dataclass keyword `M_derived_MeV=M_derived` one construction earlier.
        # Comparing raw leaves against the residual's reach put the known
        # positive in REVIEW; closing both sides is what recovers it.
        comp_leaves = _closure(_idents(comp), index)
        exp_leaves = _closure(_idents(exp), index) if exp is not None else set()
        dataflow: list[str] = []
        for ident in residual_named:
            reach = index.resolve(ident) - _STOP
            if (reach & comp_leaves) and (reach & exp_leaves):
                dataflow.append(ident)

        if dataflow:
            tier = "blocking"
        elif residual_named and shared:
            tier = "review"
        else:
            tier = "context"

        hits.append(_hit(tier, "residual-named", path, node, args, comp, exp, tol,
                         shared_roots=sorted(shared),
                         residual_named=residual_named,
                         dataflow_confirmed=dataflow))
    return hits


def _hit(tier: str, shape: str, path: Path, node: ast.Call, args: dict,
         comp, exp, tol, **extra) -> dict:
    h = {
        "tier": tier,
        "shape": shape,
        "file": str(path.relative_to(REPO)) if REPO in path.parents else str(path),
        "line": node.lineno,
        "assertion": ast.unparse(args["name"]) if "name" in args else "?",
        "computed": ast.unparse(comp),
        "expected": ast.unparse(exp) if exp is not None else None,
        "tolerance": ast.unparse(tol) if tol is not None else None,
        "shared_roots": [],
        "residual_named": [],
        "dataflow_confirmed": [],
        "proof": None,
    }
    h.update(extra)
    return h


def iter_py(extra: list[Path] | None = None):
    if extra:
        yield from extra
        return
    for r in ROOTS:
        for p in (REPO / r).rglob("*.py"):
            if "_deprecated" in p.parts or ".lake" in p.parts:
                continue
            yield p


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("paths", nargs="*", type=Path,
                    help="scan these files instead of the whole tree")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true",
                    help="check the known positive and the known benign case")
    a = ap.parse_args()

    if a.selftest:
        return selftest()

    hits = []
    for p in iter_py([q.resolve() for q in a.paths] if a.paths else None):
        hits.extend(scan_file(p))

    by = {t: [h for h in hits if h["tier"] == t] for t in ("blocking", "review", "context")}

    if a.json:
        print(json.dumps({"counts": {k: len(v) for k, v in by.items()}, "hits": hits},
                         indent=2))
        return 1 if by["blocking"] else 0

    print("tolerance-from-residual audit")
    print(f"  scanned add_assertion calls with a non-constant tolerance: {len(hits)}")
    for tier, blurb in (
        ("blocking", "tolerance is the residual it bounds — the check cannot fail"),
        ("review",   "residual-named tolerance sharing a root with `computed`; "
                     "a deliberate error-vs-error comparison lands here too"),
        ("context",  "shares a root with `computed` but nothing names an error — "
                     "usually a legitimate relative tolerance"),
    ):
        rows = by[tier]
        print(f"\n== {tier}: {len(rows)} ==\n  {blurb}")
        for h in rows if tier != "context" else rows[:12]:
            print(f"  [{h['shape']}] {h['file']}:{h['line']}  {h['assertion']}")
            print(f"      computed  = {h['computed']}")
            print(f"      expected  = {h['expected']}")
            print(f"      tolerance = {h['tolerance']}")
            if h["proof"]:
                print(f"      PROOF: {h['proof']}")
            if h["dataflow_confirmed"]:
                print(f"      residual confirmed by dataflow: "
                      f"{', '.join(h['dataflow_confirmed'])}")
        if tier == "context" and len(rows) > 12:
            print(f"  … and {len(rows) - 12} more")

    return 1 if by["blocking"] else 0


def selftest() -> int:
    """Calibrate on one known positive and one known benign case.

    The positive is only reachable from git history — it was fixed in
    `7f95ad5962` — so the self-test writes the pre-fix source to a temp file and
    scans that. A detector that cannot re-find the case it was written for is
    reporting on itself.
    """
    import subprocess, tempfile
    ok = True

    try:
        pre = subprocess.run(
            ["git", "show", "7f95ad5962^:computations/atom_mass_derived.py"],
            cwd=REPO, capture_output=True, text=True, check=True).stdout
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"  SKIP  pre-fix source unavailable ({e.__class__.__name__})")
        pre = None

    if pre is not None:
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "atom_mass_derived.py"
            f.write_text(pre, encoding="utf-8")
            hits = scan_file(f)
        block = [h for h in hits if h["tier"] == "blocking"]
        if block:
            print(f"  PASS  known positive re-found: {len(block)} blocking "
                  f"(tolerance = {block[0]['tolerance']}, "
                  f"dataflow via {block[0]['dataflow_confirmed']})")
        else:
            tiers = sorted({h["tier"] for h in hits}) or ["none"]
            print(f"  FAIL  known positive NOT blocking — got {tiers}")
            ok = False

    # Both PROVABLE shapes, pinned to SYNTHETIC fixtures rather than to live
    # files. The first version of this self-test pinned them to
    # `yekutieli_borromean_h2_extraction.py:216` and
    # `mass-from-q-symbolic.py:577` — the two cases that motivated them — and
    # then went red the moment the first of those was FIXED. A calibration
    # that a successful drain breaks is measuring the corpus, not the
    # detector. Cite the rule; re-measure the instance.
    fixtures = {
        "triangle-bound": (
            "kappa_computed",
            'w.add_assertion("kappa_computed", computed=kappa, expected=-G,\n'
            '                tolerance=max(abs(float(kappa)), abs(float(G))) * 2)\n',
        ),
        "identical-after-substitution": (
            "mass_in_MeV",
            "ratio = VOL / HBAR_SQ\n"
            "mass_MeV = ratio * M_E\n"
            'w.add_assertion("mass_in_MeV", computed=mass_MeV,\n'
            "                expected=ratio * M_E, tolerance=mass_err)\n",
        ),
    }
    for shape, (name, src) in fixtures.items():
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "fixture.py"
            f.write_text(src, encoding="utf-8")
            got = [h for h in scan_file(f) if h["assertion"].strip("\"'") == name]
        if got and got[0]["tier"] == "blocking" and got[0]["shape"] == shape:
            print(f"  PASS  {shape} fires on its fixture")
        else:
            print(f"  FAIL  {shape} lost — got "
                  f"{[(h['tier'], h['shape']) for h in got] or 'nothing'}")
            ok = False

    # NEGATIVE CONTROL. Locks in the two corrections that took this audit from
    # 38 blocking to 6: a relative tolerance built from `expected` is not a
    # residual bound, and a container assigned once but MUTATED afterwards must
    # not be substituted by its initialiser. Both were false positives here.
    control = """
import x
wired = []
per_nucleus = []
for k in x.items():
    wired.append(k)
    per_nucleus.append(k)
w.add_assertion("coverage", computed=len(wired), expected=len(per_nucleus), tolerance=0)
w.add_assertion("relative", computed=measured, expected=reference,
                tolerance=abs(reference) * 1e-8)
"""
    with tempfile.TemporaryDirectory() as d:
        f = Path(d) / "control.py"
        f.write_text(control, encoding="utf-8")
        bad = [h for h in scan_file(f) if h["tier"] == "blocking"]
    if bad:
        print("  FAIL  negative control flagged BLOCKING: "
              f"{[h['assertion'] for h in bad]}")
        ok = False
    else:
        print("  PASS  negative control clean (mutated container, relative tolerance)")

    benign = REPO / "computations/probes/binding_energy_scale_probe.py"
    if benign.exists():
        hits = [h for h in scan_file(benign)
                if h["assertion"].strip("\"'") == "E0_improves_deuteron"]
        if any(h["tier"] == "blocking" for h in hits):
            print("  FAIL  known benign case flagged BLOCKING "
                  "(it is an error-vs-error comparison and can fail)")
            ok = False
        else:
            got = hits[0]["tier"] if hits else "not reported"
            print(f"  PASS  known benign case is {got}, not blocking")
    else:
        print("  SKIP  benign calibration file absent")

    print("selftest:", "OK" if ok else "FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
