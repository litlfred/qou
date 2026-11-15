/-
# Word actions on a generator — `b_j · σ` as an explicit two-term combination

`wordAction h j` is the right action of the `j`-th normal-form basis word,
`u ↦ u · b_j`. This file evaluates all 24 of them on each of the three
generator basis vectors `e₄ 1 = σ₀`, `e₄ 2 = σ₁`, `e₄ 6 = σ₂`.

Every word is one generator applied to a shorter word — `wordAction 5` is
`mulσ₀ ∘ wordAction 4`, and so on down to `wordAction 0 = id`. So each lemma
below rewrites with its **parent's** lemma, pushes one generator through with
`mulσᵢ_add` / `mulσᵢ_smul`, and lands on the atomic facts of
`H4GeneratorAction`. The cost is one generator step per lemma; nothing here
ever expands a six-deep composite, which is the measured 2-minutes-and-fails
route these files exist to avoid.

## The peel is a lemma, not a `show`

`wordAction h j` is a `Matrix.cons` lookup, so peeling the outer generator
off it is **not** a cheap defeq. Writing the step as
`show mulσᵢ h (wordAction h inner (e₄ g)) = _` forces that lookup against an
already-applied argument and blows `maxRecDepth` — or times out `whnf` — at
the deeper indices; measured, 50 errors across the 72 (indices 17, 20, 22, 23
among them, but also plenty of shallow ones). Stated generically in `u`, the
same peel is `simp [wordAction]` and costs well under a second. So the index
lookup is paid **once per word** (`wordAction_step_j`, 24 of them) rather
than once per fact (72), and the facts below are pure `rw` chains.

## The observed shape

Every one of the 72 results has **at most two terms**, with coefficients of
degree at most one in `h`:

    b_j · σ  =  e₄ k        or        e₄ k + h • e₄ j

A generator step on a two-term combination could a priori produce four terms
with an `h²`; it never does — the quadratic fold always lands back on a term
already present. The generator that emits this file asserts the bound, so a
regression would fail there as well as in Lean.

## Why (bean qou-x64l)

These are what the generator cases of `trM4` cyclicity run on. Cyclicity need
only be checked on generators, because the elements that commute with
everything under the trace form a subalgebra — so the ASCII Gram chain, its
576 Gram pairs and its five Markov weights, are not needed for it.

## Provenance

Generated, not transcribed. The generator tables are read back out of
`H4GeneratorAction`'s own 72 statements, and the word tree out of
`wordAction`'s own `![...]` definition; the emitter checks that each word's
tail is itself a word, so the tree is verified rather than assumed. Lean then
re-checks every statement against `wordAction`.
-/
import QOU.Machinery.H4GeneratorAction

namespace QOU.Machinery.H4

variable {R : Type*} [CommRing R]

/-! ## Peeling one generator off a word

`wordAction j = mulσᵢ ∘ wordAction inner` — stated in `u`, where the
`Matrix.cons` index lookup is cheap. -/

theorem wordAction_step_0 (h : R) (u : Fin 24 → R) :
    wordAction h (0 : Fin 24) u = u := by
  simp [wordAction]

theorem wordAction_step_1 (h : R) (u : Fin 24 → R) :
    wordAction h (1 : Fin 24) u = mulσ₀ h (wordAction h (0 : Fin 24) u) := by
  simp [wordAction]

theorem wordAction_step_2 (h : R) (u : Fin 24 → R) :
    wordAction h (2 : Fin 24) u = mulσ₁ h (wordAction h (0 : Fin 24) u) := by
  simp [wordAction]

theorem wordAction_step_3 (h : R) (u : Fin 24 → R) :
    wordAction h (3 : Fin 24) u = mulσ₀ h (wordAction h (2 : Fin 24) u) := by
  simp [wordAction]

theorem wordAction_step_4 (h : R) (u : Fin 24 → R) :
    wordAction h (4 : Fin 24) u = mulσ₁ h (wordAction h (1 : Fin 24) u) := by
  simp [wordAction]

theorem wordAction_step_5 (h : R) (u : Fin 24 → R) :
    wordAction h (5 : Fin 24) u = mulσ₀ h (wordAction h (4 : Fin 24) u) := by
  simp [wordAction]

