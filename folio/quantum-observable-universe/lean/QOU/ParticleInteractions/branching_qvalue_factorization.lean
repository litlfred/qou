import Mathlib.Tactic

/-!
# QOU.ParticleInteractions.branching_qvalue_factorization — `Σ Δm_e = a^Z · b^{N−1} · (a − b)`

**Proposition** ([`prop:branching-qvalue-factorization`](../../../quantum-observable-universe/particle-interactions/branching-qvalue-factorization.md)).

*For `β⁻` decay of a nucleus `(Z, N)` with `A = Z + N`:*

```
  Σ_{all 4^A configs} Δ m_e = a^Z · b^{N−1} · (a − b)
```

*where `a = Σ_c G_P(c)` and `b = Σ_c G_N(c)` are the per-nucleon
channel sums over the four channels.*

## Lean structure — genuinely derived, not axiomatised

Earlier this block recorded the factorisation against an *abstract*
`totalDeltaM` field, which could only be asserted.  It is now **derived
sorry-free** from a concrete config-sum model:

1. **Concrete config sum.** `configSum g P` is the sum over all `4^P`
   channel assignments of `P` slots of the product of per-slot weights.
2. **Multiplicativity reduction (real content).** `configSum_eq` proves
   `configSum g P = (Σ_c g c)^P` via `Finset.prod_univ_sum` — the
   nucleon-independence / distributivity that turns the `4^A` sum into a
   product of per-nucleon channel sums.  This is the genuine combinatorial
   step, not an assumption.
3. **Total `Σ Δm_e` as a config-sum difference.** `totalDeltaM` is the
   daughter `(Z+1, N−1)` channel product minus the parent `(Z, N)` product
   — a concrete `def`, not a free field.
4. **Factorisation.** The theorem substitutes the reduction and factors by
   elementary algebra, using `0 < N` (so `b^N = b^{N−1}·b`).

## Base ring (§7c)

The whole derivation is `Finset.prod_univ_sum`, `pow_succ` and `ring`; the only
order hypothesis, `0 < N`, is on the neutron count in `ℕ`. So the channel
weights live in a generic `[CommRing R]` and the substrate evaluation is
`R := ℝ`.

-- Ref: [leitner2026] quantum-observable-universe/particle-interactions/branching-qvalue-factorization.md
-/

open Finset

namespace QOU.ParticleInteractions

variable {R : Type*} [CommRing R]

/-- Per-nucleon `Fin 4`-channel weights for the `β⁻` branching Q-value:
    `GP` for a proton, `GN` for a neutron. -/
structure BranchingChannels (R : Type*) [CommRing R] where
  /-- Proton per-channel weights `G_P(c)`. -/
  GP : Fin 4 → R
  /-- Neutron per-channel weights `G_N(c)`. -/
  GN : Fin 4 → R

namespace BranchingChannels

/-- Proton per-nucleon channel sum `a = Σ_c G_P(c)`. -/
def a (c : BranchingChannels R) : R := ∑ ch, c.GP ch

/-- Neutron per-nucleon channel sum `b = Σ_c G_N(c)`. -/
def b (c : BranchingChannels R) : R := ∑ ch, c.GN ch

end BranchingChannels

/-- **Config sum**: over all `4^P` channel assignments of `P` slots, the sum
    of the products of per-slot channel weights. -/
noncomputable def configSum (g : Fin 4 → R) (P : ℕ) : R :=
  ∑ f ∈ Fintype.piFinset (fun _ : Fin P => (Finset.univ : Finset (Fin 4))),
    ∏ i, g (f i)

/-- **Config-sum multiplicativity reduction** — the genuine combinatorial
    content.  By nucleon independence (`Finset.prod_univ_sum`), the `4^P`
    config sum collapses to the per-slot channel sum raised to the `P`. -/
theorem configSum_eq (g : Fin 4 → R) (P : ℕ) :
    configSum g P = (∑ ch, g ch) ^ P := by
  unfold configSum
  rw [← Finset.prod_univ_sum, Finset.prod_const, Finset.card_univ,
    Fintype.card_fin]

/-- **Total `Σ Δm_e`** over all `4^A` configurations: the daughter
    `(Z+1, N−1)` channel product minus the parent `(Z, N)` channel product.
    A concrete `def` (not an abstract field), so the factorisation below is
    non-vacuous. -/
noncomputable def totalDeltaM (c : BranchingChannels R) (Z N : ℕ) : R :=
  configSum c.GP (Z + 1) * configSum c.GN (N - 1)
    - configSum c.GP Z * configSum c.GN N

/-- **Branching Q-value factorisation** ([`prop:branching-qvalue-factorization`]):
    `Σ Δm_e = a^Z · b^{N−1} · (a − b)`.  Derived sorry-free from the config-sum
    multiplicativity reduction and elementary algebra (`0 < N`). -/
-- Ref: [leitner2026] quantum-observable-universe/particle-interactions/branching-qvalue-factorization.md
theorem branching_qvalue_factorization (c : BranchingChannels R) {Z N : ℕ}
    (h_N_pos : 0 < N) :
    totalDeltaM c Z N = c.a ^ Z * c.b ^ (N - 1) * (c.a - c.b) := by
  unfold totalDeltaM
  rw [configSum_eq, configSum_eq, configSum_eq, configSum_eq]
  show c.a ^ (Z + 1) * c.b ^ (N - 1) - c.a ^ Z * c.b ^ N
      = c.a ^ Z * c.b ^ (N - 1) * (c.a - c.b)
  have hb : c.b ^ N = c.b ^ (N - 1) * c.b := by
    rw [← pow_succ, Nat.sub_add_cancel h_N_pos]
  rw [pow_succ, hb]; ring

end QOU.ParticleInteractions
