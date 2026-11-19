import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:brane-tower-q-laplacian-decay",
  title:
    "Brane-tower convergence: q-Laplacian exponential decay drives the $\\hbar_q^{2n}$ tail bound",
  lean: { ref: "qou:QOU.Observations.brane_tower_q_laplacian_decay", validation: "not_checked" },
  uses: [
    "rem:non-commutative-probability-dictionary",
    "thm:jones-markov-trace",
  ],
  cites: ["wenzl1988"],
  tags: [
    "brane-tower",
    "q-laplacian",
    "exponential-decay",
    "geometric-series",
    "non-local-integration",
    "issue-649",
    "established",
  ],
  proofs: ["prf:brane-tower-q-laplacian-decay"],
  authorNotes: [
    {
      kind: "status",
      body: "**Provable.** The result is a geometric series plus the explicit spectrum of the q-Laplacian; the proof block `prf:brane-tower-q-laplacian-decay` assembles the q-integer asymptotic and the iterated Laplacian estimate.",
    },
    {
      kind: "note",
      body: "Provides an explicit absolute-convergence bound for the brane-tower integration, tightening the linkage between exponential decay of the q-Laplacian eigenfunctions and the physical justification for non-local integration.",
    },
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "`brane_tower_q_laplacian_decay.lean` is genuinely analytic: it " +
        "imports `Mathlib.Analysis.SpecificLimits.Basic` and **derives its " +
        "closed form by summing an infinite series** " +
        "(`tsum_geometric_of_lt_one` on `∑' k, M·r^(k+1)`), with `rho_L2 : ℝ` " +
        "the L² norm of the Reeb-bundle density. Convergence of a `tsum` and " +
        "an L² norm are archimedean, so the block sits on the archimedean " +
        "side of the §7c wall by construction. The Lean file's own field " +
        "docstring already says so; this note puts it where the checker reads " +
        "it.",
    },
  ],
  computation: {
    engine: "mpmath",
    script: "computations/c_k_beta_decay_witness.py",
    witness: "computations/c-k-beta-decay-bound.witness.json",
    status: "verified",
  },
});
