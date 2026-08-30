#!/usr/bin/env python3
"""Assertions whose TOLERANCE is finer than the arithmetic that produced the value.

An assertion carrying `tolerance=1e-40` on a value cast through `float()` cannot
mean what it says. IEEE double resolves ~2.2e-16 relative, so for a quantity of
order 1 there is nothing between "exactly 0.0" and "about 1e-16". Such an
assertion therefore has exactly two possible meanings, and neither is the
advertised one:

  * the cast value is exactly 0.0 -> trivially true, measuring nothing; or
  * it is nonzero at ~1e-16       -> must fail.

It can never mean "agreement verified to 1e-40". In a witness it reads as one.

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
        name = ""
        if node.args and isinstance(node.args[0], ast.Constant):
            name = str(node.args[0].value)[:60]
        out.append({
            "path": os.path.relpath(path, ROOT),
            "line": node.lineno,
            "assertion": name,
            "tolerance": tol,
            "computed": lines[comp_node.lineno - 1].strip()[:88]
            if comp_node.lineno - 1 < len(lines) else "",
        })
    return out


_SELFTEST_FIRES = '''
w.add_assertion("a", computed=float(dev), expected=0.0, tolerance=1e-40)
'''
_SELFTEST_QUIET = '''
w.add_assertion("b", computed=mpf(dev), expected=0.0, tolerance=1e-40)
w.add_assertion("c", computed=float(dev), expected=0.0, tolerance=1e-6)
w.add_assertion("d", computed=float(dev), expected=0.0, tolerance=0)
w.add_assertion("e", computed=float(dev), expected=0.0, tolerance="0")
'''


def _selftest() -> None:
    """A detector that cannot fire is not a detector. Pin both directions."""
    import tempfile
    for src, want in ((_SELFTEST_FIRES, 1), (_SELFTEST_QUIET, 0)):
        with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
            f.write(src)
            tmp = f.name
        try:
            got = len(scan_file(tmp))
            assert got == want, f"selftest: expected {want} hit(s), got {got}"
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

    print("=" * 78)
    print(" TOLERANCE BELOW THE ARITHMETIC FLOOR — a claim the type cannot support")
    print("=" * 78)
    print(f"  float64 resolution used   : {FLOAT64_FLOOR:.6e}")
    print(f"  flagged assertions        : {len(findings)}")
    print(f"  files                     : {len({f['path'] for f in findings})}")
    print("  selftest                  : PASS (1 must-fire, 4 must-stay-quiet)")
    if findings:
        print()
        for f in findings:
            print(f"  {f['path']}:{f['line']}  tol={f['tolerance']:g}")
            print(f"      {f['assertion']}")
            print(f"      {f['computed']}")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
