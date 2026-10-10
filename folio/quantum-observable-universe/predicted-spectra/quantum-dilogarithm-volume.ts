import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
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
  lean: { ref: "qou:QOU.Archimedean.quantum_dilogarithm_volume",
    validation: "not_checked",
  },
  uses: ["thm:markov-trace-factorization"],
});
