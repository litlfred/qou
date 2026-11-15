import QOU.Mass.ChainTraceFactor
import QOU.BraidsAndKnots.BorromeanMarkovTrace
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic

/-!
# The intra-nucleon ordering: what it moves, and what it provably cannot

`computations/probes/the_intra_ordering_moves_absolute_traces_not_the_bond_model_probe.py`
(beans `qou-hu1f`, `qou-gpb5`) measured that the two production assemblies of one
nucleon's intra word — the **grouped** `σ₀³σ₁⁻³` that `atom_braid_word_3A` emitted
before 2026-09-05, and the **interleaved** `(σ₀σ₁⁻¹)³` that is `β_Bor` — give traces
differing by `3.785×` to `14.325×` at `A = 2 … 4`, while the character ratio
`tr_M(W_atom)/tr_M(W_free)` is **identical** under both to `~1e-60`.

This file proves the algebra behind that split. It is deliberately a **scalar** file,
like `QOU.Mass.ChainTraceFactor` which it extends: the Hecke-algebra input — that the
chain closure is a connected sum and the Markov trace is multiplicative over it, so
that `tr_M(W_atom) = F · ∏ᵢ (z + dᵢ)` and `tr_M(W_free) = F` for a common intra factor
`F` — is a classical theorem this file assumes rather than formalises, exactly as
`ChainTraceFactor` assumes it. What is proved is everything that follows from it.

## What is proved

* **The ratio cannot see the intra ordering** (`chainRatio_eq_of_intra`). Two orderings
  with intra factors `F₁` and `F₂` — *arbitrary, unrelated, and in the measurement a
  factor of `14` apart* — give the **same** ratio. No hypothesis links `F₁` to `F₂`; the
  invariance is cancellation, not coincidence. Hence `L` and the three bond constants
  are untouched by the ordering (`L_chain_eq_sum_of_intra`), which is the formal content
  of the probe's `~1e-60` agreement.

* **The difference route can, and does** (`chainDiff_scales`, `chainDiff_ne`).
  `binding_canonical` computes `tr_M(W_free) − tr_M(W_atom)`, which equals `F (1 − P)`
  and so is *exactly proportional* to the intra factor: changing the ordering scales it
  by `F₁/F₂` and changes its value whenever `F₁ ≠ F₂` and the interface product `P ≠ 1`.

