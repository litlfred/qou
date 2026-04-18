import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:categorical-action",
  label: "rem:categorical-action-vs-chern-simons",
  title: "Comparison with the classical Chern--Simons action",
  tags: ["chern-simons", "classical-limit", "rigid-trace", "comparison"],
  uses: [
    "def:categorical-action",
    "prop:qou-canonical-action",
    "rem:physicist-translation",
    "rem:chern-simons-as-knot-invariant",
  ],
});
