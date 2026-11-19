import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:substrate-consistency-window",
  lean: { ref: "qou:QOU.Observations.substrate_consistency_window", validation: "not_checked" },
  title: "Overdetermination of the aether parameter",
  tags: [
    "substrate-parameter",
    "testable-prediction",
    "consistency",
    "fine-structure",
    "mass-ratio",
    "half-life",
    "speed-of-light",
  ],
  uses: [
    "rem:fine-structure-observation",
    "prop:crossing-energy-decomposition",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The `ℝ` of `substrate_consistency_window.lean` are **measurement " +
        "windows**: `epsilon : ℕ → ℝ` is the half-width of the measurement " +
        "window for each independent measurement class, and `q_lo k = q* - ε " +
        "k`, `q_hi k = q* + ε k` are that class's experimental bounds on the " +
        "substrate parameter. The whole content of the block is that " +
        "independent *measurements* overdetermine `q` and their ranges " +
        "overlap, so the `ℝ` is forced by the statement rather than chosen.",
    },
  ],
});
