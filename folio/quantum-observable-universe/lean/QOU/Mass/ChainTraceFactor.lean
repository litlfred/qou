import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic

/-!
# The chain trace factor: `tr₂(σ + d) = z + d`, and why the canonical `L` is a sum

`computations/probes/the_canonical_mass_trace_factorises_over_the_chain_probe.py`
(bean `qou-m3sh`) measured, at 200 bits, that the Markov trace of the full `3A`-strand
canonical atom word is the product over generators of TWO-strand traces of the
per-generator Hecke polynomials — because the closure is a linear connected sum
(`QOU.Mass.TorusKnotPages`, `prop:canonical-closure-torus-chain`) and multiplicative
invariants are multiplicative under connected sum. That multiplicativity is a theorem
about the Hecke algebra which this file does NOT formalise. What it does formalise is
the algebra of the factors, so that the arc's three bond constants rest on an identity
rather than on sixty agreeing digits:

* **The affine law.** On `H₂` under convention D the two blocks are `(2)` and `(1,1)`
  with `σ ↦ q` and `σ ↦ -q⁻¹`, weighted by the Wenzl level-2 weights
  `w₊ = [3]_q / ([3]_q + 1)` and `w₋ = 1 / ([3]_q + 1)`. The two-strand trace of the
  letter `σ + d·1` is therefore `w₊(q + d) + w₋(-q⁻¹ + d)`, and this equals `z + d` with
  `z = q³/(q² + 1)` the Markov weight (`twoStrandTrace_eq`). Every interface generator of
  the canonical word carries exactly one such letter, so its factor is `z + d`.

* **The mirror factor.** `σ⁻¹ = σ - h` with `h = q - q⁻¹`, so the `nn` factor is
  `z - h`, and `z - h = 1 / (q (q² + 1))` (`markovZ_sub_heckeH`): the `pp` and `nn`
  factors multiply to `1/[2]_q²` (`markovZ_mul_mirror`), which is
  `L_pp + L_nn = 2 log(q + q⁻¹)` (`L_pp_add_L_nn`).

* **Positivity.** For `1 ≤ q` all three factors `z`, `z - h`, `z + d_pn` are positive
  (`markovZ_pos`, `mirror_pos`, `pn_factor_pos`), so the bond constants
  `L = -log(z + d)` are defined; and `-log` of a product of positive factors is the sum
  of the `-log`s (`neg_log_prod`). Given the factorisation, the canonical `L` is
  exactly the sum over the `A - 1` interfaces of `-log(z + d_i)`: no many-body term
  exists in the canonical closure. That additive closed form is the one
  `QOU.BraidKnot.BsymLinearChain` (bean `6z40`) took as its named structural input.

Not formalised: the factorisation of the `H_{3A}` trace itself (a theorem about the
Hecke algebra, checked to `1e-59` at `A ≤ 4`), the numerical values at `q₀` (the probe,
60 digits), and the connected-sum topology. Ground field `ℝ`, `q` a free variable with
the hypotheses each statement needs. Bean `qou-m3sh`.
-/

namespace QOU.Mass.ChainTraceFactor

open Finset

/-- The quantum integer `[3]_q = q² + 1 + q⁻²`. -/
noncomputable def qint3 (q : ℝ) : ℝ := q ^ 2 + 1 + (q ^ 2)⁻¹

/-- Wenzl level-2 weight of the row `(2)` in `H₂` under convention D: `[3]_q / ([3]_q + 1)`. -/
noncomputable def wPlus (q : ℝ) : ℝ := qint3 q / (qint3 q + 1)

/-- Wenzl level-2 weight of the column `(1,1)`: `1 / ([3]_q + 1)`. -/
noncomputable def wMinus (q : ℝ) : ℝ := 1 / (qint3 q + 1)

/-- The Markov weight `z = q³ / (q² + 1)`. -/
noncomputable def markovZ (q : ℝ) : ℝ := q ^ 3 / (q ^ 2 + 1)

