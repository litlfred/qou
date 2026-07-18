import { proof } from "../../schema/builders";

export default proof({
  label: "prf:skein-finiteness-bound",
  title: "Proof of the Skein finiteness bound",
  uses: ["prop:skein-finiteness-bound", "prop:skein-polynomial-transfer-matrix"],
});
