import QOU.BraidsAndKnots.BorromeanRingColouredTrace

/-!
# The nucleon split from the position-labelled diagonal of `V³`

Beans `qou-myts` (nucleon split), related `qou-99qc`. Pre-registered in
`computations/probes/nucleon_split_v3_diagonal/PREREGISTRATION.md`; audit
`docs/audits/2026-11-27-nucleon-split-v3-diagonal.md`.

## Setting

`BorromeanRingColouredTrace` gives the ring-coloured trace
`τ_c = q^{2T³(c)} ⟨c|V³|c⟩ / [2]_q³` of `V³ = (σ₁σ₂⁻¹)³` for the six colourings: `tauP` on
`W_p` (index `0, 1, 2` = `uud, udu, duu`) and `tauN` on `W_n` (index `0, 1, 2` = `udd, dud, ddu`).
Under the Gibbs map of `NucleonSplitGibbsCoulomb` a pairing `(c_p, c_n)` gives
`m_n − m_p = E₀ · log(τ_p(c_p)/τ_n(c_n))`. This file proves the ratio `τ_p/τ_n` in closed form for
every pairing, and the symmetry of the word that singles out the middle strand.

## What is proved

1. **Strand reversal** (`strandRev_A₁`, `strandRev_A₂Inv`, `strandRev_B₁`, `strandRev_B₂Inv`):
   reversing the strands, `J = antidiag(1,1,1)`, sends `ρ(σ₁)(q)` to `ρ(σ₂)(q⁻¹)⁻¹` and
   `ρ(σ₂)⁻¹(q)` to `ρ(σ₁)(q⁻¹)`, on both weight spaces.
2. **Symmetry of the word** (`strandRev_V3A`, `strandRev_V3B`): `J · V³(q) · J = V³(q⁻¹)ᵀ`.
   So `(σ₁σ₂⁻¹)³` is fixed by strand reversal ∘ bar (`q ↦ q⁻¹`, the mirror) ∘ word reversal
   (transpose; the `ρ(σᵢ)` are symmetric). On the diagonal (`diagA_rev`, `diagB_rev`):
   `⟨rev c|V³|rev c⟩(q) = ⟨c|V³|c⟩(q⁻¹)`. No hypothesis on `q`.
3. **The middle strand** (`pair_rev_fixed_iff`, `braidPart_rev`, `braidPart_middle_bar`): on the
   nine pairings the symmetry acts by `(i, j) ↦ (rev i, rev j)` together with `q ↦ q⁻¹` on the
   braid part `⟨c_p|V³|c_p⟩/⟨c_n|V³|c_n⟩`. The only fixed pairing is `(1, 1)` = `udu ↔ dud`
   (odd quark on the middle strand for both), and its braid part is bar-invariant.
4. **Closed forms** (`ratio_eq`, `ratio_ij` for all nine pairs, `ratio_sameposition_prod`): exact
   rational functions of `q`, under the explicit non-vanishing of the denominator polynomial.

## Scope

Diagonal entries are not conjugation-invariant (`BorromeanRingColouredTrace.tauP_not_conj_invariant`):
a colouring is a boundary condition on the open braid, not a label of the closed Borromean rings.
Point 2 is a symmetry of the word `(σ₁σ₂⁻¹)³`, not of its conjugacy class. No numerical value
enters. Generic `[Field R]`.
-/

namespace QOU.Nuclear.NucleonSplitV3Diagonal

open Matrix
open QOU.BraidsAndKnots.NucleonWeightSpaceTraces
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm
open QOU.BraidsAndKnots.BorromeanRingColouredTrace
open QOU.QBeta.FlavourWeightSplit

variable {R : Type*} [Field R]

/-! ## 1. Strand reversal -/

/-- Strand reversal `i ↦ 2 − i` on a weight space (`uud ↔ duu`, `udd ↔ ddu`, middle fixed). -/
def strandRev : Matrix (Fin 3) (Fin 3) R := !![0, 0, 1; 0, 1, 0; 1, 0, 0]

theorem strandRev_mul_self : (strandRev : Matrix (Fin 3) (Fin 3) R) * strandRev = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [strandRev, Matrix.mul_apply, Fin.sum_univ_three]

