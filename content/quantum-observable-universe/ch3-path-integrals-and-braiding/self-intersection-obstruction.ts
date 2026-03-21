import { corollary } from "../../schema/builders";

/**
 * Corollary: Obstruction to Self-Intersection.
 *
 * The non-cocommutativity of the Hopf structure for q ≠ 1 acts as a
 * geometric barrier preventing knot self-intersection.  The R-matrix
 * controls the failure of the cocommutativity square.
 */
export default corollary({
  label: "cor:self-intersection-obstruction",
  title: "Obstruction to self-intersection",
  tags: [
    "knot-theory",
    "self-avoidance",
    "r-matrix",
    "hopf-algebra",
    "q-deformation",
  ],
  uses: [
    "prop:categorical-mobius-energy",
  ],
  lean: {
    decl: "QOU.PathIntegrals.SelfIntersectionObstruction",
    file: "QOU/PathIntegrals/MobiusEnergy.lean",
    validation: "not_checked",
  },
  status: "not_started",
  hasProof: true,
});
