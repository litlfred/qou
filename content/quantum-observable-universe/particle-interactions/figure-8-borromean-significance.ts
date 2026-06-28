import { remark } from "../../schema/builders";

export default remark({
  label: "rem:figure-8-borromean-significance",
  title:
    "Significance of the figure-8 cross-check for the Borromean baryon programme",
  interprets: "prop:three-calibration-inputs",
  uses: [
    "prop:three-calibration-inputs",
    "conj:borromean-baryon-mass-formula",
  ],
  tags: [
    "figure-8-knot",
    "borromean",
    "baryon-mass",
    "skein-contribution",
    "topological-mass",
  ],
});
