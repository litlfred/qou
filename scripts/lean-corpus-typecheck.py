#!/usr/bin/env python3
"""Typecheck EVERY module of a Lean library from source, resumably.

WHY THIS EXISTS.  `lake build QOU` builds only the import closure of `QOU.lean`,
which on 2026-09-07 was 890 of 2735 modules -- so 67% of the library is built by
nothing (bean qou-g5sp).  Sizing that gap needs a per-module verdict, and the
cheap proxies do not give one: olean EXISTENCE attests to whatever bulk build
seeded the cache (2722 of 2735 oleans share one mtime), and olean-vs-source mtime
compares two checkout timestamps in a fresh clone.  Only compiling answers it.

WHAT IT MEASURES, precisely.  Each module's OWN source against the dependency
oleans currently on LEAN_PATH.  It does NOT rebuild dependencies, so a module can
pass here and still be stale against a dependency whose source moved after the
cache was built -- the same snapshot-conditionality as `qou-56qy`.  Read a PASS
as "this module's source is not itself broken", not as "this module is current".
A FAIL is unconditional: the file does not typecheck as it stands.

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

LEAN_DIR = "content/quantum-observable-universe/lean"
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
        print("\n  RED:")
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
          f"checkpoint, {len(todo)} to run", flush=True)
    t0 = time.time()
    for i, m in enumerate(todo, 1):
        src = os.path.join(lean_dir, m.replace(".", "/") + ".lean")
        st = time.time()
        try:
            p = subprocess.run(["lean", *LEAN_ARGS, src], cwd=lean_dir, env=env,
                               capture_output=True, text=True, timeout=a.timeout)
            errs = [l for l in (p.stdout + p.stderr).splitlines() if "error" in l]
            rec = {"module": m, "status": "ok" if p.returncode == 0 else "red",
                   "rc": p.returncode, "secs": round(time.time()-st, 1),
                   "errors": errs[:5]}
        except subprocess.TimeoutExpired:
            rec = {"module": m, "status": "timeout", "rc": None,
                   "secs": a.timeout, "errors": []}
        with open(CKPT, "a") as fh:
            fh.write(json.dumps(rec) + "\n"); fh.flush(); os.fsync(fh.fileno())
        el = time.time() - t0
        eta = el / i * (len(todo) - i)
        print(f"  [{i}/{len(todo)}] {rec['status']:7s} {m}  "
              f"({rec['secs']}s, elapsed {el/60:.0f}m, ETA {eta/60:.0f}m)", flush=True)
    print("\n=== final ===")
    return 1 if report(load_ckpt(), mods) else 0

if __name__ == "__main__":
    sys.exit(main())
