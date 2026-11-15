import { proof } from "../../schema/builders";

export default proof({
  label: "prf:wedderburn-mass-formula",
  title: "Proof of wedderburn mass formula",
  uses: ["thm:wedderburn-mass-formula"],
  authorNotes: [
    {
      kind: "caveat",
      body: "The certifying witness previously cited for the nuclide-table cross-check (atom-mass-complete-wedderburn.witness.json) is absent from computations/; its regeneration is an open follow-up.",
    },
  ],
});
