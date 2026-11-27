import { remark } from "../../schema/builders";

export default remark({
  label: "rem:lean-lib-hecke-temperley-lieb",
  title:
    "Community Library 1 (HeckeTemperleyLieb): Iwahori--Hecke rewriting, Markov radicals, and Young--Hoefsmit representations",
  interprets: "tbl:lean-community-libraries-dag",
  uses: ["tbl:lean-community-libraries-dag"],
  cites: ["jones1987", "wenzl1988", "kangleeleeoh2002", "hoefsmit1974", "ram1991"],
  tags: ["lean-infrastructure", "reservoir", "hecke-algebra", "temperley-lieb", "appendix"],
});
