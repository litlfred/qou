import { proof } from "../../schema/builders";

export default proof({
  label: "prf:generation-completeness",
  title: "Proof of generation completeness",
  uses: ["thm:generation-completeness"],
});
