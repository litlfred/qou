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
   own mtime against the LATER of its source's last commit date and the source's
   on-disk mtime.  Commit date alone is unsound in the narrow direction: after a
   fetch+rebase the content arrives long after its commit date, so an olean built
   in between reads as fresh (worked case in `dirty_closure`).  Source mtime alone
   is unsound in the wide direction on a fresh clone.  The max() is safe: it can
   only over-sweep.
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
import threading
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
    # `{LIB}/**/*.lean` does NOT match the library ROOT file `{LIB}.lean`, which
    # sits one level up -- so the root module was outside the sweep's population
    # entirely, under either freshness rule.  Live instance: main's `545efd2c521`
    # added `import QOU.Mass.CrossTermOrderZeroComponentCount` to `QOU.lean`, the
    # 883-import root, and NOTHING in this repo checked that file.  Glob both.
    mod2path = {str(p.relative_to(PKG).with_suffix("")).replace("/", "."): p
                for p in [*PKG.glob(f"{LIB}/**/*.lean"), *PKG.glob(f"{LIB}.lean")]}
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


def _standard_dirty(mod2path, oleans, times, never_built):
    """Modules the SNAPSHOT cannot vouch for: no olean, or source newer than it.

    Separate from the --all population on purpose.  A dep of a --only chunk is
    fine to take from the snapshot when the snapshot is current for it; it is
    NOT fine when the snapshot predates a declaration the dependent needs.
    MEASURED instance, and it nearly went out as a corpus defect against main:
    `QOU.IwahoriHecke.BruhatReflection` failed with `Unknown identifier
    bruhatLe_inv_iff`.  That lemma exists, in an imported module, in an opened
    namespace -- and was added 2026-09-07 07:04 (`8ca51eb3ddc`) while the
    snapshot olean for `QOU.Machinery.CoxeterBruhat` dates from 2026-09-06
    07:04.  `strings` on that olean finds the symbol 0 times.  So the module is
    fine and the slice was wrong.
    """
    out = set(never_built)
    for m, p_ in mod2path.items():
        if m in out:
            continue
        o = oleans / (m.replace(".", "/") + ".olean")
        c = times.get(str(p_.relative_to(ROOT)))
        src = max(c, p_.stat().st_mtime) if c is not None else None
        if src is None or src > o.stat().st_mtime:
            out.add(m)
    return out


