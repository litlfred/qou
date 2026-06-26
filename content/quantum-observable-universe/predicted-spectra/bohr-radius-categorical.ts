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
  authorNotes: [
    { kind: "note", date: "2026-06-26", body: "This formulation provides a deep structural insight by deriving the Bohr 1/n^2 dependency purely from the Hecke-algebraic gap. Bypassing the standard additive kinetic/Coulomb split, it serves as a novel purely categorical recovery of a foundational quantum result." },
    {
      kind: "status",
      body: "This proposition is **not yet derived from QOU/Hecke structure**.\nThe formula $a_0 = \\hbar/(m_e c \\alpha)$ is *transported* from\nthe standard QED virial-balance argument by analogy. The\ncomponents $\\Phi_{1}^{\\mathrm{kin}}$ and $\\Phi_{1}^{\\mathrm{Coul}}$\nare *postulated* (their dimensional behavior asserted by analogy\nwith QED kinetic/Coulomb energies); they have **not** been\nconstructed as Hecke-algebraic quantities.\n\nSpecifically, a direct computational test\n([`computations/h2-molecular-binding.py`](computations/h2-molecular-binding.py))\nshows that per-generator transfer-matrix updates are in general\n*multiplicative*, mixing intra-atomic (dressed/kinetic-like) and\ninter-atomic (bare/Coulomb-like) crossing contributions\nnonlinearly within each $V_i$. Round-8 below finds that the\ncross-terms $h_b \\cdot h_d$ happen to **cancel for the optimal\nordering** $[p_1, e_2, e_1, p_2]$ of $H_2$, leaving an additive\n$\\{h_b, h_d\\}$ decomposition there; but this cancellation is\npermutation-specific and does not give a uniform\nHecke-algebraic definition of $\\Phi_1^{\\mathrm{kin}}$ vs\n$\\Phi_1^{\\mathrm{Coul}}$ that holds for arbitrary molecular\nbraids.\n\nThe proposition is recorded with this caveat — not as a closed\ntheorem — to preserve the structural mapping between QOU and\nstandard physics. Genuine categorical closure remains an open\nresearch direction; five candidate routes are surveyed below.",
    },
    {
      kind: "status",
      body: "**Proposition with explicit caveat.** The formula\n$a_{0}^{\\mathrm{cat}} = \\hbar/(m_e c \\alpha_{EM})$ is asserted as\nthe structural mapping between QOU and the standard QED Bohr\nlength, with the explicit acknowledgement that the components\n$\\Phi_{1}^{\\mathrm{kin}}, \\Phi_{1}^{\\mathrm{Coul}}$ are postulated\n(not derived) and that closure requires one of options 4a–4e.\n\nThis is intentionally weaker than a closed proposition. It serves\nas a **research target**: any future categorical derivation must\nrecover this formula. It also serves as **honest documentation**\nof the present epistemic state: we know what answer the framework\nmust give, but we have not yet derived it from algebraic\nstructure.",
    },
  ],
});
