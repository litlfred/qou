import { conjecture } from "../../schema/builders";

/**
 * The categorical Bohr radius a_0^cat = ℏ/(m_e c α_EM).
 *
 * DERIVATION STATUS — partial. The dimensional formula is asserted by
 * direct transport from the standard QED virial-balance argument
 * (kinetic ℏ²/(m_e ℓ²) = Coulomb α ℏ c/ℓ at ℓ = ℏ/(m_e c α)). This
 * proposition does NOT yet derive the kinetic and Coulomb Markov-trace
 * components Φ_1^kin and Φ_1^Coul from Hecke-algebraic structure;
 * those components are postulated by analogy with QED, not constructed
 * as Hecke quantities.
 *
 * The proposition is recorded with this caveat (not as a closed theorem)
 * to preserve the structural mapping between QOU and standard physics
 * while being honest that genuine categorical closure remains open.
 *
 * Five candidate closure routes are explored in the .md (Option 4a-4e),
 * pointing to concrete next investigations.
 */
export default conjecture({
  label: "conj:bohr-radius-categorical",
  lean: { ref: "qou:QOU.Archimedean.bohr_radius_categorical", validation: "not_checked" },
  title:
    "Categorical Bohr radius $a_0^{\\mathrm{cat}} = \\hbar/(m_e c\\,\\alpha_{EM})$ (transported from QED virial-balance; categorical derivation open)",
  tags: [
    "bohr-radius",
    "virial-theorem",
    "categorical-length",
    "alpha-em",
    "dimensional-analysis",
    "hartree-energy",
    "transport-sketch",
    "derivation-open",
  ],
});
