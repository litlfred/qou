import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): Equivalently, $\\mathcal{B}$ is the largest interval satisfying the deconfinement criterion $q > 1/\\varphi^2$ ([deconfinement threshold](#rem:deconfinement-golden-threshold)) and its bar conjugate $q < \\varphi^2$ simultaneously." },
  ],
  label: "prop:bar-self-dual-confinement-band",
  title:
    "The open interval $(1/\\varphi^2,\\,\\varphi^2)$ is the maximal bar-self-dual confinement band",
  tags: [
    "golden-ratio",
    "bar-involution",
    "skew-symmetry",
    "confinement",
    "deconfinement",
    "phase-boundary",
    "substrate-parameter",
  ],
  lean: {
    ref: "qou:QOU.Archimedean.BarSelfDualConfBand.bar_self_dual_confinement_band",
    validation: "not_checked",
  },
  uses: [
    "prop:golden-skew-dual-node",
    "rem:deconfinement-golden-threshold",
  ],
});
