import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The optimal $A$-term refinement of this raw normal form — obtained by quotienting by the adjacency / chain-collapse ideals ([quotient ideals $I_8$, $I_9$](#def:gs-quotient-ideals-I8-I9)) — is stated separately ([optimal normal form](#thm:optimal-normal-form-valley))." },
  ],
  label: "prop:shell-closure-normal-form",
  title:
    "Shell closure as symmetric Poincaré distribution in the Hecke normal form",
  tags: [
    "shell-closure",
    "normal-form",
    "hecke-algebra",
    "poincare-polynomial",
    "magic-numbers",
    "bruhat-order",
    "nuclear-structure",
    "groebner-basis",
  ],
  lean: {
    ref: "qou:QOU.Archimedean.sequential_build_always_normal_form",
    validation: "not_checked",
  },
  uses: ["prop:skein-polynomial-transfer-matrix"],
});
