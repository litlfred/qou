import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "def:su2-generators",
  lean: { ref: "qou:QOU.Su2Generators", validation: "not_checked" },
  title: "$\\mathrm{SU}(2)$ generators of $\\mathrm{Dic}_3$",
  tags: ["su2", "binary-dihedral", "dic3"],
  uses: ["def:su2-basis"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/su2-generators-0.svg", blockIndex: 0, hash: "8aacfb81d220" },
  ],

});
