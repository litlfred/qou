import { prose } from "../../schema/builders";

export default prose({
  label: "sec:surreal-appendix-conclusion",
  title: "Open questions and outlook",
  tags: [
    "surreal-numbers",
    "appendix",
    "open-problem",
    "outlook",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): 1. **Mathlib gap.** There is no mature surreal-analysis library in mathlib. Formalising the birthday-grading definition and the Hoefsmit-as-$\\{L\\mid R\\}$ proposition rigorously requires completing the surreal-numbers development in mathlib (the `SetTheory.Game.Basic` hierarchy) up to a real-closed-field witness." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The conjecture is that the flexibility is genuine when the ground ring is not a field ([infinitesimal Frobenius](#conj:infinitesimal-frobenius)); there is neither a proof nor a counterexample." },
  ],
});
