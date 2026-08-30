#!/usr/bin/env python3
"""self_fulfilling_assertion_audit.py — find `add_assertion(name, X, X)`.

THE DEFECT.  `WitnessBuilder.add_assertion(name, computed, expected)` marks an
assertion `passed` when `computed == expected`.  Nothing stops the two arguments
being the SAME EXPRESSION, and when they are, the assertion is `x == x`: it is
tautologically true, it can never fail, and it renders in the witness as
`"passed": true` — which the QA pipeline reads as evidence.

This is the compute-side twin of the Lean rule AGENTS.md already states under
§"No trivial trues, no tautologies, no laundering": *"Tautological conclusions are
banned: `X = X` ... any proposition that is provable without using any hypothesis
about the mathematical objects in question."*  The same sentence applies verbatim
to a witness assertion, and nothing was checking for it.

WORKED CASE (why this was written).  `threerow_sign_crossing_probe` had

    w.add_assertion("D_sign_qlo", iso_rows["D"]["sign_qlo"], iso_rows["D"]["sign_qlo"])
    w.add_assertion("D_sign_q0",  iso_rows["D"]["sign_q0"],  iso_rows["D"]["sign_q0"])

Between convention C and convention D the deuteron object went from order-unity
(`F(q0) = -0.19496…`) to identically zero, and the sign it asserts went `+1 -> 0`
and `-1 -> 0`.  Committed: `1/1 True`, `-1/-1 True`.  Re-run: `0/0 True`, `0/0 True`.
The measured quantity inverted and the check still passed, because it compares the
value to itself.  Bean `qou-qdtk` / the state-2 records of
`docs/audits/2026-08-25-ylambda-threerow-frame-audit.md`.

TWO CLASSES, AND THEY ARE NOT EQUALLY BAD
------------------------------------------
  MEASURED  — both slots hold a value DERIVED FROM THE COMPUTATION (a variable, a
              subscript, a conditional on measured data).  This is the dangerous
              class: it looks like a check, tracks whatever the code does, and
              cannot report a regression.  Fix by supplying an INDEPENDENT expected
              value, or by demoting it to `add_data` / `add_parameter`, which is
              what recording-without-checking is for.
  LITERAL   — both slots hold the same constant (`0`, `1`, `True`, `'pass'`).  These
              are documentary flags the author asserted, not measurements.  Still
              misleading, because they render as `passed: true` beside real checks,
              but they do not silently track a drifting quantity.  Fix by moving to
              `add_parameter`, or by making the flag actually check something.

Detection is AST-level (structural equality of the two argument nodes), so
whitespace, line breaks and formatting cannot hide a hit, and a textual
false-positive like `f(a)` vs `f(b)` cannot be produced.

Usage:  python3 computations/audits/self_fulfilling_assertion_audit.py [--selftest]
Exit 1 if any MEASURED hit is found; LITERAL hits are reported but do not gate.
"""
from __future__ import annotations

import ast
import io
import sys
from pathlib import Path

ROOTS = ("computations",)
SKIP = ("_deprecated",)


def _dump(node):
    try:
        return ast.dump(node, annotate_fields=False)
    except Exception:
        return None


def _is_literal(node) -> bool:
    """True when the expression is a constant, or a conditional over constants."""
    if isinstance(node, ast.Constant):
        return True
    if isinstance(node, ast.UnaryOp) and isinstance(node.operand, ast.Constant):
        return True
    return False


def scan(roots=ROOTS):
    hits, scanned, total = [], 0, 0
    for root in roots:
        for p in sorted(Path(root).rglob("*.py")):
            if any(s in str(p) for s in SKIP):
                continue
            try:
                tree = ast.parse(io.open(p, encoding="utf-8").read())
            except Exception:
                continue
            scanned += 1
            for node in ast.walk(tree):
                if not (isinstance(node, ast.Call)
                        and isinstance(node.func, ast.Attribute)
                        and node.func.attr == "add_assertion"):
                    continue
                total += 1
                if len(node.args) < 3:
                    continue
                d_c, d_e = _dump(node.args[1]), _dump(node.args[2])
                if d_c is None or d_c != d_e:
                    continue
                name = (node.args[0].value
                        if isinstance(node.args[0], ast.Constant) else "<dynamic>")
                hits.append({
                    "file": str(p),
                    "line": node.lineno,
                    "assertion": name,
                    "expr": ast.unparse(node.args[1])[:80],
                    "kind": "LITERAL" if _is_literal(node.args[1]) else "MEASURED",
                })
    return hits, scanned, total


def selftest() -> int:
    """Fails unless the known MEASURED instance is detected and classed correctly.

    Guards against a future narrowing quietly reporting a clean tree — the failure
    mode a name-keyed or textual detector would have.
    """
    src = ('w.add_assertion("a", d["x"], d["x"])\n'
           'w.add_assertion("b", 0, 0)\n'
           'w.add_assertion("c", d["x"], d["y"])\n')
    tree = ast.parse(src)
    found = {}
    for node in ast.walk(tree):
        if (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
                and node.func.attr == "add_assertion" and len(node.args) >= 3):
            if _dump(node.args[1]) == _dump(node.args[2]):
                found[node.args[0].value] = (
                    "LITERAL" if _is_literal(node.args[1]) else "MEASURED")
    if found.get("a") != "MEASURED":
        print("SELFTEST FAIL: a measured self-comparison was not caught as MEASURED")
        return 1
    if found.get("b") != "LITERAL":
        print("SELFTEST FAIL: a literal self-comparison was not classed LITERAL")
        return 1
    if "c" in found:
        print("SELFTEST FAIL: a genuine two-sided assertion was flagged")
        return 1
    print("SELFTEST OK")
    return 0


def main() -> int:
    if "--selftest" in sys.argv:
        return selftest()
    hits, scanned, total = scan()
    measured = [h for h in hits if h["kind"] == "MEASURED"]
    literal = [h for h in hits if h["kind"] == "LITERAL"]
    print("=" * 86)
    print(" add_assertion(name, X, X) — assertions that compare a value to itself")
    print("=" * 86)
    print(f" scanned {scanned} files, {total} add_assertion calls")
    print(f" MEASURED (cannot report a regression): {len(measured)}"
          f"   LITERAL (documentary flag): {len(literal)}\n")
    for label, group in (("MEASURED", measured), ("LITERAL", literal)):
        if not group:
            continue
        print(f" ── {label} " + "─" * (78 - len(label)))
        cur = None
        for h in sorted(group, key=lambda x: (x["file"], x["line"])):
            if h["file"] != cur:
                cur = h["file"]
                print(f"  {cur}")
            print(f"      L{h['line']:<5} {h['assertion']:<40} {h['expr']}")
        print()
    print(f" files affected: {len({h['file'] for h in hits})}")
    if measured:
        print("\n A MEASURED hit is not a style issue: the quantity can invert and the")
        print(" assertion still reports passed. Supply an independent expected value,")
        print(" or demote to add_data / add_parameter — recording is not checking.")
    return 1 if measured else 0


if __name__ == "__main__":
    raise SystemExit(main())
