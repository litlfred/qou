import { proof } from "../../schema/builders";

export default proof({
  label: "prf:aether-parameter-unique",
  renamedFrom: ["prf:substrate-parameter-unique"],
  title: "Proof of uniqueness of the aether parameter",
  uses: ["thm:aether-parameter-unique"],
});
