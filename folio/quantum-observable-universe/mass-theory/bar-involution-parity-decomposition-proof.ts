import { proof } from "../../schema/builders";

export default proof({
  label: "prf:bar-involution-parity-decomposition",
  title: "Proof of the even/odd decomposition",
  uses: ["lem:bar-involution-parity-decomposition", "def:bar-involution"],
});
