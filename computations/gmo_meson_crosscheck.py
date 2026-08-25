#!/usr/bin/env python3
"""SUPERSEDED 2026-08-07 — the comparison this script set up is a category error.

DO NOT cite the ~3.3% figure below as a QOU prediction for the Gell-Mann-Okubo
deviation, and do not compare it against the ~6% experimental deviation.

Two independent reasons, the first now machine-checked:

1. GMO HAS NO DISCRIMINATING POWER. For first-order SU(3) breaking,
   m^2(I,Y) = a + b*Y + c*(I(I+1) - Y^2/4), the combination
   4 m_K^2 - 3 m_eta^2 - m_pi^2 vanishes IDENTICALLY in a, b, c. Proved
   sorry-free over any commutative ring in
   QOU/Eightfold/GellMannOkuboIdentity.lean (`gmo_identity`), together with
   `gmo_cannot_discriminate` (two arbitrarily different breaking patterns give
   the same value, zero) and `gmo_independent_of_breaking_strength` (the
   hypercharge coefficient b cancels exactly). So reproducing GMO is not
   evidence for ANY mechanism, QOU's included.

2. THE 3.3% IS THE WRONG KIND OF QUANTITY. It is the q-deformation of
   dim_q(adjoint) — a DIMENSION, not a mass splitting. It cannot appear on
   either side of GMO.

What survives: the quantum-dimension arithmetic below is correct and is kept
for reference. What is withdrawn: the framing that it bears on GMO.

The reframed open question is the ~6% DEVIATION, which measures the failure of
first-order breaking (second-order terms plus eta-eta' singlet mixing). The
framework has derived no second-order term, so it currently predicts deviation
0. Bean qou-8pl2. Note the eta-eta' mixing route is downstream of the singlet
channel, which at N=2 does not exist at all (RowCapObstruction.lean).

Additional hygiene defect, unfixed: q0 is hardcoded to 1.11 below rather than
read from the q-pinning witness (a canonical-watcher violation). Not corrected
here because the script is no longer load-bearing.

--- original docstring follows ---

Cross-check: Gell-Mann-Okubo mass relation from q-deformed crossing energy.

The GMO relation for the pseudoscalar meson octet is:
  4 m²_K = 3 m²_η + m²_π

We check whether the QOU crossing-energy model E_×(q) = (q - q^{-1})/2
reproduces this, given the meson braid representations.

The meson mass in QOU arises from the Markov trace on the braid:
  m(meson) ~ |τ_q(β_meson)|

For the pseudoscalar mesons, the relevant braiding is on H_3(q) with
the fundamental ⊗ conjugate representation. The quantum dimension
splitting gives:

  dim_q(π) ~ [2]_q (isospin triplet contribution)
  dim_q(K) ~ [2]_q × [1]_q (mixed isospin-strangeness)
  dim_q(η) ~ ([2]_q² - 1)/[2]_q (adjoint trace)

But the actual mass formula involves the Wedderburn partition channels
and the crossing energy, not just the quantum dimensions.

This script computes the meson-octet quantum dimensions as functions
of q and checks the GMO relation at q = q₀ ≈ 1.11."""

from fractions import Fraction
import math

def q_int(n, q):
    """[n]_q = (q^n - q^{-n}) / (q - q^{-1})"""
    if abs(q - 1) < 1e-15:
        return float(n)
    return (q**n - q**(-n)) / (q - q**(-1))

def q_factorial(n, q):
    """[n]_q! = [1]_q [2]_q ... [n]_q"""
    result = 1.0
    for k in range(1, n + 1):
        result *= q_int(k, q)
    return result

def q_dim_su3(lam1, lam2, q):
    """Quantum dimension of SU(3) irrep with highest weight (lam1, lam2).
    
    dim_q(λ₁, λ₂) = [λ₁+1]_q [λ₂+1]_q [λ₁+λ₂+2]_q / [2]_q
    """
    return (q_int(lam1 + 1, q) * q_int(lam2 + 1, q) * 
            q_int(lam1 + lam2 + 2, q) / q_int(2, q))

# At q = 1: classical dimensions
print("=== Classical dimensions (q=1) ===")
for name, lam in [("3 (fund)", (1, 0)), 
                   ("3̄ (conj)", (0, 1)),
                   ("8 (adj)", (1, 1)),
                   ("6 (sym²)", (2, 0)),
                   ("10 (sym³)", (3, 0)),
                   ("1 (triv)", (0, 0))]:
    d = q_dim_su3(lam[0], lam[1], 1.0 + 1e-10)
    print(f"  dim({name}) = {d:.1f}")

