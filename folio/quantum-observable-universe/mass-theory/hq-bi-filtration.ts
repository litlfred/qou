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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): Three downstream conjectures\npopulate it:\n\n- [Joint motivic-Galois $\\times$ braid-group action on the bi-filtration $\\mathcal{H}_q^{(n, K)}$](#conj:joint-galois-braid-action)\n  — the symmetry group acting on $\\mathcal{H}_q^{(n, K)}$.\n- [Placement of paper's existing knot-indexed convolutions in the bi-filtration grid](#prop:knot-indexed-convolution-grid)\n  — placement of paper's existing knot-indexed convolutions\n  ($\\mathrm{Lk}_R^{(k)}$, $\\bowtie_K$, Markov trace, Hoefsmit pairing,\n  Higgs-vev coupling) into the $(n, K)$-grid.\n- [K-theory $\\leftrightarrow$ depth filtration Rosetta](#rem:k-theory-period-rosetta)\n  — Beilinson regulator on $K_{2n-1}^{\\mathrm{ind}}(\\overline{\\mathbb{Q}})$\n  matches the depth-$n$ axis." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): Inherited from\n[GS-depth $\\leftrightarrow$ Goncharov period-depth correspondence](#conj:gb-depth-period-correspondence):" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([depth correspondence](#conj:gb-depth-period-correspondence))" },
    {
      kind: "status",
      body: "**Definition block.** Provides the framework symbol; downstream\nblocks make claims about its structure. No proof obligations here\nbeyond well-definedness, which follows from the\nexistence of the depth filtration ([keystone](#conj:gb-depth-period-correspondence))\nand the explicit central idempotents\n([`prop:explicit-central-idempotent`](#prop:explicit-central-idempotent)).",
    },
  ],
});
