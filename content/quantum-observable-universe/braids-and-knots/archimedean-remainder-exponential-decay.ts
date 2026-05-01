import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:archimedean-remainder-exponential-decay",
  title:
    "Exponential decay of the archimedean remainder $|\\mathcal{V}_{\\mathrm{hyp}} - \\mathcal{A}_n| = O(e^{-cn})$",
  lean: {
    ref: "qou:QOU.ArchimedeanRemainder.DecayConjecture",
    validation: "not_checked",
  },
  uses: [
    "def:archimedean-realization-functor",
    "def:algebraic-quantum-volume",
    "conj:kashaev-volume-conjecture",
    "thm:markov-trace-product",
  ],
  cites: [
    "kashaev1997",
    "murakami-murakami2001",
    "zagier1986",
    "neumann-zagier1985",
  ],
  tags: [
    "archimedean-remainder",
    "exponential-decay",
    "picard-lefschetz",
    "laplace-method",
    "quantum-dilogarithm",
    "kashaev-asymptotics",
    "open-problem",
    "axiom-class",
  ],
});
