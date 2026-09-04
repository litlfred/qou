#!/usr/bin/env python3
"""Audits that go SILENT on input they could not parse (bean `qou-brkp`).

THE DEFECT. A checker whose parse is wrapped in a broad handler that returns
an empty result reports "no findings" for a file it could not read. "No
findings" and "no information" are different answers, and returning the first
for the second converts breakage into silence.

WHY IT IS NOT HYPOTHETICAL HERE. Commit 2bcbefee49 inserted `mp.dps = 50`
between a dict literal's opening brace and its first entry in two producers,
making them unparseable. The audit written in that same commit to enforce
dps-before-constants opened with `except Exception: return []`, so it reported
those two files clean. They were unrunnable from 2026-08-07 and nobody noticed
for a month. AGENTS.md calls `precision-gates.sh` "not a stopgap until CI
returns; it IS the gate" -- and six of the seven audits it runs had this shape,
so a producer that stopped parsing passed the whole NO-FLOAT64 family clean.

WHAT THIS SCRIPT DOES, AND WHAT IT DELIBERATELY DOES NOT.

  --scan (default)  Narrow by AST pattern: a `try` whose body calls ast.parse
                    and whose handler is broad (bare / Exception / SyntaxError
                    / ValueError) and swallows (return empty container, return
                    None/0/False, pass, continue). Fast, whole-tree, complete
                    for the shapes it knows.

  --verify SCRIPT   Decide by EXECUTION for one audit: plant an unparseable
                    probe, run the audit, report whether it names the probe.

**A `--scan` hit is a CANDIDATE, never a verdict, and the reason is measured.**
An audit legitimately skips a file outside its scope, and a scope filter can
run BEFORE the parse guard -- so "did not mention my probe" is not evidence of
the defect unless the probe was in scope for THAT audit. Three false verdicts
were produced this way while fixing the gate family:

  * never_raises_dps_audit    checks `emits_witness(src)` before parsing, so a
                              probe naming neither WitnessBuilder nor
                              .witness.json is skipped for a good reason.
  * no_free_parameter_certificate  walks only the import cone from
                              ENTRY_MODULES, so a probe nothing imports is
                              never visited. It does not go silent at all --
                              it CRASHES, which is the opposite failure.
  * (the same probe, twice)   read as SILENT on both before being made
                              in-scope.

Hence `--verify` takes `--probe-imports` / `--probe-names` so the probe can be
made in scope for the audit under test, and its report says plainly when it
cannot establish scope.

THIS SCRIPT MUST NOT HAVE THE DEFECT IT LOOKS FOR. A file it cannot parse is
reported as `self-unparseable`, never skipped; `--selftest` fails unless it
detects a known-positive fixture, so a future narrowing cannot report a clean
tree the way a weakened detector would.

USAGE
    python3 computations/audits/silent_parse_failure_audit.py
    python3 computations/audits/silent_parse_failure_audit.py --selftest
    python3 computations/audits/silent_parse_failure_audit.py --verify computations/mpf_float_source_audit.py
"""
from __future__ import annotations

import argparse
import ast
import json
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SEARCH_ROOTS = [ROOT / "computations", ROOT / "scripts", ROOT / "tools",
                ROOT / "content" / "pipeline"]

BROAD = {"Exception", "BaseException", "SyntaxError", "ValueError", "OSError"}

# Verdicts established by EXECUTION while fixing the gate family (2026-09-04).
# Recorded so they are not re-derived, and so a regression is visible.
GATE_FAMILY_LEDGER = {
    "computations/module_const_precision_audit.py": "was-silent, fixed",
    "computations/mpf_context_dps_audit.py": "was-silent, fixed (blind rows print but do not fail --strict)",
    "computations/mpf_float_source_audit.py": "was-silent, fixed",
    "computations/mpf_mixed_arithmetic_audit.py": "was-silent, fixed",
    "computations/never_raises_dps_audit.py": "already correct -- the positive control",
    "computations/no_free_parameter_certificate.py": "CRASHED (not silent), fixed",
    "computations/numpy_mpmath_dtype_leak_audit.py": "was-silent, fixed",
}


