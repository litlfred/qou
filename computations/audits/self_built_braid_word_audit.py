#!/usr/bin/env python3
"""Which producers BUILD their own braid word instead of asking for it.

Three sweeps have now looked for fallout from the 2026-09-05 ordering ruling
(`qou-hu1f`: the canonical intra-nucleon core is the interleaved Borromean
`(s0 s1^-1)^3`, not the grouped word), and all three missed the same producer:

  * the `qou-hu1f` witness sweep      -- keyed on witness fields
  * `binding_canonical`'s own audit   -- keyed on the producer's import cone
  * `qou-cvky` / PR #6940             -- keyed on files that RAISE

`closed_form_tau_M.compute_tau_M_nucleon_H3` is invisible to all three, and
the reason is worth naming precisely (bean `qou-y2o7`): it does not receive a
word and choke on it. It **constructs a monotone word itself**, out of the
`hecke_core` chains, and hands that to the monotone-only kernel. The kernel's
precondition is satisfied, nothing raises, and the function returns a
plausible 50-dps number that is simply the superseded ordering -- measured
tau_p 1.1458 where the canonical word gives 0.6293, a factor 1.82.

So a selector keyed on BREAKAGE finds the loud cases and undercounts the
silent ones to zero. This audit keys on the opposite feature: **where the word
came from**.

## What it classifies

For every call into a chi kernel, the first positional argument is the word.
This walks the enclosing function (and module) scope and resolves that
argument's provenance:

| verdict | meaning |
|---|---|
| `CANONICAL` | comes from `atom_braid_word_3A` -- the ruling's own emitter |
| `SELF_BUILT` | built in place from list/tuple literals or a comprehension |
| `MIXED` | bound BOTH ways -- a canonical path plus a self-built branch |
| `INHERITED` | a parameter; the caller decides, so audit the caller |
| `OTHER` | some other call or name -- reported, not judged |

`SELF_BUILT` is the class the three sweeps miss. It is a CANDIDATE, not a
verdict: a self-built word is legitimate when the producer is deliberately
testing a non-atom braid (a Hopf link, a bare generator, a scaling sweep).
What makes it a defect is a self-built word standing in for an ATOM word.

`MIXED` exists because a CORRECT FIX takes that shape, and reading only a
name's last binding calls the fix a defect. Measured: hours after
`compute_tau_M_nucleon_H3` was repaired on `main` (option B -- canonical word
by default, the old chain kept behind `intra_order="grouped"` as a documented
escape hatch), this audit still flagged it, because the historical branch is
the later assignment. A false positive that sends the next agent to re-fix a
correct file is worse than a miss. `MIXED` is reported and NOT flagged: the
defect being hunted is a producer with no canonical path at all.

## The second, value-keyed half

Where a self-built word's generator indices are literals, the generator
sequence is recovered statically and tested for monotonicity. That matters
because the two are equivalent here:

    monotone       <=>  grouped     (the superseded ordering)
    non-monotone   <=>  borromean   (the ruling)

A self-built word that is monotone AND is being used as an atom word is the
`compute_tau_M_nucleon_H3` shape exactly. Reported as `MONOTONE_LITERAL`.

## What it deliberately does NOT do

It does not decide whether a given producer OUGHT to use an atom word -- that
is a reading of the producer's purpose, not a property of its syntax. It
narrows the corpus to the handful a human must read, which is the whole point:
the three previous selectors narrowed it to zero.

No arithmetic, so no precision surface. Pure AST.
Exit 0 always -- this is a census, not a gate. Use `--strict` to exit 1 when
any `MONOTONE_LITERAL` is found.
"""
from __future__ import annotations

import argparse
import ast
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent

# The chi kernels. A word reaches the representation through one of these.
CHI_KERNELS = {
    "chi_all_lambda",
    "chi_all_lambda_reduced_block",
    "chi_all_lambda_window",
    "chi_all_lambda_general",
    "chi_all_lambda_any",
}

# The ruling's own word emitter. A word from here is canonical by construction.
CANONICAL_EMITTERS = {"atom_braid_word_3A", "atom_braid_word", "braid_word_3A"}

