import { remark } from "../../schema/builders";

export default remark({
  interprets: "cor:spectral-decomposition-qvalue",
  label: "rem:spectral-decomposition-qvalue-geometric",
  title: "Geometric interpretation and error structure of the $Q$-value decomposition",
  uses: ["cor:spectral-decomposition-qvalue"],
  computation: {
    engine: "mpmath",
    script: "computations/spectral_decomposition_qvalue_d.py",
    witness: "computations/spectral-decomposition-qvalue-d.witness.json",
    status: "verified",
  },
});
