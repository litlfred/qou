import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:terminal-resolution",
  lean: { ref: "qou:QOU.Experimental.terminal_resolution",
    validation: "not_checked",
  },
  title: "Terminal Resolution of Hadronic Mass",
  uses: [
    "rem:skein-mass-relation",
    "cor:mass-identity-C",
  ],
  proofs: ["prf:terminal-resolution"],
  tags: ["mass", "hadronic"],
});
