import { proof } from "../../schema/builders";

export default proof({
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note.** The proof shares " +
        "`lean/QOU/FeynmanPathIntegrals.lean` with the proposition it " +
        "discharges. Its `ℝ` are load-bearing at the point where the argument " +
        "actually needs them: `qNum_pos {q : ℝ} (hq : 0 < q) (hq1 : q ≠ 1) " +
        "(hn : 0 < n)` is a **strict-positivity** step (closed by " +
        "`positivity`/`linarith`), and the `q → 1` degeneration is stated as " +
        "an ε–δ limit. Positivity and limits are archimedean; the algebraic " +
        "steps (`hecke_degeneration_symmetric`, `planck_at_one` by `ring`) " +
        "would generalise, but they cannot be separated from the limit " +
        "argument they serve without splitting the proof in two. Kept whole " +
        "on the archimedean side, per §7c's \"place the specialisation after " +
        "the wall\" rather than interleave.",
    },
  ],
  label: "prf:feynman-categorical-trace",
  lean: { ref: "qou:QOU.FeynmanPathIntegrals.abs_amplitude_eq_abs_markovTrace",
    validation: "not_checked",
  },
  title: "Proof of Feynman transition amplitude as categorical trace",
  uses: [
    "prop:feynman-categorical-trace",
    "lem:feynman-markov-identification",
    "prop:categorical-mass-markov",
  ],
});
