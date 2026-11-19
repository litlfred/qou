import { table } from "../../schema/builders";
export default table({
  label: "tbl:upstream-mathlib-additions-table1-data",
  title: "Power-series definitions and origin evaluations for $\\mathrm{Li}_2$, the Bloch–Wigner function $D$, and $\\mathrm{Cl}_2$",
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
