#!/usr/bin/env python3
"""Spin-colour coupling of conj:s5-so3-fiber-action: is the STATIC (A_5-equivariant)
coupling forced by Schur's lemma?

The coupling must send the generation degree ell (an SO(3) spherical-harmonic level
V_ell on the SPIN divisor sphere) to the COLOUR Wedderburn block E_lambda, A_5-
equivariantly.  By Schur's lemma the space of A_5-equivariant maps V_ell -> E_lambda
has dimension  <chi_{V_ell|A5}, chi_{E_lambda|A5}>_{A_5}  (count of shared irreps).

This script computes those Hom-dimensions for the verified bridge pairs
(ell=1 <-> (3,1,1), ell=2 <-> (3,2)).  If each is 1, the static coupling is UNIQUE
up to scale -- i.e. FORCED, not a free construction choice.  The remaining freedom
(and the genuine open object) is then the DYNAMICAL intertwining of the two Reeb
flows, not the static rep map.

No external deps.
"""
from math import sin, sqrt, pi
import sys

PHI = (1 + sqrt(5)) / 2
# A_5 (icosahedral I) classes: (name, size, rotation angle)
A5_CLASSES = [("E", 1, 0.0), ("C5", 12, 2 * pi / 5), ("C5^2", 12, 4 * pi / 5),
              ("C3", 20, 2 * pi / 3), ("C2", 15, pi)]
A5_IRREPS = {
    "A":  [1, 1, 1, 1, 1],
    "T1": [3, PHI, 1 - PHI, 0, -1],
    "T2": [3, 1 - PHI, PHI, 0, -1],
    "G":  [4, -1, -1, 1, 0],
    "H":  [5, 0, 0, -1, 1],
}


def vell_char(ell, theta):
    """SO(3) character of V_ell at rotation angle theta."""
    if abs(theta) < 1e-12:
        return 2 * ell + 1
    return sin((2 * ell + 1) * theta / 2) / sin(theta / 2)


def inner(chi1, chi2):
    """<chi1, chi2>_{A_5} (chi as values on the 5 classes; real characters)."""
    s = 0.0
    for (_, size, _), a, b in zip(A5_CLASSES, chi1, chi2):
        s += size * a * b
    return s / 60.0


def decompose_into_a5(chi):
    """multiplicities of each A_5 irrep in a class-function chi."""
    out = {}
    for name, irr in A5_IRREPS.items():
        m = round(inner(chi, irr))
        if m:
            out[name] = m
    return out


# V_ell restricted to A_5 (class function via the rotation-angle character)
def vell_on_a5(ell):
    return [vell_char(ell, theta) for (_, _, theta) in A5_CLASSES]


# Colour Wedderburn blocks, as A_5 class functions, via their known A_5 content
# (verified S5|A5: (3,1,1)->T1(+)T2, (3,2)->H).
def block_char(a5_content):
    chi = [0.0] * 5
    for name, mult in a5_content.items():
        for i in range(5):
            chi[i] += mult * A5_IRREPS[name][i]
    return chi


BRIDGE = [
    ("electron", 1, {"T1": 1, "T2": 1}, (3, 1, 1)),   # V_1|A5 = T1 ; (3,1,1)|A5 = T1+T2
    ("muon",     2, {"H": 1},           (3, 2)),       # V_2|A5 = H  ; (3,2)|A5   = H
]

print("=" * 72)
print("Static spin-colour coupling: dim Hom_{A_5}(V_ell, E_lambda) (Schur)")
print("=" * 72)
all_unique = True
for lepton, ell, block_content, lam in BRIDGE:
    v = vell_on_a5(ell)
    e = block_char(block_content)
    vdec = decompose_into_a5(v)
    hom = round(inner(v, e))
    shared = sorted(set(vdec) & set(block_content))
    print(f"\n  {lepton}: ell={ell}")
    print(f"    V_{ell}|A5      = {vdec}")
    print(f"    E_{lam}|A5 = {block_content}")
    print(f"    shared A5 irreps = {shared}")
    print(f"    dim Hom_A5(V_{ell}, E_{lam}) = <chi_V, chi_E> = {hom}")
    if hom != 1:
        all_unique = False

print()
print("=" * 72)
print("VERDICT")
print("=" * 72)
print(f"  every bridge pair has dim Hom_A5 = 1: {all_unique}")
print("  => the STATIC A_5-equivariant coupling V_ell -> E_lambda is UNIQUE up to")
print("     scale (the isotypic projection onto the shared irrep: T1 for the")
print("     electron, H for the muon).  It is FORCED, not a construction choice.")
print("  => the genuine OPEN object is the DYNAMICAL intertwining: the coupling")
print("     must intertwine the spin Hopf Reeb flow (S^3) with the colour")
print("     Sasakian Reeb flow (S^5), a contact-geometric condition NOT implied")
print("     by the static (Schur-forced) rep map.  Concretely: the spin-ell Reeb")
print("     eigenvalue must resonate with the colour-lambda Reeb eigenvalue.")
print("  NUMEROLOGY GUARD: no claim is made that this resonance pins q0 or any")
print("  observable -- that would need the eigenvalues derived, not matched.")

assert all_unique, "static coupling must be Schur-unique (dim Hom = 1) for both generations"
print("\nSTATIC-COUPLING-FORCED ASSERTION VERIFIED.")
sys.exit(0)
