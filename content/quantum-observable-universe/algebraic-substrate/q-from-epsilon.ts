import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-from-epsilon",
  title: "The substrate parameter $q$ as $1 + \\varepsilon$",
  lean: {
    decl: "QOU.AlgebraicSubstrate.QFromEpsilon",
    validation: "not_checked",
  },
  uses: [
    "def:reeb-epsilon",
    "def:substrate-parameter-planck",
  ],
  tags: [
    "substrate-parameter",
    "surreal",
    "categorical-primitive",
    "q-expansion",
    "classical-limit",
  ],
});
