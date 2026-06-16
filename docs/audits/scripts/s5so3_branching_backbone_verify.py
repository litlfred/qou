#!/usr/bin/env python3
"""Self-contained verification of the S5 -> S3 branching backbone claimed in
docs/audits/2026-06-13-s5-so3-fiber-action-functor-resolution.md.

No external deps. Uses the symmetric-group branching rule:
  Res^{S_n}_{S_{n-1}} (irrep lambda) = sum over mu obtained by removing one
  removable corner box from the Young diagram of lambda.
Restriction S5 -> S3 = two successive single-box removals.
Dimension via the hook-length formula.
"""
from math import factorial
from collections import Counter
from functools import reduce


def removable_corners(lam):
    """Indices i of rows from which one box can be removed keeping a partition."""
    out = []
    for i in range(len(lam)):
        nxt = lam[i + 1] if i + 1 < len(lam) else 0
        if lam[i] > nxt:  # this row is strictly longer than the next
            out.append(i)
    return out


def remove_box(lam, i):
    new = list(lam)
    new[i] -= 1
    if new[i] == 0:
        new = new[:i]
    return tuple(new)


def restrict_one(lam):
    return [remove_box(lam, i) for i in removable_corners(lam)]


def restrict(lam, steps):
    """Multiset (Counter) of irreps after `steps` single-box restrictions."""
    cur = Counter({tuple(lam): 1})
    for _ in range(steps):
        nxt = Counter()
        for mu, mult in cur.items():
            for nu in restrict_one(mu):
                nxt[nu] += mult
        cur = nxt
    return cur


def hook_dim(lam, n):
    """dim of S_n irrep lambda via hook-length formula."""
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            arm = row - j - 1
            leg = sum(1 for k in range(i + 1, len(lam)) if lam[k] > j)
            prod *= (arm + leg + 1)
    return factorial(n) // prod


def fmt(counter):
    parts = []
    for mu in sorted(counter, reverse=True):
        m = counter[mu]
        s = "(" + ",".join(map(str, mu)) + ")"
        parts.append(s if m == 1 else f"{m}*{s}")
    return " + ".join(parts)


def diff(a, b):
    out = Counter()
    for k in set(a) | set(b):
        d = a[k] - b[k]
        if d:
            out[k] = d
    return out


print("=== S5 irrep dims (hook-length) ===")
for lam in [(3, 2), (2, 2, 1), (3, 1, 1)]:
    print(f"  dim {lam} = {hook_dim(lam, 5)}")

print("\n=== Branching S5 -> S3 (two box removals) ===")
b_32 = restrict((3, 2), 2)     # ell=2 (muon), 5-dim block
b_311 = restrict((3, 1, 1), 2)  # ell=1 (electron), 6-dim block
print(f"  (3,2)   downto S3 = {fmt(b_32)}")
print(f"  (3,1,1) downto S3 = {fmt(b_311)}")

print("\n=== Doc claims (2026-06-13 functor-resolution) ===")
claim_32 = Counter({(3,): 1, (2, 1): 2})
claim_311 = Counter({(1, 1, 1): 1, (2, 1): 2, (3,): 1})
ok_32 = (b_32 == claim_32)
ok_311 = (b_311 == claim_311)
print(f"  (3,2)   == (3) + 2*(2,1)            : {ok_32}")
print(f"  (3,1,1) == (1,1,1) + 2*(2,1) + (3)  : {ok_311}")

print("\n=== electron(3,1,1) - muon(3,2) restriction difference ===")
d = diff(b_311, b_32)
print(f"  difference = {fmt(d)}")
ok_diff = (d == Counter({(1, 1, 1): 1}))
print(f"  == exactly the sign rep (1,1,1)      : {ok_diff}")

print("\n=== dim conservation check (sum dim_{S3} mu == dim_{S5} lambda) ===")
for lam, br in [((3, 2), b_32), ((3, 1, 1), b_311)]:
    tot = sum(mult * hook_dim(mu, 3) for mu, mult in br.items())
    print(f"  {lam}: sum = {tot}, dim_S5 = {hook_dim(lam,5)}, match = {tot == hook_dim(lam,5)}")

all_ok = ok_32 and ok_311 and ok_diff
print("\nALL BACKBONE CLAIMS VERIFIED:" , all_ok)
import sys
sys.exit(0 if all_ok else 1)
