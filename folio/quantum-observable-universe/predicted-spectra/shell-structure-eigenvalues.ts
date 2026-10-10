import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:shell-structure-eigenvalues",
  title:
    "Orbital shells from eigenvalues of the photon-electron transfer matrix",
  tags: [
    "shell",
    "orbital",
    "eigenvalue",
    "transfer-matrix",
    "chebyshev",
    "rydberg",
    "hydrogen",
    "photon",
    "electron",
    "recurrence",
  ],
  lean: { ref: "qou:QOU.Archimedean.shell_structure_eigenvalues",
    validation: "not_checked",
  },
  uses: [
    // Declared by the .md banner and bound in the Lean (shell_eigenvalues_conditional at :174 binds [inst : BorromeanQuark]),
    // but absent here and unreachable in the uses[] graph at any depth
    // until 2026-08-30 — the dependency was recorded in prose only
    // (bean `qou-s3zd`). Not transitively reachable, so not redundant.
    "conj:borromean-quark","def:transfer-matrix-operator"
  ],
});
