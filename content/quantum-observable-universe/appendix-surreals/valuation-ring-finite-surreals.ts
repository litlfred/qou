import { definition } from "../../schema/builders";

export default definition({
  label: "def:valuation-ring-finite-surreals",
  lean: {
    decl: "QOU.AppendixSurreals.FiniteValuationRing",
    validation: "not_checked",
  },
  title:
    "Valuation ring $\\mathcal{O} \\subset \\mathbf{No}$ of finite surreals",
  tags: [
    "surreal-numbers",
    "valuation-ring",
    "finite-surreals",
    "infinitesimals",
    "standard-part",
  ],
  uses: [
    "def:standard-part-functor",
  ],
  cites: ["conway1976", "robinson1966", "ehrlich2012"],
});
