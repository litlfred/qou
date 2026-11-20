import { proof } from "../../schema/builders";

export default proof({
  label: "prf:bond-order-eq-jet-degree",
  title: "Proof that body order equals jet degree",
  uses: [
    "lem:bond-order-eq-jet-degree",
    "prop:gb-spectral-sequence",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean witness\n[`QOU.Mass.bodyorder_eq_jet_total`](#lem:bond-order-eq-jet-degree) packages the\ngraded-match (Step 1--2) and exhaustiveness as the structure hypothesis and\nextracts the body-order = jet-graded sum identity." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): atomic braid `atom_braid_word_3A` builds" },
  ],
});