theorem wordAction_step_6 (h : R) (u : Fin 24 → R) :
    wordAction h (6 : Fin 24) u = mulσ₂ h (wordAction h (0 : Fin 24) u) := by
  simp [wordAction]

theorem wordAction_step_7 (h : R) (u : Fin 24 → R) :
    wordAction h (7 : Fin 24) u = mulσ₂ h (wordAction h (2 : Fin 24) u) := by
  simp [wordAction]

theorem wordAction_step_8 (h : R) (u : Fin 24 → R) :
    wordAction h (8 : Fin 24) u = mulσ₀ h (wordAction h (6 : Fin 24) u) := by
  simp [wordAction]

theorem wordAction_step_9 (h : R) (u : Fin 24 → R) :
    wordAction h (9 : Fin 24) u = mulσ₁ h (wordAction h (6 : Fin 24) u) := by
  simp [wordAction]

theorem wordAction_step_10 (h : R) (u : Fin 24 → R) :
    wordAction h (10 : Fin 24) u = mulσ₂ h (wordAction h (4 : Fin 24) u) := by
  simp [wordAction]

theorem wordAction_step_11 (h : R) (u : Fin 24 → R) :
    wordAction h (11 : Fin 24) u = mulσ₂ h (wordAction h (3 : Fin 24) u) := by
  simp [wordAction]

theorem wordAction_step_12 (h : R) (u : Fin 24 → R) :
    wordAction h (12 : Fin 24) u = mulσ₁ h (wordAction h (7 : Fin 24) u) := by
  simp [wordAction]

theorem wordAction_step_13 (h : R) (u : Fin 24 → R) :
    wordAction h (13 : Fin 24) u = mulσ₁ h (wordAction h (8 : Fin 24) u) := by
  simp [wordAction]

theorem wordAction_step_14 (h : R) (u : Fin 24 → R) :
    wordAction h (14 : Fin 24) u = mulσ₀ h (wordAction h (9 : Fin 24) u) := by
  simp [wordAction]

theorem wordAction_step_15 (h : R) (u : Fin 24 → R) :
    wordAction h (15 : Fin 24) u = mulσ₂ h (wordAction h (5 : Fin 24) u) := by
  simp [wordAction]

theorem wordAction_step_16 (h : R) (u : Fin 24 → R) :
    wordAction h (16 : Fin 24) u = mulσ₁ h (wordAction h (10 : Fin 24) u) := by
  simp [wordAction]

theorem wordAction_step_17 (h : R) (u : Fin 24 → R) :
    wordAction h (17 : Fin 24) u = mulσ₁ h (wordAction h (11 : Fin 24) u) := by
  simp [wordAction]

theorem wordAction_step_18 (h : R) (u : Fin 24 → R) :
    wordAction h (18 : Fin 24) u = mulσ₀ h (wordAction h (12 : Fin 24) u) := by
  simp [wordAction]

theorem wordAction_step_19 (h : R) (u : Fin 24 → R) :
    wordAction h (19 : Fin 24) u = mulσ₀ h (wordAction h (13 : Fin 24) u) := by
  simp [wordAction]

theorem wordAction_step_20 (h : R) (u : Fin 24 → R) :
    wordAction h (20 : Fin 24) u = mulσ₁ h (wordAction h (15 : Fin 24) u) := by
  simp [wordAction]

theorem wordAction_step_21 (h : R) (u : Fin 24 → R) :
    wordAction h (21 : Fin 24) u = mulσ₀ h (wordAction h (16 : Fin 24) u) := by
  simp [wordAction]

theorem wordAction_step_22 (h : R) (u : Fin 24 → R) :
    wordAction h (22 : Fin 24) u = mulσ₀ h (wordAction h (17 : Fin 24) u) := by
  simp [wordAction]

theorem wordAction_step_23 (h : R) (u : Fin 24 → R) :
    wordAction h (23 : Fin 24) u = mulσ₀ h (wordAction h (20 : Fin 24) u) := by
  simp [wordAction]

