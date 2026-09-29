import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:q-geometric-langlands",
  lean: { ref: "qou:QOU.QGeometricLanglands.QGeometricLanglandsConjecture", validation: "not_checked" },
  title: "$q$-Geometric Langlands correspondence",
  uses: [
    "def:q-hecke-eigensheaf",
    "def:q-langlands-dual",
  ],
  cites: ["frenkel2007", "aganagic2018"],
  tags: ["tier:keystone", "geometric-langlands", "q-deformation", "main-conjecture"],
});
