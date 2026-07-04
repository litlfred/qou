import { remark } from "../../schema/builders";

export default remark({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "rem:bloch-wigner-mathlib-filler",
  title:
    "Bloch-Wigner dilogarithm $D$ on the unit circle — repo-internal Mathlib filler",
  interprets: "rem:clausen-function-mathlib-filler",
  uses: ["rem:clausen-function-mathlib-filler"],
  cites: ["thurston1978", "zagier1986"],
  tags: [
    "mathlib-filler",
    "bloch-wigner",
    "dilogarithm",
    "unit-circle",
    "figure-8-knot",
    "borromean-rings",
    "lean-infrastructure",
  ],
});
