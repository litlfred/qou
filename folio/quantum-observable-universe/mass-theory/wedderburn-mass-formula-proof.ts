import { proof } from "../../schema/builders";

export default proof({
  label: "prf:wedderburn-mass-formula",
  title: "Proof of wedderburn mass formula",
  uses: ["thm:wedderburn-mass-formula"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): is the degree-two baryon weight\n([degree-2 weight](#prop:degree-two-baryon-weight))" },
    {
      kind: "caveat",
      body: "The certifying witness previously cited for the nuclide-table cross-check (atom-mass-complete-wedderburn.witness.json) is absent from computations/; its regeneration is an open follow-up.",
    },
  ],
});