/-- Conjugation by `strandRev` is multiplicative. -/
theorem strandRev_conj_mul (M N : Matrix (Fin 3) (Fin 3) R) :
    strandRev * (M * N) * strandRev =
      (strandRev * M * strandRev) * (strandRev * N * strandRev) := by
  have h : (strandRev * M * strandRev) * (strandRev * N * strandRev) =
      strandRev * M * (strandRev * strandRev) * N * strandRev := by
    simp only [Matrix.mul_assoc]
  rw [h, strandRev_mul_self, Matrix.mul_one]
  simp only [Matrix.mul_assoc]

/-- Entry `(i, i)` of `J M J` is entry `(rev i, rev i)` of `M`. -/
theorem strandRev_conj_diag (M : Matrix (Fin 3) (Fin 3) R) (i : Fin 3) :
    (strandRev * M * strandRev : Matrix (Fin 3) (Fin 3) R) i i = M i.rev i.rev := by
  fin_cases i <;>
    simp [strandRev, Matrix.mul_apply, Matrix.vecMul, dotProduct, Fin.sum_univ_three, Fin.rev]

theorem strandRev_A₁ (q : R) : strandRev * A₁ q * strandRev = A₂Inv q⁻¹ := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [strandRev, A₁, A₂Inv, Matrix.mul_apply, Fin.sum_univ_three]

theorem strandRev_A₂Inv (q : R) : strandRev * A₂Inv q * strandRev = A₁ q⁻¹ := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [strandRev, A₁, A₂Inv, Matrix.mul_apply, Fin.sum_univ_three]

theorem strandRev_B₁ (q : R) : strandRev * B₁ q * strandRev = B₂Inv q⁻¹ := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [strandRev, B₁, B₂Inv, Matrix.mul_apply, Fin.sum_univ_three]

theorem strandRev_B₂Inv (q : R) : strandRev * B₂Inv q * strandRev = B₁ q⁻¹ := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [strandRev, B₁, B₂Inv, Matrix.mul_apply, Fin.sum_univ_three]

/-! ## 2. The word `(σ₁σ₂⁻¹)³` is fixed by strand reversal ∘ bar ∘ word reversal -/

theorem A₁_transpose (q : R) : (A₁ q)ᵀ = A₁ q := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [A₁]

theorem A₂Inv_transpose (q : R) : (A₂Inv q)ᵀ = A₂Inv q := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [A₂Inv]

theorem B₁_transpose (q : R) : (B₁ q)ᵀ = B₁ q := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [B₁]

theorem B₂Inv_transpose (q : R) : (B₂Inv q)ᵀ = B₂Inv q := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [B₂Inv]

/-- **`J · V³(q) · J = V³(q⁻¹)ᵀ` on `W_p`.** -/
theorem strandRev_V3A (q : R) :
    strandRev * borromeanV3A q * strandRev = (borromeanV3A q⁻¹)ᵀ := by
  have hV : strandRev * borromeanVA q * strandRev = (borromeanVA q⁻¹)ᵀ := by
    unfold borromeanVA
    rw [strandRev_conj_mul, strandRev_A₁, strandRev_A₂Inv, Matrix.transpose_mul,
      A₁_transpose, A₂Inv_transpose]
  unfold borromeanV3A
  rw [strandRev_conj_mul, strandRev_conj_mul, hV, Matrix.transpose_mul, Matrix.transpose_mul,
    Matrix.mul_assoc]

/-- **`J · V³(q) · J = V³(q⁻¹)ᵀ` on `W_n`.** -/
theorem strandRev_V3B (q : R) :
    strandRev * borromeanV3B q * strandRev = (borromeanV3B q⁻¹)ᵀ := by
  have hV : strandRev * borromeanVB q * strandRev = (borromeanVB q⁻¹)ᵀ := by
    unfold borromeanVB
    rw [strandRev_conj_mul, strandRev_B₁, strandRev_B₂Inv, Matrix.transpose_mul,
      B₁_transpose, B₂Inv_transpose]
  unfold borromeanV3B
  rw [strandRev_conj_mul, strandRev_conj_mul, hV, Matrix.transpose_mul, Matrix.transpose_mul,
    Matrix.mul_assoc]

