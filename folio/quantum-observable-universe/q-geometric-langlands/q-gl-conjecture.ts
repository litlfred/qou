import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:q-geometric-langlands",
  lean: { ref: "qou:QOU.QGeometricLanglands.QGeometricLanglandsConjecture", validation: "not_checked" },
  title: "$q$-Geometric Langlands correspondence",
  uses: [
    "def:q-hecke-eigensheaf",
    "def:q-langlands-dual",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([classical limit](#conj:q-gl-classical-limit))" },
  ],
  cites: ["frenkel2007", "aganagic2018"],
  tags: ["tier:keystone", "geometric-langlands", "q-deformation", "main-conjecture"],
});
