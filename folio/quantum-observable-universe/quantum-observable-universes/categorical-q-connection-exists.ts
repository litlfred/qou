import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-q-connection-exists",
  title: "Existence of the categorical $q$-connection",
  lean: { ref: "qou:QOU.CategoricalQConnection.exists",
    validation: "not_checked",
  },
  uses: [
    "def:categorical-q-connection",
    "prop:categorical-connection-exists",
    "def:substrate-parameter",
  ],
  proofs: ["prf:categorical-q-connection-exists"],
  tags: ["existence", "q-connection"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-22",
      body: "**Statement restated 2026-11-22 to what the Lean proves (owner ruling, round-trip pass 3).** `CategoricalQConnection.exists` builds the structure directly from its inputs, with `nabla_q` set to the formula q⁻¹∇ + (1 − q⁻¹)(ι_ξ∇ ≫ θ_∇) and `nabla_q_formula := rfl`; the existence is a definition, and the inputs ∇, ι_ξ∇, θ_∇ are arbitrary morphisms with no connection axiom imposed. The former one-sentence statement read as an existence theorem for a given universe's connection, with codomain Ω¹(A); the Lean codomain is A ⊗ Ω¹. Found by the blind round-trip audit (docs/audits/2026-11-22-roundtrip-blind-audit-pass3.md, block P19).",
    },
  ],
});
