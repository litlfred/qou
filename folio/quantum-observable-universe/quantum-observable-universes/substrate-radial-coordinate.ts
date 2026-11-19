import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:substrate-radial-coordinate",
  lean: { ref: "qou:QOU.substrate_radial_coordinate",
    validation: "not_checked",
  },
  title: "Aether parameter as the radial coordinate",
  proofs: ["prf:substrate-radial-coordinate"],
  tags: ["substrate", "projective", "boson", "fermion"],
  uses: [
    "def:contact-affine-chart",
    "def:fermion-boson-decomposition",
    "def:quantum-planck-constant",
    "ex:q-reeb-flow",
  ],
});
