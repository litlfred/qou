/-
  Bean `qou-z9ws` — the four §4 "formalize-first gate" classes are NOT vacuous,
  and the direction-sanity pair does not reject what its docstring says it does.

  WHAT THIS FILE IS, AND WHY IT HAS NO IMPORTS

  `MassAnchorStableGateClass`, `MassDirectionSanityGateClass`,
  `DirectionSanityGateClass` and `BarEvenKernel` live in **content-block
  siblings** under `content/quantum-observable-universe/mass-theory/`, not in
  the `QOU` library tree.  They are not modules, so they have no olean and
  nothing can `import` them.  The route is copy-and-compile: concatenate the
  siblings with this fragment and hand the result to `lean`.  The script
  [`scripts/lean-sibling-witness-check.sh`](../../scripts/lean-sibling-witness-check.sh)
  does exactly that; the invocation is at the bottom of this header.

  Conveniently, all three siblings import nothing but `Mathlib.Data.Real.Basic`
  and `Mathlib.Tactic.NormNum`, so the concatenation needs no other setup.

  THE VERDICT: not vacuous — these four are the good case

  Every other class hand-adjudicated in this arc is *vacuous*: inhabited with no
  hypotheses, so a `[C]` binder assumes nothing.  These four are different and
  are scored as such.  Each takes real-valued parameters and each field is a
  genuine constraint on them — an exact equality (`c2 1 = -1`), a 1e-6 relative
  tolerance (`|pole - uSubstrate| <= uSubstrate/1e6`), or a numeric band.  Each
  file also carries a `_reject` theorem showing the class is *refutable* at a
  bad parameter, which is the property a gate is supposed to have and which no
  vacuous class here possesses.  `BarEvenKernel` is inhabited below at its
  intended point — `pole := uSubstrate`, `c2 := -1`, `c3 := J_Hopf(1) = -2` —
  which is a real instance, not a degenerate one.

  BUT THE TWO DIRECTION GATES ARE MUCH WEAKER THAN THEY READ

  Both are stated additively, `|m - target| <= threshold * target`, with
  `threshold = 10`.  That is not "within 10x of the target"; it is a band of
  width `20 * target` **centred on the target**, so it reaches far below zero on
  one side:

      MassDirectionSanityGateClass:  target 2.46     pass band [-22.14, 27.06]
      DirectionSanityGateClass:      target 0.99824  pass band [ -8.98, 10.98]

  Two consequences are proved below rather than asserted.

  1. **Zero clears both gates.**  A candidate predicting magnitude `0` — no
     signal at all — instantiates each class.

  2. **The whole `z < 1` region clears `DirectionSanityGateClass`**, proved as
     `admits_everything_below_one` for every `m` in `[0, 1]`.  That matters
     because the threshold's own docstring in
     `q-beta-direction-sanity-gate.lean` states its purpose as catching
     *"order-of-magnitude direction errors (like PR #1850's z < 1 vs
     target > 1)"*.  The interval `[0, 1]` sits strictly inside the pass band,
     so **no candidate can ever be rejected on the ground the docstring names.**
     Note also that the file's own target constant is
     `qBetaTargetMagnitudeAtQ0 = 0.99824`, which is *below* 1, so the
     "target > 1" in that sentence does not describe this file either.

  WHAT THIS DOES NOT SAY.  It does not say the gates are worthless — an
  additive band still rejects a candidate off by 30x, and `mass_*_reject` shows
  it.  It says the two direction gates cannot discriminate in the region their
  motivating example lives in, and that a reader taking "10x threshold" to mean
  a multiplicative ratio test will overestimate them.  The mass-side file is
  explicit that the additive form is deliberate and that the sympy probes use
  the multiplicative variant `max(|m|/target, target/|m|) <= threshold`; the two
  are not equivalent, and only the additive one is what the Lean gate enforces.

  VERIFY (lean-direct, Mathlib oleans restored, no `lake build` — a build
  against a restored cache with `traces=0` evicts it):

      scripts/lean-sibling-witness-check.sh \
        docs/audits/2026-08-30-gate-classes-admit-zero.lean \
        content/quantum-observable-universe/mass-theory/mass-side-kernel-formalize-first-gates.lean \
        content/quantum-observable-universe/mass-theory/q-beta-direction-sanity-gate.lean \
        content/quantum-observable-universe/mass-theory/q-beta-bar-even-kernel-typeclass.lean

  Measured 2026-08-30: exit 0, 0 errors.
-/

namespace GateProbe
open QOU.Mass.MassSideKernelFormalize

/-- A candidate with ZERO cross-anchor swing clears the anchor gate.  This one
is honest as a gate: the tolerance is 1e-6, so it is genuinely tight. -/
instance : MassAnchorStableGateClass 0 where
  swing_within_tolerance := by unfold anchorTolerance; norm_num

/-- **A candidate predicting magnitude ZERO clears the direction-sanity gate.** -/
instance : MassDirectionSanityGateClass 0 where
  magnitude_within_threshold := by
    unfold directionTarget directionThreshold
    rw [abs_le]; constructor <;> norm_num

/-- The pass band is `[-22.14, 27.06]`; everything inside it clears. -/
theorem massDirection_band (m : ℝ) (h1 : -22 ≤ m) (h2 : m ≤ 27) :
    MassDirectionSanityGateClass m where
  magnitude_within_threshold := by
    unfold directionTarget directionThreshold
    rw [abs_le]; constructor <;> linarith

end GateProbe

namespace GateProbe2
open QOU.QBeta.DirectionSanityGate

/-- **Zero clears this one too.** -/
instance : DirectionSanityGateClass 0 where
  magnitude_match := by
    unfold qBetaTargetMagnitudeAtQ0 directionSanityThreshold
    rw [abs_le]; constructor <;> norm_num

/-- **EVERY candidate with magnitude in `[0, 1]` clears it** — so the whole
`z < 1` region the threshold's docstring names as what it catches is inside the
pass band, and nothing there can be rejected. -/
theorem admits_everything_below_one (m : ℝ) (h0 : 0 ≤ m) (h1 : m ≤ 1) :
    DirectionSanityGateClass m where
  magnitude_match := by
    unfold qBetaTargetMagnitudeAtQ0 directionSanityThreshold
    rw [abs_le]; constructor <;> linarith

end GateProbe2

namespace GateProbe3
open QOU.QBeta.BarEvenKernelTypeclass

/-- `BarEvenKernel` at its intended point: a genuine instance, not a degenerate
one.  Three of its four fields are exact equalities or a 1e-6 relative
tolerance; only `direction_match` is the loose band above. -/
instance : BarEvenKernel uSubstrate (fun _ => -1) (fun _ => jonesHopfAtQOne)
    directionTarget where
  pole_at_u_substrate := by
    simp only [sub_self, abs_zero]
    unfold radiusTolerance uSubstrate; norm_num
  c2_shadow := rfl
  c3_shadow := rfl
  direction_match := by
    simp only [sub_self, abs_zero]
    unfold directionThreshold directionTarget; norm_num

end GateProbe3
