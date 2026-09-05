#!/usr/bin/env python3
"""Compile every stale library module from source and report which are red.

## Why

`scripts/lean-content-sweep.sh` covers content-block `.lean` siblings.  It does
NOT cover the package's own library tree (`content/*/lean/QOU/**`), and that
population has the same exposure: a module verified `lean`-direct against the
restored olean snapshot is verified against a *snapshot*, so a dependency whose
source moved afterwards leaves it green and broken at once.

Measured instance (bean `qou-56qy`, found by a sibling session):
`QOU/QBeta/FiveTwoCuspShapeBarParity.lean` recorded `exit 0` while its one QOU
dependency `BarParityZeta4Swap` had an olean 20 days older than its source.

That file is invisible to any drift count keyed on *changed sources*, because it
is **new** — it inherits its dependency's staleness without having changed
itself.  So the population to sweep is not "modules that changed" but the
**dirty closure**: every module that changed, has no olean at all, or transitively
imports one that did.

## What it does

1. Computes the dirty closure over the whole library, per module — each olean's
   own mtime against its own source's last commit date.  (Source mtimes are
   useless: a fresh clone stamps every file with the checkout time.)
2. Rebuilds the closure from source, in topological order, into a shadow tree
   placed first on `LEAN_PATH`.
3. **Continues past a failure**, marking that module's dependents `skipped`
   rather than aborting — one break must not mask the rest, which is the whole
   point of a sweep.

`lake` is never invoked, so the restored cache cannot be evicted.  Mathlib is
never rebuilt.

## Usage

    scripts/lean-library-sweep.py [--shadow DIR] [--jobs N] [--limit N]

`--shadow` reuses a shadow across runs (~2.3 GB, and the copy is the slow part).
`--jobs` parallelises independent modules within a topological layer.
"""

from __future__ import annotations

import argparse
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor

# The lakefile's [leanOptions] are NOT applied by a bare `lean` invocation, and
# the difference is not cosmetic: `autoImplicit` defaults to TRUE in `lean` and
# is set FALSE here, so bare lean-direct silently auto-binds unbound identifiers
# that Lake correctly rejects.  Measured 2026-09-05 on
# QOU/MassTheory/AtomWordShadow.lean, same file and same LEAN_PATH:
#     lean                        -> exit 0, 0 errors
#     lean -DautoImplicit=false   -> exit 1, 6 errors
# `-s 65536` mirrors the paper lakefile's `moreLeanArgs` (one generated module
# overflows the default elaboration stack and aborts with a bare exit 134).
LEAN_OPTS = ["-DautoImplicit=false", "-s", "65536"]

ROOT = pathlib.Path(
    subprocess.run(["git", "rev-parse", "--show-toplevel"],
                   capture_output=True, text=True, check=True).stdout.strip())
PKG = ROOT / "content/quantum-observable-universe/lean"   # default; see packages()
LIB = "QOU"


def packages() -> list[tuple[pathlib.Path, str]]:
    """Every paper package: (lean dir, library name).

    Discovered, not hardcoded — a package is a `content/*/lean/` holding a
    lakefile and a top-level `<Lib>.lean` root module whose stem names the
    library (`QOU`, `UGB`, `Fred2005`).  Sweeping only the first of the three
    was the gap this closes: UGB and Fred2005 were covered by nothing.
    """
    out = []
    for lakefile in sorted(ROOT.glob("content/*/lean/lakefile.toml")):
        d = lakefile.parent
        for root_mod in sorted(d.glob("*.lean")):
            if (d / root_mod.stem).is_dir():
                out.append((d, root_mod.stem))
    return out


def find_oleans() -> pathlib.Path:
    """The restore seeds the ROOT workspace; a per-paper `lake build` seeds $PKG.

    Both are real, so probe rather than assume — hardcoding either one makes the
    script fail on exactly the tree it exists to verify against.
    """
    env = os.environ.get("OLEANS")
    cands = [pathlib.Path(env)] if env else [
        PKG / ".lake/build/lib/lean", ROOT / ".lake/build/lib/lean"]
    for c in cands:
        if (c / LIB).is_dir():
            return c
    sys.exit(f"no olean tree with a {LIB}/ dir; looked in: "
             f"{', '.join(str(c) for c in cands)}")


def load_graph() -> tuple[dict, dict]:
    mod2path = {str(p.relative_to(PKG).with_suffix("")).replace("/", "."): p
                for p in PKG.glob(f"{LIB}/**/*.lean")}
    imports = {}
    for m, p in mod2path.items():
        imports[m] = [i for i in re.findall(r"^import\s+(\S+)", p.read_text(), re.M)
                      if i in mod2path]
    return mod2path, imports


