import { proof } from "../../schema/builders";

export default proof({
  label: "prf:categorical-connection-unique",
  title: "Proof of uniqueness of categorical connections up to gauge",
  uses: ["prop:categorical-connection-unique"],
});