/-! ## The word actions on `e₄ 1` (the generator `σ₀`) -/

theorem wordAction_e₄_0_1 (h : R) :
    wordAction h (0 : Fin 24) (e₄ (1 : Fin 24)) = e₄ (1 : Fin 24) :=
  wordAction_step_0 h _

theorem wordAction_e₄_1_1 (h : R) :
    wordAction h (1 : Fin 24) (e₄ (1 : Fin 24)) = e₄ (0 : Fin 24) + h • e₄ (1 : Fin 24) := by
  rw [wordAction_step_1, wordAction_e₄_0_1, mulσ₀_e₄_1]

theorem wordAction_e₄_2_1 (h : R) :
    wordAction h (2 : Fin 24) (e₄ (1 : Fin 24)) = e₄ (4 : Fin 24) := by
  rw [wordAction_step_2, wordAction_e₄_0_1, mulσ₁_e₄_1]

theorem wordAction_e₄_3_1 (h : R) :
    wordAction h (3 : Fin 24) (e₄ (1 : Fin 24)) = e₄ (5 : Fin 24) := by
  rw [wordAction_step_3, wordAction_e₄_2_1, mulσ₀_e₄_4]

theorem wordAction_e₄_4_1 (h : R) :
    wordAction h (4 : Fin 24) (e₄ (1 : Fin 24)) = e₄ (2 : Fin 24) + h • e₄ (4 : Fin 24) := by
  rw [wordAction_step_4, wordAction_e₄_1_1]
  simp only [mulσ₁_add, mulσ₁_smul, mulσ₁_e₄_0, mulσ₁_e₄_1]

theorem wordAction_e₄_5_1 (h : R) :
    wordAction h (5 : Fin 24) (e₄ (1 : Fin 24)) = e₄ (3 : Fin 24) + h • e₄ (5 : Fin 24) := by
  rw [wordAction_step_5, wordAction_e₄_4_1]
  simp only [mulσ₀_add, mulσ₀_smul, mulσ₀_e₄_2, mulσ₀_e₄_4]

theorem wordAction_e₄_6_1 (h : R) :
    wordAction h (6 : Fin 24) (e₄ (1 : Fin 24)) = e₄ (8 : Fin 24) := by
  rw [wordAction_step_6, wordAction_e₄_0_1, mulσ₂_e₄_1]

theorem wordAction_e₄_7_1 (h : R) :
    wordAction h (7 : Fin 24) (e₄ (1 : Fin 24)) = e₄ (10 : Fin 24) := by
  rw [wordAction_step_7, wordAction_e₄_2_1, mulσ₂_e₄_4]

theorem wordAction_e₄_8_1 (h : R) :
    wordAction h (8 : Fin 24) (e₄ (1 : Fin 24)) = e₄ (6 : Fin 24) + h • e₄ (8 : Fin 24) := by
  rw [wordAction_step_8, wordAction_e₄_6_1, mulσ₀_e₄_8]

theorem wordAction_e₄_9_1 (h : R) :
    wordAction h (9 : Fin 24) (e₄ (1 : Fin 24)) = e₄ (13 : Fin 24) := by
  rw [wordAction_step_9, wordAction_e₄_6_1, mulσ₁_e₄_8]

theorem wordAction_e₄_10_1 (h : R) :
    wordAction h (10 : Fin 24) (e₄ (1 : Fin 24)) = e₄ (7 : Fin 24) + h • e₄ (10 : Fin 24) := by
  rw [wordAction_step_10, wordAction_e₄_4_1]
  simp only [mulσ₂_add, mulσ₂_smul, mulσ₂_e₄_2, mulσ₂_e₄_4]

theorem wordAction_e₄_11_1 (h : R) :
    wordAction h (11 : Fin 24) (e₄ (1 : Fin 24)) = e₄ (15 : Fin 24) := by
  rw [wordAction_step_11, wordAction_e₄_3_1, mulσ₂_e₄_5]

theorem wordAction_e₄_12_1 (h : R) :
    wordAction h (12 : Fin 24) (e₄ (1 : Fin 24)) = e₄ (16 : Fin 24) := by
  rw [wordAction_step_12, wordAction_e₄_7_1, mulσ₁_e₄_10]

