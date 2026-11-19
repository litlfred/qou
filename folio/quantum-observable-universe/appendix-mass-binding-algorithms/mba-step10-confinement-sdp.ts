import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:confinement-sdp",
  title: "Confinement primal–dual conic program and canonical $T_w$ selection",
  uses: [
    "prop:operator-selection-lp",
    "prop:lp-dual-stability",
    "alg:frobenius-pairing",
  ],
  tags: [
    "mba",
    "step-10",
    "confinement-sdp",
    "canonical-tw",
    "primal-dual",
    "canonical-chain",
  ],
});
