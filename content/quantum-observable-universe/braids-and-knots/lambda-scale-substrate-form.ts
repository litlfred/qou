import { conjecture } from "../../schema/builders";

/**
 * The Borromean baryon λ_scale has an empirical near-form
 *
 *   λ_scale ≈ 5/2 − h² · G + O(h^4)    [acknowledged-CAL-4 as of 2026-05-23]
 *
 * where h = q − q^{-1} is the Hecke deformation and G = Catalan's
 * constant. The form matches CODATA m_p / m_e to 5.4 ppm at q_0 but
 * is NOT a structural identity — see the .md for the full eight-search
 * exhaustion record (Tier 5, PR #923, #928, #941, #943, #951, #957,
 * #969).
 *
 * Decisive refutations (2026-05-23):
 *   - PR #951 q-locality: residual across q ∈ [q_0 ± 0.05] has slope
 *     ~−1.7×10⁷ ppm/q. The match at q_0 is a residual zero-crossing,
 *     not a smooth identity. Per the standing "q_0 not special"
 *     discipline, this disqualifies the form as structural.
 *   - PR #957 reframing: λ_p(q) = (m_p/m_e) · ℏ_q² / (8G) is exactly
 *     a constant times ℏ_q² (where ℏ_q := (q-1)/q, NOT h_q = q-1/q).
 *     The h²·G form uses the wrong q-parametrization by construction.
 *     Structural search target is the constant C ≈ 250.576, not F(q).
 *   - PR #969 Strategy J: tr_M(β_p)/tr_M(β_n) ratios do not predict
 *     m_n/m_p either (0.45% best pure-substrate).
 *
 * The block is RETAINED under its original label for graph stability
 * and historical reference. Readers should interpret λ_scale as
 * "the proton scale empirically pinned by CAL-4, not derived from
 * substrate" — formally an acknowledged-CAL-4 falsifiable prediction
 * per `conj:lambda-scale-bring-bloch-identity`.
 *
 * History:
 *   - 2026-05-18: emerged from a systematic search following PR #683
 *     "investigate close the ~1700× scale gap" direction. Originally
 *     framed as proposing an explicit substrate form with one
 *     structural correction term.
 *   - 2026-05-21 (PR #888): truth-in-naming demoted the literal twin
 *     to LAMBDA_PROTON_FITTED_FROM_CODATA.
 *   - 2026-05-22 (PR #904): block kind demoted from `proposition` to
 *     `conjecture` per §3b conjectural-propagation discipline.
 *   - 2026-05-23 (PR #951/#957/#969): empirical exhaustion + q-locality
 *     refutation + reframing → formal acknowledged-CAL-4 status.
 *
 * NOT used as input to any production compute. The 3-calibration chain
 * (m_e, m_μ/m_e, Q_β) is the authoritative path; this block is a
 * historical record of the empirical 5.4 ppm near-form.
 */
export default conjecture({
  label: "conj:lambda-scale-substrate-form",
  title:
    "Borromean baryon $\\lambda_{\\text{scale}}$ empirical form $5/2 - h^2 \\cdot G$ (acknowledged-CAL-4)",
  uses: [
    "conj:borromean-baryon-mass-formula",
    "thm:wedderburn-mass-formula",
    "prop:plancherel-weight-boundedness",
  ],
  cites: [
    "adams1985hyperbolic",
    "milnor1982hyperbolic",
  ],
  tags: [
    "mass-formula",
    "borromean",
    "lambda-scale",
    "catalan-constant",
    "h-squared-expansion",
    "conjecture",
    "5.4ppm",
    "acknowledged-cal-4",
    "non-smooth-in-q",
  ],
});
