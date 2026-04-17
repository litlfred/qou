import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:jet-convergence-classical-limit",
  title:
    "Jet-filtered knot invariant converges to classical dimension-weighted average",
  lean: {
    decl: "QOU.BraidKnot.jet_convergence_classical_limit",
    validation: "not_checked",
  },
  uses: [
    "conj:jet-filtered-knot-factor",
    "prop:three-parameters-wedderburn",
    "prop:confined-knot-binding",
  ],
  tags: [
    "convergence",
    "classical-limit",
    "branching-rule",
    "wedderburn",
    "jet-filtration",
  ],
});
