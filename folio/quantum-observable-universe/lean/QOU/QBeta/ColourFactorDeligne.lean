import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.Kronecker
import Mathlib.Data.Fin.VecNotation
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Data.Real.Basic

/-!
# A colour tensor factor cannot enlarge the ruled Q_β cell

Issue #8833, front 3 (owner 2026-11-21, "1 and 3 simultaneously").
Pre-registration: `computations/probes/qbeta_colour_factor/PREREGISTRATION.md`.

## Setting

The ruled cell is `ε_p(X) = q·tr_{W_p}(X)/[2]³`, `ε_n(X) = q⁻¹·tr_{W_n}(X)/[2]³` on
`X = V³`, `V = σ₀σ₁⁻¹` (`QOU/QBeta/FlavourWeightSplit.lean`). Its strands carry isospin only.

Give each strand colour too: the strand object is `C² ⊠ C^N` in the Deligne product of
`Rep U_q(sl₂)` and `Rep U_q(sl_N)`. The braid then acts by a Kronecker product
`ρ₂(X) ⊗ ρ_N(X)`, and the K-weighted trace of a Kronecker product is the product of the two
traces (`trace_kronecker_mul`). So the colour sector multiplies `ε_p` and `ε_n` by the **same**
factor `F(X)`: the colour quantum trace divided by its normaliser.

## What is proved

* `S0`, `S1` (the 2-dim `(2,1)` representation of `H₃(q)`) satisfy the Hecke and braid
  relations (`hecke_S0`, `hecke_S1`, `braid_S`), and `S1inv` is the inverse of `S1`.
* `chi21_V3`: `χ_(2,1)(V³) = 2 − h⁴[3]`, `h = q − q⁻¹`. The one-dimensional characters give
  `χ_(3)(V³) = χ_(1³)(V³) = 1` (`chiTriv_V3`, `chiSign_V3`).
* `weyl_sum`: `Σ_λ f_λ dim_q S_λ(C^N) = [N]³` on three strands, for symbolic `a = q^N`.
* `colourFactorV3_eq`: the full colour trace on `V³`, normalised by `[N]³`, is
  `1 − h⁴·[N−1][N+1]/[N]²`, and `qn_pm_one`: `[N−1][N+1] = [N]² − 1`.
* `colourFactorV3_lt_one`: for real `1 < q < a` (i.e. rank `N ≥ 2`), the factor is `< 1`.
* `framing_drops`: scaling `σ ↦ c·σ` (the sl_N framing) leaves `V = σ₀σ₁⁻¹` unchanged.
* `singletScalar_V_pow`: on the colour singlet `Λ^N_q`, every `σᵢ` acts by `−q⁻¹c` and
  `σᵢ⁻¹` by its inverse, so every `V^k` acts by `1`.

Scope (b) for this family, invariant named: the factor is `1 − h⁴(1 − 1/[N]²) ≤ 1` (full
trace), `1/[N]³`-weighted or `1` (singlet), so no member reaches the `F ≈ 2.404` the cell
needs. Nothing here is fitted or selected.
-/

set_option linter.unnecessarySeqFocus false

namespace QOU.QBeta.ColourFactorDeligne

open Matrix

section Generic

variable {R : Type*} [Field R]

/-- `h = q − q⁻¹`. -/
def hh (q : R) : R := q - q⁻¹

/-- `[3] = q² + 1 + q⁻²`. -/
def q3 (q : R) : R := q ^ 2 + 1 + q⁻¹ ^ 2

/-- `[2] = q + q⁻¹`. -/
def q2 (q : R) : R := q + q⁻¹

/-- The 2-dim `(2,1)` representation of `H₃(q)`: generator `σ₀`. -/
def S0 (q : R) : Matrix (Fin 2) (Fin 2) R := !![-q⁻¹, 1; 0, q]

/-- The 2-dim `(2,1)` representation of `H₃(q)`: generator `σ₁`. -/
def S1 (q : R) : Matrix (Fin 2) (Fin 2) R := !![q, 0; 1, -q⁻¹]

/-- `σ₁⁻¹`, written out. -/
def S1inv (q : R) : Matrix (Fin 2) (Fin 2) R := !![q⁻¹, 0; 1, -q]

theorem hecke_S0 (q : R) (hq : q ≠ 0) :
    (S0 q - !![q, 0; 0, q]) * (S0 q + !![q⁻¹, 0; 0, q⁻¹]) = 0 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [S0, Matrix.mul_apply, Fin.sum_univ_two] <;> field_simp <;> ring

