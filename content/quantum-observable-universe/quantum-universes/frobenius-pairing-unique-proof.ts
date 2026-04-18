import { proof } from "../../schema/builders";

export default proof({
  label: "prf:frobenius-pairing-unique",
  title: "Proof of uniqueness of the Frobenius pairing",
  uses: ["prop:frobenius-pairing-unique"],
});
