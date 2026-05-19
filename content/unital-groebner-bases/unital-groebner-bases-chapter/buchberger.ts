import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:buchberger",
  title: "Buchberger's theorem over commutative rings",
  lean: { ref: "ugb:UGB.UnitalGroebner.buchberger", validation: "not_checked" },
  tags: ["groebner-basis", "buchberger", "s-polynomial"],
  uses: [
    "def:admissible-system",
    "def:groebner-basis",
    "prop:s-polynomial-decomposition",
  ],
  proofs: ["prf:buchberger"],
});