theorem hecke_S1 (q : R) (hq : q ≠ 0) :
    (S1 q - !![q, 0; 0, q]) * (S1 q + !![q⁻¹, 0; 0, q⁻¹]) = 0 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [S1, Matrix.mul_apply, Fin.sum_univ_two] <;> field_simp <;> ring

theorem braid_S (q : R) (hq : q ≠ 0) : S0 q * S1 q * S0 q = S1 q * S0 q * S1 q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [S0, S1, Matrix.mul_apply, Fin.sum_univ_two] <;> field_simp <;> ring_nf <;> simp

theorem S1_mul_S1inv (q : R) (hq : q ≠ 0) : S1 q * S1inv q = 1 := by
  simp only [S1, S1inv, Matrix.mul_fin_two, Matrix.one_fin_two]
  ext i j; fin_cases i <;> fin_cases j <;> simp [hq]

/-- `σ₁⁻¹ = σ₁ − h·1` (the Hecke rewrite). -/
theorem S1inv_eq (q : R) : S1inv q = S1 q - !![hh q, 0; 0, hh q] := by
  ext i j; fin_cases i <;> fin_cases j <;> simp [S1inv, S1, hh] <;> ring

/-- The photon vertex `V = σ₀σ₁⁻¹` on the `(2,1)` block. -/
def Vmat (q : R) : Matrix (Fin 2) (Fin 2) R := S0 q * S1inv q

/-- `χ_(2,1)(V³) = 2 − h⁴[3]`. -/
theorem chi21_V3 (q : R) (hq : q ≠ 0) :
    trace (Vmat q * Vmat q * Vmat q) = 2 - hh q ^ 4 * q3 q := by
  simp only [Vmat, S0, S1inv, Matrix.mul_fin_two, Matrix.trace_fin_two_of, hh, q3]
  field_simp
  ring

/-- `χ_(3)(V³) = 1`: `σᵢ ↦ q`, so `V ↦ q·q⁻¹`. -/
theorem chiTriv_V3 (q : R) (hq : q ≠ 0) : (q * q⁻¹) ^ 3 = 1 := by
  rw [mul_inv_cancel₀ hq, one_pow]

/-- `χ_(1³)(V³) = 1`: `σᵢ ↦ −q⁻¹`, so `V ↦ (−q⁻¹)(−q)`. -/
theorem chiSign_V3 (q : R) (hq : q ≠ 0) : ((-q⁻¹) * (-q)) ^ 3 = 1 := by
  rw [neg_mul_neg, inv_mul_cancel₀ hq, one_pow]

/-- `[N + k]` for `k = -2..2`, with `a = q^N` kept symbolic. -/
def qN (q a : R) : R := (a - a⁻¹) / (q - q⁻¹)
def qNp1 (q a : R) : R := (a * q - (a * q)⁻¹) / (q - q⁻¹)
def qNp2 (q a : R) : R := (a * q ^ 2 - (a * q ^ 2)⁻¹) / (q - q⁻¹)
def qNm1 (q a : R) : R := (a * q⁻¹ - (a * q⁻¹)⁻¹) / (q - q⁻¹)
def qNm2 (q a : R) : R := (a * q⁻¹ ^ 2 - (a * q⁻¹ ^ 2)⁻¹) / (q - q⁻¹)

/-- Quantum dimension of `S_(3)(C^N)`. -/
def dS3 (q a : R) : R := qN q a * qNp1 q a * qNp2 q a / (q2 q * q3 q)

/-- Quantum dimension of `S_(2,1)(C^N)`. -/
def dS21 (q a : R) : R := qNm1 q a * qN q a * qNp1 q a / q3 q

/-- Quantum dimension of `Λ³(C^N)`. -/
def dL3 (q a : R) : R := qNm2 q a * qNm1 q a * qN q a / (q2 q * q3 q)

/-- Standing nondegeneracy hypotheses. -/
structure Good (q a : R) : Prop where
  hq : q ≠ 0
  ha : a ≠ 0
  hq21 : q ^ 2 - 1 ≠ 0
  h2 : q ^ 2 + 1 ≠ 0
  h3 : q ^ 4 + q ^ 2 + 1 ≠ 0
  hN : a ^ 2 - 1 ≠ 0

