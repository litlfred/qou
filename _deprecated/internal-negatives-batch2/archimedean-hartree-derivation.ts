import { proposition } from "../../schema/builders";

/**
 * The archimedean derivation of E_Hartree = m_e c² α² as the
 * energy unit per Φ_1 in molecular binding.
 *
 * DERIVATION STATUS — partial transport sketch. The α² scaling is
 * argued by chaining through prop:bohr-radius-categorical (which
 * itself transports QED virial-balance). The asserted "uniqueness"
 * of the archimedean energy unit reduces to "matches QED in q→1
 * limit" — empirical consistency, not a fully internal QOU
 * derivation.
 *
 * The "numerical match" with the H_2 binding witness (4.638 eV
 * vs experimental 4.476 eV) is internal-consistency arithmetic,
 * not a verification: the LP outputs a dimensionless 0.687, the
 * Python multiplies by a hardcoded conversion involving α², and
 * arithmetic gives 4.638 eV. Any framework with E_h ~ m_e c² α²
 * would match within ~10%.
 *
 * Recorded with caveats and an explicit list of what closure
 * requires (see .md). Companion to prop:bohr-radius-categorical.
 */
export default proposition({
  label: "prop:archimedean-hartree-derivation",
  lean: { ref: "qou:QOU.Archimedean.archimedean_hartree_derivation", validation: "not_started" },
  title:
    "Archimedean energy unit $E_{\\mathrm{Hartree}} = m_e c^2 \\alpha_{EM}^2$ per $\\Phi_1$ (transport sketch; closure open)",
  uses: [
    "prop:bohr-radius-categorical",
    "prop:em-coupling-projection",
    "prop:operator-selection-lp",
    "prop:h2-lp-dual-binding",
    "def:h2-molecular-braid",
    "def:archimedean-realization-functor",
    "conj:e-hartree-categorical-derivation",
  ],
  computation: {
    engine: "sympy",
    script: "computations/hecke_core.py",
    witness:
      "computations/hecke-core-symbolic-migration.witness.json",
    status: "verified",
  },
  tags: [
    "hartree-energy",
    "archimedean-functor",
    "alpha-em",
    "molecular-binding",
    "dimensional-analysis",
    "virial-theorem",
    "bohr-radius",
    "transport-sketch",
    "derivation-open",
  ],
});
