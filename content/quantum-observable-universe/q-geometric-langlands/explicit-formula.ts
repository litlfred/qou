import { theorem } from "../../schema/builders";

export default theorem({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "thm:explicit-formula",
  title: "Explicit formula as a spectral--geometric trace identity",
  lean: { ref: "qou:QOU.AlgebraicSubstrate.explicit_formula",
    validation: "not_checked",
  },
  uses: [
    "def:q-chebyshev-function",
    "thm:tannaka-krein-isomorphism",
  ],
  tags: [
    "explicit-formula",
    "trace-formula",
    "fourier-transform",
    "spectral-geometric",
  ],
  cites: ["rosen2002", "weil1948", "reshetikhin1991"],
});
