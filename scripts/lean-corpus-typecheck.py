#!/usr/bin/env python3
"""Typecheck EVERY module of a Lean library from source, resumably.

WHY THIS EXISTS.  `lake build QOU` builds only the import closure of `QOU.lean`,
which on 2026-09-07 was 890 of 2735 modules -- so 67% of the library is built by
nothing (bean qou-g5sp).  Sizing that gap needs a per-module verdict, and the
cheap proxies do not give one: olean EXISTENCE attests to whatever bulk build
seeded the cache (2722 of 2735 oleans share one mtime), and olean-vs-source mtime
compares two checkout timestamps in a fresh clone.  Only compiling answers it.

WHAT IT MEASURES, precisely.  Each module's OWN source against the dependency
oleans currently on LEAN_PATH.  It does NOT rebuild dependencies.

🛑 SO A RED FROM THIS SCRIPT IS NOT A DEFECT REPORT.  An earlier version of this
docstring said "a FAIL is unconditional: the file does not typecheck as it
stands."  **That was wrong, and it is the whole reason this warning exists.**
Measured 2026-09-07 on a 1131-module run: 10 REDs, and ZERO were corpus defects.

  * 5 (the Bruhat/Coxeter chain) were STALE DEPENDENCY OLEANS.  The chain root,
    `CoxeterDihedralOrder`, had an olean built before main added
    `bond_ne_zero_of_pow_eq_one`, so the consumer reported
    `unknown identifier` and everything downstream of it reported
    `Application type mismatch` against the old signature.  Rebuilding the six
    modules root-first made all six exit 0 with no source change whatsoever.
  * 5 (the `QOU.Hecke.*` H3A/H4A family) were SIGSEGV -- `exit 139`, ZERO bytes
    of output, the same container resource limit that makes the library root
    unverifiable here (bean `qou-ed8a`).
  * 1 was a timeout, which is not a verdict either.

A RED therefore means "this module did not typecheck against WHATEVER OLEANS
HAPPENED TO BE ON DISK", which in a container whose olean tree is a patchwork of
a restored cache plus hand rebuilds plus partial `lake build`s is a statement
about the disk, not the corpus.  **To decide whether a RED is real you must
rebuild its dependency chain from source first** -- which is what
`scripts/lean-library-sweep.py` does, and why that is the gate and this is not.

Read a PASS as "this module's source is not itself broken", never as "this module
is current".  Read a RED as "unverified here", never as "broken".

WHY NO `-o`.  Without an output path `lean` typechecks and writes nothing, so a
full pass costs ZERO disk.  That matters: this container has ~950 MB free and a
2735-module build would not fit.  Do not add `-o` to "warm the cache".

RESUMABLE BY DESIGN.  Results append to a JSONL checkpoint after every module and
are flushed immediately; re-running skips whatever the checkpoint already holds.
Container restarts are expected here -- just re-run the same command.

  python3 scripts/lean-corpus-typecheck.py                 # start or resume
  python3 scripts/lean-corpus-typecheck.py --report        # summarise, no work
  python3 scripts/lean-corpus-typecheck.py --only-missing  # only modules absent
                                                           # from the root closure
"""
import argparse, json, os, re, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor

LEAN_DIR = "folio/quantum-observable-universe/lean"
CKPT = "/tmp/lean-corpus-typecheck.jsonl"
LEAN_ARGS = ["-DautoImplicit=false", "-s", "65536"]

def lean_path(root):
    parts = [os.path.join(root, LEAN_DIR, ".lake/build/lib/lean")]
    for p in ["mathlib","batteries","aesop","Qq","proofwidgets",
              "importGraph","plausible","LeanSearchClient"]:
        parts.append(os.path.join(root, ".lake/packages", p, ".lake/build/lib/lean"))
    return ":".join(parts)

def modules(lean_dir, lib="QOU"):
    out = []
    for dp, _, fs in os.walk(os.path.join(lean_dir, lib)):
        for f in sorted(fs):
            if f.endswith(".lean"):
                rel = os.path.relpath(os.path.join(dp, f[:-5]), lean_dir)
                out.append(rel.replace(os.sep, "."))
    return sorted(out)

def root_imports(lean_dir, lib="QOU"):
    p = os.path.join(lean_dir, lib + ".lean")
    return set(re.findall(rf'^import ({lib}\.[\w.]+)', open(p).read(), re.M))

