import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:ramified-disc-fusion",
  lean: {
    ref: "qou:QOU.BraidsKnots.RamifiedDiscFusion",
    validation: "not_checked",
  },
  title: "Ramified-disc fusion at the foundry boundary",
  tags: [
    "ramified-cover",
    "monodromy",
    "exceptional-divisor",
    "s3-galois",
    "boundary-disc",
  ],
  uses: [
    "def:reeb-bundle",
    "def:color-sector-coords",
    "rem:rho-s3-holonomy-exposition",
  ],
});
