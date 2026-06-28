import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:categorical-dirac-operator",
  label: "rem:lqg-adm-ashtekar-comparison-limitations",
  title: "Limitations of the QOU/LQG comparison",
  tags: [
    "loop-quantum-gravity",
    "comparison",
    "caveat",
    "mass-gap",
  ],
  uses: [
    "def:categorical-dirac-operator",
    "rem:yang-mills-surreal-bound",
    "conj:os-reflection-positivity-from-reeb",
  ],
});
