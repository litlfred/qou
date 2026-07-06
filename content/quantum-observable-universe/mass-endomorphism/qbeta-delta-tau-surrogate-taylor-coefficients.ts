import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:qbeta-delta-tau-surrogate-taylor-coefficients",
  title:
    "Catalogue: Taylor coefficients of $\\Delta\\tau_M^{\\text{surr}}$ at $q = 1$, orders 0..7",
  uses: [
    "prop:qbeta-per-block-chi-closed-forms",
  ],
  cites: ["hoefsmit1974"],
  tags: [
    "qbeta",
    "delta-tau-M",
    "taylor-coefficients",
    "witness-catalogue",
    "pre-archimedean",
  ],
  lean: {
    ref:
      "qou:QOU.BraidKnot.delta_tau_M_surrogate_taylor_witness",
  },
  authorNotes: [
    {
      kind: "note",
      body:
        "Provenance: the order-0 and order-1 coefficients were proved sorry-free in PR #1764 (`delta_tau_M_surrogate_vanish_at_one`, `delta_tau_M_surrogate_hasDerivAt_one`). Kept in metadata (not scholarly prose) per AGENTS.md §4d; the audit trail is preserved without leaking PR refs into the rendered statement.",
    },
  ],
});
