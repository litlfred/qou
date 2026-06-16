#!/usr/bin/env python3
"""Ingredient-4 geometric-existence constraint: a Schur-Weyl obstruction on the
5-strand fibre of conj:s5-so3-fiber-action.

The geometric leg (the open content of the keystone) asks for a 2I-equivariant
5-strand Reeb realization hosting the lepton generation blocks (electron ->
(3,1,1), muon -> (3,2), verified bridge).  This script checks WHICH S_5 irreps
can live on a 5-strand tensor space (C^d)^{x5}, by Schur-Weyl duality:

    (C^d)^{x5}  =  (+)_{lambda |- 5, rows(lambda) <= d}  S^lambda (x) W^{gl_d}_lambda

so an S_5 irrep lambda appears IFF rows(lambda) <= d.  No external deps.

VERDICT: a SPINOR (C^2) 5-strand space (the 2I rep) annihilates EVERY >=3-row
partition (Temperley-Lieb / sl_2) -- in particular the electron block (3,1,1).
To host the electron the per-strand fibre must be >=3-dimensional (colour C^3).
=> the 2I spin lift lives on the divisor sphere P(C^2), NOT on the strand fibre;
the strands carry colour C^3 (matching '3 colour tubes per nucleon').
"""
from math import factorial
import sys

PARTS5 = [(5,), (4, 1), (3, 2), (3, 1, 1), (2, 2, 1), (2, 1, 1, 1), (1, 1, 1, 1, 1)]


def hook_dim(lam, **kwargs):
    """dim of the S_n irrep lambda (hook-length formula); n = sum(lam)."""
    if "n" in kwargs:
        raise AssertionError(
            "hook_dim's 'n' parameter is removed (n = sum(lam) is redundant); drop it."
        )
    n = sum(lam)
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            arm = row - j - 1
            leg = sum(1 for k in range(i + 1, len(lam)) if lam[k] > j)
            prod *= (arm + leg + 1)
    return factorial(n) // prod


def gld_dim(lam, d):
    """dim of the gl_d Weyl module for lambda (Weyl dimension formula); 0 if rows>d."""
    if len(lam) > d:
        return 0
    l = list(lam) + [0] * (d - len(lam))
    num = 1
    den = 1
    for i in range(d):
        for j in range(i + 1, d):
            num *= (l[i] - l[j] + j - i)
            den *= (j - i)
    return num // den


def report(d):
    """Schur-Weyl content of (C^d)^{x5}; returns the set of hosted partitions."""
    print(f"--- d={d}: (C^{d})^(x5), dim = {d**5} ---")
    hosted = []
    total = 0
    for lam in PARTS5:
        rows = len(lam)
        g = gld_dim(lam, d)
        s = hook_dim(lam)
        if g > 0:
            hosted.append(lam)
            total += s * g
        tag = "  <- ABSENT" if g == 0 else ""
        print(f"  lambda={str(lam):<16} rows={rows} dim_S5={s} mult(=dim_gl{d})={g}{tag}")
    ok = (total == d ** 5)
    print(f"  sum dim_S5 * dim_gl{d} = {total} (= {d}^5 = {d**5}: {ok})")
    return hosted, ok


print("=" * 70)
print("Schur-Weyl: which S5 irreps live on a 5-strand fibre (C^d)^{x5}?")
print("=" * 70)
hosted2, ok2 = report(2)   # spinor C^2 (the 2I / SU(2) spin rep)
print()
hosted3, ok3 = report(3)   # colour C^3 (SU(3) colour, '3 colour tubes per nucleon')

ELECTRON = (3, 1, 1)   # verified bridge: electron ell=1 -> T1 in S5 block (3,1,1)
MUON = (3, 2)          # muon ell=2 -> H in (3,2)

print()
print("=" * 70)
print("VERDICT — ingredient-4 fibre constraint")
print("=" * 70)
e_on_spin = ELECTRON in hosted2
e_on_col = ELECTRON in hosted3
mu_on_spin = MUON in hosted2
print(f"  electron block (3,1,1) on spinor C^2 strands : {e_on_spin}  (rows=3 > 2)")
print(f"  electron block (3,1,1) on colour C^3 strands : {e_on_col}")
print(f"  muon block     (3,2)   on spinor C^2 strands : {mu_on_spin}")
print("  => spinor (C^2) 5-strand space CANNOT host the electron (Temperley-Lieb")
print("     kills all >=3-row partitions).  The strand fibre must be >=3-dim")
print("     (colour C^3).  The 2I spin lift lives on the divisor sphere P(C^2),")
print("     NOT on the strand fibre -- the two spaces must stay distinct.")

# Assertions encode the finding.
assert hosted2 == [(5,), (4, 1), (3, 2)], "spinor content drift"
assert not e_on_spin, "electron must be ABSENT on spinor C^2"
assert mu_on_spin, "muon must be present on spinor C^2"
assert e_on_col, "electron must be present on colour C^3"
assert ok2 and ok3, "Schur-Weyl dimension count must close"
print("\nALL INGREDIENT-4 FIBRE-CONSTRAINT ASSERTIONS VERIFIED.")
sys.exit(0)
