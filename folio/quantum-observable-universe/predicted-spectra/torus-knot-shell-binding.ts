import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:torus-knot-shell-binding",
  title:
    "Withdrawn: shell binding from the torus knot hierarchy: $T_{2,3} \\to T_{2,5} \\to T_{2,7} \\to T_{2,9}$",
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
    { kind: "note", date: "2026-11-21", body: "The withdrawal of the T(2,n_s) shell-size rule is an owner ruling of 2026-11-21 (docs/coordination/owner-rulings.md). The ruling attribution was moved here from the prose on QA review of #8837." },
    { kind: "note", date: "2026-11-21", body: "Owner ruling 2026-11-21 (docs/coordination/owner-rulings.md): the nuclear Regime-I shell-size rule T(2,n_s) is withdrawn; its basis was a mislabel ((sigma_0 sigma_1)^2 sigma_0 closes to T(2,4), not T(2,5)). The block is withdrawn in place, not deleted, because observations/double-magic-delta-i-bound and hopf-link-non-magic cite it. Sidecar retriage 2026-11-21 also found the Lean sibling is rfl/decide over a hard-coded table." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([Construction rules for nuclear shells from the torus knot hierarchy](#rem:shell-construction-rules); [Magic numbers $\\mathfrak{M} = \\{2, 8, 20, 28, 50, 82, 126\\}$ as ranks of $S_5$-stable Bring period sub-lattices](#conj:magic-numbers-bring))" },
  ],
});
