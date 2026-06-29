import { remark } from "../../schema/builders";

/**
 * Interpretive follow-on to prop:shell-filling-rule: the dual variable y_0 as
 * braid-framework electronegativity, and the ILP attachment generator
 * alternation (σ_0 vs σ_1) as the Hecke manifestation of Hund's rule.
 */
export default remark({
  label: "rem:shell-filling-electronegativity-ilp",
  title: "Electronegativity and ILP generator alternation",
  interprets: "prop:shell-filling-rule",
  uses: ["def:electron-shell-braid-capacity"],
  tags: ["electronegativity", "ILP", "Hund", "generator-alternation", "LP-dual"],
});
