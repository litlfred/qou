import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:homological-shell-condensation",
  title:
    "Proposition (homological shell condensation): BB-stratified $E_\\infty^{p,>0}(n) = 0$ at magic $n$",
  lean: {
    ref: "qou:QOU.ShellCondensation.HomologicalConjecture",
    validation: "not_checked",
  },
  uses: [
    "ex:brane-tower-levels",
    "prop:gb-spectral-sequence",
    "prop:graded-trace-residue-split",
  ],
  cites: [
    "bialynicki1973",
    "yekutieli2010",
    "ariki1996",
  ],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-20",
      body: "**Citation mismatch (bean `qou-6qbv`).** The Setup cites `prop:gb-spectral-sequence` for a spectral sequence on the Białynicki-Birula filtration of the jet algebra $A_n$. That proposition is about the Hochschild complex of $H_n(R, q)$ filtered by Coxeter length, a different filtration on a different algebra, so it does not supply the sequence used here. This block's own $E_2$ statement is about its BB sequence and is not affected by the $H_3$ result ($d_2, d_4 \\neq 0$ for the length-filtered Hochschild sequence). Separately, the block is typed `proposition` while its statement is labelled a conjecture and carries the `open-problem` tag; the kind is left for the owner.",
    },
  ],
  tags: [
    "magic-numbers",
    "shell-closure",
    "spectral-sequence",
    "BB-stratification",
    "brane-tower",
    "homological-condensation",
    "open-problem",
  ],
});
