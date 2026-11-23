import { proof } from "../../schema/builders";

export default proof({
  label: "prf:hoefsmit-is-surreal-construction",
  title: "Proof of hoefsmit is surreal construction",
  uses: ["prop:hoefsmit-is-surreal-construction"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): - formalising the YJM-tableau tree structure (in Mathlib:\n  `Combinatorics.YoungTableau` plus a `successor` relation);\n- formalising Gonshor's sign-sequence-to-surreal map (open in\n  Mathlib's `SetTheory.Game.Surreal` development);\nThe Lean stub axiomatises the embedding pending these prerequisites." },
  ],
});
