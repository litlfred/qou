import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:phi-q-categorical-truncation",
  title: "Brane-tower truncation depth = NF support depth (centre stratification)",
  lean: { ref: "qou:QOU.WedderburnMass.phi_q_categorical_truncation",
    validation: "not_checked",
  },
  uses: ["cor:habiro-expansion-atomic"],
  proofs: ["prf:phi-q-categorical-truncation"],
  tags: [
    "brane-tower",
    "spectral-sequence",
    "yekutieli",
    "regularization",
    "centre-stratification",
  ],
});
