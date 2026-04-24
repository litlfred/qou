import { definition } from "../../schema/builders";

export default definition({
  label: "def:reeb-epsilon",
  title: "The Reeb infinitesimal $\\varepsilon$",
  lean: {
    decl: "QOU.AlgebraicSubstrate.ReebEpsilon",
    file: "lean/QOU/AlgebraicSubstrate/ReebEpsilon.lean",
    validation: "not_checked",
  },
  uses: [
    "def:categorical-reeb-derivation",
    "rem:calculus-up-to-epsilon",
    "def:surreal-blowup-calculus",
  ],
  tags: [
    "reeb",
    "infinitesimal",
    "derivation",
    "surreal",
    "categorical-primitive",
    "classical-limit",
  ],
  cites: ["conway1976", "gonshor1986"],
});
