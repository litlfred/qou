import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:graded-markov-trace-from-gs-filtration",
  title:
    "Graded Markov trace as the induced trace on $J^\\ell / J^{\\ell+1}$",
  lean: {
    ref: "qou:QOU.BraidKnot.GradedMarkovTraceFromGSFiltration",
    validation: "not_checked",
  },
  cites: [
    "kassel1995",
    "geckpfeiffer2000",
    "ariki1996",
    "mathas1999",
  ],
  tags: [
    "graded-trace",
    "gb-filtration",
    "markov-trace",
    "associated-graded",
    "spectral-sequence",
    "narrative-replacement",
  ],
});
