import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note.** This block's `lean.ref` resolves into " +
        "`lean/QOU/FeynmanPathIntegrals.lean`, which is archimedean because " +
        "of its **ε–δ limit statements**: `speed_diverges_at_one (ε : ℝ) " +
        "(hε : 0 < ε) : ∃ δ, 0 < δ ∧ ∀ q, 0 < q - 1 → q - 1 < δ → …`, and the " +
        "`classical_limit` field `∀ ε > 0, ∃ δ > 0, … |qNum q m - (m : ℝ)| < ε`. " +
        "A quantifier alternation over arbitrarily small positive quantities " +
        "is the archimedean property itself; it has no generic-ring form. " +
        "The Hecke/Markov content the proposition identifies with the " +
        "transition amplitude remains generic upstream — this file is the " +
        "`q → 1` degeneration side of the wall.",
    },
  ],
  label: "prop:feynman-categorical-trace",
  lean: { ref: "qou:QOU.FeynmanPathIntegrals.FeynmanCategoricalTrace",
    validation: "not_checked",
  },
  title: "Feynman transition amplitude as categorical trace",
  tags: ["path-integral", "feynman", "categorical-trace", "markov-trace", "eigenbasis"],
  uses: ["prop:categorical-mass-markov"],
  proofs: ["prf:feynman-categorical-trace"],
});
