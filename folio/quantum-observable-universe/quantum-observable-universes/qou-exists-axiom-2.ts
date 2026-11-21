import { lemma } from "../../schema/builders";

export default lemma({
  authorNotes: [
    { kind: "caveat", date: "2026-11-21", body: "Lean now states the claim with an honest `sorry`; the field `total_hom_dim_eq`, which was the conclusion, is deleted (round-trip audit pass 2, C06). The statement needs a reading. For the adjoint coaction of $\\mathcal{O}_q(G)$ on itself the invariants are the class functions, one per dominant weight by Peter--Weyl, so the claim is false in that reading. It holds for the adjoint representation of the Lie algebra $\\mathfrak{g}$ (or $U_q(\\mathfrak{g})$), whose invariants vanish for semisimple $\\mathfrak{g}$. Condition (3) of the definition inherits this ambiguity." },
  ],
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
