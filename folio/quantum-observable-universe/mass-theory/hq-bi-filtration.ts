import { definition } from "../../schema/builders";

export default definition({
  label: "def:hq-bi-filtration",
  title:
    "Knot-indexed bi-filtration $\\mathcal{H}_q^{(n, K)}$ on the aether convolution algebra",
  lean: {
    ref: "qou:QOU.AlgebraicSubstrate.HqBiFiltration.BiFiltration",
    validation: "not_checked",
  },
  uses: [
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
  authorNotes: [
    {
      kind: "status",
      body: "**Definition block.** Provides the framework symbol; downstream\nblocks make claims about its structure. No proof obligations here\nbeyond well-definedness, which follows from the\nexistence of the depth filtration ([keystone](#conj:gb-depth-period-correspondence))\nand the explicit central idempotents\n([`prop:explicit-central-idempotent`](#prop:explicit-central-idempotent)).",
    },
  ],
});
