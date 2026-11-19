import { proof } from "../../schema/builders";

export default proof({
  label: "prf:markov-trace-factorization",
  title: "Proof of markov trace factorization",
  uses: ["thm:markov-trace-factorization"],
  computation: {
    engine: "python+mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: [
      "computations/q-pinning-50-digit.witness.json",
      "computations/probes/toffoli-published-vs-construction.witness.json",
      "computations/probe-markov-trace-factorization.witness.json",
    ],
    status: "verified",
  },
});
