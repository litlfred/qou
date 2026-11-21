import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:torus-knot-shell-binding",
  title:
    "Shell binding from the torus knot hierarchy: $T_{2,3} \\to T_{2,5} \\to T_{2,7} \\to T_{2,9}$",
  tags: [
    "torus-knot",
    "shell-binding",
    "magic-numbers",
    "chebyshev",
    "hecke-algebra",
    "transfer-matrix",
    "nuclear-structure",
    "inductive-construction",
  ],
  lean: { ref: "qou:QOU.Archimedean.torus_knot_shell_binding",
    validation: "not_checked",
  },
  uses: ["def:inter-shell-operator", "def:chebyshev-torus-coefficients"],
  examples: [
    "rem:shell-construction-rules",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([Construction rules for nuclear shells from the torus knot hierarchy](#rem:shell-construction-rules); [Magic numbers $\\mathfrak{M} = \\{2, 8, 20, 28, 50, 82, 126\\}$ as ranks of $S_5$-stable Bring period sub-lattices](#conj:magic-numbers-bring))" },
  ],
});
