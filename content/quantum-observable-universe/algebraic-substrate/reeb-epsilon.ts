import { definition } from "../../schema/builders";

export default definition({
  label: "def:reeb-epsilon",
  title: "The Reeb infinitesimal $\\varepsilon$",
  lean: {
    ref: "qou:QOU.AlgebraicSubstrate.ReebEpsilon",
    validation: "not_checked",
  },
  uses: [
    "def:categorical-reeb-derivation",
    "rem:calculus-up-to-epsilon",
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
