#!/usr/bin/env python3
"""Compile the missing Mathlib oleans a QOU module needs, in topological order.

## Why

The restored `lake-cache/qou-<slug>` is short some Mathlib modules.  Seven were
already handled by `scripts/lean-restore-gap-oleans.sh`, which ships prebuilt
oleans on a tiny cache branch.  This builds a *new* gap from source, for when no
prebuilt olean exists yet.

The case it was written for: the full-library sweep reported
`QOU.Eightfold.ObstructionH2Mathlib` UNVERIFIED on a missing
`Mathlib.RepresentationTheory.Homological.GroupCohomology.LowDegree`, and the
LIBRARY ROOT `QOU` is skipped behind it -- so the one module `lake build QOU`
gates on could not be checked in this container at all.  That is a gap in the
gate, not a defect in the corpus, and it is worth closing once rather than
re-diagnosing every session.

## What it does

Walks the seed's transitive imports, collects every module with no olean, orders
them so dependencies come first, and compiles each with `lean -o` into the target
tree.  Additive only: a module that already has an olean is never rebuilt, so this
cannot evict or replace anything the restored cache provides.

Never invokes `lake` -- Lake treats untraced oleans as stale and would evict the
restored cache (AGENTS.md, bean 02kc).  The oleans it writes have no `.trace`
either, so do not `lake build` afterwards; use `lean`-direct or the sweeps.

Usage:
  scripts/lean-build-mathlib-gap-cone.py <Module> [--jobs 3] [--timeout 900]
                                         [--dest DIR] [--dry-run]
"""
import argparse, os, pathlib, re, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor

ROOT = pathlib.Path(__file__).resolve().parent.parent
PKG = ROOT / "folio/quantum-observable-universe/lean"
MATHLIB = PKG / ".lake/packages/mathlib"


def imports_of(mod):
    p = MATHLIB / (mod.replace(".", "/") + ".lean")
    if not p.exists():
        return []
    return re.findall(r"^import\s+([\w.]+)", p.read_text(), re.M)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("seed")
    ap.add_argument("--jobs", type=int, default=3)
    ap.add_argument("--timeout", type=int, default=900)
    ap.add_argument("--dest", default=str(MATHLIB / ".lake/build/lib/lean"))
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    dest = pathlib.Path(a.dest)

    def has_olean(m):
        return (dest / (m.replace(".", "/") + ".olean")).exists()

    # Collect the missing cone.  Recurse only through modules that are THEMSELVES
    # missing: a module with an olean is a leaf here, because everything it needs
    # was already present when it was built.
    seen, stack, missing = set(), [a.seed], []
    while stack:
        m = stack.pop()
        if m in seen:
            continue
        seen.add(m)
        if not has_olean(m):
            missing.append(m)
            stack.extend(i for i in imports_of(m) if i not in seen)
    if not missing:
        print(f"{a.seed}: nothing missing in {dest}")
        return 0

    deps = {m: [i for i in imports_of(m) if i in set(missing)] for m in missing}
    layers, done, todo = [], set(), set(missing)
    while todo:
        layer = sorted(m for m in todo if all(d in done for d in deps[m]))
        if not layer:
            sys.exit(f"import cycle among {len(todo)} modules")
        layers.append(layer)
        done |= set(layer)
        todo -= set(layer)

    print(f"seed        {a.seed}")
    print(f"dest        {dest}")
    print(f"MISSING     {len(missing)} module(s) in {len(layers)} layer(s)")
    if a.dry_run:
        for m in missing:
            print("   ", m)
        return 0

    env = dict(os.environ)
    env["LEAN_PATH"] = os.pathsep.join(
        [str(dest)] + [str(p / ".lake/build/lib/lean")
                       for p in (PKG / ".lake/packages").iterdir() if p.is_dir()])
    opts = ["-DautoImplicit=false", "-DmaxSynthPendingDepth=3", "-s", "65536"]  # mirror Mathlib lakefile mathlibLeanOptions
    t0, ok, red = time.time(), 0, {}

    def build(m):
        src = MATHLIB / (m.replace(".", "/") + ".lean")
        out = dest / (m.replace(".", "/") + ".olean")
        out.parent.mkdir(parents=True, exist_ok=True)
        tmp = out.with_name(out.name + f".tmp{os.getpid()}")
        try:
            r = subprocess.run(["lean", *opts, str(src), "-o", str(tmp)],
                               cwd=MATHLIB, env=env, capture_output=True,
                               text=True, timeout=a.timeout)
        except subprocess.TimeoutExpired:
            tmp.unlink(missing_ok=True)
            return m, None, f"TIMEOUT after {a.timeout}s"
        if r.returncode == 0 and tmp.exists():
            os.replace(tmp, out)          # atomic; additive, never replaces
        else:
            tmp.unlink(missing_ok=True)
        return m, r.returncode, (r.stdout + r.stderr)

    n = 0
    for layer in layers:
        runnable = [m for m in layer if not any(d in red for d in deps[m])]
        with ThreadPoolExecutor(max_workers=a.jobs) as ex:
            for m, rc, log in ex.map(build, runnable):
                n += 1
                if rc == 0:
                    ok += 1
                    print(f"  [{n}/{len(missing)}] ok   {m}", flush=True)
                else:
                    red[m] = log
                    why = "TIMEOUT" if rc is None else f"exit {rc}"
                    print(f"  [{n}/{len(missing)}] FAIL {m}  ({why})", flush=True)
                    for l in [x for x in log.splitlines() if ": error:" in x][:2]:
                        print(f"        {l}", flush=True)
    print(f"\n=== gap cone: {ok} ok, {len(red)} failed, "
          f"{time.time() - t0:.0f}s ===")
    return 1 if red else 0


if __name__ == "__main__":
    sys.exit(main())
