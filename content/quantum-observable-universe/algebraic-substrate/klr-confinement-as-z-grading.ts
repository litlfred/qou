import { proposition } from "../../schema/builders";

/**
 * Confinement levels in the multi-particle Gröbner-Shirshov engine
 * correspond exactly to the rigid ℤ-grading shifts of the underlying
 * KLR modules.
 *
 * The original heuristic "confinement levels" (used to bound multi-
 * particle interactions in the GS reduction) lift to a rigorous
 * categorical type via the KLR algebra's intrinsic ℤ-grading.  Per
 * Khovanov-Lauda 2009, KLR algebras R_n of type A_∞ are graded by
 *
 *   deg(σ_i) = 2,    deg(idempotent e_λ) = 0,
 *
 * with each Wedderburn block V_λ acquiring a specific shift d(λ).
 *
 * The confinement bound `confinement_level ≤ ℓ_max` is precisely
 *
 *   max grading-shift of accessible KLR modules ≤ ℓ_max.
 *
 * Crystal operators ẽ_i / f̃_i act on the ℤ-graded category by
 * shifts of ±1 (or other fixed integers).  A traversal that
 * attempts to push a state beyond the ℓ_max bound is geometrically
 * disallowed — the resulting module would lie in a forbidden
 * grading degree.
 *
 * Cross-references:
 *  - prop:crystal-graph-realization-stable-states (the KLR machinery)
 *  - prop:cemetery-as-annihilated-subcategory (companion ω-kernel filter)
 *  - prop:atomic-mass-gb-nf (the GS engine using confinement levels)
 *
 * Citations: Khovanov-Lauda 2009.
 */
export default proposition({
  label: "prop:confinement-as-z-grading",
  title:
    "Confinement levels as rigid $\\mathbb{Z}$-grading shifts in KLR modules",
  uses: [
    "prop:crystal-graph-realization-stable-states",
    "prop:cemetery-as-annihilated-subcategory",
    "prop:atomic-mass-gb-nf",
  ],
  cites: [
    "khovanov-lauda-2009",
  ],
  lean: {
    ref: "qou:QOU.AlgebraicSubstrate.KLRConfinementGrading.confinement_eq_grading_bound",
    validation: "not_checked",
  },
  tags: [
    "klr-algebra",
    "z-grading",
    "confinement-level",
    "wedderburn-shift",
    "kashiwara",
    "categorification",
  ],
});
