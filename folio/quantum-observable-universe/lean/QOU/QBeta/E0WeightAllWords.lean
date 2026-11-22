/-
# No braid word's convention-D trace is E₀'s weight `ℏ_q/q²`

Companion to `QOU.QBeta.E0WeightCandidates`, which rules out the six preregistered words one
by one. This file proves the statement for **every** braid word on any number of strands.

The trace is the Jimbo state sum used by the probe
`computations/probes/e0_weight/e0_weight_markov_probe.py`:

  `T_β(q) = Tr(K^{⊗n} · ρ_q(β)) / [2]^n`,   `K = diag(q, q⁻¹)`,   `[2] = q + q⁻¹`,

with the Jimbo `Ř` on a pair of strands. A strand colour `false` is the `K = q` state and `true`
is the `K = q⁻¹` state. On the two strands `(a, b)` of a letter, `Ř` acts by

* `|cc⟩ ↦ q |cc⟩`;
* `|false,true⟩ ↦ |true,false⟩`;
* `|true,false⟩ ↦ |false,true⟩ + h |true,false⟩`, with `h = q − q⁻¹`.

An inverse letter uses `Ř⁻¹ = Ř − h` (the Hecke relation `(Ř − q)(Ř + q⁻¹) = 0`).

Proved here:

* `wordMat_one`: at `q = 1` the word matrix is the permutation matrix of the word's permutation.
* `traceD_one`: `T_β(1) = trClassical(π_β) = 2^{c − n}`, where `c` is the number of cycles of the
  permutation, i.e. the number of components of the closure
  (`QOU.Braiding.ClassicalTrace`).
* `traceD_continuousAt_one`: `T_β` is continuous at `q = 1`.
* `traceD_ne_of_tendsto_zero`: hence no function tending to `0` as `q → 1⁺` equals `T_β` on
  `q > 1`.
* `traceD_ne_weight`: in particular `T_β ≠ ℏ_q/q² = (q − 1)/q³`, for every word `β`.

**Scope, stated precisely.** The theorem is about the state sum `T_β` defined below. That `T_β`
is the convention-D Markov trace (the Ocneanu trace with `z_D = q³/(q²+1)`) for every word is the
standard Jimbo–Turaev construction plus Jones' uniqueness of the Markov trace. That step is cited,
not formalised here. The probe asserts `T(σ₁) = z_D` on two strands, and the six preregistered
words were checked symbolically against their trace closed forms in `E0WeightCandidates`.

The theorem covers **single** words only. A sum or linear combination of traces, or a sum over a
tower of words, can vanish at `q = 1` and is not covered. Bean `qou-91w7`.
-/
import QOU.Braiding.MarkovTraceClassicalLimit
import Mathlib.Topology.Instances.Matrix
import Mathlib.Topology.Algebra.Order.Field
import Mathlib.Analysis.SpecificLimits.Basic

namespace QOU.QBeta.E0WeightAllWords

open Equiv Filter Topology Matrix
open QOU.Braiding.ClassicalTrace

variable {α : Type*} [Fintype α] [DecidableEq α]

/-- A colouring of the strands: one basis vector of `V^{⊗n}`, `V = ℝ²`. -/
abbrev Col (α : Type*) := α → Bool

/-- A letter of a braid word: a crossing of strands `a` and `b`, inverse if `inv`. -/
structure Letter (α : Type*) where
  a : α
  b : α
  inv : Bool

/-- `1` if `p`, else `0`. -/
def ind (p : Prop) [Decidable p] : ℝ := if p then 1 else 0

/-- Constant part of the letter matrix (row `y`, column `x`): the swap of mixed colours. -/
def e0 (l : Letter α) : Matrix (Col α) (Col α) ℝ := fun y x =>
  ind (x l.a ≠ x l.b ∧ y = x ∘ swap l.a l.b)

/-- Coefficient of `q`: the `|cc⟩ ↦ q|cc⟩` entries, the `+q` half of `h`, and `−q` from `−h`
for an inverse letter. -/
def e1 (l : Letter α) : Matrix (Col α) (Col α) ℝ := fun y x =>
  ind (x l.a = x l.b ∧ y = x) + ind (x l.a ≠ x l.b ∧ y = x ∧ x l.a = true)
    - ind (l.inv = true ∧ y = x)

/-- Coefficient of `q⁻¹`: the `−q⁻¹` half of `h`, and `+q⁻¹` from `−h` for an inverse letter. -/
def e2 (l : Letter α) : Matrix (Col α) (Col α) ℝ := fun y x =>
  -ind (x l.a ≠ x l.b ∧ y = x ∧ x l.a = true) + ind (l.inv = true ∧ y = x)

