import { proof } from "../../schema/builders";

export default proof({
  label: "prf:categorical-reeb-exists",
  title: "Proof of existence of the categorical Reeb derivation",
  uses: ["thm:categorical-reeb-exists"],
});
