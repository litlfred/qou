import QOU.Mathlib.SchenstedRSKPairInjective

/-!
# QOU.Mathlib.SchenstedRSKEquiv — the Robinson–Schensted correspondence as an `Equiv`

Brick 40 of epic `qou-nrex` (RSK inverse).

Bricks 38 and 39 give surjectivity and injectivity of `rskPair`. This packages them:

```lean
rskEquiv n : Equiv.Perm (Fin n) ≃ {X : Σ μ, SYT μ × SYT μ // X.1.cells.card = n}
```

The subtype is forced. `rskPair` lands in the `Σ` over *all* Young diagrams, but its image is exactly
the diagrams with `n` cells — `rskPair_card`, which reads off `recordingCells_card` through
`recordingShape_eq_pShape`. Cutting the codomain down to that subtype is what makes the map a
bijection rather than merely injective.

Surjectivity needs one small restatement: brick 38 produces a permutation of `Fin |μ|`, and the
subtype's index is `n`. `exists_rskPair_eq_of_card` substitutes the cardinality hypothesis, which is
legitimate here precisely because `n` is a variable — the same move that was unavailable in brick 35,
where the diagram equality had no variable side and `ofRowLens_congr` had to be proved instead.

## Scope

The correspondence, as a bijection. **Not** `RSKBurnsideHolds`. That identity is indexed by
`Nat.Partition n`, so getting to it from here needs a further count:
`Nat.card {X // X.1.cells.card = n} = ∑ p : Nat.Partition n, (dimSYT p)^2`, which in turn needs
`partitionShape` to be a bijection onto the Young diagrams with `n` cells. None of that is done here,
and `RSKBurnsideHolds` for general `n` remains proved only for `n ≤ 12`, by `rskBurnsideHolds_le12` —
a route with no RSK correspondence in it.

Pure combinatorics on `ℕ`; nothing archimedean; no fit.

**Scope note superseded (2026-08-23).** The scope paragraph above records the state of the arc when
this brick landed. `RSKBurnsideHolds` is now proved for **every** `n`
(`QOU.Mathlib.rskBurnsideHolds`, brick 42), and `SnIsotypicSpechtSplit` is inhabited, so any
statement here that they "remain open" or hold "only for `n ≤ 12`" describes history rather than the
corpus. The per-brick scope is otherwise unchanged and still accurate.

-/

namespace QOU.Mathlib.Schensted

open YoungDiagram

/-- **The image lands on diagrams of `n` cells.** -/
theorem rskPair_card {n : ℕ} (σ : Equiv.Perm (Fin n)) : (rskPair σ).1.cells.card = n := by
  show (pShape (wordOfPerm σ)).cells.card = n
  rw [← recordingShape_eq_pShape, recordingCells_card]
  simp [wordOfPerm]

/-- Brick 38 with the cardinality carried as a hypothesis, so the permutation is indexed by `n`. -/
theorem exists_rskPair_eq_of_card {μ : YoungDiagram}
    (SP SQ : QOU.Mathlib.StandardYoungTableau μ) {n : ℕ} (hn : μ.cells.card = n) :
    ∃ σ : Equiv.Perm (Fin n), rskPair σ = ⟨μ, SP, SQ⟩ := by
  subst hn
  exact exists_rskPair_eq SP SQ

/-- **The Robinson–Schensted correspondence.** Permutations of `Fin n` correspond to pairs of
standard Young tableaux of a common shape with `n` cells. -/
noncomputable def rskEquiv (n : ℕ) :
    Equiv.Perm (Fin n) ≃
      {X : (Σ μ : YoungDiagram, QOU.Mathlib.StandardYoungTableau μ ×
        QOU.Mathlib.StandardYoungTableau μ) // X.1.cells.card = n} :=
  Equiv.ofBijective (fun σ => ⟨rskPair σ, rskPair_card σ⟩)
    ⟨fun _ _ h => rskPair_injective (Subtype.ext_iff.mp h), by
      rintro ⟨⟨μ, SP, SQ⟩, hX⟩
      obtain ⟨σ, hσ⟩ := exists_rskPair_eq_of_card SP SQ hX
      exact ⟨σ, Subtype.ext hσ⟩⟩

@[simp] theorem rskEquiv_apply {n : ℕ} (σ : Equiv.Perm (Fin n)) :
    ((rskEquiv n) σ : Σ μ : YoungDiagram, QOU.Mathlib.StandardYoungTableau μ ×
      QOU.Mathlib.StandardYoungTableau μ) = rskPair σ := rfl

end QOU.Mathlib.Schensted
