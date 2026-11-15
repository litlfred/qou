import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:s-polynomial-decomposition",
  title: "$S$-polynomial decomposition of cancelling sums",
  lean: { ref: "ugb:UGB.UnitalGroebner.s_polynomial_decomposition", validation: "not_checked" },
  tags: ["groebner-basis", "s-polynomial"],
  uses: ["def:admissible-system", "def:groebner-basis"],
  proofs: ["prf:s-polynomial-decomposition"],
});
