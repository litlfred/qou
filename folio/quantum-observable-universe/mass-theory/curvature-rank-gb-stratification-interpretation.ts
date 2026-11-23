import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:curvature-rank-gb-stratification",
  label: "rem:curvature-rank-gb-stratification-interpretation",
  title: "Geometric reading: curvature-rank strata as Seifert-surface blow-up loci",
  uses: ["conj:curvature-rank-gb-stratification", "conj:topological-mass-formula"],
});