/-- The Jimbo `Ř` (or `Ř − h` for an inverse letter) on the strands of `l`. -/
noncomputable def letter (q : ℝ) (l : Letter α) : Matrix (Col α) (Col α) ℝ :=
  e0 l + q • e1 l + q⁻¹ • e2 l

/-- The word matrix `ρ_q(β) = ρ_q(l₁) ρ_q(l₂) ⋯`. -/
noncomputable def wordMat (q : ℝ) (w : List (Letter α)) : Matrix (Col α) (Col α) ℝ :=
  (w.map (letter q)).prod

/-- The `K^{⊗n}` weight of a colouring: `q` per `false` strand, `q⁻¹` per `true` strand. -/
noncomputable def kw (q : ℝ) (x : Col α) : ℝ :=
  q ^ (Finset.univ.filter fun i => x i = false).card *
    q⁻¹ ^ (Finset.univ.filter fun i => x i = true).card

/-- The state-sum trace `T_β(q) = Tr(K^{⊗n} ρ_q(β)) / [2]^n`. -/
noncomputable def traceD (q : ℝ) (w : List (Letter α)) : ℝ :=
  (∑ x, kw q x * wordMat q w x x) / (q + q⁻¹) ^ Fintype.card α

/-- The permutation matrix `P_π`, row `y`, column `x`: `1` iff `y = x ∘ π`. -/
def permMat (π : Perm α) : Matrix (Col α) (Col α) ℝ := fun y x => ind (y = x ∘ π)

/-- The permutation of a word: `π_{l :: w} = π_w * swap a b`. -/
def wordPerm : List (Letter α) → Perm α
  | [] => 1
  | l :: w => wordPerm w * swap l.a l.b

omit [Fintype α] in
theorem comp_swap_of_eq {x : Col α} {a b : α} (h : x a = x b) : x ∘ swap a b = x := by
  funext i
  simp only [Function.comp_apply, swap_apply_def]
  split_ifs with h1 h2
  · subst h1; exact h.symm
  · subst h2; exact h
  · rfl

/-- At `q = 1` a letter is the permutation matrix of its transposition. -/
theorem letter_one (l : Letter α) : letter 1 l = permMat (swap l.a l.b) := by
  ext y x
  simp only [letter, e0, e1, e2, permMat, ind, inv_one, one_smul, Matrix.add_apply]
  by_cases hab : x l.a = x l.b
  · rw [comp_swap_of_eq hab]
    by_cases hy : y = x <;> simp [hab, hy]
  · by_cases hy : y = x
    · subst hy
      have hs : y ≠ y ∘ swap l.a l.b := by
        intro h; apply hab
        have := congrFun h l.a; simp at this; exact this
      cases ha : y l.a <;> cases hb : y l.b <;> rw [ha, hb] at hab <;>
        cases hi : l.inv <;> simp_all
    · by_cases hs : y = x ∘ swap l.a l.b
      · simp [hab, hs]; ring
      · simp [hab, hy, hs]

theorem permMat_mul (π ρ : Perm α) : permMat π * permMat ρ = permMat (ρ * π) := by
  ext y x
  simp only [Matrix.mul_apply, permMat, ind, mul_ite, mul_one, mul_zero]
  rw [Finset.sum_eq_single (x ∘ ρ)]
  · simp only [if_true]
    congr 1
  · intro m _ hm; simp [hm]
  · intro h; exact absurd (Finset.mem_univ _) h

omit [DecidableEq α] in
theorem permMat_one : permMat (1 : Perm α) = 1 := by
  ext y x
  simp [permMat, ind, Matrix.one_apply]

/-- **At `q = 1` the word matrix is the permutation matrix of the word.** -/
theorem wordMat_one (w : List (Letter α)) : wordMat 1 w = permMat (wordPerm w) := by
  induction w with
  | nil => simp [wordMat, wordPerm, permMat_one]
  | cons l w ih =>
    simp only [wordMat, List.map_cons, List.prod_cons] at ih ⊢
    rw [ih, letter_one, permMat_mul, wordPerm]

omit [DecidableEq α] in
theorem kw_one (x : Col α) : kw 1 x = 1 := by simp [kw]

/-- The trace of a permutation matrix counts the colourings it fixes: the states. -/
theorem sum_permMat_diag (π : Perm α) :
    ∑ x, permMat π x x = (Fintype.card (States π) : ℝ) := by
  simp only [permMat, ind]
  rw [Finset.sum_boole, Fintype.card_subtype]
  congr 2
  ext x
  simp only [Finset.mem_filter, Finset.mem_univ, true_and]
  constructor
  · intro h i; exact (congrFun h i).symm
  · intro h; funext i; exact (h i).symm

/-- **At `q = 1` the state sum is the classical trace `2^{c−n}` of the word's permutation.** -/
theorem traceD_one (w : List (Letter α)) :
    traceD 1 w = (trClassical (wordPerm w) : ℝ) := by
  unfold traceD trClassical
  simp only [kw_one, one_mul, wordMat_one, sum_permMat_diag, inv_one]
  push_cast
  norm_num