SEARCH_ROOTS = ["computations", "tools", "qou-mass"]
SKIP_PARTS = {"_deprecated", ".git", "node_modules", "__pycache__", ".lake"}


def _iter_py():
    for r in SEARCH_ROOTS:
        base = ROOT / r
        if not base.is_dir():
            continue
        for p in sorted(base.rglob("*.py")):
            if any(part in SKIP_PARTS for part in p.parts):
                continue
            yield p


def _scopes(tree):
    """Yield (scope_node, body) for the module and every function in it."""
    yield tree
    for n in ast.walk(tree):
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
            yield n


def _params(fn):
    if not isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)):
        return set()
    a = fn.args
    out = {x.arg for x in list(a.args) + list(a.posonlyargs) + list(a.kwonlyargs)}
    if a.vararg:
        out.add(a.vararg.arg)
    if a.kwarg:
        out.add(a.kwarg.arg)
    return out


def _gen_index(elt):
    """The generator index of a word element, if it is a literal.

    A word element is `(c, d, gen)` or `(d, gen)` -- the generator is the LAST
    slot in both shapes, which is why this reads from the end rather than
    assuming an arity. Returns None when it is not a plain integer literal.
    """
    if not isinstance(elt, (ast.Tuple, ast.List)) or not elt.elts:
        return None
    last = elt.elts[-1]
    if isinstance(last, ast.Constant) and isinstance(last.value, int):
        return last.value
    # `-1` and friends parse as UnaryOp, not Constant.
    if (isinstance(last, ast.UnaryOp) and isinstance(last.op, ast.USub)
            and isinstance(last.operand, ast.Constant)
            and isinstance(last.operand.value, int)):
        return -last.operand.value
    return None


def _rewrap_source(node):
    """If `node` is a comprehension that merely RE-WRAPS another word, return
    the expression it re-wraps; else None.

    The shape, which is what a producer writes when it coerces an existing
    chain to mpf:

        word = [(mp.mpf(str(c)), mp.mpf(str(d)), g) for c, d, g in chain]

    The element's generator slot is `g`, bound by the comprehension's own
    target, so it carries no literal of its own -- the generators live in
    `chain`. Reading only the element and stopping is what a first version of
    this audit did, and it cost a true positive: at
    `nucleon_h3_marshalling_divergence_probe.py:144` the very next line up
    binds `chain` to literal generators `[0, 1]`, monotone, which is the defect
    this audit exists to find.

    It also fixes a misclassification in the other direction. When the
    re-wrapped source is a CALL (`chains([...], qv)`), the comprehension is not
    constructing a word at all -- it is passing one through -- so the site is
    not `SELF_BUILT`.
    """
    if not isinstance(node, (ast.ListComp, ast.GeneratorExp)):
        return None
    if not isinstance(node.elt, (ast.Tuple, ast.List)) or not node.elt.elts:
        return None
    last = node.elt.elts[-1]
    if not isinstance(last, ast.Name):
        return None
    if len(node.generators) != 1:
        return None
    tgt = node.generators[0].target
    bound = ({e.id for e in tgt.elts if isinstance(e, ast.Name)}
             if isinstance(tgt, (ast.Tuple, ast.List))
             else ({tgt.id} if isinstance(tgt, ast.Name) else set()))
    if last.id not in bound:
        return None
    return node.generators[0].iter


