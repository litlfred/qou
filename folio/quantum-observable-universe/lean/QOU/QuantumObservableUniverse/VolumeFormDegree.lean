import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

/-!
# QOU.QuantumObservableUniverse.VolumeFormDegree — self-duality is a degree-2
accident, not a property of volume-form objects

Bean `qou-j3w6` (the condition-5 decision), epic `qou-8lxd`.

## Why this file exists

[`def:fundamental-object`](../../../quantum-universes/fundamental-object.md)
does **not** postulate a two-dimensional object.  It postulates an object `V`
carrying a *volume form* — "the categorical determinant" — together with an
adjoint coform satisfying the snake identities, and then observes that "under a
fibre functor the volume constraint forces `rank(V) = 2`".  Rank two is the
**conclusion**; the volume form is the input.

The degree, however, is written into the definition by hand: the volume form is
declared on `Λ²V`, and *that* is what makes the rank two.  This file separates
the two, by working with the volume form at an unspecified degree `N` and
asking what each degree forces.  The answer is a dichotomy that the corpus has
been reading as two unrelated facts:

| degree `N` of the volume form `Λ^N W ≅ 𝟙` | forced rank | complementary power `Λ^{N-1}W ≅ W^∨` | duality |
|---|---|---|---|
| `2` | `2` | `Λ¹W = W` | `W^∨ ≅ W` — **self-dual, forced** |
| `3` | `3` | `Λ²W ≠ W` | `W^∨ ≅ Λ²W` — self-duality **not** forced |

So the self-duality of the fundamental object — the datum the corpus reads as
"symplectic self-dual, which is what distinguishes `SL₂/SU(2)` from `GL₂`" — is
not an extra axiom and not a general feature of volume-form objects.  **It is
what a volume form of degree exactly two says**, because two is the only degree
at which the complementary exterior power `Λ^{N-1}` is the object itself.

That matters for the eightfold way.  `QOU.Eightfold.Sym2GateFSTrichotomy`
(`gate_forces_complex_of_dim_three`, sorry-free) proves that a three-dimensional
object passing the `Sym²` gate must be **complex type** — not self-dual.  The
table above says a degree-3 volume form is exactly the structure that does not
force self-duality, and whose duality relation `W^∨ ≅ Λ²W` is the `SU(3)`
relation `𝟑̄ ≅ Λ²𝟑`.  The missing flavour object and the fundamental object are
therefore *the same construction at different degrees*, not one derived datum
and one imported one.

## What is proved here, and what is not

**Proved (unconditional, no framework hypothesis):** the whole dimension
bookkeeping of the table — that a non-trivial volume form of degree `N` forces
rank `N`, that the complementary power has the same dimension as the object,
that the complementary degree equals `1` exactly at `N = 2`, and that the
alternating cube is one-dimensional exactly at rank `3`.

**Not proved, and deliberately not asserted anywhere below:**

* that a degree-3 volume-form object *exists* in a quantum observable universe.
  Nothing here constructs one.  This file says what such an object would have to
  look like and why degree 2 cannot be bent into it; it is a *specification*,
  in the sense of bean `qou-dwsh`, not a construction.
* that `W^∨ ≅ Λ^{N-1}W` at the level of **objects**.  What is proved here is the
  dimension shadow of that isomorphism.  The object-level statement is the
  standard consequence of a non-degenerate pairing
  `Λ^{N-1}W ⊗ W → Λ^N W ≅ 𝟙` in a rigid monoidal category, cited and not
  formalised — Mathlib has no exterior-power-of-an-object API to state it
  against.  Every declaration below is about `Nat.choose`, and none of them
  silently upgrades to an object-level claim.
* anything about **which** degree the axioms supply.  Condition 5 of
  `def:quantum-observable-universe` names `Λ²`.  Whether axioms 1–4 supply a
  second volume form of another degree — the natural candidate being the
  measurability axiom's `c₁(Ad(A)) = 0`, which in the usual reading *is* the
  statement that the top exterior power of `Ad(A)` is trivial, i.e. a volume
  form of degree `rank Ad(A)` — is open, and is the question bean `qou-j3w6`
  puts to the author.  That reading of `c₁` is an interpretation of a
  categorical Chern class the corpus has no Lean carrier for; it is recorded
  here as a lead, and is asserted nowhere below.

Base ring: none — this is integer combinatorics (§7c: no `ℝ`, no ring at all).

Companion results already in the corpus, which this generalises rather than
duplicates: `QOU.BraidsAndKnots.VolumeConstraintForcesFibreTwo`
(`exteriorSquareDim_eq_one_iff`, the `N = 2` row) and
`QOU.Eightfold.RowCapObstruction` (`weyl_dim_alt_eq_zero_iff`, the vanishing of
the alternating cube below rank 3).
-/

namespace QOU.QuantumObservableUniverse.VolumeFormDegree

/-- The dimension of `Λ^k W` for an object `W` of rank `n`. -/
def extPowerDim (n k : ℕ) : ℕ := n.choose k

/-- A binomial coefficient is `1` exactly at the two ends of its row.

