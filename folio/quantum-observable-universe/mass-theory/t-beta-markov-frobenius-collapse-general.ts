import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:t-beta-markov-frobenius-collapse-general",
  title:
    "Min-Frobenius-norm collapse: T_β = S · 1_A — general unital R-algebra lift of [prop:t-beta-markov-frobenius-collapse]",
  lean: {
    ref: "qou:QOU.QBeta.MarkovFrobeniusCollapse.General.markov_frobenius_min_norm_twisted",
    validation: "not_checked",
  },
  uses: [
    "prop:t-beta-markov-frobenius-collapse",
    "prop:markov-trace-frobenius-selection",
  ],
  cites: ["jones1987", "wenzl1988"],
  tags: [
    "markov-trace",
    "frobenius",
    "q-beta",
    "min-norm",
    "categorical-collapse",
    "general-lift",
    "typeclass",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-22",
      body: "**Theorem (sorry-free).** Restated with the twisted form $\\tau(X \\cdot X^\\dagger)$ on owner ruling 2026-11-22 (bean `qou-baov`). Declarations in the sibling `t-beta-markov-collapse-general-lift.lean`, namespace `QOU.QBeta.MarkovFrobeniusCollapse.General`: `completing_the_square_twisted`, `markov_frobenius_min_norm_twisted` (the bound, under `TwistedPSDTrace`) and `markov_frobenius_min_norm_twisted_uniqueness` (the equality case, under `TwistedNonDegTrace`). The untwisted declarations (`markov_frobenius_min_norm_lift`, `_uniqueness`) are the case $\\dagger = \\mathrm{id}$. The library file `QOU/QBeta/MarkovFrobeniusCollapse/General.lean`, whose `markov_frobenius_min_norm_lift` only projected its own hypothesis, is removed.",
    },
  ],
});
