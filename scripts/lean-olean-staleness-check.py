#!/usr/bin/env python3
"""Verify Lean files and auto-repair the stale dependency oleans that break them.

WHY THIS EXISTS. A stale olean does not announce itself. It presents as a *code*
defect in the file that imports it, and a convincing one:

    olean predates a `class` being added   ->  "Function expected at QCollatz,
                                                but this term has type Type"
    olean predates a field being added     ->  "Invalid field `trace_pairing`:
                                                the environment does not contain ..."

Both were hit on 2026-08-30 in one session (bean `qou-ruo1`), on sources that
were correct and unchanged on `main`. Each cost a detour through "is my Lean
wrong?" before anyone compared the artefacts. This script runs that loop.

WHY IT DOES NOT USE TIMESTAMPS. Two timestamp discriminators were tried and BOTH
fail in this environment, for the same structural reason — measured, not assumed:

  * olean mtime vs source mtime: a container clone stamps EVERY source with the
    checkout time while oleans come from a `lake-cache/*` restore built weeks
    earlier. Reported 945 stale, i.e. the whole tree.
  * olean mtime vs the source's last COMMIT time: agent clones here are SHALLOW
    (190 commits), so `git log -1` returns a date inside the fetched window for
    essentially every file. `AdelicSubstrate.lean` reports "committed
    2026-08-29" though its source predates that by months. Reported 945 — the
    identical number, which is what exposed the problem.

A tool that flags the entire tree is the same as a tool that flags nothing. So
staleness is decided the only way that is sound here: by asking Lean. That costs
a few seconds per file, which is affordable precisely because the useful scope
is "the files this change touches", never the whole tree.

USAGE

    # the files a branch changes, vs its merge-base with main (the default)
    scripts/lean-olean-staleness-check.py

    # explicit files
    scripts/lean-olean-staleness-check.py path/to/A.lean path/to/B.lean

    # diagnose only; do not rebuild anything
    scripts/lean-olean-staleness-check.py --no-repair

On a failure it extracts the QOU modules the file imports, rebuilds each IN
PLACE into the same LEAN_PATH root, and retries. Rebuilding in place is not a
detail: LEAN_PATH does not fall through between roots — Lean resolves a module
from the first root that owns the namespace and does not fall back — so an olean
written to a second root is invisible to the consumer that needs it.

It never runs `lake build`, which would evict a restored cache.

Exit status: 0 if every file verifies (after repair), 1 otherwise.
"""
import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PKGS = [
    ("content/quantum-observable-universe/lean", "QOU"),
    ("content/unital-groebner-bases/lean", "UGB"),
    ("content/fred2005-formal-groups/lean", "Fred2005"),
]


def lean_env():
    """LEAN_PATH over every package build root, plus the toolchain on PATH."""
    roots = []
    for p in sorted((REPO / ".lake" / "packages").glob("*/.lake/build/lib/lean")):
        roots.append(str(p))
    for rel, _ in PKGS:
        r = REPO / rel / ".lake" / "build" / "lib" / "lean"
        if r.is_dir():
            roots.append(str(r))
    env = dict(os.environ)
    env["LEAN_PATH"] = ":".join(roots)
    env["ELAN_NO_OVERRIDE_NOTICE"] = "1"
    elan = Path.home() / ".elan" / "bin"
    if elan.is_dir():
        env["PATH"] = f"{elan}:{env.get('PATH','')}"
    return env


def module_to_source(mod: str):
    """Map a dotted module name to its .lean source, or None if not ours."""
    for rel, lib in PKGS:
        if mod == lib or mod.startswith(lib + "."):
            p = REPO / rel / (mod.replace(".", "/") + ".lean")
            if p.is_file():
                return p, REPO / rel
    return None


def local_imports(src: Path):
    """The in-repo modules a file imports (Mathlib and friends excluded)."""
    out = []
    for line in src.read_text(errors="replace").splitlines():
        m = re.match(r"^import\s+([A-Za-z0-9_.]+)", line)
        if m:
            hit = module_to_source(m.group(1))
            if hit:
                out.append((m.group(1), hit[0], hit[1]))
    return out


def run_lean(src: Path, env, out=None):
    cmd = ["lean", str(src)]
    if out is not None:
        out.parent.mkdir(parents=True, exist_ok=True)
        cmd += ["-o", str(out)]
    r = subprocess.run(cmd, cwd=REPO, env=env, capture_output=True,
                       text=True, timeout=1800)
    return r.returncode, (r.stdout + r.stderr)


def changed_files():
    """Lean files this branch changes against its merge-base with origin/main."""
    try:
        base = subprocess.run(["git", "merge-base", "HEAD", "origin/main"],
                              cwd=REPO, capture_output=True, text=True,
                              timeout=60).stdout.strip()
        if not base:
            return []
        names = subprocess.run(["git", "diff", "--name-only", base, "HEAD"],
                               cwd=REPO, capture_output=True, text=True,
                               timeout=120).stdout.split()
    except subprocess.TimeoutExpired:
        return []
    return [REPO / n for n in names if n.endswith(".lean") and (REPO / n).is_file()]


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="*", help="Lean files (default: this "
                    "branch's changed files vs origin/main)")
    ap.add_argument("--no-repair", action="store_true",
                    help="diagnose only; never rebuild a dependency olean")
    args = ap.parse_args()

    targets = [Path(f).resolve() for f in args.files] or changed_files()
    if not targets:
        print("no Lean files to check")
        return 0

    env = lean_env()
    failed, repaired = [], []

    for src in targets:
        rel = src.relative_to(REPO)
        code, log = run_lean(src, env)
        if code == 0:
            print(f"  ok        {rel}")
            continue

        deps = local_imports(src)
        if args.no_repair or not deps:
            print(f"  FAIL      {rel}")
            for line in log.splitlines()[:4]:
                print(f"            {line}")
            failed.append(rel)
            continue

        # Rebuild each in-repo dependency IN PLACE, then retry. A dependency
        # whose own build fails is reported rather than silently skipped.
        print(f"  stale?    {rel} — rebuilding {len(deps)} dependency olean(s)")
        for mod, dep_src, pkg_root in deps:
            root = pkg_root / ".lake" / "build" / "lib" / "lean"
            dcode, dlog = run_lean(dep_src, env,
                                   out=root / (mod.replace(".", "/") + ".olean"))
            status = "rebuilt" if dcode == 0 else "FAILED"
            print(f"            {status}  {mod}")
            if dcode != 0:
                for line in dlog.splitlines()[:3]:
                    print(f"                      {line}")

        code, log = run_lean(src, env)
        if code == 0:
            print(f"  REPAIRED  {rel} — was a stale dependency olean, not a "
                  f"source defect")
            repaired.append(rel)
        else:
            print(f"  FAIL      {rel} — survives dependency rebuild, so this "
                  f"is a real source defect")
            for line in log.splitlines()[:4]:
                print(f"            {line}")
            failed.append(rel)

    print()
    print(f"checked {len(targets)}  repaired {len(repaired)}  failed {len(failed)}")
    for r in failed:
        print(f"  still failing: {r}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
