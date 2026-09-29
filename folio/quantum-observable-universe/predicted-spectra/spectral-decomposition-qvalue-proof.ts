import { proof } from "../../schema/builders";

export default proof({
  label: "prf:spectral-decomposition-qvalue",
  title: "Proof of spectral decomposition qvalue",
  uses: ["cor:spectral-decomposition-qvalue"],
});
