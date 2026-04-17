import { proof } from "../../schema/builders";

export default proof({
  label: "prf:categorical-action-unique",
  title: "Proof of uniqueness of the categorical action",
  uses: ["prop:categorical-action-unique"],
});
