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
  lean: {
    decl: "QOU.Descartes.quantum_dilogarithm_volume",
    validation: "not_checked",
  },
  uses: [
    "thm:markov-trace-factorization",
    "prop:generator-volume-decomposition",
    "prop:topological-mass-formula",
    "def:quantum-planck-constant",
    "rem:quantum-dilogarithm",
    "prop:hadron-half-life",
  ],
});
