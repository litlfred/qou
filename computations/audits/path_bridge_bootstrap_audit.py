#!/usr/bin/env python3
"""Which `computations/` scripts cannot import `_path_bridge` standalone?

`_path_bridge` lives in `computations/`.  A script in a cluster subdirectory
(`qbeta/`, `deltalambda/`, `probes/`, ...) has `sys.path[0]` set to its OWN
directory, so `import _path_bridge` resolves ONLY if something has already put
`computations/` on the path.  Its own docstring specifies the bootstrap:

    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    import _path_bridge          # <- AFTER, never before

Get that order wrong and the script cannot be run at all.  The failure is
SILENT in normal agent use, because a caller that has already set PYTHONPATH
(or that imports the script rather than executing it) masks it completely --
which is exactly how six of these reached main.

WHY THIS SCRIPT RUNS ITS CANDIDATES INSTEAD OF TRUSTING THE PATTERN
------------------------------------------------------------------
The first version of this audit pattern-matched only `sys.path.insert(` and
reported **28** broken files.  Sampling three of them by hand showed all three
ran fine: they bootstrap with `sys.path[:0] = [...]`, a spelling the regex did
not know.  The true count is **6**.  That is a 22-file false-positive rate from
one missing spelling, and it is the same detector-blindness class catalogued in
`docs/audits/2026-08-15-detector-blindness-taxonomy.md`.

So the pattern match here is used ONLY to narrow the field to candidates; every
candidate is then actually EXECUTED and judged on whether the interpreter
really raises `ModuleNotFoundError: No module named '_path_bridge'`.  A scan
proposes; a run decides.

Exit 0 when nothing is broken, 1 otherwise.

-- Ref: [manuscript] computations/_path_bridge.py (the documented bootstrap)
-- Ref: [manuscript] docs/audits/2026-08-15-detector-blindness-taxonomy.md
"""
from __future__ import annotations

import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {"_deprecated", "__pycache__", "data"}

#: every spelling that puts something on sys.path. Deliberately broad --
#: a false NEGATIVE here costs a wasted subprocess, a false POSITIVE
#: (missing a spelling) is what produced the 28-vs-6 error.
PATH_MUT = re.compile(
    r"sys\.path\s*(?:\[[^\]]*\]\s*=|\.insert\(|\.append\(|\.extend\(|\+=)"
)
IMPORT_RE = re.compile(r"\s*import\s+_path_bridge\b")
MISSING = "No module named '_path_bridge'"


def candidates() -> list[str]:
    """Narrow the field: subdir scripts importing _path_bridge with no
    preceding sys.path mutation. Proposals only -- never a verdict."""
    out = []
    for root, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs
                   if d not in SKIP_DIRS and not d.startswith(".")]
        # a script directly in computations/ has _path_bridge as a sibling,
        # so sys.path[0] already resolves it -- never a candidate.
        if os.path.normpath(root) == os.path.normpath(ROOT):
            continue
        for fn in sorted(files):
            if not fn.endswith(".py"):
                continue
            p = os.path.join(root, fn)
            try:
                src = open(p, encoding="utf-8", errors="replace").read()
            except OSError:
                continue
            lines = src.split("\n")
            idx = [i for i, l in enumerate(lines) if IMPORT_RE.match(l)]
            if not idx:
                continue
            if not PATH_MUT.search("\n".join(lines[:idx[0]])):
                out.append(p)
    return out


def really_broken(path: str, timeout: int = 120) -> bool:
    """Execute it. The interpreter is the authority, not the regex."""
    env = dict(os.environ)
    # strip any inherited path help -- that masking is the whole bug
    env.pop("PYTHONPATH", None)
    try:
        r = subprocess.run([sys.executable, path], capture_output=True,
                           text=True, timeout=timeout, env=env, cwd=ROOT)
    except subprocess.TimeoutExpired:
        # got far enough to do real work => the import succeeded
        return False
    return MISSING in (r.stdout + r.stderr)


def main() -> int:
    cands = candidates()
    print("=" * 70)
    print(" _path_bridge bootstrap-order audit")
    print("=" * 70)
    print(f"  candidates (pattern)      : {len(cands)}")
    broken = [p for p in cands if really_broken(p)]
    print(f"  CONFIRMED broken (by run) : {len(broken)}")
    if len(cands) != len(broken):
        print(f"  pattern false positives   : {len(cands) - len(broken)}"
              "   <- why this audit executes rather than greps")
    for p in broken:
        print(f"    - {os.path.relpath(p, ROOT)}")
    if broken:
        print("\n  Fix: move `import _path_bridge` AFTER a sys.path insert of")
        print("  the parent directory, per _path_bridge's documented USAGE.")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
