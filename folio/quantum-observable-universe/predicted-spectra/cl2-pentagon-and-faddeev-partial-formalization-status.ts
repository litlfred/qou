import { remark } from "../../schema/builders";

export default remark({
  label: "rem:cl2-pentagon-and-faddeev-partial-formalization-status",
  title:
    "Formalization status of the $\\mathrm{Cl}_2$ pentagon and Faddeev-Kashaev boundary closures",
  interprets: "prop:cl2-pentagon-and-faddeev-partial",
  uses: ["prop:cl2-pentagon-and-faddeev-partial"],
  tags: ["mathlib-filler", "formalization-status", "partial-closure"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-19",
      body: "Lean declaration inventory moved from prose and tables: `Cl_2_pentagon_at_zero_unconditional`, `Cl_2_pentagon_zero_substitution`, `Cl_2_pentagon_consistent_with_zero`, `faddeev_kashaev_at_zero_unconditional`, `faddeev_kashaev_consistency_at_zero`, `faddeev_kashaev_at_zero_exact`, and `partial_closures_at_boundary` (proved via `simp`, `ring`, `linarith` from `Cl_2_zero` and `faddeev_limit_at_zero`), discharging boundary consistency for `Cl_2_PentagonHolds` and `FaddeevKashaevQuasiClassicalLimit`. Interior cases await Mathlib Fourier-series and uniform Tauberian infrastructure.",
    },
  ],
});
