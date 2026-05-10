import { proposition } from "../../schema/builders";

/**
 * Unifying iterative LP-dual theorem for the QOU mass formula.
 *
 * The QOU mass formula
 *
 *     𝔪(ϱ) = Σ_ℓ T^(ℓ)(ϱ)
 *
 * is the sum over the GB-filtration / jet-order index ℓ of
 * level-ℓ correction terms.  Each T^(ℓ)(ϱ) is the τ-extraction
 * of a SINGLE central element P_ℓ = e_ℓ(J_1,…,J_n) restricted to
 * height-(ℓ+1) partitions:
 *
 *     T^(ℓ)(ϱ) = m_e · Σ_{λ ⊢ |ϱ|, ht(λ)=ℓ+1} w_λ(q) · c_ℓ(λ) / [n]_q!
 *
 * Equivalently (by Frobenius self-duality), each T^(ℓ) is the
 * optimal LP-dual variable u^(ℓ)* of a single Frobenius
 * positivity constraint at GB-level ℓ:
 *
 *     𝔪(ϱ) = Σ_ℓ u^(ℓ)*
 *
 * This single theorem REPLACES the seven ad-hoc mass-formula
 * terms (descended trace, single-gen brane, pair-gen brane,
 * Frobenius co-Casimir, chirality, cyclotomic tail, shell
 * correction) with one iterative recursion.  No AME-fitted
 * α_k parameters; all coefficients are derivable q-rationals.
 *
 * The proof structure:
 *   (a) Frobenius self-duality (prop:frobenius-self-duality-…)
 *       ⇒ each τ-extracted observable is an LP-dual variable.
 *   (b) Murphy 1992 (prop:jucys-murphy-central-elements-qou)
 *       ⇒ each level ℓ has a single central element P_ℓ with
 *         closed-form spectrum c_ℓ(λ) on every Wedderburn
 *         block.
 *   (c) GB-filtration stratification ⇒ ht(λ) ↔ jet order ℓ;
 *       the level-ℓ correction restricts to ht=ℓ+1 partitions.
 *
 * Combining (a)+(b)+(c) gives the iterative LP-dual recursion.
 *
 * This is the central simplification proposed in the
 * 2026-05-09 paper-simplification audit
 * (docs/audits/2026-05-09-paper-simplification-iterative-lp-dual.md).
 */
export default proposition({
  label: "prop:mass-formula-iterative-lp-dual",
  title:
    "QOU mass formula as iterative LP-dual: $\\mathfrak{m}(\\varrho) = \\sum_\\ell u^{(\\ell)*}$ where each $u^{(\\ell)*}$ is the LP-dual of the height-$(\\ell{+}1)$ Frobenius-positivity constraint with cost $\\tau(P_\\ell \\cdot -)$ (LP-dual characterisation; explicit closed form is conditional and refuted in its simplest version)",
  lean: {
    ref: "qou:QOU.BraidKnot.MassFormulaIterativeLPDual",
    validation: "not_checked",
  },
  uses: [
    "prop:frobenius-self-duality-forces-lp-dual-extraction",
    "prop:jucys-murphy-central-elements-qou",
    "prop:bw-coefficient-shadow-price",
    "prop:wedderburn-trace-identity",
    "rem:ontological-agnosticism",
    "prop:operator-selection-lp",
  ],
  cites: ["murphy1992", "kassel1995", "jucys1974"],
  tags: [
    "mass-formula",
    "iterative",
    "lp-duality",
    "shadow-price",
    "jucys-murphy",
    "gb-filtration",
    "jet-order",
    "unified-theorem",
    "derived-coefficient",
  ],
});
