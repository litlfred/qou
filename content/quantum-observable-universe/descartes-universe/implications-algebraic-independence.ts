import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:hyperbolic-volume-transcendence",
  label: "rem:implications-algebraic-independence",
  title:
    "Implications if the QOU volumes are algebraically independent",
  tags: [
    "transcendence",
    "algebraic-independence",
    "yekutieli",
    "milnor",
    "confinement",
  ],
  uses: [
    "conj:hyperbolic-volume-transcendence",
    "prop:yekutieli-lifting",
    "prop:cs-evaluation-faithfulness",
    "prop:volume-tower-decomposition",
  ],
  cites: ["yekutieli2010"],
});
