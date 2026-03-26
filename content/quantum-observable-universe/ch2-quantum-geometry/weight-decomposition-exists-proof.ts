import { proof } from "../../schema/builders";

export default proof({
  label: "prf:weight-decomposition-exists",
  title: "Proof of existence of the weight decomposition",
  uses: ["thm:weight-decomposition-exists"],
});
