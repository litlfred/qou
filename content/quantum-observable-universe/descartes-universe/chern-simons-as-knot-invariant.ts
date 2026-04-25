import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:em-coupling-chern-simons",
  label: "rem:chern-simons-as-knot-invariant",
  title: "Classical Chern--Simons as a non-hyperbolic knot invariant",
  tags: [
    "chern-simons",
    "torus-knot",
    "geometric-invariant",
    "hyperbolic-volume",
    "fine-structure",
  ],
  uses: [
    "prop:em-coupling-chern-simons",
    "rem:categorical-action-vs-chern-simons",
  ],
});
