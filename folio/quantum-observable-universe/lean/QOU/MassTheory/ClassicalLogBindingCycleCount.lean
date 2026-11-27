import MathlibExt.OrbitCount
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic

/-!
# The classical part of the ruled log binding law is a merge count

Brief C2 of the compute-accuracy epic (`qou-myts`), towards the open kernel `qou-brng`.
Audit: `docs/audits/2026-11-27-classical-log-binding-cycle-count.md`; probe:
`computations/probes/classical_log_binding_cycle_count/classical_log_binding_cycle_count_probe.py`.

## Setting

The ruled binding law is `B = E₀ · log (tr_free / tr_atom)` (`QOU.Nuclear.LogFormUniqueness`).
At `q = 1` the convention-D Markov trace of a braid word is the normalised trace of the
underlying permutation `σ` on `(ℂ²)^{⊗n}`, namely `2^{c(σ)} / 2^n`, with `c = orbitCount`
(`MathlibExt.TensorTraceCharacter.trace_permMatrixOf_two`; the Hecke-to-`ℂSₙ` specialisation is
Schur–Weyl at `q = 1`, the same step 1 `ClassicalTraceFloor` uses). `ClassicalTraceFloor`
evaluated the retired **linear** difference `tr_free − tr_atom` on that trace. This file
evaluates the **ruled log** law on it. That was planned as "S2" in
`docs/audits/2026-09-07-route-c-step3-and-kz-level-plans.md` §2 and never formalised.

## What is proved

1. `classicalLogBinding_eq` — `B_cl = E₀ · log 2 · (c(σ_free) − c(σ_atom))`. The classical
   log binding is `E₀ log 2` times a whole number: the number of closure components the bonds
   merge.
2. `classicalLogBinding_of_trivial_free` — when the free word is classically trivial
   (`σ_free = 1`, as for the γγ nucleon `V³`), `B_cl = E₀ · log 2 · orbitDefect σ_atom`, where
   `orbitDefect = n − c` is the transposition (Cayley) length.
3. `orbitDefect_le_card_sub_one`, `classicalLogBinding_le_ceiling` — at most `n − 1` merges, so
   on `n = k·A` strands `B_cl ≤ E₀ · log 2 · (k A − 1) < A · E₀ · log (2^k)`; for three strands
   per nucleon the per-nucleon ceiling is `E₀ · log 8`. `ceiling_attained` shows the bound is
   reached exactly by a one-component closure.
4. `orbitDefect_mul_le` — the Cayley length is subadditive. Hence
   `classicalB3_nonpos_of_product`: if the three-nucleon atom permutation is the product of the
   three pair-bond permutations (on classically trivial nucleons), then the classical connected
   three-body term `b₃ = B₁₂₃ − B₁₂ − B₁₃ − B₂₃` is `≤ 0`. A positive classical `b₃` needs an
   atom permutation that is not a product of its pair bonds.
5. `classicalB3_quantised` — whatever the words, the classical `b₃` is `E₀ log 2` times an
   integer.
6. Concrete words (`decide`): the γγ nucleon `V³ = (σ₀σ₁⁻¹)³` is classically the identity; on
   the six-strand deuteron the selected bond `V(2)³` merges **zero** components, while the
   single vertex `V(1)` merges **two**. This is the structural reason the selected γγ deuteron
   binds by keV: its whole binding is a `q`-deformation correction. Every vertex is a 3-cycle,
   so every pure-junction bond is an even permutation and merges an even number of components
   (`merges_even_of_sign_one`, `vertex_sign`).

## What is NOT claimed

Nothing here is evaluated at `q₀`, and nothing is compared with data. The ceiling is a
statement about the `q = 1` part of the trace only; the probe measures how far the `q₀` trace
departs from it. No empirical number enters any statement.

## Base ring (§7c)

Permutation statements are over a generic `[Fintype α] [DecidableEq α]`. The log statements
are over `ℝ` because `Real.log` is archimedean; they use no ordering beyond that and no
anchor.
-/

