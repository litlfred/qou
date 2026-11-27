import CompactQuantumMetrics.OqSU2BudgetLittleQJacobi

/-!
# QOU.FluidDynamics.q_ns_block_ladder — how X₊ and X₋ couple the weight blocks
# `(αγ)^r · K[ζ]`

Bean `qou-q3dc` (q-NS Part A, `conj:regularity-breakdown`), triad front, part (b):
the coupling between weight blocks. Part (a), integration by parts on a general block,
is done in the q-Bessel thread.

`X₊ζ^{k+1}` lies in `ζ^k · αγ` (`fieldPlus_zeta_pow`), so `X₊` leaves the Cartan block
`K[ζ]` for the block spanned by `(αγ)ζ^k`. Repeating that gives the blocks
`B_r = (αγ)^r · K[ζ]`, `r ≥ 0`. This file computes `X₊` and `X₋` on them.

## Results

* `fieldPlus_alphaGamma_pow`: `X₊((αγ)^r) = 0`. Each `(αγ)^r` is killed by `X₊`.
* `fieldPlus_ladder`: `X₊((αγ)^r ζ^{k+1}) = q⁻¹[k+1]_{q⁻²} · (αγ)^{r+1} ζ^k`.
  So `X₊` maps block `r`, `ζ`-degree `k+1`, to block `r+1`, degree `k`, and keeps
  `r + k` fixed. On `B_r` it is a single shift with no mixing.
* `fieldMinus_alphaGamma`: `X₋(αγ) = 1 + (q + q⁻¹) ζ`. So `X₋` maps `B_1` back into
  `K[ζ]`, to degrees 0 and 1.
* `block_mul`: `((αγ)^r ζ^j) · ((αγ)^s ζ^k) = q^{−2js} · (αγ)^{r+s} ζ^{j+k}`. The block
  index and the `ζ`-degree both add. This is the selection rule for a triad that
  couples the blocks.
* `ladder_coeff_pos`: for `0 < q` the ladder coefficient `q⁻¹[k+1]_{q⁻²}` is positive,
  so no step of the ladder is cut. At `q = 1` it is `k + 1`. That is a statement about the
  coefficient only, with no limit taken.

## Not established

* That these blocks, the ladder and the block product carry the q-NS dynamics. The
  corpus defines no `∇_q` on `O_q(SU(2))` (see `q_ns_twisted_transport`).
* `X₋` on `B_r` for `r ≥ 2`, and the blocks with negative `r` (`(βδ)^{|r|} K[ζ]`).
* Any transfer rate along a solution, and Part A.

Everything is algebraic, so the file stays out of `QOU/Transcendental/`. No empirical
value enters any proof.

-- Ref: [woronowicz1987-twisted-su2] (the relations of `S_μU(2)`)
-- Ref: [leitner2026] (`conj:regularity-breakdown`)
-/

namespace QOU.FluidDynamics.BlockLadder

open QOU.AlgebraicSubstrate QOU.AlgebraicSubstrate.OqSU2

section Ring

variable {R : Type*} [CommRing R] (q : Rˣ)

local notation "qi" => (((q⁻¹ : Rˣ) : R))

/-- `X₊(αγ) = 0`, because `X₊α = 0` and `X₊γ = 0`. -/
theorem fieldPlus_alphaGamma : fieldPlus q (α (R := R) q * γ q) = 0 := by
  obtain ⟨ha, -, hg, -⟩ := fieldPlus_generators (R := R) q
  rw [field_leibniz, ha, hg, zero_mul, mul_zero, add_zero]

/-- `X₊((αγ)^r) = 0`. -/
theorem fieldPlus_alphaGamma_pow (r : ℕ) :
    fieldPlus q ((α (R := R) q * γ q) ^ r) = 0 := by
  induction r with
  | zero => rw [pow_zero]; exact field_one q 0 1 0
  | succ r ih => rw [pow_succ, field_leibniz, ih, fieldPlus_alphaGamma, zero_mul, mul_zero,
      add_zero]

/-- `ζ^j αγ = q^{−2j} αγ ζ^j`. -/
theorem zetaB_pow_alphaGamma (j : ℕ) :
    zetaB (R := R) q ^ j * (α q * γ q) = (qi * qi) ^ j • ((α q * γ q) * zetaB q ^ j) := by
  rw [alphaGamma_zeta_pow, smul_smul, ← mul_pow,
    show qi * qi * ((q : R) * q) = 1 by
      rw [mul_mul_mul_comm, Units.inv_mul, one_mul], one_pow, one_smul]

