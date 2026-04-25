import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:curvature-rank-delta-cs",
  title: "$\\delta_{CS} = \\hbar_q^4 \\cdot [5]_q$ as the depth-4 stratum of the curvature 2-cocycle",
  lean: {
    ref: "qou:QOU.WedderburnMass.curvature_rank_delta_cs",
    validation: "not_checked",
  },
  uses: [
    "prop:curvature-rank-gb-stratification",
    "prop:plancherel-term-7-formulation",
    "prop:exterior-square-borromean",
    "prop:alpha-em-categorical-trace",
  ],
});
