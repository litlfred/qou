import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:gram-matrix-h3-symbolic",
  lean: {
    ref: "qou:QOU.Interactions.GramMatrixH3Symbolic.gramMatrix",
    validation: "not_checked",
  },
  title:
    "Symbolic closed-form H_3(q) Hoefsmit-seminormal Gram matrix on the 6-element NF basis — 36 explicit Laurent-polynomial entries in $u = \\sqrt{q}$ with 2 of 3 structural axioms (is_symm, diag_top_one) Lean-proved.",
  // Detangler isolated-block fix (bean flus): the H_3(q) Hoefsmit Gram matrix is
  // defined "on the 6-element NF basis" (def:hecke-normal-form, braids-and-knots,
  // an earlier chapter — a backward edge, not a forward-ref). Wiring this genuine
  // upstream dependency de-isolates the block. (Its Hoefsmit/Wedderburn
  // foundations live in the later mass-theory chapter, so those are deliberately
  // not added here — they would introduce a Ch 9 → Ch 11 forward-ref.)
  uses: ["def:hecke-normal-form"],
  cites: [
    "halverson_ram_1998",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body: `**Base ring (§7c) — \`ℝ\` is load-bearing, and the entries alone would not have shown it.** The Gram entries are rational functions of \`u\` (e.g. \`u / (u² + 1)\`) and the determinant factors are polynomials, so the *data* looks purely algebraic. The content is not: the main theorem is **positive-definiteness for \`u > 1\`**, proved through a chain of per-factor positivity lemmas (\`detFactor1_pos\` …) discharged by \`linarith\` / \`positivity\`. Positive-definiteness is an ordering statement and does not survive to a generic ring — over \`ℂ\` the denominator \`u² + 1\` even vanishes.`,
    },
    {
      kind: "status",
      date: "2026-05-25",
      body:
        "**Phase 1b (follow-up to PR #1255 Option E Phase 1a).** Replaces " +
        "the deferred 'rational-encode 36 decimal entries' plan with " +
        "explicit categorical closed-form entries in $u = \\sqrt{q}$. Sympy-" +
        "verified against `gram-matrix-dual.witness.json` at q_0 to 1e-16. " +
        "**Proved (sorry-free):** `gramMatrix_isSymm` (15-cell case analysis), " +
        "`gramMatrix_top_left` (G[0,0] = 1). **Deferred to Phase 1b-2:** " +
        "`gramMatrix_det_ne_zero` — proof strategy in docstring (compute " +
        "symbolic det, factor out the (u−1) zero at the classical limit). " +
        "Numerical witness: det(G(u_0)) ≈ −0.189 at $u_0 = \\sqrt{q_0}$.",
    },
    {
      kind: "refined-framing",
      date: "2026-05-25",
      body:
        "**Why this matters per the user's 'cant we just prove it?' " +
        "directive.** The original Phase 1b plan was to encode 36 decimal " +
        "values from the empirical witness as rationals and prove " +
        "symmetry/det≠0 on those specific numerics. This delivers " +
        "WEAKER results (only at q_0) and ROTS as the witness changes. " +
        "The categorical form here is stronger: the entries are universal " +
        "rational functions in u, so the symmetry and top-left-one " +
        "properties hold for EVERY positive u — and downstream LP-dual " +
        "reasoning can cite the categorical theorems without conditional-" +
        "on-empirical-numerics caveats. The remaining sorry on " +
        "det_ne_zero is a routine symbolic-determinant computation " +
        "scoped as the next follow-up.",
    },
  ],
  computation: {
    engine: "sympy",
    script: "computations/gram_matrix_dual.py",
    witness: [
      "computations/gram-matrix-dual.witness.json",
      "computations/gram-h3-symbolic-regression.witness.json",
    ],
    consumers: [
      "computations/lp_dual_solver.py",
    ],
    status: "failed",
    // status was "verified" until 2026-08-23; the cited witness's own
    // `allPassed` is false (gram_h3_symbolic_matches_pyhecke). Per ComputationStatus,
    // "failed" = script ran, witness does NOT match expected values.
    // Nothing compared the two until scripts/check-computation-status.py.,
  },
  tags: [
    "gram-matrix",
    "hoefsmit",
    "h3",
    "symbolic",
    "option-e-phase-1b",
    "categorical",
    "frobenius",
  ],
});
