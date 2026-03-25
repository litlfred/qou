import { proof } from "../../schema/builders";

export default proof({
  label: "prf:unital-groebner-decomposition",
  uses: [
    "thm:unital-groebner-decomposition",
    "lem:generator-choice",
    "def:division-algorithm",
  ],
});
