import { remark } from "../../schema/builders";

/**
 * Interpretive remark: the recomputed low-isotope mass table after
 * the q-Hecke character gap closure (PR #572).
 *
 * Three production paths to tr_M(K) now agree to machine epsilon
 * across {proton, neutron, deuteron, tritium, helium-3}:
 *
 *   1. Canonical Markov-axiom reducer (markov_trace_recursive @ 50-dps)
 *   2. Hybrid partition-sum (30-dps Wenzl y_λ + float64 χ^λ_q)
 *   3. Symbolic partition-sum (#564 rho_k_h3a_refinement @ 50-dps mpmath)
 *
 * Mass predictions via #564's ρ_K^LO ansatz are anchor-driven:
 * M(p) = m_p, M(n) = m_n by construction, and M(D) = m_p + m_n
 * (zero binding) for the leading-order ρ_K.  The non-zero rel err
 * on D, T, ³He, ⁴He is the actual nuclear binding energy that the
 * framework needs to predict beyond leading order — territory of
 * `rho_k_h3a_refinement.py` (#564 P3') and the per-block
 * binding-fraction Δ_λ closed form.
 */
export default remark({
  label: "rem:recomputed-low-isotope-mass-table",
  title:
    "Recomputed low-isotope mass table after the q-Hecke " +
    "character gap closure (proton, neutron, D, T, ³He)",
  interprets: "prop:q-hecke-seminormal-character-closure",
  uses: [
    "prop:q-hecke-seminormal-character-closure",
    "prop:markov-trace-recursive-reducer",
  ],
  cites: [
    "wenzl1988",
    "hoefsmit1974",
  ],
  computation: {
    engine: "numpy",
    script: "computations/tr_m_q_hecke_seminormal.py",
    witness: [
      "computations/tr-m-q-hecke-seminormal.witness.json",
      "computations/atomic-tr-m-mpfr-50dps.witness.json",
      "computations/rho-k-h3a-lp-dual.witness.json",
      "computations/rho-k-h3a-gg-trajectory.witness.json",
      "computations/binding-k-solver.witness.json",
      "computations/proton-mass-codata-50dps.witness.json",
      "computations/atomic-mass-via-rho-k.witness.json",
      "computations/rho-k-h3a-refinement.witness.json",
      "computations/low-isotope-mass-table.witness.json",
      "computations/e-0-lp-dual-h3.witness.json",
      "computations/qbeta/qbeta-ck-sseries-operator-match.witness.json",
      "computations/qbeta/qbeta-delta-tr-vs-ruled-base.witness.json",
    ],
    status: "verified",
    requires: ["numpy", "sympy"],
  },
  tags: [
    "mass-table",
    "low-isotopes",
    "binding-energy",
    "tr-m",
    "q-hecke-character",
    "machine-epsilon",
    "cross-validation",
    "lp-dual",
    "shadow-price",
    "operator-selection-lp",
  ],
  authorNotes: [
    {
      kind: "note",
      body: "Computational witness: computations/atomic-mass-via-rho-k.witness.json.",
    },
  ],
});
