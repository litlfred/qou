import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:gravity-spectral-prefactor",
  title:
    "Newton's $G$ as the universal-residue prefactor of the unified mass formula",
  lean: {
    ref: "qou:QOU.Observations.gravity_spectral_prefactor",
    validation: "not_checked",
  },
  uses: [
    "prop:plancherel-term-7-formulation",
    "prop:unified-curvature-rank-mass-formula",
    "prop:confinement-categorical",
    "rem:gr-substrate-geometry",
  ],
  tags: [
    "gravity",
    "newton-constant",
    "universal-residue",
    "plancherel",
    "macroscopic-stratum",
    "planck-units",
  ],
});
