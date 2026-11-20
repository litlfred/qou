import { corollary } from "../../schema/builders";

export default corollary({
  label: "cor:jet-prolongation-C",
  lean: { ref: "qou:QOU.Torsion.jet_prolongation_C",
    validation: "not_checked",
  },
  title: "Archimedean realisation of jet prolongation",
  tags: ["archimedean", "jet-bundle"],
  uses: ["prop:jet-prolongation", "ex:c-quantum-observable-universe"],
  proofs: ["prf:jet-prolongation-C"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The formal backing `QOU.Torsion.jet_prolongation_C` returns that condition under a readable name — the Mathlib accessor idiom — and derives nothing." },
  ],
});
