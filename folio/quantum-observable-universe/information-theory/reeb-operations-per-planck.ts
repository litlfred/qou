import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note.** The Lean sibling's `ReebOperationsContext` " +
        "carries `t_P : ℝ` — the **Planck time** — alongside `q_real`, " +
        "`hbar_q`, `n_R`, and the proof opens with " +
        "`have hq0 : (0 : ℝ) < ctx.q_real := lt_trans one_pos ctx.q_gt_one` " +
        "then `linarith [ctx.q_gt_one]` to get `0 < q - 1` before dividing. A " +
        "time parameter is `ℝ` by meaning (§7c), and the `q_gt_one` ordering " +
        "is what licenses the division by `q - 1` in `t_P = q/(q-1)`. The " +
        "algebraic chain `n_R = t_P = q/(q−1) = 1/ℏ_q` is generic in form, but " +
        "its non-degeneracy here rests on that strict inequality.",
    },
  ],
  label: "prop:reeb-operations-per-planck",
  lean: { ref: "qou:QOU.Information.reeb_operations_per_planck", validation: "not_checked" },
  title: "Discrete iterations per Reeb circuit",
  tags: [
    "planck-time",
    "reeb-flow",
    "julia-set",
    "discrete-time",
    "information-theory",
  ],
  uses: [
    "def:planck-time",
    "rem:discrete-planck-step",
  ],
});
