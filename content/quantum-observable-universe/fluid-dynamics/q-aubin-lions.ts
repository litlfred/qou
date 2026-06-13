import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:q-aubin-lions",
  lean: { ref: "qou:QOU.FluidDynamics.QAubinLions" },
  title:
    "q-deformed Aubin--Lions lemma: compactness of the solution family as $q \\to 1$",
  uses: [
    "thm:quantum-peter-weyl",
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
