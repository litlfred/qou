import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:upstream-mathlib-additions",
  label: "rem:upstream-mathlib-additions-detail",
  title: "Details of the three Mathlib additions and their upstreaming targets",
  uses: ["prop:upstream-mathlib-additions"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-19",
      body: "Lean/Mathlib formalisation details: `complexLiTwo` (`tsum`-based candidate for `Real.dilog` / `Complex.dilog`, using Mathlib `Summable`), `blochWigner` (via `Complex.log` and `Complex.arg`), and unconditional theorems `Cl_2_neg` (via `Real.sin_neg` and `tsum_neg`), `complexLiTwo_zero`, `blochWigner_zero`.",
    },
  ],
});