def _swallow(handler: ast.ExceptHandler) -> str | None:
    """What this handler does with the failure, if it discards it."""
    for st in handler.body:
        if isinstance(st, ast.Return):
            v = st.value
            if v is None:
                return "return None"
            if isinstance(v, (ast.List, ast.Dict, ast.Set, ast.Tuple)):
                elts = getattr(v, "elts", None)
                keys = getattr(v, "keys", None)
                if not (elts or keys):
                    return f"return empty {type(v).__name__}"
            if isinstance(v, ast.Constant) and v.value in (None, 0, False):
                return f"return {v.value!r}"
        elif isinstance(st, ast.Pass):
            return "pass"
        elif isinstance(st, ast.Continue):
            return "continue"
    return None


def _calls_parse(node: ast.AST) -> bool:
    for n in ast.walk(node):
        if not isinstance(n, ast.Call):
            continue
        f = n.func
        if isinstance(f, ast.Attribute) and f.attr == "parse":
            return True
        if isinstance(f, ast.Name) and f.id == "parse":
            return True
    return False


def scan_source(src: str, rel: str) -> list[dict]:
    """Candidates in one file. A file that does not parse is REPORTED."""
    try:
        tree = ast.parse(src, rel)
    except SyntaxError as e:
        return [{"file": rel, "line": e.lineno or 0, "kind": "self-unparseable",
                 "detail": f"SyntaxError: {e.msg}"}]
    except Exception as e:                                   # noqa: BLE001
        return [{"file": rel, "line": 0, "kind": "self-unparseable",
                 "detail": f"{type(e).__name__}: {e}"}]

    out: list[dict] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Try) or not _calls_parse(node):
            continue
        for h in node.handlers:
            et = h.type
            if et is None:
                name = "bare"
            elif isinstance(et, ast.Name) and et.id in BROAD:
                name = et.id
            elif isinstance(et, ast.Tuple) and any(
                    isinstance(x, ast.Name) and x.id in BROAD for x in et.elts):
                name = "(" + ", ".join(getattr(x, "id", "?") for x in et.elts) + ")"
            else:
                continue
            sw = _swallow(h)
            if sw:
                out.append({"file": rel, "line": h.lineno, "kind": "candidate",
                            "detail": f"except {name} -> {sw}"})
    return out


def scan() -> list[dict]:
    rows: list[dict] = []
    for root in SEARCH_ROOTS:
        if not root.exists():
            continue
        for p in sorted(root.rglob("*.py")):
            if "_deprecated" in p.parts or ".lake" in p.parts:
                continue
            rel = p.relative_to(ROOT).as_posix()
            try:
                src = p.read_text(encoding="utf-8")
            except Exception as e:                           # noqa: BLE001
                rows.append({"file": rel, "line": 0, "kind": "self-unreadable",
                             "detail": f"{type(e).__name__}: {e}"})
                continue
            if "ast.parse" not in src and "ast import parse" not in src:
                continue
            rows.extend(scan_source(src, rel))
    return rows


PROBE_BODY = '''"""Deliberately unparseable probe planted by silent_parse_failure_audit."""
{imports}
{names}
CONST = {{

mp.dps = 50
    "x": mpf(0.1),
}}
'''


def verify(script: Path, imports: str, names: str, timeout: int) -> dict:
    """Decide by execution: does `script` mention a planted unparseable file?"""
    probe = ROOT / "computations" / "zzz_silent_parse_probe.py"
    probe.write_text(PROBE_BODY.format(imports=imports, names=names))
    try:
        ast.parse(probe.read_text())
        return {"script": script.as_posix(), "verdict": "PROBE-NOT-BROKEN",
                "note": "the planted probe parses; the test is meaningless"}
    except SyntaxError:
        pass
    try:
        r = subprocess.run([sys.executable, str(script)], cwd=ROOT,
                           capture_output=True, text=True, timeout=timeout)
        out = (r.stdout or "") + (r.stderr or "")
    except subprocess.TimeoutExpired:
        return {"script": script.as_posix(), "verdict": "TIMEOUT",
                "note": f"no verdict in {timeout}s"}
    finally:
        probe.unlink(missing_ok=True)

    named = "zzz_silent_parse_probe" in out
    crashed = "Traceback (most recent call last)" in out
    if named and not crashed:
        v = "REPORTS IT"
    elif crashed:
        v = "CRASHES (loud, but takes the whole run out)"
    else:
        v = "SILENT (or the probe was out of scope -- see the module docstring)"
    return {"script": script.as_posix(), "verdict": v, "exit": r.returncode}


