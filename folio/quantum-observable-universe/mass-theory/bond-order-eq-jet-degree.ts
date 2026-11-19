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
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
  ],
});
