import { conjecture } from "../../schema/builders";

/**
 * Conjecture: the Hartree-energy scaling
 * $E_h = m_e c_q^2 \alpha_{EM}^2$ used as input in the molecular
 * binding LP/SDP framework should arise from QOU/Hecke structure
 * rather than being an empirical conversion factor.
 *
 * Status after a 13-round investigation (recorded in the .md):
 * coupling-level parity arguments are doomed by the Skein identity
 * (no automorphism of R flips the sign of α_EM — using
 * $[n]_{-q^{-1}} = (-1)^{n+1}[n]_q$, the sign factors cancel and
 * α_EM rescales by a power of q under every obvious involution),
 * the brief's "expand y_cov in α_EM" framing was a category error
 * (y_cov is dimensionless, no α dependence), and the Hopf-link
 * rank-2 → α² mechanism is refuted (round 10).
 *
 * Genuine Hecke wins preserved: additive {h_b, h_d} decomposition
 * of V_i at LP optimum (round 8a); Bohr 1/n² shell spacing from
 * (2k+1)^-2 (8b); α_EM lives in q-dimension layer not Markov layer
 * (round 11); α_EM = h²/[q·(q^9-q^-9)(q^10-q^-10)] explicit (12).
 *
 * Single tractable closure path identified: q-dimension decoration
 * δ_q : NF basis → R, dual to GB filtration / jet expansion.
 *
 * Honest open-problem block: no closure claimed, no numerology,
 * coefficient $c_2$ conjecturally inside
 * $R = \mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$.
 */
export default conjecture({
  label: "conj:e-hartree-categorical-derivation",
  title:
    "Conjectured categorical derivation of $E_h = m_e c_q^2 \\alpha_{EM}^2$ via $J^1$-vanishing in the molecular LP dual",
  lean: {
    ref: "qou:QOU.Archimedean.EHartreeCategoricalDerivation",
    validation: "not_checked",
  },
  uses: [
    "prop:em-coupling-projection",
    "prop:alpha-em-shift-multiplicative-chain",
    "prop:h2-lp-dual-binding",
    "prop:ilp-covalent-bond",
    "prop:lp-dual-stability",
    "prop:spectral-sequence-collapse",
    "cor:commutative-chirality-vanishes",
    "conj:bohr-radius-categorical",
    "prop:force-carrier-bring-uniqueness",
    "prop:phi-q-tower-algebraic-stratification",
  ],
  computation: {
    engine: "sympy",
    script: "folio-assistant/computations/substrate/hecke_core.py",
    witness:
      "folio-assistant/computations/hecke-core-symbolic-migration.witness.json",
    status: "verified",
  },
  tags: [
    "tier:E",
    "hartree-energy",
    "molecular-binding",
    "fine-structure",
    "alpha-em",
    "lp-dual",
    "j1-vanishing",
    "open-problem",
    "derivation-roadmap",
    "conjecture",
  ],
});
