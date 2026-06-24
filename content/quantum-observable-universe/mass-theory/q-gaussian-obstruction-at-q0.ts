import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-gaussian-obstruction-at-q0",
  proofs: ["prf:q-gaussian-obstruction-at-q0"],
  title:
    "Bożejko–Speicher $q$-Gaussian obstruction at the substrate $q_0 > 1$",
  tags: [
    "q-gaussian",
    "bozejko-speicher",
    "moment-problem",
    "touchard",
    "crossing-number",
    "substrate-q0",
    "obstruction",
  ],
  lean: {
    ref: "qou:QOU.MassTheory.qGaussianObstructionAtQ0",
    validation: "not_checked",
  },
  cites: ["bozejko-speicher1991"],
});
