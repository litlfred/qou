import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:trm-hopf-sigma1-sq-closed-form",
  proofs: ["prf:trm-hopf-sigma1-sq-closed-form"],
  lean: {
    ref: "qou:QOU.Braiding.TrMHopfSigma1SqClosedForm",
    validation: "not_checked",
  },
  title: "Closed form for the canonical Markov trace of σ_1² (Hopf+ braid)",
  tags: ["hecke-algebra", "markov-trace", "closed-form", "hopf-braid", "binomial-series"],
  uses: ["thm:jones-markov-trace"],
});
