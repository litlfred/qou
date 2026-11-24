import { remark } from "../../schema/builders";

export default remark({
  label: "rem:lean-lib-toric-conic-opt",
  title:
    "Community Library 3 (ToricConicOpt): Ordered-field conic duality, symmetry-reduced certificates, and toric Gröbner bases",
  interprets: "tbl:lean-community-libraries-dag",
  uses: ["tbl:lean-community-libraries-dag", "rem:lean-lib-hecke-temperley-lieb"],
  cites: ["gatermann-parrilo2004", "conti-traverso1991", "sturmfels-thomas1997"],
  tags: ["lean-infrastructure", "reservoir", "convex-optimization", "toric-ideals", "appendix"],
});
