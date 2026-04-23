import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:torus-knot-seifert-bound",
  title: "Seifert-genus bound for torus knots in the commutative limit",
  tags: ["torus-knot", "seifert-genus", "commutative-limit", "embedding"],
  uses: [
    "conj:genus-2-ansatz",
    "thm:hyperelliptic-z5-classification",
    "def:hyperelliptic-quintic",
  ],
});
