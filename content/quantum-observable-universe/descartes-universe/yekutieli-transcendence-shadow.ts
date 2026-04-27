import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:hyperbolic-volume-transcendence",
  label: "rem:yekutieli-transcendence-shadow",
  title:
    "Algebraic independence as the transcendence shadow of non-vanishing Yekutieli obstructions",
  tags: [
    "yekutieli",
    "obstruction",
    "cosimplicial",
    "transcendence",
    "brane-tower",
    "algebraic-independence",
  ],
  uses: [
    "conj:hyperbolic-volume-transcendence",
    "prop:cosimplicial-crossed-groupoid",
  ],
  cites: ["yekutieli2010"],
});
