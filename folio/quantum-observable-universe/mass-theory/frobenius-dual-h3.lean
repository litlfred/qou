import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.Tactic

/-!
# Frobenius dual `K^∨` in `H_3(q)`

Given the non-degenerate Frobenius Gram matrix
`G : Matrix n n R` (entries `G_{ij} = tr_M(b_i · b_j)`), the
**Frobenius dual** of a coordinate vector `c` (state
`K = Σ_i c_i b_i`) is the coordinate vector

```
K^∨ = c · G⁻¹      (so (K^∨)_j = Σ_i c_i (G⁻¹)_{ij}).
```

Its defining property is the recovery of the original coordinates
under the Gram pairing: `⟨K^∨, b_j⟩_F = c_j`, i.e. `(K^∨) ⬝ G = c`.

-- Ref: [leitner2026] def:frobenius-dual-h3
-- Ref: [kassel1995] Kassel, "Quantum Groups," GTM 155, Springer (1995)
-/

namespace QOU.Archimedean

open Matrix

variable {n : Type*} [Fintype n] [DecidableEq n]
variable {R : Type*} [CommRing R]

/-- The **Frobenius dual** coordinate vector `K^∨ = c · G⁻¹` of a
state with coordinate vector `c`, relative to the Gram matrix `G`. -/
noncomputable def frobeniusDual (G : Matrix n n R) (c : n → R) : n → R :=
  c ᵥ* G⁻¹

/-- Defining property of the Frobenius dual: pairing `K^∨` back
through the Gram matrix `G` recovers the original coordinates,
provided `G` is invertible (`⟨K^∨, b_·⟩_F = c`). -/
theorem frobeniusDual_pairing
    (G : Matrix n n R) (c : n → R) (hG : IsUnit G.det) :
    (frobeniusDual G c) ᵥ* G = c := by
  unfold frobeniusDual
  rw [vecMul_vecMul, Matrix.nonsing_inv_mul G hG, vecMul_one]

end QOU.Archimedean
