import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:s4-s3-half-symmetric-projection",
  title:
    "Half-symmetric $H_4$ projection extracts one octahedral cell via $S_4 \\downarrow S_3$ branching",
  lean: { ref: "qou:QOU.BraidsAndKnots.s4_s3_half_symmetric_projection" },
  uses: ["conj:borromean-baryon-mass-formula"],
  cites: [
    "adams1985hyperbolic",
    "wenzl1988",
    "james1984representation",
  ],
  computation: {
    engine: "python",
    script:
      "computations/lambda_scale_rd_h4_half_symmetric.py",
    witness:
      "computations/lambda-scale-rd-h4-half-symmetric.witness.json",
    status: "verified",
  },
  tags: [
    "branching-rule",
    "half-symmetric",
    "S4-S3",
    "bijection",
    "octahedral-cell",
    "borromean",
    "vol-density-refinement",
  ],
});
