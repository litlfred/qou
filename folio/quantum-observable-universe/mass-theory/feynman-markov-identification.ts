import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:feynman-markov-identification",
  lean: { ref: "qou:QOU.FeynmanPathIntegrals.markov_identification_of_markovTrace",
    validation: "not_checked",
  },
  title: "Markov-weighted eigenbasis sum equals the Markov trace",
  tags: ["markov-trace", "wedderburn", "feynman", "hecke", "identification"],
  uses: ["thm:jones-markov-trace"],
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
      date: "2026-11-18",
      body:
        "**Rewritten 2026-11-18.** The `lean.ref` was `markov_identification`, which takes the branching " +
        "identity as a hypothesis. It now points to `markov_identification_of_markovTrace`, which proves it at " +
        "convention D. The weight $\\dim_q(V_\\lambda)\\dim(S_\\lambda)/\\dim_q(V^{\\otimes n})$ was wrong by " +
        "the factor $\\dim S_\\lambda$ and is replaced by the Ocneanu weight, which equals " +
        "$\\dim_q(V_\\lambda)/\\dim_q(V^{\\otimes n})$ on two-row partitions and vanishes on the rest. " +
        "Base ring $\\mathbb{R}$, forced by `seminormalRep`.",
    },
  ],

});
