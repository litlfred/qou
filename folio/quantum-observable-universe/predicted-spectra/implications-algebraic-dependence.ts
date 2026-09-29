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
    "rem:yekutieli-transcendence-shadow",
    "rem:formal-chain-transcendence",
    "prop:cs-evaluation-faithfulness",
  ],
  cites: ["yekutieli2010"],
});