namespace QOU.MassTheory.ClassicalLogBindingCycleCount

open Equiv Equiv.Perm QOU.MassTheory

/-! ## The log law on the `q = 1` trace -/

/-- The ruled log binding law, `B = E₀ · log (tr_free / tr_atom)`. -/
noncomputable def logBinding (E₀ trFree trAtom : ℝ) : ℝ := E₀ * Real.log (trFree / trAtom)

/-- The `q = 1` (Schur–Weyl) trace of a permutation of `n` strands: `2^{c(σ)} / 2^n`. -/
noncomputable def classicalTrace {α : Type*} [Fintype α] [DecidableEq α] (σ : Perm α) : ℝ :=
  (2 : ℝ) ^ orbitCount σ / (2 : ℝ) ^ Fintype.card α

/-- The classical log binding of an assembly: the log law on the `q = 1` traces. -/
noncomputable def classicalLogBinding {α : Type*} [Fintype α] [DecidableEq α]
    (E₀ : ℝ) (σFree σAtom : Perm α) : ℝ :=
  logBinding E₀ (classicalTrace σFree) (classicalTrace σAtom)

variable {α : Type*} [Fintype α] [DecidableEq α]

/-- **1. The classical log binding is a merge count.**
`B_cl = E₀ · log 2 · (c(σ_free) − c(σ_atom))`. -/
theorem classicalLogBinding_eq (E₀ : ℝ) (σFree σAtom : Perm α) :
    classicalLogBinding E₀ σFree σAtom
      = E₀ * Real.log 2 * ((orbitCount σFree : ℝ) - (orbitCount σAtom : ℝ)) := by
  unfold classicalLogBinding logBinding classicalTrace
  have h2 : (0 : ℝ) < 2 := by norm_num
  have hn : (2 : ℝ) ^ Fintype.card α ≠ 0 := by positivity
  rw [div_div_div_cancel_right₀ hn, ← zpow_natCast, ← zpow_natCast, ← zpow_sub₀ h2.ne',
    Real.log_zpow]
  push_cast
  ring

/-- `c = n − orbitDefect`, read in `ℝ` (the `ℕ` subtraction is honest). -/
theorem orbitCount_cast (σ : Perm α) :
    (orbitCount σ : ℝ) = (Fintype.card α : ℝ) - (orbitDefect σ : ℝ) := by
  have h := orbitDefect_le_card σ
  unfold orbitCount
  rw [Nat.cast_sub h]

/-- **2. Classically trivial free word.** With `σ_free = 1` the classical log binding is
`E₀ · log 2` times the Cayley length of the atom permutation. -/
theorem classicalLogBinding_of_trivial_free (E₀ : ℝ) (σAtom : Perm α) :
    classicalLogBinding E₀ 1 σAtom = E₀ * Real.log 2 * (orbitDefect σAtom : ℝ) := by
  rw [classicalLogBinding_eq, orbitCount_one, orbitCount_cast]
  ring

/-! ## The ceiling -/

/-- A permutation of a nonempty finite set has at least one cycle (fixed points count), so at
most `n − 1` merges are possible. -/
theorem orbitDefect_le_card_sub_one [Nonempty α] (σ : Perm α) :
    orbitDefect σ + 1 ≤ Fintype.card α := by
  unfold orbitDefect
  by_cases hs : σ = 1
  · subst hs
    have := (Fintype.card_pos : 0 < Fintype.card α)
    simp
    omega
  · have hct : 0 < Multiset.card σ.cycleType := by
      rw [Multiset.card_pos]
      intro h
      exact hs (cycleType_eq_zero.mp h)
    have hsupp : σ.support.card ≤ Fintype.card α := Finset.card_le_univ _
    have hle := card_cycleType_le_card_support σ
    omega

