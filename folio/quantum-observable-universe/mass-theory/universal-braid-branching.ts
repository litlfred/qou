import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:universal-braid-branching",
  title:
    "Universal braid character formula via Young's lattice branching",
  lean: { ref: "qou:QOU.BraidKnot.universal_braid_branching",
    validation: "not_checked",
  },
  // rem:body-asymptotics-catalog dropped from uses[] 2026-11-20 (owner choice, bean qou-tm3c):
  // cited in the proof only as a 'see also' pointer for the surreal-valuation notation. A remark carries no premise; the edge only put this block
  // downstream of a conjecture.
  uses: ["prop:figure-eight-branching-rule"],
  cites: ["hoefsmit1974", "wenzl1988"],
  tags: [
    "branching-rule",
    "youngs-lattice",
    "universal",
    "borromean",
    "figure-eight",
    "chebyshev",
    "convergence",
  ],
});
