import { table } from "../../schema/builders";
export default table({
  label: "tbl:upstream-mathlib-additions-table2-data",
  title: "Convergence, pentagon, reflection, and Tauberian obligations in the archimedean dilogarithm sector",
  uses: ["prop:upstream-mathlib-additions"],
  tags: ["extracted-table"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-19",
      body: "Lean/Mathlib formalisation roadmap: `Summable` proof for `complexLiTwo` on `|z| ≤ 1` (adapting `Real.tsum_geometric_lt_top` analogues); 5-term pentagon for `blochWigner` (~50-100 lines of Lean); half-period reflection via `Real.sin_two_pi_sub` analogous to `Cl_2_neg`; uniform Tauberian theorem for `complexLiTwo`.",
    },
  ],
});
