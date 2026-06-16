import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:lp-sdp-dual-emission",
  title: "LP/SDP dual-emission contract (first-class infra)",
  uses: [
    "prop:operator-selection-lp",
  ],
  computation: {
    engine: "python+numpy+cvxpy",
    script: "computations/lp_dual_witness_validator.py",
    status: "verified",
  },
  tags: [
    "mba",
    "sidecar",
    "lp-dual",
    "sdp-dual",
    "witness-contract",
    "ci-gate",
  ],
});
