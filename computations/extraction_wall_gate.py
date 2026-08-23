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


#: `count_package` returns this when the package directory is absent. It is NOT
#: a file count, and must never be compared against a baseline as one: `-1 < b`
#: for every real baseline, so a DELETED package used to be reported as
#: `IMPROVED … → -1` and the message invited `--update-baseline`, which wrote
#: the sentinel into the baseline file. After that no real count could ever
#: exceed it, so the wall for that package was permanently disabled by a missing
#: directory. Bean `qou-i5jy`.
MISSING = -1


def count_package(pkg: str) -> int:
    root = REPO / "tools" / pkg
    if not root.is_dir():
        return MISSING
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

    missing = [pkg for pkg, n in counts.items() if n == MISSING]

    if update or not BASELINE.exists():
        # Never persist the sentinel: a baseline of -1 can never be regressed
        # against. Absent packages keep whatever the baseline already said, so
        # the wall stays armed if the directory comes back.
        prior = json.loads(BASELINE.read_text()) if BASELINE.exists() else {}
        writable = {pkg: (prior.get(pkg, n) if n == MISSING else n)
                    for pkg, n in counts.items()}
        BASELINE.write_text(json.dumps(writable, indent=2) + "\n")
        if missing:
            print(f"  NOTE: {len(missing)} package(s) absent, baseline left "
                  f"unchanged for them: {', '.join(missing)}")
        print(f"baseline written: {BASELINE.relative_to(REPO)}")
        # Print what was WRITTEN, not what was measured: for an absent package
        # those differ (measured MISSING, written = prior baseline), and printing
        # the sentinel beside a "baseline written" line is how it got trusted.
        for pkg, n in writable.items():
            print(f"  {pkg}: {n}" + ("  (absent — prior baseline retained)"
                                     if counts[pkg] == MISSING else ""))
        return 0

    baseline = json.loads(BASELINE.read_text())
    regressions, improvements = [], []
    for pkg, n in counts.items():
        b = baseline.get(pkg)
        if n == MISSING:
            continue          # reported separately; a sentinel is not a count
        if b is None or n > b:
            regressions.append((pkg, b, n))
        elif n < b:
            improvements.append((pkg, b, n))

    if missing:
        for pkg in missing:
            print(f"MISSING   {pkg}: tools/{pkg}/ does not exist — NOT counted, "
                  f"NOT an improvement (baseline {baseline.get(pkg)!r} retained)")
    for pkg, b, n in improvements:
        print(f"IMPROVED  {pkg}: {b} → {n} qou-referencing files "
              f"(run --update-baseline to ratchet)")
    for pkg, b, n in regressions:
        print(f"REGRESSED {pkg}: {b} → {n} qou-referencing files — "
              f"new QOU references entering an extraction-bound package")

    if not regressions:
        n_eval = len(counts) - len(missing)
        print(f"wall gate OK: no new qou references "
              f"({sum(v for v in counts.values() if v != MISSING)} files total, "
              f"ratchet only goes down)")
        print(f"  scope: {n_eval} of {len(PACKAGES)} declared package(s) "
              f"evaluated" + (f"; {len(missing)} absent" if missing else ""))
        return 0
    print(f"wall gate: {len(regressions)} package(s) regressed "
          f"({'FAIL --strict' if strict else 'warn-only'})")
    return 1 if strict else 0


if __name__ == "__main__":
    sys.exit(main())
