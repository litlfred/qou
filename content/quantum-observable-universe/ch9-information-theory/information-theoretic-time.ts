import { definition } from "../../schema/builders";

export default definition({
  label: "def:information-theoretic-time",
  title: "Information-Theoretic Time",
  tags: [
    "information-theory",
    "planck-time",
    "discrete-time",
    "statistical-mechanics",
    "reeb-flow",
    "julia-set",
  ],
  lean: {
    decl: "QOU.informationTheoreticTime",
    validation: "leanok",
  },
  uses: [
    "def:planck-time",
    "def:quantum-planck-constant",
    "prop:reeb-operations-per-planck",
    "rem:julia-set-reeb",
    "prop:ordering-jet-compatibility",
    "ex:q-reeb-flow",
    "def:substrate-parameter",
  ],
});
