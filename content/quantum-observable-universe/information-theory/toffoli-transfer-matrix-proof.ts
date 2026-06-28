import { proof } from "../../schema/builders";

export default proof({
  label: "prf:toffoli-transfer-matrix",
  title: "Proof of toffoli transfer matrix",
  uses: ["prop:toffoli-transfer-matrix"],
});