/-- `⟨rev c|V³|rev c⟩(q) = ⟨c|V³|c⟩(q⁻¹)` on `W_p`. -/
theorem diagA_rev (q : R) (i : Fin 3) :
    borromeanV3A q i.rev i.rev = borromeanV3A q⁻¹ i i := by
  rw [← strandRev_conj_diag (borromeanV3A q) i, strandRev_V3A, Matrix.transpose_apply]

/-- `⟨rev c|V³|rev c⟩(q) = ⟨c|V³|c⟩(q⁻¹)` on `W_n`. -/
theorem diagB_rev (q : R) (i : Fin 3) :
    borromeanV3B q i.rev i.rev = borromeanV3B q⁻¹ i i := by
  rw [← strandRev_conj_diag (borromeanV3B q) i, strandRev_V3B, Matrix.transpose_apply]

/-! ## 3. Pairings, and the one the symmetry fixes -/

/-- The braid part of a pairing: `⟨c_p|V³|c_p⟩ / ⟨c_n|V³|c_n⟩`. -/
def braidPart (q : R) (i j : Fin 3) : R := borromeanV3A q i i / borromeanV3B q j j

/-- The symmetry acts on pairings by `(i, j) ↦ (rev i, rev j)` together with `q ↦ q⁻¹`. -/
theorem braidPart_rev (q : R) (i j : Fin 3) :
    braidPart q i.rev j.rev = braidPart q⁻¹ i j := by
  unfold braidPart; rw [diagA_rev, diagB_rev]

/-- **The middle pairing is the only fixed one.** `(rev i, rev j) = (i, j)` iff `i = j = 1`
(`udu ↔ dud`). -/
theorem pair_rev_fixed_iff (i j : Fin 3) : (i.rev = i ∧ j.rev = j) ↔ (i = 1 ∧ j = 1) := by
  fin_cases i <;> fin_cases j <;> decide

/-- The middle braid part is bar-invariant (independent of the mirror choice of the word). -/
theorem braidPart_middle_bar (q : R) : braidPart q 1 1 = braidPart q⁻¹ 1 1 :=
  braidPart_rev q 1 1

/-! ## 4. The ratio `τ_p/τ_n` in closed form -/

/-- `τ_p(c_p) / τ_n(c_n)` for the pairing `(i, j)`. -/
def ratio (q : R) (i j : Fin 3) : R :=
  tauP q (borromeanV3A q) i / tauN q (borromeanV3B q) j