/-- **3a. The classical ceiling.** On `n = k·A` strands, with a classically trivial free word
and `E₀ ≥ 0`, `B_cl ≤ E₀ · log 2 · (k A − 1)`. -/
theorem classicalLogBinding_le_ceiling [Nonempty α] {E₀ : ℝ} (hE : 0 ≤ E₀) {k A : ℕ}
    (hn : Fintype.card α = k * A) (σAtom : Perm α) :
    classicalLogBinding E₀ 1 σAtom ≤ E₀ * Real.log 2 * ((k * A : ℕ) - 1 : ℝ) := by
  rw [classicalLogBinding_of_trivial_free]
  have hd := orbitDefect_le_card_sub_one σAtom
  rw [hn] at hd
  have hd' : (orbitDefect σAtom : ℝ) ≤ ((k * A : ℕ) : ℝ) - 1 := by
    have : ((orbitDefect σAtom + 1 : ℕ) : ℝ) ≤ ((k * A : ℕ) : ℝ) := by exact_mod_cast hd
    push_cast at this ⊢
    linarith
  have hl : 0 ≤ E₀ * Real.log 2 := mul_nonneg hE (Real.log_nonneg (by norm_num))
  exact mul_le_mul_of_nonneg_left hd' hl

/-- **3b. Per nucleon, strictly below `E₀ · log 2^k`.** For three strands per nucleon this is
`E₀ · log 8`. -/
theorem ceiling_lt_per_nucleon {E₀ : ℝ} (hE : 0 < E₀) (k A : ℕ) :
    E₀ * Real.log 2 * ((k * A : ℕ) - 1 : ℝ) < A * (E₀ * Real.log ((2 : ℝ) ^ k)) := by
  rw [Real.log_pow]
  have hl : 0 < E₀ * Real.log 2 := mul_pos hE (Real.log_pos (by norm_num))
  push_cast
  nlinarith [hl]

theorem log_eight : Real.log 8 = 3 * Real.log 2 := by
  rw [show (8 : ℝ) = 2 ^ 3 by norm_num, Real.log_pow]
  norm_num

/-- **3c. The ceiling is attained exactly by a one-component closure.** -/
theorem ceiling_attained [Nonempty α] (E₀ : ℝ) (σAtom : Perm α)
    (h1 : orbitCount σAtom = 1) :
    classicalLogBinding E₀ 1 σAtom = E₀ * Real.log 2 * ((Fintype.card α : ℝ) - 1) := by
  rw [classicalLogBinding_eq, orbitCount_one, h1]
  push_cast
  ring

/-! ## Subadditivity of the Cayley length, and the sign of a product-assembled `b₃` -/

/-- One transposition changes the defect by at most one. -/
theorem orbitDefect_swap_mul_le (σ : Perm α) (a b : α) :
    orbitDefect (swap a b * σ) ≤ orbitDefect σ + 1 := by
  by_cases hab : a = b
  · subst hab; simp
  · by_cases hc : σ.SameCycle a b
    · have := orbitDefect_swap_mul_of_sameCycle hab hc; omega
    · have := orbitDefect_swap_mul_of_not_sameCycle hab hc; omega

/-- The product of the transpositions of a list of pairs. -/
def swapProd : List (α × α) → Perm α
  | [] => 1
  | p :: l => swap p.1 p.2 * swapProd l

theorem orbitDefect_swapProd_mul_le (l : List (α × α)) (σ : Perm α) :
    orbitDefect (swapProd l * σ) ≤ orbitDefect σ + l.length := by
  induction l with
  | nil => simp [swapProd]
  | cons p l ih =>
      simp only [swapProd, List.length_cons, mul_assoc]
      have := orbitDefect_swap_mul_le (swapProd l * σ) p.1 p.2
      omega

