import { proof } from "../../schema/builders";

export default proof({
  label: "prf:substrate-parameter-unique",
  title: "Proof of uniqueness of the substrate parameter",
  uses: ["thm:substrate-parameter-unique"],
});
