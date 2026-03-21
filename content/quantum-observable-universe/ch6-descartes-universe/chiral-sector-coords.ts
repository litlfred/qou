import { definition } from "../../schema/builders";

export default definition({
  label: "def:chiral-sector-coords",
  title: "Chiral sector coordinates $\\mathfrak{r},\\mathfrak{g},\\mathfrak{b}$",
  tags: ["descartes-universe", "chiral-sectors", "color-charge"],
  uses: [
    "def:exceptional-divisor",
    "def:substrate-parameter",
    "rem:chirality-trefoil",
  ],
});
