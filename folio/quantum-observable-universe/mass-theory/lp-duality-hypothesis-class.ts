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
});
