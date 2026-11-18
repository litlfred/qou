import QOU.Mass.GammaGammaSelectionTen
import QOU.QBeta.SingleCrossingAlwaysBinds

/-!
# Why the γγ-selected bond can unbind: the single-crossing obstruction is vacuous on γγ words

Bean `qou-ales`, step 8 — a reconciliation, not a new derivation. The corpus holds two
sorry-free bodies of work that look like they collide, and this file proves they do not.

**One side.** `QOU/QBeta/SingleCrossingAlwaysBinds.lean` proves that a **single-crossing**
interface can never unbind: its scalar is `μ = z + d` with `d ∈ [-h, 0]`, which lies in
`(0,1)` at the substrate anchor, so `B = −α·log μ > 0` (`single_crossing_binds`). Its
`t3_grading_cannot_unbind_pp` adds that the `T₃` / writhe grading cannot rescue the sign,
and its docstring states the conclusion in strong terms — the framework "picked a sign that
makes unbinding **impossible**, whatever the magnitude".

**The other side.** Step 3 (#7192) measured that the γγ-selected interface bond
`G³ = (σ₂σ₃⁻¹)³` **does** unbind the diproton (`B_pp = −4.47` keV, ratio
`tr_atom/tr_free = 1.001058`), and steps 6–7 proved `G³` is what reading 3 selects.

Both are correct. Two structural facts separate them, and both are proved here.

## 1. No non-empty γγ word is a single crossing

`length_even` (step 1) gives every γγ word an even number of crossings; a single crossing
has one. So `interfaceBond m` for `m ≥ 1` is never in the obstruction's domain
(`gammaGamma_ne_singleCrossing`, `interfaceBond_ne_singleCrossing`). The obstruction is a
statement about words of length one; the selected bond has length six.

## 2. The writhe / `T₃` grading is IDENTICALLY TRIVIAL on a γγ word

This is the sharper half. The grading multiplies the channel scalar by `c^(writhe w / 2)`,
and `writhe_eq_zero` (step 1) gives **every** γγ word writhe `0`. So the factor is `c⁰ = 1`
exactly (`writhe_normalisation_eq_one_of_gammaGamma`): on γγ words the grading neither binds
harder nor unbinds (`t3_grading_vacuous_on_gammaGamma`). The owner's ruling of 2026-09-08 —
select every braid word by γγ pair production — therefore does not *beat* the `T₃`
obstruction; it makes it **silent**.

## 3. What is still measured, and what is now proved

The sign law itself is proved (`unbound_iff_ratio_gt_one`): with `α > 0` and `μ > 0`,
`−α·log μ < 0` iff `μ > 1`. And `obstruction_conclusion_false_of_ratio_gt_one` shows the
obstruction's `μ < 1` hypothesis is *essential* — for a ratio above one its conclusion is
false, not merely unproved. So of the step-3 diproton result, exactly **one number remains
a measurement**: the ratio `1.001058`. Everything else about the sign is now algebra.

Nothing here reads AME2020, a CODATA binding value, or a census, and nothing here asserts
the ratio — it is carried as a hypothesis wherever it is used.

## Base ring (§7c)

The writhe section is `ℤ`/`ℕ` combinatorics on words; the scalar statements are on `ℝ`,
as the obstruction they reconcile with (`Real.log`, `Real.rpow`, an order).
-/

namespace QOU.Mass.GammaGammaEscapesSingleCrossing

open QOU.Mass.GammaGammaWordSelection
open QOU.Mass.GammaGammaSelectorH3
open QOU.Mass.GammaGammaH6Interface

/-! ## 1. A γγ word is never a single crossing -/

/-- **No non-empty γγ word is a single crossing**: γγ words have even length
(`length_even`), and a single crossing has length one. -/
theorem gammaGamma_ne_singleCrossing {w : Word} (h : GammaGammaWord w) (c : Crossing) :
    w ≠ [c] := by
  intro hw
  have := length_even h
  rw [hw] at this
  simp only [List.length_cons, List.length_nil, Nat.zero_add] at this
  exact (Nat.not_even_iff_odd.mpr ⟨0, rfl⟩) this

/-- In particular no interface bond `G^m` is a single crossing: it has `2m` crossings
(`interfaceBond_length`), which is never one. -/
theorem interfaceBond_ne_singleCrossing (m : ℕ) (c : Crossing) :
    interfaceBond m ≠ [c] :=
  gammaGamma_ne_singleCrossing (interfaceBond_gammaGamma m) c

/-- The selected bond has six crossings, so a fortiori it is not one. -/
theorem interfaceBond_three_length_ne_one : (interfaceBond 3).length ≠ 1 := by
  rw [interfaceBond_length]; norm_num

/-! ## 2. The writhe grading is identically trivial on γγ words -/

/-- The writhe grading exponent `e = writhe w / 2` of the `T₃` normalisation. -/
noncomputable def writheExponent (w : Word) : ℝ := (writhe w : ℝ) / 2

/-- **Every γγ word has grading exponent `0`** — immediate from `writhe_eq_zero`. -/
theorem writheExponent_eq_zero_of_gammaGamma {w : Word} (h : GammaGammaWord w) :
    writheExponent w = 0 := by
  unfold writheExponent
  rw [writhe_eq_zero h]
  norm_num

/-- **The writhe normalisation factor is exactly `1` on a γγ word**, for any base. -/
theorem writhe_normalisation_eq_one_of_gammaGamma {w : Word} (h : GammaGammaWord w) (c : ℝ) :
    c ^ writheExponent w = 1 := by
  rw [writheExponent_eq_zero_of_gammaGamma h, Real.rpow_zero]

/-- **The `T₃` / writhe grading is VACUOUS on a γγ word**: it multiplies the channel
scalar by exactly `1`, so it can neither bind harder nor unbind. This is why the
`t3_grading_cannot_unbind_pp` obstruction has no purchase on a γγ-selected bond — not
because the bond defeats it, but because the grading it argues about is trivial there. -/
theorem t3_grading_vacuous_on_gammaGamma {w : Word} (h : GammaGammaWord w) (μ c : ℝ) :
    μ * c ^ writheExponent w = μ := by
  rw [writhe_normalisation_eq_one_of_gammaGamma h c, mul_one]

/-! ## 3. The sign law, and why the obstruction's hypothesis is essential -/

/-- **The sign law**: with a positive scale `α` and a positive trace ratio `μ`, the
binding `B = −α·log μ` is negative (unbound) exactly when the bond moves the trace
*upward*, `μ > 1`. -/
theorem unbound_iff_ratio_gt_one {α μ : ℝ} (hα : 0 < α) (hμ : 0 < μ) :
    -α * Real.log μ < 0 ↔ 1 < μ := by
  constructor
  · intro hB
    have hlog : 0 < Real.log μ := by nlinarith
    exact (Real.log_pos_iff hμ.le).mp hlog
  · intro h1
    have hlog : 0 < Real.log μ := Real.log_pos h1
    nlinarith

/-- The mirror statement: a ratio below one binds. This is the content
`single_crossing_binds` supplies for a single crossing, stated on the ratio alone. -/
theorem bound_iff_ratio_lt_one {α μ : ℝ} (hα : 0 < α) (hμ : 0 < μ) :
    0 < -α * Real.log μ ↔ μ < 1 := by
  constructor
  · intro hB
    have hlog : Real.log μ < 0 := by nlinarith
    exact (Real.log_neg_iff hμ).mp hlog
  · intro h1
    have hlog : Real.log μ < 0 := Real.log_neg hμ h1
    nlinarith

/-- **The obstruction's `μ < 1` hypothesis is essential, not decorative.** For a channel
scalar above one, carried through a writhe-`0` (γγ) grading, the conclusion of
`nonneg_writhe_cannot_unbind` is FALSE — so a bond whose trace ratio exceeds one is
genuinely outside that theorem's scope rather than an unproved case of it. -/
theorem obstruction_conclusion_false_of_ratio_gt_one {w : Word} (h : GammaGammaWord w)
    {μ c : ℝ} (hμ : 1 < μ) : ¬ (μ * c ^ writheExponent w < 1) := by
  rw [t3_grading_vacuous_on_gammaGamma h μ c]
  exact not_lt.mpr hμ.le

/-- **The reconciliation, on the selected bond.** Given only that the selected
interface bond `G³` moves the diproton trace upward — the one number step 3 measured —
the log law makes the diproton unbound, and the single-crossing obstruction does not
apply: its grading is trivial here (`t3_grading_vacuous_on_gammaGamma`) and its
hypothesis fails (`obstruction_conclusion_false_of_ratio_gt_one`). -/
theorem selected_bond_unbinds_of_ratio_gt_one {α μ : ℝ} (hα : 0 < α) (hμ : 1 < μ) :
    -α * Real.log μ < 0 ∧ ∀ c : ℝ, ¬ (μ * c ^ writheExponent (interfaceBond 3) < 1) := by
  refine ⟨(unbound_iff_ratio_gt_one hα (by linarith)).mpr hμ, fun c => ?_⟩
  exact obstruction_conclusion_false_of_ratio_gt_one (interfaceBond_gammaGamma 3) hμ


/-- **Zero-power specialization of `interfaceBond_ne_singleCrossing` (`qou-0gqn`).**
The empty interface bond `interfaceBond 0` is not a single crossing `[c]`. -/
theorem interfaceBond_ne_singleCrossing_zero (c : Crossing) :
    interfaceBond 0 ≠ [c] :=
  interfaceBond_ne_singleCrossing 0 c

end QOU.Mass.GammaGammaEscapesSingleCrossing
