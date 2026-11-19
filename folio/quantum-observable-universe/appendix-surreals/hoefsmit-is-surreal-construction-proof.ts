import { proof } from "../../schema/builders";

export default proof({
  label: "prf:hoefsmit-is-surreal-construction",
  title: "Proof of hoefsmit is surreal construction",
  uses: ["prop:hoefsmit-is-surreal-construction"],
  authorNotes: [
    {
      kind: "note",
      body:
        "Lean formalisation requires a YJM successor relation over Mathlib's Combinatorics.YoungTableau and Gonshor's sign-sequence-to-surreal map over SetTheory.Game.Surreal; the Lean stub currently axiomatises the sign-sequence embedding.",
    },
  ],
});
