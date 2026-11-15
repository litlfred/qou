import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:qou-exists-axiom-4",
  lean: { ref: "qou:QOU.QuantumObservableUniverse.exists_axiom_4_volume",
    validation: "not_checked",
  },
  title: "Axiom 4 — categorical volume constraint via the quantum determinant",
  tags: ["volume-constraint", "quantum-determinant", "exterior-power", "ribbon"],
  uses: [],
  proofs: ["prf:qou-exists-axiom-4"],
  cites: ["kassel1995"],
});
