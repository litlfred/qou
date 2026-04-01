import { proof } from "../../schema/builders";

export default proof({
  label: "prf:substrate-parameter-exists",
  title: "Proof of existence of the substrate parameter",
  uses: [
    "thm:substrate-parameter-exists",
    "prop:braiding-eigenvalue-extraction",
  ],
});
