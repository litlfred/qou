import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    { kind: "note", body: "Lean theorems in `QOU.Information.*`: `toffoliDiagonal_pos`, `toffoliP66_pos`, `toffoliFlip_eq_zero_iff`, `toffoliFlip_neg_of_one_lt`, `toffoliFlip_pos_of_lt_one`, `toffoli_antisymmetry_defect`, `toffoli_not_antisymmetric`, `wStd_pos`, `toffoliDiagonal_mul_wStd_pos`, `toffoliFlip_mul_coneCoord_nonpos`, `cone_sign_change_unexplained_by_factors`, `cone_eq_quadratic_in_amplitudes`, `coneCoordRow5_pos_iff`, `cone_eq_markov_hecke_polynomial`, `markov_hecke_relation` (all using only `propext`, `Classical.choice`, `Quot.sound`), together with `QOU.Machinery.MarkovTraceH4.TRM` and numerical Gram cross-check against `gram_matrix_mp`." },
    { kind: "status", date: "2026-08-09", body: "Dual shadow-price figure kappa(G(q_0)) ≈ 3.03 withdrawn (computed under excised convention C with naive length rule tr_M(T_w) = z^{ell(w)} in float64; under convention D the Markov-Gram form is singular on the full 6D NF span pending radical-quotient formulation and regeneration of toffoli-lp-stability.witness.json). Probe verifications: toffoli_nf_coordinates_and_lp_feasibility.py, toffoli_sign_inversion_is_structural.py (7/7), toffoli_amplitude_sign_claims.py (9/9), toffoli_cone_in_entry_subring.py (8/8), toffoli_cone_in_markov_hecke_parameters.py (13/13)." },
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
    witness: [
      "computations/toffoli-lp-stability.witness.json",
      "computations/gram-h3-symbolic-regression.witness.json",
      "computations/qbeta/qbeta-c3-ladder-trace-convention-sensitivity.witness.json",
      "computations/hecke/h3-gram-degeneracy-is-wedderburn-weight-vanishing.witness.json",
    ],
    status: "verified",
  },
});
