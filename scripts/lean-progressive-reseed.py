#!/usr/bin/env python3
"""Progressively refresh the local olean snapshot, one namespace chunk at a time.

## Why

`lean`-direct exit 0 is a claim about the olean SNAPSHOT, not about the library
source (bean `qou-56qy`).  On 2026-09-14 the gap was **692 changed / 1261 dirty
closure = 43.6 % of the library**, up from the 305 recorded on 2026-09-05 -- it
compounds, it does not drain.  `scripts/lean-library-sweep.py` already rebuilds
the dirty closure from source into a shadow to verify it; what it does not do is
KEEP that work.  Every run throws the rebuilt oleans away, so the next agent
starts from the same stale snapshot.

This driver keeps them: sweep a chunk, install the freshly-built oleans over the
stale ones in the real tree, reclaim the shadow, move to the next chunk.

## Why it must be progressive, and it is NOT a tuning preference

The sweep's own docstring estimates 0.22 MB per rebuilt module.  **Measured on
this corpus it is ~1.2 MB** (25 modules cost 30 MB of shadow).  At 1261 modules
a single run needs ~1.5 GB of shadow, and a container here runs at 99 % of a
~38 GB per-session quota with a few hundred MB free.  So a whole-corpus run in
one shot does not fit and never did; reclaiming between chunks is what makes it
run at all.  Installing is close to free: a rebuilt olean REPLACES a stale one
of similar size, so the tree does not grow (measured: 486 -> 491 MB free across
the pilot, i.e. it went UP once the shadow was reclaimed).

## What this does NOT do, and the trap it would otherwise walk into

The installed oleans come from `lean`-direct builds, which write **no `.trace`**.
Lake treats an untraced olean as stale, so a subsequent `lake build` will rebuild
them -- and per AGENTS.md (bean `02kc`) a `lake build` against a restored tree
EVICTS it.  This driver therefore:

  * refreshes the tree that `lean`-direct and both sweeps read, which is what
    every Lean verification in this repo actually uses; and
  * does NOT claim to make `lake build` incremental, and must not be described
    as doing so.

It also does not push anything to a `lake-cache/*` branch.  Seeding a branch is
a separate job with a separate disk profile (the full seed is ~1.7 GiB of parts)
and is deliberately out of scope here.

## Usage

    scripts/lean-progressive-reseed.py --list                 # chunk census
    scripts/lean-progressive-reseed.py QOU.Hecke QOU.SchurWeyl
    scripts/lean-progressive-reseed.py --all                  # every chunk, biggest last

A RED module is reported and its olean is NOT installed -- a chunk that fails
leaves the snapshot exactly as it was for that module.
"""
import argparse, collections, importlib.util, os, pathlib, shutil, subprocess, sys, time

ROOT = pathlib.Path(__file__).resolve().parent.parent
SWEEP = ROOT / "scripts" / "lean-library-sweep.py"


def _sweep_module():
    spec = importlib.util.spec_from_file_location("lls", SWEEP)
    m = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(m)
    except SystemExit:
        pass
    m.PKG = ROOT / "content/quantum-observable-universe/lean"
    m.LIB = "QOU"
    return m


def census():
    m = _sweep_module()
    oleans = m.find_oleans()
    mod2path, imports = m.load_graph()
    dirty, changed, never, _ = m.dirty_closure(mod2path, imports, oleans)
    by = collections.Counter(".".join(x.split(".")[:2]) for x in dirty)
    return oleans, dirty, changed, never, by


