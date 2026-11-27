import { remark } from "../../schema/builders";

export default remark({
  label: "rem:lean-lib-braid-knot-octonion",
  title:
    "Community Library 6 (BraidKnotOctonion): Artin braid towers, Bring's curve $\\Sigma_4$, and octonionic $G_2 / \\mathrm{SU}(3)$ algebra",
  interprets: "tbl:lean-community-libraries-dag",
  uses: ["tbl:lean-community-libraries-dag", "rem:lean-lib-hecke-temperley-lieb"],
  cites: ["birman1974", "baez2002", "bring1786", "braden-northover-2012"],
  tags: ["lean-infrastructure", "reservoir", "braid-group", "brings-curve", "octonions", "appendix"],
});
