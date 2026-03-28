import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:reeb-operations-per-planck",
  title: "Reeb operations per Planck unit",
  tags: [
    "planck-time",
    "reeb-flow",
    "julia-set",
    "discrete-time",
    "information-theory",
  ],
  uses: [
    "def:planck-time",
    "def:quantum-planck-constant",
    "rem:julia-set-reeb",
    "def:substrate-parameter",
    "ex:q-reeb-flow",
    "rem:discrete-planck-step",
    "prop:local-substrate-q",
  ],
});
