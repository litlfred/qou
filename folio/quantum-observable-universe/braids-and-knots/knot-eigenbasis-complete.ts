import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-15",
      body: "Corrected on owner ruling (2026-11-15). Part (1) said H_n = End_{B_n}(V^{⊗n}); H_n maps onto the Temperley–Lieb quotient TL_n, which is the SU_q(2) commutant. Part (3) built the direct limit from inclusions induced by the unit η: 1 → V, which is the zero map since Hom(1, V) = 0 for the fundamental; it now uses x ↦ x ⊗ v₀, which is H_n-equivariant but not SU_q(2)-equivariant. The Lean `KnotEigenbasisData` still carries completeness as a field (self-assuming); that is for the Lean-foundations work.",
    },
    {
      kind: "refined-framing",
      date: "2026-11-15",
      body: "Rescoped on owner ruling (2026-11-15): summands are labelled by partitions with at most two rows, not by knot types, and part (2) now claims only that every summand is detected by some braid closure. The knot-type eigenbasis and Feynman-integral reading moved to `rem:knot-eigenbasis-complete-reading`.",
    },
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:knot-eigenbasis-complete",
  lean: { ref: "qou:QOU.Braiding.knot_eigenbasis_complete",
    validation: "not_checked",
  },
  title: "Complete decomposition of the tensor tower",
  tags: ["braid-group", "hecke-algebra", "knot-invariant", "schur-weyl"],
  uses: ["prop:braid-action-tensor"],
  proofs: ["prf:knot-eigenbasis-complete"],
});
