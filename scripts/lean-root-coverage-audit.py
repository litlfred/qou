#!/usr/bin/env python3
"""Which QOU library modules does the library ROOT actually import?

`lake build QOU` builds the import closure of `QOU.lean`.  A module outside that
closure is built by nothing -- not by the root build, and not by any sweep that
starts from the root.  This reports the gap.

CORRECTED 2026-09-08: this measured the root's DIRECT import lines and called
everything else "not in the root".  `lake build QOU` builds the TRANSITIVE closure,
so the direct count understates coverage badly and the gap was overstated by the
same amount.  On main 1ec22a9040c the two differ by 540 modules:

    direct import lines in QOU.lean       910   <- what this used to report
    TRANSITIVE closure of QOU.lean       1450   <- what `lake build QOU` builds
    outside the root build               1324   (47.7%), not 1863 (67%)

The overstated figure reached bean qou-g5sp's headline, this script's own
docstring, an audit doc and a PR body before being caught.  Quote the transitive
number.  Bean qou-g5sp.

Usage:  python3 scripts/lean-root-coverage-audit.py [--package QOU] [--list NS]
"""
import argparse, os, re, sys
from collections import Counter

def measure(lean_dir, lib):
    root_file = os.path.join(lean_dir, lib + ".lean")
    if not os.path.exists(root_file):
        sys.exit(f"no library root at {root_file}")
    on_disk = set()
    for dp, _, fs in os.walk(os.path.join(lean_dir, lib)):
        for f in fs:
            if f.endswith(".lean"):
                rel = os.path.relpath(os.path.join(dp, f[:-5]), lean_dir)
                on_disk.add(rel.replace(os.sep, "."))

    def imports_of(m):
        f = os.path.join(lean_dir, m.replace(".", os.sep) + ".lean")
        if not os.path.exists(f):
            return []
        return [i for i in re.findall(rf'^import ({lib}\.[\w.]+)',
                                      open(f).read(), re.M) if i in on_disk]

    # TRANSITIVE closure, not the root's direct import lines.  `lake build QOU`
    # builds everything QOU.lean reaches, so a module imported only by another
    # imported module IS built -- counting it as "outside the root" overstates the
    # gap.  Measured difference on this corpus: 910 direct vs 1450 transitive.
    covered, stack = set(), [lib]
    for d in imports_of(lib):
        if d not in covered:
            covered.add(d); stack.append(d)
    while stack:
        for d in imports_of(stack.pop()):
            if d not in covered:
                covered.add(d); stack.append(d)
    covered &= on_disk
    return on_disk, covered, on_disk - covered

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lean-dir", default="content/quantum-observable-universe/lean")
    ap.add_argument("--package", default="QOU")
    ap.add_argument("--list", metavar="NS",
                    help="print every missing module in this namespace")
    a = ap.parse_args()

    on_disk, covered, missing = measure(a.lean_dir, a.package)
    pct = 100 * len(missing) / len(on_disk) if on_disk else 0
    print(f"{a.package} library root coverage")
    print(f"  modules on disk   {len(on_disk):5d}")
    print(f"  root closure      {len(covered):5d}   (transitive, = what `lake build {0}` builds)".format(a.package) if False else f"  root closure      {len(covered):5d}   (TRANSITIVE — what `lake build` builds)")
    print(f"  NOT in the root   {len(missing):5d}   ({pct:.0f}%)")

    if a.list:
        for m in sorted(x for x in missing if x.split(".")[1:2] == [a.list]):
            print("   ", m)
        return 1 if missing else 0

    print("\n  by namespace, worst first:")
    c = Counter(m.split(".")[1] for m in missing if "." in m[len(a.package):].lstrip("."))
    for ns, n in c.most_common(15):
        tot = sum(1 for m in on_disk if m.split(".")[1:2] == [ns])
        print(f"    {ns:28s} {n:5d} missing of {tot}")
    return 1 if missing else 0

if __name__ == "__main__":
    sys.exit(main())
