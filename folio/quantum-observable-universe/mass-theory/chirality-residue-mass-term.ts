import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:chirality-residue-mass-term",
  title: "Chirality / non-chirality split: $\\mathfrak{m} = \\mathfrak{m}^{\\mathrm{chir}} + \\mathfrak{m}^{\\neg\\mathrm{chir}}$ refining the unified mass formula",
  lean: {
    ref: "qou:QOU.WedderburnMass.chirality_residue_mass_term",
    validation: "not_checked",
  },
  // rem:confinement-curvature-rank dropped from uses[] 2026-11-20 (owner choice, bean qou-tm3c):
  // not cited in the statement or proof. A remark carries no premise; the edge only put this block
  // downstream of a conjecture.
  uses: ["prop:mass-tower-coefficient-stratification"],
});
