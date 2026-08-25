import { corollary } from "../../schema/builders";

export default corollary({
  label: "cor:interface-never-realises-isospin-weight",
  title:
    "No admissible interface element realises either isospin weight: the two mechanisms compute on disjoint sets",
  lean: {
    ref: "qou:QOU.QBeta.GramSignature.interface_never_equals_isospin_weight",
    validation: "not_checked",
  },
  uses: ["prop:interface-band-between-isospin-weights"],
  tags: ["impossibility", "isospin", "interface", "convention-d"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-09",
      body:
        "The two component conditionals GramSignature.mu_triplet_above_ceiling and " +
        "mu_singlet_below_floor are deliberately left unreferenced by any block. They are the " +
        "two halves of the band statement and carry no exposition of their own; hosting them " +
        "on a prf: sibling would add a proof block whose whole content is 'divide by a positive " +
        "denominator'. Recorded here so their absence from the content graph reads as a " +
        "decision rather than an omission.",
    },
  ],
});
