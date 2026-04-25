import { remark } from "../../schema/builders";

export default remark({
  interprets: "thm:knot-mass-formula-unified",
  label: "rem:np-discrepancy-resolution",
  title:
    "n/p discrepancy resolution: calibration-dependent, not structural",
  tags: [
    "proton",
    "neutron",
    "mass-splitting",
    "calibration",
    "beta-decay",
    "interpretation",
  ],
  uses: [
    "thm:knot-mass-formula-unified",
    "prop:categorical-mass-markov",
    "prop:partition-sum-proton-residual",
    "thm:frobenius-codim-universal",
    "prop:mass-endomorphism-tower",
    "prop:figure-eight-bw-coefficients",
  ],
});
