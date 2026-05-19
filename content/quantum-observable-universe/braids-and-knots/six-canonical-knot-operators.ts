import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:six-canonical-knot-operators",
  lean: {
    ref: "qou:QOU.CategoricalReeb.SixCanonicalKnotOperators",
    validation: "not_checked",
  },
  title:
    "Six canonical knot operators as Reeb-flow trajectories ($S_3$ realisation)",
  tags: [
    "knot-operator",
    "reeb-flow",
    "s3-galois",
    "braid-group",
    "garside-element",
    "coral-sectors",
  ],
  uses: [
    "def:q-reeb-flow-on-coral-coords",
    "def:coral-sector-coords",
    "rem:rho-s3-holonomy-exposition",
    "prop:lagrange-resolvent-transform",
    "prop:vertex-is-exceptional-divisor",
  ],
});
