import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:bond-order-eq-jet-degree",
  lean: {
    ref: "qou:QOU.Mass.bodyorder_eq_jet_total",
    validation: "validated",
  },
  title: "Body order equals jet degree: the n-nucleon cluster sits at jet vertical degree n",
  uses: [
    "prop:gb-spectral-sequence",
    "prop:jet-prefix-gb-filtration",
  ],
  proofs: ["prf:bond-order-eq-jet-degree"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): assembled by\n`atom_braid_word_3A` — and equip" },
  ],
});