theorem wordAction_e₄_13_1 (h : R) :
    wordAction h (13 : Fin 24) (e₄ (1 : Fin 24)) = e₄ (9 : Fin 24) + h • e₄ (13 : Fin 24) := by
  rw [wordAction_step_13, wordAction_e₄_8_1]
  simp only [mulσ₁_add, mulσ₁_smul, mulσ₁_e₄_6, mulσ₁_e₄_8]

theorem wordAction_e₄_14_1 (h : R) :
    wordAction h (14 : Fin 24) (e₄ (1 : Fin 24)) = e₄ (19 : Fin 24) := by
  rw [wordAction_step_14, wordAction_e₄_9_1, mulσ₀_e₄_13]

theorem wordAction_e₄_15_1 (h : R) :
    wordAction h (15 : Fin 24) (e₄ (1 : Fin 24)) = e₄ (11 : Fin 24) + h • e₄ (15 : Fin 24) := by
  rw [wordAction_step_15, wordAction_e₄_5_1]
  simp only [mulσ₂_add, mulσ₂_smul, mulσ₂_e₄_3, mulσ₂_e₄_5]

theorem wordAction_e₄_16_1 (h : R) :
    wordAction h (16 : Fin 24) (e₄ (1 : Fin 24)) = e₄ (12 : Fin 24) + h • e₄ (16 : Fin 24) := by
  rw [wordAction_step_16, wordAction_e₄_10_1]
  simp only [mulσ₁_add, mulσ₁_smul, mulσ₁_e₄_7, mulσ₁_e₄_10]

theorem wordAction_e₄_17_1 (h : R) :
    wordAction h (17 : Fin 24) (e₄ (1 : Fin 24)) = e₄ (20 : Fin 24) := by
  rw [wordAction_step_17, wordAction_e₄_11_1, mulσ₁_e₄_15]

theorem wordAction_e₄_18_1 (h : R) :
    wordAction h (18 : Fin 24) (e₄ (1 : Fin 24)) = e₄ (21 : Fin 24) := by
  rw [wordAction_step_18, wordAction_e₄_12_1, mulσ₀_e₄_16]

theorem wordAction_e₄_19_1 (h : R) :
    wordAction h (19 : Fin 24) (e₄ (1 : Fin 24)) = e₄ (14 : Fin 24) + h • e₄ (19 : Fin 24) := by
  rw [wordAction_step_19, wordAction_e₄_13_1]
  simp only [mulσ₀_add, mulσ₀_smul, mulσ₀_e₄_9, mulσ₀_e₄_13]

theorem wordAction_e₄_20_1 (h : R) :
    wordAction h (20 : Fin 24) (e₄ (1 : Fin 24)) = e₄ (17 : Fin 24) + h • e₄ (20 : Fin 24) := by
  rw [wordAction_step_20, wordAction_e₄_15_1]
  simp only [mulσ₁_add, mulσ₁_smul, mulσ₁_e₄_11, mulσ₁_e₄_15]

theorem wordAction_e₄_21_1 (h : R) :
    wordAction h (21 : Fin 24) (e₄ (1 : Fin 24)) = e₄ (18 : Fin 24) + h • e₄ (21 : Fin 24) := by
  rw [wordAction_step_21, wordAction_e₄_16_1]
  simp only [mulσ₀_add, mulσ₀_smul, mulσ₀_e₄_12, mulσ₀_e₄_16]

theorem wordAction_e₄_22_1 (h : R) :
    wordAction h (22 : Fin 24) (e₄ (1 : Fin 24)) = e₄ (23 : Fin 24) := by
  rw [wordAction_step_22, wordAction_e₄_17_1, mulσ₀_e₄_20]

theorem wordAction_e₄_23_1 (h : R) :
    wordAction h (23 : Fin 24) (e₄ (1 : Fin 24)) = e₄ (22 : Fin 24) + h • e₄ (23 : Fin 24) := by
  rw [wordAction_step_23, wordAction_e₄_20_1]
  simp only [mulσ₀_add, mulσ₀_smul, mulσ₀_e₄_17, mulσ₀_e₄_20]

