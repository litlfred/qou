import { proof } from "../../schema/builders";

export default proof({
  label: "prf:brane-boundary",
  title: "Proof of Structure of the defining boundary",
  uses: ["prop:brane-boundary", "def:frobenius-pairing"],
});
