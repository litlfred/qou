#!/usr/bin/env python3
"""source_float64_import_audit — the NO-FLOAT64 ratchet for SOURCE, not witnesses.

`witness_raw_float64_audit.py` catches float64 that has already reached a
witness. This catches it one step earlier, where it enters: a producer importing
the FLOAT form of a substrate constant from `q_parameter`.

`q_parameter` exports both forms of every constant. The float form is the
contamination:

    Q      (float)   2.725e-17 relative against the 50-dps closed form
    Q_MP   (mpf)     2.015e-50

Owner directive (AGENTS.md, re-affirmed 2026-08-31): NO FLOAT64 — excise. The
backlog is tolerated; it must only SHRINK, exactly like the witness baseline.
Adding a file to the baseline to silence a failure defeats the gate — excise at
the import instead.

Detection is by AST, not grep, for two reasons found the hard way while
measuring this population:
  * grep MISSES multi-line `from q_parameter import (...)` — it undercounted
    the file population by 17;
  * grep also COUNTS docstrings — `computations/__init__.py` and
    `_path_bridge.py` merely *describe* `from q_parameter import Q` in prose
    and have no such import at all.

Usage:
    python3 computations/audits/source_float64_import_audit.py [--strict] [--update-baseline]

`--strict` exits non-zero if any file gained float imports, or if a file with
none acquired some. Bean `qou-wsfl`.
"""
from __future__ import annotations

import ast
import io
import json
import os
import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent.parent
sys.path.insert(0, str(_ROOT / "computations"))
sys.path.insert(0, str(_ROOT / "tools" / "qou-substrate" / "python"))

# The FLOAT exports of q_parameter. Each has an `_MP` counterpart that is the
# excision target; `q_int` and the `_STR` forms are not float and are fine.
FLOAT_NAMES = frozenset({
    "Q", "Q_INV", "HA", "E_CROSS", "HBAR_Q", "HBAR_Q_SQ",
    "LN_Q", "TWO_Q", "VOL_4_1", "S_SKEIN", "TANH_LN_Q",
})

BASELINE = _ROOT / "computations" / "source-float64-import-baseline.json"
SCAN_ROOTS = ("computations",)
SKIP_PARTS = ("_deprecated", "__pycache__", ".git", "node_modules")


def _scan() -> dict:
    """{repo-relative path: [imported float name, ...]} for every producer."""
    found: dict[str, list[str]] = {}
    for root in SCAN_ROOTS:
        for dirpath, _dirnames, filenames in os.walk(_ROOT / root):
            if any(part in dirpath for part in SKIP_PARTS):
                continue
            for fn in sorted(filenames):
                if not fn.endswith(".py"):
                    continue
                path = Path(dirpath) / fn
                try:
                    tree = ast.parse(io.open(path, encoding="utf-8").read())
                except (SyntaxError, OSError, UnicodeDecodeError):
                    continue  # not this audit's business
                names = [
                    alias.name
                    for node in ast.walk(tree)
                    if isinstance(node, ast.ImportFrom)
                    and node.module == "q_parameter"
                    for alias in node.names
                    if alias.name in FLOAT_NAMES
                ]
                if names:
                    found[str(path.relative_to(_ROOT))] = sorted(names)
    return found


def main() -> int:
    t0 = time.monotonic()
    strict = "--strict" in sys.argv
    update = "--update-baseline" in sys.argv

    current = _scan()
    n_files = len(current)
    n_names = sum(len(v) for v in current.values())

    print("=" * 78)
    print(" NO-FLOAT64 source ratchet — q_parameter FLOAT imports")
    print("=" * 78)
    print(f"  files importing a float constant : {n_files}")
    print(f"  imported names                   : {n_names}")

    by_name: dict[str, int] = {}
    for names in current.values():
        for nm in names:
            by_name[nm] = by_name.get(nm, 0) + 1
    print("  by constant:", ", ".join(
        f"{k}={v}" for k, v in sorted(by_name.items(), key=lambda kv: -kv[1])))

    if not BASELINE.exists() or update:
        BASELINE.write_text(json.dumps({
            "note": ("Producers importing the FLOAT form of a q_parameter "
                     "constant, by name. The backlog is tolerated; it must only "
                     "SHRINK. Adding a file here to silence a failure defeats "
                     "the gate — excise at the import instead."),
            "enforced_rule": "AGENTS.md: NO-FLOAT64 — excise (owner, 2026-08-31).",
            "excision_target": "import the _MP counterpart (Q -> Q_MP, HA -> HA_MP, ...)",
            "bean": "qou-wsfl",
            "files_count": n_files,
            "names_count": n_names,
            "files": current,
        }, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"\n  baseline written: {BASELINE.name}")
        return 0

    base = json.loads(BASELINE.read_text(encoding="utf-8"))
    base_files = base.get("files", {})

    regressed, drained, new = [], [], []
    for path, names in sorted(current.items()):
        was = base_files.get(path)
        if was is None:
            new.append((path, names))
        elif len(names) > len(was):
            regressed.append((path, len(was), len(names)))
    for path, was in sorted(base_files.items()):
        now = current.get(path)
        if now is None:
            drained.append((path, len(was)))
        elif len(now) < len(was):
            drained.append((path, len(was) - len(now)))

    print(f"\n  regressed (count increased) : {len(regressed)}")
    for path, a, b in regressed[:20]:
        print(f"      {a} -> {b}   {path}")
    print(f"  NEW files with float imports: {len(new)}")
    for path, names in new[:20]:
        print(f"      {', '.join(names)}   {path}")
    print(f"  drained (progress)          : {len(drained)} file(s)")
    for path, delta in drained[:10]:
        print(f"      -{delta}   {path}")

    print(f"\n  elapsed: {time.monotonic() - t0:.1f}s")
    if strict and (regressed or new):
        print("\nFAIL (--strict): float64 imports were added.")
        print("  Excise at the import: Q -> Q_MP, Q_INV -> Q_INV_MP, HA -> HA_MP,")
        print("  E_CROSS -> E_CROSS_MP. Do NOT widen the baseline.")
        print("  Finish the file or revert it — a PARTIAL excision leaves matrices")
        print("  mixed and can be less precise than before (bean qou-wsfl).")
        return 1
    if strict:
        print("\nPASS (--strict): no new float64 imports.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
