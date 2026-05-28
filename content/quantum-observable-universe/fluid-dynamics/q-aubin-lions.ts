import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-aubin-lions",
  title:
    "q-deformed Aubin--Lions lemma: compactness of the solution family as $q \\to 1$",
  uses: [
    "thm:quantum-peter-weyl",
    "prop:ns-counterexample",
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
