import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:categorical-neutrality-saturated-shells",
  title:
    "Proposition (categorical neutrality of saturated shells): the full-twist acts trivially on $\\Phi_n$ at magic $n$",
  lean: {
    ref: "qou:QOU.ShellNeutrality.SaturatedShellConjecture",
    validation: "not_checked",
  },
  uses: [
    "conj:mass-endomorphism",
    "def:hecke-mass-element",
    "prop:categorical-mass-markov",
    "prop:hoefsmit-seminormal-form",
    "thm:wedderburn-mass-formula",
  ],
  cites: [
    "kassel1995",
    "geckpfeiffer2000",
    "ariki1996",
    "jucys1974",
    "murphy1992",
    "mathas1999",
  ],
  tags: [
    "magic-numbers",
    "shell-closure",
    "full-twist",
    "global-section",
    "categorical-neutrality",
    "ribbon-element",
    "framing-anomaly",
    "open-problem",
  ],
});
