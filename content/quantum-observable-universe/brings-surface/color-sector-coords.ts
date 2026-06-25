import { definition } from "../../schema/builders";

export default definition({
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
