/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import QOU.OrientedSkein.Model.GLnTrace
import QOU.SchurWeyl.MarkovTraceInstance

/-!
# `QOU.OrientedSkein.Model.GLnCrossCheck` — at `n = 2` the closure trace is the convention-`D` trace

Cross-check for dispatch B of PR #7705 (bean `qou-slck`).  For `n = 2` the loop value of the
`GL_n` model (`QOU.OrientedSkein.Model.GLnTrace`) is `[2]_q = q + q⁻¹`, the curl is `q²`, so the
Markov parameter of its closure trace is

`z = q² / (q + q⁻¹) = q³ / (q² + 1) = z_D`,

the convention-`D` parameter of the corpus.  `QOU.SchurWeyl.MarkovTraceInstance` proved that the
Ocneanu-weighted seminormal trace `wtrace` is a Markov trace with parameter `z_D`.  By uniqueness of
the Markov trace (`HeckeCoset.markovTrace_unique`) the two coincide at every level of the Hecke
tower: the normalised closure of the `R²` quantum trace, computed in `ModuleCat K` through the
oriented-skein left trace, equals `wtrace` (`closure_eq_wtrace_two`).

The hypotheses are those of `ocneanuMarkovTrace`: `q ≠ 0`, `q` not a root of unity, `q² + 1 ≠ 0`
and `q²` not a root of unity.

## Scope

This is a comparison of two traces on the abstract tower `QOU.SchurWeyl.Hecke K q q⁻¹ m`.  It is
not a comparison with `QOU.IwahoriHecke.TensorMarkovModel`, whose trace is defined on the
presented algebra `Pres N (q - q⁻¹) 1`; no map between the two presentations is in the tree.

Sorry-free; no axioms beyond Lean/Mathlib's.
-/

namespace QOU.OrientedSkein.GLn

open CategoryTheory MonoidalCategory QOU.SchurWeyl

universe u

/-- Transport a Markov trace family along an equality of Markov parameters. -/
def castMarkov {R : Type*} [CommRing R] {q qi z z' : R} (T : HeckeCoset.MarkovTraceFamily R q qi z)
    (hz : z = z') : HeckeCoset.MarkovTraceFamily R q qi z' where
  tr := T.tr
  tr_one := T.tr_one
  tr_cyclic := T.tr_cyclic
  tr_incl := T.tr_incl
  tr_markov := hz ▸ T.tr_markov

variable {K : Type u} [Field K]

theorem sum_wt_two (q qi : K) : (∑ i, wt 2 q qi i) = q + qi := by
  simp [wt, W, Fin.sum_univ_two]

/-- **The `n = 2` closure trace is the convention-`D` Markov trace.**  For every level `m` and
every `x ∈ H_{m+1}(q)`, `[2]_q^{-(m+1)}` times the closure of `ρ_m(x)` on `(K²)^{⊗(m+1)}` equals
the Ocneanu-weighted seminormal trace `wtrace` of `x`. -/
theorem closure_eq_wtrace_two (q : K) (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (hq21 : q ^ 2 + 1 ≠ 0) (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : K) ^ i ≠ 1)
    (m : ℕ) (x : Hecke K q q⁻¹ m) :
    (q + q⁻¹)⁻¹ ^ (m + 1) *
        unitScalar K ((leftTrace (n := 2) q q⁻¹ (mul_inv_cancel₀ hq0)).fullTr (m + 1)
          ((crossing (n := 2) q q⁻¹ (mul_inv_cancel₀ hq0)).revAction m x)) =
      _root_.QOU.SchurWeyl.SeminormalRep.wtrace q hq0 hq2 m x := by
  have hd0 : q + q⁻¹ ≠ 0 := by
    intro h0
    apply hq21
    have : q * (q + q⁻¹) = q ^ 2 + 1 := by field_simp
    rw [← this, h0, mul_zero]
  have hd : (∑ i, wt 2 q q⁻¹ i) * (q + q⁻¹)⁻¹ = 1 := by
    rw [sum_wt_two, mul_inv_cancel₀ hd0]
  have hz : q ^ 2 * (q + q⁻¹)⁻¹ = q ^ 3 / (q ^ 2 + 1) := by
    field_simp
  have key := HeckeCoset.markovTrace_unique
    (castMarkov (markovFamily (n := 2) q q⁻¹ (mul_inv_cancel₀ hq0) (q + q⁻¹)⁻¹ hd) hz)
    (_root_.QOU.SchurWeyl.SeminormalRep.ocneanuMarkovTrace q hq0 hq2 hq21 hgen) m x
  exact key

end QOU.OrientedSkein.GLn
