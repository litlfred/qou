import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-18",
      body:
        "**Rewritten 2026-11-18.** The `lean.ref` was the structure `FeynmanCategoricalTrace`, whose field " +
        "`amplitude_eq_markov` assumed the identity. It now points to `abs_amplitude_eq_abs_markovTrace` in " +
        "`QOU/FeynmanPathIntegrals/MarkovIdentificationInstance.lean`, which derives it at convention D from " +
        "`eq_wtrace_of_markov`. Three statement errors were also fixed: the inverse Markov rule is " +
        "$(z - h)\\,\\mathrm{tr}_M(x)$, not $z^{-1}\\mathrm{tr}_M(x)$; the weight is " +
        "$\\dim_q(V_\\lambda)/\\dim_q(V^{\\otimes n})$, without the extra factor $\\dim S_\\lambda$; and the mass is " +
        "$|\\mathrm{tr}_M|$, not $\\mathrm{tr}_M$. Base ring $\\mathbb{R}$, forced by `seminormalRep`.",
    },
  ],
  label: "prop:feynman-categorical-trace",
  lean: { ref: "qou:QOU.FeynmanPathIntegrals.abs_amplitude_eq_abs_markovTrace",
    validation: "not_checked",
  },
  title: "Feynman transition amplitude as categorical trace",
  tags: ["path-integral", "feynman", "categorical-trace", "markov-trace", "eigenbasis"],
  uses: ["prop:categorical-mass-markov", "lem:feynman-markov-identification"],
  proofs: ["prf:feynman-categorical-trace"],
});
