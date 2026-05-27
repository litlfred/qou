import { conjecture } from "../../schema/builders";

export default proposition({
  label: "prop:jet-convergence-classical-limit",
  title:
    "Jet-filtered knot invariant converges to classical dimension-weighted average",
  lean: { ref: "qou:QOU.BraidKnot.jet_convergence_classical_limit",
    validation: "not_checked",
  },
  uses: ["prop:jet-filtered-knot-factor"],
  tags: [
    "convergence",
    "classical-limit",
    "branching-rule",
    "wedderburn",
    "jet-filtration",
  ],
  cites: [
    "feray2010",
    "kerov1996",
  ],
});
