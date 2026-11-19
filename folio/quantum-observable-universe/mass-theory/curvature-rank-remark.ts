import { remark } from "../../schema/builders";

export default remark({
  label: "rem:curvature-rank-remark",
  title: "Curvature-rank as a reduction count",
  interprets: "def:curvature-rank",
  uses: [
    "def:curvature-rank",
    "def:hecke-curvature-2-cocycle",
  ],
});
