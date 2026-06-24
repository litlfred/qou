import { proof } from "../../schema/builders";

export default proof({
  label: "prf:collatz-no-cycles",
  title: "Proof of prop:collatz-no-cycles",
  uses: ["prop:collatz-no-cycles"],
});
