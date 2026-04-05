import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:reeb-equidistribution",
  title:
    "Weyl equidistribution of the Reeb phase under torsion avoidance",
  uses: [
    "def:categorical-reeb-derivation",
    "rem:substrate-gm-torsion",
    "def:reeb-bundle",
    "prop:reeb-operations-per-planck",
    "def:weight-decomposition",
  ],
  tags: [
    "reeb-flow",
    "equidistribution",
    "weyl",
    "torsion-avoidance",
    "ergodic",
    "collatz",
  ],
});
