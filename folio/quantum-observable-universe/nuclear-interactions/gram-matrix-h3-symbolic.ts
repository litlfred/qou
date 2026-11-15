import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:gram-matrix-h3-symbolic",
  lean: {
    ref: "qou:QOU.Interactions.GramMatrixH3Symbolic.gramMatrix",
    validation: "not_checked",
  },
  title:
    "The H_3(q) Hoefsmit-seminormal Gram matrix on the 6-element normal-form basis, with the Markov weight $z$ carried symbolically: its determinant factors so that the canonical weight $z = q^3/(q^2+1)$ is a root, hence the canonical Gram is singular with the three-strand $q$-antisymmetriser as its radical.",
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
      kind: "status",
      date: "2026-08-23",
      body: `**This block was convention C throughout, and its headline claim is false in the canonical frame.** Everything written below this note predates the 2026-08-15 owner ruling that makes convention D (\`z = q³/(q²+1)\`) canonical. It is kept as recorded — the mathematics is right, and it is right about C — but read it as C-frame, and note that two of the claims it makes do not survive:

- **\`gramMatrix_det_ne_zero\` is false under D.** Carrying the Markov weight \`z\` symbolically, the determinant factors as \`−(z−q)⁵(qz+1)⁵((q²+1)z − q³)(q³z + qz + 1)/q⁸\`. The third factor vanishes *identically in q* exactly at \`z = q³/(q²+1)\` — so D is a **root of the H₃ Gram determinant as a polynomial in z**, and the canonical Gram is singular for every \`q\`, with the three-strand q-antisymmetriser as its radical. This is a scope-(b) structural exclusion per AGENTS.md, and the invariant is that factorisation — an exact symbolic identity, not a numerical probe.
- **The positive-definiteness reading in the 2026-08-08 base-ring note is false under D twice over:** the form is singular, and the reference witness records a *negative* eigenvalue at \`q₀\` besides, so it is indefinite rather than positive-semi-definite.

**What survives:** \`gramMatrix_isSymm\` and \`gramMatrix_top_left\` hold for *every* \`z\`, so they transfer unchanged (\`gramMatrixD_isSymm\`, \`gramMatrixD_top_left\`).

**Also corrected here:** the 2026-05-25 status note below records \`gramMatrix_det_ne_zero\` as "Deferred to Phase 1b-2". It was discharged — the file is sorry-free, and \`gram_det_eq\` proves the full factorisation. That note has been stale since; it is left in place as the historical record rather than rewritten.

**Epistemic tiers of the four numbered claims in the \`.md\`.** Claims (1), (3) and (4) are **Lean-proved sorry-free** (\`gramMatrixD_isSymm\` / \`gramMatrixD_top_left\`; \`gramMatrixD_det_eq_zero\` + \`gramMatrixD_mulVec_radical\` + \`gramMatrixD_not_posDef\`; \`gramMatrix_det_ne_zero\`). Claim (2) — the generic factorisation over ℚ(q,z) — is **symbolic-exact, not Lean-proved**: the Lean carries its two specialisations, and the generic identity is established in \`computations/probes/gram_h3_convention_frame_probe.py\`, which also reproduces \`gram_det_eq\` factor for factor as a cross-check on the derivation.`,
      see: "computations/probes/gram_h3_convention_frame_probe.py",
    },
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
    // The file is hyphenated on disk. The underscored spelling this field
    // carried until 2026-08-23 resolves to nothing — a dead producer path.
    script: "computations/gram-matrix-dual.py",
    witness: [
      "computations/gram-matrix-dual.witness.json",
      "computations/gram-h3-symbolic-regression.witness.json",
      "computations/probes/gram-h3-convention-frame-probe.witness.json",
    ],
    consumers: [
      "computations/lp_dual_solver.py",
    ],
    status: "verified",
    // Was "verified" -> "failed" -> "verified" over 2026-08-23, and the round
    // trip is not a wobble: each step was a different fact.
    //
    //  1. "verified" was UNEARNED. The cited witness's own `allPassed` was
    //     false (gram_h3_symbolic_matches_pyhecke, red at 0.17218519049094
    //     against 1e-14). Nothing had ever compared the two until
    //     scripts/check-computation-status.py.
    //  2. "failed" was correct AS OF THEN, and per ComputationStatus is what a
    //     non-matching witness means.
    //  3. "verified" again once the guard was REPAIRED — not re-baselined.
    //     Diagnosis in gram_h3_convention_frame_probe.py: the red number was
    //     never drift. The guard transcribed the Lean `gramEntry` definitions,
    //     which are convention C, and differenced them against a reference
    //     regenerated under convention D on 2026-08-15; 0.17218519049094 is
    //     exactly the C-D gap and nothing else. Both sides were internally
    //     exact the whole time. The guard now transcribes `gramEntryD` and
    //     compares canonical against canonical, which is the drift check it
    //     was written to be, and it passes at 2.27e-16 — the float64 floor of
    //     the strings the reference stores. The C-D gap is retained in the
    //     witness as `data`, explicitly NOT as an assertion, so the number
    //     stays visible without posing as a drift measurement.
    //
    // No tolerance was widened and no baseline was touched; what changed is
    // which two things are being compared.
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
