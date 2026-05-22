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
  lean: { ref: "qou:QOU.Descartes.markov_trace_factorization",
    validation: "not_checked",
  },
  uses: ["prop:generator-volume-decomposition", "thm:markov-trace-product"],
  computation: {
    engine: "mpmath",
    witness: "folio-assistant/computations/gram-matrix-dual.witness.json",
    status: "verified",
  },
});
