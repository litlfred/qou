import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:categorical-neutrality-saturated-shells",
  title:
    "Proposition 1. Categorical neutrality of saturated shells (full-twist trivial action)",
  lean: {
    ref: "qou:QOU.BraidKnot.ShellNeutrality.SaturatedShellConjecture",
    validation: "not_checked",
  },
  uses: [
    "conj:mass-endomorphism",
    "prop:hoefsmit-seminormal-form",
    "prop:shell-closure-stability",
  ],
  cites: [
    "kassel1995",
    "turaev2010",
    "mathas1999",
    "jucys1974",
    "murphy1992",
    "hoefsmit1974",
  ],
  tags: [
    "full-twist",
    "ribbon",
    "hecke-center",
    "jucys-murphy",
    "self-conjugate",
    "shell-closure",
    "global-section",
    "open-problem",
    "axiom-class",
  ],
});
