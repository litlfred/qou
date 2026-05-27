import { remark } from "../../schema/builders";

export default remark({
  label: "rem:k-theory-period-rosetta",
  title:
    "K-theory $\\leftrightarrow$ depth filtration Rosetta: Beilinson regulator matches iterated-integral grading on $\\mathcal{H}_q$",
  interprets: "rem:transcendental-accounting",
  uses: [
    "prop:gb-depth-period-correspondence",
    "rem:transcendental-accounting",
    "def:hq-bi-filtration",
    "prop:joint-galois-braid-action",
    "prop:cl3-zeta5-geometric-realization",
    "prop:bring-figure-eight-depth-2-witness",
    "prop:bring-trilog-depth-3-witness",
  ],
  cites: ["bloch2000", "kontsevich1995", "zagier1986"],
  tags: [
    "k-theory",
    "beilinson-regulator",
    "borel-theorem",
    "k_3-indecomposable",
    "rosetta",
    "graded-mikusinski",
    "external-language",
  ],
});
