import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:plancherel-term-7-formulation",
  proofs: ["prf:plancherel-term-7-formulation"],
  title:
    "Universal residue at curvature-rank $k \\geq 4$ (q-deformed Wedderburn-weighted log functional)",
  lean: {
    ref: "qou:QOU.WedderburnMass.plancherel_term_7",
    validation: "not_checked",
  },
  uses: [
    "prop:spectral-sequence-collapse",
  ],
});
