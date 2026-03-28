import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-logarithmic-zeta",
  title: "The $q$-logarithmic zeta function",
  tags: [
    "zeta-function",
    "q-deformation",
    "information-theory",
    "reeb-flow",
    "dynamical-zeta",
    "critical-line",
  ],
  lean: {
    decl: "QOU.Information.qLogarithmicZeta",
    validation: "not_checked",
  },
  uses: [
    "def:operational-entropy",
    "rem:julia-set-reeb",
    "rem:discrete-planck-step",
    "def:planck-time",
  ],
  cites: [
    "ruelle1982",
  ],
});