def _literal_gen_sequence(node, binds=None, depth=0):
    """Recover the generator sequence from a word expression, or None.

    Handles the shapes that actually occur: a list display of tuple literals; a
    `+` concatenation of comprehensions whose element is a tuple literal (the
    `compute_tau_M_nucleon_H3` shape, `[(c,d,0) for ...] + [(c,d,1) for ...]`);
    and a re-wrapping comprehension, resolved through to its source.

    A comprehension contributes its generator ONCE, not once per iteration.
    That is enough for monotonicity: repeating a value cannot turn a
    non-decreasing sequence into a decreasing one, or the reverse.
    """
    if depth > 6:
        return None
    binds = binds or {}
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        left = _literal_gen_sequence(node.left, binds, depth + 1)
        right = _literal_gen_sequence(node.right, binds, depth + 1)
        if left is None or right is None:
            return None
        return left + right
    if isinstance(node, ast.Name):
        vals = binds.get(node.id)
        if not vals:
            return None
        return _literal_gen_sequence(vals[-1], binds, depth + 1)
    if isinstance(node, (ast.ListComp, ast.GeneratorExp)):
        src = _rewrap_source(node)
        if src is not None:
            return _literal_gen_sequence(src, binds, depth + 1)
        g = _gen_index(node.elt)
        return None if g is None else [g]
    if isinstance(node, (ast.List, ast.Tuple)):
        out = []
        for e in node.elts:
            if isinstance(e, ast.Starred):
                return None
            g = _gen_index(e)
            if g is None:
                return None
            out.append(g)
        return out or None
    return None


def _is_built(node, depth=0):
    """True when the expression CONSTRUCTS a word in place.

    A re-wrapping comprehension is resolved through to its source rather than
    counted as construction: `[(mpf(c), mpf(d), g) for c, d, g in chain]` builds
    nothing, it coerces. Whether that site is self-built is a property of
    `chain`, not of the coercion.
    """
    if depth > 6:
        return False
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        return _is_built(node.left, depth + 1) or _is_built(node.right, depth + 1)
    if isinstance(node, (ast.ListComp, ast.GeneratorExp)):
        src = _rewrap_source(node)
        if src is not None:
            return _is_built(src, depth + 1)
        return isinstance(node.elt, (ast.Tuple, ast.List))
    if isinstance(node, (ast.List, ast.Tuple)):
        return any(isinstance(e, (ast.Tuple, ast.List)) for e in node.elts)
    return False


def _from_canonical(node):
    if isinstance(node, ast.Call):
        f = node.func
        name = f.id if isinstance(f, ast.Name) else (
            f.attr if isinstance(f, ast.Attribute) else None)
        return name in CANONICAL_EMITTERS
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        return _from_canonical(node.left) or _from_canonical(node.right)
    return False


def _bindings(scope):
    """name -> list of assigned expressions, within one scope (no nesting)."""
    out: dict[str, list] = {}
    nested = {n for s in _scopes(scope) if s is not scope for n in ast.walk(s)}
    for n in ast.walk(scope):
        if n in nested and scope is not n:
            continue
        if isinstance(n, ast.Assign):
            for t in n.targets:
                if isinstance(t, ast.Name):
                    out.setdefault(t.id, []).append(n.value)
        elif isinstance(n, (ast.AnnAssign, ast.AugAssign)) and \
                isinstance(n.target, ast.Name) and n.value is not None:
            out.setdefault(n.target.id, []).append(n.value)
    return out


def _classify_expr(node, binds, params, seen=None):
    """(verdict, gen_sequence_or_None) for ONE expression.

    Resolves through two kinds of indirection before judging: a short chain of
    local name bindings, and a re-wrapping comprehension (see
    `_rewrap_source`). Both are the difference between reporting where a word
    is COERCED and reporting where it is BUILT.

    A name with SEVERAL bindings is judged over all of them (see `_classify`),
    not over whichever came last.
    """
    seen = set() if seen is None else seen
    for _ in range(8):
        rew = _rewrap_source(node)
        if rew is not None:                # a coercion: judge its source
            node = rew
            continue
        if _from_canonical(node):
            return "CANONICAL", None
        if _is_built(node):
            return "SELF_BUILT", _literal_gen_sequence(node, binds)
        if isinstance(node, ast.Name):
            if node.id in params:
                return "INHERITED", None
            if node.id in seen:
                break
            seen.add(node.id)
            vals = binds.get(node.id)
            if not vals:
                break
            if len(vals) > 1:
                return _combine(
                    [_classify_expr(v, binds, params, set(seen)) for v in vals])
            node = vals[0]
            continue
        break
    return "OTHER", None


