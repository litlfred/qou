import { proposition } from "../../schema/builders";

/**
 * Pole order at q = 0 of the seminormal diagonal entry of a boundary
 * generator: 1 iff the axial distance rho_T(i) = c(i+1) - c(i) is <= -1.
 *
 * Proved (2026-11-21) from Hoefsmit's diagonal entry
 * (q - q^-1)/(1 - q^(-2 rho)) by explicit factorisation over any field:
 * mass-theory/crystal-r-matrix-sub-lemma.lean, using
 * QOU/BraidKnot/SeminormalDiagonalPoleOrder.lean. No crystal hypothesis.
 * Until that date the block was stated conditional on
 * conj:crystal-graph-realization, with the boxed identity carried as a
 * class field.
 *
 * Verified numerically by `crystal_pole_order.py` (column-SYT counts,
 * including T_{2,9} = 9 and T_{3,5} = 10).
 */
export default proposition({
  label: "prop:crystal-r-matrix-sub-lemma",
  title:
    "Crystal R-matrix Sub-lemma 2.1: pole order of the seminormal diagonal entry",
  uses: [
    // conj:crystal-graph-realization removed (qou-tm3c, 2026-11-21): the pole order is proved from Hoefsmit's diagonal entry; no crystal input is used.
    "prop:alpha-shift-torus-knot",
  ],
  cites: [
    "mathas1999",
    "hoefsmit1974",
    "wenzl1988",
    "brundankleshchev2009",
    "kashiwara1991",
  ],
  lean: {
    ref: "qou:QOU.BraidKnot.CrystalRMatrix.seminormalDiag_of_le_neg_one",
  },
  computation: {
    engine: "python",
    script: "computations/crystal_pole_order.py",
    witness: [
      "computations/crystal-pole-order.witness.json",
    ],
    status: "verified",
    requires: [],
  },
  tags: [
    "crystal-r-matrix",
    "sub-lemma-2-1",
    "operator-valued",
    "pole-order",
    "axial-distance",
    "hecke-branching",
  ],
});
