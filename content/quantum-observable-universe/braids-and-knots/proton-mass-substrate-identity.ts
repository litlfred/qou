import { proposition } from "../../schema/builders";

/**
 * Substrate-categorical identity for the proton mass at substrate q_0:
 *
 *   m_p = 2 · m_μ · |tr_M(β_Bor, q_0)| · [3]_q! / q_0^3  −  12 · m_e
 *
 * Matches CODATA m_p to 0.24 ppm (95-dps verified).  Building blocks
 * are all Lean-proved closed forms:
 *
 *   |tr_M(β_Bor, q)| = (4 + h² − 3h⁴ − h⁶) / (h² + 4)
 *                    (BorromeanMarkovTrace.lean)
 *
 *   [3]_q! = (q² + 1 + q⁻²)(q + q⁻¹)
 *           (YLambdaQSchur.lean qFactorial_three)
 *
 * Combined with prop:flavor-split-substrate (canonically-derived
 * Hecke-skein flavor split), this gives a full m_p + m_n derivation
 * from only (m_e, m_μ, q_0) — CAL-3 (Q_β) becomes a DERIVED quantity,
 * not an input.
 *
 * Structural identifications:
 *   - "2"  = bar-pair partition count: (3) ↔ (1,1,1) transpose pair
 *           under bar-Mullineux symmetry (PR #1289 rectangular conjecture
 *           confirms the (1,1,1) dominance at A=1).
 *   - "12" = inverse of the Ocneanu cancellation leading-pole coefficient
 *           in tr_M(β_Bor, q) ∼ −1/(12·q^10) as q → 0
 *           (per 2026-05-04-ocneanu-cancellation-numerical-verification.md,
 *           verified to 200 dps).
 *
 * The factor 12 connects two distinct categorical layers — the q=0
 * Laurent-pole structure (Ocneanu cancellation) and the q=q_0
 * substrate mass formula — via a single Bernoulli-like integer.
 *
 * Status: empirical near-identity at 0.24 ppm.  Categorical proof
 * requires:
 *   1. Bar-pair derivation of the factor 2 from y_(3) ↔ y_(1,1,1)
 *      transpose-pair (currently Lean-proved at the y_λ level via
 *      yLambdaQSchur_transpose_pair).
 *   2. Categorical derivation of the 12 via Ocneanu / Hoefsmit
 *      symbolic (PR #546's 2×2 bug fix is pending).
 *   3. Identification of F_Bor(q) := |tr_M(β_Bor, q)| · [3]_q! / q^3
 *      as a natural categorical observable.
 *
 * Refs:
 *   - docs/audits/2026-05-25-proton-mass-identity-12-me-ocneanu.md (full writeup)
 *   - docs/audits/2026-05-04-ocneanu-cancellation-numerical-verification.md (the −1/12)
 *   - folio-assistant/computations/m_p_substrate_identity_50dps.py
 *   - PR #1272 (origin), PR #546 (Hoefsmit symbolic for −1/12)
 */
export default proposition({
  label: "prop:proton-mass-substrate-identity",
  title:
    "Proton-mass substrate identity $m_p = 2 \\cdot m_\\mu \\cdot |\\mathrm{tr}_M(\\beta_{\\mathrm{Bor}}, q_0)| \\cdot [3]_q! / q_0^3 - 12 \\cdot m_e$",
  uses: [
    "thm:borromean-markov-trace-closed-form",
    "thm:q-schur-y-lambda-closed-form",
    "prop:flavor-split-substrate",
    "conj:rho-k-pair-gen-canonical-form",
  ],
  cites: [
    "adams1985hyperbolic",
    "wenzl1988hecke",
    "chlouveraki2016hdr",
  ],
  tags: [
    "mass-formula",
    "proton",
    "borromean",
    "substrate-identity",
    "ocneanu-cancellation",
    "bernoulli-12",
    "0.24ppm",
    "two-calibration-baryon",
    "lean-proved-building-blocks",
  ],
});
