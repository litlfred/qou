import { remark } from "../../schema/builders";

/**
 * Consolidated knot–particle–force dictionary with flavor layer.
 *
 * This remark synthesizes the eightfold-way classification developed
 * in this chapter with the knot-particle dictionary from Ch 9.
 * It adds the flavor quantum numbers (I₃, Y) to the existing
 * dictionary entries and notes which entries have derived vs open
 * charge assignments.
 */
export default remark({
  label: "rem:dictionary-flavor-layer",
  title: "The knot--particle--force dictionary: flavor supplement",
  interprets: "prop:schur-weyl-eightfold",
  lean: {
    ref: "qou:QOU.Eightfold.HyperbolicMesonClaspAndDiquarkSplit.framedMesonClaspDatum_injective",
  },
  uses: [
    "rem:knot-particle-dictionary",
    "prop:a2-from-three-strands",
    "rem:flavor-charge-assignments",
    "prop:meson-octet-decomposition",
    "prop:schur-weyl-eightfold",
    "prop:color-su3-from-g2",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-23",
      body: "Framed meson clasp injectivity (`qou-8fw2`, `qou-3ttt`, `qou-qpj9`, `qou-8fl1`): `QOU/Eightfold/HyperbolicMesonClaspAndDiquarkSplit.lean` proves `Dmeson_K0_generationPair_swapped` (`D̄⁰ ↦ (5,3) ≠ (3,5) ↤ K⁰`), `claspMarkovTrace_separates_Dbar0_K0`, and `framedMesonClaspDatum_injective` across all five dictionary mesons (`pion`, `kaon`, `etaPhi`, `Dmeson`, `K0`).",
    },
  ],
});
