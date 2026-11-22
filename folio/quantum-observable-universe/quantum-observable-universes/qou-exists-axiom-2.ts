import { lemma } from "../../schema/builders";

export default lemma({
  authorNotes: [
    { kind: "caveat", date: "2026-11-21", body: "Lean now proves the Lie-algebra statement sorry-free: over a field with $2 \\neq 0$ the adjoint module of $\\mathfrak{sl}_2$ has no nonzero invariant vector (`maxTrivSubmodule = ⊥`), i.e. $\\mathrm{Hom}(\\mathbf{1}, V_1) = 0$. The generic-$q$ step for $U_q(\\mathfrak{sl}_2)$ is cited, not formalised. The earlier class of free naturals, whose field `total_hom_dim_eq` was the conclusion, is gone (round-trip audit pass 2, C06; QA on #8888). The statement is the Lie-algebra one (title and .md say so). The other reading, the adjoint coaction of $\\mathcal{O}_q(G)$ on itself, is excluded: there the invariants are the class functions, one per dominant weight by Peter--Weyl, so the claim would be false." },
  ],
  label: "lem:qou-exists-axiom-2",
  lean: { ref: "qou:QOU.QuantumObservableUniverse.exists_axiom_2_observability",
    validation: "not_checked",
  },
  title: "Axiom 2 — the adjoint representation of $\\mathfrak{sl}_2$ has no invariants",
  tags: ["observability", "adjoint-action", "lie-algebra", "sl2"],
  uses: [],
  proofs: ["prf:qou-exists-axiom-2"],
  cites: ["woronowicz1988"],
});
