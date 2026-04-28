import { proof } from "../../schema/builders";

export default proof({
  label: "prf:q-casimir-exists",
  title: "Proof of existence of the $q$-Casimir element",
  uses: ["prop:q-casimir-exists"],
});
