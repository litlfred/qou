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
      kind: "status",
      date: "2026-09-03",
      body:
        "**Branching identity derived at convention D.** `markovTrace_branching` is a named, unasserted proposition " +
        "on `main` (bean `qou-z9ws`). `QOU.FeynmanPathIntegrals.MarkovIdentificationInstance` now proves it " +
        "from `QOU.SchurWeyl.MarkovTraceInstance.eq_wtrace_of_markov` (every Markov trace at $z_D = q^3/(q^2+1)$ is the " +
        "Ocneanu-weighted seminormal trace, general $n$, sorry-free), so for that instance the decomposition " +
        "$\\mathrm{tr}_M = \\sum_\\lambda w_\\lambda\\,\\mathrm{tr}_{S_\\lambda}$ is a theorem with concrete " +
        "weights (Ocneanu) and partial traces (seminormal block traces); `markov_identification_of_markovTrace` is this " +
        "lemma for it. Convention D only; general $z$ remains open (bean `qou-gzgi`).",
    },
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
