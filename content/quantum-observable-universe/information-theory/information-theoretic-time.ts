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
  lean: { ref: "qou:QOU.informationTheoreticTime",
    validation: "leanok",
  },
  uses: [
    "prop:reeb-operations-per-planck",
    "prop:ordering-jet-compatibility",
  ],
});
