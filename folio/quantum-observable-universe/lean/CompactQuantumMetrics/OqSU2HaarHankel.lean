import CompactQuantumMetrics.OqSU2HaarPositivity
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic

/-!
# The Haar Gram matrix on the weight-zero block: a q-Hilbert (Hankel) matrix

Bean `qou-wkgp` (well-typed Plancherel statement), O_q(SU(2)) side.

Haar on `O_q(SU(2))` is torus-invariant, so it vanishes off the weight-zero block, which in
the PBW basis of `OqSU2PBW.lean` is spanned by `ζ^k` (`ζ = βγ`). The Haar Gram matrix of
that block is the Hankel matrix of moments `h(ζ^{j+k}) = haarMoment (j + k)
= (-q)^{j+k} / [j+k+1]_{q²}` (`haarState_zeta_pow`): a signed q-Hilbert matrix.

* `haarHankel N`: the `N × N` Hankel matrix of Haar moments.
* `haarHankel_eq_gram`: its entries are `h(ζ^j ζ^k)` (Gram matrix of the PBW monomials `ζ^k`).
* `haarHankel_det_two`: `det H₂ = q⁴ / ([2]²_{q²} [3]_{q²})`, using `[2]² − [3] = q²`.

## Conjecture (not proved here)

`det H_N = q^{N(N−1)} · D_N(q²)`, with `D_N` the q-Hilbert determinant
`det (1/[j+k+1]_{q²})`, which has a product form in q-factorials, the q-analogue of
Cauchy's Hilbert determinant `∏ (k!)⁴ / ((2k)! (2k+1)!)`. Equivalently, `det H_N` is the
product of the squared norms of the first `N` monic orthogonal polynomials of the Haar
moment functional (little q-Legendre). This is the Plancherel product on the weight-zero
block. No empirical value enters.
-/

namespace QOU.AlgebraicSubstrate.OqSU2

variable {K : Type*} [Field K] (q : Kˣ)

/-- The `N × N` Hankel matrix of Haar moments, `(H_N)_{jk} = haarMoment (j + k)`. -/
noncomputable def haarHankel (N : ℕ) : Matrix (Fin N) (Fin N) K :=
  Matrix.of fun j k => haarMoment q ((j : ℕ) + k)

/-- The Hankel matrix is the Haar Gram matrix of the PBW monomials `ζ^k`. -/
theorem haarHankel_eq_gram (N : ℕ) (j k : Fin N) :
    haarHankel q N j k = haarState q (zeta q ^ (j : ℕ) * zeta q ^ (k : ℕ)) := by
  rw [← pow_add, haarState_zeta_pow]
  rfl

/-- `det H₂ = q⁴ / ([2]²_{q²} [3]_{q²})`, when `[2]_{q²}` and `[3]_{q²}` are non-zero. -/
theorem haarHankel_det_two (h2 : qSqNum q 1 ≠ 0) (h3 : qSqNum q 2 ≠ 0) :
    (haarHankel q 2).det = (q : K) ^ 4 / (qSqNum q 1 ^ 2 * qSqNum q 2) := by
  rw [Matrix.det_fin_two]
  simp only [haarHankel, Matrix.of_apply, Fin.val_zero, Fin.val_one, haarMoment]
  have e1 : qSqNum q 1 = 1 + (q : K) ^ 2 := by
    simp [qSqNum, Finset.sum_range_succ]
  have e2 : qSqNum q 2 = 1 + (q : K) ^ 2 + (q : K) ^ 4 := by
    simp [qSqNum, Finset.sum_range_succ]
  have e0 : qSqNum q 0 = 1 := by simp [qSqNum]
  simp only [Nat.add_zero, Nat.zero_add, show (1 : ℕ) + 1 = 2 from rfl, e0, e1, e2] at h2 h3 ⊢
  field_simp
  ring

end QOU.AlgebraicSubstrate.OqSU2