/-! ## The word actions on `e₄ 2` (the generator `σ₁`) -/

theorem wordAction_e₄_0_2 (h : R) :
    wordAction h (0 : Fin 24) (e₄ (2 : Fin 24)) = e₄ (2 : Fin 24) :=
  wordAction_step_0 h _

theorem wordAction_e₄_1_2 (h : R) :
    wordAction h (1 : Fin 24) (e₄ (2 : Fin 24)) = e₄ (3 : Fin 24) := by
  rw [wordAction_step_1, wordAction_e₄_0_2, mulσ₀_e₄_2]

theorem wordAction_e₄_2_2 (h : R) :
    wordAction h (2 : Fin 24) (e₄ (2 : Fin 24)) = e₄ (0 : Fin 24) + h • e₄ (2 : Fin 24) := by
  rw [wordAction_step_2, wordAction_e₄_0_2, mulσ₁_e₄_2]

theorem wordAction_e₄_3_2 (h : R) :
    wordAction h (3 : Fin 24) (e₄ (2 : Fin 24)) = e₄ (1 : Fin 24) + h • e₄ (3 : Fin 24) := by
  rw [wordAction_step_3, wordAction_e₄_2_2]
  simp only [mulσ₀_add, mulσ₀_smul, mulσ₀_e₄_0, mulσ₀_e₄_2]

theorem wordAction_e₄_4_2 (h : R) :
    wordAction h (4 : Fin 24) (e₄ (2 : Fin 24)) = e₄ (5 : Fin 24) := by
  rw [wordAction_step_4, wordAction_e₄_1_2, mulσ₁_e₄_3]

theorem wordAction_e₄_5_2 (h : R) :
    wordAction h (5 : Fin 24) (e₄ (2 : Fin 24)) = e₄ (4 : Fin 24) + h • e₄ (5 : Fin 24) := by
  rw [wordAction_step_5, wordAction_e₄_4_2, mulσ₀_e₄_5]

theorem wordAction_e₄_6_2 (h : R) :
    wordAction h (6 : Fin 24) (e₄ (2 : Fin 24)) = e₄ (7 : Fin 24) := by
  rw [wordAction_step_6, wordAction_e₄_0_2, mulσ₂_e₄_2]

theorem wordAction_e₄_7_2 (h : R) :
    wordAction h (7 : Fin 24) (e₄ (2 : Fin 24)) = e₄ (6 : Fin 24) + h • e₄ (7 : Fin 24) := by
  rw [wordAction_step_7, wordAction_e₄_2_2]
  simp only [mulσ₂_add, mulσ₂_smul, mulσ₂_e₄_0, mulσ₂_e₄_2]

theorem wordAction_e₄_8_2 (h : R) :
    wordAction h (8 : Fin 24) (e₄ (2 : Fin 24)) = e₄ (11 : Fin 24) := by
  rw [wordAction_step_8, wordAction_e₄_6_2, mulσ₀_e₄_7]

theorem wordAction_e₄_9_2 (h : R) :
    wordAction h (9 : Fin 24) (e₄ (2 : Fin 24)) = e₄ (12 : Fin 24) := by
  rw [wordAction_step_9, wordAction_e₄_6_2, mulσ₁_e₄_7]

theorem wordAction_e₄_10_2 (h : R) :
    wordAction h (10 : Fin 24) (e₄ (2 : Fin 24)) = e₄ (15 : Fin 24) := by
  rw [wordAction_step_10, wordAction_e₄_4_2, mulσ₂_e₄_5]

theorem wordAction_e₄_11_2 (h : R) :
    wordAction h (11 : Fin 24) (e₄ (2 : Fin 24)) = e₄ (8 : Fin 24) + h • e₄ (11 : Fin 24) := by
  rw [wordAction_step_11, wordAction_e₄_3_2]
  simp only [mulσ₂_add, mulσ₂_smul, mulσ₂_e₄_1, mulσ₂_e₄_3]

