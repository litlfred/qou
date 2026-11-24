import { remark } from "../../schema/builders";

export default remark({
  label: "rem:lean-lib-q-calculus",
  title:
    "Community Library 5 (QCalculus): Thomae--Jackson $q$-integrals, $q$-Pochhammer products, and Habiro expansions",
  interprets: "tbl:lean-community-libraries-dag",
  uses: ["tbl:lean-community-libraries-dag"],
  cites: ["gasper-rahman-2004", "andrews1976", "habiro2004cyclotomic"],
  tags: ["lean-infrastructure", "reservoir", "q-calculus", "habiro-ring", "appendix"],
});
