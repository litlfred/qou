#!/usr/bin/env python3
"""Value-based convention-C detector — tests the ANSWER, not the source.

Every existing convention detector in this repo keys on how the Markov
parameter was *written*: `scripts/convention-c-producer-audit.py` shape-matches
assignment RHS forms, `scripts/lean-markov-convention-audit.py` regex-matches
three known Lean spellings.  Both are structurally blind to a spelling nobody
has thought of, and
`docs/audits/2026-08-15-detector-blindness-taxonomy.md` catalogues **thirteen**
distinct blind spellings — four of which were found *by* detectors written to
catch the previous blind spot.  The taxonomy is evidence that the shape-matching
strategy loses this race by construction: each new detector closes one spelling
and the next author invents another.

This one cannot be evaded by re-spelling, because it does not read the
spelling.  It walks every `computations/**/*.py` with `ast`, finds each binding
whose right-hand side is a closed arithmetic expression in exactly one free
variable, compiles that expression to a function, and **evaluates it** against
the four reference curves below at two independent sample points.  A site is
reported when it agrees with a reference at *both* points — one point is a
numeric coincidence, two is functional identity.

    z_C(x) = sqrt(x)/(x+1)      convention C, q-variable
    z_D(x) = x**3/(x**2+1)      convention D, q-variable   (canonical)
    z_C(x**2) = x/(x**2+1)      convention C, sqrt-variable disguise
    z_D(x**2) = x**6/(x**4+1)   convention D, sqrt-variable disguise

The sqrt-variable rows matter: the Tier-2 Lean migration that replaced
`Real.sqrt` with a generic `markovZ (u : R)` did **not** change the convention.
It removed the square root, which was its stated goal, and left C harder to see
(`docs/audits/2026-08-26-convention-c-in-lean-and-the-markovz-overload.md`).

**A `-sqrtvar` verdict is a CANDIDATE, not a finding, and the report says so.**
`x/(x**2+1)` is `z_C` when `x` is the square root of q and is `1/[2]_q` -- a
different, convention-neutral quantity -- when `x` IS q.  Nothing in the
expression distinguishes the two; only what the variable MEANS does.  The
report therefore prints the variable name and triages on it (`s`, `u`, `t`,
`v`, `sq`, `qh`, `q_half`, `sqq`, `qhalf`, `rq` read as square-root variables;
`q`, `q0`, `_q` read as q itself), and an unrecognised name is reported
`unknown` rather than guessed.  Do not quote a `-sqrtvar` count as a
convention-C count without resolving the variables.

NO FLOAT64.  All arithmetic is `mpmath.mpf` at 60 dps, per AGENTS.md
§"PROBES ARE NOT EXEMPT" — a float64 evaluation resolves to ~1e-16 no matter
what is true, which for a detector means it cannot distinguish `z_C` from a
near-miss and would report agreement as a fact about the arithmetic.

COMPARISON SITES, AND WHY THE COUNT ALONE MISLEADS (bean `qou-ztee`).  Because
this audit reads neither names nor comments, it cannot tell a producer computing
at the wrong convention (a defect) from a probe binding `z_C` **beside** `z_D` in
order to compare them (the subject).  Both are confirmed convention-C bindings
and both were counted identically.  As the C surface drains, the census therefore
converges to a floor consisting entirely of the second kind, at which point the
report reads "N confirmed, exit 1" with every entry deliberate — and the obvious
next move, "drain the last N", deletes measurements.  Two things address that,
and the difference between them is the point:

  * **co-binding is a HINT.**  A confirmed-C site with a convention-D binding in
    the same enclosing scope is reported `[co-bound with z_D]`.  It is a
    value-level signal — no name, no comment — and it is the shape a comparison
    has.  It carries **no exemption power**, deliberately: an author could game
    it by adding a throwaway `z_D` beside the site.
  * **the ledger DECIDES.**  `docs/audits/convention-c-comparison-ledger.json`
    holds adjudicated sites, keyed on path + target + a hash of the source line.
    An entry there, and only an entry there, stops a site blocking.  It cannot
    be self-granted: it lives outside the scanned tree, must be committed
    separately, and expires the moment the site's source line changes.

Exit is 1 while any confirmed-C site is unadjudicated, so the gate can actually
reach green once the surface is drained-or-adjudicated, rather than staying red
forever and training its readers to ignore it.

  python3 scripts/convention-c-value-audit.py            # C sites only
  python3 scripts/convention-c-value-audit.py --all      # C and D
  python3 scripts/convention-c-value-audit.py --selftest
  python3 scripts/convention-c-value-audit.py --propose-ledger   # stubs to adjudicate
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import pathlib
import sys

from mpmath import mp

mp.dps = 60

#: Two independent sample points.  q0 is the substrate anchor (proton pin) so a
#: hit is reported at the value the corpus actually evaluates at; q1 is a plain
#: second point with no special status, present only to turn "agrees here" into
#: "is the same function".  Both are > 1 so `q - 1/q > 0` and no reference curve
#: is near a pole.
_Q0 = mp.mpf("1.1099785827513808")
_Q1 = mp.mpf("1.7")

_REFS = {
    "C": lambda x: mp.sqrt(x) / (x + 1),
    "D": lambda x: x ** 3 / (x ** 2 + 1),
    "C-sqrtvar": lambda x: x / (x ** 2 + 1),
    "D-sqrtvar": lambda x: x ** 6 / (x ** 4 + 1),
}

#: Names a single-argument call may carry and still be arithmetic we can
#: evaluate.  `mpf`/`Rational`/`Fraction` are casts; `sqrt` is the one function
#: that actually appears in a Markov-parameter spelling.
_CALLS = {
    "sqrt": mp.sqrt,
    "mpf": lambda v: v,
    "mpmathify": lambda v: v,
    "Rational": lambda v: v,
    "Fraction": lambda v: v,
    "Decimal": lambda v: v,
}

_SKIP_DIRS = {".git", ".lake", "__pycache__", "_deprecated", "fsh-guts", "node_modules"}

#: Variable names that conventionally denote sqrt(q) in this corpus, and those
#: that denote q itself.  Used only to triage a `-sqrtvar` match; an unlisted
#: name is reported `unknown`, never assumed.
#  FALLBACK ONLY as of 2026-08-30 (qou-t9r1). The primary route is
#  `_sqrt_bindings`, which resolves a name AT ITS BINDING in the file being
#  scanned. This list now covers exactly what binding-site resolution CANNOT
#  reach:
#
#    * FUNCTION PARAMETERS. `def z_C_s(ss): return ss / (ss**2 + 1)` has no
#      binding site — the parameter's meaning is fixed by the CALLER, not the
#      definition. Resolving it properly needs call-site analysis, which is a
#      strictly larger job and is not attempted here. `ss` is listed for this
#      reason and is the worked example.
#    * names bound in another module and imported.
#
#  Everything else should resolve at its binding; if a new sqrt-variable lands
#  in UNRESOLVED and IS assigned in-file, that is a resolver gap to fix rather
#  than a name to add here.
_SQRT_VARS = {"s", "u", "t", "v", "sq", "sqq", "qh", "qhalf", "q_half", "rq",
              "sqrt_q", "qsqrt", "shalf", "ss"}
_Q_VARS = {"q", "q0", "_q", "q_0", "qq", "Q", "Q0"}

#: path -> names bound to sqrt(q) in that file, filled during the scan.
_SQRT_BINDINGS_BY_PATH: dict = {}


def _sqrt_bindings(text: str, tree: "ast.AST") -> set:
    """Names bound to sqrt(q) IN THIS FILE, resolved at the binding site.

    The name list below is a fallback, not the primary route: it is the same
    brittleness this audit exists to avoid, and it demonstrably hid sites --
    `_s` and `ss` sat in UNRESOLVED, which is invisible in BOTH directions
    (not blocking, so a drain reads as finished; not adjudicable, because the
    ledger matcher only reaches resolved rows).

    Two binding shapes are recognised:

      X = <anything>.sqrt(<q-var>)      AST-visible
      X = <anything>.symbols(...)  # ... sqrt ...

    The second is comment-keyed because a sympy symbol carries no arithmetic
    the AST can inspect -- `_s = sp.symbols("s", positive=True)  # s = sqrt(q)`
    is the real case, and the comment is the only statement of intent. That is
    weaker evidence than the first shape and is deliberately limited to lines
    whose comment actually mentions a square root.
    """
    import ast as _ast
    names, lines = set(), text.splitlines()
    for node in _ast.walk(tree):
        if not isinstance(node, _ast.Assign) or len(node.targets) != 1:
            continue
        tgt = node.targets[0]
        if not isinstance(tgt, _ast.Name):
            continue
        v = node.value
        if isinstance(v, _ast.Call) and isinstance(v.func, _ast.Attribute):
            if v.func.attr == "sqrt" and v.args:
                a = v.args[0]
                if isinstance(a, _ast.Name) and a.id in _Q_VARS:
                    names.add(tgt.id); continue
            if v.func.attr in ("symbols", "Symbol"):
                ln = lines[node.lineno - 1] if node.lineno <= len(lines) else ""
                cmt = ln.split("#", 1)[1].lower() if "#" in ln else ""
                if "sqrt" in cmt or "\u221a" in cmt:
                    names.add(tgt.id)
    return names


def _var_kind(var: str, sqrt_names: set = frozenset()) -> str:
    if var in sqrt_names:          # resolved AT ITS BINDING in this file
        return "sqrt(q)"
    if var in _SQRT_VARS:          # fallback: corpus-wide conventional names
        return "sqrt(q)"
    if var in _Q_VARS:
        return "q"
    return "unknown"


#: Adjudicated comparison sites — the ONLY thing that can stop a confirmed C
#: binding from blocking.  See `_load_ledger` for why it is a committed file
#: rather than a source-level annotation.
_LEDGER = pathlib.Path("docs/audits/convention-c-comparison-ledger.json")


def _site_hash(src: str) -> str:
    """12 hex of sha256 over the site's source line, whitespace-normalised.

    Keyed on the SOURCE rather than the line number so an adjudication survives
    the line moving, and expires the moment the line's content changes.
    """
    return hashlib.sha256(" ".join(src.split()).encode()).hexdigest()[:12]


def _scope_of(tree: ast.AST) -> dict:
    """Map each line to its innermost enclosing `def`/`class`, else `<module>`.

    Used for the co-binding signal only.  File-level would over-credit: a large
    producer could bind C in one function and D in an unrelated other, and read
    as a comparison when it is not.
    """
    spans = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            end = getattr(node, "end_lineno", None) or node.lineno
            spans.append((node.lineno, end, node.name))
    spans.sort(key=lambda s: s[1] - s[0])          # innermost (narrowest) first

    def lookup(line: int) -> str:
        for start, end, name in spans:
            if start <= line <= end:
                return name
        return "<module>"
    return lookup


def _load_ledger(path: pathlib.Path) -> dict:
    """Adjudicated comparison sites, keyed `(path, target, source-hash)`.

    WHY A COMMITTED FILE RATHER THAN A SOURCE ANNOTATION.  A `# comparison only`
    comment or a `z_C`-style name would be an exemption an author grants
    themselves, in the file being audited — which is the evasion surface this
    detector exists to close, reintroduced one level up.  A ledger entry cannot
    be granted that way: it lives outside the scanned tree, it has to be
    committed as a separate deliberate act, and because the key includes a hash
    of the site's own source line, editing that line expires the adjudication
    automatically.  Same shape as `docs/audits/lean-vacuity-review-ledger.json`,
    which carries agent verdicts a machine cannot reach for the same reason.
    """
    if not path.exists():
        return {}
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(f"  !! ledger unreadable ({exc}); treating every site as unadjudicated")
        return {}
    out = {}
    for e in doc.get("entries", []):
        out[(e.get("path"), e.get("target"), e.get("source_hash"))] = e
    return out


class _NotArithmetic(Exception):
    """The expression is not a closed arithmetic form we can evaluate."""


def _evaluate(node: ast.AST, var: str, x):
    """Evaluate `node` with the single free name `var` bound to `x`.

    Raises `_NotArithmetic` for anything outside the closed arithmetic
    fragment, which is the whole safety story: this never executes repo code,
    it re-implements a deliberately tiny expression language.
    """
    if isinstance(node, ast.Constant):
        if isinstance(node.value, bool) or not isinstance(node.value, (int, float)):
            raise _NotArithmetic
        # A float LITERAL in the source is fine to read -- it is the author's
        # written constant.  It is re-created as mpf so the ARITHMETIC below
        # never happens in float64.
        return mp.mpf(repr(node.value))
    if isinstance(node, ast.Name):
        if node.id != var:
            raise _NotArithmetic
        return x
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
        v = _evaluate(node.operand, var, x)
        return v if isinstance(node.op, ast.UAdd) else -v
    if isinstance(node, ast.BinOp):
        a = _evaluate(node.left, var, x)
        b = _evaluate(node.right, var, x)
        op = node.op
        if isinstance(op, ast.Add):
            return a + b
        if isinstance(op, ast.Sub):
            return a - b
        if isinstance(op, ast.Mult):
            return a * b
        if isinstance(op, ast.Div):
            if b == 0:
                raise _NotArithmetic
            return a / b
        if isinstance(op, ast.Pow):
            return a ** b
        raise _NotArithmetic
    if isinstance(node, ast.Call):
        fn = node.func
        name = fn.attr if isinstance(fn, ast.Attribute) else getattr(fn, "id", None)
        if name not in _CALLS or len(node.args) != 1 or node.keywords:
            raise _NotArithmetic
        # A cast whose argument is a plain string literal -- mpf("1.109...").
        arg = node.args[0]
        if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
            try:
                return mp.mpf(arg.value)
            except (ValueError, TypeError):
                raise _NotArithmetic
        return _CALLS[name](_evaluate(arg, var, x))
    raise _NotArithmetic


def _free_names(node: ast.AST) -> set[str]:
    """Names the expression reads as VALUES.

    A `Name` in callee position is not a free variable -- `sqrt(q)` reads one
    variable, not two.  Missing this made the detector blind to every spelling
    that calls a function, which is most of them.
    """
    callees = {c.func for c in ast.walk(node)
               if isinstance(c, ast.Call) and isinstance(c.func, ast.Name)}
    # An attribute BASE is not a free variable either -- `mp.mpf("nan")` reads
    # the module `mp`, not a quantity.  Counting it made every `mp.mpf(...)`
    # binding look like a one-variable expression, and combined with the NaN
    # hole below that produced four false positives on the first run.
    bases = {a.value for a in ast.walk(node)
             if isinstance(a, ast.Attribute) and isinstance(a.value, ast.Name)}
    return {n.id for n in ast.walk(node)
            if isinstance(n, ast.Name) and n not in callees and n not in bases}


def _classify(node: ast.AST) -> str | None:
    """Return the reference curve `node` IS, or None.

    Agreement is required at BOTH sample points.  The tolerance is 1e-40, far
    below any real near-miss and far above mpf round-off at 60 dps, so it
    separates "the same function" from "a different function that happens to
    pass nearby".
    """
    names = _free_names(node)
    if len(names) != 1:
        return None
    (var,) = names
    for label, ref in _REFS.items():
        try:
            vals = [_evaluate(node, var, pt) for pt in (_Q0, _Q1)]
            # NaN and infinity compare out of every inequality, so `abs(got -
            # ref) > tol` is FALSE for them and a NaN binding "agrees" with
            # whatever it is tested against.  `mp.mpf("nan")` appears all over
            # this corpus as a sentinel; without this guard it is reported as
            # convention C.  Reject non-finite before comparing anything.
            if not all(mp.isfinite(v) for v in vals):
                raise _NotArithmetic
            # A constant is not a Markov parameter.  Requiring the expression
            # to MOVE between the two sample points is what makes agreement at
            # both points mean "same function" rather than "same number".
            if vals[0] == vals[1]:
                raise _NotArithmetic
            for got, pt in zip(vals, (_Q0, _Q1)):
                if abs(got - ref(pt)) > mp.mpf("1e-40"):
                    raise _NotArithmetic
        except (_NotArithmetic, ZeroDivisionError, ValueError, TypeError,
                OverflowError, ArithmeticError):
            continue
        return label
    return None


def scan(root: pathlib.Path):
    """Yield (path, lineno, target, label, source, variable, scope) per site."""
    for path in sorted(root.rglob("*.py")):
        if any(part in _SKIP_DIRS for part in path.parts):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
            tree = ast.parse(text)
        except (SyntaxError, OSError, UnicodeDecodeError):
            continue
        lines = text.splitlines()
        scope_at = _scope_of(tree)
        _SQRT_BINDINGS_BY_PATH[str(path)] = _sqrt_bindings(text, tree)
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                value, targets = node.value, node.targets
            elif isinstance(node, (ast.AnnAssign, ast.AugAssign)):
                value, targets = node.value, [node.target]
            elif isinstance(node, ast.Return) and node.value is not None:
                value, targets = node.value, []
            else:
                continue
            if value is None:
                continue
            label = _classify(value)
            if label is None:
                continue
            names = [t.id for t in targets if isinstance(t, ast.Name)] or ["<return>"]
            src = lines[node.lineno - 1].strip() if node.lineno <= len(lines) else ""
            (var,) = _free_names(value)
            yield (path, node.lineno, names[0], label, src, var,
                   scope_at(node.lineno))


_SELFTEST = '''
z_nan        = mp.mpf("nan")
z_const      = 7 / (3 + 1)
z_plain      = sqrt(q) / (q + 1)
z_recip      = 1 / (sqrt(q) + 1 / sqrt(q))
z_halfpow    = q ** 0.5 / (q + 1)
z_sqrtvar    = u / (u ** 2 + 1)
z_returned   = 0
z_d          = q ** 3 / (q ** 2 + 1)
z_d_sqrtvar  = s ** 6 / (s ** 4 + 1)
not_markov   = q / (q + 1)
two_vars     = a / (b + 1)
def f(q):
    return sqrt(q) * (q + 1) ** -1

def compares(q):
    z_c_here = sqrt(q) / (q + 1)
    z_d_here = q ** 3 / (q ** 2 + 1)
    return z_c_here, z_d_here

def c_only(q):
    z_c_alone = sqrt(q) / (q + 1)
    return z_c_alone
'''


def _selftest() -> int:
    """Nine spellings, four of which no shape-matcher in this repo catches.

    `z_recip` and `z_halfpow` are the same NUMBER as `z_plain` and
    structurally nothing like it; `z_sqrtvar` is the Tier-2 disguise; the
    `return` form is the spelling that was invisible to the producer audit
    until 2026-08-16 because it keys on assignment targets.  `not_markov` is
    the control: `q/(q+1)` is one character from `sqrt(q)/(q+1)` and is a
    different function, so a detector that passes it is over-matching.
    """
    want = {
        "z_plain": "C", "z_recip": "C", "z_halfpow": "C", "z_sqrtvar": "C-sqrtvar",
        "<return>": "C", "z_d": "D", "z_d_sqrtvar": "D-sqrtvar",
        "z_c_here": "C", "z_d_here": "D", "z_c_alone": "C",
    }
    tmp = pathlib.Path("/tmp/_conv_selftest")
    tmp.mkdir(exist_ok=True)
    (tmp / "case.py").write_text(_SELFTEST)
    rows = list(scan(tmp))
    (tmp / "case.py").unlink()
    tmp.rmdir()
    got = {r[2]: r[3] for r in rows}
    scopes = {r[2]: r[6] for r in rows}
    srcs = {r[2]: r[4] for r in rows}
    ok = True
    for target, label in want.items():
        if got.get(target) != label:
            print(f"  FAIL  {target}: want {label}, got {got.get(target)}")
            ok = False
    for spurious in ("not_markov", "two_vars", "z_nan", "z_const"):
        if spurious in got:
            print(f"  FAIL  {spurious} matched {got[spurious]} -- over-matching")
            ok = False

    # Scope, and the co-binding signal built on it.  `compares` binds C and D
    # together and must read as co-bound; `c_only` binds C in its own scope and
    # must NOT, even though the same FILE contains D bindings elsewhere.  A
    # file-level signal would credit `c_only` wrongly, which is the whole reason
    # `_scope_of` exists.
    d_scopes = {(r[0], r[6]) for r in rows if r[3].startswith("D")}
    for target, want_scope, want_cobound in (("z_c_here", "compares", True),
                                             ("z_c_alone", "c_only", False),
                                             ("z_plain", "<module>", True)):
        if scopes.get(target) != want_scope:
            print(f"  FAIL  {target}: scope want {want_scope}, got {scopes.get(target)}")
            ok = False
        row = next((r for r in rows if r[2] == target), None)
        cob = row is not None and (row[0], row[6]) in d_scopes
        if cob != want_cobound:
            print(f"  FAIL  {target}: co-bound want {want_cobound}, got {cob}")
            ok = False

    # The ledger key must expire when the site's source changes.  This is the
    # property that stops an adjudication from being something an author grants
    # themselves by editing the file: same text -> same key, any edit -> miss.
    src = srcs.get("z_c_here", "")
    if _site_hash(src) != _site_hash("   " + " ".join(src.split()) + "  "):
        print("  FAIL  _site_hash is not whitespace-stable")
        ok = False
    if _site_hash(src) == _site_hash(src.replace("sqrt(q)", "sqrt(q) * 1")):
        print("  FAIL  _site_hash did not change when the source changed")
        ok = False

    print("  selftest PASS" if ok else "  selftest FAIL")
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--all", action="store_true", help="report convention-D sites too")
    ap.add_argument("--root", default="computations", help="tree to scan")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--ledger", default=str(_LEDGER),
                    help="adjudicated-comparison ledger (JSON)")
    ap.add_argument("--propose-ledger", action="store_true",
                    help="print ledger stubs for the co-bound sites, for an "
                         "adjudicator to edit and commit; does not write")
    args = ap.parse_args()
    if args.selftest:
        return _selftest()

    rows = list(scan(pathlib.Path(args.root)))
    c_rows = [r for r in rows if r[3].startswith("C")]
    d_rows = [r for r in rows if r[3].startswith("D")]

    # Split the C rows by whether the variable resolves.  A `-sqrtvar` shape on
    # a q-variable is `1/[2]_q`, NOT convention C, and must not be counted as
    # one -- see the module docstring.
    confirmed, notc, unresolved = [], [], []
    for r in c_rows:
        label, var = r[3], r[5]
        kind = _var_kind(var, _SQRT_BINDINGS_BY_PATH.get(str(r[0]), frozenset()))
        if label == "C":
            confirmed.append(r)
        elif kind == "sqrt(q)":
            confirmed.append(r)
        elif kind == "q":
            notc.append(r)
        else:
            unresolved.append(r)

    # Co-binding: does a convention-D binding sit in the SAME enclosing scope?
    # That is a value-level signal — it reads no name and no comment — and it is
    # the shape a comparison has: both parameters bound together so they can be
    # set against each other.  It is a HINT ONLY and deliberately carries no
    # exemption power, because it CAN be gamed: an author wanting to silence a
    # site could add a throwaway `z_D = q**3/(q**2+1)` beside it.  Only the
    # ledger, which lives outside the scanned tree, can stop a site blocking.
    d_scopes = {(r[0], r[6]) for r in d_rows}
    ledger = _load_ledger(pathlib.Path(args.ledger))
    seen_keys = set()

    adjudicated, blocking = [], []
    for r in confirmed:
        key = (str(r[0]), r[2], _site_hash(r[4]))
        seen_keys.add(key)
        (adjudicated if key in ledger else blocking).append(r)
    stale = [k for k in ledger if k not in seen_keys]

    def cobound(r) -> bool:
        return (r[0], r[6]) in d_scopes

    print("VALUE-BASED convention audit — the expression is EVALUATED, not matched.")
    print(f"  root: {args.root}")
    print(f"  convention-C bindings (confirmed): {len(confirmed)}")
    print(f"      of which co-bound with z_D in the same scope: "
          f"{sum(1 for r in confirmed if cobound(r))}  (hint only — not an exemption)")
    print(f"      of which adjudicated in the ledger: {len(adjudicated)}")
    print(f"      BLOCKING (confirmed, unadjudicated): {len(blocking)}")
    print(f"  sqrtvar shape on a q-variable = 1/[2]_q, NOT C: {len(notc)}")
    print(f"  sqrtvar shape, variable unresolved (needs an eye): {len(unresolved)}")
    print(f"  convention-D bindings: {len(d_rows)}")
    if stale:
        print(f"\n  !! {len(stale)} ledger entr(y/ies) match nothing — the site "
              f"moved, changed or went away.  Non-blocking; prune them.")
        for p, t, h in stale:
            print(f"     stale: {p}  {t}  {h}")

    # The co-bound marker is printed ONLY for the confirmed-C groups.  A NOT-C
    # or UNRESOLVED row sitting beside a D binding is not evidence of anything —
    # `1/[2]_q` on a q-variable is convention-neutral — and marking it made the
    # visible markers (45) disagree with the summary count (44, over confirmed
    # rows), which is the kind of small discrepancy that costs a report its
    # credibility faster than the missing signal would have.
    for title, group, mark_cobound in (
            ("BLOCKING — confirmed convention C, unadjudicated", blocking, True),
            ("ADJUDICATED as comparisons (ledger)", adjudicated, True),
            ("UNRESOLVED — variable name not recognised", unresolved, False),
            ("NOT C — 1/[2]_q on a q-variable", notc, False)):
        if not group:
            continue
        print(f"\n  === {title} ({len(group)}) ===")
        for row in group:
            path, line, target, label, src, var, scope = row
            mark = "  [co-bound with z_D]" if (mark_cobound and cobound(row)) else ""
            print(f"  [{label:10s} var={var:8s}] {path}:{line}  scope={scope}{mark}")
            print(f"      {target} = {src[:100]}")
    if args.all and d_rows:
        print(f"\n  === convention D ({len(d_rows)}) ===")
        for path, line, target, label, src, var, scope in d_rows:
            print(f"  [{label:10s} var={var:8s}] {path}:{line}   {target}")

    if args.propose_ledger:
        stubs = [{
            "path": str(r[0]), "target": r[2], "source_hash": _site_hash(r[4]),
            "line_when_adjudicated": r[1], "scope": r[6],
            "source": r[4][:120],
            "verdict": "comparison",
            "rationale": "FILL IN: why this site binds z_C deliberately.",
            "adjudicated_by": "FILL IN", "date": "FILL IN (YYYY-MM-DD)",
        } for r in blocking if cobound(r)]
        print(f"\n  === ledger stubs for the {len(stubs)} co-bound blocking site(s) ===")
        print("  Edit the rationale/attribution and commit into the ledger's "
              "`entries`.  Co-binding is why these are PROPOSED; it is not why "
              "they would be exempt — the commit is.")
        print(json.dumps(stubs, indent=2))

    return 1 if blocking else 0


if __name__ == "__main__":
    sys.exit(main())
