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

# ---------------------------------------------------------------------------
# GENERALISED 2026-08-30: `_path_bridge` is one SPELLING of the defect, not the
# defect. The class is "a bare-name import that only the bootstrap can resolve,
# placed before the bootstrap". Measured the same day: this audit reported 0
# while SEVEN scripts were broken exactly that way --
#
#   from q_parameter import Q_50_DIGIT_STR          (x3)
#   from substrate.q_parameter import ...           (x2)
#   from _precision import set_compute_dps          (x1)
#   from canonical_braid_crossings import CTYPES    (x1)
#
# -- three of them with the bootstrap present but LATER in the file. They were
# found by `producer_importability_audit`, which decides by importing rather
# than by pattern; this audit's own pattern could not see them. Entry 17 for
# docs/audits/2026-08-15-detector-blindness-taxonomy.md, and the same shape as
# the 28-vs-6 error above: one unknown spelling, a confidently wrong count.
#
# The importable-name set is DERIVED from the tree rather than hardcoded, so it
# cannot go stale the way a literal list would. `_bare_names()` collects every
# module a bootstrapped script can reach by bare name: the `.py` stems directly
# under computations/, the stems in every cluster subdir, and the subdir names
# themselves (for the `from substrate.q_parameter import ...` package form).
# ---------------------------------------------------------------------------
BARE_IMPORT_RE = re.compile(
    r"^\s*(?:from\s+(?P<f>[A-Za-z_][A-Za-z0-9_]*)(?:\.[A-Za-z0-9_.]+)?\s+import\b"
    r"|import\s+(?P<i>[A-Za-z_][A-Za-z0-9_]*)\s*(?:$|#|,))"
)
_MISSING_RE = re.compile(r"No module named '([A-Za-z_][A-Za-z0-9_]*)'")


def _bare_names() -> set[str]:
    """Modules a bootstrapped computations/ script can import by bare name."""
    names: set[str] = set()
    for fn in os.listdir(ROOT):
        full = os.path.join(ROOT, fn)
        if fn.endswith(".py"):
            names.add(fn[:-3])
        elif os.path.isdir(full) and fn not in SKIP_DIRS and not fn.startswith("."):
            names.add(fn)
            for sub in os.listdir(full):
                if sub.endswith(".py"):
                    names.add(sub[:-3])
    names.discard("__init__")
    return names


BARE = _bare_names()


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

            # the generalised form: any bare-name import of an in-repo module
            # that is NOT a sibling of this script (a sibling resolves via
            # sys.path[0] with no bootstrap at all, so it is never a defect)
            here = {f[:-3] for f in files if f.endswith(".py")}
            for i, line in enumerate(lines):
                m = BARE_IMPORT_RE.match(line)
                if not m:
                    continue
                mod = m.group("f") or m.group("i")
                if mod in BARE and mod not in here:
                    idx.append(i)

            if not idx:
                continue
            if not PATH_MUT.search("\n".join(lines[:min(idx)])):
                out.append(p)
    return out


#: A script that gets past its imports is not broken, and `really_broken`
#: already reads a timeout as "not broken" -- the safe direction. Imports
#: resolve in well under this, so a shorter budget costs nothing in accuracy
#: and is what makes the pre-commit hook usable: at 120 s a five-candidate
#: sweep of compute-heavy probes ran past two minutes.
RUN_TIMEOUT = 25


def really_broken(path: str, timeout: int = RUN_TIMEOUT) -> bool:
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
    out = r.stdout + r.stderr
    if MISSING in out:
        return True
    # generalised: the interpreter could not find an in-repo module, i.e. the
    # bootstrap that would have made it reachable did not run first. A missing
    # THIRD-PARTY package (snappy, matplotlib) is an environment fact and is
    # deliberately not this audit's business.
    return any(m in BARE for m in _MISSING_RE.findall(out))


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    only = None
    if argv and argv[0] == "--files":
        # Scope to specific paths, for the pre-commit hook: checking the files
        # a commit touches is near-instant, where a whole-tree sweep is not.
        only = {os.path.abspath(a) for a in argv[1:]}
        if not only:
            return 0
    cands = candidates()
    if only is not None:
        cands = [c for c in cands if os.path.abspath(c) in only]
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
        print("\n  Fix: move the import AFTER a sys.path insert of the parent")
        print("  directory, per _path_bridge's documented USAGE. This covers any")
        print("  bare-name import of an in-repo module, not only _path_bridge.")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
