import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:frobenius-gram-matrix",
  lean: { ref: "qou:QOU.Archimedean.frobenius_gram_matrix", validation: "not_checked" },
  title: "Frobenius Gram matrix and dual construction in $H_3(q)$",
  uses: [],
  tags: [
    "gram-matrix",
    "frobenius-dual",
    "hecke-algebra",
    "markov-trace",
    "knot-operator",
    "pair-production",
    "annihilation",
  ],
  computation: {
    engine: "sympy",
    script: "computations/probes/frobenius_gram_matrix_probe.py",
    witness: "computations/probes/frobenius-gram-matrix-probe.witness.json",
    status: "failed",
    // "verified" -> "failed" on 2026-08-23. The cited witness's own `allPassed`
    // is false: `gram_matrix_nondegenerate` computes 1 (one degenerate
    // direction) against an expected 0. This block came in from main during the
    // merge and is the 13th instance of the qou-bm4i class.
    //
    // The failure is CORRECT and should not be cleared by re-running anything.
    // Its `source` reads "Frobenius self-duality A ≅ A^∨ implies the
    // Markov-trace pairing is non-degenerate at generic q" — true of GENERIC q,
    // and the canonical Markov weight is not generic. Over ℚ(q,z),
    //
    //     det G(q,z) = −(z−q)⁵(qz+1)⁵((q²+1)z − q³)(q³z + qz + 1)/q⁸
    //
    // and the third factor vanishes identically at z = q³/(q²+1), which IS
    // convention D. So the canonical Gram is singular for every q, with a
    // one-dimensional radical — proved sorry-free this session as
    // `QOU.Interactions.GramMatrixH3Symbolic.gramMatrixD_det_eq_zero` and
    // `gramMatrixD_mulVec_radical`. Generic-q non-degeneracy simply does not
    // survive the specialisation.
    //
    // Two independent producers agree, which is worth recording: this probe
    // finds exactly ONE degenerate direction and an INDEFINITE signature; the
    // Lean exhibits the radical explicitly as the three-strand
    // q-antisymmetriser (-q³, q², q², -q, -q, 1) and proves
    // `gramMatrixD_not_posDef`. They were arrived at separately — this probe on
    // main at 09:23, the Lean on this branch — and describe the same object.
    //
    // Note the block's own statement already flags that the `z³ ↦ hz² + z`
    // correction "has still to be propagated", so its entries are pre-correction
    // in places. Repairing that is authoring, not a status fix.
  },
  authorNotes: [
    {
      kind: "note",
      date: "2026-06-04",
      body: "**Markov-bug fix.** Earlier versions of this block asserted $\\mathrm{tr}_M(e^-) = z^3$ and offered a 'peel-from-the-right' derivation. This was incorrect: $\\sigma_1\\sigma_0$ is **not** in the sub-algebra $H_2 = \\langle \\sigma_0 \\rangle$ (the Markov axiom $\\mathrm{tr}_M(\\sigma_n \\cdot x) = z\\,\\mathrm{tr}_M(x)$ requires $x \\in H_n$), so the Markov-property step cannot be applied directly to $\\sigma_1 \\cdot \\sigma_0\\sigma_0$ after the cyclicity step. The canonical Ocneanu–Wenzl recursion gives $\\mathrm{tr}_M(e^-) = hz^2 + z$, verified independently in `docs/audits/-trm5-markov-bug.md` against the y-lambda Wenzl-bridge consistency $\\mathrm{tr}_M(b_i) = \\sum_\\lambda y_\\lambda(q) \\chi_\\lambda(b_i)$ (residual $\\sim 10^{-32}$ after fix; $\\sim 0.12$ before). The fix has been applied to `tools/pyhecke/python/pyhecke/gram.py` and the Gram matrix table below.",
    },
    {
      kind: "note",
      date: "2026-06-04",
      body: "**Symbolic Gram entries require recomputation.** The proposition's matrix and $g_{ij}$ formulas were derived assuming $\\mathrm{tr}_M(e^-) = z^3$ (now known to be incorrect — see Markov-bug note above). The entries that involve $\\mathrm{tr}_M$ applied to a product whose Hecke normal form contains $e^-$ must be rederived with $\\mathrm{tr}_M(e^-) = hz^2 + z$. Numerically, the post-fix Gram matrix is symmetric to machine precision and reproduces the y-lambda Wenzl-bridge identity exactly (Markov-bug audit, § 'Visible symptom: Gram matrix non-symmetric'). The corrected Python compute lives at `tools/pyhecke/python/pyhecke/gram.py`; a follow-up commit will recompute the symbolic table below.",
    },
    {
      kind: "note",
      date: "2026-08-09",
      body: "**Convention move, and two withdrawn claims.** The owner ruling of 2026-08-09 excised convention C ($z = 1/(q^{1/2}+q^{-1/2})$) in favour of convention D ($z = q^3/(q^2+1)$) repo-wide — registry `docs/coordination/trace-convention-registry.md`. Two assertions in the closing paragraph of this proposition were wrong and are now corrected there. (i) **Non-degeneracy is false under D.** $y_{(1^3)} = 0$ symbolically, so the $(1^3)$ Wedderburn block *is* the radical of the form, $\\det G = 0$ identically, and $G^{-1}$ does not exist. Under C the determinant was $-0.18920521914403668$ and the inverse existed. `tools/pyhecke/python/pyhecke/gram.py` was for that reason a deliberately **blocked** C→D migration — it exported `G_INV` at import, and `np.linalg.inv` on the singular D matrix raises nothing, it returns inverted rounding noise. **That block was lifted 2026-08-15:** the module is on convention D, `G_INV` is gone rather than renamed, and `G_PINV` (the inverse on the quotient $H_3(q)/\\mathrm{rad}$) replaces it, with `RADICAL` carrying the null direction in closed form as the $q$-antisymmetriser $\\sum_w (-1/q)^{\\ell(w)} T_w$. The degeneracy is now established **exactly**, not numerically: under D both $z$ and $h$ are rational in $q$, so at a rational $q$ the whole Gram lies in $\\mathbb{Q}$ and $\\det G = 0$ *exactly* with rank $5$ — a statement no float path can make, since $\\texttt{numpy}$'s $3.998\\times10^{-17}$ is equally consistent with a singular matrix and a merely tiny one. (ii) **The 'indefinite signature' reading is withdrawn** (commit `748ba9b1`). It quoted the *bilinear* pairing $\\mathrm{tr}_M(b_i b_j)$ without naming it; the Hecke star is $T_w^* = T_{w^{-1}}$, and on the star pairing $\\mathrm{tr}_M(b_i b_j^*)$ the form is positive — $(6,0,0)$ under C, $(5,0,1)$ under D. Never write 'indefinite' or 'Lorentzian' of this matrix without saying which pairing. The two 2026-06-04 notes above stay live: the $6\\times6$ symbolic table is still the uncorrected $z^3$ table, so it is now wrong on two independent counts — the trace rule and the convention — and recomputing it needs `computations/probes/frobenius_gram_matrix_probe.py`, not an edit.",
    },
  ],
});
