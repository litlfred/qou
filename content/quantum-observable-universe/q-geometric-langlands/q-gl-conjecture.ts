import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-geometric-langlands",
  lean: { ref: "qou:QOU.QGeometricLanglands.QGeometricLanglandsConjecture", validation: "not_checked" },
  title: "$q$-Geometric Langlands correspondence",
  uses: [
    "def:q-hecke-eigensheaf",
    "def:q-langlands-dual",
  ],
  cites: ["frenkel2007", "aganagic2018"],
  tags: ["geometric-langlands", "q-deformation", "main-conjecture"],
});
