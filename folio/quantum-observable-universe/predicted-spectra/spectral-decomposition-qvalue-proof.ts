import { proof } from "../../schema/builders";

export default proof({
  label: "prf:spectral-decomposition-qvalue",
  title: "Proof of spectral decomposition qvalue",
  uses: ["cor:spectral-decomposition-qvalue"],
  computation: {
    engine: "mpmath",
    script: "computations/spectral_decomposition_qvalue_d.py",
    witness: "computations/spectral-decomposition-qvalue-d.witness.json",
    status: "verified",
  },
});
