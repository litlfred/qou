import { proof } from "../../schema/builders";

export default proof({
  label: "prf:categorical-action-exists",
  title: "Proof of existence of the categorical action",
  uses: ["prop:categorical-action-exists"],
});
