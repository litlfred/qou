import { remark } from "../../schema/builders";

export default remark({
  label: "rem:six-term-per-derivation-weights-argument",
  interprets: "conj:six-term-per-derivation-weights",
  title: "Argument for the six-term per-derivation weights (not a proof)",
  computation: {
    engine: "python",
    script: "computations/chi_convention_audit.py",
    witness: [
      "computations/codata-masses.witness.json"
    ],
    status: "verified",
  },
  uses: ["conj:six-term-per-derivation-weights"],
});
