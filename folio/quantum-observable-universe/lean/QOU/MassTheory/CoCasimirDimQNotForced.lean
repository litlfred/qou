import QOU.SchurWeyl.SpinSectorMeasure
import QOU.Mass.QHookDimension

/-!
# Which `dim_q` the convention-D trace assigns, and why the hook formula is not it

The surviving-block co-Casimir `C° = Σ_{τ(p_λ) ≠ 0} p_λ / (dim_q(λ) · τ(p_λ))` takes `dim_q` as
block data (`CoCasimirSurvivingBlocks`, `CoCasimirHeckeBridge`). Production uses the q-hook-length
formula `dimQ λ = [n]_q! / ∏ [h]_q` (`QOU.Mass.QHookDimension.dimQ`). This file asks whether the
trace itself forces that choice.

## What the trace assigns (already proved in the corpus)

At `z_D = q³/(q²+1)` the trace of a block idempotent is `τ(p_λ) = #SYT(λ) · W_λ`, and the weight is

* `W_λ = schurPrincipal 2 (q²) λ / (q²+1)^{|λ|}` (`ocneanuWeight_conventionD_eq_schurPrincipal`),
  the principal specialisation of the Schur function in **two** variables;
* on a two-row shape `(m, k)`, `W_(m,k) = [m − k + 1]_q / [2]_q^{m+k}`
  (`SpinSector.ocneanuWeight_twoRow_conventionD`).

So the q-dimension the trace carries is `[m − k + 1]_q`: the quantum dimension of the spin
`(m − k)/2` representation of `U_q(sl₂)`, which is the `gl₂` side of Schur–Weyl duality. It is not
built from the hook lengths of `λ`.

## What this file proves

The hook formula `dimQ` is the q-analogue of the **Hecke** side dimension `#SYT(λ)`. It is not a
λ-independent multiple of the trace weight. At `n = 3`, on the two surviving blocks `(3)` and
`(2,1)`:

* `trace_weight_ratio_n3`: `W_(2,1) · (q² + q⁻²) = W_(3)`;
* `dimQ q [2,1] = [2]_q · dimQ q [3]` (from `dimQ_three`, `dimQ_two_one`);
* `hookDim_proportional_to_weight_n3`: a common `κ` with `dimQ λ = κ · W_λ` on both blocks forces
  `(q + q⁻¹)(q² + q⁻²) = 1`;
* `not_hookDim_proportional_to_weight_n3`: over an ordered field with `q > 0` that is impossible.

## Scope

This is an exact statement about two objects, not a numerical comparison. It shows the trace does
not *force* the hook formula; it does not show the hook formula is *wrong* for Term 4. That
`dim_q` in the co-Casimir should be the hook formula, the trace's `gl₂` dimension, or something
else is a definition the corpus has not derived.

## Base ring (§7c)

The identities are over a generic `[Field R]`. Only the final impossibility uses an ordered field,
because "`q > 0`" is an order statement; it uses nothing archimedean.

LaTeX label: `thm:cocasimir-dimq-not-forced`
-/

namespace QOU.MassTheory.CoCasimirDimQ

open QOU.SchurWeyl QOU.SchurWeyl.SpinSector

section Generic

variable {R : Type*} [Field R]

/-- `W_(3)`: the convention-D weight of the one-row shape with three cells. -/
noncomputable abbrev W3 (q : R) : R :=
  ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) (twoRow 3 0 (by omega))

/-- `W_(2,1)`: the convention-D weight of the shape `(2,1)`. -/
noncomputable abbrev W21 (q : R) : R :=
  ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) (twoRow 2 1 (by omega))

