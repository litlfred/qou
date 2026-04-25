import { remark } from "../../schema/builders";

export default remark({
  label: "rem:confinement-curvature-rank",
  title: "Curvature-rank as confinement layer (categorical reading of confinement)",
  interprets: "prop:confinement-categorical",
  uses: [
    "prop:confinement-categorical",
    "prop:curvature-rank-gb-stratification",
    "prop:unified-curvature-rank-mass-formula",
    "prop:plancherel-term-7-formulation",
  ],
});
