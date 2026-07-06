import { remark } from "../../schema/builders";

export default remark({
  label: "rem:elliptic-stability-locus",
  interprets: "prop:integer-stability",
  title:
    "The nuclear degeneracy locus is an elliptic curve over the Bring's surface",
  lean: {
    ref: "qou:QOU.EllipticStabilityLocus.EllipticStabilityLocus",
    validation: "not_checked",
  },
  tags: [
    "elliptic-curve",
    "stability",
    "diophantine",
    "color-fibration",
    "coulomb",
    "pairing",
    "bring-surface",
  ],
  uses: [
    "prop:integer-stability",
    "def:color-tube-fibers",
  ],
});
