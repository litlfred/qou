import { proposition } from "../../schema/builders";

/**
 * The Möbius cumulants of a subset function on the nucleons of an atomic
 * braid: reconstruction, the size-only (c_k) recursion for exchangeable
 * systems, and the vanishing of mixed cumulants across an additive split.
 *
 * Pure algebra over any commutative ring; the three facts are proved in
 * `lean/QOU/Mass/SubsetCumulantRecursion.lean` (sorry-free). What makes the
 * bond model an instance — exchangeability of L_S and its n-independence —
 * is established numerically at 200 bits, not formalised, and the block says
 * so.
 */
export default proposition({
  label: "prop:subset-cumulant-recursion",
  title:
    "Subset cumulants of the bond model: reconstruction, the $c_k$-only recursion, and vanishing across a split",
  lean: {
    ref: "qou:QOU.Mass.SubsetCumulantRecursion.cum_eq_sizeCum",
    sorryFree: true,
    validation: "not_checked",
  },
  uses: [
    "def:atomic-braid",
    "def:canonical-braid-interface-composition",
  ],
  cites: [],
  tags: [
    "mass-theory",
    "binding",
    "cumulants",
    "mobius-inversion",
    "many-body",
    "lean-formalised",
    "draft",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): are proved as `sum_powerset_cum`, `cum_eq_sizeCum` and `cum_eq_zero_of_additive_split` in `QOU.Mass.SubsetCumulantRecursion`. ... they are **not** formalised: the corpus's `MarkovTrace.lean` carries cyclicity and single-generator conjugation, not the split-link tensor rule" },
  ],
});