private lemma qq (q : R) (hq : q ≠ 0) (h : q ^ 2 - 1 ≠ 0) : q - q⁻¹ ≠ 0 := by
  rw [show q - q⁻¹ = (q ^ 2 - 1) / q by field_simp]
  exact div_ne_zero h hq

section Forms
variable (q a : R) (hq : q ≠ 0) (ha : a ≠ 0) (h1 : q ^ 2 - 1 ≠ 0)
include hq ha h1

private lemma f0 : qN q a = (a ^ 2 - 1) * q / (a * (q ^ 2 - 1)) := by
  unfold qN; rw [eq_div_iff (mul_ne_zero ha h1)]; field_simp
private lemma fp1 : qNp1 q a = (a ^ 2 * q ^ 2 - 1) / (a * (q ^ 2 - 1)) := by
  unfold qNp1; rw [eq_div_iff (mul_ne_zero ha h1)]; field_simp
private lemma fp2 : qNp2 q a = (a ^ 2 * q ^ 4 - 1) / (a * q * (q ^ 2 - 1)) := by
  unfold qNp2; rw [eq_div_iff (mul_ne_zero (mul_ne_zero ha hq) h1)]; field_simp
private lemma fm1 : qNm1 q a = (a ^ 2 - q ^ 2) / (a * (q ^ 2 - 1)) := by
  unfold qNm1; rw [eq_div_iff (mul_ne_zero ha h1)]; field_simp
private lemma fm2 : qNm2 q a = (a ^ 2 - q ^ 4) / (a * q * (q ^ 2 - 1)) := by
  unfold qNm2; rw [eq_div_iff (mul_ne_zero (mul_ne_zero ha hq) h1)]; field_simp

end Forms

private lemma f2 (q : R) (hq : q ≠ 0) : q2 q = (q ^ 2 + 1) / q := by
  unfold q2; field_simp
private lemma f3 (q : R) (hq : q ≠ 0) : q3 q = (q ^ 4 + q ^ 2 + 1) / q ^ 2 := by
  unfold q3; field_simp

/-- `Σ_λ f_λ dim_q S_λ(C^N) = [N]³` on three strands (`f_(3) = f_(1³) = 1`, `f_(2,1) = 2`). -/
theorem weyl_sum (q a : R) (g : Good q a) :
    dS3 q a + 2 * dS21 q a + dL3 q a = qN q a ^ 3 := by
  have := g.hq; have := g.ha; have := g.hq21; have := g.h2; have := g.h3
  unfold dS3 dS21 dL3
  rw [f0 q a g.hq g.ha g.hq21, fp1 q a g.hq g.ha g.hq21, fp2 q a g.hq g.ha g.hq21,
    fm1 q a g.hq g.ha g.hq21, fm2 q a g.hq g.ha g.hq21, f2 q g.hq, f3 q g.hq]
  have h4 : 1 + q ^ 2 + q ^ 4 ≠ 0 := by intro h; apply g.h3; linear_combination h
  field_simp
  ring_nf
  field_simp
  ring

/-- `[N−1][N+1] = [N]² − 1`. -/
theorem qn_pm_one (q a : R) (g : Good q a) :
    qNm1 q a * qNp1 q a = qN q a ^ 2 - 1 := by
  have := g.hq; have := g.ha; have := g.hq21
  rw [f0 q a g.hq g.ha g.hq21, fp1 q a g.hq g.ha g.hq21, fm1 q a g.hq g.ha g.hq21]
  field_simp
  ring

/-- The full colour quantum trace on `V³`, normalised by `[N]³`: the characters of `V³` on
the three blocks weighted by the quantum dimensions of the colour Schur functors. -/
def colourFactorV3 (q a : R) : R :=
  (dS3 q a * (q * q⁻¹) ^ 3 + dS21 q a * trace (Vmat q * Vmat q * Vmat q)
    + dL3 q a * ((-q⁻¹) * (-q)) ^ 3) / qN q a ^ 3

theorem qN_ne_zero (q a : R) (g : Good q a) : qN q a ≠ 0 := by
  have := g.hq; have := g.ha; have hqq := qq q g.hq g.hq21
  unfold qN
  refine div_ne_zero ?_ hqq
  rw [show a - a⁻¹ = (a ^ 2 - 1) / a by field_simp]
  exact div_ne_zero g.hN g.ha

