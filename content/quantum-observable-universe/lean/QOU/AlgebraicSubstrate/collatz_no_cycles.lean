/-!
# QOU.AlgebraicSubstrate.collatz_no_cycles — placeholder stub

**Placeholder canonical** for content block at
[`quantum-observable-universe/appendix-surreals/collatz-no-cycles.ts`](quantum-observable-universe/appendix-surreals/collatz-no-cycles.ts).

The full Lean statement is pending; this stub exists so the
`lean.ref` URI `qou:QOU.AlgebraicSubstrate.collatz_no_cycles` resolves to a real declaration in the `qou`
Lake package.
-/

namespace QOU.AlgebraicSubstrate


/-- Abstract context for the `collatz_no_cycles` claim — fields encode the
    manuscript hypotheses; the `holds` field is the substantive
    claim of the lemma. -/
class CollatzNoCyclesContext where
  /-- The `Prop`-valued claim of the lemma (see docstring on
      `collatz_no_cycles` below for the manuscript statement). -/
  holds : Prop

/-- Placeholder for `collatz_no_cycles` (no manuscript-statement docstring found). -/
-- Ref: [manuscript] quantum-observable-universe/appendix-surreals/collatz-no-cycles.ts
theorem collatz_no_cycles [ctx : CollatzNoCyclesContext] : ctx.holds := by
  -- Manuscript proof referenced above; concretisation requires
  -- type-level Lean translation of the hypotheses.
  sorry

end QOU.AlgebraicSubstrate
