import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:diagrammatic-double-magic-lr-fusion",
  title:
    "Proposition 3. Diagrammatic double-magic and LR-fusion rigidity",
  lean: {
    ref: "qou:QOU.Interactions.LRFusion.DoubleMagicConjecture",
    validation: "not_checked",
  },
  uses: [
    "conj:categorical-neutrality-saturated-shells",
    "conj:homological-shell-condensation",
    "prop:magic-numbers-from-q",
    "conj:mass-endomorphism",
  ],
  cites: [
    "mathas1999",
    "kassel1995",
    "turaev2010",
    "jucys1974",
    "murphy1992",
  ],
  tags: [
    "littlewood-richardson",
    "fusion",
    "double-magic",
    "self-conjugate",
    "jucys-murphy",
    "shell-closure",
    "open-problem",
    "axiom-class",
  ],
});
