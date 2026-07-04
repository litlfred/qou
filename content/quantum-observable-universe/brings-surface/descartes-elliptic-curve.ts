import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:descartes-elliptic-curve",
  title:
    "The Descartes elliptic curve $\\mathcal{E}_q$",
  tags: [
    "elliptic-curve",
    "descartes",
    "color-fibration",
    "substrate-parameter",
    "golden-ratio",
    "weierstrass",
  ],
  lean: { ref: "qou:QOU.Archimedean.descartes_elliptic_curve",
    validation: "not_checked",
  },
  uses: [
    "rem:color-tube-cubic",
  ],
});
