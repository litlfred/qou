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
  uses: ["thm:knot-mass-formula-unified"],
  computation: {
    engine: "python+mpmath",
    script: "computations/probes/gpmt_sign_block_qbeta_and_np_splitting_probe.py",
    witness: "computations/probes/gpmt-sign-block-qbeta-and-np-splitting.witness.json",
    status: "verified",
  },
});
