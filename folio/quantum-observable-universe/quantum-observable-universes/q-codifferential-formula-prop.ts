import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-codifferential-formula",
  title: "Closed formula for the $q$-codifferential $\\delta_q$",
  tags: ["codifferential", "reeb", "adjoint", "webster"],
  lean: { ref: "qou:QOU.QuantumGeometry.q_codifferential_formula",
    validation: "not_checked",
  },
  uses: [
    "def:categorical-q-ext-deriv",
    "ex:reeb-decomposition",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-09-04",
      body:
        "**Sibling `.lean` rewritten; it now declares no `axiom`.** The previous " +
        "version asserted the contact-form data as 13 standalone axioms over an " +
        "opaque `axiom DiffForm : Type u`. It is now a `structure " +
        "ContactFormAlgebra R F` over `[AddCommGroup F] [Module R F]`, with the " +
        "Webster pairing typed `F →ₗ[R] F →ₗ[R] R` and the six geometric " +
        "operators typed `F →ₗ[R] F`; every declaration `#print axioms` to " +
        "`[propext, Quot.sound]`. The closed formula is derived from three " +
        "adjointness fields plus bilinearity, and holds for *every* such " +
        "structure rather than for one opaque constant. No **geometric** model " +
        "is built — that residual gap is now carried in the hypotheses of each " +
        "statement rather than in the axiom list.",
    },
    {
      kind: "caveat",
      date: "2026-09-04",
      body:
        "**The uniqueness clause in the prose is an analytic fact, not a formal " +
        "one.** Over compactly supported forms with the real $L^2$ Webster " +
        "inner product the pairing is non-degenerate, so \"uniquely " +
        "characterised\" is correct as written. The Lean is stated over an " +
        "arbitrary commutative ring and an arbitrary bilinear pairing, where " +
        "non-degeneracy does **not** come for free: `δq_unique` takes it as an " +
        "explicit hypothesis, and `degenerate_adjoint_not_unique` exhibits a " +
        "model of the remaining structure in which the adjoint is not unique " +
        "(the identically zero pairing). The retired axiom " +
        "`adjoint_exists_unique'` asserted `∃!` with no such hypothesis, and " +
        "for an arbitrary — not necessarily linear — operator.",
    },
  ],
});
