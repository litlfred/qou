import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:qns-shell-tail-collapse",
  lean: {
    ref: "qou:QOU.FluidDynamics.PhysicalLayerLeray.trajectory_tail_collapse",
  },
  title:
    "Per-amplitude tail collapse in the discrete $q$-shell hierarchy",
  uses: ["def:qns-unit-layers"],
  tags: [
    "navier-stokes",
    "fluid-dynamics",
    "shell-model",
    "tail-bounds",
    "millennium-problem",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-08-15",
      body:
        "All six Lean declarations sorry-free in " +
        "`QOU/FluidDynamics/physical_layer_leray.lean` (PRs #5066, #5072, " +
        "#5078); lean-direct exit 0 against the real import cone. " +
        "Hypothesis-carrying discrete style throughout — the DN " +
        "per-amplitude step and the dissipation-scale condition are " +
        "explicit hypotheses, never assumed of full NS.",
    },
    {
      kind: "note",
      body: "Lean declarations in `QOU.FluidDynamics.PhysicalLayerLeray`: `rung_equilibrium_forced` (1), `trajectory_ladder_bounds` (2), `trajectory_tail_collapse` (3), and `rung_equilibrium_two_source`, `two_source_ladder_collapse`, `trajectory_two_source_bounds`, `multi_source_ladder_uniform` (4).",
    },
  ],
});
