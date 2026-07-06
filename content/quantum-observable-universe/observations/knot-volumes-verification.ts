import { proof } from "../../schema/builders";

/**
 * Computational proof: knot volumes verified via SnapPy.
 *
 * This proof block verifies all hyperbolic volume claims in the paper
 * by computing them independently using the SnapPea kernel (via SnapPy).
 * The witness file records computed values, expected values, and error bounds.
 *
 * Trust chain:
 *   SnapPy computation → witness JSON → Lean axiom (with -- Ref: [computation])
 */
export default proof({
  label: "prf:knot-volumes-verification",
  title: "Knot volume verification (SnapPy)",
  tags: ["computation", "snappea", "hyperbolic", "verification"],
  uses: [
    "prop:topological-mass-formula",
    "sec:hyperbolic-volumes-prose",
  ],
  computation: {
    engine: "snappea",
    script: "computations/knot-volumes.py",
    witness: "computations/substrate/knot-volumes.witness.json",
    status: "verified",
    requires: ["snappy>=3.3"],
  },
});
