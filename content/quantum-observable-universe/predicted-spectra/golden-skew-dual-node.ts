import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:golden-skew-dual-node",
  title:
    "Skew-dual golden node at $q = \\varphi^2$ under the bar involution $q \\leftrightarrow q^{-1}$",
  tags: [
    "golden-ratio",
    "bar-involution",
    "skew-symmetry",
    "elliptic-degeneration",
    "stability-margin",
    "substrate-parameter",
  ],
  lean: {
    ref: "qou:QOU.Archimedean.golden_skew_dual_node",
    validation: "not_checked",
  },
  uses: ["rem:golden-ratio-degeneration"],
});
