import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:six-canonical-knot-operators",
  lean: {
    ref: "qou:QOU.CategoricalReeb.boundary_perm_realises_S3",
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
    "color-sectors",
  ],
  uses: [
    "def:q-reeb-flow-on-color-coords",
    "rem:rho-s3-holonomy-exposition",
    "prop:vertex-is-exceptional-divisor",
  ],
  computation: {
    engine: "python",
    script: "computations/reeb_flow_garside_closed_form_verification.py",
    witness: "computations/reeb-flow-garside-closed-form-verification.witness.json",
    status: "verified",
  },
});