theorem wordAction_e₄_12_2 (h : R) :
    wordAction h (12 : Fin 24) (e₄ (2 : Fin 24)) = e₄ (9 : Fin 24) + h • e₄ (12 : Fin 24) := by
  rw [wordAction_step_12, wordAction_e₄_7_2]
  simp only [mulσ₁_add, mulσ₁_smul, mulσ₁_e₄_6, mulσ₁_e₄_7]

theorem wordAction_e₄_13_2 (h : R) :
    wordAction h (13 : Fin 24) (e₄ (2 : Fin 24)) = e₄ (17 : Fin 24) := by
  rw [wordAction_step_13, wordAction_e₄_8_2, mulσ₁_e₄_11]

theorem wordAction_e₄_14_2 (h : R) :
    wordAction h (14 : Fin 24) (e₄ (2 : Fin 24)) = e₄ (18 : Fin 24) := by
  rw [wordAction_step_14, wordAction_e₄_9_2, mulσ₀_e₄_12]

theorem wordAction_e₄_15_2 (h : R) :
    wordAction h (15 : Fin 24) (e₄ (2 : Fin 24)) = e₄ (10 : Fin 24) + h • e₄ (15 : Fin 24) := by
  rw [wordAction_step_15, wordAction_e₄_5_2]
  simp only [mulσ₂_add, mulσ₂_smul, mulσ₂_e₄_4, mulσ₂_e₄_5]

theorem wordAction_e₄_16_2 (h : R) :
    wordAction h (16 : Fin 24) (e₄ (2 : Fin 24)) = e₄ (20 : Fin 24) := by
  rw [wordAction_step_16, wordAction_e₄_10_2, mulσ₁_e₄_15]

theorem wordAction_e₄_17_2 (h : R) :
    wordAction h (17 : Fin 24) (e₄ (2 : Fin 24)) = e₄ (13 : Fin 24) + h • e₄ (17 : Fin 24) := by
  rw [wordAction_step_17, wordAction_e₄_11_2]
  simp only [mulσ₁_add, mulσ₁_smul, mulσ₁_e₄_8, mulσ₁_e₄_11]

theorem wordAction_e₄_18_2 (h : R) :
    wordAction h (18 : Fin 24) (e₄ (2 : Fin 24)) = e₄ (14 : Fin 24) + h • e₄ (18 : Fin 24) := by
  rw [wordAction_step_18, wordAction_e₄_12_2]
  simp only [mulσ₀_add, mulσ₀_smul, mulσ₀_e₄_9, mulσ₀_e₄_12]

theorem wordAction_e₄_19_2 (h : R) :
    wordAction h (19 : Fin 24) (e₄ (2 : Fin 24)) = e₄ (22 : Fin 24) := by
  rw [wordAction_step_19, wordAction_e₄_13_2, mulσ₀_e₄_17]

theorem wordAction_e₄_20_2 (h : R) :
    wordAction h (20 : Fin 24) (e₄ (2 : Fin 24)) = e₄ (16 : Fin 24) + h • e₄ (20 : Fin 24) := by
  rw [wordAction_step_20, wordAction_e₄_15_2]
  simp only [mulσ₁_add, mulσ₁_smul, mulσ₁_e₄_10, mulσ₁_e₄_15]

theorem wordAction_e₄_21_2 (h : R) :
    wordAction h (21 : Fin 24) (e₄ (2 : Fin 24)) = e₄ (23 : Fin 24) := by
  rw [wordAction_step_21, wordAction_e₄_16_2, mulσ₀_e₄_20]

theorem wordAction_e₄_22_2 (h : R) :
    wordAction h (22 : Fin 24) (e₄ (2 : Fin 24)) = e₄ (19 : Fin 24) + h • e₄ (22 : Fin 24) := by
  rw [wordAction_step_22, wordAction_e₄_17_2]
  simp only [mulσ₀_add, mulσ₀_smul, mulσ₀_e₄_13, mulσ₀_e₄_17]

theorem wordAction_e₄_23_2 (h : R) :
    wordAction h (23 : Fin 24) (e₄ (2 : Fin 24)) = e₄ (21 : Fin 24) + h • e₄ (23 : Fin 24) := by
  rw [wordAction_step_23, wordAction_e₄_20_2]
  simp only [mulσ₀_add, mulσ₀_smul, mulσ₀_e₄_16, mulσ₀_e₄_20]

