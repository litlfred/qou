#!/usr/bin/env python3
"""Assertions whose TOLERANCE is below the CANCELLATION floor of the verdict.

THE VERDICT IS ALWAYS COMPUTED IN FLOAT64. This is the fact the whole audit
turns on, and it is not a call-site property:

    # qou_substrate/witness.py:830, Assertion.passed
    return abs(float(self.computed) - float(self.expected)) <= float(self.tolerance)

So how a producer PASSES a value -- mpf, str, float -- changes what the witness
RECORDS but never changes the verdict. Every `passed` in this corpus is a
float64 subtraction.

WHERE THAT BITES, AND WHERE IT DOES NOT
---------------------------------------
Not where you would guess, and not where this file guessed twice. Measured:

  * `float(mpf("1e-45"))` is `1e-45`, EXACTLY. IEEE double carries 16
    significant digits at ANY exponent down to ~1e-308. A tiny residual
    survives the cast intact.
  * So `computed=float(delta), expected=0.0, tolerance=1e-40` WORKS: it fails
    at delta=1e-30 and passes at delta=1e-45, which is what it advertises.
    There is no cancellation, because subtracting exact 0 removes nothing.
  * `computed = 1 + 1e-30` against `expected = 1.0` gives
    `float(c) - 1.0 == 0.0`. The assertion passes at tolerance 1e-40 VACUOUSLY,
    and would pass identically on a value that missed by 1e-20.

The defect is CATASTROPHIC CANCELLATION between two same-scale numbers, so the
floor is RELATIVE to the compared magnitude:

    reachable resolution ~ 2.22e-16 * |expected|

A tolerance below that cannot be reached by the verdict at that scale. A
tolerance against `expected == 0` is not flagged: nothing cancels.

THE FIX AT A CALL SITE is not to drop the cast -- that does not touch the
verdict. It is to SUBTRACT IN THE PRODUCER'S OWN ARITHMETIC and assert the
residual against exactly 0:

    # vacuous: cancels in float64 at ~1e-16 regardless of how `norm` is passed
    add_assertion("normalised", computed=norm, expected=mp.mpf(1), tolerance=1e-25)
    # meaningful: float64 renders a tiny mpf faithfully at any exponent
    add_assertion("normalised", computed=abs(norm - 1), expected=0, tolerance=1e-25)

TWO CORRECTIONS TO THIS FILE, IN ONE SESSION, THE SECOND INVERTING THE FIRST
---------------------------------------------------------------------------
Recorded because the errors are more instructive than the detector.

  1. FIRST VERSION flagged any `float()` cast under a sub-2.2e-16 tolerance, on
     the argument that "float64 resolves ~2.2e-16 relative". That argument is
     about a quantity OF ORDER 1. A residual is not of order 1 -- that is what
     makes it a residual -- so the argument did not apply to the very case it
     was aimed at.
  2. SECOND VERSION split on `expected == 0` and called that bucket "the real
     defect", gating on it, with the nonzero bucket advisory. Measured, that is
     exactly BACKWARDS: `expected == 0` is the safe case and `expected != 0` is
     where cancellation lives.

Both were published before being measured. The measurement that settles it is
four lines of mpmath and should have come first.

WHAT THIS AUDIT STILL CANNOT SEE. A residual asserted against 0 that was itself
computed in float64 from O(1) inputs is noise at ~1e-16 and no tolerance below
that is reachable -- but deciding it needs the residual's provenance, not its
call site. That is `mpf_float_source_audit`'s question, not this one's.

METHOD. AST. Pair each `add_assertion`'s `expected` with its `tolerance`; flag
when both are numeric literals, `expected != 0`, and
`tolerance < FLOAT64_EPS * |expected|`.

Exit 0 when clean, 1 otherwise.

-- Ref: [manuscript] docs/audits/2026-08-15-detector-blindness-taxonomy.md
"""
from __future__ import annotations

import ast
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {"_deprecated", "__pycache__", "data", "node_modules"}

#: IEEE-754 double machine epsilon. The RELATIVE resolution; multiply by the
#: compared magnitude to get the absolute cancellation floor at that scale.
FLOAT64_EPS = 2.220446049250313e-16

#: Serializers that render a value to N SIGNIFICANT DIGITS. Their second
#: argument is N, and it imposes a SECOND floor on the comparison -- coarser
#: than float64 whenever N < 17. Measured: mp.nstr keeps a residual's exponent
#: (nstr(1e-40, 10) == "1.0e-40"), so like float64 it costs nothing against an
#: expected of 0; what it caps is the comparison of two SAME-SCALE values, at
#: 10^-(N-1) relative instead of 2.22e-16.
_DIGIT_SERIALIZERS = {"nstr", "N", "n"}

