#!/usr/bin/env python3
"""Which QOU library modules does the library ROOT actually import?

`lake build QOU` builds the import closure of `QOU.lean`.  A module outside that
closure is built by nothing -- not by the root build, and not by any sweep that
starts from the root.  This reports the gap.

Measured 2026-09-07 on main 8432b885fb: 2735 on disk, 890 in the root, 1845 (67%)
outside it, worst BraidKnot at 409 of 435.  Bean qou-g5sp.

Usage:  python3 scripts/lean-root-coverage-audit.py [--package QOU] [--list NS]
"""
import argparse, os, re, sys
from collections import Counter

def measure(lean_dir, lib):
    root_file = os.path.join(lean_dir, lib + ".lean")
    if not os.path.exists(root_file):
        sys.exit(f"no library root at {root_file}")
    root = set(re.findall(rf'^import ({lib}\.[\w.]+)',
                          open(root_file).read(), re.M))
    on_disk = set()
    for dp, _, fs in os.walk(os.path.join(lean_dir, lib)):
        for f in fs:
            if f.endswith(".lean"):
                rel = os.path.relpath(os.path.join(dp, f[:-5]), lean_dir)
                on_disk.add(rel.replace(os.sep, "."))
    return on_disk, root & on_disk, on_disk - root

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
    print(f"  imported by root  {len(covered):5d}")
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
