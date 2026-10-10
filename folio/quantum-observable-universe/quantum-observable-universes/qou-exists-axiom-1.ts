import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:qou-exists-axiom-1",
  lean: { ref: "qou:QOU.QuantumObservableUniverse.exists_axiom_1_frobenius",
    validation: "not_checked",
  },
  title: "Axiom 1 — Haar state gives a non-degenerate Frobenius pairing",
  tags: ["haar-state", "frobenius-pairing", "non-degenerate", "woronowicz"],
  uses: [],
  proofs: ["prf:qou-exists-axiom-1"],
  cites: ["woronowicz1987"],
});
