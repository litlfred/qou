import { conjecture } from "../../schema/builders";

export default conjecture({
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-24",
      body: "Formalisation audit (`qou-x60n`): `2026-09-04-borromean-quark-carriers-trivial.lean` (`T7`) inhabits the local `BorromeanQuark` carrier in `ShellTransitionKnot.lean` with `crossingNumber := 3`.",
      see: "docs/audits/2026-09-04-borromean-quark-carriers-trivial.lean",
    },
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
  lean: { ref: "qou:QOU.Core.ShellTransitionKnot",
    validation: "not_checked",
  },
  uses: ["conj:orbital-fourier-decomposition"],
});
