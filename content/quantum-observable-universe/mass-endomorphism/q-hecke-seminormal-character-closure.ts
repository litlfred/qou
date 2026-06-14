import { proposition } from "../../schema/builders";

/**
 * The q-Hecke character gap is closed: the partition-sum form of
 * the Markov trace
 *
 *     tr_M(β) = Σ_{λ ⊢ 3A} y_λ(q) · χ^λ_q(β)
 *
 * agrees with the canonical Markov-axiom reducer to numerical
 * precision (1e-13 for proton/neutron, 1e-10 for deuteron at
 * float64; 1.4e-16 at 50-dps mpmath via PR #564's
 * `rho_k_h3a_refinement.py`).
 *
 * The closure has two ingredients, both already in the repo:
 *   1. y_λ(q): Wenzl's Schur principal specialization
 *      (`markov_weights_symbolic.solve_y_lambda` →
 *       `wedderburn_jones_markov.y_lambda_at`,
 *       numerical-q-from-start).
 *   2. χ^λ_q(β): trace of the Hoefsmit seminormal representation
 *      ρ_λ(β) at q (`hecke_characters.build_seminormal_matrices` +
 *      `mass_at_3A_proper.chi_lambda_of_word`).
 *
 * The composition lives in
 * `wedderburn_jones_markov.global_wedderburn_sum_q_hecke_seminormal`.
 *
 * Verified by `tr_m_q_hecke_seminormal.py` against
 * `markov_trace_recursive` (canonical) for proton, neutron, deuteron.
 *
 * No new sorrys: the proposition is an equality between three
 * already-implemented numerical paths.  This block records that
 * agreement so downstream consumers know the partition-sum form is
 * usable for ρ_K binding-fraction analysis (#564 P3') without
 * re-deriving.
 */
export default proposition({
  label: "prop:q-hecke-seminormal-character-closure",
  title:
    "Partition-sum form of $\\mathrm{tr}_M$ via Wenzl $y_\\lambda$ and " +
    "Hoefsmit $\\chi^\\lambda_q$ agrees with the canonical Markov-axiom reducer",
  lean: {
    ref: "qou:QOU.BraidKnot.QHeckeSeminormalCharacterClosure.character_closure_holds",
    validation: "not_checked",
  },
  uses: [],
  cites: [
    "wenzl1988",
    "hoefsmit1974",
    "mathas1999",
    "jones1987",
    "jing-liu-2021",
  ],
  computation: {
    engine: "numpy",
    script: "folio-assistant/computations/tr_m_q_hecke_seminormal.py",
    witness: [
      "folio-assistant/computations/tr-m-q-hecke-seminormal.witness.json",
    ],
    status: "verified",
    requires: ["numpy", "sympy"],
  },
  tags: [
    "q-hecke-character",
    "seminormal",
    "hoefsmit",
    "wenzl",
    "jones-markov",
    "partition-sum",
    "cross-check",
    "infrastructure",
  ],
  authorNotes: [
    {
      kind: "status",
      body: "The proposition is a numerical-equality claim between three\nimplemented paths, all of which agree to their precision floors.\nMathematical proof: the partition-sum form is the spectral\nexpansion of $\\mathrm{tr}_M$ in the Wedderburn–Artin basis. The\ncanonical Hecke character $\\chi^\\lambda_q$ is the diagonal of\n$\\rho_\\lambda^q$ in the seminormal basis (Hoefsmit 1974, Mathas\n1999 §3.4); $y_\\lambda(q)$ is the unique Jones-Markov weight given\nthe Markov axioms (Wenzl 1988). Combining: the partition-sum form\nidentically equals the recursive Markov ascent. Numerical\nverification confirms.",
    },
  ],
});
