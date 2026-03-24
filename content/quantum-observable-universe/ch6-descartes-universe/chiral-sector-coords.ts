import { definition } from "../../schema/builders";

export default definition({
  label: "def:chiral-sector-coords",
  lean: { decl: "QOU.ChiralSectorCoords" },
  title: "Chiral sector coordinates $\\mathfrak{r},\\mathfrak{g},\\mathfrak{b}$",
  tags: ["descartes-universe", "chiral-sectors", "color-charge"],
  uses: [
    "def:exceptional-divisor",
    "def:substrate-parameter",
    "rem:chirality-trefoil",
  ],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/chiral-sector-coords-0.svg", blockIndex: 0, hash: "1c3e0203468f" },
  ],

});