/-- Every permutation is a product of exactly `orbitDefect` transpositions. -/
theorem exists_swapProd (τ : Perm α) :
    ∃ l : List (α × α), l.length = orbitDefect τ ∧ swapProd l = τ := by
  induction hd : orbitDefect τ generalizing τ with
  | zero =>
      refine ⟨[], rfl, ?_⟩
      by_contra hne
      obtain ⟨x, hx⟩ : ∃ x, τ x ≠ x := by
        by_contra hall
        push_neg at hall
        exact hne (by ext x; simp [swapProd, hall x])
      have := orbitDefect_swap_apply_mul hx
      omega
  | succ d ih =>
      obtain ⟨x, hx⟩ : ∃ x, τ x ≠ x := by
        by_contra hall
        push_neg at hall
        have : τ = 1 := by ext x; simp [hall x]
        subst this
        rw [orbitDefect_one] at hd
        omega
      have hstep := orbitDefect_swap_apply_mul hx
      obtain ⟨l, hl, hp⟩ := ih (swap x (τ x) * τ) (by omega)
      refine ⟨(x, τ x) :: l, by simp [hl], ?_⟩
      simp only [swapProd, hp, ← mul_assoc, swap_mul_self, one_mul]

/-- **4a. The Cayley length is subadditive.** -/
theorem orbitDefect_mul_le (τ σ : Perm α) :
    orbitDefect (τ * σ) ≤ orbitDefect τ + orbitDefect σ := by
  obtain ⟨l, hl, hp⟩ := exists_swapProd τ
  have := orbitDefect_swapProd_mul_le l σ
  rw [hp] at this
  omega

/-- The classical connected three-body term: the atom's classical binding minus the three
pair bonds', each on the same strands with a classically trivial free word. -/
noncomputable def classicalB3 (E₀ : ℝ) (π₁₂₃ π₁₂ π₁₃ π₂₃ : Perm α) : ℝ :=
  classicalLogBinding E₀ 1 π₁₂₃ - classicalLogBinding E₀ 1 π₁₂
    - classicalLogBinding E₀ 1 π₁₃ - classicalLogBinding E₀ 1 π₂₃

/-- **5. Quantisation.** For any four words, the classical `b₃` is `E₀ log 2` times an integer,
the defect combination below. -/
theorem classicalB3_quantised (E₀ : ℝ) (π₁₂₃ π₁₂ π₁₃ π₂₃ : Perm α) :
    classicalB3 E₀ π₁₂₃ π₁₂ π₁₃ π₂₃
      = E₀ * Real.log 2 * (((orbitDefect π₁₂₃ : ℤ) - orbitDefect π₁₂ - orbitDefect π₁₃
          - orbitDefect π₂₃ : ℤ) : ℝ) := by
  unfold classicalB3
  simp only [classicalLogBinding_of_trivial_free]
  push_cast
  ring

/-- **4b. A product-assembled three-body atom has `b₃ ≤ 0` classically.** If the atom's
permutation is the product of the three pair-bond permutations, subadditivity forces the
merge count of the whole to be at most the sum of the parts. -/
theorem classicalB3_nonpos_of_product {E₀ : ℝ} (hE : 0 ≤ E₀) (π₁₂ π₁₃ π₂₃ : Perm α) :
    classicalB3 E₀ (π₁₂ * π₁₃ * π₂₃) π₁₂ π₁₃ π₂₃ ≤ 0 := by
  rw [classicalB3_quantised]
  have h1 := orbitDefect_mul_le (π₁₂ * π₁₃) π₂₃
  have h2 := orbitDefect_mul_le π₁₂ π₁₃
  have hint : ((orbitDefect (π₁₂ * π₁₃ * π₂₃) : ℤ) - orbitDefect π₁₂ - orbitDefect π₁₃
      - orbitDefect π₂₃ : ℤ) ≤ 0 := by omega
  have hl : 0 ≤ E₀ * Real.log 2 := mul_nonneg hE (Real.log_nonneg (by norm_num))
  have : (((orbitDefect (π₁₂ * π₁₃ * π₂₃) : ℤ) - orbitDefect π₁₂ - orbitDefect π₁₃
      - orbitDefect π₂₃ : ℤ) : ℝ) ≤ 0 := by exact_mod_cast hint
  exact mul_nonpos_of_nonneg_of_nonpos hl this

