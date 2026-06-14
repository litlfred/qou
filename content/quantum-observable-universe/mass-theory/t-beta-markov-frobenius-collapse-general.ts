import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:t-beta-markov-frobenius-collapse-general",
  title:
    "Min-Frobenius-norm collapse: T_β = S · 1_A — general unital R-algebra lift of [prop:t-beta-markov-frobenius-collapse]",
  lean: {
    ref: "qou:QOU.QBeta.MarkovFrobeniusCollapse.General.markov_frobenius_min_norm_lift",
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
      body: "**Theorem (sorry-free, LSP-verified).** Lean proof landed via [PR #1761](https://github.com/litlfred/qou/pull/1761) at namespace `QOU.QBeta.MarkovFrobeniusCollapse.General`.  Three sorry-free declarations + one reusable lemma:\n\n- `smul_one_sq` — reusable algebraic identity $(r \\cdot 1)(r \\cdot 1) = (r^2 \\cdot 1)$ over any unital $R$-algebra.\n- `completing_the_square_general` — the algebraic content of the Lagrangian proof, over $[\\mathrm{CommRing}\\, R]$.\n- `markov_frobenius_min_norm_lift` — the inequality $S^2 \\le \\tau(X \\cdot X)$ under $\\mathsf{PSDTrace}$.\n- `markov_frobenius_min_norm_uniqueness` — the equality case $\\tau(X \\cdot X) = S^2 \\Leftrightarrow X = S \\cdot 1$ under $\\mathsf{PSDTrace} + \\mathsf{NonDegTrace}$.\n\nSee sibling `.lean` file for the re-export.",
    },
  ],
});
