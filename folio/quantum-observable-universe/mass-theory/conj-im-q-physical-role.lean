import Mathlib.Algebra.Field.Defs
import Mathlib.Analysis.Complex.Basic


/-!
# QOU.BraidKnot.ImQPhysicalRole

Conjectural physical role of `Im(q)`: a substrate moduli parameter with no
current observable, and three candidate roles (chirality, phase-dual-to-CAL-2,
non-Hermitian deformation).

Ref: [leitner2026] conj:im-q-physical-role
Ref: [leitner2026] rem:im-q-vs-p-skew

## What is asserted, and what is derived

The conjecture is carried by the class `ImQPhysicalRole obs q`, whose two
fields are the *hypotheses*:

* `factors_through_modulus` — the observable is `‖F ·‖` for a
  conjugation-equivariant `F` (true of the categorical mass formula, whose
  `F` is a Markov trace with real coefficients);
* `leading_order_real` — at leading order the observable takes the same value
  at `q` as at `Re q`.

Everything below the class is **derived** from those, not asserted: the
conjugation invariance `obs (conj q) = obs q`, and the payoff
`im_q_undetermined` — an observable satisfying the class does not determine
`Im(q)`, because it takes one value on two points of different imaginary part.

**Scope, stated precisely because the two are easy to conflate.**
`obs_conj_invariance` needs only the first field and is therefore
unconditional for any modulus observable: such an observable cannot see the
**sign** of `Im(q)`. That is strictly weaker than the conjecture, which is
about the **magnitude** and is carried by the second field. Do not cite the
first as evidence for the second.

Non-vacuity is exhibited from both sides: `imQPhysicalRole_realPart` is a
model that satisfies the class with a non-constant observable, and
`not_imQPhysicalRole_norm` shows an observable that does see `Im(q)` fails it,
so the class is not satisfied by everything.
-/

namespace QOU.BraidKnot

/-- The default real-axis projection of the complex substrate parameter `q : ℂ`,
    discarding `Im(q)` so that `Im(default_q_real q) = 0` (bean `qreal`). -/
noncomputable def default_q_real (q : ℂ) : ℂ := ((q.re : ℝ) : ℂ)

/-- Under modulus projection (categorical mass formula), a mass observable
    `m(q) = |F(q)|` is invariant under `q ↦ q̄` for any conjugation-equivariant
    `F` — in particular for a real-coefficient polynomial (e.g. the Markov
    trace), where `F(q̄) = F(q)‾` holds and is supplied as the hypothesis `hF`. -/
-- Ref: [leitner2026] conj:im-q-physical-role
theorem mass_observable_conj_invariance
    {F : ℂ → ℂ} (q : ℂ)
    (hF : F (starRingEnd ℂ q) = starRingEnd ℂ (F q)) :
    ‖F (starRingEnd ℂ q)‖ = ‖F q‖ := by
  rw [hF]
  exact Complex.norm_conj (F q)

/-- Three candidate roles for `Im(q)`, enumerated for audit visibility. The
    conjecture does not pick one; identifying the physical role is open work. -/
inductive ImQCandidateRole
  | chirality_orientation
  | phase_dual_to_cal2
  | non_hermitian_deformation

/-- **Conjecture (primary, §3b-tax).** The real observable `obs` cannot resolve
    `Im(q)` at the substrate modulus `q`: it factors through the modulus of a
    conjugation-equivariant map, and at leading order its value at `q` agrees
    with its value at `Re q`.

    Both fields are hypotheses about the *observable*, not about `Im(q)`; the
    conclusion that `Im(q)` is undetermined is derived below. There is
    deliberately **no instance** for the QOU mass observable — supplying one is
    the open work. -/
class ImQPhysicalRole (obs : ℂ → ℝ) (q : ℂ) : Prop where
  /-- The observable is the modulus of a conjugation-equivariant map. -/
  factors_through_modulus :
    ∃ F : ℂ → ℂ,
      (∀ z, F (starRingEnd ℂ z) = starRingEnd ℂ (F z)) ∧ (∀ z, obs z = ‖F z‖)
  /-- At leading order the observable does not move when `Im(q)` is discarded. -/
  leading_order_real : obs q = obs ((q.re : ℝ) : ℂ)

variable {obs : ℂ → ℝ} {q : ℂ}

/-- Derived from the first field alone: a modulus observable is blind to the
    **sign** of `Im(q)`. Weaker than the conjecture — see the scope note. -/
theorem obs_conj_invariance [h : ImQPhysicalRole obs q] (z : ℂ) :
    obs (starRingEnd ℂ z) = obs z := by
  obtain ⟨F, hF, hobs⟩ := h.factors_through_modulus
  rw [hobs, hobs, hF]
  exact Complex.norm_conj (F z)

/-- **Payoff.** An observable satisfying the class cannot tell the substrate
    modulus `q` from a *real* number: some point with zero imaginary part,
    distinct from `q`, carries the same observable value. This is the precise
    sense in which `Im(q)` has no current observable. The conclusion is not a
    class field — it is derived from `leading_order_real`. -/
theorem im_q_undetermined [h : ImQPhysicalRole obs q] (hq : q.im ≠ 0) :
    ∃ z : ℂ, z.im = 0 ∧ z ≠ q ∧ obs z = obs q := by
  refine ⟨((q.re : ℝ) : ℂ), by simp, ?_, h.leading_order_real.symm⟩
  intro hz
  exact hq (by simpa using congrArg Complex.im hz.symm)

/-- Non-vacuity, positive side: taking the real part is a **non-constant**
    observable satisfying the class at every `q`. -/
theorem imQPhysicalRole_realPart (q : ℂ) :
    ImQPhysicalRole (fun z => ‖((z.re : ℝ) : ℂ)‖) q where
  factors_through_modulus :=
    ⟨fun z => ((z.re : ℝ) : ℂ), by intro z; simp, by intro z; rfl⟩
  leading_order_real := by simp

/-- That model really is non-constant, so the positive side above is not the
    trivial `obs = 0` witness. -/
theorem imQPhysicalRole_realPart_nonconstant :
    (fun z : ℂ => ‖((z.re : ℝ) : ℂ)‖) 0 ≠ (fun z : ℂ => ‖((z.re : ℝ) : ℂ)‖) 1 := by
  simp

/-- Non-vacuity, negative side: the modulus `‖·‖` **does** see `Im(q)` and so
    fails the class at `q = i`. The class is therefore falsifiable. -/
theorem not_imQPhysicalRole_norm :
    ¬ ImQPhysicalRole (fun z => ‖z‖) Complex.I := by
  intro h
  have := h.leading_order_real
  simp at this

end QOU.BraidKnot
