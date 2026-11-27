import { remark } from "../../schema/builders";

export default remark({
  label: "rem:lean-lib-twisted-frobenius-hopf",
  title:
    "Community Library 2 (TwistedFrobeniusHopf): Nakayama-twisted Frobenius--Hopf algebras and Woronowicz differential calculi",
  interprets: "tbl:lean-community-libraries-dag",
  uses: ["tbl:lean-community-libraries-dag", "rem:lean-lib-hecke-temperley-lieb"],
  cites: ["kock2004", "woronowicz1989"],
  tags: ["lean-infrastructure", "reservoir", "frobenius-algebra", "hopf-algebra", "appendix"],
});
