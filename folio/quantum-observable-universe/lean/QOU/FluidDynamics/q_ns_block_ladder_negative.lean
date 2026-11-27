import CompactQuantumMetrics.OqSU2BudgetLittleQJacobi

/-!
# QOU.FluidDynamics.q_ns_block_ladder_negative — the X₋ ladder on the blocks
# `(βδ)^r · K[ζ]`

Bean `qou-q3dc` (q-NS Part A, `conj:regularity-breakdown`), triad front, part (b). This is
the mirror of `q_ns_block_ladder` (#9690), which treats `(αγ)^r · K[ζ]`. The Haar
integration by parts on a general weight block pairs `(αγ)^s K[ζ]` with
`(βδ)^s K[ζ]` (#9707), so it needs `X₋` and `X₊` on these blocks.

## Results

* `fieldMinus_betaDelta_pow`: `X₋((βδ)^r) = 0`, since `X₋β = X₋δ = 0`.
* `zetaB_pow_betaDelta`: `ζ^k βδ = q^{2k} βδ ζ^k`.
* `fieldMinus_ladder`: `X₋((βδ)^r ζ^{k+1}) = [k+1]_{q²} · (βδ)^{r+1} ζ^k`. So `X₋` takes
  block `−r` at degree `k+1` to block `−(r+1)` at degree `k`.
* `block_mul_neg`: `((βδ)^r ζ^j)((βδ)^s ζ^k) = q^{2js} (βδ)^{r+s} ζ^{j+k}`.
* `haarState_fieldPlus_betaDelta`: `h(X₊(βδ)) = 0`. This checks the first case of
  `h ∘ X₊ = 0`. It uses `X₊(βδ) = q + (q²+1)ζ` and `h(ζ) = −q/(1+q²)`.

## Not established

* `h ∘ X₊ = 0` in general. The general integration by parts on weight blocks needs it.
* `X₊` on `(βδ)^r K[ζ]` for `r ≥ 2`.
* That any of this carries the q-NS dynamics (the corpus has no `∇_q` on `O_q(SU(2))`).
  Part A is not addressed.

Everything is algebraic, so the file stays out of `QOU/Transcendental/`.

-- Ref: [woronowicz1987-twisted-su2] (the relations and Haar state of `S_μU(2)`)
-- Ref: [leitner2026] (`conj:regularity-breakdown`)
-/

namespace QOU.FluidDynamics.BlockLadderNeg

open QOU.AlgebraicSubstrate QOU.AlgebraicSubstrate.OqSU2

section Ring

variable {R : Type*} [CommRing R] (q : Rˣ)

local notation "qi" => (((q⁻¹ : Rˣ) : R))

/-- `X₋(βδ) = 0`. -/
theorem fieldMinus_betaDelta : fieldMinus q (β (R := R) q * δ q) = 0 := by
  obtain ⟨-, hb, -, hd⟩ := fieldMinus_generators (R := R) q
  rw [field_leibniz, hb, hd, zero_mul, mul_zero, add_zero]

/-- `X₋((βδ)^r) = 0`. -/
theorem fieldMinus_betaDelta_pow (r : ℕ) :
    fieldMinus q ((β (R := R) q * δ q) ^ r) = 0 := by
  induction r with
  | zero => rw [pow_zero]; exact field_one q 0 0 1
  | succ r ih => rw [pow_succ, field_leibniz, ih, fieldMinus_betaDelta, zero_mul, mul_zero,
      add_zero]

/-- `ζ βδ = q² βδ ζ`. -/
theorem zetaB_betaDelta :
    zetaB (R := R) q * (β q * δ q) = ((q : R) * q) • ((β q * δ q) * zetaB q) := by
  rw [betaDelta_zeta, smul_smul,
    show (q : R) * q * (qi * qi) = 1 by rw [mul_mul_mul_comm, Units.mul_inv, one_mul],
    one_smul]

/-- `ζ^k βδ = q^{2k} βδ ζ^k`. -/
theorem zetaB_pow_betaDelta (k : ℕ) :
    zetaB (R := R) q ^ k * (β q * δ q) = ((q : R) * q) ^ k • ((β q * δ q) * zetaB q ^ k) := by
  induction k with
  | zero => simp
  | succ k ih =>
    rw [pow_succ', mul_assoc, ih, mul_smul_comm, ← mul_assoc, zetaB_betaDelta, smul_mul_assoc,
      smul_smul, mul_assoc, ← pow_succ', ← pow_succ]

/-- `ζ^j (βδ)^s = q^{2js} (βδ)^s ζ^j`. -/
theorem zetaB_pow_betaDelta_pow (j s : ℕ) :
    zetaB (R := R) q ^ j * (β q * δ q) ^ s =
      (((q : R) * q) ^ j) ^ s • ((β q * δ q) ^ s * zetaB q ^ j) := by
  induction s with
  | zero => simp
  | succ s ih =>
    rw [pow_succ, ← mul_assoc, ih, smul_mul_assoc, mul_assoc, zetaB_pow_betaDelta,
      mul_smul_comm, smul_smul, ← mul_assoc, ← pow_succ, pow_succ]

/-- **The block product.** `((βδ)^r ζ^j)((βδ)^s ζ^k) = q^{2js} (βδ)^{r+s} ζ^{j+k}`. -/
theorem block_mul_neg (r j s k : ℕ) :
    ((β (R := R) q * δ q) ^ r * zetaB q ^ j) * ((β q * δ q) ^ s * zetaB q ^ k) =
      (((q : R) * q) ^ j) ^ s • ((β q * δ q) ^ (r + s) * zetaB q ^ (j + k)) := by
  calc ((β (R := R) q * δ q) ^ r * zetaB q ^ j) * ((β q * δ q) ^ s * zetaB q ^ k)
      = (β q * δ q) ^ r * (zetaB q ^ j * (β q * δ q) ^ s) * zetaB q ^ k := by
        simp only [mul_assoc]
    _ = _ := by
        rw [zetaB_pow_betaDelta_pow, mul_smul_comm, smul_mul_assoc, pow_add, pow_add]
        simp only [mul_assoc]

/-- **The ladder.** `X₋((βδ)^r ζ^{k+1}) = [k+1]_{q²} · (βδ)^{r+1} ζ^k`. -/
theorem fieldMinus_ladder (r k : ℕ) :
    fieldMinus q ((β (R := R) q * δ q) ^ r * zetaB q ^ (k + 1)) =
      jk ((q : R) * q) (k + 1) • ((β q * δ q) ^ (r + 1) * zetaB q ^ k) := by
  have hrev := jk_reverse (show (q : R) * q * (qi * qi) = 1 by
    rw [mul_mul_mul_comm, Units.mul_inv, one_mul]) k
  rw [field_leibniz, fieldMinus_betaDelta_pow, zero_mul, zero_add, fieldMinus_zeta_pow,
    mul_smul_comm, zetaB_pow_betaDelta, mul_smul_comm, smul_smul, ← mul_assoc, ← pow_succ,
    ← hrev]
  congr 1
  ring

end Ring

section Haar

variable {K : Type*} [Field K] (q : Kˣ)

/-- `h(X₊(βδ)) = 0`, the first case of `h ∘ X₊ = 0`. -/
theorem haarState_fieldPlus_betaDelta (hq : ∀ n, qSqNum q n ≠ 0) :
    haarState q (fieldPlus q (β (R := K) q * δ q)) = 0 := by
  have h1 := haarState_zetaB_pow q 1
  have h0 := haarState_zetaB_pow q 0
  rw [pow_one] at h1
  rw [pow_zero] at h0
  rw [fieldPlus_betaDelta, map_add, map_smul, map_smul, h1, h0]
  simp only [haarMoment, smul_eq_mul]
  have := hq 0
  have := hq 1
  simp [qSqNum, Finset.sum_range_succ] at *
  field_simp
  ring

end Haar

end QOU.FluidDynamics.BlockLadderNeg
