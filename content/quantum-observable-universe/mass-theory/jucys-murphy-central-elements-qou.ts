import { proposition } from "../../schema/builders";

/**
 * Jucys–Murphy central elements at the QOU substrate.
 *
 * Murphy (1981) showed that, in the Iwahori–Hecke algebra
 * H_n(q), the elementary symmetric polynomials in the
 * Jucys–Murphy elements
 *
 *     e_ℓ(J_1, J_2, …, J_n)  ∈  Z(H_n(q))
 *
 * lie in the centre.  By Schur's lemma, each acts as a scalar
 * on every Wedderburn block V_λ; the scalar is the elementary
 * symmetric polynomial in the JM-eigenvalues
 *
 *     c_ℓ(λ)  =  e_ℓ\big(\{q^{2c(\square)} : \square \in \lambda\}\big)
 *
 * where c(□) = j − i is the cell content.
 *
 * Application to QOU: the GB-filtration level ℓ correction to
 * the mass formula is the τ-extraction of e_ℓ(J_1,…,J_n)|_{ht=ℓ+1}
 * — a CENTRAL element with closed-form spectrum.  This converts
 * every "level ℓ correction term" (α_5 shell correction, etc.)
 * from an AME-fitted parameter into a derivable q-rational
 * combinatorial sum.
 *
 * The block instantiates Murphy 1981 in the QOU formalism and
 * is the engine that powers prop:mass-formula-iterative-lp-dual.
 */
export default proposition({
  label: "prop:jucys-murphy-central-elements-qou",
  proofs: ["prf:jucys-murphy-central-elements-qou"],
  title:
    "Elementary symmetric polynomials in Jucys–Murphy elements are central in $H_n(q)$ with closed-form spectrum on each Wedderburn block",
  lean: {
    ref: "qou:QOU.BraidKnot.JucysMurphyCentralElementsQOU",
    validation: "not_checked",
  },
  uses: ["prop:frobenius-self-duality-forces-lp-dual-extraction"],
  cites: ["murphy1992", "jucys1974", "kassel1995"],
  tags: [
    "jucys-murphy",
    "central-element",
    "hecke-algebra",
    "wedderburn-block",
    "cell-content",
    "elementary-symmetric-polynomial",
    "derived-coefficient",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/probes/jucys_murphy_central_elements_qou_probe.py",
    witness: "computations/probes/jucys-murphy-central-elements-qou-probe.witness.json",
    status: "verified",
  },
});
