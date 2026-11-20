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

**Unconditional.** Both theorems below hold for every genuine Markov
(Ocneanu) trace `T` on an `R_q`-algebra. Until 2026-11-20 they were stated
conditional on a class `MarkovTraceAxioms z` whose axioms were the product
recursion itself, so they held by definition (bean `qou-ltwg`).

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

variable {A : Type*} [Ring A] [Algebra R_q A]

/-- The Markov-trace value of an adjacent pair of chains `[c₁, c₂]` placed on
    `σ_n, σ_{n+1}`: `tr_M = V̂(c₁) · V̂(c₂)`, for every genuine Markov trace. -/
-- Ref: [jones1987] §5 (The Markov trace)
theorem markov_pair_value (T : QOU.MathlibExt.OcneanuTrace.MarkovTrace R_q A)
    (c₁ c₂ : GeneratorChain) (n : ℕ) :
    T.tr (chainListWord T [c₁, c₂] n) = vertexVolume T.z c₁ * vertexVolume T.z c₂ := by
  rw [markov_trace_product]
  simp [chainProduct]

/-- **Adjacent-pair Markov-trace identity** `tr_M(σ_i · σ_{i+1}) = z²`, for
    every genuine Markov trace and every `i`. -/
-- Ref: [kassel1995] Ch. X (Hecke algebras and Markov trace)
theorem markov_pair_z2 (T : QOU.MathlibExt.OcneanuTrace.MarkovTrace R_q A) (i : ℕ) :
    T.tr (T.g i * T.g (i + 1)) = T.z * T.z :=
  T.tr_g_mul_g_succ i

end QOU.Hecke