def last_commit_times() -> dict[str, int]:
    """Repo-relative path -> unix time of its most recent commit, in one pass."""
    out = subprocess.run(
        ["git", "log", "--format=%ct", "--name-only", "--", str(PKG / LIB)],
        cwd=ROOT, capture_output=True, text=True).stdout
    times, ts = {}, None
    for line in out.splitlines():
        if not line:
            continue
        if line.isdigit():
            ts = int(line)
        elif line.endswith(".lean"):
            times.setdefault(line, ts)      # newest-first, so first wins
    return times


def dirty_closure(mod2path, imports, oleans):
    times = last_commit_times()
    changed, never_built = set(), set()
    for m, p in mod2path.items():
        o = oleans / (m.replace(".", "/") + ".olean")
        if not o.exists():
            changed.add(m)
            never_built.add(m)
            continue
        c = times.get(str(p.relative_to(ROOT)))
        if c is None or c > o.stat().st_mtime:
            changed.add(m)

    sys.setrecursionlimit(100000)
    dirty, clean = set(), set()

    def is_dirty(m):
        if m in dirty:
            return True
        if m in clean:
            return False
        if m in changed or any(is_dirty(d) for d in imports[m]):
            dirty.add(m)
            return True
        clean.add(m)
        return False

    for m in mod2path:
        is_dirty(m)
    return dirty, changed, never_built


def layers(need, imports):
    """Topological layers: everything in a layer is independent of its peers."""
    out, done = [], set()
    remaining = set(need)
    while remaining:
        layer = sorted(m for m in remaining
                       if all(d in done or d not in need for d in imports[m]))
        if not layer:
            sys.exit(f"import cycle among {len(remaining)} modules")
        out.append(layer)
        done |= set(layer)
        remaining -= set(layer)
    return out


def lib_slug() -> str:
    return LIB.lower()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--shadow")
    ap.add_argument("--jobs", type=int, default=3)
    ap.add_argument("--limit", type=int, default=0,
                    help="stop after N modules (for a smoke test)")
    ap.add_argument("--package", action="append", metavar="LIB",
                    help="library name (QOU, UGB, Fred2005); repeatable, "
                         "default all discovered")
    args = ap.parse_args()

    global PKG, LIB
    todo_pkgs = packages()
    if args.package:
        want = set(args.package)
        todo_pkgs = [(d, l) for d, l in todo_pkgs if l in want]
        missing = want - {l for _, l in todo_pkgs}
        if missing:
            sys.exit(f"unknown package(s): {', '.join(sorted(missing))}; "
                     f"have {', '.join(l for _, l in packages())}")
    if not todo_pkgs:
        sys.exit("no paper packages discovered under content/*/lean/")

    rc = 0
    for i, (pkg_dir, lib) in enumerate(todo_pkgs):
        if i:
            print()
        print(f"########## {lib}  ({pkg_dir.relative_to(ROOT)})")
        PKG, LIB = pkg_dir, lib
        rc |= sweep_one(args)
    return rc


