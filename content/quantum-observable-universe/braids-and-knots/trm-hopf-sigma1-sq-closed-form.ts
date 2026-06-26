import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", date: "2026-06-26", body: "While the derivation itself follows a standard Hecke/Markov calculation, this closed form represents the simplest nontrivial derived Markov-trace in the framework. The value-driven finding that the bare-Markov $\\epsilon^{2n}$ coefficients are *not* the $\\mathfrak{Q}_\\beta$ precision-ladder $c_n$ (meaning $F_n$ is a separate categorical decomposition) adds substantive novel mathematical content to the framework." },
  ],
  label: "prop:trm-hopf-sigma1-sq-closed-form",
  lean: {
    ref: "qou:QOU.Braiding.TrMHopfSigma1SqClosedForm",
    validation: "not_checked",
  },
  title: "Closed form for the canonical Markov trace of σ_1² (Hopf+ braid)",
  tags: ["hecke-algebra", "markov-trace", "closed-form", "hopf-braid", "binomial-series"],
  uses: ["thm:jones-markov-trace"],
});
