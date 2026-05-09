import { proposition } from "../../schema/builders";

/**
 * The cemetery group is the localizing Serre subcategory of the
 * KLR-categorified module category that is annihilated by the
 * Observation Frame functor τ (= ω in the original branch directive).
 *
 * Geometrically: the cemetery group is the kernel of decategorification.
 * Modules in this subcategory are homologically acyclic complexes;
 * their graded Euler characteristic vanishes, so they map to zero
 * under τ.
 *
 * Algorithmically: this provides a "kill switch" for the Gröbner-
 * Shirshov reduction engine.  When a sequence of crystal operators
 * pushes a state into the cemetery subcategory, the computation
 * branch is instantly truncated — no algebraic cancellations need
 * be computed; the state drops natively.
 *
 * Cross-references:
 *  - prop:crystal-graph-realization-stable-states (the KLR machinery)
 *  - prop:observation-frame (the τ functor / decategorification)
 *  - prop:atomic-mass-gb-nf (the GS engine that consumes the kill-switch)
 *
 * Citations: Khovanov-Lauda 2009, Brundan-Kleshchev 2009,
 * Gabriel 1962 (localizing subcategories).
 */
export default proposition({
  label: "prop:cemetery-as-annihilated-subcategory",
  title:
    "Cemetery group as the $\\tau$-annihilated localizing subcategory of $\\mathcal{C}_n$",
  uses: [
    "prop:crystal-graph-realization-stable-states",
    "prop:observation-frame",
    "prop:atomic-mass-gb-nf",
  ],
  cites: [
    "khovanov-lauda-2009",
    "brundan-kleshchev-2009",
    "gabriel-1962",
  ],
  lean: {
    ref: "qou:QOU.AlgebraicSubstrate.KLRCemeteryAnnihilated.cemetery_eq_tau_kernel",
    validation: "not_checked",
  },
  tags: [
    "klr-algebra",
    "cemetery-group",
    "observation-frame",
    "decategorification",
    "localizing-subcategory",
    "kill-switch",
    "categorification",
  ],
});
