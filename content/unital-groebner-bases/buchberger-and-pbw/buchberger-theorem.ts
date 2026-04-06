import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:ugb-buchberger",
  title: "Buchberger's theorem over a commutative ring",
  tags: ["groebner-basis", "buchberger", "criterion"],
  uses: [
    "def:unital-groebner-basis",
    "def:admissible-system",
    "prop:ugb-s-poly-decomposition",
  ],
});
