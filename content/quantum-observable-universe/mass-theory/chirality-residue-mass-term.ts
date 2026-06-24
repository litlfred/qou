import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:chirality-residue-mass-term",
  proofs: ["prf:chirality-residue-mass-term"],
  title: "Chirality / non-chirality split: $\\mathfrak{m} = \\mathfrak{m}^{\\mathrm{chir}} + \\mathfrak{m}^{\\neg\\mathrm{chir}}$ refining the unified mass formula",
  lean: {
    ref: "qou:QOU.WedderburnMass.chirality_residue_mass_term",
    validation: "not_checked",
  },
  uses: [
    "rem:confinement-curvature-rank",
    "prop:mass-tower-coefficient-stratification",
  ],
});