#: Constructors that merely re-type a literal. Their argument is the value.
_NUMERIC_CTORS = {"mpf", "mpmathify", "float", "int", "Decimal", "Fraction",
                  "Integer", "Float", "Rational", "S"}


def _numeric(node: ast.AST):
    """The literal value if this is a plain number, else None.

    Deliberately does NOT evaluate names or arithmetic: a bound that is not a
    literal is not something this audit can judge, and guessing is the
    false-positive mechanism the taxonomy keeps recording.
    """
    if isinstance(node, ast.Constant) and isinstance(node.value, bool):
        return None
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return float(node.value)
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        try:
            return float(node.value)
        except ValueError:
            return None
    if (isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub)):
        inner = _numeric(node.operand)
        return None if inner is None else -inner
    # A literal wrapped in a numeric constructor -- `mp.mpf(1)`, `mpf("1e-25")`,
    # `sp.Integer(-1)`, `Fraction(1)`. This is NOT pedantry: it is the exact
    # shape a first attempt at fixing one of these sites produces, so without it
    # the audit goes quiet on its own bad advice. Measured: `expected=mp.mpf(1)`
    # in atom_mass_full_hecke_qdeformed was invisible until this was added, and
    # it is as vacuous as the `expected=1.0` it replaced -- the verdict casts to
    # float64 either way.
    if isinstance(node, ast.Call) and len(node.args) == 1 and not node.keywords:
        fn = node.func
        nm = fn.attr if isinstance(fn, ast.Attribute) else (
            fn.id if isinstance(fn, ast.Name) else None)
        if nm in _NUMERIC_CTORS:
            return _numeric(node.args[0])
    return None


def _serialization_digits(node: ast.AST):
    """N, if this expression is serialized to N significant digits.

    `mp.nstr(x, 10)` under a 1e-20 bound is unreachable BEFORE float64 enters --
    a 10-digit string cannot express the difference. Found while draining, in
    four sites the float64-only criterion flagged for the wrong reason and two
    it would have under-corrected: `qbeta_ohtsuki_sixone_kappa_series` compares
    `mp.nstr(det, 10)` at 1e-20, where nstr is the binding floor by 11 orders.
    """
    best = None
    for sub in ast.walk(node):
        if not isinstance(sub, ast.Call) or len(sub.args) < 2:
            continue
        fn = sub.func
        nm = fn.attr if isinstance(fn, ast.Attribute) else (
            fn.id if isinstance(fn, ast.Name) else None)
        if nm not in _DIGIT_SERIALIZERS:
            continue
        d = _numeric(sub.args[1])
        if d is not None and d >= 1:
            best = int(d) if best is None else min(best, int(d))
    return best


def scan_file(path: str) -> list[dict]:
    try:
        src = open(path, encoding="utf-8", errors="replace").read()
        tree = ast.parse(src)
    except (OSError, SyntaxError):
        return []
    lines = src.split("\n")
    out = []
    for node in ast.walk(tree):
        if not (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
                and node.func.attr == "add_assertion"):
            continue
        kw = {k.arg: k.value for k in node.keywords if k.arg}
        tol_node, exp_node = kw.get("tolerance"), kw.get("expected")
        if tol_node is None or exp_node is None:
            continue
        tol, exp = _numeric(tol_node), _numeric(exp_node)
        if tol is None or exp is None or tol <= 0:
            continue
        if exp == 0.0:
            continue                      # nothing cancels against exact zero
        f64_floor = FLOAT64_EPS * abs(exp)
        comp_node = kw.get("computed")
        digits = _serialization_digits(comp_node) if comp_node is not None else None
        ser_floor = (10.0 ** -(digits - 1)) * abs(exp) if digits else 0.0
        # The binding floor is the COARSER of the two -- whichever the comparison
        # hits first. Reported separately so a fix targets the right one.
        floor = max(f64_floor, ser_floor)
        binding = "serialization" if ser_floor > f64_floor else "float64"
        if tol >= floor:
            continue
        name = ""
        if node.args and isinstance(node.args[0], ast.Constant):
            name = str(node.args[0].value)[:60]
        # The `expected=` keyword's OWN line, not the call's. In a fluent builder
        # chain every chained Call node carries the lineno where the WHOLE chain
        # starts, so distinct assertions collapse onto one line -- AST-correct
        # and useless for finding the site.
        ln = exp_node.lineno
        out.append({
            "path": os.path.relpath(path, ROOT),
            "line": ln,
            "assertion": name,
            "tolerance": tol,
            "expected": exp,
            "floor": floor,
            "binding": binding,
            "digits": digits,
            "shortfall": floor / tol,
            "snippet": lines[ln - 1].strip()[:88] if ln - 1 < len(lines) else "",
        })
    return out