def _combine(results):
    """Fold the verdicts of a name's several bindings into one.

    Why this exists, and it is the sharpest lesson this audit has produced:
    a "last assignment wins" reading is WRONG on the shape a correct fix takes.
    `compute_tau_M_nucleon_H3`, as repaired under the ruling (option B), is

        if intra_order == "borromean":
            word = atom_braid_word_3A(...)       # canonical -- and the DEFAULT
        else:
            word = [(mpf(c), mpf(d), 0) for ...] + [... 1 for ...]   # historical

    Reading only the last binding reports SELF_BUILT and flags a file that has
    just been correctly fixed -- a false positive that would send the next
    agent to re-fix it. Measured: this audit did exactly that, on `main`, hours
    after the fix landed.

    So a name bound both canonically and self-built is `MIXED`: it carries a
    canonical path, and the self-built one is a branch a reader must judge.
    It is reported and NOT flagged, because the defect this audit hunts is a
    producer with no canonical path at all.
    """
    verdicts = {v for v, _g in results}
    if verdicts == {"SELF_BUILT"}:
        gens = next((g for _v, g in results if g is not None), None)
        return "SELF_BUILT", gens
    if "CANONICAL" in verdicts and "SELF_BUILT" in verdicts:
        return "MIXED", None
    for pref in ("CANONICAL", "INHERITED", "SELF_BUILT"):
        if pref in verdicts:
            return pref, next((g for v, g in results if v == pref), None)
    return "OTHER", None


def _classify(arg, binds, params):
    """(verdict, gen_sequence_or_None) for a word argument."""
    return _classify_expr(arg, binds, params)


def audit():
    rows = []
    for path in _iter_py():
        try:
            tree = ast.parse(path.read_text(encoding="utf-8", errors="replace"))
        except (SyntaxError, ValueError):
            continue
        rel = str(path.relative_to(ROOT))
        for scope in _scopes(tree):
            binds = _bindings(scope)
            params = _params(scope)
            nested = {n for s in _scopes(scope) if s is not scope
                      for n in ast.walk(s)}
            for n in ast.walk(scope):
                if n in nested:
                    continue
                if not isinstance(n, ast.Call):
                    continue
                f = n.func
                name = f.id if isinstance(f, ast.Name) else (
                    f.attr if isinstance(f, ast.Attribute) else None)
                if name not in CHI_KERNELS or not n.args:
                    continue
                verdict, gens = _classify(n.args[0], binds, params)
                monotone = None
                if gens is not None:
                    monotone = all(a <= b for a, b in zip(gens, gens[1:]))
                rows.append({
                    "file": rel,
                    "line": n.lineno,
                    "kernel": name,
                    "scope": getattr(scope, "name", "<module>"),
                    "verdict": verdict,
                    "gen_sequence": gens,
                    "monotone_literal": bool(
                        verdict == "SELF_BUILT" and monotone is True),
                })
    return rows


# Shapes this audit MUST detect. Each is a real one that was missed by an
# earlier version of this very script or by a prior sweep, so a future
# narrowing that reports a clean corpus fails here first rather than being
# believed. Precedent: `cached_accessor_shape_audit.py --selftest`.
_SELFTEST = [
    ("direct literal generators -- the compute_tau_M_nucleon_H3 shape", """
def f(g0, g1):
    word = [(mpf(c), mpf(d), 0) for c, d in g0] + [(mpf(c), mpf(d), 1) for c, d in g1]
    return chi_all_lambda(word, 3)
""", "SELF_BUILT", True),
    ("RE-WRAPPED literals -- missed by the first version of this audit", """
def f(g0, g1):
    chain = [(c, d, 0) for c, d in g0] + [(c, d, 1) for c, d in g1]
    word = [(mpf(str(c)), mpf(str(d)), g) for c, d, g in chain]
    return chi_all_lambda(word, 3)
""", "SELF_BUILT", True),
    ("re-wrap of a CALL builds nothing -- must NOT be SELF_BUILT", """
def f(qv):
    w = chains(["u", "u", "d"], qv)
    return chi_all_lambda([(c, d, g) for c, d, g in w], 3)
""", "OTHER", False),
    ("the canonical emitter", """
def f(Z, N):
    return chi_all_lambda_any(atom_braid_word_3A(Z, N), 3 * (Z + N))
""", "CANONICAL", False),
    ("non-monotone literals are self-built but NOT the defect", """
def f(g0):
    word = [(mpf(c), mpf(d), 0) for c, d in g0] + [(mpf(c), mpf(d), 1) for c, d in g0] \\
         + [(mpf(c), mpf(d), 0) for c, d in g0]
    return chi_all_lambda(word, 3)
""", "SELF_BUILT", False),
    ("a parameter is the caller's business", """
def f(word):
    return chi_all_lambda(word, 3)
""", "INHERITED", False),
    ("a canonical default WITH a historical branch is MIXED, not a defect --\n"
     "          the repaired compute_tau_M_nucleon_H3 shape (option B)", """
def f(Z, N, intra_order):
    if intra_order == "borromean":
        word = atom_braid_word_3A(Z, N)
    else:
        word = [(mpf(c), mpf(d), 0) for c, d in g0] + [(mpf(c), mpf(d), 1) for c, d in g1]
    return chi_all_lambda_any(word, 3)
""", "MIXED", False),
]


