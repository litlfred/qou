#!/usr/bin/env python3
"""Extraction wall gate — Phase 0 of the tooling-extraction workplan.

Counts files containing "qou" (case-insensitive) per extraction-bound
package under tools/ and compares against the committed baseline
(tools/extraction-wall-baseline.json).  New references above baseline
WARN by default; --strict exits non-zero (flips to hard once Phase 2
de-QOU completes).  --update-baseline rewrites the baseline after an
authorized de-QOU change (counts should only ever go DOWN).

Workplan: docs/workplans/2026-06-11-tooling-extraction-skills-migration.md
Ledger:   docs/coordination/tooling-extraction.md
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
BASELINE = REPO / "tools" / "extraction-wall-baseline.json"

PACKAGES = [
    "pyhecke",
    "pyhecke-native",
    "hecke-engine",
    "hecke-engine-wasm",
    "hecke-engine-node",
    "hecke-engine-r",
    "hecke-engine-jvm",
    "hecke-engine-c",
    "witness-schema",
]

SKIP_DIRS = {".git", "target", "node_modules", ".lake", "dist", "build", "__pycache__"}


def count_package(pkg: str) -> int:
    root = REPO / "tools" / pkg
    if not root.is_dir():
        return -1
    n = 0
    for r, dirs, files in os.walk(root):
        # prune in place so os.walk never descends into artifact dirs
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in files:
            f = Path(r) / name
            try:
                text = f.read_text(errors="ignore")
            except OSError:
                continue
            if "qou" in text.lower():
                n += 1
    return n


def main() -> int:
    strict = "--strict" in sys.argv
    update = "--update-baseline" in sys.argv

    counts = {pkg: count_package(pkg) for pkg in PACKAGES}

    if update or not BASELINE.exists():
        BASELINE.write_text(json.dumps(counts, indent=2) + "\n")
        print(f"baseline written: {BASELINE.relative_to(REPO)}")
        for pkg, n in counts.items():
            print(f"  {pkg}: {n}")
        return 0

    baseline = json.loads(BASELINE.read_text())
    regressions, improvements = [], []
    for pkg, n in counts.items():
        b = baseline.get(pkg)
        if b is None or n > b:
            regressions.append((pkg, b, n))
        elif n < b:
            improvements.append((pkg, b, n))

    for pkg, b, n in improvements:
        print(f"IMPROVED  {pkg}: {b} → {n} qou-referencing files "
              f"(run --update-baseline to ratchet)")
    for pkg, b, n in regressions:
        print(f"REGRESSED {pkg}: {b} → {n} qou-referencing files — "
              f"new QOU references entering an extraction-bound package")

    if not regressions:
        print(f"wall gate OK: no new qou references "
              f"({sum(v for v in counts.values() if v > 0)} files total, "
              f"ratchet only goes down)")
        return 0
    print(f"wall gate: {len(regressions)} package(s) regressed "
          f"({'FAIL --strict' if strict else 'warn-only'})")
    return 1 if strict else 0


if __name__ == "__main__":
    sys.exit(main())
