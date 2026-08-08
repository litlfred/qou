import { remark } from "../../schema/builders";

export default remark({
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note.** This remark interprets exactly the " +
        "archimedean part of `lean/QOU/FeynmanPathIntegrals.lean`: the " +
        "`ClassicalLimit` fields `planck_limit : ∀ (ε : ℝ), 0 < ε → ∃ (δ : ℝ), " +
        "0 < δ ∧ ∀ (q : ℝ), …` and the quantum-dimension convergence " +
        "`|qNum q m - (m : ℝ)| < ε`. The classical limit *is* a statement " +
        "about arbitrarily small positive reals, so `ℝ` is not a " +
        "specialisation of this content — it is the content. Nothing here " +
        "generalises to a base ring without an ordering.",
    },
  ],
  interprets: "prop:feynman-classical-limit",
  label: "rem:feynman-classical-limit-interpretation",
  lean: { ref: "qou:QOU.FeynmanPathIntegrals.jones_trace_generator_at_one",
    validation: "not_checked",
  },
  title: "Classical limit and the symmetric degeneration",
  tags: ["path-integral", "classical-limit", "symmetric-group", "specht-module"],
  uses: ["prop:feynman-classical-limit"],
});
