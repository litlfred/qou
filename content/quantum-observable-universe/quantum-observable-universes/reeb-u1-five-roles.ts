import { remark } from "../../schema/builders";

export default remark({
  label: "rem:reeb-u1-five-roles",
  interprets: "prop:reeb-u1-chart-swap",
  title:
    "Five roles of the Reeb $U(1)$: Wick rotation, $i$, chart-swap, knot framing, OS reflection",
  tags: [
    "reeb",
    "chart-transition",
    "wick-rotation",
    "imaginary-unit",
    "u1-action",
    "knot-operator",
  ],
  uses: [
    "prop:reeb-u1-chart-swap",
    "rem:affine-chart-origin-of-i-and-q",
    "def:frobenius-hopf-substrate",
  ],
});
