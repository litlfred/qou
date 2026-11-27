import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:knot-operator-energy-exists",
  title: "Existence of the knot operator energy",
  lean: { ref: "qou:QOU.BraidsAndKnots.BraidKnot.KnotOperatorEnergy.exists",
    validation: "not_checked",
  },
  uses: ["def:knot-operator-energy"],
  tags: ["existence", "knot-operator", "shadow-price", "lp-dual"],
  authorNotes: [
    { kind: "note", date: "2026-11-24", body: "Relocated from the block prose by the reading-order drain (qou-d4kh): by [mass-coefficient-shadow-price](#prop:mass-coefficient-shadow-price)" },
  ],
});
