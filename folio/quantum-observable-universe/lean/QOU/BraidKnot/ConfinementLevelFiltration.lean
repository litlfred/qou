/-!
# Filtration Monotonicity, Functional Shadow-Price Canonicity, and Dressing Chains

Bean `qou-9yt9`. Companion to `QOU.BraidKnot.ConfinementLevel`,
`QOU.BraidKnot.DressedParticle`, and the `KnotOperatorEnergy` structure refactor.

## What this file proves

1. **Filtration refinement anti-monotonicity (`ConfinementLevel`):**
   `QOU.BraidKnot.ConfinementLevel` indexes the confinement level by a
   filtration predicate `valid : Datum → Nat → Prop` and carries both
   `level_valid` and `level_min`. When one filtration predicate refines another
   (`∀ ℓ, valid₁ d ℓ → valid₂ d ℓ`, e.g. enlarging the operator ideal `J^ℓ`),
   the minimum level moves monotonically downward (`L₂.level ≤ L₁.level`);
   when two filtration predicates are pointwise equivalent, their minimum
   levels are identical (`L₁.level = L₂.level`).
2. **Functional-parameter canonicity (`KnotOperatorEnergy`):**
   Carrying the LP-dual shadow price map `dualValue : List Nat → R → R` as a
   functional parameter and `shadowPrice_eq : shadowPrice = dualValue partition q`
   as a proof field makes `shadowPrice` uniquely determined (`E₁.shadowPrice = E₂.shadowPrice`)
   without any axiom, whereas a plain structure with `shadowPrice` as an
   unconstrained field admits an explicit pair of records at the same
   `(partition, q)` with distinct `shadowPrice` values.
3. **Multi-step dressing chain level preservation (`DressedParticle`):**
   By induction along any finite chain of dressing morphisms where each step
   preserves the confinement level, the final composite particle's level equals
   the initial bare nuclear core's level.

-- Ref: [leitner2026] bean qou-9yt9; QOU/BraidKnot/ConfinementLevel.lean;
-- QOU/BraidKnot/DressedParticle.lean
-/

namespace QOU.BraidKnot

universe u

/-- Abstract minimum-level witness for a filtration predicate `valid : α → Nat → Prop`
    at datum `d : α`, mirroring `QOU.BraidKnot.ConfinementLevel` without Mathlib
    ring imports. -/
structure FiltrationMinLevel {α : Type u} (valid : α → Nat → Prop) (d : α) where
  /-- The minimum filtration level `ℓ ∈ ℕ`. -/
  level : Nat
  /-- `level` satisfies the filtration predicate at `d`. -/
  level_valid : valid d level
  /-- Minimality: every valid level at `d` is at least `level`. -/
  level_min : ∀ ℓ, valid d ℓ → level ≤ ℓ

/-- **Uniqueness of the minimum filtration level** at a fixed datum and predicate. -/
theorem FiltrationMinLevel.unique {α : Type u} {valid : α → Nat → Prop} {d : α}
    (L₁ L₂ : FiltrationMinLevel valid d) : L₁.level = L₂.level :=
  Nat.le_antisymm (L₁.level_min L₂.level L₂.level_valid)
    (L₂.level_min L₁.level L₁.level_valid)

/-- **Anti-monotonicity under filtration inclusion:** if `valid₁ d ℓ → valid₂ d ℓ`
    for all `ℓ` (enlarging the admissible operator set `J^ℓ`), then the minimum
    level for `valid₂` is at most the minimum level for `valid₁`. -/
theorem FiltrationMinLevel.le_of_imp {α : Type u}
    {valid₁ valid₂ : α → Nat → Prop} {d : α}
    (himp : ∀ ℓ, valid₁ d ℓ → valid₂ d ℓ)
    (L₁ : FiltrationMinLevel valid₁ d) (L₂ : FiltrationMinLevel valid₂ d) :
    L₂.level ≤ L₁.level :=
  L₂.level_min L₁.level (himp L₁.level L₁.level_valid)

/-- **Invariance under pointwise-equivalent filtrations.** -/
theorem FiltrationMinLevel.eq_of_iff {α : Type u}
    {valid₁ valid₂ : α → Nat → Prop} {d : α}
    (hiff : ∀ ℓ, valid₁ d ℓ ↔ valid₂ d ℓ)
    (L₁ : FiltrationMinLevel valid₁ d) (L₂ : FiltrationMinLevel valid₂ d) :
    L₁.level = L₂.level :=
  Nat.le_antisymm
    (FiltrationMinLevel.le_of_imp (fun ℓ h => (hiff ℓ).mpr h) L₂ L₁)
    (FiltrationMinLevel.le_of_imp (fun ℓ h => (hiff ℓ).mp h) L₁ L₂)

