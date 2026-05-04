import { conjecture } from "../../schema/builders";

/**
 * Conjecture: the Hartree-energy scaling
 * $E_h = m_e c_q^2 \alpha_{EM}^2$ used as input in the molecular
 * binding LP/SDP framework should arise as the leading non-trivial
 * coefficient of the LP-dual variable $y_{\mathrm{cov}}$ expanded
 * in powers of $\alpha_{EM}$, with the $J^1$ (linear-in-$\alpha$)
 * contribution vanishing by a categorical-symmetry argument that
 * is currently *open*.
 *
 * Three candidate mechanisms are surveyed in the .md (Pauli /
 * 2-electron combinatorial counting; Frobenius LP quadratic-form;
 * antipode invariance of the Markov trace), each with an explicit
 * gap. The most promising route — the $q \mapsto -q^{-1}$
 * substrate involution, which *does* flip the sign of
 * $\alpha_{EM} = 1/(q\,[9]_q\,[10]_q)$ — is identified as the
 * recommended next step.
 *
 * Honest open-problem block: no closure claimed, no numerology,
 * coefficient $c_2$ conjecturally inside
 * $R = \mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$.
 */
export default conjecture({
  label: "conj:e-hartree-categorical-derivation",
  title:
    "Conjectured categorical derivation of $E_h = m_e c_q^2 \\alpha_{EM}^2$ via $J^1$-vanishing in the molecular LP dual",
  uses: [
    "prop:em-coupling-projection",
    "prop:h2-lp-dual-binding",
    "prop:ilp-covalent-bond",
    "prop:operator-selection-lp",
    "prop:lp-dual-stability",
    "prop:antiparticle-crossing-reversal",
    "prop:spectral-sequence-collapse",
    "prop:curvature-rank-gb-stratification",
    "cor:commutative-chirality-vanishes",
    "prop:bohr-radius-categorical",
    "prop:archimedean-hartree-derivation",
  ],
  tags: [
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