#: Cancellation at scale 1: floor 2.2e-16, tolerance 1e-30 -> unreachable.
_SELFTEST_FIRES = '''
w.add_assertion("a", computed=norm, expected=1.0, tolerance=1e-30)
w.add_assertion("b", computed=float(x), expected=60.0, tolerance="1e-25")
'''
#: Each of these must stay quiet, and each for a DIFFERENT reason.
#: nstr(x, 10) under 1e-20: the SERIALIZATION floor (1e-9 here) binds, not
#: float64 (2.2e-15). Must fire AND attribute correctly.
_SELFTEST_SERIAL = '''
w.add_assertion("i", computed=mp.nstr(d, 10), expected="7", tolerance="1e-20")
'''
_SELFTEST_QUIET = '''
w.add_assertion("c", computed=float(dev), expected=0.0, tolerance=1e-40)
w.add_assertion("d", computed=float(dev), expected=1.0, tolerance=1e-12)
w.add_assertion("e", computed=float(dev), expected=1.0, tolerance=0)
w.add_assertion("f", computed=flag, expected=True, tolerance=1e-30)
w.add_assertion("g", computed=x, expected=some_name, tolerance=1e-30)
'''
#: The constructor-wrapped shape, which a first-pass "fix" of one of these
#: sites produces. Must fire: mp.mpf(1) cancels in the verdict exactly as 1.0 does.
_SELFTEST_CTOR = '''
w.add_assertion("h", computed=norm, expected=mp.mpf(1), tolerance=mp.mpf("1e-25"))
'''


def _selftest() -> None:
    """A detector that cannot fire is not a detector, and one that fires on the
    safe case is worse. Pin both, including the `expected == 0` non-firing --
    that is the case a previous version of this file GATED on."""
    import tempfile
    cases = ((_SELFTEST_FIRES, 2, None), (_SELFTEST_CTOR, 1, None),
             (_SELFTEST_SERIAL, 1, "serialization"), (_SELFTEST_QUIET, 0, None))
    for src, want, binding in cases:
        with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
            f.write(src)
            tmp = f.name
        try:
            hits = scan_file(tmp)
            got = len(hits)
            assert got == want, f"selftest: expected {want} hit(s), got {got}"
            if binding:
                assert hits[0]["binding"] == binding, (
                    f"selftest: expected binding {binding}, got {hits[0]['binding']}")
        finally:
            os.unlink(tmp)


def main(argv: list[str] | None = None) -> int:
    _selftest()
    argv = list(sys.argv[1:] if argv is None else argv)
    findings = []
    if argv and argv[0] == "--files":
        for a in argv[1:]:
            if a.endswith(".py") and os.path.exists(a):
                findings.extend(scan_file(os.path.abspath(a)))
    else:
        for root, dirs, files in os.walk(ROOT):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
            for fn in sorted(files):
                if fn.endswith(".py"):
                    findings.extend(scan_file(os.path.join(root, fn)))
    findings.sort(key=lambda r: -r["shortfall"])

    print("=" * 78)
    print(" TOLERANCE BELOW THE CANCELLATION FLOOR — a bound the verdict cannot reach")
    print("=" * 78)
    print(f"  float64 machine epsilon   : {FLOAT64_EPS:.6e}  (RELATIVE)")
    print("  verdict path              : abs(float(c) - float(e)) <= float(t)")
    print("                              qou_substrate/witness.py:830 — always float64")
    print(f"  flagged assertions        : {len(findings)}")
    print(f"  files                     : {len({f['path'] for f in findings})}")
    print("  serialization floor       : 10^-(N-1) for mp.nstr(x, N) / sp.N(x, N)")
    print("  selftest                  : PASS (4 must-fire incl. mp.mpf(1)-wrapped")
    print("                              and nstr-bound,")
    print("                              5 must-stay-quiet incl. expected==0, which an")
    print("                              earlier version of this file GATED on)")
    if findings:
        print()
        print("  Sorted by shortfall = how many times below the reachable floor.")
        print("  Fix by asserting the RESIDUAL against 0, not the value against a target.")
        print()
        for f in findings:
            print(f"  {f['path']}:{f['line']}")
            print(f"      {f['assertion']}")
            print(f"      expected={f['expected']:g}  tol={f['tolerance']:g}  "
                  f"floor={f['floor']:.3e}  shortfall={f['shortfall']:.1e}x")
            print(f"      {f['snippet']}")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
