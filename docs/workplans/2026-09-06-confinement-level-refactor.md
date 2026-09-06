# ConfinementLevel refactor — explored and VERIFIED (bean `qou-i6u4`)

Date: 2026-09-06. The whole refactor compiles, `lean`-direct exit 0, and
`#print axioms` reports **no axioms at all** on all three results — not even
`propext` or `Classical.choice`.

## What it replaces

| current | after |
|---|---|
| `ConfinementLevel.level_canonical` — **false axiom** | deleted |
| `ConfinementLevel.unique` — derived from it | **theorem**, one line |
| `ConfinementLevel.nonempty` — junk record `⟨0,1,0,0⟩` | `ofNonempty` — real construction via `Nat.find` |
| (nothing) | `level_eq_find` — the level literally IS the minimum |

## The verified code

```lean
structure BraidDatum (R : Type u) [CommRing R] where
  braidIndex : ℕ
  nStrands : ℕ
  q : R

/-- **Confinement level at a datum.**  `valid` is the filtration predicate
    `fun d ℓ => T_w(d) ∈ J^ℓ(d.q)`, carried as a PARAMETER — a function of the
    datum — rather than as a free field. That is the whole repair: the old
    plain structure let `level` vary independently of the braid. -/
structure ConfinementLevel {R : Type u} [CommRing R]
    (valid : BraidDatum R → ℕ → Prop) (d : BraidDatum R) where
  level : ℕ
  level_valid : valid d level
  level_min : ∀ ℓ, valid d ℓ → level ≤ ℓ

/-- **Uniqueness — now a THEOREM.** Two confinement levels for the same braid
    datum agree. This is the `.md`'s "therefore the minimum exists and is
    unique", and it needs only antisymmetry. -/
theorem ConfinementLevel.unique {R : Type u} [CommRing R]
    {valid : BraidDatum R → ℕ → Prop} {d : BraidDatum R}
    (L₁ L₂ : ConfinementLevel valid d) : L₁.level = L₂.level :=
  Nat.le_antisymm (L₁.level_min _ L₂.level_valid) (L₂.level_min _ L₁.level_valid)

/-- **Existence — also a theorem**, from well-ordering, given the `.md`'s
    point 3 (the valid set is nonempty because `J^m = H_n`). -/
noncomputable def ConfinementLevel.ofNonempty {R : Type u} [CommRing R]
    {valid : BraidDatum R → ℕ → Prop} {d : BraidDatum R}
    [DecidablePred (valid d)] (h : ∃ ℓ, valid d ℓ) : ConfinementLevel valid d :=
  ⟨Nat.find h, Nat.find_spec h, fun _ hl => Nat.find_min' h hl⟩

/-- The level is literally the minimum. -/
theorem ConfinementLevel.level_eq_find {R : Type u} [CommRing R]
    {valid : BraidDatum R → ℕ → Prop} {d : BraidDatum R}
    [DecidablePred (valid d)] (h : ∃ ℓ, valid d ℓ)
    (L : ConfinementLevel valid d) : L.level = Nat.find h :=
  ConfinementLevel.unique L (ConfinementLevel.ofNonempty h)

```
