import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:markov-trace-axiomatic-closed-form",
  label: "rem:vassiliev-filtration-graded-lp",
  title:
    "Vassiliev filtration gives a graded hierarchy of operator-selection LPs",
  uses: [
    "prop:markov-trace-axiomatic-closed-form",
    "rem:vassiliev-filtration-mass-tower",
    "def:knot-operator-energy",
  ],
  tags: [
    "vassiliev",
    "optimization",
    "lp-sdp",
    "operator-selection",
    "graded-hierarchy",
  ],
});
