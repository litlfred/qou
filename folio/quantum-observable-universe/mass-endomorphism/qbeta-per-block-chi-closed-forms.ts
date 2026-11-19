import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:qbeta-per-block-chi-closed-forms",
  title:
    "Per-block character closed forms for $\\chi_\\lambda(\\Delta_{T_\\beta})(q)$ over $H_3(q)$, antipode pairing, and vanishing at $q = 1$",
  uses: [
    "prop:markov-trace-axiomatic-closed-form",
  ],
  cites: ["hoefsmit1974"],
  tags: [
    "qbeta",
    "per-block",
    "pre-archimedean",
    "wedderburn",
    "antipode",
    "closed-form",
  ],
  lean: {
    ref: "qou:QOU.BraidKnot.chi_block_antipode_pairing",
  },
  authorNotes: [
    { kind: "note", body: "Archimedean specialisation over R (§7c)." },
  ],
});
