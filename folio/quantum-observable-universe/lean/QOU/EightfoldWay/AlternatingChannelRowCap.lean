import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.Data.Fintype.Card
import Mathlib.Tactic

/-!
# QOU.EightfoldWay.AlternatingChannelRowCap — the row cap on the actual tensor cube

`MathlibExt/RowCapObstruction.lean` proves `C(N, 3) = 0 ↔ N < 3`, with the dimension of the
alternating channel *taken to be* `C(N, 3)` (hook-content formula, cited).  The eightfold-way
ledger accordingly lists the row cap `ℓ(λ) ≤ N` as cited, not proved.

This module proves the statement the chapter actually uses, on the actual module: model
`V^{⊗3}` for `V = ℚ^N` by its coordinates, functions on index triples `(Fin 3 → Fin N) → ℚ`,
with `S₃` permuting the three tensor slots.  The **alternating channel** (the `λ = (1³)`
isotypic part, the singlet channel of the eightfold way) is the subspace of `f` with
`f (t ∘ σ) = sign σ · f t`.  Then

* `altChannel_eq_bot_iff` — **the alternating channel is zero iff `N < 3`.**

The `N < 3` direction is pigeonhole: a triple in a set of fewer than three values repeats a
value, and the transposition of the repeated slots fixes the triple while flipping the sign.
The `N ≥ 3` direction exhibits the determinant witness.  No hook-content formula and no
Schur–Weyl duality are used.  This is the classical (`q = 1`) statement; the `q`-deformed one
is the cited flatness of Drinfeld–Jimbo quantisation, as recorded in the ledger.

Base ring `ℚ`; nothing archimedean, no empirical input.
-/

namespace QOU.EightfoldWay.AlternatingChannelRowCap

open Equiv

/-- Coordinates of `V^{⊗3}` for `V = ℚ^N`: functions on index triples. -/
abbrev Cube (N : ℕ) := (Fin 3 → Fin N) → ℚ

/-- The **alternating channel** (`λ = (1³)`) of `V^{⊗3}`. -/
def altChannel (N : ℕ) : Submodule ℚ (Cube N) where
  carrier := {f | ∀ (σ : Perm (Fin 3)) (t : Fin 3 → Fin N),
    f (t ∘ σ) = ((Perm.sign σ : ℤ) : ℚ) * f t}
  add_mem' := by
    intro f g hf hg σ t
    simp only [Pi.add_apply, hf σ t, hg σ t]; ring
  zero_mem' := by intro σ t; simp
  smul_mem' := by
    intro c f hf σ t
    simp only [Pi.smul_apply, smul_eq_mul, hf σ t]; ring

/-- Below three values, every alternating tensor vanishes (pigeonhole). -/
theorem altChannel_eq_bot_of_lt {N : ℕ} (hN : N < 3) : altChannel N = ⊥ := by
  rw [eq_bot_iff]
  intro f hf
  rw [Submodule.mem_bot]
  funext t
  obtain ⟨i, j, hij, htij⟩ : ∃ i j, i ≠ j ∧ t i = t j :=
    Fintype.exists_ne_map_eq_of_card_lt t (by simpa using hN)
  have hfix : t ∘ (swap i j : Perm (Fin 3)) = t := by
    funext k
    simp only [Function.comp_apply]
    by_cases hki : k = i
    · subst hki; simp [swap_apply_left, htij]
    · by_cases hkj : k = j
      · subst hkj; simp [swap_apply_right, htij]
      · simp [swap_apply_of_ne_of_ne hki hkj]
  have h := hf (swap i j) t
  rw [hfix, Perm.sign_swap hij] at h
  simp only [Pi.zero_apply]
  push_cast at h
  linarith

/-- The determinant witness: `t ↦ det` of the `3 × 3` matrix whose row `i` is the
indicator of `t i` among the first three coordinates. -/
def detWitness (N : ℕ) : Cube N := fun t =>
  (Matrix.of fun i j : Fin 3 => if (t i : ℕ) = (j : ℕ) then (1 : ℚ) else 0).det

theorem detWitness_mem (N : ℕ) : detWitness N ∈ altChannel N := by
  intro σ t
  have := Matrix.det_permute σ
    (Matrix.of fun i j : Fin 3 => if (t i : ℕ) = (j : ℕ) then (1 : ℚ) else 0)
  simpa [detWitness, Matrix.submatrix] using this

theorem detWitness_ne_zero {N : ℕ} (hN : 3 ≤ N) : detWitness N ≠ 0 := by
  intro h
  have h0 := congrFun h (fun i => ⟨i.1, by omega⟩)
  have : (Matrix.of fun i j : Fin 3 =>
      if ((⟨i.1, by omega⟩ : Fin N) : ℕ) = (j : ℕ) then (1 : ℚ) else 0) = 1 := by
    ext i j
    simp [Matrix.one_apply, Fin.ext_iff]
  simp [detWitness, this] at h0

/-- **Row cap for the singlet channel, on the actual tensor cube.** The alternating channel
of `(ℚ^N)^{⊗3}` is zero if and only if `N < 3`. -/
theorem altChannel_eq_bot_iff (N : ℕ) : altChannel N = ⊥ ↔ N < 3 := by
  constructor
  · intro h
    by_contra hN
    push_neg at hN
    have hmem := detWitness_mem N
    rw [h, Submodule.mem_bot] at hmem
    exact detWitness_ne_zero hN hmem
  · exact altChannel_eq_bot_of_lt

/-- The fibre supplied by condition (iii) has `N = 2`, so its singlet channel is zero. -/
theorem altChannel_two_eq_bot : altChannel 2 = ⊥ :=
  altChannel_eq_bot_of_lt (by norm_num)

/-- The flavour fibre `N = 3` has a nonzero singlet channel. -/
theorem altChannel_three_ne_bot : altChannel 3 ≠ ⊥ := by
  rw [Ne, altChannel_eq_bot_iff]; norm_num

end QOU.EightfoldWay.AlternatingChannelRowCap
