import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:curvature-rank-gb-stratification",
  label: "rem:curvature-rank-gb-stratification-interpretation",
  title: "Geometric reading: curvature-rank strata as Seifert-surface blow-up loci",
  uses: ["prop:curvature-rank-gb-stratification", "prop:topological-mass-formula"],
});
