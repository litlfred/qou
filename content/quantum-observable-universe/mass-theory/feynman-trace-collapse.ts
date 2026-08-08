import { lemma } from "../../schema/builders";

export default lemma({
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note.** The collapse is stated in " +
        "`lean/QOU/FeynmanPathIntegrals.lean` via " +
        "`class MarkovIdentification (sumWeightedTraces markovTrace : ℝ)`, " +
        "whose surrounding content is the `q → 1` degeneration expressed as " +
        "ε–δ limits (`speed_diverges_at_one`, `planck_limit`). The lemma's " +
        "own arithmetic — `planck_at_one : (1 : ℝ) - (1 : ℝ)⁻¹ = 0` closed by " +
        "`ring`, and `q_energy_classical_limit` — is generic in shape, but it " +
        "exists to feed those limits, and the numeric constants it collapses " +
        "to are the archimedean substrate values. Placed after the wall " +
        "deliberately.",
    },
  ],
  label: "lem:feynman-trace-collapse",
  lean: { ref: "qou:QOU.FeynmanPathIntegrals.trace_collapse",
    validation: "not_checked",
  },
  title: "Path integral collapses to a finite sum on the eigenbasis",
  tags: ["feynman", "path-integral", "trace-collapse", "semisimplicity"],
  uses: ["lem:feynman-eigenbasis-decomposition"],
  proofs: ["prf:feynman-trace-collapse"],
});
