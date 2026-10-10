import { remark } from "../../schema/builders";

export default remark({
  label: "rem:surreal-squeeze-interpretation",
  title: "Interpretation: cost dominates budget, and the downstream bounds",
  interprets: "lem:surreal-squeeze",
  uses: ["lem:surreal-squeeze"],
  tags: [
    "surreal",
    "squeeze",
    "error-bounds",
    "millennium-problem",
    "classical-limit",
  ],
});
