import { conjecture } from "../../schema/builders";

export default conjecture({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "conj:shell-transition-knot",
  title:
    "Stability pairs from Borromean spin-orbit shell-transition knots",
  tags: [
    "stability-pairs",
    "nuclear-shell",
    "harmonic-oscillator",
    "spin-orbit",
    "borromean",
    "shell-transition",
    "crossing-number",
  ],
  lean: { ref: "qou:QOU.Conjectures.ShellTransitionKnot",
    validation: "not_checked",
  },
  uses: ["conj:orbital-fourier-decomposition"],
});
