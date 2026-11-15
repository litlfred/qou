import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:qou-exists-axiom-3",
  lean: { ref: "qou:QOU.QuantumObservableUniverse.exists_axiom_3_chern",
    validation: "not_checked",
  },
  title: "Axiom 3 — vanishing categorical Chern classes for the adjoint bundle",
  tags: ["chern-class", "modular-tensor-category", "level", "tilting"],
  uses: [],
  proofs: ["prf:qou-exists-axiom-3"],
  cites: ["reshetikhin1991"],
});
