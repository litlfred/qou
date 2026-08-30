#!/usr/bin/env python3
"""Assertions whose TOLERANCE is finer than the arithmetic that produced the value.

An assertion carrying `tolerance=1e-40` on a RESIDUAL cast through `float()`
cannot mean what it says. IEEE double resolves ~2.2e-16 relative, so for a
quantity of order 1 there is nothing between "exactly 0.0" and "about 1e-16".
Such an assertion has exactly two possible meanings, and neither is the
advertised one:

  * the cast value is exactly 0.0 -> trivially true, measuring nothing; or
  * it is nonzero at ~1e-16       -> must fail.

It can never mean "agreement verified to 1e-40". In a witness it reads as one.

TWO BUCKETS, AND ONLY ONE OF THEM IS A DEFECT
---------------------------------------------
The argument above is about ROUNDOFF, so it only bites when the compared
quantity is a residual — something whose exact value is 0 and whose float
representation therefore carries error. It does NOT bite when the quantity is
EXACTLY REPRESENTABLE in float64, and integers below 2^53 are.

  w.add_assertion("integer_spin_dim_sum_squares",
                  computed=float(result["int_burnside_sum_sq"]),
                  expected=60.0, tolerance=1e-30)

`int_burnside_sum_sq` is an integer sum of squares; `float(60)` is exactly
`60.0`; the comparison is exact and the tight tolerance is meaningful — it is an
integer equality check written with a tolerance, not a precision claim. Three
such sites live in `probes/gap_a4_T10_mckay_character_2I_probe.py:172,182,192`.
They are FALSE POSITIVES of the criterion this file was first written with, and
they are the reason it now splits its output.

So the report has two sections:

  RESIDUAL   `expected` is a literal 0 -> the defect. Roundoff lives exactly
             where the tolerance claims resolution. GATING (exit 1).
  EQUALITY   `expected` is nonzero or non-literal -> MAY be an exact-integer
             equality check, may be a genuine float64 precision claim on a
             non-integral quantity. ADVISORY: the audit cannot tell which, and
             guessing is the false-positive mechanism the taxonomy records.
             Inspect by hand; ask whether the computed quantity is an integer
             count or an integer-valued algebraic invariant.

I published "none of the 61 is an integer count" in this file's own first
commit (`f5aa6e5ce9`). That was wrong. It came from a grep for
`float\((n_|len\(|count|num_|int\()`, which cannot match
`float(result["int_burnside_sum_sq"])` — the integer-ness is in the DICT KEY,
where no pattern over the call shape can see it. Corrected here.

WHY NO EXISTING AUDIT CATCHES THIS
----------------------------------
`witness_raw_float64_audit` sees the `float()` and flags the FIELD.
`always_vacuous_assertion_scan` looks for `computed == expected`.
Neither compares the TOLERANCE against the RESOLUTION OF THE TYPE the value is
carried in — which is the actual defect, and is mechanically checkable.

Found 2026-08-30 in `fr_pullback_borromean_h3a_test.py:549,554` while answering
"which probes are on float or not trustworthy". That file also carries a
substrate-pure banner (it claims to be float-free), and its witness has never
been committed — so the numbers behind those 1e-40 claims have never existed.
Bean `qou-58zw`.

METHOD. AST, not grep: parse each `computations/**/*.py`, find `add_assertion`
calls, and pair the `computed` expression with the `tolerance` literal. A call
is flagged when the tolerance is a real number strictly below FLOAT64_FLOOR and
the computed expression contains a `float(...)` cast. Both halves are required
— `tolerance=1e-40` on an `mpf` value is legitimate and common here, and a
`float()` cast under a loose tolerance is merely a display choice.

NOT FLAGGED, deliberately:
  * `mpf`/`mpmath` computed values at any tolerance — the point of 50-dps work.
  * string tolerances (`"0"`, `"0.5"`) — those go through mpf downstream.
  * tolerance 0 / 0.0 — an exactness claim, a different question, and one the
    vacuous-assertion scans already cover.

RUNTIME ~9.7 s (measured 3x, 3490 files AST-parsed). Not the ~1 s I first
claimed in this file's own commit message. That matters: it is 10x the
`--files`-scoped bootstrap-order guard, so wiring this into the PreToolUse
commit hook as a whole-tree sweep would put ten seconds on every commit.
Give it a `--files` mode first if it is ever hooked.

Exit 0 when clean, 1 otherwise.

-- Ref: [manuscript] docs/audits/2026-08-15-detector-blindness-taxonomy.md
"""
from __future__ import annotations

