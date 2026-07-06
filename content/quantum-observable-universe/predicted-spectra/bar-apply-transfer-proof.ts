import { proof } from "../../schema/builders";

export default proof({
  label: "prf:bar-apply-transfer",
  title: "Proof of bar apply transfer",
  uses: ["prop:bar-apply-transfer"],
});
