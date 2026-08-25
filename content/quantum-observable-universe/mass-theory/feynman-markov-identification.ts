import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:feynman-markov-identification",
  lean: { ref: "qou:QOU.FeynmanPathIntegrals.markov_identification",
    validation: "not_checked",
  },
  title: "Markov-weighted eigenbasis sum equals the Markov trace",
  tags: ["markov-trace", "wedderburn", "feynman", "hecke", "identification"],
  uses: ["lem:feynman-eigenbasis-decomposition", "thm:jones-markov-trace"],
  proofs: ["prf:feynman-markov-identification"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module `lean/QOU/FeynmanPathIntegrals/markov_identification.lean` " +
        "names specific values via module-level `opaque` constants (`markovTrace`, `markovWeight`, `spechtPartialTrace`); a polymorphic `opaque` would be a family of unrelated constants, so the `ℝ` is load-bearing. " +
        "The `ℝ` is therefore forced by the statement itself rather than " +
        "chosen, so the block sits on the archimedean side of the §7c wall " +
        "by construction.",
    },
  ],

});