/-- **The trace's own weights at `n = 3`:** `W_(2,1) · (q² + q⁻²) = W_(3)`. -/
theorem trace_weight_ratio_n3 (q : R) (hq : q ≠ 0) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : R) ^ i ≠ 1) :
    W21 q * (q ^ 2 + q⁻¹ ^ 2) = W3 q := by
  have h3 := ocneanuWeight_twoRow_conventionD q hq hq21 hgen (m := 3) (k := 0) (by omega)
  have h21 := ocneanuWeight_twoRow_conventionD q hq hq21 hgen (m := 2) (k := 1) (by omega)
  norm_num at h3 h21
  have hq1 : q ^ 2 ≠ 1 := by simpa using hgen 1 one_pos
  have hsub : q - q⁻¹ ≠ 0 := by
    intro h
    apply hq1
    have : q * (q - q⁻¹) = q ^ 2 - 1 := by field_simp
    rw [h, mul_zero] at this
    linear_combination -this
  have hadd : q + q⁻¹ ≠ 0 := by
    intro h
    apply hq21
    have : q * (q + q⁻¹) = q ^ 2 + 1 := by field_simp
    rw [h, mul_zero] at this
    exact this.symm
  have hD : (q - q⁻¹) * (q + q⁻¹) ^ 3 ≠ 0 := mul_ne_zero hsub (pow_ne_zero _ hadd)
  apply mul_right_cancel₀ hD
  calc W21 q * (q ^ 2 + q⁻¹ ^ 2) * ((q - q⁻¹) * (q + q⁻¹) ^ 3)
      = (W21 q * (q - q⁻¹) * (q + q⁻¹) ^ 3) * (q ^ 2 + q⁻¹ ^ 2) := by ring
    _ = (q ^ 2 - q⁻¹ ^ 2) * (q ^ 2 + q⁻¹ ^ 2) := by rw [h21]; ring
    _ = W3 q * (q - q⁻¹) * (q + q⁻¹) ^ 3 := by rw [h3]; ring
    _ = W3 q * ((q - q⁻¹) * (q + q⁻¹) ^ 3) := by ring

/-- **The hook formula is not a λ-independent multiple of the trace weight.** If one constant `κ`
had `dimQ λ = κ · W_λ` on both surviving blocks at `n = 3`, then `(q + q⁻¹)(q² + q⁻²) = 1`. -/
theorem hookDim_proportional_to_weight_n3 (q : R) (hq : q ≠ 0) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : R) ^ i ≠ 1) (h3 : QOU.Mass.qInt q 3 ≠ 0)
    (hκ : ∃ κ : R, QOU.Mass.dimQ q [3] = κ * W3 q ∧ QOU.Mass.dimQ q [2, 1] = κ * W21 q) :
    (q + q⁻¹) * (q ^ 2 + q⁻¹ ^ 2) = 1 := by
  obtain ⟨κ, e3, e21⟩ := hκ
  have h2 : QOU.Mass.qInt q 2 ≠ 0 := by
    rw [QOU.Mass.qInt_two]
    intro h
    apply hq21
    have : q * (q + q⁻¹) = q ^ 2 + 1 := by field_simp
    rw [h, mul_zero] at this
    exact this.symm
  rw [QOU.Mass.dimQ_three q h2 h3] at e3
  rw [QOU.Mass.dimQ_two_one q h3, QOU.Mass.qInt_two] at e21
  have hr := trace_weight_ratio_n3 q hq hq21 hgen
  -- `1 = κ W₃ = κ W₂₁ (q² + q⁻²) = (q + q⁻¹)(q² + q⁻²)`
  calc (q + q⁻¹) * (q ^ 2 + q⁻¹ ^ 2) = κ * W21 q * (q ^ 2 + q⁻¹ ^ 2) := by rw [e21]
    _ = κ * (W21 q * (q ^ 2 + q⁻¹ ^ 2)) := by ring
    _ = κ * W3 q := by rw [hr]
    _ = 1 := e3.symm

end Generic

section Ordered

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- **For `q > 0` no such `κ` exists**, so on the surviving blocks the hook formula is not the
trace's q-dimension up to an overall constant. -/
theorem not_hookDim_proportional_to_weight_n3 (q : R) (hq : 0 < q)
    (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : R) ^ i ≠ 1) (h3 : QOU.Mass.qInt q 3 ≠ 0) :
    ¬ ∃ κ : R, QOU.Mass.dimQ q [3] = κ * W3 q ∧ QOU.Mass.dimQ q [2, 1] = κ * W21 q := by
  intro hκ
  have hq21 : q ^ 2 + 1 ≠ 0 := by positivity
  have h := hookDim_proportional_to_weight_n3 q hq.ne' hq21 hgen h3 hκ
  have ht : 0 < q⁻¹ := inv_pos.mpr hq
  have hqt : q * q⁻¹ = 1 := mul_inv_cancel₀ hq.ne'
  have hsum : 2 ≤ q + q⁻¹ := by nlinarith [sq_nonneg (q - q⁻¹)]
  have hsq : 0 < q ^ 2 + q⁻¹ ^ 2 := by positivity
  have hsq2 : 2 ≤ q ^ 2 + q⁻¹ ^ 2 := by nlinarith [sq_nonneg (q - q⁻¹), hqt]
  nlinarith

end Ordered

end QOU.MassTheory.CoCasimirDimQ
