import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:categorical-dirac-operator",
  label: "rem:lqg-adm-ashtekar-comparison-advantages",
  title:
    "Three structural advantages of QOU over canonical quantum gravity",
  tags: [
    "loop-quantum-gravity",
    "barbero-immirzi",
    "problem-of-time",
    "self-duality",
    "comparison",
  ],
  uses: [
    "def:categorical-dirac-operator",
    "def:categorical-instanton",
    "prop:reeb-u1-chart-swap",
    "thm:categorical-reeb-exists",
    "def:frobenius-hopf-substrate",
    "def:adelic-substrate",
  ],
});
