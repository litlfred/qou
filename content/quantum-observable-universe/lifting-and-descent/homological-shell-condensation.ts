import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:homological-shell-condensation",
  title:
    "Proposition 2. Homological shell condensation ($E_\\infty^{p, >0}(n) = 0$ at magic $n$)",
  lean: {
    ref: "qou:QOU.LiftingDescent.HomologicalCondensation.ShellCondensationConjecture",
    validation: "not_checked",
  },
  uses: [
    "conj:categorical-neutrality-saturated-shells",
    "prop:yekutieli-lifting",
    "cor:jet-prolongation-C",
    "prop:categorical-jet-prolongation",
    "conj:mass-endomorphism",
    "prop:magic-numbers-from-q",
  ],
  cites: [
    "yekutieli2010",
    "yekutieli2008",
    "yekutieli2015",
    "kassel1995",
    "mathas1999",
  ],
  tags: [
    "spectral-sequence",
    "bb-stratification",
    "yekutieli-jet",
    "magic-numbers",
    "shell-condensation",
    "homological",
    "open-problem",
    "axiom-class",
  ],
});
