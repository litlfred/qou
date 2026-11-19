import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:jones-markov-trace",
  lean: { ref: "qou:QOU.Braiding.JonesMarkovTrace",
    validation: "not_checked",
  },
  title: "Existence and non-degeneracy of the Markov trace (Jones, 1987)",
  tags: ["hecke-algebra", "markov-trace", "jones-polynomial", "external-proof"],
  uses: ["prop:braid-action-tensor", "prop:braiding-eigenvalue-extraction"],
  computation: {
    engine: "sympy",
    script: "computations/markov/markov_trace_recursive.py",
    witness: "computations/markov/markov-trace-recursive.witness.json",
    status: "verified",
  },
});
