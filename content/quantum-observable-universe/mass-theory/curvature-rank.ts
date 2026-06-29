import { definition } from "../../schema/builders";

export default definition({
  label: "def:curvature-rank",
  title: "Curvature-rank $r(T_w)$",
  lean: {
    ref: "qou:QOU.WedderburnMass.curvatureRank",
    validation: "not_checked",
  },
  uses: ["def:hecke-curvature-2-cocycle"],
  cites: ["bokutchen2014"],
  tags: [
    "curvature-rank",
    "gb-filtration",
    "normal-form",
    "hecke",
    "reduction",
  ],
});
