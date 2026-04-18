import { proof } from "../../schema/builders";

export default proof({
  label: "prf:q-casimir-unique",
  title: "Proof of uniqueness of the $q$-Casimir element",
  uses: ["prop:q-casimir-unique"],
});
