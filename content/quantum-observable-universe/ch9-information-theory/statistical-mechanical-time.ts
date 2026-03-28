import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:information-theoretic-time",
  label: "rem:statistical-mechanical-time",
  title: "Statistical mechanical emergence of continuous time",
  tags: [
    "statistical-mechanics",
    "planck-time",
    "information-theory",
    "reeb-flow",
    "thermodynamic-limit",
    "julia-set",
  ],
  uses: [
    "def:information-theoretic-time",
    "def:planck-time",
    "prop:reeb-operations-per-planck",
    "def:quantum-planck-constant",
    "rem:julia-set-reeb",
    "rem:discrete-planck-step",
    "rem:jet-planck-steps",
    "ex:q-reeb-flow",
  ],
});
