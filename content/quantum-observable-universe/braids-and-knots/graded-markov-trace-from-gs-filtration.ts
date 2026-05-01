import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:graded-markov-trace-from-gs-filtration",
  title:
    "Graded Markov trace from the Gröbner-Shirshov filtration on $H_n(R, q)$",
  lean: {
    ref: "qou:QOU.BraidKnot.graded_markov_trace_from_gs_filtration",
    validation: "not_checked",
  },
  uses: [
    "thm:jones-markov-trace",
    "prop:gb-spectral-sequence",
    "prop:graded-trace-residue-split",
  ],
  cites: ["bokut1978", "shirshov1962", "buchberger1965"],
  tags: [
    "markov-trace",
    "gs-filtration",
    "groebner-shirshov",
    "graded-piece",
    "hecke-algebra",
    "narrative-anchor",
  ],
});
