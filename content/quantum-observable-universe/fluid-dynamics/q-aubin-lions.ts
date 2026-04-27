import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:q-aubin-lions",
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
