import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:generator-volume-decomposition",
  title:
    "Nuclear energy as a sum of generator volumes via Chebyshev recurrence",
  tags: [
    "generator-volume",
    "chebyshev",
    "hecke-algebra",
    "energy",
    "factorization",
    "braid-word",
    "nuclear",
    "binding-energy",
  ],
  lean: { ref: "qou:QOU.Archimedean.generator_volume_decomposition",
    validation: "not_checked",
  },
  uses: ["thm:groebner-shirshov-energy"],
});
