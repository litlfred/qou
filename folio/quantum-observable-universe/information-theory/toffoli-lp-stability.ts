import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    { kind: "note", body: "Lean theorems in `QOU.Information.*`: `toffoliDiagonal_pos`, `toffoliP66_pos`, `toffoliFlip_eq_zero_iff`, `toffoliFlip_neg_of_one_lt`, `toffoliFlip_pos_of_lt_one`, `toffoli_antisymmetry_defect`, `toffoli_not_antisymmetric`, `wStd_pos`, `toffoliDiagonal_mul_wStd_pos`, `toffoliFlip_mul_coneCoord_nonpos`, `cone_sign_change_unexplained_by_factors`, `cone_eq_quadratic_in_amplitudes`, `coneCoordRow5_pos_iff`, `cone_eq_markov_hecke_polynomial`, `markov_hecke_relation` (all using only `propext`, `Classical.choice`, `Quot.sound`), together with `QOU.Machinery.MarkovTraceH4.TRM` and numerical Gram cross-check against `gram_matrix_mp`." },
  ],
  label: "prop:toffoli-lp-stability",
  title:
    "LP-dual stability of the $q$-Toffoli braid and the golden-ratio threshold",
  tags: [
    "toffoli",
    "lp-duality",
    "stability",
    "gram-matrix",
    "golden-ratio",
    "substrate-q",
    "hecke-algebra",
    "q-AND",
  ],
  lean: { ref: "qou:QOU.Information.toffoli_lp_stable",
    validation: "not_checked",
  },
  uses: [
    "prop:toffoli-transfer-matrix",
    "prop:lp-dual-stability",
  ],
  computation: {
    engine: "python",
    script: "computations/toffoli-lp-stability.py",
    witness: "computations/toffoli-lp-stability.witness.json",
    status: "verified",
  },
});