/-- The Hecke parameter `h = q - q⁻¹`; the quadratic relation is `σ - σ⁻¹ = h`. -/
noncomputable def heckeH (q : ℝ) : ℝ := q - q⁻¹

/-- The interface correction `δ = (q - 1)² (1 - q⁻⁴) / 3` of the `pn` offset. -/
noncomputable def deltaPN (q : ℝ) : ℝ := (q - 1) ^ 2 * (1 - (q ^ 4)⁻¹) / 3

/-- The `pn` offset `d_pn = -h (1 - δ/2) / 2` (`pn_interface_offset`,
`bring_color_weighted` convention). -/
noncomputable def dPN (q : ℝ) : ℝ := -(heckeH q) * (1 - deltaPN q / 2) / 2

/-- Two-strand Markov trace of the letter `σ + d·1`: `σ ↦ q` on `(2)`, `σ ↦ -q⁻¹` on `(1,1)`. -/
noncomputable def twoStrandTrace (q d : ℝ) : ℝ := wPlus q * (q + d) + wMinus q * (-q⁻¹ + d)

lemma qint3_eq (q : ℝ) (hq : q ≠ 0) : qint3 q = (q ^ 4 + q ^ 2 + 1) / q ^ 2 := by
  unfold qint3
  field_simp

lemma qint3_add_one (q : ℝ) (hq : q ≠ 0) : qint3 q + 1 = (q ^ 2 + 1) ^ 2 / q ^ 2 := by
  unfold qint3
  field_simp
  ring

