/-
  # Unified `BarEvenKernel` typeclass — bundling the four §4 gates

  Sibling .lean for the `prop:q-beta-bar-even-kernel-typeclass` block.
  Bundles the four §4 formalize-first invariants from PR #1875,
  PR #1889, and PR #1890 (Tracks A + B) into a single parametric Lean
  typeclass so any future kernel candidate is evaluable as ONE
  class-instance attempt rather than four separate gate checks.

  Composition:

    BarEvenKernel pole c2 c3 magnitude  ⇔
      §4(a) pole at u_substrate
    ∧ §4(c) c2(1) = -1  ∧  c3(1) = J_Hopf(1) = -2
    ∧ §4(d) magnitude within 10× of direction-target

  The §4(b) bar-even invariant is a CommRing R structural identity
  (PR #1875) that holds AUTOMATICALLY for substrate-derived candidates;
  the typeclass does not duplicate it. Use the standalone PR #1875
  gate when checking non-substrate candidates.

  Sorry-free. Three lifting lemmas show the bundle is consistent with
  the parametric gate classes from PR #1890.

  Ref: [pr1786] https://github.com/litlfred/qou/pull/1786
       [pr1875] https://github.com/litlfred/qou/pull/1875
       [pr1889] https://github.com/litlfred/qou/pull/1889
       [pr1890] https://github.com/litlfred/qou/pull/1890
       docs/audits/2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md
       docs/audits/2026-06-05-qbeta-formalize-first-gates-consolidation.md
-/

import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum

namespace QOU.QBeta.BarEvenKernelTypeclass

universe u

/-! ## Substrate constants (inherited from the per-gate files) -/

/-- The established u_substrate value (PR #1727 cross-anchor). -/
-- Ref: [pr1727] https://github.com/litlfred/qou/pull/1727
noncomputable def uSubstrate : ℝ := 0.008517234550156142

/-- Radius-of-convergence fibre tolerance (1 ppm relative). -/
-- Ref: [pr1727] https://github.com/litlfred/qou/pull/1727
noncomputable def radiusTolerance : ℝ := uSubstrate / 1000000

/-- The Hopf-Jones classical value `J_Hopf(q=1) = -2` (registry §3). -/
-- Ref: [jones1985] doi:10.2307/1971403
noncomputable def jonesHopfAtQOne : ℝ := -2

/-- Direction-sanity target magnitude (PR #1727 + PR #1786 substrate
    derivation: `Q_β / [Q_A · cos α_eff] ≈ 0.998` at q_0).

    Comparison-boundary constant: `0.99824` is computed from the measured
    `Q_β`, so a gate stated against it is a screening check at the
    comparison with measurement, not a derived invariant of the kernel. -/
-- Ref: [pr1727] https://github.com/litlfred/qou/pull/1727
noncomputable def directionTarget : ℝ := 0.99824

/-- Direction-sanity threshold (10× order-of-magnitude check). -/
-- Ref: [pr1850] https://github.com/litlfred/qou/pull/1850
noncomputable def directionThreshold : ℝ := 10

/-! ## The unified typeclass -/

/-- **`BarEvenKernel` — the unified formalize-first typeclass.**

    Parametric over the four candidate-specific values:
    - `pole`: the candidate's nearest singularity in the u-plane
    - `c2`, `c3`: the candidate's per-rung ladder coefficient functions
    - `magnitude`: the candidate's substrate magnitude |F(q_0)|

    Instantiation requires the candidate to clear all three structural
    §4 gates that depend on candidate-specific data: §4(a) radius-of-
    convergence, §4(c) q=1 shadow, and §4(d) direction sanity. The
    §4(b) bar-even invariant is automatic for substrate-derived
    candidates (it's a CommRing R structural identity) and is checked
    separately via PR #1875's standalone lemma when needed.

    Per Gemini's HIGH-priority feedback on PR #1890: PARAMETRIC over
    the candidate-specific arguments so multiple candidates can be
    checked in the same environment. -/
-- Ref: [leitner2026] prop:q-beta-bar-even-kernel-typeclass
class BarEvenKernel
    (pole : ℝ) (c2 c3 : ℝ → ℝ) (magnitude : ℝ) : Prop where
  /-- §4(a) radius-of-convergence: candidate's nearest pole is at
      `u_substrate` within the fibre-level tolerance. -/
  pole_at_u_substrate :
    |pole - uSubstrate| ≤ radiusTolerance
  /-- §4(c) q=1 classical-limit shadow for c_2: must equal -1
      (PR #1786 Taylor-exact anchor). -/
  c2_shadow : c2 1 = -1
  /-- §4(c) q=1 classical-limit shadow for c_3: must equal
      `J_Hopf(1) = -2` (registry §3 anchor). -/
  c3_shadow : c3 1 = jonesHopfAtQOne
  /-- §4(d) direction sanity: candidate's substrate magnitude is
      within the 10× threshold of the target. -/
  direction_match :
    |magnitude - directionTarget| ≤ directionThreshold * directionTarget

/-! ## Lifting lemmas — composition with the parametric gate classes -/

/-- **§4(a) lifting**: from the bundle, the radius-of-convergence
    pole-location invariant. -/
-- Ref: [leitner2026] prop:q-beta-bar-even-kernel-typeclass
-- Ref: [pr1889] https://github.com/litlfred/qou/pull/1889
theorem bar_even_kernel_implies_radius_of_convergence
    (pole : ℝ) (c2 c3 : ℝ → ℝ) (magnitude : ℝ)
    [hK : BarEvenKernel pole c2 c3 magnitude] :
    |pole - uSubstrate| ≤ radiusTolerance :=
  hK.pole_at_u_substrate

/-- **§4(c) lifting**: from the bundle, both q=1 classical-limit
    shadows hold.

    **Assumed, not derived here** — "from the bundle" means projected from
    it: the body is `⟨hK.c2_shadow, hK.c3_shadow⟩`, both conjuncts carried
    verbatim as `BarEvenKernel` fields. The lifting is the repackaging, not a
    derivation of the shadows. `c2`/`c3` are arbitrary functions, so the
    statement is genuinely conditional and may not be strengthened to a
    global `axiom`. -/
-- Ref: [leitner2026] prop:q-beta-bar-even-kernel-typeclass
-- Ref: [pr1890] https://github.com/litlfred/qou/pull/1890 (Track A)
def bar_even_kernel_implies_q_one_shadow
    (pole : ℝ) (c2 c3 : ℝ → ℝ) (magnitude : ℝ)
    [hK : BarEvenKernel pole c2 c3 magnitude] :
    c2 1 = -1 ∧ c3 1 = jonesHopfAtQOne :=
  ⟨hK.c2_shadow, hK.c3_shadow⟩

/-- **§4(d) lifting**: from the bundle, the direction-sanity
    magnitude-match invariant. -/
-- Ref: [leitner2026] prop:q-beta-bar-even-kernel-typeclass
-- Ref: [pr1890] https://github.com/litlfred/qou/pull/1890 (Track B)
theorem bar_even_kernel_implies_direction_sanity
    (pole : ℝ) (c2 c3 : ℝ → ℝ) (magnitude : ℝ)
    [hK : BarEvenKernel pole c2 c3 magnitude] :
    |magnitude - directionTarget|
      ≤ directionThreshold * directionTarget :=
  hK.direction_match


/-- **The bundle IS the conjunction of its gates** — the `.md`'s
    *"instantiating `BarEvenKernel` is equivalent to clearing all four gates
    simultaneously"*, stated.

    Added 2026-08-31 (bean `qou-z9ws`). The three lifting lemmas above are the
    **forward** half of this equivalence and nothing more: each returns the
    class field its type restates, which is the accessor idiom
    (`Group.mul_assoc`), not a derivation. The `.md` claims an *equivalence*,
    and the converse — that the four facts suffice to build the bundle — was
    never stated, so the block's actual claim had no Lean. It does now, and the
    lifting lemmas are one direction of it rather than free-standing
    projections.

    Note that §4(b), the bar-even invariant, is deliberately **not** a field of
    `BarEvenKernel` (it is automatic for substrate-derived candidates, per the
    module docstring), so "all four gates" here is three class fields plus the
    two `q = 1` shadows. -/
-- Ref: [leitner2026] prop:q-beta-bar-even-kernel-typeclass
theorem barEvenKernel_iff
    (pole : ℝ) (c2 c3 : ℝ → ℝ) (magnitude : ℝ) :
    BarEvenKernel pole c2 c3 magnitude ↔
      (|pole - uSubstrate| ≤ radiusTolerance ∧
        c2 1 = -1 ∧
        c3 1 = jonesHopfAtQOne ∧
        |magnitude - directionTarget|
          ≤ directionThreshold * directionTarget) :=
  ⟨fun h => ⟨h.pole_at_u_substrate, h.c2_shadow, h.c3_shadow,
             h.direction_match⟩,
   fun h => ⟨h.1, h.2.1, h.2.2.1, h.2.2.2⟩⟩

/-- **Rejection: if any of the four invariants fail, the bundle is
    unsatisfiable.**

    The Lean type system enforces this automatically — there is no
    way to construct `BarEvenKernel pole c2 c3 magnitude` if any of
    the four field hypotheses cannot be discharged. This rejection
    lemma makes the obstruction explicit for one specific failure
    mode (wrong c_2 shadow); analogous rejection lemmas exist
    per-field in PR #1890's parametric gate classes. -/
-- Ref: [leitner2026] prop:q-beta-bar-even-kernel-typeclass
theorem bar_even_kernel_reject_wrong_c2_shadow
    (pole : ℝ) (c2 c3 : ℝ → ℝ) (magnitude a : ℝ)
    (h_candidate_c2 : c2 1 = a) (h_mismatch : a ≠ -1) :
    ¬ BarEvenKernel pole c2 c3 magnitude := by
  intro hK
  have h_eq : a = -1 := by
    rw [← h_candidate_c2]
    exact hK.c2_shadow
  exact h_mismatch h_eq

/-- **Direction threshold positivity**: 10 > 0. Used downstream when
    reasoning about the magnitude check. -/
-- Ref: [leitner2026] prop:q-beta-bar-even-kernel-typeclass
theorem direction_threshold_positive :
    directionThreshold > 0 := by
  unfold directionThreshold
  norm_num

/-! ## The gate ACCEPTS at its intended point

    This file proved that `BarEvenKernel` can **reject**
    (`bar_even_kernel_reject_wrong_c2_shadow`) and never that it can
    **accept**, and the two are not the same evidence.

    Why the missing half matters here specifically: the three lifting lemmas
    above are *projections* — `bar_even_kernel_implies_radius_of_convergence`
    is literally `hK.pole_at_u_substrate`, and the §4(c) one says so in its own
    docstring ("Assumed, not derived here"). Under the `qou-z9ws` inhabitation
    discriminator a projection is the legitimate Mathlib accessor idiom **only
    when something builds the bundle**; with no witness, a `[BarEvenKernel …]`
    binder and its three unbundlers are indistinguishable from a `Fact` wrapper
    around an assumption nobody can meet.

    The witness existed and was in the wrong place. Bean `qou-z9ws` built it in
    `docs/audits/2026-08-30-gate-classes-admit-zero.lean`, which — as its own
    header explains — **has no imports and is imported by nothing**: these
    classes live in content-block siblings rather than the `QOU` library tree,
    so that probe is reachable only by concatenating the files and handing the
    result to `lean`. A non-degeneracy witness a reader cannot follow from the
    class is not doing the job. It is reproduced here, at the class. -/

/-- **`BarEvenKernel` accepts at its intended point** — `pole = u_substrate`,
    `c₂ ≡ -1`, `c₃ ≡ J_Hopf(1) = -2`, `magnitude = directionTarget`.

    A genuine instance, not a degenerate one: three of the four fields are
    exact equalities or a 1e-6 relative tolerance, and the parameters are the
    substrate values the gates were written for rather than values chosen to
    pass. Together with `bar_even_kernel_reject_wrong_c2_shadow` this makes the
    class a gate in both directions — it admits something and refuses
    something — which is the property the three lifting lemmas need in order to
    be accessors rather than assumptions.

    A `def`, not an `instance`. It would only ever fire at these exact
    arguments, so global resolution is not the hazard it is for a
    parameter-free carrier; but a caller should still say
    `letI := barEvenKernelAtIntendedPoint` and have the dependence visible at
    the use site. -/
-- Ref: [leitner2026] prop:q-beta-bar-even-kernel-typeclass
noncomputable def barEvenKernelAtIntendedPoint :
    BarEvenKernel uSubstrate (fun _ => -1) (fun _ => jonesHopfAtQOne)
      directionTarget where
  pole_at_u_substrate := by
    simp only [sub_self, abs_zero]
    unfold radiusTolerance uSubstrate; norm_num
  c2_shadow := rfl
  c3_shadow := rfl
  direction_match := by
    simp only [sub_self, abs_zero]
    unfold directionThreshold directionTarget; norm_num

/-- The class is inhabited — the statement the three lifting lemmas rest on,
    now available at the class rather than only in an unimported probe. -/
-- Ref: [leitner2026] prop:q-beta-bar-even-kernel-typeclass
theorem barEvenKernel_nonempty :
    Nonempty (BarEvenKernel uSubstrate (fun _ => -1)
      (fun _ => jonesHopfAtQOne) directionTarget) :=
  ⟨barEvenKernelAtIntendedPoint⟩

end QOU.QBeta.BarEvenKernelTypeclass
