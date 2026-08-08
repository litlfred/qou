import { remark } from "../../schema/builders";

export default remark({
  label: "rem:mass-tower-deeper-fillers",
  title:
    "Deeper conditional-class fillers: Term-7 enumeration, Demazure sub-crystals, KL classical limit, BlochGroup carrier, Cl_2 pentagon",
  interprets: "prop:crystal-basis-resolves-mass-tower-open-problems",
  uses: [
    "prop:type-b-folded-crystal-combinatorics",
    "rem:bloch-wigner-mathlib-filler",
  ],
  cites: [
    "borel1974",
    "bloch2000",
    "suslin1991",
    "kashiwara1991",
    "khovanovlauda2009",
    "zagier1986",
  ],
  tags: [
    "mathlib-filler",
    "deeper-scaffolding",
    "height-6-partition",
    "demazure-sub-crystal",
    "kazhdan-lusztig",
    "bloch-group",
    "pentagon-identity",
    "lean-infrastructure",
  ],
});
