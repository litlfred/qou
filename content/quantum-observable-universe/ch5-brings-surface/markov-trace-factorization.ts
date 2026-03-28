import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:markov-trace-factorization",
  title:
    "Exact factorization of the nuclear Markov trace",
  tags: [
    "markov-trace",
    "factorization",
    "jones-polynomial",
    "link-invariant",
    "hecke-algebra",
    "chebyshev",
    "generator-volume",
    "nuclear",
  ],
  lean: {
    decl: "QOU.Descartes.markov_trace_factorization",
    validation: "not_checked",
  },
  uses: [
    "prop:generator-volume-decomposition",
    "thm:groebner-shirshov-energy",
    "prop:nuclear-groebner-reduction",
    "def:braid-group",
    "def:stable-nucleus",
    "def:skein-binding-lagrangian",
    "prop:local-substrate-q",
  ],
});
