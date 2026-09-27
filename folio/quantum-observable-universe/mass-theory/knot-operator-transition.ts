import { proposition } from "../../schema/builders";
export default proposition({
  label: "prop:knot-operator-transition",
  title: "Nucleon-addition operators: Hopf link at $A{=}3$, trefoil at $A{=}4$",
  lean: { ref: "qou:QOU.BraidKnot.knot_operator_transition", validation: "not_checked" },
  uses: ["def:per-nucleon-channel-decomposition"],
  tags: ["knot-operator", "hopf-link", "trefoil", "nucleon-addition", "topology-transition"],
});
