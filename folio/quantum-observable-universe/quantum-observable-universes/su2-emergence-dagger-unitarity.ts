import { lemma } from "../../schema/builders";

export default lemma({
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-21",
      body: "**Lean scope (disclosure, not a change of claim).** The `lean.ref` theorem proves the linear-algebra tail only: a 2×2 complex matrix that preserves the standard inner product lies in U(2) (`su2_emergence_gauge_group_unitary` lifts this to a set). The categorical premise, that the gauge group G preserves a positive-definite Hermitian form on the two-dimensional image τ(V), is not formalised; neither are the sesquilinear structure, positive-definiteness, the action of S(f) on morphisms, or dim τ(V) = 2. Found by the blind round-trip audit (docs/audits/2026-11-20-roundtrip-blind-audit-pass1.md, block B03; bean qou-1iit).",
    },
  ],
  label: "lem:su2-emergence-dagger-unitarity",
  lean: { ref: "qou:QOU.su2_emergence_dagger_unitarity",
    validation: "not_checked",
  },
  title: "Frobenius dagger forces $G \\subseteq \\mathrm{U}(2)$",
  tags: ["frobenius", "dagger", "unitarity", "u2"],
  uses: [
    "prop:fiber-adjoint-involution",
    "prop:positive-definite-dagger",
  ],
  proofs: ["prf:su2-emergence-dagger-unitarity"],
});
