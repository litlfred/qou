import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:mobius-golden-fixed-points",
  title:
    "Fixed-point quartet of the baryon integration-limit Möbius pair: $\\{1/\\varphi, -\\varphi, \\varphi, -1/\\varphi\\}$",
  tags: [
    "mobius-transformation",
    "golden-ratio",
    "integration-limit",
    "color-tube",
    "binomial",
    "fixed-point",
    "bar-involution",
    "skew-symmetry",
  ],
  lean: { ref: "qou:QOU.Archimedean.mobius_golden_fixed_points",
    validation: "not_checked",
  },
  uses: [
    "rem:picard-lefschetz-thimble",
    "rem:color-tube-cubic",
    "prop:golden-skew-dual-node",
    "prop:moduli-symmetry-d4",
  ],
});