def load_ckpt():
    done = {}
    if os.path.exists(CKPT):
        for line in open(CKPT):
            line = line.strip()
            if not line: continue
            try: r = json.loads(line)
            except json.JSONDecodeError: continue   # truncated final write
            done[r["module"]] = r
    return done

def report(done, targets):
    ok  = [m for m in targets if done.get(m, {}).get("status") == "ok"]
    red = [m for m in targets if done.get(m, {}).get("status") == "red"]
    to  = [m for m in targets if done.get(m, {}).get("status") == "timeout"]
    todo = [m for m in targets if m not in done]
    print(f"  done {len(done and [m for m in targets if m in done])}/{len(targets)}"
          f"   ok {len(ok)}   RED {len(red)}   timeout {len(to)}   remaining {len(todo)}")
    if red:
        print("\n  RED -- NOT defect reports; see the module docstring.  A red here"
              "\n  can be a stale dependency olean or a SIGSEGV, and measured on this"
              "\n  corpus 10 of 10 were exactly that.  Rebuild the dependency chain"
              "\n  from source (lean-library-sweep.py) before believing any of them:")
        for m in red:
            first = (done[m].get("errors") or [""])[0][:110]
            print(f"    {m}\n        {first}")
    if to:
        print("\n  TIMEOUT (not a verdict -- re-run with a larger --timeout):")
        for m in to: print(f"    {m}")
    return len(red)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lean-dir", default=LEAN_DIR)
    ap.add_argument("--package", default="QOU")
    ap.add_argument("--timeout", type=int, default=900)
    ap.add_argument("--only-missing", action="store_true",
                    help="only modules NOT in the library root's import list")
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--jobs", type=int, default=1,
                    help="parallel lean processes; oleans are mmap'd so they share")
    ap.add_argument("--limit", type=int)
    a = ap.parse_args()

    root = subprocess.run(["git","rev-parse","--show-toplevel"],
                          capture_output=True, text=True).stdout.strip()
    lean_dir = os.path.join(root, a.lean_dir)
    mods = modules(lean_dir, a.package)
    if a.only_missing:
        inroot = root_imports(lean_dir, a.package)
        mods = [m for m in mods if m not in inroot]
    if a.limit: mods = mods[:a.limit]

    done = load_ckpt()
    if a.report:
        return 1 if report(done, mods) else 0

    env = dict(os.environ, LEAN_PATH=lean_path(root))
    todo = [m for m in mods if m not in done]
    print(f"corpus typecheck: {len(mods)} target(s), {len(done)} already in "
          f"checkpoint, {len(todo)} to run, jobs={a.jobs}", flush=True)
    t0 = time.time()

    def one(m):
        src = os.path.join(lean_dir, m.replace(".", "/") + ".lean")
        st = time.time()
        try:
            p = subprocess.run(["lean", *LEAN_ARGS, src], cwd=lean_dir, env=env,
                               capture_output=True, text=True, timeout=a.timeout)
            errs = [l for l in (p.stdout + p.stderr).splitlines() if "error" in l]
            return {"module": m, "status": "ok" if p.returncode == 0 else "red",
                    "rc": p.returncode, "secs": round(time.time()-st, 1),
                    "errors": errs[:5]}
        except subprocess.TimeoutExpired:
            return {"module": m, "status": "timeout", "rc": None,
                    "secs": a.timeout, "errors": []}

    # One writer: the checkpoint is append-only and fsynced per record, so a kill
    # at any instant loses at most the record in flight.
    done_n = 0
    with ThreadPoolExecutor(max_workers=a.jobs) as ex, open(CKPT, "a") as fh:
        for rec in ex.map(one, todo):
            done_n += 1
            fh.write(json.dumps(rec) + "\n"); fh.flush(); os.fsync(fh.fileno())
            el = time.time() - t0
            eta = el / done_n * (len(todo) - done_n)
            print(f"  [{done_n}/{len(todo)}] {rec['status']:7s} {rec['module']}  "
                  f"({rec['secs']}s, elapsed {el/60:.0f}m, ETA {eta/60:.0f}m)", flush=True)
    print("\n=== final ===")
    return 1 if report(load_ckpt(), mods) else 0

if __name__ == "__main__":
    sys.exit(main())
