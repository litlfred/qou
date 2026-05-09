import { remark } from "../../schema/builders";

/**
 * Empirical findings: the simplest JM-central closed form for
 * α_5 is NOT atom-independent at q_0.
 *
 * The witness alpha-5-jucys-murphy-central.witness.json
 * (2026-05-09) computes:
 *
 *   α_5(A) := Σ_{λ ⊢ 3A, ht(λ)=6} w_λ(q_0) · c_5(λ)
 *
 * for A = 2, 3, 4 with c_5(λ) = e_5({q^{2c(□)} : □ ∈ λ}).
 * Normalised by [3A]_q_0!:
 *
 *   A=2: +6.69e-7
 *   A=3: +3.34e-6
 *   A=4: +1.12e-7
 *
 * Relative spread: 482%. The simplest form is NOT
 * atom-independent.
 *
 * This refutes the strongest version of
 * prop:mass-formula-iterative-lp-dual Step 5 — the JM-central
 * elementary symmetric polynomial does not, by itself, give
 * the AME-fitted α_5 ≈ −4.2 × 10^5 MeV.
 *
 * Structural framework (Frobenius self-duality, Murphy 1992,
 * GB-filtration) remains intact. Open question: which
 * REFINEMENT of the closed form yields atom-independence?
 *
 * Candidates:
 *   (1) Per-atom strand recipe: weighted sub-sum over
 *       partitions specific to the atom-knot-recipe (vs. all
 *       height-6 partitions of 3A).
 *   (2) Refined jet stratification: cut by Frobenius
 *       coordinate or Demazure sub-crystal, not just height.
 *   (3) Higher-order q-corrections from the categorical
 *       q-connection beyond leading-order JM-central scalars.
 */
export default remark({
  label: "rem:alpha-5-jm-central-empirical-findings",
  title:
    "Empirical refutation of the simplest JM-central closed form for $\\alpha_5$",
  interprets: "prop:mass-formula-iterative-lp-dual",
  uses: [
    "prop:mass-formula-iterative-lp-dual",
    "prop:jucys-murphy-central-elements-qou",
    "conj:shell-correction-term-seven",
  ],
  tags: [
    "empirical-finding",
    "alpha-5",
    "atom-dependence",
    "negative-result",
    "research-direction",
    "shell-correction",
  ],
});
