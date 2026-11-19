import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:qbeta-delta-tau-canonical-conditional-q2-minus-1-factor",
  title:
    "Conditional on canonical Markov weights: $\\Delta\\mathrm{tr}_M^{\\text{can}}(q)$ factors $(q^2 - 1)$",
  uses: [
    "prop:qbeta-per-block-chi-closed-forms",
  ],
  cites: ["wenzl1988", "hoefsmit1974"],
  tags: [
    "qbeta",
    "delta-tau-M",
    "canonical",
    "conditional",
    "3b-cond",
    "pre-archimedean",
  ],
  lean: {
    ref:
      "qou:QOU.BraidKnot.delta_tau_M_canonical_has_q2_minus_1_factor",
  },
  authorNotes: [
    { kind: "note", body: "Archimedean specialisation over R (§7c)." },
    {
      kind: "status",
      body: "This block is a AGENTS.md §3b-cond conditional theorem:\n\n- **Class axiomatisation.** The Lean\n  `class CanonicalMarkovWeightsH3` ([`qbeta-per-block-chi-closed-forms.lean`](qbeta-per-block-chi-closed-forms.lean))\n  is the single sorry point. A concrete instance would need to encode\n  the canonical Wenzl construction's $\\sqrt q$-bearing weights and\n  verify the normalisation axiom.\n- **Explicit hypothesis on Lean side.** The Lean theorem\n  `delta_tau_M_canonical_has_q2_minus_1_factor` carries\n  `[CanonicalMarkovWeightsH3]` as an explicit `[Instance]` hypothesis.\n- **Explicit conditional banner on narrative side.** The opening\n  \"Proposition (conditional on ...)\" above.\n- **`uses[]` includes the conjectural upstream.** The block uses\n  `prop:qbeta-per-block-chi-closed-forms`, whose Lean file hosts\n  the class declaration.\n\nOnce a concrete instance lands (closing the canonical weights gap),\nthis proposition becomes unconditional — fully verified by Lean.",
    },
    {
      kind: "note",
      date: "2026-08-08",
      body: "Cross-session tracking for this cluster — the open $f$-map keystone on the bridge to the $c_k$ precision ladder, and the status of the `CanonicalMarkovWeightsH3` instance — lives in `docs/coordination/1ppq-qbeta.md`. That ledger is a branch-local working note and is no longer cited from the published prose of this block, its proof, `qbeta-canonical-markov-weights-explicit-instance`, or `qbeta-delta-tau-surrogate-taylor-coefficients`.",
    },
  ],
});
