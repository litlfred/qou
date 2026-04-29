import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:phi-q-categorical-truncation",
  title: "Brane-tower truncation depth = NF support depth (centre stratification)",
  lean: { ref: "qou:QOU.WedderburnMass.phi_q_categorical_truncation",
    validation: "not_checked",
  },
  uses: [
    "prop:spectral-sequence-collapse",
    "prop:curvature-rank-gb-stratification",
    "prop:categorical-mass-markov",
    "cor:quantum-dilogarithm",
    "def:hecke-normal-form",
    "def:confinement-level",
  ],
  proofs: ["prf:phi-q-categorical-truncation"],
  tags: [
    "brane-tower",
    "spectral-sequence",
    "yekutieli",
    "regularization",
    "centre-stratification",
  ],
});
