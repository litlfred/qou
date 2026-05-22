import { definition } from "../../schema/builders";

export default definition({
  label: "def:coral-sector-coords",
  lean: { ref: "qou:QOU.CoralSectorCoords", validation: "not_checked" },
  title: "Coral sector coordinates $\\mathfrak{r},\\mathfrak{g},\\mathfrak{b}$",
  tags: ["descartes-universe", "coral-sectors", "colour-charge"],
  uses: [
    "def:exceptional-divisor",
    "def:substrate-parameter",
    "rem:chirality-trefoil",
  ],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/coral-sector-coords-0.svg", blockIndex: 0, hash: "1c3e0203468f" },
  ],

});
