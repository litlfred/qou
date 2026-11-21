import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:calibration-cohomology-alignment",
  title: "The three calibrations are the three cohomological data of H¹(Bring)",
  uses: [
    "prop:prolonged-periods-fixed-depth",
    "prop:sl2-prolongation-recurrence",
    "prop:electron-period-base",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-20",
      body: "**Demoted from `prop:calibration-cohomology-alignment` (owner choice, 2026-11-20; bean qou-tm3c).** The Lean sibling did not formalise the claim. `calibrations_eq_cohomology` took the three equalities $\\mathrm{CAL}_i = (\\text{datum})_i$ as structure fields and rewrote with them, and `cohomology_data_count` was `2 + 1 = 3 := rfl`. Neither says anything about Bring's curve. The sibling was removed rather than kept as a placeholder. A faithful statement needs the polarised Hodge structure of $H^1(\\mathrm{Bring})$ and its $S_5$-isotypic decomposition, which Mathlib does not provide.",
    },
  ],
});
