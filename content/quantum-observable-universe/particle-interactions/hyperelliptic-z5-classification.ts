import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:hyperelliptic-z5-classification",
  proofs: ["prf:hyperelliptic-z5-classification"],
  lean: { ref: "qou:QOU.HyperellipticQuintic.minimal_z5_classification", validation: "not_checked" },
  title: "Minimal-genus hyperelliptic curves with faithful $\\mathbb{Z}_5$-symmetry",
  tags: ["riemann-hurwitz", "hyperelliptic", "z5", "classification", "minimal-genus"],
  uses: [
    "def:hyperelliptic-quintic",
  ],
  cites: ["bolza1887"],
});
