import { proof } from "../../schema/builders";

export default proof({
  label: "prf:frobenius-pairing-exists",
  title: "Proof of existence of the Frobenius pairing",
  uses: ["prop:frobenius-pairing-exists"],
});