def pull_in(prefix: str, exact: bool, dirty, imports, untrusted) -> set:
    """The modules a chunk will ACTUALLY compile, by the sweep's own rule.

    `lean-library-sweep.py` seeds on the selection and then transitively pulls
    in every *untrusted* import across namespaces, because a dependency the
    snapshot cannot vouch for would otherwise be a guaranteed spurious RED.
    Sizing a chunk by its own module count therefore understates it, and for
    the LIBRARY ROOT it understates it catastrophically: `QOU` imports the whole
    library, so its pull-in is the entire dirty closure.

    MEASURED: the root chunk was estimated at ~1 MB and was compiling
    `QOU.Mathlib.HeckeAlgebra` at 3.4 GB RSS with the shadow back at 2.4 GB when
    it was killed.  That is the SECOND time this driver blew up on the root
    chunk -- the first was `--only` being a prefix, fixed by `--only-exact`, and
    fixing it exposed this one underneath.  A guard that counts the wrong set is
    not a weaker guard, it is a guard pointed at the wrong question.
    """
    seeds = {m for m in dirty if (m == prefix if exact else m.startswith(prefix))}
    need, stack = set(seeds), list(seeds)
    while stack:
        for d in imports[stack.pop()]:
            if d in untrusted and d not in need:
                need.add(d)
                stack.append(d)
    return need


def install(shadow: pathlib.Path, real: pathlib.Path) -> tuple[int, int, float]:
    """Copy shadow oleans that were REBUILT (hardlink broken) or are NEW.

    Identifying them by inode rather than by mtime is deliberate: the shadow is
    hardlinked from the real tree, and `shutil.copy2`/`tar` both PRESERVE mtime,
    so an mtime test cannot tell a rebuilt file from a linked one.  A rebuild
    unlinks first, which breaks the hardlink -- that is the signal.
    """
    n = r = 0
    byt = 0.0
    for p in (shadow / "QOU").rglob("*.olean"):
        t = real / p.relative_to(shadow)
        if t.exists() and p.stat().st_ino == t.stat().st_ino:
            continue
        new = not t.exists()
        t.parent.mkdir(parents=True, exist_ok=True)
        byt += p.stat().st_size
        shutil.copy2(p, t)
        n, r = (n + 1, r) if new else (n, r + 1)
    return r, n, byt / 1e6


def free_mb() -> float:
    s = os.statvfs("/")
    return s.f_bavail * s.f_frsize / 1e6


