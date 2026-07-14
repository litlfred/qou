import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:tower-geometric-lower-bound",
  title: "Super-exponential brane-tower growth (GAP-A-3)",
  lean: {
    ref: "qou:QOU.Mass.LevelSelection.TowerGeometricLowerBound",
    validation: "not_checked",
  },
  tags: ["binding", "brane-tower", "level-selection", "gap-a-3", "plancherel"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-07-13",
      body: "Open combinatorial core: verified exact for `k ≤ 10` (`computations/deltalambda/wlambda_wstd_growth_bound_probe.py`); a faithful proof needs SYT / skew-tableau / Plancherel-measure Mathlib infrastructure. Carried in Lean as the §3b class `TowerGeometricLowerBound` with **no** fabricated instance (the honest open state). Per the anti-laundering rule, axiomatizing the class is not a proof of the bound.",
    },
  ],
});
