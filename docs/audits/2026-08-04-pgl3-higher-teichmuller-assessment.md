# T3e assessment: PGL(3) higher Teichmüller as route to rank-2 structure

**Date:** 2026-08-04
**Bean:** `qou-52fu` (T3e), epic `qou-8lxd`

## Status: RESEARCH DIRECTION DOCUMENTED — not actionable yet

## 1. The question

Does hyperbolic geometry on the knot complement give SU(3)?

## 2. The answer: NO, but a related construction might

### 2a. Hyperbolic holonomy is rank 1

The holonomy representation of a hyperbolic 3-manifold M is
ρ: π₁(M) → PSL(2,ℂ). This is **rank 1** — it reinforces the
dim V = 2 cap, not circumvents it.

QOU is an SL(2) theory throughout:
- SU(2) gauge group (Descartes condition)
- SL(2,ℂ) holonomy (hyperbolic structures)
- U_q(sl₂) quantum group
- Jones polynomial = sl₂ specialization of HOMFLY

### 2b. The rank-2 generalization: PGL(3,ℂ)

The geometric route to a rank-2 structure on the knot complement is
the **higher Teichmüller theory** of Fock-Goncharov:

- **PGL(N,ℂ) gluing equations:** Garoufalidis-Thurston-Zickert
  generalize the Neumann-Zagier gluing equations from PGL(2,ℂ) to
  PGL(N,ℂ) for any N.
- **Fock-Goncharov coordinates:** Higher coordinates on the moduli
  space of framed PGL(N,ℂ)-local systems on the knot complement.
- **N=3:** A PGL(3,ℂ) decoration would give a rank-2 representation
  ρ₃: π₁(M) → PGL(3,ℂ), and SU(3) is a real form of SL(3,ℂ).

### 2c. Connection to the corpus

The corpus already has Neumann-Zagier / A-polynomial machinery for
PGL(2). Generalizing to PGL(3) would:
1. Provide a 3-dimensional representation on the complement
2. The resulting 3-dim fundamental would be non-self-dual (PGL(3) is
   rank 2 with non-trivial outer automorphism)
3. Connect to the HOMFLY-PT at N=3 (the HOMFLY A-polynomial
   generalizes the Jones A-polynomial to PGL(N))

### 2d. Obstructions

- **Not every knot complement admits a PGL(3,ℂ) structure.** Whether
  the knots in the particle dictionary (trefoil, figure-eight,
  Borromean links) admit non-trivial PGL(3) representations is
  untested.
- **The trefoil (electron) is a torus knot.** Its complement is
  Seifert-fibered, not hyperbolic. The PGL(3) story for Seifert-
  fibered manifolds is different from the hyperbolic case.
- **Mathlib gap:** No PGL(N) gluing equations, no Fock-Goncharov
  coordinates.

## 3. Recommendation

This is a valid research direction but **not actionable in the near
term** without significant new mathematical infrastructure (PGL(3)
gluing equations). The more promising route is the dual-trace approach
from T3b §2c: use the existing Hecke tower with the N=3 Ocneanu
parameter, which requires no new manifold geometry.

Mark as **documented** but leave as **todo** — the PGL(3) route
becomes actionable if/when someone computes PGL(3) representations
for the trefoil, figure-eight, and Borromean links.
