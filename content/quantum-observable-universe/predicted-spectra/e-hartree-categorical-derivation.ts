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
    script: "computations/substrate/hecke_core.py",
    witness:
      "computations/hecke-core-symbolic-migration.witness.json",
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
  authorNotes: [
    {
      kind: "status",
      body: "The standard physics linear-Stark vanishing is\n$\\langle \\psi_0 \\,|\\, \\hat r \\,|\\, \\psi_0 \\rangle = 0$, where the\nparity-odd object is the *operator* $\\hat r$ (the dipole), not the\ncoupling $\\alpha_{EM}$. The categorical analogue should therefore\nseek a $\\sigma$-antisymmetric *Hecke-algebra perturbation operator*\n$\\Delta_{\\mathrm{cov}}$ (built from\n$(\\sigma_i - \\sigma_i^{-1})$ skein factors, which *are*\n$\\sigma$-antisymmetric in $R$) and test whether the bare atomic\nMarkov trace\n$\\Phi_1(\\mathcal{M}_{\\mathrm{atom}} \\cdot \\Delta_{\\mathrm{cov}})$\nvanishes by a categorical parity selection rule (atomic ground state\n$\\sigma$-symmetric, perturbation $\\sigma$-antisymmetric, trace odd\nunder $\\sigma$, hence zero).\n\nThe leading non-trivial contribution would then come from the\nsecond-order (Rayleigh–Schrödinger-style) correction:\n\n$$\n  \\delta y_{\\mathrm{cov}}^{(2)}\n  \\;=\\;\n  \\sum_{n \\neq 0}\n    \\frac{\\bigl|\\Phi_1(\\mathcal{M}_n^{\\dagger} \\cdot \\Delta_{\\mathrm{cov}}\n                         \\cdot \\mathcal{M}_{\\mathrm{atom}})\\bigr|^{2}}\n         {E_0 - E_n},\n$$\n\nwhich is bilinear in $\\Delta_{\\mathrm{cov}}$ and so accordingly\n$\\alpha_{EM}^{2}$-scaled if one factor of $\\alpha_{EM}$ accompanies\neach insertion of $\\Delta_{\\mathrm{cov}}$.\n\n**Concrete next investigation:**\n(i) identify the explicit $\\sigma$-antisymmetric component\n$\\Delta_{\\mathrm{cov}}$ of the covalent Hecke perturbation;\n(ii) verify $\\Phi_1(\\mathcal{M}_{\\mathrm{atom}} \\cdot \\Delta_{\\mathrm{cov}}) = 0$\nsymbolically in $R$;\n(iii) compute the second-order coefficient $c_2$ from the\nRayleigh–Schrödinger sum above and check it lies in $R$.\n\nThis is closer to a tractable computation than the\ncoupling-parity route, and aligns with how\n[antiparticle crossing reversal](#prop:antiparticle-crossing-reversal)\nalready realises $\\sigma$ on Hecke generators at the operator level.",
    },
    {
      kind: "status",
      body: "Pursue the **combined $\\sigma \\cdot \\varepsilon$ parity** for the\n$H_2$ molecular braid:\n\n1. Make $\\varepsilon$ explicit as conjugation by a specific braid\n $\\gamma \\in B_4$ that swaps strands $(p_1 \\leftrightarrow p_2,\n   e_1 \\leftrightarrow e_2)$.\n2. Decompose the covalent perturbation\n $\\Delta_{\\mathrm{cov}}$ into joint $(\\sigma, \\varepsilon)$\n parity sectors; identify the\n $(\\sigma\\text{-anti}, \\varepsilon\\text{-sym})$ component.\n3. Show that the bare $H_2$ ground state\n $\\mathcal{M}_{\\mathrm{atom}}^{\\otimes 2}$ lies in the\n $(\\sigma\\text{-sym}, \\varepsilon\\text{-sym})$ sector.\n4. Conclude — IF the joint parity argument goes through — that\n $\\mathrm{tr}_M(\\mathcal{M}_{\\mathrm{atom}}^{\\otimes 2} \\cdot\n   \\Delta_{\\mathrm{cov}}^{(\\sigma\\text{-anti},\\,\\varepsilon\\text{-sym})})\n   = 0$ exactly (not just up to factor $h$), giving the desired\n $J^{1}$-vanishing.\n\nThe heteronuclear case (CO, HCl, etc.) does **not** satisfy\n$\\varepsilon$-symmetry. Standard physics predicts a nonzero\npermanent dipole moment for such molecules, and\n$\\alpha_{EM}^{1}$ contributions to binding *do* in fact appear\n(though they are smaller than $\\alpha_{EM}^{2}$ at\n$\\alpha_{EM} \\approx 1/137$). This is consistent with the\n$\\sigma\\varepsilon$ argument requiring nuclear-exchange symmetry.",
    },
  ],
});
