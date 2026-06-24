import { proposition } from "../../schema/builders";

/**
 * Structural justification for the LP-dual formulation of mass.
 *
 * The Markov trace τ on H_n(R, q) is non-degenerate (Frobenius
 * pairing). This makes (H_n(R,q), τ) a Frobenius algebra, hence
 * canonically self-dual: there is an isomorphism
 *
 *     Φ : H_n → H_n*,    a ↦ τ(a · −).
 *
 * In the operator-selection LP, the primal variable is the
 * nuclear braid x ∈ H_n; the dual variable u ∈ H_n* lives in
 * the dual space. Frobenius self-duality identifies these two
 * spaces — strong duality is structural, not analytic.
 *
 * Consequence: the Observation Frame (the τ-extraction of an
 * observable) does not "choose" between primal and dual — it
 * extracts both simultaneously. Each mass-formula coefficient
 * is therefore canonically a *shadow price*, not a primal
 * value. This is the structural reason every BW-style
 * coefficient at every filtration level ℓ is an LP-dual.
 *
 * This block is the foundation for
 * prop:mass-formula-iterative-lp-dual.
 */
export default proposition({
  label: "prop:frobenius-self-duality-forces-lp-dual-extraction",
  proofs: ["prf:frobenius-self-duality-forces-lp-dual-extraction"],
  title:
    "Frobenius self-duality of $(H_n(R,q),\\tau)$ forces $\\tau$-extraction to produce LP-dual variables",
  lean: {
    ref: "qou:QOU.BraidKnot.FrobeniusSelfDualityForcesLPDualExtraction",
    validation: "not_checked",
  },
  tags: [
    "frobenius-self-duality",
    "lp-duality",
    "shadow-price",
    "markov-trace",
    "observation-frame",
    "structural-justification",
  ],
});
