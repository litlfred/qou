import { conjecture } from "../../schema/builders";

/**
 * The Borromean baryon λ_scale has substrate-form
 *
 *   λ_scale = 5/2 − h² · G + O(h^4)
 *
 * where h = q − q^{-1} is the Hecke deformation, G = Catalan's constant
 * = Vol(B_3)/8 the per-cell hyperbolic volume of the Borromean rings
 * complement, and "5/2" is the conjugate-pair half-symmetric partition
 * count at the proton's Markov-stabilised Hecke level H_4.
 *
 * Numerical evidence: at MPFR 80 dps with q_0 from CAL-2,
 * the formula matches CODATA m_p / m_e to 5.4 ppm under
 * the Borromean baryon mass formula
 * (`conj:borromean-baryon-mass-formula`).
 *
 * Refines the open Status #2 ("derivation of λ_scale from substrate")
 * of `conj:borromean-baryon-mass-formula` by proposing an explicit
 * substrate form with one structural correction term.
 *
 * History (2026-05-18): emerged from a systematic search over q-integer
 * products + Vol/ℏ_q²-related combinations following the user's
 * direction "investigate close the ~1700× scale gap" on PR #683.
 * Both the "5/2" leading term and the "h²·G" correction have
 * plausible categorical interpretations (see .md), but neither is yet
 * rigorously derived. The status is JUSTIFICATION (numerical match
 * with structural interpretation) — not derivation.
 *
 * Conditional implications if proved:
 *   - Closes the m_p chain to 5.4 ppm (better than 1% threshold)
 *   - Lifts ¹H from `derivation_pending` → `derived` per
 *     `low_isotope_mass_table.py`
 *   - Tightens M_P_DERIVED_MAX_REL_DIFF from 1% → 10 ppm
 */
export default conjecture({
  label: "conj:lambda-scale-substrate-form",
  title:
    "Borromean baryon $\\lambda_{\\text{scale}}$ substrate form: $5/2 - h^2 \\cdot G + O(h^4)$",
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
    "substrate-derivation",
    "borromean",
    "lambda-scale",
    "catalan-constant",
    "h-squared-expansion",
    "conjecture",
    "5.4ppm",
  ],
});
