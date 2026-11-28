import Mathlib.Algebra.Ring.GeomSum
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

/-!
# Why the brane tower weights level `n` by `ℏ_q^(2n)`: exponent = order × level

The tower `T(ρ) = Σ_n ℏ_q^(2n) Δ⁽ⁿ⁾(ρ)` (`obs:brane-tower-q-laplacian-decay`) uses iterates of a
second-order q-Laplacian. This file shows where the power of `ℏ_q` comes from, with no `ℝ`.

Write `u = q⁻¹`, so `ℏ_q = 1 − u`. The scale-free first difference `δ f(x) = f(x) − f(u x)` has
eigenvalue `1 − uᵏ` on the mode `xᵏ`. By the geometric sum,

  `1 − uᵏ = (1 − u) · [k]_u`,  `[k]_u = 1 + u + ⋯ + u^(k−1)`.

So each difference carries exactly one `ℏ_q`, and an operator of order `r` iterated `n` times
carries `ℏ_q^(r n)` times the prefactor `[k]_u^(r n)` (`level_eig`). With `r = 2` (Laplacian)
this is the tower weight `ℏ_q^(2n)` (`laplacian_level_eig`).

The prefactor `[k]_u` equals `k` at `u = 1`, so for `k ≥ 1` it has no zero at the classical point
and adds no pole to the energy reading. The pole of a level factor
(`LevelWeightEnergy.energy_hbar_zpow_mul`) therefore comes from `ℏ_q` alone, and its size is
order × level.

Not derived here: which mode `k` a lepton occupies (that fixes the prefactor), and why the mass
should carry the inverse weight `ℏ_q^(−2n)` rather than the tower's `ℏ_q^(2n)`.
-/

namespace QOU.MassTheory.LevelWeightOrder

variable {R : Type*} [CommRing R]

/-- The q-integer `[k]_u = Σ_{i<k} uⁱ`. -/
def qInt (u : R) (k : ℕ) : R := ∑ i ∈ Finset.range k, u ^ i

/-- **One difference carries one `ℏ_q`:** `1 − uᵏ = (1 − u)·[k]_u`. -/
theorem diff_eig (u : R) (k : ℕ) : 1 - u ^ k = (1 - u) * qInt u k := by
  unfold qInt
  have h := geom_sum_mul u k
  linear_combination h

/-- **Order `r`, level `n`:** `(1 − uᵏ)^(r n) = (1 − u)^(r n) · [k]_u^(r n)`. -/
theorem level_eig (u : R) (k r n : ℕ) :
    (1 - u ^ k) ^ (r * n) = (1 - u) ^ (r * n) * qInt u k ^ (r * n) := by
  rw [diff_eig, mul_pow]

/-- **Laplacian (`r = 2`):** level `n` carries `ℏ_q^(2n)`. -/
theorem laplacian_level_eig (u : R) (k n : ℕ) :
    (1 - u ^ k) ^ (2 * n) = (1 - u) ^ (2 * n) * qInt u k ^ (2 * n) :=
  level_eig u k 2 n

/-- **The prefactor at the classical point:** `[k]_1 = k`. -/
theorem qInt_one (k : ℕ) : qInt (1 : R) k = k := by
  simp [qInt]

end QOU.MassTheory.LevelWeightOrder
