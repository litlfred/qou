import { definition } from "../../schema/builders";

/**
 * Finite LP strong-duality + complementary-slackness as a §3b-cond
 * conditional-class hypothesis carrier.
 *
 * Closes the §3b-cond locale gap for the two `sorry`s in
 * `confinement-nf-partial-proof.lean` (theorems `strong_duality` +
 * `complementary_slackness`): instead of two free-standing
 * top-level `sorry`s, the LP-theory inputs become two fields of
 * a hypothesis class `HasFiniteLPDuality lp`.  When Mathlib gets
 * a finite-dim LP-duality library, the trivial-model sorrys can
 * be discharged unconditionally.
 *
 * The class is purely infrastructure — does not advance the math
 * of #567's crystal-R-matrix work, but provides a clean Lean
 * locale for #565 F11 (LP/SDP CI gate) or a future Mathlib-LP
 * wiring PR to consume.
 */
export default definition({
  label: "def:lp-duality-hypothesis-class",
  title:
    "Finite LP strong-duality + complementary-slackness " +
    "hypothesis class (§3b-cond)",
  uses: [
    "prop:operator-selection-lp",
  ],
  cites: [
    "schrijver1986theory",
  ],
  lean: {
    ref: "qou:QOU.BraidKnot.HasFiniteLPDuality",
    validation: "stub",
  },
  tags: [
    "lp-duality",
    "complementary-slackness",
    "strong-duality",
    "conditional-class",
    "section-3b-cond",
    "schrijver",
    "infrastructure",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Definition (`HasFiniteLPDuality` hypothesis class).**\n*The finite LP strong-duality and complementary-slackness theorems map into Lean via the hypothesis class:*\n\n```lean\nclass HasFiniteLPDuality (lp : OperatorSelectionLP) : Type where\n  dualityGapZero       : lp.duality_gap = 0\n  complementarySlackness :\n    ∀ (λ : lp.Λ), λ ∈ lp.active_set ↔ lp.tight λ\n```\n\nThis isolates standard LP-theory proofs—currently awaiting a full finite-dimensional LP Mathlib module—into explicit conditional fields. Consumer proofs pull this hypothesis class instead of bare `sorry` tags. When the formal Mathlib support lands, a trivial model substitution will unconditionally discharge the class requirements without altering any downstream mathematical commitments." },
  ],
});
