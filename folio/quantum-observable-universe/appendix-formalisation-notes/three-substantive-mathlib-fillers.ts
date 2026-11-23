import { remark } from "../../schema/builders";

export default remark({
  label: "rem:three-substantive-mathlib-fillers",
  title:
    "Three substantive Mathlib gaps: BlochGroup quotient, $\\mathrm{Cl}_2$ pentagon, Faddeev-Kashaev limit",
  interprets: "rem:mass-tower-deeper-fillers",
  uses: ["rem:mass-tower-deeper-fillers"],
  cites: [
    "bloch2000",
    "suslin1991",
    "borel1974",
    "zagier1986",
    "faddeev1994",
    "kashiwara1991",
  ],
  tags: [
    "mathlib-filler",
    "substantive-gap",
    "bloch-group",
    "pentagon-identity",
    "faddeev-kashaev",
    "free-abelian-group",
    "lean-infrastructure",
  ],
});
