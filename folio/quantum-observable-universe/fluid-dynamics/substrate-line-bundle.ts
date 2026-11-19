import { definition } from "../../schema/builders";

export default definition({
  label: "def:substrate-line-bundle",
  title:
    "The aether line bundle and the $\\mathbb{G}_m$-family of differentials",
  lean: {
    ref: "qou:QOU.FluidDynamics.SubstrateLineBundle",
    validation: "not_checked",
  },
  uses: ["def:substrate-parameter"],
  tags: [
    "line-bundle",
    "multiplicative-group",
    "projective",
    "substrate",
    "family",
  ],
});
