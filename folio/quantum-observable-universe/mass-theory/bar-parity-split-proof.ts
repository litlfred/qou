import { proof } from "../../schema/builders";

export default proof({
  label: "prf:bar-parity-split",
  title: "Proof of the bar-parity split",
  uses: ["prop:bar-parity-split", "def:bar-involution"],
});