This is the arithmetic core of the whole file: it is what makes "the volume form
is an isomorphism onto the unit" a statement about the *rank*, since `𝟙` is
one-dimensional.  Mathlib has `choose_eq_zero_iff` but no `= 1` companion, so it
is proved here. -/
theorem choose_eq_one_iff (n k : ℕ) : n.choose k = 1 ↔ k = 0 ∨ k = n := by
  constructor
  · intro h
    rcases Nat.eq_zero_or_pos k with rfl | hk
    · exact Or.inl rfl
    · right
      obtain ⟨j, rfl⟩ : ∃ j, k = j + 1 := ⟨k - 1, by omega⟩
      cases n with
      | zero => simp at h
      | succ m =>
        -- Above the row the coefficient vanishes, so the degree is in range.
        have hle : j + 1 ≤ m + 1 := by
          by_contra hc
          rw [Nat.choose_eq_zero_iff.mpr (by omega)] at h
          exact absurd h (by norm_num)
        -- Absorption: `(m+1) · C(m, j) = C(m+1, j+1) · (j+1)`, and the right
        -- factor `C(m+1, j+1)` is the `1` we are assuming.
        have habs := Nat.succ_mul_choose_eq m j
        simp only [Nat.succ_eq_add_one] at habs
        rw [h, one_mul] at habs
        have hpos : 0 < m.choose j := Nat.choose_pos (by omega)
        have hge : m + 1 ≤ j + 1 := by
          calc m + 1 = (m + 1) * 1 := (Nat.mul_one _).symm
            _ ≤ (m + 1) * m.choose j := Nat.mul_le_mul_left _ hpos
            _ = j + 1 := habs
        omega
  · rintro (rfl | rfl)
    · exact Nat.choose_zero_right _
    · exact Nat.choose_self _

/-- **A volume form forces the rank to be its degree.**  If `Λ^N W ≅ 𝟙` with
`N ≥ 1`, then `rank W = N`.  The hypothesis `1 ≤ N` is what excludes the
degenerate `Λ⁰W ≅ 𝟙`, which holds for every object and says nothing. -/
theorem rank_eq_of_volumeForm {n N : ℕ} (hN : 1 ≤ N) (h : extPowerDim n N = 1) :
    n = N := by
  rcases (choose_eq_one_iff n N).mp h with h0 | hn
  · omega
  · omega

/-- The `N = 2` row: the corpus's own volume constraint, recovered.  Matches
`QOU.BraidsAndKnots.VolumeConstraintForcesFibreTwo.exteriorSquareDim_eq_one_iff`. -/
theorem degree_two_forces_rank_two {n : ℕ} (h : extPowerDim n 2 = 1) : n = 2 :=
  rank_eq_of_volumeForm (by norm_num) h

/-- The `N = 3` row: a degree-3 volume form forces rank `3`. -/
theorem degree_three_forces_rank_three {n : ℕ} (h : extPowerDim n 3 = 1) : n = 3 :=
  rank_eq_of_volumeForm (by norm_num) h

/-- **The complementary power has the same dimension as the object.**  For a
rank-`N` object, `dim Λ^{N-1}W = N = dim W`.  This is the dimension shadow of
`W^∨ ≅ Λ^{N-1}W`, the isomorphism the volume form induces; the object-level
statement is cited, not formalised (see the module docstring). -/
theorem complementary_dim {N : ℕ} (hN : 1 ≤ N) : extPowerDim N (N - 1) = N := by
  simp only [extPowerDim]
  rw [Nat.choose_symm hN]
  simp

/-- **The dichotomy.**  The complementary degree `N - 1` equals `1` — i.e. the
dual of `W` is `W` itself, so the volume form makes `W` self-dual — exactly when
the degree is `2`. -/
theorem complementaryDegree_eq_one_iff_degree_two {N : ℕ} (hN : 1 ≤ N) :
    N - 1 = 1 ↔ N = 2 := by omega

/-- **The consequence for the eightfold way.**  At degree `3` the complementary
power is `Λ²`, not `Λ¹`, so the volume form relates `W` to its *exterior square*
rather than to itself.  Self-duality is therefore not forced, which is precisely
what `Sym2GateFSTrichotomy.gate_forces_complex_of_dim_three` requires of any
three-dimensional object passing the `Sym²` gate. -/
theorem degree_three_complementary_is_two : (3 : ℕ) - 1 = 2 := by norm_num

/-- Restated as a non-self-duality statement: for every degree `N ≥ 3` the
complementary power is not `Λ¹`. -/
theorem complementaryDegree_ne_one_of_three_le {N : ℕ} (h : 3 ≤ N) : N - 1 ≠ 1 := by
  omega

/-- **The eightfold singlet exists exactly at rank 3.**  The totally
antisymmetric channel of `W^{⊗3}` — the `𝟏` of `𝟑 ⊗ 𝟑 ⊗ 𝟑 = 𝟏𝟎 ⊕ 𝟖 ⊕ 𝟖 ⊕ 𝟏` — is
one-dimensional iff the rank is `3`. -/
theorem altCube_dim_eq_one_iff {n : ℕ} : extPowerDim n 3 = 1 ↔ n = 3 := by
  constructor
  · intro h
    exact rank_eq_of_volumeForm (by norm_num) h
  · rintro rfl
    decide

/-- And it is absent at rank `2`: `Λ³` of the corpus's fundamental object
vanishes.  This is why no amount of re-fibring `V` produces the eightfold
singlet — see `QOU.Eightfold.FibreFunctorDimensionNotCategorical`. -/
theorem altCube_vanishes_at_rank_two : extPowerDim 2 3 = 0 := by decide

/-- The two degrees are mutually exclusive on one object: an object cannot carry
a volume form of degree `2` **and** one of degree `3`, since each forces its own
rank.  So a second fundamental object is genuinely a *second object*, not a
re-reading of the first. -/
theorem degrees_two_and_three_exclusive {n : ℕ}
    (h2 : extPowerDim n 2 = 1) (h3 : extPowerDim n 3 = 1) : False := by
  have e2 := degree_two_forces_rank_two h2
  have e3 := degree_three_forces_rank_three h3
  omega

end QOU.QuantumObservableUniverse.VolumeFormDegree