import ast
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {"_deprecated", "__pycache__", "data", "node_modules"}

#: IEEE-754 double: ~2.220446e-16 relative. A tolerance at or below this cannot
#: be distinguished from zero by a float64 quantity of order unity.
FLOAT64_FLOOR = 2.220446049250313e-16


def _is_float_cast(node: ast.AST) -> bool:
    """Does this expression pass through a `float(...)` call?"""
    for sub in ast.walk(node):
        if (isinstance(sub, ast.Call) and isinstance(sub.func, ast.Name)
                and sub.func.id == "float"):
            return True
    return False


def _numeric(node: ast.AST):
    """The literal value if this is a plain number, else None.

    Deliberately does NOT evaluate names or arithmetic: a tolerance that is not
    a literal is not something this audit can judge, and guessing would be the
    false-positive mechanism the taxonomy keeps recording.
    """
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return float(node.value)
    if (isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub)
            and isinstance(node.operand, ast.Constant)
            and isinstance(node.operand.value, (int, float))):
        return -float(node.operand.value)
    return None


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
        tol_node, comp_node = kw.get("tolerance"), kw.get("computed")
        if tol_node is None or comp_node is None:
            continue
        tol = _numeric(tol_node)
        if tol is None or tol <= 0 or tol >= FLOAT64_FLOOR:
            continue
        if not _is_float_cast(comp_node):
            continue
        # A literal 0 expected means the computed value is a RESIDUAL, so the
        # roundoff argument applies and this is the defect. Anything else may be
        # an exact-integer equality check (see the module docstring) and the
        # audit cannot decide which -- so it reports it without gating on it.
        exp = _numeric(kw["expected"]) if "expected" in kw else None
        bucket = "residual" if exp == 0.0 else "equality"
        name = ""
        if node.args and isinstance(node.args[0], ast.Constant):
            name = str(node.args[0].value)[:60]
        out.append({
            "path": os.path.relpath(path, ROOT),
            # The `computed=` expression's OWN line, not the call's. In a fluent
            # builder chain -- `WitnessBuilder(...).set_description(...)
            # .add_assertion(...).add_assertion(...)` -- every chained Call node
            # carries the lineno where the WHOLE chain starts, so three distinct
            # assertions all reported one line (measured:
            # gauge_coupling_uniqueness_probe 3x line 125,
            # explicit_central_idempotent_probe 3x line 204). AST-correct and
            # useless for finding the site. The snippet was already taken from
            # `comp_node.lineno`, so the two disagreed in the same row.
            "line": comp_node.lineno,
            "assertion": name,
            "tolerance": tol,
            "bucket": bucket,
            "expected": exp,
            "computed": lines[comp_node.lineno - 1].strip()[:88]
            if comp_node.lineno - 1 < len(lines) else "",
        })
    return out


_SELFTEST_RESIDUAL = '''
w.add_assertion("a", computed=float(dev), expected=0.0, tolerance=1e-40)
'''
#: The gap_a4_T10 shape: an integer-valued quantity compared to a nonzero
#: literal. Must be SEEN (so a real precision claim on a non-integral quantity
#: is not lost) but must NOT gate (so the integer checks do not read as defects).
_SELFTEST_EQUALITY = '''
w.add_assertion("f", computed=float(r["int_burnside_sum_sq"]), expected=60.0,
                tolerance=1e-30)
'''
_SELFTEST_QUIET = '''
w.add_assertion("b", computed=mpf(dev), expected=0.0, tolerance=1e-40)
w.add_assertion("c", computed=float(dev), expected=0.0, tolerance=1e-6)
w.add_assertion("d", computed=float(dev), expected=0.0, tolerance=0)
w.add_assertion("e", computed=float(dev), expected=0.0, tolerance="0")
'''


