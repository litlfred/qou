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
    {
      kind: "note",
      body:
        "Mathlib gap: formalising birthday grading and the Hoefsmit-as-{L|R} embedding rigorously in Lean requires extending Mathlib's SetTheory.Game.Basic / Surreal hierarchy up to a real-closed-field witness.",
    },
  ],
});
