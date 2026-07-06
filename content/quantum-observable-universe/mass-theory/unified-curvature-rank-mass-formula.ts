import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:unified-curvature-rank-mass-formula",
  title: "Unified curvature-rank mass formula (clarifies six terms + Term 7)",
  lean: {
    ref: "qou:QOU.WedderburnMass.unified_curvature_rank_mass",
    validation: "not_checked",
  },
  uses: ["prop:plancherel-term-7-formulation"],
});
