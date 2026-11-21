import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The three sectors correspond to the three copies of $S_3 \\subset S_5$ in [chirality and trefoil](#rem:chirality-trefoil): $\\mathfrak{r}$ constitutes the first, $\\mathfrak{g}$ the second, and $\\mathfrak{b}$ the third." },
  ],
  label: "def:color-sector-coords",
  lean: { ref: "qou:QOU.ColorSectorCoords", validation: "not_checked" },
  title: "Color sector coordinates $\\mathfrak{r},\\mathfrak{g},\\mathfrak{b}$",
  tags: ["archimedean-universe", "color-sectors", "colour-charge"],
  uses: [
    "def:exceptional-divisor",
    "def:substrate-parameter",
    "rem:chirality-trefoil",
  ],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/color-sector-coords-0.svg", blockIndex: 0, hash: "1c3e0203468f" },
  ],

});
