import { proof } from "../../schema/builders";

export default proof({
  label: "prf:bounded-width-trace-cost",
  title: "Proof that a fixed-width trace costs linear time",
  uses: ["prop:bounded-width-trace-cost"],
});