/-- **The colour factor on `V³`**: `1 − h⁴·[N−1][N+1]/[N]²`. -/
theorem colourFactorV3_eq (q a : R) (g : Good q a) :
    colourFactorV3 q a = 1 - hh q ^ 4 * (qNm1 q a * qNp1 q a) / qN q a ^ 2 := by
  have hN := qN_ne_zero q a g
  have hw := weyl_sum q a g
  unfold colourFactorV3
  rw [chiTriv_V3 q g.hq, chiSign_V3 q g.hq, chi21_V3 q g.hq]
  have h3ne : q3 q ≠ 0 := by
    rw [f3 q g.hq]; exact div_ne_zero g.h3 (pow_ne_zero _ g.hq)
  have hd : dS21 q a * q3 q = qNm1 q a * qN q a * qNp1 q a := by
    unfold dS21; field_simp
  rw [div_eq_iff (pow_ne_zero 3 hN)]
  have e : dS3 q a + dL3 q a = qN q a ^ 3 - 2 * dS21 q a := by linear_combination hw
  calc dS3 q a * 1 + dS21 q a * (2 - hh q ^ 4 * q3 q) + dL3 q a * 1
      = (dS3 q a + dL3 q a) + 2 * dS21 q a - hh q ^ 4 * (dS21 q a * q3 q) := by ring
    _ = (1 - hh q ^ 4 * (qNm1 q a * qNp1 q a) / qN q a ^ 2) * qN q a ^ 3 := by
      rw [e, hd]; field_simp; ring

/-- The sl_N framing `σ ↦ c·σ` drops out of `V = σ₀σ₁⁻¹`. -/
theorem framing_drops (q c : R) (hc : c ≠ 0) :
    (c • S0 q) * (c⁻¹ • S1inv q) = Vmat q := by
  rw [Matrix.smul_mul, Matrix.mul_smul, smul_smul, mul_inv_cancel₀ hc, one_smul]; rfl

/-- On the colour singlet every `σᵢ` acts by the scalar `s = −q⁻¹c`, `σᵢ⁻¹` by `s⁻¹`, so
every power of `V` acts by `1`. -/
theorem singletScalar_V_pow (s : R) (hs : s ≠ 0) (k : ℕ) : (s * s⁻¹) ^ k = 1 := by
  rw [mul_inv_cancel₀ hs, one_pow]

/-- Flavour-blindness: the K-weighted trace of a Kronecker product factorises, so the colour
factor multiplies the proton and neutron components alike. -/
theorem trace_kronecker_mul {m n : Type*} [Fintype m] [Fintype n] [DecidableEq m]
    [DecidableEq n] (A : Matrix m m R) (B : Matrix n n R) :
    trace (kroneckerMap (· * ·) A B) = trace A * trace B :=
  Matrix.trace_kronecker A B

end Generic

section Real

/-- `[N] > 1` for real `1 < q < a`. -/
theorem qN_gt_one {q a : ℝ} (hq : 1 < q) (ha : q < a) : 1 < qN q a := by
  have hq0 : 0 < q := by linarith
  unfold qN
  have hden : 0 < q - q⁻¹ := by
    have : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
    linarith
  rw [lt_div_iff₀ hden, one_mul]
  have : a⁻¹ < q⁻¹ := inv_strictAnti₀ hq0 ha
  linarith

/-- **Scope (b)**: for every rank `N ≥ 2` (`a = q^N > q`) and every real `q > 1`, the full
colour factor on `V³` is strictly below 1. -/
theorem colourFactorV3_lt_one {q a : ℝ} (hq : 1 < q) (ha : q < a) :
    colourFactorV3 q a < 1 := by
  have hq0 : 0 < q := by linarith
  have ha0 : 0 < a := by linarith
  have hN := qN_gt_one hq ha
  have hhpos : 0 < hh q := by
    unfold hh; have : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq; linarith
  have g : Good q a :=
    { hq := hq0.ne', ha := ha0.ne', hq21 := by nlinarith,
      h2 := by positivity, h3 := by positivity, hN := by nlinarith }
  rw [colourFactorV3_eq q a g, qn_pm_one q a g]
  have hN2 : 0 < qN q a ^ 2 := by positivity
  have : 0 < hh q ^ 4 * (qN q a ^ 2 - 1) / qN q a ^ 2 := by
    apply div_pos _ hN2
    apply mul_pos (by positivity)
    nlinarith
  linarith

end Real

end QOU.QBeta.ColourFactorDeligne
