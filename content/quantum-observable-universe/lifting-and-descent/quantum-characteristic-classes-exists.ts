import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-08-08",
      body:
        "**Lean sibling proves a degenerate witness, and drops the " +
        "quantifier.** `QOU.QuantumCharClasses.exists` is " +
        "`Nonempty QuantumCharacteristicClass.{0}` — a *single* inhabitant " +
        "with `κ = 0` over `ℤ` — while the statement above asserts existence " +
        "*for every* $n \\ge 0$ (Class B scope mismatch on top of the " +
        "degenerate witness). Restoring the quantifier is statable, since " +
        "`QuantumCharacteristicClass` has a `level` field, but it was " +
        "deliberately not done: a `∀ n` over classes that are all zero is no " +
        "less vacuous than one, and would only make the theorem read as " +
        "stronger. The obstruction claim itself — that $\\kappa_n$ obstructs " +
        "the lift $\\mathfrak{G}_n \\to \\mathfrak{G}_{n+1}$ — is unstatable " +
        "against the type, which carries no lift. Blocked on gerbe " +
        "infrastructure not yet in Mathlib. Narrative audit: " +
        "`docs/audits/2026-08-08-narrative-lean-equivalence-nonempty-kernels.md`.",
      see: "docs/audits/2026-08-08-narrative-lean-equivalence-nonempty-kernels.md",
    },
  ],
  label: "prop:quantum-characteristic-classes-exists",
  title: "Existence of quantum characteristic classes",
  lean: { ref: "qou:QOU.QuantumCharClasses.exists",
    validation: "not_checked",
  },
  uses: ["def:quantum-characteristic-classes"],
  proofs: ["prf:quantum-characteristic-classes-exists"],
  tags: ["existence", "characteristic-classes", "cohomology"],
});
