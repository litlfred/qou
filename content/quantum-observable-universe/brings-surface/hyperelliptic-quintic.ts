import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "def:hyperelliptic-quintic",
  lean: { ref: "qou:QOU.HyperellipticQuintic", validation: "not_checked" },
  title: "The hyperelliptic quintic $\\mathcal{X}_5 \\colon y^2 = x^5 - 1$",
  tags: ["hyperelliptic", "genus-2", "bolza", "roots-of-unity"],
  uses: ["prop:lagrange-resolvent-transform"],
  cites: [
    "bolza1887",
  ],
});
