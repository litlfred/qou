import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-from-epsilon",
  title: "The aether parameter $q$ as $1 + \\varepsilon$",
  lean: {
    ref: "qou:QOU.AlgebraicSubstrate.QFromEpsilon",
    validation: "not_checked",
  },
  uses: ["def:reeb-epsilon"],
  tags: [
    "substrate-parameter",
    "surreal",
    "categorical-primitive",
    "q-expansion",
    "classical-limit",
  ],
});
