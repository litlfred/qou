#!/usr/bin/env python3
"""Full-library red census — bottom-up fixpoint `lean -o` build of all QOU modules
against the restored lake-cache Mathlib oleans (no `lake`; avoids the cache-wipe gotcha).

Classifies each module:
  GREEN          — compiles to olean (imports satisfied, no source error)
  blocked        — fails ONLY on a missing QOU dependency olean (retried in the fixpoint)
  cache-artifact — fails on a missing *Mathlib* olean (outside the cached closure; compiles in CI)
  RED            — genuine source error (imports loaded)

Run on a working tree checked out to the commit you want to census. Mathlib oleans must be
restored first (lake-cache/qou-<toolchain-slug>; see lean-environment-setup.md).
"""
import os, subprocess, glob, re, shutil, sys
from concurrent.futures import ThreadPoolExecutor

LEANBIN = os.path.expanduser("~/.elan/toolchains/lean-v4.24.0/bin/lean")
ROOT = subprocess.check_output(["git", "rev-parse", "--show-toplevel"]).decode().strip()
LEANDIR = f"{ROOT}/content/quantum-observable-universe/lean"
deps = subprocess.check_output(
    ["find", f"{ROOT}/.lake/packages", "-maxdepth", "5", "-type", "d",
     "-path", "*/.lake/build/lib/lean"]).decode().split()
QOULIB = f"{LEANDIR}/.lake/build/lib/lean"
env = dict(os.environ, LEAN_PATH=":".join(deps + [QOULIB]))
os.chdir(LEANDIR)

# fresh: drop stale QOU oleans (keep mathlib deps)
shutil.rmtree(f"{QOULIB}/QOU", ignore_errors=True)
for f in glob.glob(f"{QOULIB}/QOU.olean"):
    os.remove(f)
os.makedirs(f"{QOULIB}/QOU", exist_ok=True)

modules = sorted(set(glob.glob("QOU/**/*.lean", recursive=True)) | {"QOU.lean"})
print(f"modules: {len(modules)}; deps on LEAN_PATH: {len(deps)}", flush=True)
def olean_path(m): return os.path.join(QOULIB, m[:-5] + ".olean")

# classification keys on the missing-olean PATH (the error quotes the absolute path, not the
# bare module name — the bug in the first run was matching the bare name).
def classify_fail(err):
    if ("unknown module prefix 'QOU" in err
            or re.search(r"object file '[^']*/QOU/[^']*\.olean'", err)):
        return "blocked"
    if ("module Mathlib does not exist" in err
            or re.search(r"object file '[^']*/[Mm]athlib[^']*\.olean'", err)):
        return "cache"
    return "RED"

def compile_one(m):
    op = olean_path(m); os.makedirs(os.path.dirname(op), exist_ok=True)
    try:
        r = subprocess.run([LEANBIN, "-o", op, m], env=env, capture_output=True, text=True, timeout=300)
    except subprocess.TimeoutExpired:
        return (m, "RED", "TIMEOUT (>300s) [perf/maxHeartbeats]")
    if r.returncode == 0:
        return (m, "GREEN", "")
    err = (r.stdout + "\n" + r.stderr).strip()
    cls = classify_fail(err)
    elines = [l for l in err.splitlines() if "error" in l.lower()]
    first = (elines[0] if elines else (err.splitlines()[0] if err.splitlines() else "?"))[:240]
    return (m, cls, first)

status, info, remaining, pass_n = {}, {}, set(modules), 0
while True:
    pass_n += 1
    with ThreadPoolExecutor(max_workers=6) as ex:
        results = list(ex.map(compile_one, sorted(remaining)))
    new_green = 0
    for (m, cls, err) in results:
        if cls == "GREEN":
            status[m] = "GREEN"; remaining.discard(m); new_green += 1
        elif cls in ("RED", "cache"):
            status[m] = cls; info[m] = err; remaining.discard(m)
        # 'blocked' stays in remaining for the next pass
    nred = sum(1 for s in status.values() if s == "RED")
    print(f"pass {pass_n}: +{new_green} green | remaining(blocked) {len(remaining)} | red {nred}", flush=True)
    if new_green == 0:
        break

def count(s): return sum(1 for v in status.values() if v == s)
print(f"\n=== {count('GREEN')} GREEN | {count('RED')} RED | {count('cache')} cache-artifact | "
      f"{len(remaining)} blocked-by-red ===", flush=True)
for label in ("RED", "cache"):
    print(f"\n=== {label} ===", flush=True)
    for m in sorted(m for m in status if status[m] == label):
        print(f"{label}\t{m}\t{info[m]}", flush=True)
print("\n=== blocked-by-red (downstream of a RED/cache dep) ===", flush=True)
for m in sorted(remaining):
    print(f"BLK\t{m}", flush=True)
