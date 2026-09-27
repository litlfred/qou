import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:u1-equivariant-reduction",
  lean: { ref: "qou:QOU.CommutativeQOU.u1EquivariantReduction", validation: "not_checked" },
  title: "$\\mathrm{U}(1)$-equivariant reduction of the exceptional divisor",
  tags: ["exceptional-divisor", "u1", "equivariant", "commutative-limit"],
  uses: [
    "def:exceptional-divisor",
    "def:commutative-qou",
  ],
});