theorem trClassical_pos (π : Perm α) : 0 < trClassical π := by
  unfold trClassical
  have : 0 < Fintype.card (States π) :=
    Fintype.card_pos_iff.2 ⟨⟨fun _ => false, fun _ => rfl⟩⟩
  positivity

theorem letter_continuousAt (l : Letter α) : ContinuousAt (fun q : ℝ => letter q l) 1 := by
  unfold letter
  have hinv : ContinuousAt (fun q : ℝ => q⁻¹) 1 := continuousAt_inv₀ one_ne_zero
  exact (continuousAt_const.add (continuousAt_id.smul continuousAt_const)).add
    (hinv.smul continuousAt_const)

theorem wordMat_continuousAt (w : List (Letter α)) :
    ContinuousAt (fun q : ℝ => wordMat q w) 1 := by
  induction w with
  | nil => simp only [wordMat, List.map_nil, List.prod_nil]; exact continuousAt_const
  | cons l w ih =>
    simp only [wordMat, List.map_cons, List.prod_cons] at ih ⊢
    exact (letter_continuousAt l).mul ih

omit [DecidableEq α] in
theorem kw_continuousAt (x : Col α) : ContinuousAt (fun q : ℝ => kw q x) 1 := by
  unfold kw
  exact (continuousAt_id.pow _).mul ((continuousAt_inv₀ one_ne_zero).pow _)

/-- **`T_β` is continuous at `q = 1`.** -/
theorem traceD_continuousAt_one (w : List (Letter α)) :
    ContinuousAt (fun q : ℝ => traceD q w) 1 := by
  unfold traceD
  have hM := wordMat_continuousAt w
  have hnum : ContinuousAt (fun q : ℝ => ∑ x, kw q x * wordMat q w x x) 1 := by
    exact tendsto_finset_sum _ fun x _ =>
      (kw_continuousAt x).mul (continuousAt_pi.1 (continuousAt_pi.1 hM x) x)
  have hden : ContinuousAt (fun q : ℝ => (q + q⁻¹) ^ Fintype.card α) 1 :=
    (continuousAt_id.add (continuousAt_inv₀ one_ne_zero)).pow _
  exact hnum.div hden (by norm_num)

