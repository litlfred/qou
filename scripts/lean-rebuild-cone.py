#!/usr/bin/env python3
"""Rebuild a set of QOU modules and their transitive QOU dependency cone, in
topological order, so that `#print axioms` verdicts are about the SOURCE.

WHY THIS EXISTS (2026-08-26)
----------------------------
`#print axioms` reads the LOADED ENVIRONMENT, which comes from `.olean` files.
In a restored container those oleans are a MIXED-VINTAGE cache: measured on this
tree the same day, QOU olean build dates ranged over 2026-06-09 .. 2026-08-26.
An olean built from an older source reports THAT source's axioms.

Verified instance, not a hypothetical. `QOU/MathlibExt/PosSemidefDiagZero.lean`
proves `Matrix.PosSemidef.entry_sq_le_diag_mul` as a THEOREM. Its restored olean
was built 2026-06-09, when the same result was an `axiom`
(`entry_sq_le_diag_mul_axiom`). Two SDP declarations therefore reported a
dependency on an axiom THAT NO LONGER EXISTS IN THE SOURCE; rebuilding that one
module removed it from both cones.

That direction of error is benign (it over-reports assumed mathematics). The
same mechanism runs the other way: a cached olean can report `clean` for a
declaration whose current source has regressed. `lean-axiom-guard.py` does not
check olean freshness -- it assumes the modules are built, not that they are
built FROM THE CURRENT SOURCE. This script is what makes that assumption true.

WHY NOT mtime
-------------
Do not compare olean mtime to source mtime. A git checkout stamps every source
with the clone time and a tar restore preserves the oleans' original build
times, so EVERY restored olean is "older than its source" by construction.
Measured here: 845 of 1046 QOU oleans, which is exactly the set that came from
the tar -- a number that looks like a finding and is an artifact.

WHY NOT `lake build`
--------------------
A restored tree has no `.trace` files, so Lake treats every olean as stale,
rebuilds from source and EVICTS the restore (AGENTS.md, bean qou-r13s). This
uses `lean`-direct with `-o`, which writes the olean without consulting Lake.

Usage
-----
    scripts/lean-rebuild-cone.py --from-guard      # the axiom guard's registry
    scripts/lean-rebuild-cone.py QOU.Foo QOU.Bar   # explicit roots
    scripts/lean-rebuild-cone.py --from-guard --dry-run
    scripts/lean-rebuild-cone.py --selftest        # needs no Lean

`LEAN_PATH` must already be set (see local/lean-environment-setup.md).
Exit codes: 0 = every module rebuilt; 1 = at least one failed; 2 = setup problem.
"""

from __future__ import annotations

import argparse
import os
import pathlib
import re
import subprocess
import sys
import time

LEAN_ROOT = pathlib.Path("content/quantum-observable-universe/lean")
BUILD = LEAN_ROOT / ".lake/build/lib/lean"
IMPORT_RE = re.compile(r"^import\s+(QOU[\w.]*)", re.M)


def module_to_src(m: str) -> pathlib.Path:
    return LEAN_ROOT / (m.replace(".", "/") + ".lean")


def module_to_olean(m: str) -> pathlib.Path:
    return BUILD / (m.replace(".", "/") + ".olean")


def read_imports(m: str) -> list[str]:
    src = module_to_src(m)
    if not src.is_file():
        return []
    return IMPORT_RE.findall(src.read_text())


def topo_cone(roots: list[str], imports_of=read_imports) -> list[str]:
    """Transitive QOU cone of `roots`, dependencies strictly before dependents.

    Iterative post-order with an explicit stack: a recursive walk blows the
    Python stack on this corpus, and the cone is a DAG with long chains.
    A module already on the current path is a cycle -- Lean forbids those, so
    it is skipped rather than treated as an error here.
    """
    order: list[str] = []
    placed: set[str] = set()
    onpath: set[str] = set()
    # (module, expanded?) -- expanded means its deps have already been pushed
    stack: list[tuple[str, bool]] = [(r, False) for r in reversed(roots)]
    while stack:
        m, expanded = stack.pop()
        if expanded:
            onpath.discard(m)
            if m not in placed:
                placed.add(m)
                order.append(m)
            continue
        if m in placed or m in onpath:
            continue
        onpath.add(m)
        stack.append((m, True))
        for d in reversed(imports_of(m)):
            if d not in placed:
                stack.append((d, False))
    return order


