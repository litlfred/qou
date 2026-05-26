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
 *   - "2"  = dim V_{(2,1)} — classical dimension of the standard irrep
 *           of S_3 (trace-dominant per Wedderburn diagnostic at 49% of T1).
 *           Lean-proved via hook-length formula in DimStandardRepS3.lean.
 *   - "12" = empirical integer near-match (to ~10⁻⁴ relative accuracy).
 *           CORRECTION (2026-05-26): earlier Ocneanu −1/12 attribution was
 *           WRONG — that pole belongs to a different braid (canonical SDP
 *           T_w_proton, not β_Bor). Structural origin of the 12 is OPEN.
 *
 * The factor 12's categorical origin is the main open problem for
 * elevating this from empirical (0.24 ppm) to proved.
 *
 * Status: empirical near-identity at 0.24 ppm.  Categorical proof
 * requires:
 *   1. Factor 2 = dim V_{(2,1)} is NOW Lean-proved in
 *      DimStandardRepS3.lean (hook-length formula: 3!/3 = 2).
 *   2. Categorical derivation of the 12 — structural origin OPEN.
 *      Earlier Ocneanu −1/12 attribution corrected as wrong braid.
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
