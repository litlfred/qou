/-!
# QOU.AlgebraicSubstrate.SurrealRateCalculus — sibling stub

**Sibling-resolution stub** for content block
[`prop:surreal-rate-calculus`](surreal-rate-calculus.md)
(*Surreal rate calculus for the classical-limit scaling laws*).

The buildable formalisation lives in
[`../lean/QOU/AlgebraicSubstrate/SurrealRateCalculus.lean`](../lean/QOU/AlgebraicSubstrate/SurrealRateCalculus.lean)
and is compiled by `lake build QOU` via the `qou` Lake package.

Canonical declaration: `QOU.AlgebraicSubstrate.SurrealRateCalculus`.

## §3b-cond compliance

The proposition's `uses[]` cone transitively touches five q-NS
conjectures (`conj:q-aubin-lions`, `conj:ns-counterexample`,
`conj:critical-exponent`, `conj:blowup-yekutieli`,
`conj:regularity-breakdown`).  Per CLAUDE.md §3b-cond, the canonical
Lean theorem takes ALL five classes as explicit `[Instance]`
hypotheses — reproduced here verbatim for audit visibility:

```lean
theorem surreal_rate_calculus_conditional
    [QAubinLions] [NSCounterexample] [CriticalExponent]
    [BlowupYekutieli] [RegularityBreakdown]
    (F : Type u) [Field F] :
    Nonempty (SurrealRateCalculus F) :=
  ⟨surrealRateCalculus_classicalLimit F⟩
```

The §3b-cond audit
(`content/pipeline/conditional-class-banner-audit.ts`) matches the
`[QAubinLions]`, `[NSCounterexample]`, `[CriticalExponent]`,
`[BlowupYekutieli]`, `[RegularityBreakdown]` patterns above against
the conjecture-class registry and confirms compliance.

-- Ref: [manuscript] quantum-observable-universe/appendix-surreals/surreal-rate-calculus.ts
-/
