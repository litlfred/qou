import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:ring-closure-barrier-quantitative",
  title:
    "Quantitative ring-closure barrier $\\Delta E_{\\mathrm{closure}}(N)$",
  tags: [
    "ring-closure",
    "barrier",
    "alexander-polynomial",
    "energy-prediction",
    "even-N",
  ],
  lean: { ref: "qou:QOU.Organic.ringClosureBarrierQuantitative",
    validation: "not_checked",
  },
  uses: [
    "lem:alexander-T2N-closed-form",
    "prop:molecular-crossing-quantum",
    "prop:ring-closure-barrier",
  ],
  cites: [],
});
