import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:genus-2-ansatz",
  title: "Genus-2 ansatz for the commutative limit",
  tags: ["commutative-limit", "genus-2", "ansatz", "hyperelliptic"],
  uses: [
    "def:commutative-qou",
    "def:brings-surface",
  ],
});
