import { remark } from "../../schema/builders";

export default remark({
  label: "rem:chi-v21-hoefsmit-matrix-derivation",
  interprets: "rem:chi-per-irrep-cyclotomic-closed-forms",
  title:
    "V_(2,1) Hoefsmit 2×2 matrix derivation: scalar trace + Hecke-quadratic identities + Laurent decomposition of the closed form $-(q^4+1)(q^2-1)/(4q^3)$",
  uses: ["rem:chi-per-irrep-cyclotomic-closed-forms"],
  cites: ["hoefsmit1974", "jones1985", "wenzl1988"],
  tags: [
    "lean-infrastructure",
    "v21-hoefsmit",
    "matrix-derivation",
    "laurent-decomposition",
    "scaffolding",
  ],
  computation: {
    engine: "sympy",
    script: "computations/probe_per_wedderburn_block_ck.py",
    status: "experimental",
  },
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data. Exported declarations: `hoefsmit_v21_sigma0_trace`, `hoefsmit_v21_sigma1_trace`, `chi_V21_difference_factored_eq_polynomial`, `chi_V21_laurent_decomposition`, `chi_V21_difference_at_one`, `chi_V21_difference_at_two`, `hoefsmit_v21_braid_relation`, `chi_v21_matrix_trace_identity`, `sigma0_v21`, `sigma1_v21`, `TypedCrossingV21`, `beta_p_word_v21`, `beta_n_word_v21`, `chi_v21_on_word` (closed via `Matrix.trace_fin_two_of` + `ring_nf` + `field_simp`)." },
    {
      kind: "status",
      body: "**Closed at the rational-identity level** (5 theorems sorry-free):\nfactored $\\leftrightarrow$ polynomial, Laurent decomposition, numerical checks\nat q=1, q=2.\n\n**Matrix-product trace identity STATED** with explicit matrices\nand word; proof marked sorry with `-- Ref:` to the sympy\nverification per AGENTS.md §1.\n\nThis honestly captures both what's formally proved and what's\nempirically backed.",
    },
  ],
});
