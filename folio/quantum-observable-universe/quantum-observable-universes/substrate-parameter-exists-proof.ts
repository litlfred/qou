import { proof } from "../../schema/builders";

export default proof({
  label: "prf:aether-parameter-exists",
  renamedFrom: ["prf:substrate-parameter-exists"],
  title: "Proof of existence of the aether parameter",
  uses: [
    "thm:aether-parameter-exists",
    "prop:braiding-eigenvalue-extraction",
  ],
});