def rebuild(modules: list[str], dry_run: bool = False) -> int:
    failures = []
    t0 = time.monotonic()
    for i, m in enumerate(modules, 1):
        src, ol = module_to_src(m), module_to_olean(m)
        if not src.is_file():
            print(f"  [skip] {m}  (no source; package-external)")
            continue
        if dry_run:
            print(f"  [dry ] {m}")
            continue
        ol.parent.mkdir(parents=True, exist_ok=True)
        r = subprocess.run(["lean", str(src), "-o", str(ol)],
                           capture_output=True, text=True)
        if r.returncode != 0:
            failures.append(m)
            print(f"  [FAIL] {i}/{len(modules)} {m}")
            for line in (r.stdout + r.stderr).strip().split("\n")[:4]:
                print(f"         {line}")
        else:
            print(f"  [ok  ] {i}/{len(modules)} {m}")
    dt = time.monotonic() - t0
    print(f"\nrebuilt {len(modules) - len(failures)}/{len(modules)} in {dt:.0f}s")
    if failures:
        print("FAILED: " + ", ".join(failures))
        return 1
    return 0


_SELFTEST_GRAPH = {
    "QOU.A": ["QOU.B", "QOU.C"],
    "QOU.B": ["QOU.D"],
    "QOU.C": ["QOU.D"],
    "QOU.D": [],
    "QOU.Cyc1": ["QOU.Cyc2"],
    "QOU.Cyc2": ["QOU.Cyc1"],
}


def selftest() -> int:
    bad = 0

    def imports_of(m):
        return _SELFTEST_GRAPH.get(m, [])

    order = topo_cone(["QOU.A"], imports_of)
    checks = [
        ("all four reached", len(order) == 4),
        ("D before B", order.index("QOU.D") < order.index("QOU.B")),
        ("D before C", order.index("QOU.D") < order.index("QOU.C")),
        ("B before A", order.index("QOU.B") < order.index("QOU.A")),
        ("C before A", order.index("QOU.C") < order.index("QOU.A")),
        ("no duplicates", len(order) == len(set(order))),
    ]
    # a diamond must not emit the shared dependency twice, and a cycle must
    # terminate rather than hang -- both are the failure modes of the naive
    # recursive version this replaced.
    cyc = topo_cone(["QOU.Cyc1"], imports_of)
    checks.append(("cycle terminates", set(cyc) == {"QOU.Cyc1", "QOU.Cyc2"}))
    for label, ok in checks:
        print(f"  [{'ok  ' if ok else 'FAIL'}] {label}")
        bad += 0 if ok else 1
    print("rebuild-cone selftest: " + ("PASS" if not bad else f"{bad} FAILURE(S)"))
    return 0 if not bad else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("modules", nargs="*", help="root modules (QOU.Foo.Bar)")
    ap.add_argument("--from-guard", action="store_true",
                    help="use lean-axiom-guard.py --print-modules as the roots")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--selftest", action="store_true",
                    help="exercise the topological walk; needs no Lean")
    args = ap.parse_args()

    if args.selftest:
        return selftest()

    roots = list(args.modules)
    if args.from_guard:
        g = subprocess.run([sys.executable, "scripts/lean-axiom-guard.py",
                            "--print-modules"], capture_output=True, text=True)
        if g.returncode != 0:
            print("could not read the guard registry", file=sys.stderr)
            return 2
        roots += g.stdout.split()
    if not roots:
        print("no roots given (use --from-guard or name modules)", file=sys.stderr)
        return 2
    if not LEAN_ROOT.is_dir():
        print(f"run from the repo root ({LEAN_ROOT} not found)", file=sys.stderr)
        return 2
    if not args.dry_run and not os.environ.get("LEAN_PATH"):
        print("LEAN_PATH is unset -- see local/lean-environment-setup.md",
              file=sys.stderr)
        return 2

    cone = topo_cone(roots)
    print(f"{len(roots)} root module(s) -> {len(cone)} in the transitive QOU cone\n")
    return rebuild(cone, args.dry_run)


if __name__ == "__main__":
    raise SystemExit(main())
