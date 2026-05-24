import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:operator-selection-lp",
  label: "rem:sdp-as-thimble-flow",
  title: "SDP/LP selection as Picard--Lefschetz steepest descent",
  uses: [
    "prop:confinement-sdp",
    "prop:mass-coefficient-shadow-price",
    "rem:picard-lefschetz-thimble",
    "conj:gb-reduction-pl-thimble-bijection",
  ],
  cites: ["witten2011", "neumann-zagier1985"],
  tags: [
    "interpretation",
    "picard-lefschetz",
    "sdp-duality",
    "shadow-price",
    "thimble",
    "geometric-face",
    "encounter",
  ],
});
