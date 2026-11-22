import QOU.QBeta.LeverLogDerivative
import Mathlib.Order.Filter.Basic
import Mathlib.Analysis.Calculus.MeanValue

/-!
# The bar-odd ladder shape — the c₃ S falsification kit as a class

Machine-checked skeleton of everything the merged probe chain established
about the c₃ bar-odd `S` (PRs #3540/#3562/#3596/#3621 + the q* probes):
`S = A/u³` with `A` smooth, `A(q*) = 0` (q* = the decay-sector determination
of q₀, 80.3 % muon-ward), `A′(q*) ≈ +2.37 > 0`, and `u > 0` (the ladder
lever).  The class fields encode those *hypotheses*; the theorems below
**derive** the observed phenomenology from them, sorry-free:

* the S sign-flip across q* (`eventually_sign_flip_S`) — the "hard fact" of
  the 2026-07-11 S-leak audit, here a consequence, not an observation;
* the un-levered identity `S·u³ = A` (the round-1 `r = S·u³` reframing);
* `hasDerivAt_S_at_qstar`: at q* the S-slope is **exactly** `A′/u(q*)³` —
  the pure static lever with zero log-derivative correction (because
  `A(q*) = 0`), chaining the merged `LeverLogDerivative` decomposition.

The **numerical instance** of this class is witnessed by the committed
probes (`qbeta-c3-phib-mq-logderivative-constraint`, the q* full-precision
witness).  The **geometric instance** — realizing `A/u³` as `Im 𝔙(m(q))` of
a categorical meridian assignment through the (now unconditionally
inhabited) `FaddeevPhi`/`phiBProd` — is the single named open problem
(`conj:algebraic-geometric-dilog-equivalence`).  Per §3b-tax the class
carries content-bearing hypothesis fields and no conclusion projection.

-- Ref: [leitner2026] docs/coordination/1ppq-qbeta.md (Φ_b arc entries, 2026-07-11/12)
-/

namespace QOU.QBeta

open Filter

/-- **Bar-odd ladder shape** (hypothesis carrier, §3b): `S = A/u³` with a
positive lever `u`, a simple zero of the numerator at `q*`, and positive
numerator slope `A′` there.  All fields are the *measured/derived inputs*
of the c₃ bar-odd chain; the theorems below are consequences. -/
class BarOddLadderShape (S A u : ℝ → ℝ) (qstar A' : ℝ) : Prop where
  /-- The ladder shape `S = A/u³` (the N=3 rung lever). -/
  ladder : ∀ q, S q = A q / u q ^ 3
  /-- The lever is positive (substrate `u = b·ℏ_q² > 0` for `q > 1`). -/
  u_pos : ∀ q, 0 < u q
  /-- The numerator vanishes at the decay-sector determination `q*`. -/
  zero_at_qstar : A qstar = 0
  /-- The numerator is differentiable at `q*` with derivative `A′`. -/
  deriv_at_qstar : HasDerivAt A A' qstar
  /-- The numerator slope at `q*` is positive (measured `A′ ≈ +2.37`). -/
  slope_pos : 0 < A'

namespace BarOddLadderShape

variable {S A u : ℝ → ℝ} {qstar A' : ℝ}

/-- The un-levered identity `S·u³ = A` — the round-1 `r = S·u³` reframing,
now an algebraic consequence of the class. -/
theorem unlevered [h : BarOddLadderShape S A u qstar A'] (q : ℝ) :
    S q * u q ^ 3 = A q := by
  rw [h.ladder q]
  field_simp [(h.u_pos q).ne']

/-- **The numerator sign-flips across `q*`** (simple zero, positive slope):
eventually on the punctured neighborhood, `A > 0` right of `q*` and `A < 0`
left of it. -/
theorem eventually_sign_flip_A [h : BarOddLadderShape S A u qstar A'] :
    ∀ᶠ q in nhdsWithin qstar {qstar}ᶜ,
      (qstar < q → 0 < A q) ∧ (q < qstar → A q < 0) := by
  have hslope : Tendsto (slope A qstar)
      (nhdsWithin qstar {qstar}ᶜ) (nhds A') :=
    hasDerivAt_iff_tendsto_slope.mp h.deriv_at_qstar
  have hpos : ∀ᶠ q in nhdsWithin qstar {qstar}ᶜ, 0 < slope A qstar q :=
    hslope.eventually_const_lt h.slope_pos
  filter_upwards [hpos, self_mem_nhdsWithin] with q hq hne
  have hne' : q - qstar ≠ 0 :=
    sub_ne_zero.mpr (Set.mem_compl_singleton_iff.mp hne)
  have hAq : A q = slope A qstar q * (q - qstar) := by
    rw [slope_def_field, h.zero_at_qstar, sub_zero, div_mul_cancel₀ _ hne']
  constructor
  · intro hlt
    rw [hAq]
    exact mul_pos hq (sub_pos.mpr hlt)
  · intro hlt
    rw [hAq]
    exact mul_neg_of_pos_of_neg hq (sub_neg.mpr hlt)

/-- **The S sign-flip across `q*`** — the "hard fact" of the S-leak audit
(`S(muon) > 0 > S(proton)` with `q_p < q* < q_μ`), derived: the positive
lever `u³` preserves the numerator's sign. -/
theorem eventually_sign_flip_S [h : BarOddLadderShape S A u qstar A'] :
    ∀ᶠ q in nhdsWithin qstar {qstar}ᶜ,
      (qstar < q → 0 < S q) ∧ (q < qstar → S q < 0) := by
  filter_upwards [eventually_sign_flip_A (S := S) (A := A) (u := u) (A' := A')] with q hq
  have hu3 : 0 < u q ^ 3 := pow_pos (h.u_pos q) 3
  refine ⟨fun hlt => ?_, fun hlt => ?_⟩
  · rw [h.ladder q]
    exact div_pos (hq.1 hlt) hu3
  · rw [h.ladder q]
    exact div_neg_of_neg_of_pos (hq.2 hlt) hu3

/-- **The S-slope at `q*` is exactly the pure static lever `A′/u(q*)³`**:
because `A(q*) = 0`, the log-derivative correction of the
`LeverLogDerivative` decomposition vanishes identically at `q*` — the
one-anchor derivative gate is exact there, for any `u`-derivative `u'`. -/
theorem hasDerivAt_S_at_qstar [h : BarOddLadderShape S A u qstar A']
    {u' : ℝ} (hu : HasDerivAt u u' qstar) :
    HasDerivAt S (A' / u qstar ^ 3) qstar := by
  have hS : S = fun q => A q / u q ^ 3 := funext h.ladder
  have hd := QOU.QBeta.LeverLogDerivative.hasDerivAt_div_pow_three
    h.deriv_at_qstar hu (h.u_pos qstar).ne'
  rw [hS]
  convert hd using 1
  rw [h.zero_at_qstar]
  ring

end BarOddLadderShape

end QOU.QBeta
