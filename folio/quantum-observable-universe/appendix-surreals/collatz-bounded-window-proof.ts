import { proof } from "../../schema/builders";

export default proof({
  label: "prf:collatz-bounded-window",
  title: "Proof that a $q$-Collatz orbit with bounded support converges",
  uses: ["prop:collatz-bounded-window", "prop:collatz-syracuse-lift", "prop:collatz-no-cycles"],
});