* **The two confinement words are different objects** (`grouped_ne_borromean`). The
  grouped word's value is the per-generator product `tr₂(σ³) · tr₂(σ⁻³)`; the
  interleaved word's is the Borromean closed form
  `(4 + h² − 3h⁴ − h⁶)/(h² + 4)` of `QOU.BraidsAndKnots.BorromeanMarkovTrace`. At `q = 1`
  — the undeformed point, where `h = 0` and both are elementary — the first is `1/4` and
  the second is `1`. So they differ as functions of `q`, and the discrepancy is not an
  artefact of the deformation. (At `q₀` the measured values are `0.180064539535501098`
  and `0.998562163836787266`, an `82 %` gap; those sixty digits are the probe's, not
  this file's.)

## What is NOT proved

That the interleaved word *is* the one the framework wants — that is settled by
`quark-antiquark-production-reduction` ("confined by the Borromean braid `B₃`") plus the
`5e-60` match to the closed form, both outside Lean. That the chain trace factors at all
(the connected-sum input above). Any numerical value at `q₀`. And nothing here says the
bond model is *right* — only that whatever it is, the intra ordering cannot change it.
`B = α L` remains the open interpretation of `rem:bond-log-ratio-is-a-free-energy`.
-/

namespace QOU.Mass.IntraOrdering

open QOU.Mass.ChainTraceFactor QOU.BraidsAndKnots

/-! ## The bond model cannot see the intra ordering -/

/-- The chain ratio `tr_M(W_atom)/tr_M(W_free)` when the trace factors as
`intra × interfaces`: the intra factor cancels. -/
theorem chainRatio_eq_interfaceProd {F P : ℝ} (hF : F ≠ 0) : (F * P) / F = P :=
  mul_div_cancel_left₀ _ hF

/-- **Ordering invariance of the bond model.** Two intra orderings produce intra
factors `F₁` and `F₂`; no hypothesis relates them — in the measurement they differ by
up to `14.325×` — and yet the chain ratio is the same. This is why `L`, the three bond
constants, and every log-ratio binding number are untouched by the ordering. -/
theorem chainRatio_eq_of_intra {F₁ F₂ P : ℝ} (h₁ : F₁ ≠ 0) (h₂ : F₂ ≠ 0) :
    (F₁ * P) / F₁ = (F₂ * P) / F₂ := by
  rw [chainRatio_eq_interfaceProd h₁, chainRatio_eq_interfaceProd h₂]

/-- **`L` is the interface sum whatever the intra ordering is.** For an arbitrary
nonzero intra factor `F`, the bond constant read off the chain ratio is the sum of
`-log(z + dᵢ)` over the interfaces. This is `ChainTraceFactor.neg_log_prod` transported
through the cancellation above. -/
theorem L_chain_eq_sum_of_intra {ι : Type*} (s : Finset ι) (q : ℝ) (d : ι → ℝ)
    (hpos : ∀ i ∈ s, 0 < markovZ q + d i) {F : ℝ} (hF : F ≠ 0) :
    -Real.log ((F * ∏ i ∈ s, (markovZ q + d i)) / F)
      = ∑ i ∈ s, -Real.log (markovZ q + d i) := by
  rw [chainRatio_eq_interfaceProd hF]
  exact neg_log_prod s _ hpos

/-- Two orderings give the same `L`, for the same reason. -/
theorem L_chain_indep_of_intra {ι : Type*} (s : Finset ι) (q : ℝ) (d : ι → ℝ)
    {F₁ F₂ : ℝ} (h₁ : F₁ ≠ 0) (h₂ : F₂ ≠ 0) :
    -Real.log ((F₁ * ∏ i ∈ s, (markovZ q + d i)) / F₁)
      = -Real.log ((F₂ * ∏ i ∈ s, (markovZ q + d i)) / F₂) := by
  rw [chainRatio_eq_of_intra h₁ h₂]

/-! ## The difference route can, and the scaling is exact -/

/-- **`binding_canonical`'s `Δtr` is proportional to the intra factor.** Its
`tr_M(W_free) − tr_M(W_atom)` equals `F (1 − P)`, so changing the ordering multiplies it
by `F₁/F₂` — the same `3.785 … 14.325` the probe measures on the traces themselves. -/
theorem chainDiff_scales {F₁ F₂ P : ℝ} (h₂ : F₂ ≠ 0) :
    F₁ - F₁ * P = (F₁ / F₂) * (F₂ - F₂ * P) := by
  field_simp

/-- And it genuinely moves: the difference route distinguishes the orderings whenever
the intra factors differ and the interface product is not `1`. (At `q₀` every factor
`z + d` lies in `(0,1)`, so `P ≠ 1` holds for every nonempty chain.) -/
theorem chainDiff_ne {F₁ F₂ P : ℝ} (hP : P ≠ 1) (hF : F₁ ≠ F₂) :
    F₁ - F₁ * P ≠ F₂ - F₂ * P := by
  intro hEq
  apply hF
  have h1 : F₁ * (1 - P) = F₂ * (1 - P) := by ring_nf; ring_nf at hEq; linarith
  have : (1 : ℝ) - P ≠ 0 := sub_ne_zero.mpr (Ne.symm hP)
  exact mul_right_cancel₀ this h1

/-! ## The two confinement words are different objects

`tr₂(σᵏ) = w₊ qᵏ + w₋ (−q⁻¹)ᵏ`, the level-2 Wenzl expectation of the block eigenvalues.
The grouped word `σ₀³σ₁⁻³` has each generator's letters contiguous, so its trace is the
per-generator product `tr₂(σ³) · tr₂(σ⁻³)`. The interleaved word `(σ₀σ₁⁻¹)³` does not,
and its trace is the Borromean closed form. -/

/-- `tr₂(σ³) = w₊ q³ + w₋ (−q⁻¹)³`. -/
noncomputable def twoStrandCube (q : ℝ) : ℝ := wPlus q * q ^ 3 + wMinus q * (-q⁻¹) ^ 3

/-- `tr₂(σ⁻³) = w₊ (q⁻¹)³ + w₋ (−q)³`, the mirror letter. -/
noncomputable def twoStrandCubeInv (q : ℝ) : ℝ :=
  wPlus q * (q⁻¹) ^ 3 + wMinus q * (-q) ^ 3

/-- The **grouped** confinement value: the per-generator product, which is what a
word with each generator's letters contiguous contributes. -/
noncomputable def groupedConfinement (q : ℝ) : ℝ := twoStrandCube q * twoStrandCubeInv q

/-- The **interleaved** confinement value: `|tr_M(β_Bor)|`, the closed form
`(4 + h² − 3h⁴ − h⁶)/(h² + 4)` in `h = q − q⁻¹`. -/
noncomputable def borromeanConfinement (q : ℝ) : ℝ :=
  trM_borromean_num (heckeH q) / trM_borromean_den (heckeH q)

theorem heckeH_at_one : heckeH 1 = 0 := by
  unfold heckeH; norm_num

theorem trM_borromean_den_pos_real (h : ℝ) : (0 : ℝ) < trM_borromean_den h := by
  unfold trM_borromean_den; positivity

/-- The Borromean factor in the form that makes its size obvious:
`1 − (3h⁴ + h⁶)/(h² + 4)`, so it is at most `1` and falls away from `1` at order `h⁴`.
(At `q₀`, `h = 0.209…` and this is `0.998562…`.) -/
theorem borromeanConfinement_eq_one_sub (q : ℝ) :
    borromeanConfinement q
      = 1 - (3 * (heckeH q) ^ 4 + (heckeH q) ^ 6) / ((heckeH q) ^ 2 + 4) := by
  unfold borromeanConfinement trM_borromean_num trM_borromean_den
  have hden : ((heckeH q) ^ 2 + 4 : ℝ) ≠ 0 := by positivity
  field_simp
  ring

theorem borromeanConfinement_le_one (q : ℝ) : borromeanConfinement q ≤ 1 := by
  rw [borromeanConfinement_eq_one_sub]
  have hden : (0 : ℝ) < (heckeH q) ^ 2 + 4 := by positivity
  have hnum : (0 : ℝ) ≤ 3 * (heckeH q) ^ 4 + (heckeH q) ^ 6 := by positivity
  have : (0 : ℝ) ≤ (3 * (heckeH q) ^ 4 + (heckeH q) ^ 6) / ((heckeH q) ^ 2 + 4) :=
    div_nonneg hnum hden.le
  linarith

/-- At the undeformed point `q = 1` the Borromean factor is `1`. -/
theorem borromeanConfinement_at_one : borromeanConfinement 1 = 1 := by
  unfold borromeanConfinement trM_borromean_num trM_borromean_den
  rw [heckeH_at_one]
  norm_num

theorem wPlus_at_one : wPlus 1 = 3 / 4 := by
  unfold wPlus qint3; norm_num

theorem wMinus_at_one : wMinus 1 = 1 / 4 := by
  unfold wMinus qint3; norm_num

/-- At `q = 1` the grouped per-generator product is `1/4`: each factor is
`3/4 − 1/4 = 1/2`. -/
theorem groupedConfinement_at_one : groupedConfinement 1 = 1 / 4 := by
  unfold groupedConfinement twoStrandCube twoStrandCubeInv
  rw [wPlus_at_one, wMinus_at_one]
  norm_num

/-- **The grouped word is not `β_Bor`.** They already disagree at `q = 1`, where both
are elementary — `1/4` against `1` — so the `82 %` gap measured at `q₀` is not a
deformation artefact but a difference of objects. -/
theorem grouped_ne_borromean_at_one :
    groupedConfinement 1 ≠ borromeanConfinement 1 := by
  rw [groupedConfinement_at_one, borromeanConfinement_at_one]
  norm_num

/-- As functions of `q`. -/
theorem grouped_ne_borromean : groupedConfinement ≠ borromeanConfinement := by
  intro hEq
  exact grouped_ne_borromean_at_one (congrFun hEq 1)

/-- The per-generator form is what the *grouped* assembly computes, by definition.
Stated so the contrast with `grouped_ne_borromean` is explicit: the identity
`tr_M = ∏_gen tr₂` holds for the word whose generators are contiguous, and the
interleaved word does not satisfy it. -/
theorem perGeneratorProduct_eq_grouped (q : ℝ) :
    twoStrandCube q * twoStrandCubeInv q = groupedConfinement q := rfl

end QOU.Mass.IntraOrdering
