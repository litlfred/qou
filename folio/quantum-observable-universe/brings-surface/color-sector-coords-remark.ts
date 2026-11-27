import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:color-sector-coords",
  label: "rem:color-sector-coords-remark",
  title: "The color twist and the tiling of the exceptional divisor",
  uses: ["def:color-sector-coords", "def:exceptional-divisor", "rem:chirality-trefoil"],
});
