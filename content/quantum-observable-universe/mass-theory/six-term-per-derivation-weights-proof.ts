import { proof } from "../../schema/builders";

export default proof({
  label: "prf:six-term-per-derivation-weights",
  title: "Proof of six term per derivation weights",
  computation: {
    engine: "python",
    script: "computations/chi_convention_audit.py",
    witness: [
      "computations/codata-masses.witness.json"
    ],
    status: "verified",
  },
  uses: ["prop:six-term-per-derivation-weights"],
});
