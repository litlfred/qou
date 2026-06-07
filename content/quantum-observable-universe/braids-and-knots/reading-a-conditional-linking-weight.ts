import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:reading-a-conditional-linking-weight",
  title:
    "Reading-A linking-weight: $\\mathrm{linkingWeight}(q) = \\tfrac{5}{2} + (-G) h^2$ (conditional)",
  lean: {
    ref: "qou:QOU.BraidKnot.ReadingAValidAtH2",
    validation: "not_checked",
  },
  uses: [
    "thm:lambda-scale-substrate-form",
  ],
  cites: [
    "adams1985hyperbolic",
    "yekutieli2015",
  ],
  tags: [
    "linking-weight",
    "reading-a",
    "borromean",
    "conjecture",
    "h2-coefficient",
    "open-problem",
    "ppm-coincidence-basin",
  ],
});
