import { conjecture } from "../../schema/builders";

export default conjecture({
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-16",
      body: "Demoted from proposition to conjecture on owner ruling (decision card, 2026-11-16). The former proof assumed that each central idempotent $e_\\lambda$ carries a GB-filtration depth indexed by the partition, an identification it said was \"not stated there and assumed here\", and it never derived the coefficients $\\alpha_k$. The Lean reference is a `def` that takes the decomposition as its definition. The former proof is kept as a sketch remark.",
    },
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "conj:unified-curvature-rank-mass-formula",
  title: "Unified curvature-rank mass formula (clarifies six terms + Term 7)",
  lean: {
    ref: "qou:QOU.WedderburnMass.unified_curvature_rank_mass",
    validation: "not_checked",
  },
  uses: ["prop:plancherel-term-7-formulation"],
});
