import { proof } from "../../schema/builders";

export default proof({
  label: "prf:dq-squared",
  title: "Proof of d_q^2 does not vanish",
  uses: ["prop:dq-squared"],
});
