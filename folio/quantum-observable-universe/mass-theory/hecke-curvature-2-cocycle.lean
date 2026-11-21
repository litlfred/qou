import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic

/-!
# Hecke curvature 2-cocycle `F`

For the Hecke algebra `H_n(R, q)` with generators `σ_1, …, σ_{n-1}`
subject to the Hecke quadratic relation and the Yang–Baxter braid
relation, the **Hecke curvature 2-cocycle** `F` is defined on
generator pairs by

```
F(σ_i, σ_j) = R_H(i)          if i = j      (Hecke relation residue)
            = R_YB(i)         if |i-j| = 1  (Yang–Baxter residue)
            = [σ_i, σ_j]      if |i-j| ≥ 2  (commutator)
```

and extended by the Leibniz rule. `F` is a Hochschild 2-cochain
measuring the failure of commutativity at each generator pair,
analogous to the curvature `F_A = dA + A ∧ A` of a connection.

This sibling axiomatises the generator-pair residues `R_H` and
`R_YB` and the diagonal vanishing of the cocycle on equal
generators after the Hecke relation is imposed.

-- Ref: [leitner2026] def:hecke-curvature-2-cocycle
-- Ref: [kassel1995] Kassel, "Quantum Groups," GTM 155, Springer (1995)
-/

namespace QOU.WedderburnMass

variable {R : Type*} [CommRing R]

/-- The **Hecke quadratic-relation residue**
`R_H(σ) = σ² - (q - q⁻¹)·σ - 1` for a generator `σ` with deformation
parameter `q` (and its inverse `qinv = q⁻¹` supplied explicitly so
the definition stays over a generic `CommRing`). -/
def heckeResidue (q qinv σ : R) : R :=
  σ * σ - (q - qinv) * σ - 1

/-- The **Yang–Baxter residue**
`R_YB(σ, τ) = στσ - τστ` for adjacent generators `σ, τ`. -/
def ybResidue (σ τ : R) : R :=
  σ * τ * σ - τ * σ * τ

/-- When the Hecke relation `σ² = (q - q⁻¹)·σ + 1` holds, the Hecke
residue of `σ` vanishes — the cocycle has no curvature on a
generator already in normal form. -/
theorem heckeResidue_eq_zero_of_rel
    (q qinv σ : R) (h : σ * σ = (q - qinv) * σ + 1) :
    heckeResidue q qinv σ = 0 := by
  unfold heckeResidue
  rw [h]; ring

end QOU.WedderburnMass
