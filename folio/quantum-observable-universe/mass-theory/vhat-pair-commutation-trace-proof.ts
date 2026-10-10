import { proof } from "../../schema/builders";

export default proof({
  label: "prf:vhat-pair-commutation-trace",
  title: "Proof of vhat pair commutation trace",
  uses: ["lem:vhat-pair-commutation-trace"],
});
