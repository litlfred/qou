import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:unital-groebner-decomposition",
  title: "Free module decomposition via unital Gröbner--Shirshov bases",
  tags: ["groebner-basis", "free-module", "decomposition"],
  uses: [
    "def:admissible-system",
    "def:groebner-basis",
    "def:remainder-module",
  ],
  proofs: ["prf:unital-groebner-decomposition"],
});
