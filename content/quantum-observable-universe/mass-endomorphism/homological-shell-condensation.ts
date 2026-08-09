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