def run_chunk(prefix: str, shadow_root: pathlib.Path, jobs: int, timeout: int,
              exact: bool = False) -> int:
    """Rebuild one chunk into a shadow, install the fresh oleans, reclaim.

    `exact` selects `--only-exact` over `--only`, and it is NOT cosmetic.
    `--only` is a PREFIX, so the library root chunk `QOU` matches every module
    in the corpus: the chunk silently becomes a whole-corpus sweep needing
    ~1.5 GB of shadow.  AGENTS.md documents this trap and this driver walked
    into it anyway on its first full run -- caught at 482 MB free with the
    shadow already at 2.4 GB, by watching, not by a guard.

    Note what did NOT save it: `--min-free-mb` is checked BEFORE a chunk, so it
    cannot stop a chunk that turns out to be 50x its advertised size once it is
    running.  Sizing the chunk correctly up front is the only defence.
    """
    real = _sweep_module().find_oleans()
    shutil.rmtree(shadow_root, ignore_errors=True)
    shadow_root.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    cp = subprocess.run(
        [sys.executable, str(SWEEP), "--package", "QOU",
         "--only-exact" if exact else "--only", prefix,
         "--shadow", str(shadow_root), "--jobs", str(jobs),
         "--timeout", str(timeout)],
        cwd=ROOT, capture_output=True, text=True)
    tail = [l for l in cp.stdout.splitlines()
            if " RED" in l or "library sweep:" in l or "TIMEOUT" in l]
    for l in tail:
        print("   " + l)
    shadow = shadow_root / "qou"
    if shadow.is_dir():
        r, n, mb = install(shadow, real)
        print(f"   installed {r} rebuilt + {n} new ({mb:.1f} MB) "
              f"in {time.time()-t0:.0f}s; free {free_mb():.0f} MB")
    shutil.rmtree(shadow_root, ignore_errors=True)
    return cp.returncode


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("prefixes", nargs="*")
    ap.add_argument("--list", action="store_true", help="print the chunk census and exit")
    ap.add_argument("--all", action="store_true", help="every chunk, smallest first")
    ap.add_argument("--jobs", type=int, default=2)
    ap.add_argument("--timeout", type=int, default=1800)
    ap.add_argument("--shadow", default=os.environ.get("RESEED_SHADOW", "/tmp/qou-reseed"))
    ap.add_argument("--min-free-mb", type=int, default=250,
                    help="abort before a chunk if free space is below this. A "
                         "container that runs out mid-build cannot even write "
                         "the harness's own output capture (AGENTS.md §Disk).")
    args = ap.parse_args()

    oleans, dirty, changed, never, by = census()
    deferred: list[str] = []
    print(f"olean tree: {oleans}")
    print(f"dirty closure {len(dirty)}  (changed {len(changed)}, never-built {len(never)})")
    if args.list:
        for p, n in by.most_common():
            print(f"  {p:44s} {n:5d}")
        return 0

    todo = args.prefixes or ([p for p, _ in sorted(by.items(), key=lambda kv: kv[1])]
                             if args.all else [])
    if not todo:
        ap.error("give one or more prefixes, or --all, or --list")

    rc = 0
    for i, p in enumerate(todo, 1):
        # Recompute before every chunk, not once up front.  Earlier chunks make
        # their modules trusted, which SHRINKS later chunks' pull-in -- the
        # library root in particular goes from "the whole dirty closure" to
        # nearly nothing once its dependencies are fresh.  A single up-front
        # sizing would refuse it forever.
        m = _sweep_module()
        oleans = m.find_oleans()
        mod2path, imports = m.load_graph()
        dirty, changed, never, untrusted = m.dirty_closure(mod2path, imports, oleans)
        exact = p in dirty
        need = pull_in(p, exact, dirty, imports, untrusted)
        if not need:
            print(f"[{i}/{len(todo)}] {p}  already clean, skipping")
            continue
        est = len(need) * 1.2
        if est > free_mb() - args.min_free_mb:
            print(f"[{i}/{len(todo)}] {p}  DEFER: pull-in {len(need)} modules "
                  f"~{est:.0f} MB, {free_mb():.0f} MB free (reserve "
                  f"{args.min_free_mb}) -- retry after other chunks shrink it")
            deferred.append(p)
            continue
        if free_mb() < args.min_free_mb:
            print(f"STOP before {p}: free {free_mb():.0f} MB < --min-free-mb "
                  f"{args.min_free_mb}")
            return 2
        print(f"[{i}/{len(todo)}] {p}  (pull-in {len(need)}"
              f"{', exact' if exact else ''}, ~{est:.0f} MB)")
        rc |= run_chunk(p, pathlib.Path(args.shadow), args.jobs, args.timeout,
                        exact=exact)

    if deferred:
        print(f"\nretrying {len(deferred)} deferred chunk(s); their pull-in "
              f"should have shrunk as earlier chunks made modules trusted")
        for i, p in enumerate(deferred, 1):
            m = _sweep_module()
            oleans = m.find_oleans()
            mod2path, imports = m.load_graph()
            dirty, changed, never, untrusted = m.dirty_closure(
                mod2path, imports, oleans)
            exact = p in dirty
            need = pull_in(p, exact, dirty, imports, untrusted)
            est = len(need) * 1.2
            if not need:
                print(f"[retry {i}/{len(deferred)}] {p}  now clean")
                continue
            if est > free_mb() - args.min_free_mb:
                print(f"[retry {i}/{len(deferred)}] {p}  STILL TOO BIG: "
                      f"pull-in {len(need)} ~{est:.0f} MB vs {free_mb():.0f} MB "
                      f"free -- split this prefix one level deeper")
                rc |= 4
                continue
            print(f"[retry {i}/{len(deferred)}] {p}  (pull-in {len(need)}, "
                  f"~{est:.0f} MB)")
            rc |= run_chunk(p, pathlib.Path(args.shadow), args.jobs,
                            args.timeout, exact=exact)
    return rc


if __name__ == "__main__":
    sys.exit(main())
