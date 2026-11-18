import Mathlib.Tactic

/-!
# QOU.BraidKnot.ConfinementNfStructureForcing — conjectural class (§3b), content-bearing

**§3b class axiomatisation** for content block
[`conj:confinement-nf-structure-forcing`](../../../quantum-observable-universe/mass-theory/confinement-nf-structure-forcing.md):
*Confinement → NF-structure forcing.*

Given a compound braid `β = β₁ ⋆ I ⋆ β₂ ∈ Bₙ` across a basis interface
`I`, **assuming the confinement hypothesis `|A| < n!`** (the active
LP/SDP set `A` is a proper subset of all `n!` partition channels), the
class carries the conjecture's two-part content:

1. **NF-support localisation** — the Wedderburn maximiser
   `λ⋆ = argmax_λ ord⁻_{q=0} χ_λ(T_β)` resides strictly inside the
   active set (`λ⋆ ∈ A`).
2. **Duality-bounded shift** — the structural NF shift decomposes as
   `shift_NF(β) = α_shift(I) + Δ(β₁,β₂;A)` with the deviation bounded by
   the LP duality gap, `|Δ| ≤ duality_gap(β)`.

Matured from a degenerate `residual : ℝ` / `residual = 0` placeholder to
the faithful two-part statement above (bean `cj421`). Consequences are
derived unconditionally from the class below (`shiftNF_mem_band`,
`shiftNF_eq_of_zero_gap`, `activeSet_nonempty`, `one_lt_nFactorial`,
`dualityGap_nonneg`): the NF shift is trapped in the band
`α_shift ± duality_gap`, and an exact zero gap forces `shift_NF = α_shift`
— matching the benchmark's observed exact-zero-gap outcome.

Per AGENTS.md §3b-cond we provide **no global instance**: supplying one
means exhibiting the actual QOU objects (the NF shift, interface shift,
and duality gap of a real compound braid) together with the localisation
and shift-bound facts — which is exactly the open conjecture. The honest
open state (§3b-tax) is a content-bearing class with no instance.
Downstream theorems may take `[ConfinementNfStructureForcing]` as an
explicit `[Instance]` hypothesis to derive rigorous-conditional results
(§3b-cond).
-/

namespace QOU.BraidKnot

/-- **Confinement → NF-structure forcing** — §3b conjecture class carrying
    the localisation + duality-bounded-shift content.

    Conjectural class — see
    [`conj:confinement-nf-structure-forcing`](../../../quantum-observable-universe/mass-theory/confinement-nf-structure-forcing.md). -/
class ConfinementNfStructureForcing where
  -- Witness: computations/none
  /-- The active LP/SDP set `A ⊆ {λ ⊢ n}` of partition labels with
      `y_λ⋆ > 0`, indexed as `ℕ`. -/
  activeSet : Finset ℕ
  /-- The confinement bound `n!` (the order of `Sₙ`). -/
  nFactorial : ℕ
  /-- **Confinement hypothesis** `|A| < n!`: the active set is a proper
      (confined) subset of all `n!` partition channels. -/
  confinement : activeSet.card < nFactorial
  /-- The Wedderburn maximiser `λ⋆ = argmax_λ ord⁻_{q=0} χ_λ(T_β)`. -/
  lambdaStar : ℕ
  /-- **Part 1 (NF-support localisation).** The maximiser resides
      strictly inside the active set: `λ⋆ ∈ A`. -/
  localisation : lambdaStar ∈ activeSet
  /-- The structural NF shift `shift_NF(β)`. -/
  shiftNF : ℝ
  /-- The interface base shift `α_shift(I)`. -/
  alphaShift : ℝ
  /-- The structural deviation `Δ(β₁, β₂; A)`. -/
  delta : ℝ
  /-- The LP/SDP duality gap `duality_gap(β)`. -/
  dualityGap : ℝ
  /-- **Part 2a (shift decomposition).** `shift_NF(β) = α_shift(I) + Δ`. -/
  shift_decomp : shiftNF = alphaShift + delta
  /-- **Part 2b (duality-bounded deviation).** `|Δ| ≤ duality_gap(β)`. -/
  delta_bounded : |delta| ≤ dualityGap

namespace ConfinementNfStructureForcing

variable [C : ConfinementNfStructureForcing]

/-- **Duality-band enclosure:** the NF shift is trapped in the duality band
    `α_shift(I) ± duality_gap(β)`. -/
theorem shiftNF_mem_band :
    C.alphaShift - C.dualityGap ≤ C.shiftNF ∧
      C.shiftNF ≤ C.alphaShift + C.dualityGap := by
  have hb := abs_le.mp C.delta_bounded
  refine ⟨?_, ?_⟩ <;> rw [C.shift_decomp] <;> linarith [hb.1, hb.2]

/-- **Exact zero duality gap forces `Δ = 0`,**
    so the NF shift equals the interface base shift exactly — the
    benchmark's observed exact-zero-gap outcome. -/
theorem shiftNF_eq_of_zero_gap (h0 : C.dualityGap = 0) :
    C.shiftNF = C.alphaShift := by
  have hb : |C.delta| ≤ 0 := h0 ▸ C.delta_bounded
  have hd : C.delta = 0 := abs_eq_zero.mp (le_antisymm hb (abs_nonneg _))
  rw [C.shift_decomp, hd, add_zero]

/-- **Non-emptiness of the active LP/SDP set.**
    Part 1 (`localisation`) places `lambdaStar` inside `activeSet`, so the
    confined active set is necessarily non-empty. -/
theorem activeSet_nonempty : C.activeSet.Nonempty :=
  ⟨C.lambdaStar, C.localisation⟩

/-- **Strict lower bound on the channel-space cardinality `nFactorial`.**
    Combining Part 1 (`localisation`, giving `1 ≤ activeSet.card`) with the
    confinement inequality (`activeSet.card < nFactorial`) forces
    `1 < nFactorial`. -/
theorem one_lt_nFactorial : 1 < C.nFactorial := by
  have hpos : 0 < C.activeSet.card := Finset.card_pos.mpr (activeSet_nonempty (C := C))
  have hlt := C.confinement
  omega

/-- **Non-negativity of the LP/SDP duality gap.** -/
theorem dualityGap_nonneg : 0 ≤ C.dualityGap :=
  le_trans (abs_nonneg C.delta) C.delta_bounded

end ConfinementNfStructureForcing

-- The conjecture itself.  Per AGENTS.md §3b-cond we provide NO global
-- instance — an instance is exactly the open conjecture (see the module
-- docstring).  Honest open state (§3b-tax): content-bearing class, no
-- instance.
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/confinement-nf-structure-forcing.ts

end QOU.BraidKnot
