import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:qou-exists-axiom-2",
  lean: { ref: "qou:QOU.QuantumObservableUniverse.exists_axiom_2_observability",
    validation: "not_checked",
  },
  title: "Axiom 2 — observability via Peter--Weyl decomposition",
  tags: ["peter-weyl", "observability", "adjoint-action", "compact-quantum-group"],
  uses: [],
  proofs: ["prf:qou-exists-axiom-2"],
  cites: ["woronowicz1988"],
});
