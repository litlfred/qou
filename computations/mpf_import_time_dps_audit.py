#!/usr/bin/env python3
# polynomial_q_not_applicable: source-hygiene audit, no q-dependence.
"""Catch mpf constants built at IMPORT time, when mp.dps is still 15.

Owner directive: NO FLOAT64.

This closes the gap the other two float64 gates structurally cannot see.

    witness_float64_padding_audit.py   finds padding sitting in a witness
    mpf_float_source_audit.py          finds mpf(<float literal>) in source
    THIS                               finds mpf("<string>") built too early

The third is invisible to the second because the call is *already the
compliant form*. `mp.mpf("2.22456607")` is exactly what the source audit
tells you to write. But at module scope it runs at IMPORT time, when
`mp.dps` is still mpmath's default **15** — about binary64. The value is
rounded to ~53 bits before `set_compute_dps()` is ever called, and raising
dps afterwards cannot recover what was already discarded. Serialize it at
50 dps and you print the binary64 expansion:

    mp.mpf("2.22456607")  built at dps=15, printed at 50 dps
      -> 2.2245660699999998399789546965621411800384521484375000...
                          ^^^ binary64 expansion, i.e. float64 padding

So **string-sourcing is necessary but not sufficient — the timing matters
too.** This is why a corpus with 5661 compliant `mpf("...")` call sites
still regenerated 289 padded fields on a single producer re-run.

The correct forms, both already used in this corpus:

    with mp.workdps(max(50, mp.mp.dps)):     # codata_constants._ame_binding_mev
        return +(mp.mpf(str(x)) / 1000)

    set_compute_dps()                        # 152 producers, at module level
    CONST = mp.mpf("2.22456607")             # ...then build constants

**Exactly-representable literals are not flagged** — `mpf(0)`, `mpf(1)`,
`mpf("0.5")`, `mpf("1e-40")`-style tolerances that survive the round trip
lose nothing by being built early. The discriminator is direct: build the
literal at dps=15 and again at dps=60; if they differ, precision was lost.

History: found 2026-08-07 while draining the re-padders measured in
docs/audits/2026-08-07-producer-repadding-empirical-sweep.md. The clean
sibling `binding_depth_stratified.py` reads its constants from
`codata_constants` (workdps-wrapped); the three that re-padded hand-typed
the same numbers at module scope.

Usage:
    python3 computations/mpf_import_time_dps_audit.py            # report
    python3 computations/mpf_import_time_dps_audit.py --strict   # exit 1 on defects
    python3 computations/mpf_import_time_dps_audit.py --self-test
"""
from __future__ import annotations

import argparse
import ast
import sys
from pathlib import Path

from mpmath import mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

# Directories whose constants never reach a committed witness.
SKIP_DIRS = {"_deprecated", "__pycache__", "data"}


def loses_precision(literal: str) -> bool:
    """True if building this literal at dps=15 discards information.

    Exactly-representable values (integers, dyadic rationals) round-trip
    identically and are harmless to build early.
    """
    try:
        with mp.workdps(15):
            early = +mp.mpf(literal)
        with mp.workdps(60):
            late = +mp.mpf(literal)
        with mp.workdps(60):
            return +early != +late
    except Exception:
        return False


def _literal_of(call: ast.Call) -> str | None:
    """The constant argument of an mpf(...) call, as a string, if it is one."""
    if not call.args:
        return None
    a = call.args[0]
    if isinstance(a, ast.Constant) and isinstance(a.value, (str, int, float)):
        return str(a.value)
    # mpf(-x) — unary minus over a constant
    if (isinstance(a, ast.UnaryOp) and isinstance(a.op, ast.USub)
            and isinstance(a.operand, ast.Constant)):
        return f"-{a.operand.value}"
    return None


def _is_mpf(call: ast.Call) -> bool:
    f = call.func
    name = (f.attr if isinstance(f, ast.Attribute)
            else f.id if isinstance(f, ast.Name) else None)
    return name == "mpf"


def _raises_dps(stmt: ast.stmt) -> bool:
    """Does this module-scope statement raise working precision?

    Three idioms are in use here and all three count:
      set_compute_dps()          — 152 producers
      mp.dps = 50 / mp.mp.dps    — the option_e and probe families
      with mp.workdps(...)       — codata_constants
    """
    if isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Call):
        f = stmt.value.func
        name = (f.attr if isinstance(f, ast.Attribute)
                else f.id if isinstance(f, ast.Name) else None)
        if name in {"set_compute_dps", "workdps"}:
            return True
    if isinstance(stmt, ast.Assign):
        for t in stmt.targets:
            if isinstance(t, ast.Attribute) and t.attr == "dps":
                return True
    return False


