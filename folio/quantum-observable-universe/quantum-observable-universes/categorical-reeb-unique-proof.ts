import { proof } from "../../schema/builders";

export default proof({
  label: "prf:categorical-reeb-unique",
  title: "Proof of uniqueness of the categorical Reeb derivation",
  uses: ["prop:categorical-reeb-unique"],
});
