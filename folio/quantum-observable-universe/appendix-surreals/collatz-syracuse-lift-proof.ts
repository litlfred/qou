import { proof } from "../../schema/builders";

export default proof({
  label: "prf:collatz-syracuse-lift",
  title: "Proof that the $q$-Collatz orbit lifts the Syracuse orbit",
  uses: ["prop:collatz-syracuse-lift", "prop:collatz-no-cycles"],
});
