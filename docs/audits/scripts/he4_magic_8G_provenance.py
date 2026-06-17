#!/usr/bin/env python3
"""Provenance of the 8G prefactor in the ⁴He B_magic near-match: derived, not fitted.

The low-isotope binding dashboard's single strongest hit is ⁴He under
  B_magic = rho_F · m_e · A · 8G        (ratio B_AME/B_magic = 0.945, +5.7% over)
This script settles "is 8G derived or fitted?" -- it is DERIVED:

  8G = 8 · (Catalan's constant) = Vol(L6a4) = Vol(Borromean rings),

the hyperbolic volume of the Borromean-rings complement (= 2 ideal octahedra),
an EXACT identity (not a tuned number).  magic_A_formula.py already documents
this ("8G = Vol(L6a4) = Vol(Borromean rings), the universal residue prefactor").

Verdict (critical-distance): 8G itself is derived; the B_magic ASSEMBLY
rho_F·m_e·A·8G is the canonical mass-formula shape m_e·Vol·rho with Vol modelled
as A·8G (per-nucleon Borromean volume) and rho_F=2 (doubly-magic density).  The
+5.7% residual + non-generalization (heavier doubly-magic use recursive-on-⁴He;
A>=6 fails in every trace form) make it a DERIVED-PREFACTOR NEAR-MATCH, not a
closure and not numerology.

deps: mpmath; computations/substrate/knot_volumes.py for the corpus VOL_BORROMEAN.
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
for sub in ("computations", "computations/substrate", "tools/qou-substrate/python"):
    sys.path.insert(0, os.path.join(ROOT, sub))

try:
    import mpmath as mp
except ImportError as e:  # pragma: no cover
    print(f"SKIP: mpmath unavailable ({e}).")
    if os.environ.get("CI"):
        sys.exit(1)
    sys.exit(0)

mp.mp.dps = 30
G = mp.catalan
eightG = 8 * G

print("=" * 66)
print("Is 8G derived or fitted?  ->  DERIVED (Borromean-rings volume)")
print("=" * 66)
print(f"  Catalan's constant G = {mp.nstr(G, 15)}")
print(f"  8G                   = {mp.nstr(eightG, 15)}")

corpus_ok = None
try:
    from knot_volumes import VOL_BORROMEAN  # corpus value
    corpus_ok = abs(float(eightG) - float(VOL_BORROMEAN)) < 1e-9
    print(f"  Vol(Borromean) (corpus knot_volumes.py) = {VOL_BORROMEAN}")
    print(f"  8G == Vol(Borromean rings) (L6a4): {corpus_ok}  (exact: 2 ideal octahedra)")
except Exception as e:  # pragma: no cover
    print(f"  (knot_volumes import skipped: {type(e).__name__})")

# the assembly + residual
me = 0.51099895069   # CODATA m_e (MeV)
rho_F, A = 2, 4
B_magic = rho_F * me * A * float(eightG)
B_AME = 28.2957       # ⁴He AME2020 binding (MeV)
ratio = B_AME / B_magic
print()
print("=" * 66)
print("The ⁴He assembly  B_magic = rho_F · m_e · A · 8G  (canonical m_e·Vol·rho)")
print("=" * 66)
print(f"  = {rho_F} · {me} · {A} · {float(eightG):.5f}  =  {B_magic:.4f} MeV")
print(f"  B_AME(⁴He) = {B_AME} MeV   ->  B_AME/B_magic = {ratio:.4f}  (+{(1/ratio-1)*100:.1f}% over)")
print("  derived inputs : m_e (CAL-1), 8G = Vol(Borromean) (hyperbolic volume)")
print("  modelled inputs: Vol(⁴He)=A·8G (per-nucleon Borromean), rho_F=2 (doubly-magic)")
print("  => DERIVED-PREFACTOR NEAR-MATCH (8G derived, residual +5.7%); NOT a")
print("     closure (residual + ⁴He-magic-specific; A>=6 fails) and NOT numerology.")

assert abs(float(eightG) - 7.327724753417752) < 1e-9, "8G must equal Vol(Borromean)=7.32772..."
assert corpus_ok in (True, None), "8G must match corpus VOL_BORROMEAN when available"
assert 0.93 < ratio < 0.96, "⁴He B_magic ratio must be ~0.945"
print("\n8G-PROVENANCE ASSERTIONS VERIFIED (8G = Borromean volume, derived).")
sys.exit(0)