/-- **Anti-vacuity for 4b.** Subadditivity is not equality: on three points the product of
two different transpositions merges two components, the same as the sum, but the product of a
transposition with itself merges none, against a sum of two. So the bound is strict on some
inputs and tight on others. -/
example : orbitDefect (swap (0 : Fin 3) 1 * swap 0 1) = 0 ∧
    orbitDefect (swap (0 : Fin 3) 1) = 1 := by decide

example : orbitDefect (swap (0 : Fin 3) 1 * swap 1 2) = 2 := by decide

/-! ## The γγ words at `q = 1` -/

/-- The classical image of the chiral vertex `V(s) = σ_s σ_{s+1}⁻¹`: both letters specialise
to their transposition at `q = 1`. -/
def vertex {n : ℕ} (s : ℕ) (h : s + 2 < n) : Perm (Fin n) :=
  swap ⟨s, by omega⟩ ⟨s + 1, by omega⟩ * swap ⟨s + 1, by omega⟩ ⟨s + 2, by omega⟩

/-- **6a. The γγ nucleon `V³` is classically the identity** (a 3-cycle cubed). -/
theorem nucleon_V3_classically_trivial : (vertex 0 (by omega) : Perm (Fin 3)) ^ 3 = 1 := by
  decide

/-- The six-strand free deuteron: `V³ ⊗ V³`. -/
def freeDeuteron : Perm (Fin 6) := vertex 0 (by omega) ^ 3 * vertex 3 (by omega) ^ 3

theorem freeDeuteron_eq_one : freeDeuteron = 1 := by decide

/-- **6b. The selected γγ bond `V(2)³` merges no components.** -/
theorem selected_bond_merges_none :
    orbitDefect ((vertex 2 (by omega) : Perm (Fin 6)) ^ 3 * freeDeuteron) = 0 := by decide

/-- …and neither does `V(1)³`, the other selected-cheapest site. -/
theorem selected_bond_V1_merges_none :
    orbitDefect ((vertex 1 (by omega) : Perm (Fin 6)) ^ 3 * freeDeuteron) = 0 := by decide

/-- **6c. A single vertex `V(1)` (or `V(2)`) merges two components.** These are the bonds that
bind by MeV at `q₀` and fail reading 3. -/
theorem single_vertex_bond_merges_two :
    orbitDefect ((vertex 1 (by omega) : Perm (Fin 6)) * freeDeuteron) = 2 ∧
    orbitDefect ((vertex 2 (by omega) : Perm (Fin 6)) * freeDeuteron) = 2 := by decide

/-- **6e. Merges by an even permutation come in pairs.** Every vertex is a 3-cycle, so every
pure-junction bond word is an even permutation and merges an even number of components: its
classical binding is a multiple of `2 E₀ log 2`, never `E₀ log 2`. -/
theorem merges_even_of_sign_one (σ : Perm α) (h : sign σ = 1) : Even (orbitDefect σ) := by
  rw [sign_eq_neg_one_pow_orbitDefect] at h
  exact (neg_one_pow_eq_one_iff_even (by decide)).mp h

theorem vertex_sign {n : ℕ} (s : ℕ) (h : s + 2 < n) : sign (vertex s h : Perm (Fin n)) = 1 := by
  unfold vertex
  rw [map_mul, sign_swap (by simp [Fin.ext_iff]), sign_swap (by simp [Fin.ext_iff])]
  decide

/-- **6d. So the selected deuteron's classical log binding is exactly zero**: its binding at
`q₀` is entirely a `q`-deformation effect. -/
theorem selected_deuteron_classical_binding_zero (E₀ : ℝ) :
    classicalLogBinding E₀ 1 ((vertex 2 (by omega) : Perm (Fin 6)) ^ 3 * freeDeuteron) = 0 := by
  rw [classicalLogBinding_of_trivial_free, selected_bond_merges_none]
  simp

end QOU.MassTheory.ClassicalLogBindingCycleCount
