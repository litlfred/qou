import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:pn-averaging-uniqueness",
  title: "Canonical p-n interface averaging uniqueness",
  chapter: "mass-theory",
  cites: ["jones1987", "wenzl1988"],
  uses: ["thm:averaging-resonance-rule"],
  proofs: ["prf:pn-averaging-uniqueness"],
  defines: [],
  tags: ["normalization", "frobenius", "no-fitting", "uniqueness"],
  lean: { ref: "qou:QOU.BraidKnot.pn_averaging_unique" },
  authorNotes: [
    {
      kind: "note",
      date: "2026-05-30",
      body: "The closed-form-weight derivation chain was established 2026-05-30.",
    },
  ],
});
