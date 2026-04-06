import { proof } from "../../schema/builders";

export default proof({
  label: "prf:buchberger",
  uses: [
    "thm:buchberger",
    "prop:s-polynomial-decomposition",
  ],
});