/-! ## The word actions on `e₄ 6` (the generator `σ₂`) -/

theorem wordAction_e₄_0_6 (h : R) :
    wordAction h (0 : Fin 24) (e₄ (6 : Fin 24)) = e₄ (6 : Fin 24) :=
  wordAction_step_0 h _

theorem wordAction_e₄_1_6 (h : R) :
    wordAction h (1 : Fin 24) (e₄ (6 : Fin 24)) = e₄ (8 : Fin 24) := by
  rw [wordAction_step_1, wordAction_e₄_0_6, mulσ₀_e₄_6]

theorem wordAction_e₄_2_6 (h : R) :
    wordAction h (2 : Fin 24) (e₄ (6 : Fin 24)) = e₄ (9 : Fin 24) := by
  rw [wordAction_step_2, wordAction_e₄_0_6, mulσ₁_e₄_6]

theorem wordAction_e₄_3_6 (h : R) :
    wordAction h (3 : Fin 24) (e₄ (6 : Fin 24)) = e₄ (14 : Fin 24) := by
  rw [wordAction_step_3, wordAction_e₄_2_6, mulσ₀_e₄_9]

theorem wordAction_e₄_4_6 (h : R) :
    wordAction h (4 : Fin 24) (e₄ (6 : Fin 24)) = e₄ (13 : Fin 24) := by
  rw [wordAction_step_4, wordAction_e₄_1_6, mulσ₁_e₄_8]

theorem wordAction_e₄_5_6 (h : R) :
    wordAction h (5 : Fin 24) (e₄ (6 : Fin 24)) = e₄ (19 : Fin 24) := by
  rw [wordAction_step_5, wordAction_e₄_4_6, mulσ₀_e₄_13]

theorem wordAction_e₄_6_6 (h : R) :
    wordAction h (6 : Fin 24) (e₄ (6 : Fin 24)) = e₄ (0 : Fin 24) + h • e₄ (6 : Fin 24) := by
  rw [wordAction_step_6, wordAction_e₄_0_6, mulσ₂_e₄_6]

theorem wordAction_e₄_7_6 (h : R) :
    wordAction h (7 : Fin 24) (e₄ (6 : Fin 24)) = e₄ (12 : Fin 24) := by
  rw [wordAction_step_7, wordAction_e₄_2_6, mulσ₂_e₄_9]

theorem wordAction_e₄_8_6 (h : R) :
    wordAction h (8 : Fin 24) (e₄ (6 : Fin 24)) = e₄ (1 : Fin 24) + h • e₄ (8 : Fin 24) := by
  rw [wordAction_step_8, wordAction_e₄_6_6]
  simp only [mulσ₀_add, mulσ₀_smul, mulσ₀_e₄_0, mulσ₀_e₄_6]

theorem wordAction_e₄_9_6 (h : R) :
    wordAction h (9 : Fin 24) (e₄ (6 : Fin 24)) = e₄ (2 : Fin 24) + h • e₄ (9 : Fin 24) := by
  rw [wordAction_step_9, wordAction_e₄_6_6]
  simp only [mulσ₁_add, mulσ₁_smul, mulσ₁_e₄_0, mulσ₁_e₄_6]

theorem wordAction_e₄_10_6 (h : R) :
    wordAction h (10 : Fin 24) (e₄ (6 : Fin 24)) = e₄ (16 : Fin 24) := by
  rw [wordAction_step_10, wordAction_e₄_4_6, mulσ₂_e₄_13]

theorem wordAction_e₄_11_6 (h : R) :
    wordAction h (11 : Fin 24) (e₄ (6 : Fin 24)) = e₄ (18 : Fin 24) := by
  rw [wordAction_step_11, wordAction_e₄_3_6, mulσ₂_e₄_14]

theorem wordAction_e₄_12_6 (h : R) :
    wordAction h (12 : Fin 24) (e₄ (6 : Fin 24)) = e₄ (7 : Fin 24) + h • e₄ (12 : Fin 24) := by
  rw [wordAction_step_12, wordAction_e₄_7_6, mulσ₁_e₄_12]

