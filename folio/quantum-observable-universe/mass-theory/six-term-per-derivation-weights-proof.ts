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
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The `term4_frobenius_codim` evaluation gives the same value for bound and free configurations" },
  ],
});
