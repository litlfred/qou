import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:genus-2-ansatz",
  title: "Commutative-limit substrate: hyperelliptic $\\mathbb{Z}_5$-residual",
  tags: ["commutative-limit", "ansatz", "hyperelliptic", "z5-residual"],
  uses: [
    "def:commutative-qou",
    "def:brings-surface",
    "thm:hyperelliptic-z5-classification",
  ],
});
