import { definition } from "../../schema/builders";

export default definition({
  label: "def:reeb-epsilon",
  title: "The Reeb infinitesimal $\\varepsilon$",
  lean: {
    decl: "QOU.AlgebraicSubstrate.ReebEpsilon",
    validation: "not_checked",
  },
  uses: [
    "def:categorical-reeb-derivation",
    "def:frobenius-hopf-substrate",
  ],
  tags: [
    "reeb",
    "infinitesimal",
    "derivation",
    "surreal",
    "categorical-primitive",
    "classical-limit",
  ],
});