/-- **Upward-closure transport:** if `valid d` is upward-closed (`ℓ ≤ ℓ' → valid d ℓ → valid d ℓ'`),
    then `valid d ℓ` holds if and only if `L.level ≤ ℓ`. -/
theorem FiltrationMinLevel.valid_iff_level_le {α : Type u}
    {valid : α → Nat → Prop} {d : α}
    (hup : ∀ ℓ ℓ', ℓ ≤ ℓ' → valid d ℓ → valid d ℓ')
    (L : FiltrationMinLevel valid d) (ℓ : Nat) :
    valid d ℓ ↔ L.level ≤ ℓ :=
  ⟨L.level_min ℓ, fun hle => hup L.level ℓ hle L.level_valid⟩

/-- Functional-indexed shadow-price datum (`qou-9yt9` `KnotOperatorEnergy` pattern):
    `shadowPrice` is pinned to `dualValue partition q` by `shadowPrice_eq`. -/
structure IndexedShadowPrice {R : Type u}
    (dualValue : List Nat → R → R) (partition : List Nat) (q : R) where
  /-- Shadow price `y_λ(q) ∈ R`. -/
  shadowPrice : R
  /-- Pinned to the LP-dual value map. -/
  shadowPrice_eq : shadowPrice = dualValue partition q
  /-- Optional absolute energy witness. -/
  energy : Option R := none

/-- Canonical constructor from `dualValue`. -/
def IndexedShadowPrice.ofDualValue {R : Type u}
    (dualValue : List Nat → R → R) (partition : List Nat) (q : R) :
    IndexedShadowPrice dualValue partition q :=
  { shadowPrice := dualValue partition q, shadowPrice_eq := rfl }

/-- **Existence of the indexed shadow-price datum (`qou-9yt9`).** -/
theorem IndexedShadowPrice.nonempty {R : Type u}
    (dualValue : List Nat → R → R) (partition : List Nat) (q : R) :
    Nonempty (IndexedShadowPrice dualValue partition q) :=
  ⟨IndexedShadowPrice.ofDualValue dualValue partition q⟩

/-- **Uniqueness of the shadow price (`qou-9yt9`)** — a theorem from functional
    indexing, requiring zero axioms. -/
theorem IndexedShadowPrice.shadowPrice_unique {R : Type u}
    {dualValue : List Nat → R → R} {partition : List Nat} {q : R}
    (E₁ E₂ : IndexedShadowPrice dualValue partition q) :
    E₁.shadowPrice = E₂.shadowPrice := by
  rw [E₁.shadowPrice_eq, E₂.shadowPrice_eq]

/-- Pre-refactor plain structure with `shadowPrice` as an unconstrained field,
    used only to exhibit the counterexample documented in `qou-9yt9`. -/
structure UnconstrainedShadowPrice (R : Type u) where
  partition : List Nat
  q : R
  shadowPrice : R

/-- **Explicit counterexample to the retired `shadowPrice_canonical` axiom (`qou-9yt9`):**
    two `UnconstrainedShadowPrice Int` records with identical `partition` and `q`
    have distinct `shadowPrice` values. -/
theorem unconstrainedShadowPrice_not_canonical :
    ∃ E₁ E₂ : UnconstrainedShadowPrice Int,
      E₁.partition = E₂.partition ∧ E₁.q = E₂.q ∧ E₁.shadowPrice ≠ E₂.shadowPrice :=
  ⟨⟨[], 0, 0⟩, ⟨[], 0, 1⟩, rfl, rfl, by decide⟩

/-- Multi-step dressing level chain (`qou-9yt9` `DressedParticle.dressing_composes`
    generalised to `k` sequential shell dressings): if every adjacent pair in a
    non-empty list of particle levels has equal levels, the head and last levels
    coincide. -/
inductive LevelPreservingChain : Nat → Nat → Type where
  | refl (ℓ : Nat) : LevelPreservingChain ℓ ℓ
  | step {ℓ₀ ℓ₁ ℓ₂ : Nat} (h : ℓ₂ = ℓ₁) (rest : LevelPreservingChain ℓ₀ ℓ₁) :
      LevelPreservingChain ℓ₀ ℓ₂

/-- **Multi-step dressing composition preserves confinement level.** -/
theorem LevelPreservingChain.level_eq {ℓ₀ ℓ_final : Nat}
    (chain : LevelPreservingChain ℓ₀ ℓ_final) : ℓ_final = ℓ₀ := by
  induction chain with
  | refl => rfl
  | step h _ ih => rw [h, ih]

end QOU.BraidKnot