def _selftest() -> None:
    """A detector that cannot fire is not a detector. Pin all three directions.

    The middle case is the one this selftest exists for: before the split, the
    equality shape fired as a defect. Pinning it as `equality` is what stops a
    future narrowing from quietly re-merging the buckets.
    """
    import tempfile
    cases = ((_SELFTEST_RESIDUAL, 1, "residual"),
             (_SELFTEST_EQUALITY, 1, "equality"),
             (_SELFTEST_QUIET, 0, None))
    for src, want, bucket in cases:
        with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
            f.write(src)
            tmp = f.name
        try:
            got = scan_file(tmp)
            assert len(got) == want, f"selftest: expected {want} hit(s), got {len(got)}"
            if bucket:
                assert got[0]["bucket"] == bucket, (
                    f"selftest: expected bucket {bucket}, got {got[0]['bucket']}")
        finally:
            os.unlink(tmp)


def main(argv: list[str] | None = None) -> int:
    _selftest()
    argv = list(sys.argv[1:] if argv is None else argv)
    findings = []
    if argv and argv[0] == "--files":
        # Scope to specific paths, for the pre-commit hook. A whole-tree sweep
        # AST-parses 3490 files at ~9.7 s; the files one commit touches is
        # milliseconds. A PreToolUse hook runs BEFORE the tool call, so the
        # difference is seconds added to every commit.
        for a in argv[1:]:
            if a.endswith(".py") and os.path.exists(a):
                findings.extend(scan_file(os.path.abspath(a)))
    else:
        for root, dirs, files in os.walk(ROOT):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
            for fn in sorted(files):
                if fn.endswith(".py"):
                    findings.extend(scan_file(os.path.join(root, fn)))
    findings.sort(key=lambda r: (r["path"], r["line"]))
    residual = [f for f in findings if f["bucket"] == "residual"]
    equality = [f for f in findings if f["bucket"] == "equality"]

    def _dump(rows):
        for f in rows:
            exp = "non-literal" if f["expected"] is None else f"{f['expected']:g}"
            print(f"  {f['path']}:{f['line']}  tol={f['tolerance']:g}  expected={exp}")
            print(f"      {f['assertion']}")
            print(f"      {f['computed']}")

    print("=" * 78)
    print(" TOLERANCE BELOW THE ARITHMETIC FLOOR — a claim the type cannot support")
    print("=" * 78)
    print(f"  float64 resolution used   : {FLOAT64_FLOOR:.6e}")
    print(f"  flagged assertions        : {len(findings)}")
    print(f"    RESIDUAL (gating)       : {len(residual)}   expected == 0")
    print(f"    EQUALITY (advisory)     : {len(equality)}   expected != 0 / non-literal")
    print(f"  files                     : {len({f['path'] for f in findings})}")
    print("  selftest                  : PASS (residual fires, equality classifies,")
    print("                              4 must-stay-quiet)")
    if residual:
        print()
        print("-- RESIDUAL — the defect. A residual's exact value is 0, so float64")
        print("   roundoff lives exactly where the tolerance claims resolution.")
        print()
        _dump(residual)
    if equality:
        print()
        print("-- EQUALITY — ADVISORY, NOT GATING. May be an exact-integer equality")
        print("   check (integers below 2^53 are exact in float64, so `float(60)`")
        print("   compared to `60.0` under tol=1e-30 is meaningful), or may be a")
        print("   genuine float64 precision claim on a non-integral quantity. This")
        print("   audit cannot tell which; inspect the computed quantity by hand.")
        print()
        _dump(equality)
    return 1 if residual else 0


if __name__ == "__main__":
    sys.exit(main())
