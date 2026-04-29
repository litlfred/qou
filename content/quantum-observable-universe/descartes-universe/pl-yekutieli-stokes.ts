import { remark } from "../../schema/builders";

export default remark({
  label: "rem:pl-yekutieli-stokes",
  interprets: "def:picard-lefschetz-thimble",
  title:
    "Picard--Lefschetz contour collapse as the archimedean realisation of non-abelian Stokes",
  chapter: "descartes-universe",
  cites: ["yekutieli2015", "witten2011"],
  uses: [
    "def:picard-lefschetz-thimble",
    "rem:yekutieli-stokes",
    "prop:topological-mass-formula",
    "prop:sw-period-thimble-equivalence",
  ],
  defines: [],
  tags: [
    "picard-lefschetz",
    "non-abelian-stokes",
    "yekutieli",
    "categorical-license",
    "archimedean",
    "topological-mass",
  ],
});
