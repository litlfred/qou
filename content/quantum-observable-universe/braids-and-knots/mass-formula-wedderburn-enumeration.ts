import { remark } from "../../schema/builders";

export default remark({
  label: "rem:mass-formula-wedderburn-enumeration",
  title:
    "Every $\\lambda \\vdash n$ appears in the unified mass formula exactly once",
  interprets: "prop:unified-curvature-rank-mass-formula",
  uses: [
    "prop:unified-curvature-rank-mass-formula",
    "prop:plancherel-term-7-formulation",
    "prop:spectral-sequence-collapse",
    "prop:confinement-categorical",
    "prop:curvature-rank-gb-stratification",
  ],
  tags: [
    "completeness",
    "enumeration",
    "wedderburn",
    "plancherel",
    "all-blocks-used",
    "no-gaps",
  ],
});
