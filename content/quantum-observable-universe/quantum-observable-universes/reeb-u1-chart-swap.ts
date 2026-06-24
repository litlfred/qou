import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:reeb-u1-chart-swap",
  proofs: ["prf:reeb-u1-chart-swap"],
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
    // conj:os-reflection-positivity-from-reeb removed (2026-06-08 §3b sweep):
    // the chart-swap U(1) = Reeb U(1) identity is proved unconditionally; OS
    // positivity is one downstream application, not a hypothesis. Prose keeps the ref.
  ],
  lean: {
    ref: "qou:QOU.ChartSwap.eqReeb",
    validation: "not_checked",
  },
});
