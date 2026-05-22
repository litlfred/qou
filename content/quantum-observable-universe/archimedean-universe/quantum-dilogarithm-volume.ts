import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:quantum-dilogarithm-volume",
  title:
    "Nuclear energy from the quantum dilogarithm of the Markov trace",
  tags: [
    "quantum-dilogarithm",
    "volume",
    "markov-trace",
    "generator-volume",
    "intensive",
    "binding-energy",
    "q-value",
    "topological-mass",
  ],
  lean: { ref: "qou:QOU.Descartes.quantum_dilogarithm_volume",
    validation: "not_checked",
  },
  uses: [
    "thm:markov-trace-factorization",
    "cor:quantum-dilogarithm",
  ],
});
