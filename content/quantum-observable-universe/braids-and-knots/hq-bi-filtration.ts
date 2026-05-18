import { definition } from "../../schema/builders";

export default definition({
  label: "def:hq-bi-filtration",
  title:
    "Knot-indexed bi-filtration $\\mathcal{H}_q^{(n, K)}$ on the substrate convolution algebra",
  lean: {
    ref: "qou:QOU.AlgebraicSubstrate.HqBiFiltration.BiFiltration",
    validation: "not_checked",
  },
  uses: [
    "def:frobenius-hopf-substrate",
    "conj:gb-depth-period-correspondence",
    "prop:explicit-central-idempotent",
    "rem:bring-embeddable-knots",
    "rem:chirality-period-pairing",
  ],
  cites: ["kontsevich1995", "bloch2000"],
  tags: [
    "bi-filtration",
    "depth-filtration",
    "knot-indexed",
    "graded-mikusinski",
    "framework-definition",
  ],
});
