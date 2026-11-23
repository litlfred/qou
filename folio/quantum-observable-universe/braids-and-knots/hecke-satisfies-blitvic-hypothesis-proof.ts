import { proof } from "../../schema/builders";

export default proof({
  label: "prf:hecke-satisfies-blitvic-hypothesis",
  title: "Proof: the third centred moment of a Hecke generator",
  uses: [
    "prop:hecke-satisfies-blitvic-hypothesis",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([centred Hecke variance positivity](#prop:centered-hecke-variance-positive))" },
  ],
});