theorem wPlus_eq (q : ℝ) (hq : q ≠ 0) : wPlus q = (q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2 := by
  unfold wPlus
  rw [qint3_add_one q hq, qint3_eq q hq]
  have h1 : q ^ 2 + 1 ≠ 0 := by positivity
  field_simp

theorem wMinus_eq (q : ℝ) (hq : q ≠ 0) : wMinus q = q ^ 2 / (q ^ 2 + 1) ^ 2 := by
  unfold wMinus
  rw [qint3_add_one q hq]
  have h1 : q ^ 2 + 1 ≠ 0 := by positivity
  field_simp

/-- The two weights sum to one. -/
theorem wPlus_add_wMinus (q : ℝ) (hq : q ≠ 0) : wPlus q + wMinus q = 1 := by
  rw [wPlus_eq q hq, wMinus_eq q hq]
  have h1 : q ^ 2 + 1 ≠ 0 := by positivity
  field_simp
  ring

/-- **The affine law.** `tr₂(σ + d) = z + d`. This is the factor every interface
generator of the canonical word contributes. -/
theorem twoStrandTrace_eq (q d : ℝ) (hq : q ≠ 0) : twoStrandTrace q d = markovZ q + d := by
  unfold twoStrandTrace markovZ
  rw [wPlus_eq q hq, wMinus_eq q hq]
  have h1 : q ^ 2 + 1 ≠ 0 := by positivity
  field_simp
  ring

/-- `tr₂(σ) = z`. -/
theorem twoStrandTrace_zero (q : ℝ) (hq : q ≠ 0) : twoStrandTrace q 0 = markovZ q := by
  rw [twoStrandTrace_eq q 0 hq, add_zero]

/-- **The mirror factor.** `tr₂(σ⁻¹) = tr₂(σ - h) = z - h = 1 / (q (q² + 1))`. -/
theorem markovZ_sub_heckeH (q : ℝ) (hq : q ≠ 0) :
    markovZ q - heckeH q = 1 / (q * (q ^ 2 + 1)) := by
  unfold markovZ heckeH
  have h1 : q ^ 2 + 1 ≠ 0 := by positivity
  field_simp
  ring

/-- `tr₂(σ) · tr₂(σ⁻¹) = 1 / [2]_q²`, with `[2]_q = q + q⁻¹`. -/
theorem markovZ_mul_mirror (q : ℝ) (hq : q ≠ 0) :
    markovZ q * (markovZ q - heckeH q) = 1 / (q + q⁻¹) ^ 2 := by
  rw [markovZ_sub_heckeH q hq]
  unfold markovZ
  have h1 : q ^ 2 + 1 ≠ 0 := by positivity
  field_simp

theorem markovZ_pos {q : ℝ} (hq : 0 < q) : 0 < markovZ q := by
  unfold markovZ
  positivity

theorem mirror_pos {q : ℝ} (hq : 0 < q) : 0 < markovZ q - heckeH q := by
  rw [markovZ_sub_heckeH q hq.ne']
  positivity

theorem heckeH_nonneg {q : ℝ} (hq : 1 ≤ q) : 0 ≤ heckeH q := by
  unfold heckeH
  have hq0 : 0 < q := by linarith
  have : q - q⁻¹ = (q ^ 2 - 1) / q := by
    field_simp
  rw [this]
  apply div_nonneg _ hq0.le
  nlinarith

theorem deltaPN_nonneg {q : ℝ} (hq : 1 ≤ q) : 0 ≤ deltaPN q := by
  unfold deltaPN
  have hq0 : 0 < q := by linarith
  have h4 : (q ^ 4)⁻¹ ≤ 1 := by
    rw [inv_le_one₀ (by positivity)]
    nlinarith [sq_nonneg (q - 1), sq_nonneg (q + 1), sq_nonneg (q ^ 2 - 1)]
  have : 0 ≤ 1 - (q ^ 4)⁻¹ := by linarith
  positivity

/-- The `pn` factor `z + d_pn` is at least the `nn` factor `z - h`, hence positive, for `1 ≤ q`:
`d_pn = -h/2 + hδ/4 ≥ -h`. -/
theorem pn_factor_pos {q : ℝ} (hq : 1 ≤ q) : 0 < markovZ q + dPN q := by
  have hq0 : 0 < q := by linarith
  have hh := heckeH_nonneg hq
  have hd := deltaPN_nonneg hq
  have hm := mirror_pos hq0
  unfold dPN
  nlinarith [mul_nonneg hh hd]

/-- `-log` of a product of positive factors is the sum of the `-log`s: given the
factorisation of the trace over the chain, the canonical `L` is a sum over interfaces. -/
theorem neg_log_prod {ι : Type*} (s : Finset ι) (f : ι → ℝ) (hf : ∀ i ∈ s, 0 < f i) :
    -Real.log (∏ i ∈ s, f i) = ∑ i ∈ s, -Real.log (f i) := by
  rw [Real.log_prod s f (fun i hi => (hf i hi).ne'), Finset.sum_neg_distrib]

/-- The three bond constants as `-log` of their two-strand factors. -/
noncomputable def L_pp (q : ℝ) : ℝ := -Real.log (markovZ q)
noncomputable def L_nn (q : ℝ) : ℝ := -Real.log (markovZ q - heckeH q)
noncomputable def L_pn (q : ℝ) : ℝ := -Real.log (markovZ q + dPN q)

/-- `L_pp + L_nn = 2 log(q + q⁻¹) = 2 log [2]_q`. -/
theorem L_pp_add_L_nn {q : ℝ} (hq : 0 < q) : L_pp q + L_nn q = 2 * Real.log (q + q⁻¹) := by
  unfold L_pp L_nn
  rw [← neg_add, ← Real.log_mul (markovZ_pos hq).ne' (mirror_pos hq).ne',
    markovZ_mul_mirror q hq.ne', one_div, Real.log_inv, Real.log_pow]
  push_cast
  ring

/-- `L_nn = log q + log(q² + 1)`: the `nn` bond constant in closed form. -/
theorem L_nn_eq {q : ℝ} (hq : 0 < q) : L_nn q = Real.log q + Real.log (q ^ 2 + 1) := by
  unfold L_nn
  rw [markovZ_sub_heckeH q hq.ne', one_div, Real.log_inv,
    Real.log_mul hq.ne' (by positivity)]
  ring

/-!
## The `pn` bond can never be the strongest (bean `qou-mu1h`)

`computations/probes/the_pn_bond_is_an_average_and_cannot_be_extremal_probe.py` measured
at `A = 2`, where no ordering or arrangement convention is in play, that the three bond
constants come out `L_pp < L_pn < L_nn` — so the model ranks the unbound dineutron above
the bound deuteron. That is not a numerical accident. The `pn` interface letter is by
definition the weighted average of the `pp` letter (`σ`, offset `0`) and the `nn` letter
(`σ⁻¹`, offset `-h`), the two-strand trace is affine in the offset (`twoStrandTrace_eq`),
and `-log` is strictly decreasing, so the ordering is forced for every `q > 0` and every
`δ ∈ (0,2)`. Since exactly one of the three two-body systems binds, and a binding-ranking
constant would have to put that one at an EXTREME, a convex combination cannot do it.

`δ` at the substrate's `q₀` is `0.00138`, and it would have to reach `2` — at `q ≈ 3.458`
— before the convexity even breaks, so nothing here is tunable. The physics is NOT
formalised: that only `pn` binds is an empirical input, and this arc's `L` carries no
spin (the real distinction is `3S1` versus `1S0`). What is proved is the ordering.
-/

/-- The `pn` offset written as the convex combination of the `pp` offset `0` and the
`nn` offset `-h` with weights `1/2 + δ/4` and `1/2 - δ/4`, which sum to `1`. -/
theorem dPN_eq_convex (q : ℝ) :
    dPN q = (1 / 2 + deltaPN q / 4) * 0 + (1 / 2 - deltaPN q / 4) * (-(heckeH q)) := by
  unfold dPN
  ring

theorem convex_weights_sum (q : ℝ) :
    (1 / 2 + deltaPN q / 4) + (1 / 2 - deltaPN q / 4) = 1 := by ring

/-- The `pn` offset lies strictly between the `nn` offset `-h` and the `pp` offset `0`,
whenever `0 < h` and `0 < δ < 2`. -/
theorem dPN_strict_between {q : ℝ} (hh : 0 < heckeH q) (hd0 : 0 < deltaPN q)
    (hd2 : deltaPN q < 2) : -(heckeH q) < dPN q ∧ dPN q < 0 := by
  unfold dPN
  constructor <;> nlinarith [mul_pos hh hd0]

/-- **The forced ordering.** With the offsets strictly ordered and `tr₂(σ + d) = z + d`
affine, the three trace factors are strictly ordered the same way. -/
theorem factors_strict_mono {q : ℝ} (hh : 0 < heckeH q) (hd0 : 0 < deltaPN q)
    (hd2 : deltaPN q < 2) :
    markovZ q - heckeH q < markovZ q + dPN q ∧ markovZ q + dPN q < markovZ q := by
  obtain ⟨h1, h2⟩ := dPN_strict_between hh hd0 hd2
  constructor <;> linarith

/-- **`L_pp < L_pn < L_nn`, for every `q > 0` and every `δ ∈ (0,2)`.** The bound
two-body system is assigned the MIDDLE bond constant, and no choice of `q` changes it:
`L = -log(z + d)` is strictly decreasing in the offset, and the `pn` offset is a convex
combination of the other two. -/
theorem L_strict_mono {q : ℝ} (hq : 0 < q) (hh : 0 < heckeH q) (hd0 : 0 < deltaPN q)
    (hd2 : deltaPN q < 2) : L_pp q < L_pn q ∧ L_pn q < L_nn q := by
  obtain ⟨hlo, hhi⟩ := factors_strict_mono hh hd0 hd2
  have hnn : 0 < markovZ q - heckeH q := mirror_pos hq
  have hpn : 0 < markovZ q + dPN q := by linarith
  unfold L_pp L_pn L_nn
  exact ⟨by simpa using Real.log_lt_log hpn hhi, by simpa using Real.log_lt_log hnn hlo⟩

/-- `h = q - q⁻¹ > 0` for `q > 1`: the hypothesis the substrate supplies. -/
theorem heckeH_pos {q : ℝ} (hq : 1 < q) : 0 < heckeH q := by
  have hq0 : 0 < q := by linarith
  unfold heckeH
  have : q⁻¹ < 1 := by rw [inv_lt_one₀ hq0]; exact hq
  linarith

end QOU.Mass.ChainTraceFactor
