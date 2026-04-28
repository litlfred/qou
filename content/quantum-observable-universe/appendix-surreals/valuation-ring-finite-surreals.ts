import { remark } from "../../schema/builders";

export default remark({
  label: "rem:valuation-ring-finite-surreals",
  title:
    "Standard-part as valuation-ring projection $\\mathcal{O} \\twoheadrightarrow \\mathcal{O}/\\mathfrak{m} \\cong \\mathbb{R}$",
  tags: [
    "surreal-numbers",
    "valuation-ring",
    "finite-surreals",
    "standard-part",
    "cross-reference",
  ],
  interprets: "def:standard-part-functor",
  uses: [
    "def:standard-part-functor",
  ],
  cites: ["conway1976", "robinson1966", "ehrlich2012"],
});
