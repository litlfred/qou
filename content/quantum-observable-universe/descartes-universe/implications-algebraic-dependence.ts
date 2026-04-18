import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:hyperbolic-volume-transcendence",
  label: "rem:implications-algebraic-dependence",
  title:
    "Implications if the QOU volumes are algebraically dependent",
  tags: [
    "transcendence",
    "algebraic-dependence",
    "yekutieli",
    "tower-collapse",
    "falsification",
  ],
  uses: [
    "conj:hyperbolic-volume-transcendence",
    "prop:yekutieli-lifting",
    "prop:cs-evaluation-faithfulness",
    "prop:volume-tower-decomposition",
  ],
  cites: ["yekutieli2010"],
});
