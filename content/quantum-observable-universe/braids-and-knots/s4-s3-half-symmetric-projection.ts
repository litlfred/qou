import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:s4-s3-half-symmetric-projection",
  title:
    "Half-symmetric $H_4$ projection extracts one octahedral cell via $S_4 \\downarrow S_3$ branching",
  lean: { ref: "qou:QOU.BraidsAndKnots.s4_s3_half_symmetric_projection" },
  uses: [
    "conj:borromean-baryon-mass-formula",
    "def:frobenius-hopf-substrate",
  ],
  cites: [
    "adams1985hyperbolic",
    "wenzl1988",
    "james1984representation",
  ],
  tags: [
    "branching-rule",
    "half-symmetric",
    "S4-S3",
    "bijection",
    "octahedral-cell",
    "borromean",
    "geom-full-refinement",
  ],
});