def dirty_closure(mod2path, imports, oleans, all_dirty=False):
    """Modules to compile.  With `all_dirty`, that is EVERY module.

    The freshness rule below decides which modules the *snapshot* cannot vouch
    for.  It is the right population for a gate run per-branch.  It is the wrong
    population for one question: **how much of the library actually compiles at
    all.**  A module the restored cache built weeks ago is "clean" here and has
    still never been checked against today's source by anything in this repo --
    `lake build QOU` reaches only the root's import closure, which is 910 of 2773
    modules (`scripts/lean-root-coverage-audit.py`), so the other 1863 are outside
    every routine build.  `--all` is for measuring that population; do not make it
    the default, because it costs hours where the closure costs minutes.
    """
    times = last_commit_times()
    changed, never_built = set(), set()
    if all_dirty:
        # --all says "verify every module"; it does NOT say every olean is wrong.
        # Those are different facts and --only needs the second one, so compute
        # the standard freshness verdict too and hand it back as `untrusted`.
        for m, p_ in mod2path.items():
            if not (oleans / (m.replace(".", "/") + ".olean")).exists():
                never_built.add(m)
        untrusted = _standard_dirty(mod2path, oleans, times, never_built)
        return set(mod2path), set(mod2path), never_built, untrusted
    for m, p in mod2path.items():
        o = oleans / (m.replace(".", "/") + ".olean")
        if not o.exists():
            changed.add(m)
            never_built.add(m)
            continue
        c = times.get(str(p.relative_to(ROOT)))
        # Take the LATER of the source's last-commit date and its on-disk mtime.
        #
        # Commit date alone is UNSOUND, and the hole is the normal case after a
        # fetch+rebase: a commit dated 06:36 UTC arrives in this tree at 08:0x,
        # and an olean built at 07:24 -- from the OLD content -- is then "newer
        # than the commit" and judged clean.
        #
        # The ordering is real and routine -- upstream commit 06:36 UTC, local olean
        # 07:24 built from the tree BEFORE that commit arrived, content arriving at
        # 08:0x on fetch+rebase -- but NO instance of it is currently reachable by
        # this sweep, and the case that looked like one is not: `QOU.lean` has
        # exactly that ordering, and it was missed because the module ENUMERATION
        # excluded the library root (see `load_graph`), not because of this rule.
        # So this is cheap insurance in the safe direction, not a fix for an
        # observed miss -- do not cite it as the latter.
        #
        # The corollary that makes instances rare: if a module's last commit
        # PREDATES its olean and no later commit touched it, the on-disk content IS
        # what the olean was built from, so it is genuinely clean and a newer mtime
        # is churn (branch switching rewrites the mtime of every differing file).
        # Only content arriving out of commit-date order -- a fetch of upstream
        # commits dated before your last local build -- opens the hole.
        #
        # The docstring's objection to mtimes -- "a fresh clone stamps every file
        # with the checkout time" -- is a statement about COST, not correctness:
        # it makes the closure too WIDE there, never too narrow.  Wide is the safe
        # direction for a gate; narrow is the defect.  Measured on this container
        # the max() widens the root-dirty set 12 -> 80 of 2712 and the QOU closure
        # 16 -> 201, i.e. 311 s rather than 32 s -- minutes, not hours.
        #
        # NOT sound in the other direction either: branch switching rewrites the
        # mtime of every file that differs, so some of that widening is churn on
        # content the olean was in fact built from.  A content hash recorded beside
        # each olean would decide it exactly; a RESTORED olean carries no such hash,
        # so that is a larger change than this one.
        src = max(c, p.stat().st_mtime) if c is not None else None
        if src is None or src > o.stat().st_mtime:
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
    return dirty, changed, never_built, _standard_dirty(mod2path, oleans, times, never_built)


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
    ap.add_argument("--timeout", type=int, default=1800,
                    help="per-module seconds; on expiry the module is reported "
                         "TIMEOUT (unverified) and the sweep CONTINUES")
    ap.add_argument("--limit", type=int, default=0,
                    help="stop after N modules (for a smoke test)")
    ap.add_argument("--all", action="store_true",
                    help="compile EVERY module, not just the dirty closure -- the "
                         "measurement for 'how much of the library compiles', since "
                         "1863 of 2773 are outside the root build and so outside "
                         "every routine check.  Hours, not minutes.")
    ap.add_argument("--only", metavar="PREFIX",
                    help="restrict to modules whose name starts with PREFIX "
                         "(e.g. QOU.BraidKnot).  Exists so a --all run can be "
                         "CHUNKED: the shadow's newly-written oleans are the only "
                         "real bytes it costs (0.22 MB/module), so a full run needs "
                         "~610 MB at once, and reclaiming the shadow between chunks "
                         "is what makes it fit a container at 99%.  NOTE this "
                         "weakens the run slightly: modules in a later chunk resolve "
                         "their earlier-chunk imports against the SNAPSHOT olean "
                         "rather than one this run rebuilt.  That is the same "
                         "snapshot-conditionality the sweep already carries for "
                         "clean dependencies -- not a new hole -- but it means a "
                         "chunked green is not identical to a single-run green.")
    ap.add_argument("--only-exact", metavar="MODULE",
                    help="like --only but matches ONE module exactly.  Needed for "
                         "the library root: `--only QOU` is a prefix and EVERY "
                         "module starts with it, so the root's chunk silently "
                         "became the whole corpus (measured: `TO COMPILE 2774 "
                         "[--only QOU + its untrusted deps]`).")
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
    dirty, changed, never_built, untrusted = dirty_closure(mod2path, imports,
                                                oleans, all_dirty=args.all)
    sel = args.only or args.only_exact
    if sel:
        # Filter the population to compile, NOT the import graph -- dependencies
        # outside the selection must stay resolvable.
        if args.only_exact:
            seeds = {m for m in dirty if m == args.only_exact}
        else:
            seeds = {m for m in dirty if m.startswith(args.only)}
        if not seeds:
            print(f"  selection {sel}: no modules match; nothing to do")
            return 0
        # ...but a dependency is only "resolvable from the snapshot" if the
        # snapshot HAS it.  A never-built module has no olean at all, so a
        # selection that drops it makes every importer a GUARANTEED spurious
        # RED -- reported as a corpus failure when it is an artifact of how the
        # run was sliced.  MEASURED, not hypothetical: the first chunked run
        # reported `QOU.BraidKnot.DominanceIsBruhat` RED with
        #   error: object file '.../QOU/Machinery/BruhatRankCriterion.olean' ...
        #   of module QOU.Machinery.BruhatRankCriterion does not exist
        # because that dep is one of the 60 never-built modules and sits in a
        # different namespace.  So pull the never-built cone in regardless of
        # prefix.  5 modules corpus-wide need this; 24 of them are dependencies
        # of the library ROOT alone.
        need, stack = set(seeds), list(seeds)
        while stack:
            for d in imports[stack.pop()]:
                if d in untrusted and d not in need:
                    need.add(d); stack.append(d)
        pulled = need - seeds
        if pulled:
            nb = len(pulled & never_built)
            print(f"  selection {sel}: +{len(pulled)} untrusted dep(s) pulled in "
                  f"across namespaces ({nb} never built, {len(pulled) - nb} stale) "
                  f"-- else they are spurious REDs")
        dirty = need

    print(f"library modules        {len(mod2path)}")
    if args.all:
        # Under --all the freshness rule never runs, so `changed` is "everything"
        # by construction.  Printing it as `source-changed` would report a
        # fabricated measurement in the same column a real one normally occupies
        # -- exactly the cannot-verify-vs-fails conflation this sweep exists to
        # avoid.  `never_built` IS measured (olean presence), so it stays.
        print(f"  never built (new)     {len(never_built)}   [measured]")
        print(f"  source-changed        n/a  (--all: freshness rule not consulted)")
        label = "[= every module]" if not sel else f"[{sel} + its untrusted deps]"
        print(f"  TO COMPILE (--all)    {len(dirty)}   {label}")
    else:
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
        # BOTH package locations are included deliberately, PAPER FIRST.  The
        # root Lake workspace has `.lake/packages/` and each paper package has
        # its own `<paper>/lean/.lake/packages/`; the documented sandbox restore
        # (AGENTS.md §"Mathlib cache 403 fallback") fills the PAPER one, so that
        # is the tree it GUARANTEES.
        #
        # The root tree is not reliably broken -- it is not reliably POPULATED,
        # which is worse for a gate.  Measured on two containers: on one, root
        # held a 0-byte `Mathlib/Tactic.olean`, no `Mathlib/Data/Real/Basic.olean`
        # and 1212 oleans, so every Mathlib-importing module failed with
        # "invalid header" / "does not exist" and this sweep reported 22 REDs
        # that were entirely about its own environment.  On another, root was a
        # 6990-olean SUPERSET of the paper tree with both files byte-identical,
        # and the same code was fine.  Globbing the root alone therefore makes
        # this gate correct by luck of environment.  Bean `qou-tpdg`.
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

        red, skipped, timed_out, unverified, ok = {}, {}, {}, {}, 0
        broken = set()
        t0 = time.time()
        n = sum(len(l) for l in order)
        done_ct = 0

        def build(m: str):
            src = PKG / (m.replace(".", "/") + ".lean")
            out = shadow / (m.replace(".", "/") + ".olean")
            out.parent.mkdir(parents=True, exist_ok=True)
            # The shadow is hardlinked to the real tree, so the target must not be
            # written THROUGH: that would mutate the real olean tree, which is the
            # one thing the shadow exists to prevent.
            #
            # Write to a private temp path and `os.replace` it into place.  Do NOT
            # unlink first, which is what this did and which is a RACE, MEASURED
            # 2026-09-08:
            #   [292/383] ok           QOU.Mathlib.SchenstedStandardTableau
            #   [293/383] UNVERIFIED   QOU.Mathlib.SkewSYTBranchingBijection
            #                          (missing olean QOU.Mathlib.SchenstedStandardTableau)
            # The dependency built fine and its dependent could not find it, one
            # line apart.  `layers()` orders on DIRECT imports, but Lean loads the
            # whole TRANSITIVE closure, so two modules can share a layer while one
            # needs the other's olean -- and with --jobs 3 the reader then hits the
            # window between unlink and write.  `os.replace` is atomic: a concurrent
            # reader sees the old hardlinked olean or the new one, never absence.
            # It also breaks the hardlink (a fresh inode is moved into the name), so
            # the real tree stays protected exactly as before.
            #
            # The failure was SAFE -- it understated coverage rather than inventing
            # a defect, and the honest UNVERIFIED label is what made it findable.
            for stale in (out.with_suffix(".olean.hash"), out.with_suffix(".ilean")):
                try:
                    stale.unlink()
                except (FileNotFoundError, IsADirectoryError):
                    pass
            tmp = out.with_name(out.name + f".tmp{os.getpid()}.{threading.get_ident()}")
            try:
                r = subprocess.run(["lean", *LEAN_OPTS, str(src.relative_to(PKG)), "-o", str(tmp)],
                                   cwd=PKG, env=env, capture_output=True, text=True,
                                   timeout=args.timeout)
            except subprocess.TimeoutExpired:
                # A TIMEOUT IS NOT A RED.  It says the module was not verified, not
                # that it fails -- reporting it as a failure would send someone
                # hunting a defect that has not been shown to exist.  It is also not
                # a reason to abandon the sweep: this exception used to propagate out
                # of ThreadPoolExecutor.map and kill the whole run, so ONE slow module
                # suppressed the verdict on every module after it (measured
                # 2026-09-07: QOU.Machinery.HeckeH4Semisimple exceeded 1800s at
                # module 527 of 628, and the remaining 101 were never attempted AND
                # no summary was printed -- bean qou-xumu).
                tmp.unlink(missing_ok=True)
                return m, None, f"TIMEOUT after {args.timeout}s"
            if r.returncode == 0 and tmp.exists():
                os.replace(tmp, out)     # atomic; no window where `out` is absent
            else:
                tmp.unlink(missing_ok=True)
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
                    elif rc is None:
                        timed_out[m] = log
                        broken.add(m)   # dependents cannot be judged either
                        print(f"  [{done_ct}/{n}] TIMEOUT  {m}  ({log})", flush=True)
                    else:
                        errs = [l for l in log.splitlines() if ": error:" in l]
                        # THREE ways a non-zero exit is NOT a failing module, and
                        # reporting any of them as RED sends the next reader
                        # hunting a defect that has not been shown to exist --
                        # the same cannot-verify-vs-fails conflation `qou-xumu`
                        # made this script separate TIMEOUT out for.
                        #
                        # 1. Killed by a signal (rc < 0), typically SIGSEGV on a
                        #    large import closure.  A sibling measured 5 of these
                        #    on QOU.Hecke.* H3A/H4A -- exit 139, zero bytes of
                        #    output (audit `333e491eaa4`, bean qou-g5sp).
                        # 2. Non-zero with NO diagnostic at all: nothing was
                        #    judged, so there is no verdict to report.
                        # 3. A missing object file.  For a Mathlib module that is
                        #    the restored cache being short (MEASURED here:
                        #    `Mathlib.RepresentationTheory.Homological.
                        #    GroupCohomology.LowDegree` absent from BOTH mathlib
                        #    trees, which made the library ROOT unjudgeable); for
                        #    a QOU module it is a build-order or slicing problem.
                        #    Neither is the module's source being wrong.
                        missing = [l for l in errs if "does not exist" in l
                                   and "object file" in l]
                        if rc < 0 or not errs or missing:
                            if rc < 0:
                                why = f"killed by signal {-rc}"
                            elif missing:
                                # Name the MISSING MODULE, not the first 120
                                # characters of its absolute path -- the path is
                                # the same prefix for every hit and the module is
                                # the only part that tells you what to fix.
                                mo = re.search(r"of module ([\w.]+) does not exist",
                                               missing[0])
                                mm = mo.group(1) if mo else "?"
                                where = "mathlib cache" if mm.startswith("Mathlib") \
                                        else "build order"
                                why = f"missing olean {mm} ({where})"
                            else:
                                why = f"exit {rc}, no diagnostic"
                            unverified[m] = why
                            broken.add(m)
                            print(f"  [{done_ct}/{n}] UNVERIFIED  {m}  ({why})",
                                  flush=True)
                        else:
                            red[m] = errs[:5]
                            broken.add(m)
                            print(f"  [{done_ct}/{n}] RED  {m}", flush=True)
                            for e in errs[:3]:
                                print(f"        {e}", flush=True)

        print(f"\n=== library sweep: {ok} ok, {len(red)} RED, "
              f"{len(timed_out)} TIMEOUT + {len(unverified)} UNVERIFIED (NOT failing), "
              f"{len(skipped)} skipped (dependency red), "
              f"{time.time() - t0:.0f}s ===")
        for m in sorted(timed_out):
            print(f"TIMEOUT {m} -- unverified; re-run with a larger --timeout to judge it")
        for m, why in sorted(unverified.items()):
            print(f"UNVERIFIED {m} -- {why}  (NOT a corpus defect on this evidence)")
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