/-- **No function vanishing as `q → 1⁺` is the trace of a braid word on `q > 1`.** -/
theorem traceD_ne_of_tendsto_zero (w : List (Letter α)) (f : ℝ → ℝ)
    (hf : Tendsto f (𝓝[>] 1) (𝓝 0)) : ¬ ∀ q : ℝ, 1 < q → traceD q w = f q := by
  intro h
  have hT : Tendsto (fun q => traceD q w) (𝓝[>] 1) (𝓝 (traceD 1 w)) :=
    (traceD_continuousAt_one w).tendsto.mono_left nhdsWithin_le_nhds
  have heq : (fun q => traceD q w) =ᶠ[𝓝[>] 1] f :=
    eventually_nhdsWithin_of_forall fun q hq => h q hq
  have h0 : traceD 1 w = 0 := tendsto_nhds_unique (hT.congr' heq) hf
  rw [traceD_one] at h0
  have := trClassical_pos (wordPerm w)
  exact absurd h0 (by exact_mod_cast this.ne')

/-- E₀'s weight `w(q) = ℏ_q/q² = (q − 1)/q³`. -/
noncomputable def weight (q : ℝ) : ℝ := (q - 1) / q ^ 3

theorem weight_tendsto : Tendsto weight (𝓝[>] 1) (𝓝 0) := by
  have : ContinuousAt weight 1 := by
    unfold weight
    exact (continuousAt_id.sub continuousAt_const).div (continuousAt_id.pow 3) (by norm_num)
  have h := this.tendsto.mono_left (nhdsWithin_le_nhds (s := Set.Ioi (1 : ℝ)))
  simpa [weight] using h

/-- **No braid word, on any number of strands, has `ℏ_q/q²` as its convention-D trace.** -/
theorem traceD_ne_weight (w : List (Letter α)) :
    ¬ ∀ q : ℝ, 1 < q → traceD q w = weight q :=
  traceD_ne_of_tendsto_zero w weight weight_tendsto

/-! ### Tower-level objects (prereg Addendum 1)

The invariant is the order of vanishing at `q = 1`. `w` has order exactly `1`
(`w/(q − 1) → 1`). The lemmas below exclude objects of order `0` (a non-zero limit) and of
order `≥ 2` (`ℏ_q²` times anything finite at `1`). They also give the first-order coefficient of
the skein difference `h · T_β`, the one canonical tower operation of order `1`.
-/

/-- `ℏ_q = 1 − q⁻¹`. -/
noncomputable def hbar (q : ℝ) : ℝ := 1 - q⁻¹

/-- **Order 0.** No function with a non-zero limit at `q → 1⁺` is `w` on `q > 1`. This covers
the Markov stabilisation tower `z_Dⁿ`, `z_D/(1 − z_D)` and the levels and partial sums of
`Σ_{k ≥ 2} q⁻ᵏ` (prereg T2, T3). -/
theorem ne_weight_of_tendsto_ne_zero (f : ℝ → ℝ) (c : ℝ) (hc : c ≠ 0)
    (hf : Tendsto f (𝓝[>] 1) (𝓝 c)) : ¬ ∀ q : ℝ, 1 < q → f q = weight q := by
  intro h
  have heq : f =ᶠ[𝓝[>] 1] weight := eventually_nhdsWithin_of_forall fun q hq => h q hq
  exact hc (tendsto_nhds_unique (hf.congr' heq) weight_tendsto)

/-- **Order ≥ 2.** `ℏ_q² · g` is never `w` on `q > 1` when `g` is continuous at `1`. This covers
every brane-tower level `(ℏ_q²λ)ⁿ`, its sum `ℏ_q²λ/(1 − ℏ_q²λ)` and the implemented correction
`1/(1 − ℏ_q²) − 1`, whenever `λ` is finite at `q = 1` (prereg T1). -/
theorem hbar_sq_mul_ne_weight (g : ℝ → ℝ) (hg : ContinuousAt g 1) :
    ¬ ∀ q : ℝ, 1 < q → hbar q ^ 2 * g q = weight q := by
  intro h
  have h1 : Tendsto (fun q : ℝ => 1 / q ^ 3) (𝓝[>] 1) (𝓝 1) := by
    have : ContinuousAt (fun q : ℝ => 1 / q ^ 3) 1 :=
      continuousAt_const.div (continuousAt_id.pow 3) (by norm_num)
    simpa using this.tendsto.mono_left (nhdsWithin_le_nhds (s := Set.Ioi (1 : ℝ)))
  have h2 : Tendsto (fun q : ℝ => (q - 1) * g q / q ^ 2) (𝓝[>] 1) (𝓝 0) := by
    have : ContinuousAt (fun q : ℝ => (q - 1) * g q / q ^ 2) 1 :=
      ((continuousAt_id.sub continuousAt_const).mul hg).div (continuousAt_id.pow 2)
        (by norm_num)
    simpa using this.tendsto.mono_left (nhdsWithin_le_nhds (s := Set.Ioi (1 : ℝ)))
  have heq : (fun q : ℝ => (q - 1) * g q / q ^ 2) =ᶠ[𝓝[>] 1] (fun q : ℝ => 1 / q ^ 3) := by
    refine eventually_nhdsWithin_of_forall fun q (hq : 1 < q) => ?_
    have e := h q hq
    have hq0 : q ≠ 0 := by positivity
    have hq1 : q - 1 ≠ 0 := sub_ne_zero.2 (ne_of_gt hq)
    unfold hbar weight at e
    field_simp at e ⊢
    linear_combination e
  exact one_ne_zero (tendsto_nhds_unique (h2.congr' heq) h1).symm

/-- **Order 1, the skein difference.** `h · T_β`, `h = q − q⁻¹ = τ(βσ) − τ(βσ⁻¹)`, vanishes to
first order at `q = 1` with coefficient `2 · trClassical(π_β) = 2^{c − n + 1}`. It matches `w`'s
first-order coefficient `1` exactly when `c = n − 1` (prereg T4). Exact equality would force
`T_β = w/h = 1/(q²(q + 1))`, which has a pole at `q = −1` while every word trace is finite there.
That last step is a rational-function argument recorded in the audit, not formalised here. -/
theorem skein_first_order (w : List (Letter α)) :
    Tendsto (fun q : ℝ => (q - q⁻¹) * traceD q w / (q - 1)) (𝓝[>] 1)
      (𝓝 (2 * (trClassical (wordPerm w) : ℝ))) := by
  have hc : ContinuousAt (fun q : ℝ => (q + 1) / q * traceD q w) 1 :=
    ((continuousAt_id.add continuousAt_const).div continuousAt_id (by norm_num)).mul
      (traceD_continuousAt_one w)
  have ht := hc.tendsto.mono_left (nhdsWithin_le_nhds (s := Set.Ioi (1 : ℝ)))
  rw [traceD_one] at ht
  norm_num at ht
  refine ht.congr' (eventually_nhdsWithin_of_forall fun q (hq : 1 < q) => ?_)
  have hq0 : q ≠ 0 := by positivity
  have hq1 : q - 1 ≠ 0 := sub_ne_zero.2 (ne_of_gt hq)
  field_simp
  ring

end QOU.QBeta.E0WeightAllWords
