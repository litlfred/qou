import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:ugb-buchberger",
  proofs: ["prf:ugb-buchberger"],
  title: "Buchberger's theorem over a commutative ring",
  lean: { ref: "ugb:UGB.BuchbergerPBW.buchberger_theorem", validation: "not_checked" },
  tags: ["groebner-basis", "buchberger", "criterion"],
  uses: [
    "def:unital-groebner-basis",
    "def:admissible-system",
    "prop:ugb-s-poly-decomposition",
  ],
});
