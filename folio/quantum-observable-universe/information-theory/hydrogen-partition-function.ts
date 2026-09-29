import { example } from "../../schema/builders";

export default example({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "ex:hydrogen-partition-function",
  title: "Partition function for monatomic hydrogen",
  tags: [
    "hydrogen",
    "partition-function",
    "statistical-mechanics",
    "knot-gas",
    "borromean",
  ],
  uses: ["prop:quantum-ideal-gas-law"],
});
