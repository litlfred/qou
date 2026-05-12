import QOU.Hecke.MarkovTraceProduct

/-!
# QOU.Hecke.MarkovPairZ2 — All-pairs Markov-trace identity

For adjacent generators σ_i, σ_j with `|i - j| = 1`, the Markov
trace satisfies

  tr_M(σ_i · σ_j) = z²

where z is the Markov parameter `1/(v + v⁻¹)` (with `v² = q` the
formal square root of the substrate parameter).  This follows from
two applications of the Markov property:

  tr_M(σ_i σ_j) = z · tr_M(σ_i)  (peel σ_j)
                = z · z = z².

The identity is the **depth-2 cap** of the all-pairs jet-tower
formula in `prop:mass-endomorphism-tower` — pairs are the largest
`|S|` at which the Markov property preserves closure
([forward-derivation §A Step 17](../../../docs/audits/2026-05-02-forward-derivation-pre-archimedean.md)).

**Pre-Archimedean (formal-chain) version.**  Polymorphic in the
ground ring `R_q = ℤ[q^±1]`.  Conditional on a `MarkovTraceAxioms`
instance.

**Parallel formalisations.** This chain-list version coexists with
the algebra-level version in `Hecke/MarkovTrace.lean`
(`theorem QOU.Hecke.MarkovTrace.trace_pair`, currently a `sorry`)
and the heavier `Interactions/MarkovPeel.lean` (`class MarkovTrace`
with peeling axioms).  The chain-list version is the lightweight
form used by the audit's downstream consumers; the algebra-level
version is the full-Hecke-algebra statement.

LaTeX label: `prop:markov-pair-z2`

## References

- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
- [jones1987] https://doi.org/10.2307/1971403
-/

namespace QOU.Hecke

/-- The Markov-trace value of an adjacent pair `[c₁, c₂]`,
    conditional on a `MarkovTraceAxioms z` instance.  Two cons-axiom
    applications give

      `trace [c₁, c₂] = vertexVolume z c₁ · vertexVolume z c₂`. -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
theorem markov_pair_value
    {z : R_q} [inst : MarkovTraceAxioms z]
    (c₁ c₂ : GeneratorChain) :
    MarkovTraceAxioms.trace (z := z) [c₁, c₂] =
      vertexVolume z c₁ * vertexVolume z c₂ := by
  rw [markov_trace_product_recursion]
  simp [chainProduct, mul_assoc]

/-- **All-pairs Markov-trace identity (depth-2 cap).**

    For an adjacent pair of "trivial" generator chains (each chain
    is `σ_i · 1 + 0`, i.e. the bare braid generator at index `i`),
    each `vertexVolume` equals `z`, so the pair's trace is `z²`. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
theorem markov_pair_z2
    {z : R_q} [inst : MarkovTraceAxioms z]
    (i j : ℕ)
    (hi : (⟨i, 1, 0⟩ : GeneratorChain).a = 1)
    (hi₀ : (⟨i, 1, 0⟩ : GeneratorChain).b = 0)
    (hj : (⟨j, 1, 0⟩ : GeneratorChain).a = 1)
    (hj₀ : (⟨j, 1, 0⟩ : GeneratorChain).b = 0) :
    MarkovTraceAxioms.trace (z := z)
        [⟨i, 1, 0⟩, ⟨j, 1, 0⟩] = z * z := by
  rw [markov_pair_value]
  simp [vertexVolume, hi, hi₀, hj, hj₀]

end QOU.Hecke