def _selftest() -> int:
    bad = 0
    for label, src, want_verdict, want_flag in _SELFTEST:
        tree = ast.parse(src)
        got_v, got_f = None, None
        for scope in _scopes(tree):
            binds, params = _bindings(scope), _params(scope)
            for n in ast.walk(scope):
                if not (isinstance(n, ast.Call) and n.args):
                    continue
                f = n.func
                name = f.id if isinstance(f, ast.Name) else (
                    f.attr if isinstance(f, ast.Attribute) else None)
                if name not in CHI_KERNELS:
                    continue
                v, gens = _classify(n.args[0], binds, params)
                mono = gens is not None and all(
                    a <= b for a, b in zip(gens, gens[1:]))
                got_v, got_f = v, (v == "SELF_BUILT" and mono)
        ok = (got_v == want_verdict and got_f == want_flag)
        bad += 0 if ok else 1
        print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n"
              f"          verdict {got_v} (want {want_verdict}), "
              f"flagged {got_f} (want {want_flag})")
    print(f"\n  {len(_SELFTEST) - bad}/{len(_SELFTEST)} self-test shapes")
    return 1 if bad else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true",
                    help="check the detector against shapes it must catch")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 when any MONOTONE_LITERAL is found")
    args = ap.parse_args()

    if args.selftest:
        return _selftest()

    rows = audit()
    if args.json:
        print(json.dumps(rows, indent=2))
        return 0

    counts: dict[str, int] = {}
    for r in rows:
        counts[r["verdict"]] = counts.get(r["verdict"], 0) + 1
    flagged = [r for r in rows if r["monotone_literal"]]

    print(f"  chi-kernel call sites: {len(rows)}\n")
    for v in ("CANONICAL", "MIXED", "SELF_BUILT", "INHERITED", "OTHER"):
        print(f"    {v:<12} {counts.get(v, 0):>4}")

    print(f"\n  SELF_BUILT / MIXED sites "
          f"(the class three prior sweeps could not see):")
    for r in rows:
        if r["verdict"] not in ("SELF_BUILT", "MIXED"):
            continue
        seq = r["gen_sequence"]
        tag = ("  <-- MONOTONE LITERAL" if r["monotone_literal"]
               else ("  (has a canonical path too; branch for a reader)"
                     if r["verdict"] == "MIXED"
                     else ("" if seq is None else "  (non-monotone)")))
        shown = ("gens unrecoverable" if seq is None else f"gens {seq}")
        if r["verdict"] == "MIXED":
            shown = "MIXED"
        print(f"    {r['file']}:{r['line']}  {r['scope']}()  "
              f"[{r['kernel']}]  {shown}{tag}")

    print(f"\n  MONOTONE_LITERAL: {len(flagged)}")
    print("  A monotone self-built word IS the grouped (superseded) ordering.\n"
          "  That is a CANDIDATE, not a verdict: legitimate when the producer\n"
          "  deliberately tests a non-atom braid. A human reads these; the\n"
          "  point is that there are few enough to read.")
    return 1 if (args.strict and flagged) else 0


if __name__ == "__main__":
    raise SystemExit(main())
