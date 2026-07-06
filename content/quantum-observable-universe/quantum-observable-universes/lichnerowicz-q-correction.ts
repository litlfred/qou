import { remark } from "../../schema/builders";

export default remark({
  label: "rem:lichnerowicz-q-correction",
  interprets: "prop:categorical-lichnerowicz",
  title:
    "The $\\tfrac14\\mathrm{Sc}_q$ correction term and its vanishing on the Bring background",
  tags: ["lichnerowicz", "q-laplacian", "q-anomaly", "scalar-curvature"],
  uses: [
    "prop:categorical-lichnerowicz",
    "rem:q-laplacian-expansion",
    "ex:categorical-reeb-brings",
  ],
});