theorem wordAction_e₄_13_6 (h : R) :
    wordAction h (13 : Fin 24) (e₄ (6 : Fin 24)) = e₄ (4 : Fin 24) + h • e₄ (13 : Fin 24) := by
  rw [wordAction_step_13, wordAction_e₄_8_6]
  simp only [mulσ₁_add, mulσ₁_smul, mulσ₁_e₄_1, mulσ₁_e₄_8]

theorem wordAction_e₄_14_6 (h : R) :
    wordAction h (14 : Fin 24) (e₄ (6 : Fin 24)) = e₄ (3 : Fin 24) + h • e₄ (14 : Fin 24) := by
  rw [wordAction_step_14, wordAction_e₄_9_6]
  simp only [mulσ₀_add, mulσ₀_smul, mulσ₀_e₄_2, mulσ₀_e₄_9]

theorem wordAction_e₄_15_6 (h : R) :
    wordAction h (15 : Fin 24) (e₄ (6 : Fin 24)) = e₄ (21 : Fin 24) := by
  rw [wordAction_step_15, wordAction_e₄_5_6, mulσ₂_e₄_19]

theorem wordAction_e₄_16_6 (h : R) :
    wordAction h (16 : Fin 24) (e₄ (6 : Fin 24)) = e₄ (10 : Fin 24) + h • e₄ (16 : Fin 24) := by
  rw [wordAction_step_16, wordAction_e₄_10_6, mulσ₁_e₄_16]

theorem wordAction_e₄_17_6 (h : R) :
    wordAction h (17 : Fin 24) (e₄ (6 : Fin 24)) = e₄ (22 : Fin 24) := by
  rw [wordAction_step_17, wordAction_e₄_11_6, mulσ₁_e₄_18]

theorem wordAction_e₄_18_6 (h : R) :
    wordAction h (18 : Fin 24) (e₄ (6 : Fin 24)) = e₄ (11 : Fin 24) + h • e₄ (18 : Fin 24) := by
  rw [wordAction_step_18, wordAction_e₄_12_6]
  simp only [mulσ₀_add, mulσ₀_smul, mulσ₀_e₄_7, mulσ₀_e₄_12]

theorem wordAction_e₄_19_6 (h : R) :
    wordAction h (19 : Fin 24) (e₄ (6 : Fin 24)) = e₄ (5 : Fin 24) + h • e₄ (19 : Fin 24) := by
  rw [wordAction_step_19, wordAction_e₄_13_6]
  simp only [mulσ₀_add, mulσ₀_smul, mulσ₀_e₄_4, mulσ₀_e₄_13]

theorem wordAction_e₄_20_6 (h : R) :
    wordAction h (20 : Fin 24) (e₄ (6 : Fin 24)) = e₄ (23 : Fin 24) := by
  rw [wordAction_step_20, wordAction_e₄_15_6, mulσ₁_e₄_21]

theorem wordAction_e₄_21_6 (h : R) :
    wordAction h (21 : Fin 24) (e₄ (6 : Fin 24)) = e₄ (15 : Fin 24) + h • e₄ (21 : Fin 24) := by
  rw [wordAction_step_21, wordAction_e₄_16_6]
  simp only [mulσ₀_add, mulσ₀_smul, mulσ₀_e₄_10, mulσ₀_e₄_16]

theorem wordAction_e₄_22_6 (h : R) :
    wordAction h (22 : Fin 24) (e₄ (6 : Fin 24)) = e₄ (17 : Fin 24) + h • e₄ (22 : Fin 24) := by
  rw [wordAction_step_22, wordAction_e₄_17_6, mulσ₀_e₄_22]

theorem wordAction_e₄_23_6 (h : R) :
    wordAction h (23 : Fin 24) (e₄ (6 : Fin 24)) = e₄ (20 : Fin 24) + h • e₄ (23 : Fin 24) := by
  rw [wordAction_step_23, wordAction_e₄_20_6, mulσ₀_e₄_23]

end QOU.Machinery.H4
