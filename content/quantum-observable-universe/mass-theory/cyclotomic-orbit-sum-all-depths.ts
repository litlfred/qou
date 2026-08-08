import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note.** The Lean sibling's only `ℝ` is `zetaN : ℝ` " +
        "in `orbit_sum_all_depths`, fed to `clNAtZetaPredicted n N zetaN`. " +
        "The object being summed is the **Clausen function** `Cl_n(2πk/N)` " +
        "(via `QOU.Infra.Clausen`) — a real-analytic special function of a " +
        "real angle, involving `π`. There is no generic-ring Clausen value to " +
        "generalise to, so `ℝ` is load-bearing.",
    },
    {
      kind: "caveat",
      date: "2026-08-08",
      body:
        "**Flagged for the vacuity queue, not fixed here.** " +
        "`orbit_sum_all_depths` is a `def` whose body concludes " +
        "`clNAtZetaPredicted n N zetaN = clNAtZetaPredicted n N zetaN` by " +
        "`rfl`, and both `2 ≤ n` / `2 ≤ N` hypotheses are anonymous and " +
        "unused. That is a tautology in `def` clothing (§1a " +
        "`def-disguised-true` family). Recorded during base-ring triage; the " +
        "vacuity drain owns the fix.",
    },
  ],
  label: "prop:cyclotomic-orbit-sum-all-depths",
  title:
    "General orbit-sum at every depth: $\\sum_k \\mathrm{Cl}_n(2\\pi k/N) = (N^{1-n} - 1)\\zeta(n)$ for $n$ odd, $0$ for $n$ even",
  lean: {
    ref: "qou:QOU.BraidKnot.CyclotomicOrbitSumAllDepths.orbit_sum_all_depths",
    validation: "not_checked",
  },
  computation: {
    engine: "mpmath",
    script: "computations/jonquiere_cyclotomic_general.py",
    witness:
      "computations/jonquiere-cyclotomic-general.witness.json",
    status: "verified",
  },
  cites: ["bloch2000", "zagier1986"],
  tags: [
    "multiplication-formula",
    "orbit-sum",
    "all-depths",
    "general-form",
    "polylogarithm",
    "cyclotomic",
    "graded-mikusinski",
    "theorem-level",
  ],
});
