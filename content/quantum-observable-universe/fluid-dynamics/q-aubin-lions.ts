import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:q-aubin-lions",
  lean: {
    decl: "QOU.FluidDynamics.q_aubin_lions",
    validation: "not_checked",
  },
  title:
    "q-deformed Aubin--Lions lemma: compactness of the solution family as $q \\to 1$",
  uses: [
    "thm:q-ns-wellposedness",
    "thm:quantum-peter-weyl",
    "prop:q-spectral-sobolev",
    "prop:q-ns-nonlinear-uniqueness",
    "def:q-navier-stokes",
    "def:frobenius-pairing",
    "conj:ns-counterexample",
  ],
  tags: [
    "aubin-lions",
    "compactness",
    "convergence",
    "weak-limit",
    "counter-example",
    "millennium-problem",
  ],
});
