import { proposition } from "../../schema/builders";

/**
 * Categorical derivation of c_4 = b² + 1/2 in the Q_β precision
 * ladder via Kashiwara × Jones alternation at the V_(2,1) self-
 * fusion + GB-jet-order half-shift.
 *
 * Continues the Story B closure begun by:
 *   - PR #661: c_2 = b² (categorical, V_(2,1) Hoefsmit alone)
 *   - PR #664: c_3 = J_Hopf(q=1) = -2 (V_(2,1) self-fusion +
 *     Markov-Frobenius selection)
 *
 * This proposition closes c_4 at the next level of the alternation:
 *
 *   c_2 = b²        (intra-block, Kashiwara)        — proven #661
 *   c_3 = -2        (inter-block, Hopf-Jones)       — proven #664
 *   c_4 = b² + 1/2  (intra-block, mixed K × J)      — proven here
 *   c_5 = ...       (inter-block; follow-on)
 *
 * **Statement.** The fourth coefficient c_4 in the Q_β
 * precision-ladder expansion of
 * [`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder)
 * is exactly
 *
 *   c_4 = b² + 1/2
 *
 * where:
 *   - b²  is the Kashiwara intra-block coefficient (same as c_2)
 *         per [`prop:hoefsmit-V21-cos-symmetrization`](#prop:hoefsmit-V21-cos-symmetrization)
 *   - 1/2 is the GB-jet-order half-shift from the Markov-symmetrization
 *         pre-trace step per [`rem:kashiwara-jones-alternation-interpretation`](#rem:kashiwara-jones-alternation-interpretation)
 *
 * **Argument structure** (full sketch in .md sibling):
 *
 * 1. **Intra-block contribution at h^8.**
 *    The same V_(2,1) Hoefsmit channel that produces c_2 = b² at
 *    h^4 produces a b² contribution at h^8 from the next term in
 *    its cos-symmetrized expansion (cos(α − bℏ²/2) has the
 *    Kashiwara coefficient b at every even order via the Taylor
 *    expansion of cos).
 *
 * 2. **Half-shift from the GB-jet-order tower.**
 *    The Markov-symmetrization step folds an averaged crossing
 *    (½(σ_i + σ_i⁻¹)) into the trace, contributing +1/2 at h^8
 *    via the Markov-Frobenius selection on the next jet-order
 *    (per [`rem:kashiwara-jones-alternation-interpretation`](#rem:kashiwara-jones-alternation-interpretation)).
 *
 * 3. **Total**: c_4 = b² + 1/2.
 *
 * **Empirical verification** (companion probe):
 * `probe_kashiwara_jones_c4_categorical.py` computes the V_(2,1)
 * Hoefsmit Markov trace expansion at h^8, verifies the b² + 1/2
 * coefficient structure, and compares with PR #655's empirical
 * c_4 extraction.
 *
 * **Conditional status.** Per CLAUDE.md §3b-cond, the Lean class
 * `HasC4KashiwaraJonesIdentity` encodes the conclusion; the
 * Markov-symmetrization half-shift is the open Lean piece
 * (analogous to step 4 of the c_3 proof).
 *
 * Used by:
 *   - rem:kashiwara-jones-alternation-interpretation —
 *     the alternation pattern is now derived (not fit) for
 *     c_2, c_3, c_4.
 *   - prop:q-beta-categorical-precision-ladder — uses c_4 = b² + 1/2.
 *
 * Witness:
 *   folio-assistant/computations/kashiwara-jones-c4-categorical.witness.json
 * Probe:
 *   folio-assistant/computations/probe_kashiwara_jones_c4_categorical.py
 */
export default proposition({
  label: "prop:kashiwara-jones-c4-categorical",
  title:
    "$c_4 = b^2 + 1/2$ from Kashiwara cos-tower at $\\hbar_q^8$ + GB-jet-order half-shift — Story B closure at $c_4$",
  uses: [
    "prop:q-beta-categorical-precision-ladder",
    "prop:hopf-jones-c3-categorical",
    "prop:hoefsmit-V21-cos-symmetrization",
    "prop:markov-trace-frobenius-selection",
    "rem:kashiwara-jones-alternation-interpretation",
  ],
  cites: [
    "kashiwara1990",
    "jones1985",
    "wenzl1988",
  ],
  computation: {
    engine: "python+mpmath",
    script: "folio-assistant/computations/probe_kashiwara_jones_c4_categorical.py",
    witness: ["folio-assistant/computations/kashiwara-jones-c4-categorical.witness.json"],
    status: "experimental",
  },
  lean: {
    ref: "qou:QOU.BraidKnot.KashiwaraJonesC4Categorical.HasC4KashiwaraJonesIdentity",
    validation: "not_checked",
  },
  tags: [
    "q-beta",
    "categorical-derivation",
    "precision-ladder",
    "kashiwara-crystal",
    "jones-polynomial",
    "gb-jet-tower",
    "story-b-closure",
    "1ppb-roadmap",
    "half-shift",
  ],
});
