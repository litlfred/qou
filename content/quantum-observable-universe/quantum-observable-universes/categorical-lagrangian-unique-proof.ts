import { proof } from "../../schema/builders";

export default proof({
  label: "prf:categorical-lagrangian-unique",
  title: "Proof of uniqueness of the categorical Lagrangian",
  uses: ["prop:categorical-lagrangian-unique"],
});