/-- The `[2]_q³` cancels and the `K`-weights give `q²`. -/
theorem ratio_eq (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (i j : Fin 3) :
    ratio q i j = q ^ 2 * braidPart q i j := by
  have hD : qd2 q ^ 3 ≠ 0 := pow_ne_zero 3 (qd2_ne_zero q hq hq2)
  unfold ratio tauP tauN braidPart
  rw [div_div_div_cancel_right₀ hD, div_eq_mul_inv, div_eq_mul_inv, mul_inv, inv_inv]
  ring

/-- Denominator polynomials. -/
def den0 (q : R) : R := q ^ 6 - 2 * q ^ 4 + 3 * q ^ 2 - 1
def den1 (q : R) : R := (q ^ 4 - q ^ 2 + 1) * (q ^ 8 - 3 * q ^ 6 + 3 * q ^ 4 - 3 * q ^ 2 + 1)
def den2 (q : R) : R := q ^ 6 - 3 * q ^ 4 + 2 * q ^ 2 - 1

theorem diagB_zero' (q : R) (hq : q ≠ 0) : borromeanV3B q 0 0 = den0 q / q ^ 4 := by
  rw [borromeanV3B_diag_zero q hq, den0]

theorem diagB_one' (q : R) (hq : q ≠ 0) : borromeanV3B q 1 1 = -den1 q / q ^ 6 := by
  rw [borromeanV3B_diag_one q hq, den1]; ring

theorem diagB_two' (q : R) (hq : q ≠ 0) : borromeanV3B q 2 2 = -den2 q / q ^ 2 := by
  rw [borromeanV3B_diag_two q hq, den2]

section closed
variable (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
include hq hq2

theorem ratio_00 (h : den0 q ≠ 0) :
    ratio q 0 0 = -q ^ 6 * (q ^ 2 - 2) * (q ^ 4 - q ^ 2 + 1) / den0 q := by
  rw [ratio_eq q hq hq2, braidPart, borromeanV3A_diag_zero q hq, diagB_zero' q hq]
  field_simp

theorem ratio_01 (h : den1 q ≠ 0) :
    ratio q 0 1 = q ^ 8 * (q ^ 2 - 2) * (q ^ 4 - q ^ 2 + 1) / den1 q := by
  rw [ratio_eq q hq hq2, braidPart, borromeanV3A_diag_zero q hq, diagB_one' q hq]
  field_simp

theorem ratio_02 (h : den2 q ≠ 0) :
    ratio q 0 2 = q ^ 4 * (q ^ 2 - 2) * (q ^ 4 - q ^ 2 + 1) / den2 q := by
  rw [ratio_eq q hq hq2, braidPart, borromeanV3A_diag_zero q hq, diagB_two' q hq]
  field_simp

theorem ratio_10 (h : den0 q ≠ 0) : ratio q 1 0 = q ^ 6 / den0 q := by
  rw [ratio_eq q hq hq2, braidPart, borromeanV3A_diag_one q hq, diagB_zero' q hq]
  field_simp

/-- **The middle (structurally selected) pairing `udu ↔ dud`.** -/
theorem ratio_11 (h : den1 q ≠ 0) : ratio q 1 1 = -q ^ 8 / den1 q := by
  rw [ratio_eq q hq hq2, braidPart, borromeanV3A_diag_one q hq, diagB_one' q hq]
  field_simp

theorem ratio_12 (h : den2 q ≠ 0) : ratio q 1 2 = -q ^ 4 / den2 q := by
  rw [ratio_eq q hq hq2, braidPart, borromeanV3A_diag_one q hq, diagB_two' q hq]
  field_simp

theorem ratio_20 (h : den0 q ≠ 0) :
    ratio q 2 0 = (2 * q ^ 2 - 1) * (q ^ 4 - q ^ 2 + 1) / den0 q := by
  rw [ratio_eq q hq hq2, braidPart, borromeanV3A_diag_two q hq, diagB_zero' q hq]
  field_simp

theorem ratio_21 (h : den1 q ≠ 0) :
    ratio q 2 1 = -q ^ 2 * (2 * q ^ 2 - 1) * (q ^ 4 - q ^ 2 + 1) / den1 q := by
  rw [ratio_eq q hq hq2, braidPart, borromeanV3A_diag_two q hq, diagB_one' q hq]
  field_simp

theorem ratio_22 (h : den2 q ≠ 0) :
    ratio q 2 2 = -(2 * q ^ 2 - 1) * (q ^ 4 - q ^ 2 + 1) / (q ^ 2 * den2 q) := by
  rw [ratio_eq q hq hq2, braidPart, borromeanV3A_diag_two q hq, diagB_two' q hq]
  field_simp

/-- The product over the same-position matching (`duu↔udd`, `udu↔dud`, `uud↔ddu`). Every perfect
matching has this product (`ratio_matching_prod_eq`), so its cube root is the class geometric
mean. -/
theorem ratio_sameposition_prod (h0 : den0 q ≠ 0) (h1 : den1 q ≠ 0) (h2 : den2 q ≠ 0) :
    ratio q 2 0 * ratio q 1 1 * ratio q 0 2 =
      -q ^ 12 * (q ^ 2 - 2) * (2 * q ^ 2 - 1) * (q ^ 4 - q ^ 2 + 1) ^ 2 /
        (den0 q * den1 q * den2 q) := by
  rw [ratio_20 q hq hq2 h0, ratio_11 q hq hq2 h1, ratio_02 q hq hq2 h2]
  field_simp

end closed

/-- Any matching has the same product: e.g. the identity matching equals the same-position one. -/
theorem ratio_matching_prod_eq (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    ratio q 0 0 * ratio q 1 1 * ratio q 2 2 = ratio q 2 0 * ratio q 1 1 * ratio q 0 2 := by
  simp only [ratio_eq q hq hq2, braidPart, div_eq_mul_inv]
  ring

end QOU.Nuclear.NucleonSplitV3Diagonal
