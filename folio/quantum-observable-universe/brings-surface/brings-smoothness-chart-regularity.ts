import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:brings-smoothness-resolution",
  label: "rem:brings-smoothness-chart-regularity",
  title: "Regularity of the Briggs--Klein chart",
  tags: ["brings-surface", "smooth", "resolution", "branch-point", "color"],
  uses: [
    "prop:brings-smoothness-resolution",
    "def:briggs-klein-chart",
  ],
});