/-- `ζ^j (αγ)^s = q^{−2js} (αγ)^s ζ^j`. -/
theorem zetaB_pow_alphaGamma_pow (j s : ℕ) :
    zetaB (R := R) q ^ j * (α q * γ q) ^ s =
      ((qi * qi) ^ j) ^ s • ((α q * γ q) ^ s * zetaB q ^ j) := by
  induction s with
  | zero => simp
  | succ s ih =>
    rw [pow_succ, ← mul_assoc, ih, smul_mul_assoc, mul_assoc, zetaB_pow_alphaGamma,
      mul_smul_comm, smul_smul, ← mul_assoc, ← pow_succ, pow_succ]

/-- **The block product.** `((αγ)^r ζ^j)((αγ)^s ζ^k) = q^{−2js} (αγ)^{r+s} ζ^{j+k}`. -/
theorem block_mul (r j s k : ℕ) :
    ((α (R := R) q * γ q) ^ r * zetaB q ^ j) * ((α q * γ q) ^ s * zetaB q ^ k) =
      ((qi * qi) ^ j) ^ s • ((α q * γ q) ^ (r + s) * zetaB q ^ (j + k)) := by
  calc ((α (R := R) q * γ q) ^ r * zetaB q ^ j) * ((α q * γ q) ^ s * zetaB q ^ k)
      = (α q * γ q) ^ r * (zetaB q ^ j * (α q * γ q) ^ s) * zetaB q ^ k := by
        simp only [mul_assoc]
    _ = ((qi * qi) ^ j) ^ s • ((α q * γ q) ^ (r + s) * zetaB q ^ (j + k)) := by
        rw [zetaB_pow_alphaGamma_pow, mul_smul_comm, smul_mul_assoc, pow_add, pow_add]
        simp only [mul_assoc]

/-- **The ladder.** `X₊((αγ)^r ζ^{k+1}) = q⁻¹[k+1]_{q⁻²} · (αγ)^{r+1} ζ^k`. -/
theorem fieldPlus_ladder (r k : ℕ) :
    fieldPlus q ((α (R := R) q * γ q) ^ r * zetaB q ^ (k + 1)) =
      (qi * jk (qi * qi) (k + 1)) • ((α q * γ q) ^ (r + 1) * zetaB q ^ k) := by
  have hrev := jk_reverse (show qi * qi * ((q : R) * q) = 1 by
    rw [mul_mul_mul_comm, Units.inv_mul, one_mul]) k
  rw [field_leibniz, fieldPlus_alphaGamma_pow, zero_mul, zero_add, fieldPlus_zeta_pow,
    mul_smul_comm, zetaB_pow_alphaGamma, mul_smul_comm, smul_smul, ← mul_assoc, ← pow_succ,
    ← hrev]
  congr 1
  ring

/-- `X₋(αγ) = 1 + (q + q⁻¹) ζ`. -/
theorem fieldMinus_alphaGamma :
    fieldMinus q (α (R := R) q * γ q) = 1 + ((q : R) + qi) • zetaB q := by
  obtain ⟨ha, -, hg, -⟩ := fieldMinus_generators (R := R) q
  obtain ⟨-, -, tg, -⟩ := field_twist_generators (R := R) q
  rw [field_leibniz, ha, hg, tg, alpha_delta, mul_smul_comm,
    show β (R := R) q * γ q = zetaB q from rfl, add_smul]
  abel

end Ring

section Ordered

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- For `0 < q` the ladder coefficient `q⁻¹[k+1]_{q⁻²}` is positive. -/
theorem ladder_coeff_pos (q : Kˣ) (hq : 0 < (q : K)) (k : ℕ) :
    0 < (((q⁻¹ : Kˣ) : K)) * jk ((((q⁻¹ : Kˣ) : K)) * (((q⁻¹ : Kˣ) : K))) (k + 1) := by
  have hi : 0 < (((q⁻¹ : Kˣ) : K)) := by
    rw [Units.val_inv_eq_inv_val]; exact inv_pos.2 hq
  have hj : 0 < jk ((((q⁻¹ : Kˣ) : K)) * (((q⁻¹ : Kˣ) : K))) (k + 1) := by
    induction k with
    | zero => simp
    | succ k ih => rw [jk_succ']; positivity
  positivity

end Ordered

end QOU.FluidDynamics.BlockLadder
