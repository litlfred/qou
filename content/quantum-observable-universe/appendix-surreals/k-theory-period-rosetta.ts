import { remark } from "../../schema/builders";

export default remark({
  label: "rem:k-theory-period-rosetta",
  title:
    "K-theory $\\leftrightarrow$ depth filtration Rosetta: Beilinson regulator matches iterated-integral grading on $\\mathcal{H}_q$",
  interprets: "rem:transcendental-accounting",
  uses: ["conj:cl3-zeta5-geometric-realization"],
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
