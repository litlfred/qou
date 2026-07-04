import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:pawlowski-leitner-basis",
  title: "Pawlowski--Leitner basis for $\\mathrm{Hom}(V_j, V_{1/2}^{\\otimes n})$",
  lean: { ref: "qou:QOU.PawLeiBasis",
    validation: "not_checked",
  },
  uses: [
    "rem:spin-half-representation",
    "unital-groebner-bases:cor:pbw",
  ],
  examples: ["rem:adjoint-trace"],
  tags: ["basis", "intertwiner", "representation", "pawlei"],
  cites: [
    "leitnerpawloski2004",
  ],
});
