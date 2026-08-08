import { proposition } from "../../schema/builders";

/**
 * Wedderburn trace identity: the Markov trace of the identity is unit,
 * Σ_λ d_λ · y_λ(q) = 1 — the normalization that partitions the total
 * Markov weight among the Wedderburn blocks.
 */
export default proposition({
  label: "prop:wedderburn-trace-identity",
  title: "Markov-trace normalization for $H_n(q)$",
  tags: [
    "wedderburn",
    "markov-trace",
    "plancherel",
    "normalization",
    "hecke-algebra",
    "partition",
  ],
  lean: { ref: "qou:QOU.BraidsAndKnots.PlancherelViaRecipe.plancherel_via_recipe",
    validation: "not_checked",
  },
  uses: ["prop:three-parameters-wedderburn"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-07",
      body:
        "**§7c base-ring note (archimedean specialisation).** The Lean " +
        "`PlancherelViaRecipe` states the Markov-trace normalisation " +
        "`Σ_λ d_λ y_λ(q) = 1` over `ℝ`, evaluated at the substrate anchor. " +
        "Separately (not a base-ring issue): the current declaration is a " +
        "placeholder concluding `(1 : ℝ) = 1` rather than the displayed sum, " +
        "tracked in `docs/audits/lean-vacuity-review-ledger.json`.",
    },
    {
      kind: "refined-framing",
      date: "2026-06-29",
      body:
        "Restated from the earlier (false) claim `Σ_λ dim_q(λ)² = [n]_q!` to the " +
        "Markov-trace normalization `Σ_λ d_λ·y_λ(q) = 1`. The old sum identity does " +
        "not hold at generic q (disproved n=2..5; `Σ dim_q² = 2 ≠ q+1 = [2]_q!`), and " +
        "its `.md` table even wrote the inconsistent `1+1=2.230` — see " +
        "`docs/audits/2026-06-29-wedderburn-trace-identity-false-at-generic-q.md`. The " +
        "consumers (Wigner coefficient, descent, shadow prices) only ever used `[n]_q!` " +
        "as a Hecke-level scale (computed directly as the q-factorial) and the per-block " +
        "ratio `dim_q²/[n]_q!`, plus the genuine Markov normalization here; nothing " +
        "depended on the false sum equality, so the restatement leaves every mass/binding " +
        "number unchanged. lean.ref repointed from the false sorry'd " +
        "`QOU.BraidKnot.wedderburn_trace_identity` to the true `plancherel_via_recipe`.",
    },
  ],
});
