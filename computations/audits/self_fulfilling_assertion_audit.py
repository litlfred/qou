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
SKIP = ("_deprecated", "fsh-guts",)


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


def _call_parts(node: ast.Call):
    """(name, computed, expected) for an add_assertion call, either calling form.

    `add_assertion(name, computed, expected)` and
    `add_assertion("name", computed=..., expected=...)` are the same call. This
    audit read ONLY the positional form for its first year, and positional is
    the minority form: measured on this corpus, 487 positional against 3300
    keyword. So it was scanning 13% of the calls and reporting "MEASURED: 0"
    while 58 measured self-comparisons sat in the keyword form, including
    `habiro_tr_M_proton_matches_direct` — a name asserting a cross-check that
    compares a value to itself and therefore cannot fail.
    """
    kw = {k.arg: k.value for k in node.keywords}
    name = kw.get("name")
    if name is None and node.args:
        name = node.args[0]
    computed = kw.get("computed")
    expected = kw.get("expected")
    if computed is None and len(node.args) >= 2:
        computed = node.args[1]
    if expected is None and len(node.args) >= 3:
        expected = node.args[2]
    if computed is None or expected is None:
        return None
    return name, computed, expected


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
                if not isinstance(node, ast.Call):
                    continue
                fn = node.func
                if (getattr(fn, "attr", None) or getattr(fn, "id", None)) \
                        != "add_assertion":
                    continue
                total += 1
                parts = _call_parts(node)
                if parts is None:
                    continue
                name_node, c_node, e_node = parts
                d_c, d_e = _dump(c_node), _dump(e_node)
                if d_c is None or d_c != d_e:
                    continue
                name = (name_node.value
                        if isinstance(name_node, ast.Constant) else "<dynamic>")
                hits.append({
                    "file": str(p),
                    "line": node.lineno,
                    "assertion": name,
                    "expr": ast.unparse(c_node)[:80],
                    "kind": "LITERAL" if _is_literal(c_node) else "MEASURED",
                })
    return hits, scanned, total


def selftest() -> int:
    """Fails unless the known MEASURED instance is detected and classed correctly.

    Guards against a future narrowing quietly reporting a clean tree — the failure
    mode a name-keyed or textual detector would have.
    """
    src = ('w.add_assertion("a", d["x"], d["x"])\n'
           'w.add_assertion("b", 0, 0)\n'
           'w.add_assertion("c", d["x"], d["y"])\n'
           # KEYWORD form — the majority of calls in this corpus, and entirely
           # unscanned until 2026-08-30. The selftest used to exercise only the
           # positional path, so it validated the one branch that worked.
           'w.add_assertion(name="kw_measured", computed=d["x"], expected=d["x"])\n'
           'w.add_assertion(name="kw_literal", computed=1836.152, '
           'expected=1836.152)\n'
           'w.add_assertion(name="kw_ok", computed=d["x"], expected=d["y"])\n'
           # mixed: positional name, keyword values
           'w.add_assertion("mixed", computed=d["x"], expected=d["x"])\n')
    tree = ast.parse(src)
    found = {}
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        fn = node.func
        if (getattr(fn, "attr", None) or getattr(fn, "id", None)) != "add_assertion":
            continue
        parts = _call_parts(node)
        if parts is None:
            continue
        name_node, c_node, e_node = parts
        if _dump(c_node) == _dump(e_node) and isinstance(name_node, ast.Constant):
            found[name_node.value] = (
                "LITERAL" if _is_literal(c_node) else "MEASURED")
    if found.get("a") != "MEASURED":
        print("SELFTEST FAIL: a measured self-comparison was not caught as MEASURED")
        return 1
    if found.get("b") != "LITERAL":
        print("SELFTEST FAIL: a literal self-comparison was not classed LITERAL")
        return 1
    if "c" in found:
        print("SELFTEST FAIL: a genuine two-sided assertion was flagged")
        return 1
    if found.get("kw_measured") != "MEASURED":
        print("SELFTEST FAIL: KEYWORD-form measured self-comparison missed "
              "(the blind spot that hid 58 of them)")
        return 1
    if found.get("kw_literal") != "LITERAL":
        print("SELFTEST FAIL: keyword-form literal self-comparison missed")
        return 1
    if found.get("mixed") != "MEASURED":
        print("SELFTEST FAIL: positional-name + keyword-values form missed")
        return 1
    if "kw_ok" in found:
        print("SELFTEST FAIL: a genuine keyword-form assertion was flagged")
        return 1
    print("SELFTEST OK")
    return 0


def main() -> int:
    if "--selftest" in sys.argv or "--self-test" in sys.argv:
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