def sweep_one(args) -> int:
    oleans = find_oleans()
    print(f"olean tree: {oleans}")
    mod2path, imports = load_graph()
    dirty, changed, never_built = dirty_closure(mod2path, imports, oleans)

    print(f"library modules        {len(mod2path)}")
    print(f"  source-changed        {len(changed) - len(never_built)}")
    print(f"  never built (new)     {len(never_built)}")
    print(f"  DIRTY CLOSURE         {len(dirty)}")
    print(f"  snapshot-current      {len(mod2path) - len(dirty)}")
    if not dirty:
        print("nothing to sweep")
        return 0

    keep = bool(args.shadow)
    # Per-library subdirectory: LEAN_PATH resolves a module from the first root
    # holding that package dir, so two libraries must not share one shadow root.
    shadow = (pathlib.Path(args.shadow) / lib_slug() if keep
              else pathlib.Path(tempfile.mkdtemp()))
    shadow.mkdir(parents=True, exist_ok=True)
    try:
        if not (shadow / LIB).is_dir():
            # The shadow MUST contain the whole library tree, not just the
            # modules we rebuild.  Lean commits to the FIRST LEAN_PATH root that
            # holds the module's top-level namespace directory and never
            # consults a later root for anything under it -- measured three
            # ways: a shadow with no `<LIB>/` falls through and exits 0; a
            # shadow with `<LIB>/` holding one unrelated module fails with
            # "does not exist" on every other import from it.  So a partial
            # shadow MASKS the real tree rather than layering over it, which is
            # also why two libraries must not share one shadow root (above).
            # Bean `qou-tpdg`.
            #
            # Hardlink rather than copy.  The tree is ~2.3 GB and a container
            # here has a per-session quota (AGENTS.md §Disk space); a real copy
            # simply fails with ENOSPC, which is what blocked this sweep from
            # running at all.  Hardlinks cost ~0 (`du` reports 2.3 GB while
            # `df` does not move) and are safe because `build()` unlinks its
            # target before writing, so a rebuild never writes through a shared
            # inode into the real tree.
            print(f"linking {LIB} olean tree into shadow ({shadow}) ...")
            try:
                shutil.copytree(oleans / LIB, shadow / LIB, copy_function=os.link)
            except OSError as e:
                # different filesystem, or a hardlink-hostile mount
                print(f"  hardlink failed ({e}); falling back to a real copy")
                shutil.rmtree(shadow / LIB, ignore_errors=True)
                shutil.copytree(oleans / LIB, shadow / LIB)

        siblings = [str(p) for p in ROOT.glob("content/*/lean/.lake/build/lib/lean")
                    if p != oleans]
        # Dependency olean roots, in the order Lean should search them.
        #
        # BOTH package locations are included deliberately.  The root Lake
        # workspace has `.lake/packages/`, and each paper package has its own
        # `<paper>/lean/.lake/packages/` — and the documented sandbox restore
        # (AGENTS.md §"Mathlib cache 403 fallback") populates the PAPER one.
        # Globbing only the root gave a tree with a 0-byte `Mathlib/Tactic.olean`
        # and no `Mathlib/Data/Real/Basic.olean` at all (1212 oleans against the
        # paper tree's 3477), so every Mathlib-importing module failed with
        # "invalid header" / "does not exist" and the sweep reported 22 REDs
        # that were entirely about its own environment.  Bean `qou-tpdg`.
        pkg_roots = ([str(p) for p in ROOT.glob("content/*/lean/.lake/packages/*/.lake/build/lib/lean")]
                     + [str(p) for p in ROOT.glob(".lake/packages/*/.lake/build/lib/lean")])
        lean_path = ":".join([str(shadow)] + pkg_roots + siblings + [str(oleans)])
        env = dict(os.environ,
                   LEAN_PATH=lean_path,
                   PATH=f"{os.path.expanduser('~')}/.elan/bin:{os.environ['PATH']}")

        order = layers(dirty, imports)
        todo = list(dirty)
        if args.limit:
            todo = [m for layer in order for m in layer][:args.limit]
            todo_set = set(todo)
            order = [[m for m in layer if m in todo_set] for layer in order]
            order = [l for l in order if l]

        red, skipped, ok = {}, {}, 0
        broken = set()
        t0 = time.time()
        n = sum(len(l) for l in order)
        done_ct = 0

        def build(m: str):
            src = PKG / (m.replace(".", "/") + ".lean")
            out = shadow / (m.replace(".", "/") + ".olean")
            out.parent.mkdir(parents=True, exist_ok=True)
            # The shadow is hardlinked to the real tree, so REMOVE the target
            # before `lean -o` writes it.  Writing through a shared inode would
            # mutate the real olean tree -- the thing the shadow exists to
            # prevent.  Also drop same-stem siblings that would then be stale.
            for stale in (out, out.with_suffix(".olean.hash"), out.with_suffix(".ilean")):
                try:
                    stale.unlink()
                except (FileNotFoundError, IsADirectoryError):
                    pass
            r = subprocess.run(["lean", *LEAN_OPTS, str(src.relative_to(PKG)), "-o", str(out)],
                               cwd=PKG, env=env, capture_output=True, text=True,
                               timeout=1800)
            return m, r.returncode, (r.stdout + r.stderr)

        for layer in order:
            # A module whose dependency is red cannot be judged; say so rather
            # than reporting a cascade of derived failures as findings.
            runnable = [m for m in layer
                        if not any(d in broken for d in imports[m])]
            for m in layer:
                if m not in runnable:
                    skipped[m] = sorted(d for d in imports[m] if d in broken)
                    broken.add(m)
            if not runnable:
                continue
            with ThreadPoolExecutor(max_workers=args.jobs) as ex:
                for m, rc, log in ex.map(build, runnable):
                    done_ct += 1
                    if rc == 0:
                        ok += 1
                        print(f"  [{done_ct}/{n}] ok   {m}", flush=True)
                    else:
                        errs = [l for l in log.splitlines() if ": error:" in l]
                        red[m] = errs[:5]
                        broken.add(m)
                        print(f"  [{done_ct}/{n}] RED  {m}", flush=True)
                        for e in errs[:3]:
                            print(f"        {e}", flush=True)

        print(f"\n=== library sweep: {ok} ok, {len(red)} RED, "
              f"{len(skipped)} skipped (dependency red), "
              f"{time.time() - t0:.0f}s ===")
        for m, errs in sorted(red.items()):
            print(f"\nRED {m}")
            for e in errs:
                print(f"    {e}")
        for m, deps in sorted(skipped.items()):
            print(f"SKIPPED {m}  (red dependency: {', '.join(deps)})")
        if keep:
            print(f"\nshadow kept at {shadow}")
        return 1 if red else 0
    finally:
        if not keep:
            shutil.rmtree(shadow, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