# At q₀ ≈ 1.11: q-deformed dimensions
q0 = 1.11  # approximate observed substrate parameter
print(f"\n=== q-deformed dimensions (q₀ = {q0}) ===")
for name, lam in [("3 (fund)", (1, 0)), 
                   ("3̄ (conj)", (0, 1)),
                   ("8 (adj)", (1, 1)),
                   ("6 (sym²)", (2, 0)),
                   ("10 (sym³)", (3, 0)),
                   ("1 (triv)", (0, 0))]:
    d = q_dim_su3(lam[0], lam[1], q0)
    print(f"  dim_q({name}) = {d:.6f}")

# Meson masses via quantum Casimir
# The mass-squared of a meson state at weight (I₃, Y) in the octet
# gets a contribution from the quadratic Casimir:
#   C₂(λ₁, λ₂) = (λ₁² + λ₂² + λ₁λ₂ + 3λ₁ + 3λ₂) / 3
# q-deformed: C₂^q(λ) = [C₂(λ)]_q

def casimir_su3(lam1, lam2):
    """Quadratic Casimir of SU(3) irrep."""
    return (lam1**2 + lam2**2 + lam1*lam2 + 3*lam1 + 3*lam2) / 3.0

# Meson masses from flavor-SU(3) breaking
# In the standard quark model with SU(3) breaking parameter ε:
#   m²_π = B(m_u + m_d)
#   m²_K = B(m_u + m_s)
#   m²_η = B(m_u + m_d + 4m_s) / 3
# GMO: 4m²_K = 3m²_η + m²_π → 4B(m_u+m_s) = B(m_u+m_d+4m_s) + B(m_u+m_d)
#                              = 4Bm_u + 4Bm_s + 2Bm_d - 2Bm_d
# holds if m_u ≈ m_d (isospin symmetry)

print("\n=== Gell-Mann-Okubo cross-check (experimental) ===")
# Experimental masses (MeV):
m_pi = 139.57  # charged pion
m_K = 493.68   # charged kaon
m_eta = 547.86  # eta

gmo_lhs = 4 * m_K**2
gmo_rhs = 3 * m_eta**2 + m_pi**2
gmo_ratio = gmo_lhs / gmo_rhs

print(f"m_π = {m_pi} MeV")
print(f"m_K = {m_K} MeV")
print(f"m_η = {m_eta} MeV")
print(f"4m²_K = {gmo_lhs:.0f} MeV²")
print(f"3m²_η + m²_π = {gmo_rhs:.0f} MeV²")
print(f"Ratio 4m²_K / (3m²_η + m²_π) = {gmo_ratio:.6f}")
print(f"Deviation from GMO: {abs(1 - gmo_ratio)*100:.2f}%")

# The GMO relation holds to ~7% experimentally
# (exact SU(3) flavour symmetry would give 1.000)

# q-deformed Casimir splitting
print(f"\n=== q-deformed Casimir at q₀ = {q0} ===")
# Octet Casimir
c2_8 = casimir_su3(1, 1)  # = 3
# Fundamental Casimir
c2_3 = casimir_su3(1, 0)  # = 4/3
# The mass splitting within the octet comes from the 
# SU(3)-breaking through strange quark mass, not from Casimir alone.

print(f"C₂(8) = {c2_8:.4f}")
print(f"C₂(3) = {c2_3:.4f}")
print(f"[C₂(8)]_q = {q_int(c2_8, q0):.6f}")
print(f"[C₂(3)]_q = {q_int(c2_3, q0):.6f}")

# Crossing energy
E_cross = 0.5 * (q0 - q0**(-1))
print(f"\nCrossing energy E_×(q₀) = (q₀ - q₀⁻¹)/2 = {E_cross:.6f}")

# q-integer values relevant to mass formulas
print(f"\n=== q-integers at q₀ = {q0} ===")
for n in [1, 2, 3, 4, 5, 6]:
    print(f"  [{n}]_q = {q_int(n, q0):.6f}")

print(f"\n=== SUMMARY ===")
print(f"GMO experimental: holds to {abs(1-gmo_ratio)*100:.1f}%")
print(f"The q-deformation at q₀ ≈ {q0} modifies SU(3) dimensions by")
print(f"  dim_q(8)/dim(8) = {q_dim_su3(1,1,q0)/8:.6f}")
print(f"  dim_q(3)/dim(3) = {q_dim_su3(1,0,q0)/3:.6f}")
print(f"This is a {abs(1-q_dim_su3(1,1,q0)/8)*100:.1f}% deformation")
print(f"of the adjoint dimension, comparable to the GMO deviation.")
