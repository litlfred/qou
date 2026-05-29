import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:reading-a-conditional-linking-weight",
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
    "adams1985",
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
