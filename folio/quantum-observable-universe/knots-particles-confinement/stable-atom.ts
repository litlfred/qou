import { definition } from "../../schema/builders";

export default definition({
  label: "def:stable-atom",
  title: "Stable atom (Frobenius positivity of the normal form)",
  lean: { ref: "qou:QOU.BraidKnot.StableAtom",
    validation: "not_checked",
  },
  uses: [
    "def:atom-knot",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict):  ([mass-coefficient-shadow-price](#prop:mass-coefficient-shadow-price))" },
  ],
  cites: [],
  tags: [
    "stability",
    "ilp",
    "lp-dual",
    "atom",
    "frobenius-positivity",
  ],
});
