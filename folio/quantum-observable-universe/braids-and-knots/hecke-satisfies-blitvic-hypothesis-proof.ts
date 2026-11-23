import { proof } from "../../schema/builders";

export default proof({
  label: "prf:hecke-satisfies-blitvic-hypothesis",
  title: "Proof: Hecke generators satisfy Blitvić's pair-partition hypothesis",
  uses: [
    "prop:hecke-satisfies-blitvic-hypothesis",
    "prop:trace-locality-meets-gs-non-locality",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([centred Hecke variance positivity](#prop:centered-hecke-variance-positive))" },
  ],
});
