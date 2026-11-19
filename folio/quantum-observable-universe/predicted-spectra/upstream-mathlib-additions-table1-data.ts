import { table } from "../../schema/builders";
export default table({
  label: "tbl:upstream-mathlib-additions-table1-data",
  title: "Table 1 from prop:upstream-mathlib-additions",
  uses: ["prop:upstream-mathlib-additions"],
  tags: ["extracted-table"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-19",
      body: "Lean/Mathlib declarations in `upstream-mathlib-additions.lean`: `complexLiTwo : ℂ → ℂ`, `complexLiTwo_zero`, `blochWigner : ℂ → ℝ` (using `Complex.log`, `Complex.arg`, `Complex.abs`), `blochWigner_zero` (via `Real.log_zero = 0`), `Cl_2_neg` (via `tsum` rearrangement and `Real.sin_neg`), `Cl_2_zero_via_oddness`.",
    },
  ],
});
