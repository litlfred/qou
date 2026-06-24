import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:x5-bring-weight-identification",
  proofs: ["prf:x5-bring-weight-identification"],
  lean: { ref: "qou:QOU.HyperellipticQuintic.bring_weight_match", validation: "not_checked" },
  title: "$\\mathbb{Z}_5$-weight identification: $x$ on $\\mathcal{X}_5$ matches $w_1$ on Bring",
  tags: ["lagrange-resolvent", "z5", "weight-grading", "bring", "hyperelliptic"],
  uses: ["prop:x5-z5-automorphism"],
});
