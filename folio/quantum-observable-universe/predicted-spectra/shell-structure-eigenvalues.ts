import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Electron ruling (owner, 2026-11-21): relabelled the electron from the trefoil T_{2,3} to the word sigma_0 sigma_1 sigma_0 in B_3 (closure: Hopf link). Wording only; no number moved. Line 60 no longer calls the trefoil the electron (sidecar retriage 2026-11-21)." },
    {
      kind: "refined-framing",
      date: "2026-08-09",
      body: "Corrected 2026-08-09. The block carried a spurious square root and wrong decimals: √(h²+4) was published as 2.0054 (correct 2.010897 = [2]_q), λ₊ as 1.1073 (correct 1.109979 = q), λ₋ as −0.9027 (correct −0.900918 = −q⁻¹). The wrong figures were then retained in prose under a correction banner; they are now replaced by the correct values.",
    },
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
