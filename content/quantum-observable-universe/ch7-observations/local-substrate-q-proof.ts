import { proof } from "../../schema/builders";

export default proof({
  label: "prf:local-substrate-q",
  title: "Proof of Local Value of the Substrate Parameter",
  uses: ["prop:local-substrate-q"],
});
