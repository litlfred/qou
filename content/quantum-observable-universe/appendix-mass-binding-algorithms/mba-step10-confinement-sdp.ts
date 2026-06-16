import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:confinement-sdp",
  title: "Confinement SDP and canonical $T_w$",
  uses: [
    "prop:operator-selection-lp",
  ],
  computation: {
    engine: "python+numpy+cvxpy",
    script: "computations/confinement-operator-selection.py",
    witness: "computations/confinement-operator-selection.witness.json",
    status: "verified",
  },
  tags: [
    "mba",
    "step-10",
    "confinement-sdp",
    "canonical-tw",
    "lp-dual",
    "canonical-chain",
  ],
});
