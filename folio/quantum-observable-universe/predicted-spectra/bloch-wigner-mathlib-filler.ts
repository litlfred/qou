import { remark } from "../../schema/builders";

export default remark({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    {
      kind: "note",
      date: "2026-11-19",
      body: "Formalization inventory moved from prose and tables (`bloch-wigner-mathlib-filler.lean`): `BlochWigner_unit_circle`, `BlochWigner_unit_circle_zero` (`Cl_2_zero`), `BlochWigner_figure_8_per_tetrahedron`, `BlochWigner_Borromean_per_octahedron`, `Vol_figure_8_eq_two_BW_tetrahedron` (`rfl`), `Vol_Borromean_eq_two_BW_octahedron` (`ring`). General complex extension $D : \\mathbb{C} \\setminus \\{0,1\\} \\to \\mathbb{R}$, `BlochGroup F`, and `BlochSuslinUniqueness` remain upstream Mathlib gaps.",
    },
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