def selftest() -> int:
    """A known-positive MUST be detected. A detector that can report a clean
    tree without proving it can still see the defect is the defect."""
    pos = '''import ast
def f(p):
    try:
        return ast.parse(p.read_text())
    except Exception:
        return []
'''
    neg = '''import ast
def f(p):
    try:
        return ast.parse(p.read_text())
    except SyntaxError as e:
        return [{"kind": "syntax-error", "detail": e.msg}]
'''
    bad_hits = scan_source(pos, "<pos>")
    good_hits = scan_source(neg, "<neg>")
    broken = scan_source("def f(:\n", "<broken>")

    fails = []
    if not any(h["kind"] == "candidate" for h in bad_hits):
        fails.append("known-positive NOT detected")
    if any(h["kind"] == "candidate" for h in good_hits):
        fails.append("known-negative falsely flagged")
    if not any(h["kind"] == "self-unparseable" for h in broken):
        fails.append("an unparseable input was not reported as self-unparseable")

    if fails:
        print("SELF-TEST FAILED:")
        for f_ in fails:
            print(f"   {f_}")
        return 1
    print("SELF-TEST PASSED — positive detected, negative not flagged, "
          "unparseable input reported rather than skipped.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--verify", metavar="SCRIPT",
                    help="run one audit against a planted unparseable probe")
    ap.add_argument("--probe-imports",
                    default="import numpy as np\nimport mpmath\nfrom mpmath import mp, mpf",
                    help="import block for the probe, to bring it IN SCOPE")
    ap.add_argument("--probe-names",
                    default="from qou_substrate.witness import WitnessBuilder   # .witness.json",
                    help="extra lines naming markers an audit's prefilter looks for")
    ap.add_argument("--timeout", type=int, default=300)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if this script could not read or parse a file it scanned")
    args = ap.parse_args()

    if args.selftest:
        return selftest()
    if args.verify:
        res = verify(Path(args.verify), args.probe_imports, args.probe_names,
                     args.timeout)
        print(json.dumps(res, indent=2))
        return 0

    rows = scan()
    cands = [r for r in rows if r["kind"] == "candidate"]
    selfbad = [r for r in rows if r["kind"].startswith("self-")]
    by_file: dict[str, int] = {}
    for r in cands:
        by_file[r["file"]] = by_file.get(r["file"], 0) + 1

    if args.json:
        print(json.dumps({"candidates": cands, "self_unreadable": selfbad,
                          "ledger": GATE_FAMILY_LEDGER}, indent=2))
        return 1 if (args.strict and selfbad) else 0

    print("=" * 74)
    print("SILENT PARSE-FAILURE AUDIT — checkers that go quiet on unreadable input")
    print("=" * 74)
    print(f"  candidate sites        : {len(cands)}")
    print(f"  files                  : {len(by_file)}")
    print(f"  this script could not read/parse : {len(selfbad)}")
    print()
    print("  A CANDIDATE IS NOT A VERDICT. An audit may skip a file for a good")
    print("  reason, and a scope filter can run BEFORE the parse guard. Decide")
    print("  with --verify, and make the probe in scope for the audit under test.")

    if by_file:
        print("\n  candidates by file:")
        for f, c in sorted(by_file.items(), key=lambda kv: (-kv[1], kv[0])):
            mark = "  [gate-family: " + GATE_FAMILY_LEDGER[f] + "]" if f in GATE_FAMILY_LEDGER else ""
            print(f"    {c:>3}  {f}{mark}")

    if selfbad:
        print("\n  THIS SCRIPT WAS BLIND TO:")
        for r in selfbad:
            print(f"    {r['file']}:{r['line']}  {r['detail']}")

    return 1 if (args.strict and selfbad) else 0


if __name__ == "__main__":
    sys.exit(main())
