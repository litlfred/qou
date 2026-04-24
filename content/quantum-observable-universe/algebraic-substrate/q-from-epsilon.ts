import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-from-epsilon",
  title: "The substrate parameter $q$ as $1 + \\varepsilon$",
  lean: {
    decl: "QOU.AlgebraicSubstrate.QFromEpsilon",
    file: "lean/QOU/AlgebraicSubstrate/QFromEpsilon.lean",
    validation: "not_checked",
  },
  uses: [
    "def:reeb-epsilon",
    "conj:infinitesimal-frobenius",
  ],
  tags: [
    "substrate-parameter",
    "surreal",
    "categorical-primitive",
    "q-expansion",
    "classical-limit",
  ],
});
