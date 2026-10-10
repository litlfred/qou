#!/usr/bin/env python3
"""Build a QOU module's full transitive import closure from source, in
topological order.

    python3 scripts/lean-build-cone.py QOU.MathlibExt.WenzlSchurElement

Requires the usual lean-direct environment (AGENTS.md §"VERIFY a single file
with lean-direct"):

    export PATH="$HOME/.elan/bin:$PATH"
    export LEAN_PATH="<QOU build lib>:<ROOT .lake/packages/*/.lake/build/lib/lean>"

WHY THIS EXISTS (bean qou-pv3a). The restored `lake-cache/*` oleans are a
snapshot: for some modules they are ABSENT, and for others PRESENT-BUT-STALE
(e.g. a `QPartitionCombinatorics.olean` defining `hookLength` via `List.get?`
where current source uses `lam[i]?`). Both break a build, but they fail very
differently:

  * absent  -> "object file ... does not exist", naming the module. Easy.
  * stale   -> a plausible-looking PROOF ERROR deep inside an unrelated file
               ("unsolved goals" in `hookLength_pos`), naming nothing.

The stale case is the dangerous one. It looks exactly like a genuine red, and
an agent that stashes to pristine `main` to check "is this mine?" reproduces it
there too — because the stale olean is still in the way — and concludes the file
is broken on `main`. It is not. That misdiagnosis happened on 2026-08-15 and
was written into a PR body before this script disproved it.

A loop that rebuilds only the modules named in "does not exist" errors is NOT a
fix: it steps over every stale-but-present olean and then reports "converged"
while the target still fails. Build the whole cone, in dependency order, from
source. It is cheap — the `WenzlSchurElement` cone is 6 modules and ~17 s.

Exits non-zero if any module in the cone fails, printing the first few lines of
each failure.
"""
import os, re, subprocess, sys, time

LEAN_ROOT = "/home/user/qou/folio/quantum-observable-universe/lean"
OUT = os.path.join(LEAN_ROOT, ".lake/build/lib/lean")
IMPORT_RE = re.compile(r"^\s*import\s+(QOU(?:\.[A-Za-z0-9_']+)*)\s*$", re.M)


def src_of(mod):
    return os.path.join(LEAN_ROOT, mod.replace(".", "/") + ".lean")


def imports_of(mod):
    p = src_of(mod)
    if not os.path.isfile(p):
        return None  # not a QOU source module we can build
    with open(p, encoding="utf-8", errors="replace") as f:
        return IMPORT_RE.findall(f.read())


def closure(root):
    """Topologically ordered list of QOU modules, dependencies first."""
    order, seen, stack = [], {}, [(root, False)]
    while stack:
        mod, expanded = stack.pop()
        if expanded:
            if seen.get(mod) != "done":
                seen[mod] = "done"
                order.append(mod)
            continue
        if seen.get(mod) == "done":
            continue
        if seen.get(mod) == "open":
            continue  # cycle guard; Lean forbids these anyway
        deps = imports_of(mod)
        if deps is None:
            seen[mod] = "done"
            continue
        seen[mod] = "open"
        stack.append((mod, True))
        for d in deps:
            if seen.get(d) != "done":
                stack.append((d, False))
    return order


def build(mod):
    out = os.path.join(OUT, mod.replace(".", "/") + ".olean")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    t0 = time.time()
    r = subprocess.run(["lean", src_of(mod), "-o", out],
                       capture_output=True, text=True, cwd=LEAN_ROOT, timeout=900)
    return r.returncode, time.time() - t0, (r.stdout + r.stderr)


def main():
    root = sys.argv[1]
    mods = closure(root)
    print(f"cone of {root}: {len(mods)} QOU modules", flush=True)
    failures = []
    for i, m in enumerate(mods, 1):
        rc, dt, log = build(m)
        status = "ok " if rc == 0 else "FAIL"
        print(f"[{i:3}/{len(mods)}] {status} {dt:6.1f}s  {m}", flush=True)
        if rc != 0:
            failures.append((m, log.strip().splitlines()[:4]))
    print(f"\n=== {len(mods) - len(failures)}/{len(mods)} built, "
          f"{len(failures)} failed", flush=True)
    for m, log in failures:
        print(f"\n--- {m}")
        for line in log:
            print(f"    {line}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
