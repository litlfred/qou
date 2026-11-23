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
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-21",
      body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner: fix issues): The [standard-part map](#def:standard-part-functor) $\\mathrm{st} : \\mathbf{No}_{\\mathrm{fin}} \\to \\mathbb{R}$ admits (the definition of the standard-part map is now stated inline, copied from the later definition block).",
    },
    {
      kind: "status",
      body: "The Lean infrastructure lives in\n`QOU.AppendixSurreals.Basic`:\n\n- `IsFinite` (= membership in $\\mathcal{O}$)\n- `IsInfinitesimal` (= membership in $\\mathfrak{m}$)\n- `standardPart` (the quotient projection $\\mathrm{st}$)\n- `isFinite_decomposition` (proves $\\mathcal{O} = \\mathbb{R}\n  \\oplus \\mathfrak{m}$ as $\\mathbb{R}$-vector spaces via\n  Dedekind-sSup construction)\n- `standardPart_add`, `standardPart_mul` (proves the ring-hom\n  property)\n\nThe valuation-ring and maximal-ideal as `Subring`/`Ideal`\nobjects are not yet formalised — this would be a\nstraightforward follow-up given the existing predicates.",
    },
  ],
});
