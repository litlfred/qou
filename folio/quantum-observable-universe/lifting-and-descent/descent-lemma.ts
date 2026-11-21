import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:descent",
  examples: ["ex:descent-lemma-su2"],
  lean: { ref: "qou:QOU.DescentLemma", validation: "not_checked" },
  title: "Descent preserves the quantum observable universe",
  tags: ["descent", "frobenius-hopf", "star-homomorphism"],
  uses: ["def:recursive-brane-tower"],
  proofs: ["prf:descent"],
  defines: ["descent"],
});
