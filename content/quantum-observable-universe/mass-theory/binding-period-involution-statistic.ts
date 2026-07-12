import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:binding-period-involution-statistic",
  lean: {
    ref: "qou:QOU.Mass.BindingInvolutionStatistic.binding_period_involution_statistic_four",
  },
  title:
    "The balanced dimension sum is the involution generating function for $2\\,\\mathrm{maj} + \\mathrm{content} \\circ \\mathrm{RSK}$",
  proofs: ["prf:binding-period-involution-statistic"],
});
