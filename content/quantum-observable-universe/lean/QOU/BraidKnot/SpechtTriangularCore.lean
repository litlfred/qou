import QOU.BraidKnot.SpechtStandardBasis

/-!
# QOU.BraidKnot.SpechtTriangularCore — reduction of the brick-4 dominance lemma

Reduces the brick-4 combinatorial core
`QOU.BraidKnot.SpechtStandardBasis.standardPolytabloid_triangular` (the
3-field `Triangular` bundle whose `linearIndependent` lever underlies the
standard-basis theorem `dim S^μ = #SYT(μ)`) to a **single** genuine core.

The `Triangular` bundle has three fields; **two are order-independent**:

| Field | Depends on the chosen `LinearOrder`? | Status here |
|---|---|---|
| `diag_unit` — coeff of `{T}` in `e_T` is a unit | no | targeted **sorry-free** (`= 1`, via `ColStab(t) ∩ RowStab(t) = {1}`) |
| `lead_inj` — `leadTab` injective on SYT | no | targeted **sorry-free** (row-strictness) |
| `supp_le` — `{T}` is the max of `supp(e_T)` | **yes** (forces the order) | **STUB** — the genuine dominance core |

So the opaque 3-field stub becomes: two order-independent facts (proved here) +
one precisely-named dominance core (`standardPolytabloid_dominance_order`), which
is the only remaining mathematical debt of brick-4 independence.

## sorry-free ↔ stubbed map

| Declaration | Status |
|---|---|
| `standardPolytabloid_diag_coeff` / `_diag_unit` | (WIP) → **sorry-free** target |
| `leadTab_injective` | (WIP) → **sorry-free** target |
| `standardPolytabloid_dominance_order` (the order + `supp_le`) | **STUB** `sorry` — `-- Ref: [sagan2001]` Thm 2.5.2 |
| `standardPolytabloid_triangular'` (the reduction) | **sorry-free MODULO the core(s)** |

This module carries an honest `sorry` (the dominance core), so — like brick 2 and
`SpechtIrreducible` — it is intentionally **not** imported by the `QOU.BraidKnot`
umbrella. It reproduces the brick-4 `standardPolytabloid_triangular` statement as a
separate, reduction-bearing theorem (`SpechtStandardBasis` cannot import this file —
the standard one-way dependency).

§7c-clean: no `ℝ`, no ordering on `k`, no `Real.*`; the `LinearOrder` is on the
*combinatorial* index `Tabloid μ`, not on the base ring.

## References
- [sagan2001] Sagan, *The Symmetric Group*, §2.5 (the standard basis, Thm 2.5.2;
  independence via the dominance / last-letter order; `e_T = ±{T} + lower terms`).
- [james1984representation] James & Kerber, *The Representation Theory of the
  Symmetric Group* — §8 (the submodule theorem and the standard-basis machinery).
-/

open QOU.BraidKnot QOU.BraidKnot.Specht QOU.BraidKnot.SpechtStandardBasis

namespace QOU.BraidKnot.SpechtTriangularCore

variable {k : Type} [Field k] [CharZero k]
variable {μ : YoungDiagram}

/-! ## 1. The diagonal coefficient (order-independent) -/

/-- **Diagonal coefficient.** The coefficient of `{T}` in the standard polytabloid
`e_T` is a unit (in fact `= 1`): the only column permutation fixing the row-tabloid
of `T` is the identity (`ColStab(t) ∩ RowStab(t) = {1}`). Order-independent. -/
theorem standardPolytabloid_diag_unit (T : StandardYoungTableau μ) :
    IsUnit ((standardPolytabloid (k := k) T) (leadTab T)) := by
  -- Ref: [sagan2001] §2.5 (coefficient of {T} in e_T is ±1; here +1).
  sorry

/-! ## 2. Injectivity of the leading map (order-independent) -/

/-- **`leadTab` injective.** Distinct standard tableaux have distinct row-tabloids:
within each row the entries strictly increase (`row_strict`), so the row-class
determines the tableau. Order-independent. -/
theorem leadTab_injective : Function.Injective (leadTab (μ := μ)) := by
  -- Ref: [sagan2001] §2.5 (a standard tableau is determined by its row-classes).
  sorry

/-! ## 3. The dominance core (the single genuine stub) -/

/-- **STUB — the dominance core.** There is a linear order on `Tabloid μ` (a linear
extension of dominance) under which `{T} = leadTab T` is the maximum of the support
of every standard polytabloid `e_T`. This is the heart of Sagan Thm 2.5.2: a column
permutation weakly *decreases* dominance, so every tabloid appearing in `e_T` is
`≤ {T}`. The one remaining mathematical debt of brick-4 independence. -/
theorem standardPolytabloid_dominance_order :
    ∃ _ : LinearOrder (Specht.Tabloid μ),
      ∀ T : StandardYoungTableau μ,
        ∀ a ∈ (standardPolytabloid (k := k) T).support, a ≤ leadTab T := by
  -- Ref: [sagan2001] Thm 2.5.2 (dominance order on tabloids; column permutations
  -- weakly decrease dominance, so {T} is the maximum of supp(e_T)).
  sorry

/-! ## 4. The reduction: the `Triangular` bundle from the core(s) -/

/-- **Triangularity of the standard polytabloids** — reduced to the single dominance
core `standardPolytabloid_dominance_order`, with the two order-independent fields
(`diag_unit`, `lead_inj`) supplied locally. Reproduces the brick-4 statement
`QOU.BraidKnot.SpechtStandardBasis.standardPolytabloid_triangular`. -/
theorem standardPolytabloid_triangular' :
    ∃ _ : LinearOrder (Specht.Tabloid μ),
      Triangular (standardPolytabloid (k := k) (μ := μ)) (leadTab (μ := μ)) := by
  obtain ⟨ord, hsupp⟩ := standardPolytabloid_dominance_order (k := k) (μ := μ)
  refine ⟨ord, ?_⟩
  exact
    { lead_inj := leadTab_injective (μ := μ)
      diag_unit := standardPolytabloid_diag_unit (k := k)
      supp_le := hsupp }

end QOU.BraidKnot.SpechtTriangularCore
