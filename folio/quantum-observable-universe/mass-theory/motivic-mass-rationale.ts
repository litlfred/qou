import { remark } from "../../schema/builders";

export default remark({
  label: "rem:motivic-mass-rationale",
  title: "Why a motivic measure: singular intermediate states and the archimedean realization",
  interprets: "def:motivic-mass-measure",
  tags: ["motivic", "mass", "lefschetz", "arc-space"],
  uses: [
    "def:motivic-mass-measure",
    "prop:mass-endomorphism-tower",
    "conj:topological-mass-formula",
    "def:archimedean-realization-functor",
  ],
});
