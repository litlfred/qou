import { remark } from "../../schema/builders";

export default remark({
  label: "rem:chi-v3-closed-form-proof",
  interprets: "prop:hecke-1d-irrep-closed-form-character",
  title:
    "Formal proof of the V_(3) per-irrep character difference closed form: $\\chi_{(3)}(\\beta_n) - \\chi_{(3)}(\\beta_p) = -(q^2 + 1)^2 (q^2 - 1)/(4q) = -(q^5 + q^3 - q - q^{-1})/4$, with explicit $\\varepsilon^k$ pattern via polynomial + geometric decomposition",
  uses: ["rem:typed-b3-sub-braid-extraction"],
  cites: [
    "jones1985",
    "wenzl1988",
    "hoefsmit1974",
  ],
  tags: [
    "lean-infrastructure",
    "v3-symmetric-irrep",
    "per-wedderburn-block",
    "closed-form",
    "epsilon-expansion",
    "geometric-series",
  ],
  computation: {
    engine: "sympy",
    script: "computations/probe_per_wedderburn_block_ck.py",
    status: "experimental",
  },
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data. Exported theorems: `chi_V3_difference_eq_factored`, `chi_V3_difference_factored_eq_polynomial`, `chi_V3_difference_eq_polynomial`, `chi_V3_difference_decomposition`, `chi_V3_polynomial_part_at_one`, `chi_V3_geom_part_at_one`, `chi_V3_difference_at_two`, `chi_V3_difference_at_one`, `chi_V3_decomposition_at_two`." },
    {
      kind: "status",
      body: "V_(2,1) and V_(1,1,1) await analogous formal closed forms:\n\n- **V_(1,1,1)** is the **q $\\leftrightarrow$ $-q^{-1}$ mirror** of V_(3) (antisymmetric irrep where each $\\sigma_i$ acts as $-q^{-1}$). The proof should mirror this module's structure exactly with $q \\mapsto -q^{-1}$.\n- **V_(2,1)** requires the 2$\\times$2 Hoefsmit matrix expansion (more involved — needs the $\\sigma_0$, $\\sigma_1$ matrix products).\n\nFollowing the user direction \"first prove formally V\", this block\ncloses V_(3) and provides the template for V_(1,1,1). V_(2,1) is\nthe next concrete follow-up.",
    },
  ],
});
