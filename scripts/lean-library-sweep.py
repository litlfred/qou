#!/usr/bin/env python3
"""Compile every stale library module from source and report which are red.

## Why

`scripts/lean-content-sweep.sh` covers content-block `.lean` siblings.  It does
NOT cover the package's own library tree (`folio/*/lean/QOU/**`), and that
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
A reused shadow is topped up on every run -- anything the real olean tree
gained since it was built is linked in, because the shadow MASKS that tree
rather than layering over it and a gap reads as a RED (see refresh_shadow).
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
PKG = ROOT / "folio/quantum-observable-universe/lean"   # default; see packages()
LIB = "QOU"


def packages() -> list[tuple[pathlib.Path, str]]:
    """Every paper package: (lean dir, library name).

    Discovered, not hardcoded — a package is a `folio/*/lean/` holding a
    lakefile and a top-level `<Lib>.lean` root module whose stem names the
    library (`QOU`, `UGB`, `Fred2005`).  Sweeping only the first of the three
    was the gap this closes: UGB and Fred2005 were covered by nothing.
    """
    out = []
    for lakefile in sorted(ROOT.glob("folio/*/lean/lakefile.toml")):
        d = lakefile.parent
        for root_mod in sorted(d.glob("*.lean")):
            if (d / root_mod.stem).is_dir():
                out.append((d, root_mod.stem))
    return out


MATHLIB_DEPS = (
    "Qq", "Batteries", "LeanSearchClient", "Aesop",
    "Plausible", "ImportGraph", "ProofWidgets",
)


def _nonempty_olean_count(d: pathlib.Path) -> int:
    """Count non-empty `.olean` files under `d` (0-byte files count as 0)."""
    if not d.is_dir():
        return -1
    n = 0
    for root, _dirs, files in os.walk(d):
        for f in files:
            if f.endswith(".olean"):
                try:
                    if (pathlib.Path(root) / f).stat().st_size > 0:
                        n += 1
                except OSError:
                    pass
    return n


def find_oleans() -> pathlib.Path:
    """The restore seeds the ROOT workspace; a per-paper `lake build` seeds $PKG.

    Both are real, so pick by COMPLETENESS (largest count of non-empty `.olean`
    files under `<cand>/<LIB>`), matching `scripts/lean-shadow-verify.sh`,
    rather than taking the first candidate with a `<LIB>/` directory (which may
    be an incomplete mid-build stub).  Bean `qou-fo7l`.
    """
    env = os.environ.get("OLEANS")
    if env:
        c = pathlib.Path(env)
        if (c / LIB).is_dir():
            return c
        sys.exit(f"no olean tree with a {LIB}/ dir; looked in: {c}")
    cands = [PKG / ".lake/build/lib/lean", ROOT / ".lake/build/lib/lean"]
    best_c, best_n = None, -1
    for c in cands:
        if not (c / LIB).is_dir():
            continue
        n = _nonempty_olean_count(c / LIB)
        if n > best_n:
            best_c, best_n = c, n
    if best_c is not None:
        return best_c
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
        # BOTH paths.  `PKG/LIB` is the namespace DIRECTORY; the library root
        # module `PKG/LIB.lean` sits BESIDE it and is not under it, so a log
        # scoped to the directory alone never sees the root and returns no time
        # for it.  `dirty_closure` then marks a module with no commit time as
        # changed UNCONDITIONALLY, so the root was permanently dirty by
        # construction -- a floor of exactly 1 that no amount of rebuilding can
        # clear.  Measured 2026-09-14: after a full progressive reseed took the
        # QOU closure 1261 -> 1, that surviving 1 was the root, and it was this,
        # not work left undone.
        ["git", "log", "--format=%ct", "--name-only", "--",
         str(PKG / LIB), str(PKG / f"{LIB}.lean")],
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
    ap.add_argument("--jobs", type=int, default=2,
                    help="concurrent lean processes.  DEFAULT 2, NOT 3, and the "
                         "reason is arithmetic: LEAN_NUM_THREADS is derived as "
                         "nproc//jobs (see the parallelism block below), so a "
                         "jobs that does not DIVIDE nproc wastes the remainder.  "
                         "On the 4-core container this repo runs in, --jobs 3 "
                         "gives 1 thread each = 3 of 4 cores, leaving one idle; "
                         "--jobs 2 gives 2 threads each = 4 of 4, AND halves "
                         "per-module wall-clock.  It dominates on both axes.  "
                         "Prefer a divisor of nproc when overriding.")
    ap.add_argument("--timeout", type=int, default=1800,
                    help="per-module seconds; on expiry the module is reported "
                         "TIMEOUT (unverified) and the sweep CONTINUES")
    ap.add_argument("--limit", type=int, default=0,
                    help="stop after N modules (for a smoke test)")
    ap.add_argument("--all", action="store_true",
                    help="compile EVERY module, not just the dirty closure -- the "
                         "measurement for 'how much of the library compiles'.  "
                         "CORRECTED 2026-09-13: this said '1863 of 2773 are outside "
                         "the ROOT BUILD'.  Both halves were wrong.  The count came "
                         "from a direct-import measure corrected on 2026-09-08 (the "
                         "transitive figure is ~48%%, 1385 of 2836); and `lake build "
                         "QOU` builds the WHOLE TREE, because the paper lakefile "
                         "declares globs = [\"QOU\", \"QOU.+\"] (bean qou-rc7b, done "
                         "2026-08-08) -- so those modules are outside the root's "
                         "IMPORT CLOSURE, not outside the build.  What IS true is "
                         "that nothing runs that build automatically (CI is "
                         "workflow_dispatch-only), which is why this flag is worth "
                         "having.  Hours, not minutes.  Bean qou-g5sp.")
    ap.add_argument("--only", metavar="PREFIX",
                    help="restrict to modules whose name starts with PREFIX "
                         "(e.g. QOU.BraidKnot).  Exists so a --all run can be "
                         "CHUNKED: the shadow's newly-written oleans are the only "
                         "real bytes it costs (0.22 MB/module), so a full run needs "
                         "~610 MB at once, and reclaiming the shadow between chunks "
                         "is what makes it fit a container at 99%%.  NOTE this "
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
    ap.add_argument("--report", action="store_true",
                    help="print the snapshot-drift census and EXIT 0 without "
                         "compiling anything.  Exists because the numbers this "
                         "sweep already computes are the answer to a question "
                         "nobody could ask cheaply: `lean`-direct exit 0 is a "
                         "claim about the olean SNAPSHOT, not about the library "
                         "source (bean qou-56qy), and the size of that gap was "
                         "only obtainable by importing this module and calling "
                         "its internals -- which is how the last measurement got "
                         "`len()` of a 4-tuple and reported a closure of 4 "
                         "against a 683-module seed.  A closure cannot be smaller "
                         "than its seed; print it here so the check is one "
                         "command and that class of error has nowhere to live.")
    ap.add_argument("--package", action="append", metavar="LIB",
                    help="library name (QOU, UGB, Fred2005); repeatable, "
                         "default all discovered")
    args = ap.parse_args()

    # Make the root and paper olean trees hold the same union before anything
    # resolves against them (bean qou-4h26, wired 2026-11-21).  Lean answers a
    # whole package from the FIRST LEAN_PATH root holding its directory, so an
    # incomplete tree first on the path produced phantom MISSING-OLEAN reds
    # (qou-tpdg).  Hardlinks only, idempotent, ~0.2 s when already in sync.
    if os.environ.get("LEAN_NO_TREE_SYNC") != "1":
        r = subprocess.run([str(ROOT / "scripts/lean-sync-olean-trees.sh")],
                           capture_output=True, text=True)
        if r.returncode != 0:
            print("WARNING: lean-sync-olean-trees.sh failed; a MISSING-OLEAN "
                  "red may be an environment artifact.\n" + r.stderr[-800:],
                  file=sys.stderr)

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
        sys.exit("no paper packages discovered under folio/*/lean/")

    rc = 0
    for i, (pkg_dir, lib) in enumerate(todo_pkgs):
        if i:
            print()
        print(f"########## {lib}  ({pkg_dir.relative_to(ROOT)})")
        PKG, LIB = pkg_dir, lib
        rc |= sweep_one(args)
    return rc


def refresh_shadow(src: pathlib.Path, dst: pathlib.Path) -> int:
    """Link into a REUSED shadow every file the real tree has and it lacks.

    A shadow is only populated once, when it is created.  With `--shadow` it is
    reused across runs, and anything written into the real olean tree after that
    point is missing from it -- a background `lake build` is the documented case
    (AGENTS.md: a SessionStart build re-fired by compaction moved the QOU tree
    2660 -> 2713 oleans mid-sweep).

    That is not a harmless gap.  Per the masking note at the call site, Lean
    commits to the FIRST LEAN_PATH root holding `<LIB>/` and never consults a
    later root for anything beneath it, so the real tree is NOT a fallback: a
    module missing from the shadow reads as "does not exist" and the sweep
    reports a RED that is about its own shadow.  Measured by a sibling session
    on `lean-content-sweep.sh`'s `cp -al` shadow: 209 files missing, surfacing
    as a bogus `QOU.BraidKnot` failure naming an `EdgeDecoupling.olean` that was
    present in the real tree the whole time (PR #7378 comment 5677632542).

    Only MISSING paths are linked.  A shadow file that differs from its real-tree
    twin is one a previous run REBUILT -- newer and correct -- and overwriting it
    would throw away the work the shadow exists to hold.
    """
    linked = 0
    for dirpath, _dirnames, filenames in os.walk(src):
        rel = pathlib.Path(dirpath).relative_to(src)
        for name in filenames:
            target = dst / rel / name
            if target.exists():
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            try:
                os.link(pathlib.Path(dirpath) / name, target)
            except OSError:
                shutil.copy2(pathlib.Path(dirpath) / name, target)
            linked += 1
    return linked


def sweep_one(args) -> int:
    if args.report:
        # Report mode must survive a package with no snapshot at all, because
        # that IS one of the things worth reporting.  `find_oleans` exits for
        # the sweep path on purpose -- a gate with no tree to check against
        # must not silently pass -- so catch it here only, leaving that
        # behaviour untouched for every non-report run.  Measured: without
        # this, a plain `--report` aborts on Fred2005 (no olean tree in a
        # container restored from the qou cache branch) and never reaches QOU,
        # which is the package anyone running it cares about.
        try:
            oleans = find_oleans()
        except SystemExit as e:
            print(f"  no snapshot for {LIB}: {e}")
            return 0
    else:
        oleans = find_oleans()
    print(f"olean tree: {oleans}")
    mod2path, imports = load_graph()
    dirty, changed, never_built, untrusted = dirty_closure(mod2path, imports,
                                                oleans, all_dirty=args.all)

    if args.report:
        total = len(mod2path)
        pct = (100.0 * len(dirty) / total) if total else 0.0
        print(f"  modules in graph                              {total}")
        print(f"  never built (no olean at all)                 {len(never_built)}")
        print(f"  changed (source newer than its own olean)     {len(changed)}")
        print(f"  standard-dirty (snapshot cannot vouch)        {len(untrusted)}")
        print(f"  DIRTY CLOSURE (changed + their importers)     {len(dirty)}"
              f"  ({pct:.1f}% of the library)")
        print(f"  clean in snapshot                             {total - len(dirty)}")
        print("  -- a `lean`-direct green on any DIRTY module is a claim about "
              "the snapshot, not the source; rebuild its cone first.")
        if sel := (args.only or args.only_exact):
            hit = ({m for m in dirty if m == args.only_exact} if args.only_exact
                   else {m for m in dirty if m.startswith(args.only)})
            print(f"  selection {sel}: {len(hit)} of them are dirty")
            for m in sorted(hit):
                tag = ("NEVER-BUILT" if m in never_built
                       else "CHANGED" if m in changed else "via-imports")
                print(f"      {tag:12s} {m}")
        return 0
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
        else:
            # Reused shadow (`--shadow`): top it up.  See refresh_shadow().
            added = refresh_shadow(oleans / LIB, shadow / LIB)
            if added:
                print(f"refreshing reused shadow: linked {added} file(s) "
                      f"the real tree gained since it was built")

        siblings = [str(p) for p in sorted(ROOT.glob("folio/*/lean/.lake/build/lib/lean"))
                    if p != oleans]
        # Dependency olean roots, in the order Lean should search them.
        #
        # 1. Deterministically sort all glob results (`Path.glob` returns raw
        #    filesystem `scandir` order).
        # 2. Order the current package's `PKG/.lake/packages/*` and
        #    `ROOT/.lake/packages/*` ahead of other `folio/*/lean/.lake/packages/*`
        #    roots.
        # 3. Filter out incomplete package roots that hold fewer non-empty
        #    `.olean` files than the most complete root for that package name,
        #    so a partial package directory earlier on `LEAN_PATH` can never
        #    shadow a complete one (`qou-fo7l`, `qou-4h26`, `qou-tpdg`).
        raw_pkg_cands = (
            sorted(PKG.glob(".lake/packages/*/.lake/build/lib/lean"))
            + sorted(ROOT.glob(".lake/packages/*/.lake/build/lib/lean"))
            + [p for p in sorted(ROOT.glob("folio/*/lean/.lake/packages/*/.lake/build/lib/lean"))
               if not p.is_relative_to(PKG)]
        )
        seen_cands: list[pathlib.Path] = []
        seen_set: set[pathlib.Path] = set()
        for p in raw_pkg_cands:
            if p not in seen_set and p.is_dir():
                seen_set.add(p)
                seen_cands.append(p)
        pkg_counts: dict[pathlib.Path, int] = {}
        best_pkg_count: dict[str, int] = {}
        for p in seen_cands:
            pkg_name = p.parents[3].name
            cnt = _nonempty_olean_count(p)
            pkg_counts[p] = cnt
            if cnt > best_pkg_count.get(pkg_name, -1):
                best_pkg_count[pkg_name] = cnt
        pkg_roots = [
            str(p) for p in seen_cands
            if pkg_counts[p] > 0 and pkg_counts[p] >= best_pkg_count.get(p.parents[3].name, 0)
        ]
        lean_path = ":".join([str(shadow)] + pkg_roots + siblings + [str(oleans)])

        # BOUND TOTAL PARALLELISM, not process count.  `--jobs N` spawns N `lean`
        # processes, and EACH ONE sizes its own task pool from hardware concurrency
        # -- measured 7-8 OS threads per process, ~198% CPU apiece.  So `--jobs 3`
        # on a 4-core box is not "3 of 4 cores used, one spare"; it is three
        # processes each trying to take all four, ~24 threads on 4 cores, and each
        # module gets about a THIRD of the machine instead of the whole of it.
        #
        # That is what produced the sweep's four false TIMEOUTs (bean `qou-ed8a`):
        # every one of them compiles clean when run alone, and the worst case needs
        # 459s with 4 cores against an 1800s budget -- ~1400s at a third of the
        # machine, so the budget is reached by starvation, not by any property of
        # the module.  The timeout then reports the harness, and 14 further modules
        # were SKIPPED behind the cascade.
        #
        # Memory compounds it: per-process RSS was measured climbing to 5.3 GB, so
        # three concurrent would be ~16 GB on a 16 GB box with NO SWAP -- i.e. at
        # the OOM ceiling, which would surface as a signal death (UNVERIFIED), a
        # different and equally misleading label.
        #
        # `jobs * threads <= nproc` keeps a module's share predictable, which is
        # what a per-module wall-clock budget needs in order to mean anything.
        # Respect an explicit LEAN_NUM_THREADS from the caller.
        cores = os.cpu_count() or 1
        lean_threads = max(1, cores // max(1, args.jobs))
        env = dict(os.environ,
                   LEAN_PATH=lean_path,
                   PATH=f"{os.path.expanduser('~')}/.elan/bin:{os.environ['PATH']}")
        env.setdefault("LEAN_NUM_THREADS", str(lean_threads))
        if "LEAN_NUM_THREADS" in os.environ:
            print(f"  parallelism: --jobs {args.jobs}, LEAN_NUM_THREADS="
                  f"{os.environ['LEAN_NUM_THREADS']} (from caller), {cores} cores")
        else:
            print(f"  parallelism: --jobs {args.jobs} x {lean_threads} thread(s) "
                  f"= {args.jobs * lean_threads} of {cores} cores")
        # Integer division bottoms out at one thread, so --jobs > cores still
        # oversubscribes and a wall-clock budget is again measuring starvation
        # rather than the module.  Say so rather than silently under-delivering.
        if args.jobs > cores:
            print(f"  WARNING: --jobs {args.jobs} exceeds {cores} cores; even at "
                  f"1 thread each that is {args.jobs}/{cores} oversubscribed, so "
                  f"a TIMEOUT here may report the harness (bean qou-ed8a).")

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
                        errs = [l for l in log.splitlines()
                                if re.search(r": error(?:\([^)]*\))?:", l)]
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
                                # Sort `missing` deterministically by module
                                # name before picking the diagnostic to report:
                                # Lean elaborates imports across threads, so
                                # stderr lines arrive in thread-completion race
                                # order (`qou-fo7l`).
                                def _missing_mod(line: str) -> str:
                                    m_ = re.search(r"of module ([\w.]+) does not exist", line)
                                    return m_.group(1) if m_ else "?"
                                missing_sorted = sorted(missing, key=lambda l: (_missing_mod(l), l))
                                mm = _missing_mod(missing_sorted[0])
                                if mm == "Mathlib" or mm.startswith("Mathlib."):
                                    where = "mathlib cache"
                                elif any(mm == d or mm.startswith(f"{d}.") for d in MATHLIB_DEPS):
                                    where = "mathlib dep cache"
                                else:
                                    where = "build order"
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
