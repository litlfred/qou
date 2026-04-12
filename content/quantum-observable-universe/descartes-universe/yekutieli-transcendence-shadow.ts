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
    "def:quantum-characteristic-classes",
    "prop:cosimplicial-crossed-groupoid",
    "prop:yekutieli-lifting",
  ],
  cites: ["yekutieli2010"],
});
