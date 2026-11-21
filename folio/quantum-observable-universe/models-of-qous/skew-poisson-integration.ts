import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "caveat", date: "2026-11-21", body: "Lean now states the three sub-claims with an honest `sorry`; the three context fields that held them are deleted (round-trip audit pass 2, C17). The library context is opaque data, so the statement is not yet provable from it. \"Skewed-Poisson structure\" is not defined in the block, and sub-claim 3 calls the bialgebra compatibility the Frobenius relation; they are different identities." },
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:skew-poisson-integration",
  lean: { ref: "qou:QOU.Archimedean.skew_poisson_integration",
    validation: "not_checked",
  },
  title: "Integration of skewed-Poisson structures",
  uses: ["def:witt-vector-lift"],
  proofs: ["prf:skew-poisson-integration"],
});
