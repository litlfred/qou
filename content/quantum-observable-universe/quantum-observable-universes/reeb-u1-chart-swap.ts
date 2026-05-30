import { remark } from "../../schema/builders";

export default remark({
  label: "rem:reeb-u1-chart-swap",
  title:
    "Chart-swap $U(1)$ is the Reeb flow: Wick rotation, $i$, and knot operators",
  tags: [
    "reeb",
    "chart-transition",
    "wick-rotation",
    "imaginary-unit",
    "u1-action",
    "knot-operator",
    "categorical-coordinate",
  ],
  uses: [
    "def:contact-affine-chart",
    "rem:affine-chart-origin-of-i-and-q",
    "thm:categorical-reeb-exists",
    "ex:categorical-reeb-brings",
    "ex:reeb-su2",
    "def:frobenius-hopf-substrate",
    "rem:i-as-braiding-orientation",
  ],
  interprets: "def:contact-affine-chart",
});
