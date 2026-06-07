/-
  # Mass-side `MassSideKernel` typeclass — formalize-first §4 gates

  Sibling .lean for the `prop:mass-side-kernel-formalize-first-gates`
  block. Mass-theory analog of the Q_β decay-side `BarEvenKernel`
  typeclass from PR #1893.

  Bundles three parametric §4 gate classes for any candidate
  `linking_weight` function w : ℝ → ℝ:

    §4(a) MassAnchorStableGateClass swing
          — cross-anchor swing |w(q_μ) - w(q_p)| / |w(q_p)| < 1 ppm

    §4(c) MassQOneShadowGateClass w (anchor : Option ℝ)
          — w(1) matches a registered categorical anchor
            (currently OPEN — no registered anchor exists per PR #1896;
            class parameterized on `anchor` so future candidates can
            be evaluated against hypothetical anchors)

    §4(d) MassDirectionSanityGateClass m_candidate
          — |m_candidate - target| ≤ threshold · target (additive
            form, matches PR #1890 Lean precedent; sympy probes
            implement the multiplicative variant per PR #1899)

  The §4(b) bar-even invariant is the Q_β CommRing R structural
  identity (PR #1875) and works for any kernel; cited externally.

  Per Gemini review on PR #1921: the per-gate classes only carry the
  parameters they USE (no unused `w` in anchor / direction gates).
  `MassSideKernel` uses `extends` rather than duplicating fields, so
  lifting becomes automatic via parent-class projections.

  Sorry-free.

  Ref: https://github.com/litlfred/qou/pull/1786
       https://github.com/litlfred/qou/pull/1850  (z<1 obstruction)
       https://github.com/litlfred/qou/pull/1875  (bar-even §4(b))
       https://github.com/litlfred/qou/pull/1889  (Q_β §4(a))
       https://github.com/litlfred/qou/pull/1890  (Q_β §4(c) + (d))
       https://github.com/litlfred/qou/pull/1893  (Q_β BarEvenKernel)
       https://github.com/litlfred/qou/pull/1896  (mass-side §4 matrix)
       https://github.com/litlfred/qou/pull/1899  (mass-side q=1 anchor hunt: Σf^λ/4 = 5/2)
-/

import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum

namespace QOU.Mass.MassSideKernelFormalize

universe u

/-! ## Substrate constants (inherited from PR #1893's typeclass) -/

/-- The proton-pinned substrate q_0 (50 dps). -/
-- Ref: https://github.com/litlfred/qou/pull/1727
noncomputable def q_substrate : ℝ := 1.10997858275138

/-- Anchor-stability tolerance (1 ppm relative, per PR #1727 fibre-level). -/
-- Ref: https://github.com/litlfred/qou/pull/1727
noncomputable def anchorTolerance : ℝ := 0.000001

/-- Direction-sanity target for `linking_weight` at q_0 (CODATA-implied
    near-match ≈ 2.46 per PR #1850 framing). -/
-- Ref: https://github.com/litlfred/qou/pull/1850
noncomputable def directionTarget : ℝ := 2.46

/-- Direction-sanity threshold (10× order-of-magnitude check). -/
-- Ref: https://github.com/litlfred/qou/pull/1850
noncomputable def directionThreshold : ℝ := 10

/-! ## Per-gate parametric conditional classes

    Each class carries only the parameters its field hypothesis USES
    (per Gemini review on PR #1921: unused `w` in anchor/direction
    classes hampers Lean 4 typeclass synthesis). The candidate
    `w : ℝ → ℝ` is threaded through the unified `MassSideKernel`
    bundle below, where the §4(c) `MassQOneShadowGateClass` needs it. -/

/-- **§4(a) mass-side anchor-stability gate.**

    Parametric over the cross-anchor swing magnitude `swing` (typically
    computed by a sympy probe as `|w(q_μ) - w(q_p)| / |w(q_p)|`).
    Instantiation requires the swing to be within the 1 ppm fibre-level
    tolerance. -/
-- Ref: [manuscript] prop:mass-side-kernel-formalize-first-gates
class MassAnchorStableGateClass (swing : ℝ) : Prop where
  /-- The candidate's cross-anchor swing is within the 1 ppm
      fibre-level tolerance (PR #1727). -/
  swing_within_tolerance :
    swing ≤ anchorTolerance

/-- **Gate theorem (forward, §4(a)):** under the class, the swing is
    bounded. -/
-- Ref: [manuscript] prop:mass-side-kernel-formalize-first-gates
theorem mass_anchor_stable_forward
    (swing : ℝ) [hC : MassAnchorStableGateClass swing] :
    swing ≤ anchorTolerance :=
  hC.swing_within_tolerance

/-- **Gate theorem (refute, §4(a)):** if the swing exceeds the
    tolerance, the class cannot be instantiated. -/
-- Ref: [manuscript] prop:mass-side-kernel-formalize-first-gates
theorem mass_anchor_stable_reject
    (swing : ℝ) (h_swing_too_large : swing > anchorTolerance) :
    ¬ MassAnchorStableGateClass swing := by
  intro hC
  exact absurd hC.swing_within_tolerance (not_le.mpr h_swing_too_large)

/-- **§4(c) mass-side q=1 classical-limit shadow gate.**

    Parametric over the candidate `linking_weight` function w AND the
    registered anchor (Option ℝ). The anchor is `Option` because the
    registered categorical value for linking_weight(q=1) is the OPEN
    GAP identified by PR #1896 — no canonical derivation exists yet.

    The field is stated as `∀ a, anchor = some a → w 1 = a` rather
    than a `match`-on-type to keep the class fully Prop-valued without
    relying on iota reduction in user-facing theorems. When
    `anchor = none` this is vacuously true; when `anchor = some a` it
    requires `w 1 = a`.

    This enables FUTURE candidates (e.g. PR #1899's Σ f^λ/4 = 5/2
    finding = #involutions(S_4)/4) to be evaluated against the
    hypothetical anchor `some (5/2)`. -/
-- Ref: [manuscript] prop:mass-side-kernel-formalize-first-gates
-- Ref: https://github.com/litlfred/qou/pull/1896
-- Ref: https://github.com/litlfred/qou/pull/1899
class MassQOneShadowGateClass
    (w : ℝ → ℝ) (anchor : Option ℝ) : Prop where
  /-- The candidate's q=1 limit matches the registered anchor (when
      one exists). Vacuously true when `anchor = none`. -/
  shadow_holds : ∀ a, anchor = some a → w 1 = a

/-- **Gate theorem (forward, §4(c)):** under the class with a
    registered anchor, the candidate's q=1 limit matches. -/
-- Ref: [manuscript] prop:mass-side-kernel-formalize-first-gates
theorem mass_q_one_shadow_forward
    (w : ℝ → ℝ) (a : ℝ)
    [hC : MassQOneShadowGateClass w (some a)] :
    w 1 = a :=
  hC.shadow_holds a rfl

/-- **Gate theorem (refute, §4(c)):** if a registered anchor exists
    and the candidate's q=1 limit disagrees, the class is rejected. -/
-- Ref: [manuscript] prop:mass-side-kernel-formalize-first-gates
theorem mass_q_one_shadow_reject
    (w : ℝ → ℝ) (a : ℝ) (h_candidate : w 1 ≠ a) :
    ¬ MassQOneShadowGateClass w (some a) := by
  intro hC
  exact h_candidate (hC.shadow_holds a rfl)

/-- **§4(d) mass-side direction-sanity gate.**

    Parametric over the candidate's substrate magnitude
    `m_candidate = |w(q_0)|`. Instantiation requires
    `|m_candidate - target| ≤ threshold · target` — the additive
    form that matches PR #1890's `q-beta-direction-sanity-gate.lean`
    Lean precedent.

    Note: sympy probes (e.g. `mass_theory_formalize_first_invariants_probe.py`,
    PR #1896) implement the multiplicative variant
    `max(|m|/target, target/|m|) ≤ threshold` for the operational
    direction-magnitude check; the additive form here is the Lean-
    side abstract scaffold that admits both variants as instances
    (a multiplicative-passing candidate also satisfies the additive
    form within the same threshold magnitude). -/
-- Ref: [manuscript] prop:mass-side-kernel-formalize-first-gates
class MassDirectionSanityGateClass (m_candidate : ℝ) : Prop where
  /-- Additive bound: |m_candidate - target| ≤ threshold · target. -/
  magnitude_within_threshold :
    |m_candidate - directionTarget|
      ≤ directionThreshold * directionTarget

/-- **Gate theorem (forward, §4(d)):** under the class, the magnitude
    is bounded. -/
-- Ref: [manuscript] prop:mass-side-kernel-formalize-first-gates
theorem mass_direction_sanity_forward
    (m_candidate : ℝ)
    [hC : MassDirectionSanityGateClass m_candidate] :
    |m_candidate - directionTarget|
      ≤ directionThreshold * directionTarget :=
  hC.magnitude_within_threshold

/-- **Gate theorem (refute, §4(d)):** if the magnitude exceeds the
    threshold, the class cannot be instantiated. -/
-- Ref: [manuscript] prop:mass-side-kernel-formalize-first-gates
theorem mass_direction_sanity_reject
    (m_candidate : ℝ)
    (h_mismatch :
      |m_candidate - directionTarget|
        > directionThreshold * directionTarget) :
    ¬ MassDirectionSanityGateClass m_candidate := by
  intro hC
  exact absurd hC.magnitude_within_threshold (not_le.mpr h_mismatch)

/-! ## Unified typeclass — extends the per-gate classes

    Per Copilot + Gemini reviews on PR #1921: `extends` is the
    idiomatic Lean 4 way to bundle parent classes. Lifting lemmas
    become automatic via inherited field projections, eliminating
    drift risk between the bundle and individual gate definitions. -/

/-- **`MassSideKernel` — the unified mass-side formalize-first typeclass.**

    Parametric over the four candidate-specific values:
    - `w`: the candidate linking_weight function
    - `swing`: cross-anchor swing magnitude (probe-computed)
    - `anchor`: registered q=1 categorical anchor (None for open gap)
    - `magnitude`: |w(q_0)| substrate magnitude

    Defined as the extension of the three per-gate parametric classes
    so the bundle equals the conjunction of its parents by construction.
    Mirrors the decay-side `BarEvenKernel` typeclass; uses the
    `extends` pattern for cleaner downstream composition.

    The §4(b) bar-even invariant is automatic for substrate-derived
    candidates via the Q_β CommRing R lemma (PR #1875). -/
-- Ref: [manuscript] prop:mass-side-kernel-formalize-first-gates
class MassSideKernel
    (w : ℝ → ℝ) (swing : ℝ) (anchor : Option ℝ) (magnitude : ℝ)
    extends MassAnchorStableGateClass swing,
            MassQOneShadowGateClass w anchor,
            MassDirectionSanityGateClass magnitude : Prop

/-! ## Lifting lemmas (via inherited field projections) -/

/-- **§4(a) lifting**: from the bundle, the anchor-stability gate holds. -/
-- Ref: [manuscript] prop:mass-side-kernel-formalize-first-gates
theorem mass_side_kernel_implies_anchor_stable
    (w : ℝ → ℝ) (swing : ℝ) (anchor : Option ℝ) (magnitude : ℝ)
    [hK : MassSideKernel w swing anchor magnitude] :
    swing ≤ anchorTolerance :=
  hK.swing_within_tolerance

/-- **§4(d) lifting**: from the bundle, the direction-sanity gate holds. -/
-- Ref: [manuscript] prop:mass-side-kernel-formalize-first-gates
theorem mass_side_kernel_implies_direction_sanity
    (w : ℝ → ℝ) (swing : ℝ) (anchor : Option ℝ) (magnitude : ℝ)
    [hK : MassSideKernel w swing anchor magnitude] :
    |magnitude - directionTarget|
      ≤ directionThreshold * directionTarget :=
  hK.magnitude_within_threshold

/-- **§4(c) lifting (when registered)**: from the bundle with a
    registered anchor, the q=1 shadow holds. -/
-- Ref: [manuscript] prop:mass-side-kernel-formalize-first-gates
theorem mass_side_kernel_implies_q_one_shadow
    (w : ℝ → ℝ) (swing : ℝ) (a : ℝ) (magnitude : ℝ)
    [hK : MassSideKernel w swing (some a) magnitude] :
    w 1 = a :=
  hK.shadow_holds a rfl

/-- **Rejection: failing the §4(a) gate prevents bundle instantiation.**

    Concrete rejection lemma for the most common failure mode
    (cross-anchor swing too large). Analogous rejection lemmas exist
    per-field via the parametric gate classes above. -/
-- Ref: [manuscript] prop:mass-side-kernel-formalize-first-gates
theorem mass_side_kernel_reject_anchor_too_large
    (w : ℝ → ℝ) (swing : ℝ) (anchor : Option ℝ) (magnitude : ℝ)
    (h_swing : swing > anchorTolerance) :
    ¬ MassSideKernel w swing anchor magnitude := by
  intro hK
  exact absurd hK.swing_within_tolerance (not_le.mpr h_swing)

/-- **Threshold positivity helper**: the direction threshold is > 0. -/
-- Ref: [manuscript] prop:mass-side-kernel-formalize-first-gates
theorem mass_direction_threshold_positive :
    directionThreshold > 0 := by
  unfold directionThreshold
  norm_num

end QOU.Mass.MassSideKernelFormalize
