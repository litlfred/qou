import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:spectral-chart-correspondence",
  title:
    "Spectral--chart correspondence: Hecke eigenspaces realise the chart-glue of $\\mathbb{P}_q(V)$",
  cites: ["kassel1995", "woronowicz1988"],
  tags: [
    "braiding",
    "eigenvalue",
    "affine-chart",
    "projective-line",
    "substrate-parameter",
    "categorical",
  ],
  lean: { ref: "qou:QOU.spectral_chart_correspondence",
    validation: "not_checked",
  },
  uses: ["rem:affine-chart-origin-of-i-and-q"],
});
