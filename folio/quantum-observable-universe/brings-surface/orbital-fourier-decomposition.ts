import { conjecture } from "../../schema/builders";

export default conjecture({
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-24",
      body: "Formalisation audit (`qou-x60n`): `2026-09-04-borromean-quark-carriers-trivial.lean` (`T1`) exhibits a definitional instance of the local `BorromeanQuark` modelling carrier.",
      see: "docs/audits/2026-09-04-borromean-quark-carriers-trivial.lean",
    },
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "conj:orbital-fourier-decomposition",
  title:
    "Quantum numbers from Fourier decomposition of normal-bundle sections",
  tags: [
    "orbital",
    "fourier",
    "normal-bundle",
    "quantum-numbers",
    "spherical-harmonic",
    "laplacian",
    "trefoil",
  ],
  lean: { ref: "qou:QOU.orbital_fourier_decomposition",
    validation: "not_checked",
  },
  uses: ["conj:orbital-space-normal-bundle"],
});
