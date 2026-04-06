import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:buchberger",
  title: "Buchberger's theorem over commutative rings",
  tags: ["groebner-basis", "buchberger", "s-polynomial"],
  uses: [
    "def:admissible-system",
    "def:groebner-basis",
    "prop:s-polynomial-decomposition",
  ],
  proofs: ["prf:buchberger"],
});
