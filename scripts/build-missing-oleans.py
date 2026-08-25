#!/usr/bin/env python3
"""Build only the Mathlib oleans missing from a restored lake-cache set.

WHY THIS EXISTS
---------------
`lake-cache/qou-<toolchain-slug>` carries a *partial* Mathlib olean set — the
import cone QOU needed when that branch was seeded, not all 6990 modules. A file
importing outside that cone fails with

    error: object file '.../Mathlib/Foo/Bar.olean' of module Mathlib.Foo.Bar
    does not exist

That is a **cache gap, not a defect in the file under test**. Do not report the
file as failing to compile, and do not go looking for a bad import — check
whether the named module is a *Mathlib* module first. If it is, run this.

The naive alternative — `lake build <Module>` — re-resolves the dependency graph
and rebuilds Mathlib from source (~3000 modules through `import Mathlib.Tactic`)
*and* wipes the restored oleans. This script instead walks the import graph from
one target, builds bottom-up only what is absent, and leaves everything present
untouched.

MEASURED: closing the gap that blocked `QOU/MathlibExt/EndBaseChange.lean`
(`Mathlib.Algebra.Module.LinearMap.Polynomial`) took **13 modules, 0 failures**,
against 46 of its cone already present. Minutes, not the 40-minute `lake build`
storm.

PREREQUISITE — Mathlib sources
------------------------------
The cache ships oleans only; `.lake/packages/mathlib/Mathlib/` does not exist,
so restoring the cache cannot fill its own holes. Clone the sources at the rev
pinned in the root `lakefile.toml` (github.com egress is available):

    REV=$(grep -A3 '"mathlib"' lakefile.toml | grep 'rev' | cut -d'"' -f2)
    mkdir -p ~/mathlib-src && cd ~/mathlib-src
    git init -q && git remote add origin https://github.com/leanprover-community/mathlib4
    git fetch --depth 1 origin $REV && git checkout -q FETCH_HEAD

Do NOT symlink that tree into `.lake/packages/mathlib/Mathlib` — `lean` rejects
an input file that resolves outside the root directory. This script invokes the
toolchain binary by absolute path from a common parent instead, which also
sidesteps the elan per-directory override (running `lean` from outside the repo
otherwise fails with "no default toolchain configured").

USAGE
-----
    export LEAN_PATH=<the restored build/lib/lean dirs, colon-separated>
    python3 -u scripts/build-missing-oleans.py Mathlib.Algebra.Module.LinearMap.Polynomial

Then verify the file that was blocked with `lean`-direct as usual.

Paths are overridable by env var for non-default layouts:
QOU_MATHLIB_SRC, QOU_OLEAN_OUT, QOU_LEAN_BIN.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys

def _find_src() -> str:
    """Locate the Mathlib source tree.

    Do NOT assume `~/mathlib-src`: these sandboxes run as root, so `~` is
    `/root` while the repo (and any sibling clone) lives under `/home/user`.
    That mismatch made the first version of this script report "sources not
    found" on a machine that had them. Search the plausible spots instead.
    """
    env = os.environ.get("QOU_MATHLIB_SRC")
    if env:
        return env
    repo = os.getcwd()
    for cand in (
        os.path.join(os.path.dirname(repo), "mathlib-src"),
        os.path.join(os.path.dirname(repo), "mathlib4"),  # AGENTS.md local clone
        os.path.expanduser("~/mathlib-src"),
        "/home/user/mathlib-src",
        os.path.join(repo, ".lake/packages/mathlib"),      # if sources present
    ):
        if os.path.isdir(os.path.join(cand, "Mathlib")):
            return cand
    return os.path.join(os.path.dirname(repo), "mathlib-src")  # for the error msg


SRC = _find_src()
OUT = os.environ.get(
    "QOU_OLEAN_OUT",
    os.path.join(os.getcwd(), ".lake/packages/mathlib/.lake/build/lib/lean"),
)
LEAN = os.environ.get("QOU_LEAN_BIN", "")

IMPORT_RE = re.compile(r"^import\s+([A-Za-z0-9_.]+)", re.M)


def find_lean_bin() -> str:
    if LEAN:
        return LEAN
    import glob
    cands = sorted(glob.glob(os.path.expanduser("~/.elan/toolchains/*/bin/lean")))
    if not cands:
        sys.exit("no lean binary found under ~/.elan/toolchains/*/bin/lean; "
                 "set QOU_LEAN_BIN")
    return cands[0]


def main() -> int:
    if len(sys.argv) < 2:
        sys.exit(f"usage: {sys.argv[0]} <Mathlib.Module.Name> [...]")
    if not os.path.isdir(SRC):
        sys.exit(f"Mathlib sources not found at {SRC} — see the docstring for "
                 f"the clone recipe (they are NOT in the olean cache).")
    if not os.environ.get("LEAN_PATH"):
        print("WARNING: LEAN_PATH is unset; builds will almost certainly fail.\n",
              file=sys.stderr)

    lean_bin = find_lean_bin()
    built: list[str] = []
    failed: list[tuple[str, str]] = []
    present = 0
    visiting: set[str] = set()

    def olean_path(mod: str) -> str:
        return os.path.join(OUT, mod.replace(".", "/") + ".olean")

    def src_path(mod: str) -> str:
        return os.path.join(SRC, mod.replace(".", "/") + ".lean")

    def ensure(mod: str) -> bool:
        nonlocal present
        # Only Mathlib is cached partially; batteries/aesop/Qq ship complete.
        if not mod.startswith("Mathlib"):
            return True
        op = olean_path(mod)
        if os.path.exists(op):
            present += 1
            return True
        if mod in visiting:
            return True
        visiting.add(mod)
        sp = src_path(mod)
        if not os.path.exists(sp):
            failed.append((mod, "no source at the pinned rev"))
            return False
        with open(sp, encoding="utf-8", errors="replace") as fh:
            for dep in IMPORT_RE.findall(fh.read()):
                ensure(dep)
        os.makedirs(os.path.dirname(op), exist_ok=True)
        # cwd is a common parent of both trees so `lean` accepts the input path.
        common = os.path.commonpath([os.path.abspath(SRC), os.path.abspath(OUT)])
        r = subprocess.run([lean_bin, sp, "-o", op], capture_output=True,
                           text=True, cwd=common, timeout=3600)
        if r.returncode != 0:
            failed.append((mod, (r.stdout + r.stderr)[:400]))
            print(f"  FAIL  {mod}", flush=True)
            return False
        built.append(mod)
        print(f"  built [{len(built)}] {mod}", flush=True)
        return True

    ok = True
    for target in sys.argv[1:]:
        print(f"target: {target}")
        ok = ensure(target) and ok

    print(f"\nbuilt={len(built)}  already-present={present}  "
          f"failed={len(failed)}  ok={ok}")
    for mod, err in failed[:10]:
        first = err.splitlines()[0] if err else ""
        print(f"  FAILED {mod}: {first}")
    return 0 if ok and not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
