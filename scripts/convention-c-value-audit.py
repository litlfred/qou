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

  python3 scripts/convention-c-value-audit.py            # C sites only
  python3 scripts/convention-c-value-audit.py --all      # C and D
  python3 scripts/convention-c-value-audit.py --selftest
"""
from __future__ import annotations

import argparse
import ast
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

_SKIP_DIRS = {".git", ".lake", "__pycache__", "_deprecated", "node_modules"}

#: Variable names that conventionally denote sqrt(q) in this corpus, and those
#: that denote q itself.  Used only to triage a `-sqrtvar` match; an unlisted
#: name is reported `unknown`, never assumed.
_SQRT_VARS = {"s", "u", "t", "v", "sq", "sqq", "qh", "qhalf", "q_half", "rq",
              "sqrt_q", "qsqrt", "shalf"}
_Q_VARS = {"q", "q0", "_q", "q_0", "qq", "Q"}


def _var_kind(var: str) -> str:
    if var in _SQRT_VARS:
        return "sqrt(q)"
    if var in _Q_VARS:
        return "q"
    return "unknown"


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
    """Yield (path, lineno, target, label, source, variable) per classified site."""
    for path in sorted(root.rglob("*.py")):
        if any(part in _SKIP_DIRS for part in path.parts):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
            tree = ast.parse(text)
        except (SyntaxError, OSError, UnicodeDecodeError):
            continue
        lines = text.splitlines()
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
            yield path, node.lineno, names[0], label, src, var


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
    }
    tmp = pathlib.Path("/tmp/_conv_selftest")
    tmp.mkdir(exist_ok=True)
    (tmp / "case.py").write_text(_SELFTEST)
    got = {t: lab for _, _, t, lab, _, _ in scan(tmp)}
    (tmp / "case.py").unlink()
    tmp.rmdir()
    ok = True
    for target, label in want.items():
        if got.get(target) != label:
            print(f"  FAIL  {target}: want {label}, got {got.get(target)}")
            ok = False
    for spurious in ("not_markov", "two_vars", "z_nan", "z_const"):
        if spurious in got:
            print(f"  FAIL  {spurious} matched {got[spurious]} -- over-matching")
            ok = False
    print("  selftest PASS" if ok else "  selftest FAIL")
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--all", action="store_true", help="report convention-D sites too")
    ap.add_argument("--root", default="computations", help="tree to scan")
    ap.add_argument("--selftest", action="store_true")
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
        kind = _var_kind(var)
        if label == "C":
            confirmed.append(r)
        elif kind == "sqrt(q)":
            confirmed.append(r)
        elif kind == "q":
            notc.append(r)
        else:
            unresolved.append(r)

    print("VALUE-BASED convention audit — the expression is EVALUATED, not matched.")
    print(f"  root: {args.root}")
    print(f"  convention-C bindings (confirmed): {len(confirmed)}")
    print(f"  sqrtvar shape on a q-variable = 1/[2]_q, NOT C: {len(notc)}")
    print(f"  sqrtvar shape, variable unresolved (needs an eye): {len(unresolved)}")
    print(f"  convention-D bindings: {len(d_rows)}")
    for title, group in (("CONFIRMED convention C", confirmed),
                         ("UNRESOLVED — variable name not recognised", unresolved),
                         ("NOT C — 1/[2]_q on a q-variable", notc)):
        if not group:
            continue
        print(f"\n  === {title} ({len(group)}) ===")
        for path, line, target, label, src, var in group:
            print(f"  [{label:10s} var={var:8s}] {path}:{line}")
            print(f"      {target} = {src[:100]}")
    if args.all and d_rows:
        print(f"\n  === convention D ({len(d_rows)}) ===")
        for path, line, target, label, src, var in d_rows:
            print(f"  [{label:10s} var={var:8s}] {path}:{line}   {target}")
    return 1 if confirmed else 0


if __name__ == "__main__":
    sys.exit(main())
