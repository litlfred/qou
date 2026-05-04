import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:quantum-dilogarithm-stratified",
  title: "Quantum dilogarithm stratifies by partition GB-depth",
  lean: {
    ref: "qou:QOU.WedderburnMass.phi_q_frobenius_truncation",
    validation: "not_checked",
  },
  uses: [
    "cor:quantum-dilogarithm",
    "prop:curvature-rank-gb-stratification",
    "prop:spectral-sequence-collapse",
    "def:hecke-normal-form",
    "def:q-pochhammer-partial-product",
  ],
  proofs: ["prf:quantum-dilogarithm-stratified"],
  tags: [
    "quantum-dilogarithm",
    "brane-tower",
    "centre-stratification",
    "spectral-sequence",
  ],
});
