import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:reeb-u1-chart-swap",
  title:
    "Chart-swap $U(1)$ equals the Reeb $U(1)$ as subgroups of $\\mathrm{Aut}(\\mathbb{P}(V))$",
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
    "def:projective-line-object",
    "def:quantum-observable-universe",
    "conj:os-reflection-positivity-from-reeb",
  ],
  lean: {
    ref: "qou:QOU.ChartSwap.eqReeb",
    validation: "not_checked",
  },
});
