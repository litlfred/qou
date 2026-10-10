import { proof } from "../../schema/builders";

export default proof({
  label: "prf:vacuum-state",
  title: "Proof of Existence and Uniqueness of the Vacuum State",
  uses: ["prop:vacuum-state", "def:frobenius-pairing"],
});