def scan_file(path: Path) -> list[dict]:
    """Module-scope mpf literals built BEFORE precision is raised.

    Position matters: a constant appearing after a module-level
    `set_compute_dps()` / `mp.dps = 50` is built at full precision and is
    correct. Only what precedes the raise is lossy — so this walks module
    statements in order and stops flagging once precision has been set.
    """
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"))
    except Exception:
        return []
    out: list[dict] = []
    for stmt in tree.body:                      # module scope only, in order
        if isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            continue
        if _raises_dps(stmt):
            break                               # everything after is fine
        # `with mp.workdps(...)` at module scope is the correct pattern
        if isinstance(stmt, ast.With) and "workdps" in ast.dump(stmt):
            continue
        for node in ast.walk(stmt):
            if not (isinstance(node, ast.Call) and _is_mpf(node)):
                continue
            try:
                rel = path.relative_to(ROOT).as_posix()
            except ValueError:
                rel = path.as_posix()
            lit = _literal_of(node)
            if lit is None:
                # mpf(<expression>) — e.g. mpf(str(G_A_PDG_ERR)). Lossiness
                # cannot be proved statically because the value is not in the
                # source, but the POSITION carries the same risk: built here it
                # is built at dps=15. Reported as `expr`, not as proven.
                # Skipping these was a real miss — gt_matrix_pslq_probe's
                # `PDG_G_A_ERR = mp.mpf(str(G_A_PDG_ERR))` emits
                # 0.00129999999999999994032551242639… for a datum of 0.0013.
                out.append({"file": rel, "line": node.lineno,
                            "literal": None, "kind": "expr"})
                continue
            if loses_precision(lit):
                out.append({"file": rel, "line": node.lineno,
                            "literal": lit, "kind": "literal"})
    return out


def emits_witness(path: Path) -> bool:
    """Does this script write a committed witness?

    A constant that never reaches a witness can lose precision at import
    without misrepresenting anything — a plot bound or a grid step is not
    a claim. Restricting to witness-emitting scripts is what separates
    'lossy' from 'dishonest'.
    """
    try:
        s = path.read_text(encoding="utf-8")
    except Exception:
        return False
    return "WitnessBuilder" in s or ".witness.json" in s


def scan(all_files: bool = False) -> list[dict]:
    rows: list[dict] = []
    for p in sorted(HERE.rglob("*.py")):
        if set(p.relative_to(HERE).parts) & SKIP_DIRS:
            continue
        if p.name == Path(__file__).name:
            continue
        if not all_files and not emits_witness(p):
            continue
        rows.extend(scan_file(p))
    return rows


def self_test() -> int:
    cases = [
        # (literal, loses precision at dps=15?)
        ("2.22456607", True),    # the live instance
        ("7.7180428", True),
        ("28.295674", True),
        ("1.1099785955573347", True),
        ("0.5", False),          # dyadic — exact
        ("0", False),
        ("1", False),
        ("0.25", False),
    ]
    bad = 0
    for lit, want in cases:
        got = loses_precision(lit)
        if got != want:
            print(f"  FAIL {lit}: expected {want}, got {got}")
            bad += 1
    if bad:
        print(f"SELF-TEST FAILED — {bad}/{len(cases)}")
        return 1
    print(f"SELF-TEST PASSED — {len(cases)} cases: lossy literals detected, "
          f"exactly-representable ones not flagged.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any import-time-lossy constant is found")
    ap.add_argument("--all", action="store_true",
                    help="include scripts that emit no witness (candidates, not defects)")
    a = ap.parse_args()
    if a.self_test:
        return self_test()

    rows = scan(all_files=a.all)
    by_file: dict[str, list[dict]] = {}
    for r in rows:
        by_file.setdefault(r["file"], []).append(r)

    scope = "all scripts" if a.all else "witness-emitting scripts"
    lit = sum(1 for r in rows if r.get("kind") == "literal")
    exp = sum(1 for r in rows if r.get("kind") == "expr")
    print(f"module-scope mpf built before precision is raised: {len(rows)}  [{scope}]")
    print(f"   proven lossy (literal arg): {lit}")
    print(f"   position-risky (expr arg, not statically provable): {exp}")
    print(f"files affected: {len(by_file)}\n")
    for f in sorted(by_file, key=lambda k: -len(by_file[k]))[:25]:
        print(f"  {f}  ({len(by_file[f])})")
        for r in by_file[f][:3]:
            k = r.get("kind", "literal")
            arg = repr(r['literal']) if r.get('literal') is not None else '<expr>'
            print(f"      L{r['line']}: mpf({arg})  [{k}]")

    if rows:
        print("\nFix: build the constant at compute precision — either call "
              "set_compute_dps() at module level BEFORE it, or wrap "
              "construction in `with mp.workdps(max(50, mp.mp.dps)):`, or "
              "read it from codata_constants (already workdps-wrapped).")
    if a.strict and rows:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
