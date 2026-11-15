import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:x5-z5-automorphism",
  lean: { ref: "qou:QOU.HyperellipticQuintic.z5_automorphism", validation: "not_checked" },
  title: "$\\mathbb{Z}_5$ automorphism of the hyperelliptic quintic",
  tags: ["automorphism", "z5", "roots-of-unity", "hyperelliptic"],
  uses: [
    "def:hyperelliptic-quintic",
    "rem:lagrange-resolvents",
  ],
});
