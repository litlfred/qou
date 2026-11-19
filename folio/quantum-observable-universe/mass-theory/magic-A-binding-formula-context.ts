import { remark } from "../../schema/builders";

export default remark({
  label: "rem:magic-A-binding-formula-context",
  title:
    "Regime necessity, the ρ_F prefactor, and the comparison witness for the doubly-magic binding formula",
  interprets: "prop:magic-A-binding-formula",
  tags: ["binding", "doubly-magic", "catalan", "borromean", "strutinsky"],
  uses: ["prop:magic-A-binding-formula"],
  authorNotes: [
    {
      kind: "note",
      body: "Computational witness: computations/binding-alpha-shift-witness.witness.json.",
    },
  ],
});
