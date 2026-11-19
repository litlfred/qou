import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:bohr-radius-categorical",
  label: "rem:bohr-radius-round8-findings",
  title: "Round-8 partial Hecke-algebraic progress on the Bohr radius",
  uses: ["conj:bohr-radius-categorical"],
  computation: {
    engine: "python",
    script: "computations/h2-molecular-binding.py",
    witness: [
      "computations/h2-molecular-binding.witness.json",
      "computations/qbeta/qbeta-d-frame-bar-even-normalisation-deadend.witness.json",
    ],
    status: "verified",
  },
});
