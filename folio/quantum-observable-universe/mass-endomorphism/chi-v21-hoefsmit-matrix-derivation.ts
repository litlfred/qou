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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): ## Content of this module\n\n| theorem | content | proof |\n|---|---|---|\n| `hoefsmit_v21_sigma0_trace` | $q + (-q^{-1}) = q - q^{-1}$ | `ring` |\n| `hoefsmit_v21_sigma1_trace` | $d_1 + d_2 = q - q^{-1}$ | `field_simp + ring` |\n| `chi_V21_difference_factored_eq_polynomial` | factored $\\leftrightarrow$ polynomial form | `field_simp + ring` |\n| `chi_V21_laurent_decomposition` | explicit Laurent: $-q^3/4 + q/4 - q^{-1}/4 + q^{-3}/4$ | `field_simp + ring` |\n| `chi_V21_difference_at_{one,two}` | numerical cross-checks at $q = 1, 2$ | `norm_num` |\n| `hoefsmit_v21_braid_relation` | $\\sigma_0\\sigma_1\\sigma_0 = \\sigma_1\\sigma_0\\sigma_1$, generic $b$ with $b^2 = d_1d_2+1$ | `fin_cases` + `field_simp` + `nlinarith` |\n| `chi_v21_matrix_trace_identity` | **the 11-crossing matrix-product trace difference** | `simp only` + `Matrix.trace_fin_two_of` + `ring_nf` + `field_simp` |\n\n\n\n\n## Formalization of the matrix-product trace identity\n\nThe full matrix-product trace derivation is formalized and proved in `chi_v21_matrix_trace_identity`:\n\n1. The Hoefsmit matrices $\\sigma_0, \\sigma_1$ are declared locally on `(Fin 2) × (Fin 2) → ℝ`.\n\n3. The explicit 11-crossing word orders for $\\beta_p$ and $\\beta_n$ are encoded as `beta_p_word_v21` and `beta_n_word_v21` and consumed directly by the proof.\n\n**The one tactic choice that decides it.** Project the folded matrix with\n`Matrix.trace_fin_two_of` (which rewrites $\\mathrm{tr}\\,!![a,b;c,d]$ straight\nto $a+d$), never `Matrix.trace_fin_two` (which leaves `M 0 0 + M 1 1` as\n*applications*). With the latter, `field_simp` runs on the un-projected\nexpression and exhausts 2 000 000 heartbeats. Projecting first also removes\nthe need for any `linear_combination` certificate: only **even** powers of\n$b$ reach the trace, because each index-1 factor is symmetric with\noff-diagonal $b$ and a path from a diagonal slot back to itself takes an even\nnumber of off-diagonal steps. Odd powers do occur — $b^3$ appears 20 times in\nthe normalised matrix — but only in the off-diagonal entries, which the trace\ndiscards.\n\n\n\n## Full matrix-product trace theorem (statement)\n\nNow formalised explicitly with the Hoefsmit 2$\\times$2 matrices:\n\n```lean\nnoncomputable def sigma0_v21 (q : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=\n  !![q, 0; 0, -q⁻¹]\n\nnoncomputable def sigma1_v21 (q : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=\n  !![d_1, Real.sqrt bSq; Real.sqrt bSq, d_2]\n\ninductive TypedCrossingV21 | sig | siginv | avg\n\ndef beta_p_word_v21, beta_n_word_v21 : TypedB3Word\n   -- explicit 11-crossing lists per atom_canonical_crossings\n\nnoncomputable def chi_v21_on_word (q : ℝ) (w : TypedB3Word) : ℝ :=\n  Matrix.trace (w.foldl ... fun acc c => acc * crossing_to_matrix q c)\n```\n\nThe theorem statement is now **explicit at the matrix-product\nlevel**. The proof is the only remaining `sorry` here — discharged by the substantive sympy\nverification recorded in `per-wedderburn-block-ck.witness.json`.\n\nA full Lean proof would unfold the 11-matrix product on\n`(Fin 2) × (Fin 2) → ℝ` matrices with `Real.sqrt` entries; tractable\nbut length-substantial.\n" },
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    {
      kind: "status",
      body: "**Closed at the rational-identity level** (5 theorems sorry-free):\nfactored $\\leftrightarrow$ polynomial, Laurent decomposition, numerical checks\nat q=1, q=2.\n\n**Matrix-product trace identity STATED** with explicit matrices\nand word; proof marked sorry with `-- Ref:` to the sympy\nverification per AGENTS.md §1.\n\nThis honestly captures both what's formally proved and what's\nempirically backed.",
    },
  ],
});
