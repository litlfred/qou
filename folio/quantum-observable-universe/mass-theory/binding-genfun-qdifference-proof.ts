import { proof } from "../../schema/builders";

export default proof({
  label: "prf:binding-genfun-qdifference",
  title: "Proof of the q-difference recurrence of the binding generating function",
  uses: [
    "prop:binding-genfun-qdifference",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): $\\widehat{G}=\\tau G$ — the Dirac-type equation. The Lean witness\n[`QOU.Mass.binding_qdifference_recurrence`](#prop:binding-genfun-qdifference)\npackages the depth-$d$ recurrence, with position-dependent coefficients, as\na structure and extracts the term identity; the existence\n\n(carried as the structure hypothesis)." },
  ],
});
