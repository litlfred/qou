import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Data.Matrix.Basis
import Mathlib.Algebra.BigOperators.Pi
import Mathlib.Tactic
import QOU.SchurWeyl.OcneanuWeightWenzl

/-!
# Term 4 on the surviving blocks: the co-Casimir on the radical quotient

## The problem this file settles

Term 4 of the mass formula (the "Frobenius co-Casimir",
`prop:frobenius-codim-universal`) is

  `τ(C)`,   `C = Σ_λ p_λ / (dim_q(λ) · τ(p_λ))`,

over the central idempotents `p_λ` of a semisimple algebra `A` carrying a trace `τ`.
`frobenius_codim_universal` proves `τ(C) = Σ_λ 1/dim_q(λ)` **under the class hypothesis
`τ(p_λ) ≠ 0` for every block**.

Under convention D (Markov parameter `z_D = q³/(q²+1)`) that hypothesis is **false**:
`SchurWeyl.ocneanuWeight_conventionD_eq_zero_iff` proves `τ(p_λ) = 0` exactly for the
partitions with three or more rows. So `C` has a zero denominator on every such block and
is undefined. Production nevertheless sums `1/dim_q` over **all** `λ ⊢ 3A`.

## What is proved here (all algebraic, generic field, sorry-free)

The model of `A` is a finite product of matrix blocks `A = Π_λ Mat_{d_λ}(K)` with the
trace `τ(a) = Σ_λ w_λ · Tr(a_λ)` (`w_λ` the block weights). This is the Wedderburn form of
`H_n(q)` at generic `q`; the weights at convention D are `ocneanuWeight q z_D`.

1. `mem_traceRadical_iff` — the radical of the trace form `(a, b) ↦ τ(ab)` is **exactly**
   the sum of the blocks with `w_λ = 0`. So `A/rad τ` is the product of the *surviving*
   blocks, and `τ` descends to a nondegenerate trace on it.
2. `no_full_coCasimir` — if some block dies, **no** central element `c` has
   `τ(c · p_λ) = 1/dim_q(λ)` on every block. The formal sum over all `λ` is not the trace
   of any element of `A`; it cannot be repaired by choosing `C` more cleverly.
3. `coCasimirSurv` (the definition `C°`) and `tr_coCasimirSurv` —
   `C° := Σ_{τ(p_λ) ≠ 0} p_λ / (dim_q(λ) · τ(p_λ))` is central and
   `τ(C°) = Σ_{λ : τ(p_λ) ≠ 0} 1/dim_q(λ)`.
4. `tr_eq_of_sub_mem_radical` — **well-definedness on the quotient**: every lift `x` of the
   class of `C°` in `A/rad τ` has the same trace. So `τ̄(C̄°)` is an invariant of the
   quotient object, not of the representative.
5. `coCasimirSurv_unique_mod_radical` — `C°` is characterised, modulo the radical, by the
   co-Casimir property on surviving blocks; the dead-block coefficients are not data.
6. `tr_coCasimirSurv_of_forall_ne_zero` — when no block dies this is the old identity, so
   the definition extends `frobenius_codim_universal` rather than replacing it.
7. `conventionD_support_iff` / `tr_coCasimirSurv_conventionD` — at convention D the
   surviving blocks are exactly the partitions with at most two rows (the Temperley–Lieb
   quotient), so `τ̄(C̄°) = Σ_{λ ⊢ n, ℓ(λ) ≤ 2} 1/dim_q(λ)`, for every `n`.
8. `tr_coCasimirSurv_n3` — at `n = 3`: `1 + 1/[2]_q`, against production's `2 + 1/[2]_q`.

Nothing here touches production compute. Which sum the mass formula should use is the
owner's ruling on the radical quotient; this file only makes the surviving-block sum a
theorem and shows the all-`λ` sum is not a trace.

## What is cited, not proved

* That `H_n(q)` at generic `q` is the product of matrix blocks indexed by partitions, with
  the Markov trace given by block weights (Wedderburn + Ocneanu). The corpus carries this as
  the seminormal-basis input (Ram Thm 4.1), listed as an open assumption of the mass
  pipeline. Statement 7 needs only the weights, which are proved in
  `SchurWeyl.OcneanuWeightWenzl`.
* `dim_q` is taken as given block data (the production hook formula). The theorems need
  only `dim_q(λ) ≠ 0` on surviving blocks.

## Base ring

Generic `[Field K]` throughout (AGENTS.md §7c). No ordering, no `ℝ`. The convention-D
specialisation needs `q` not a root of unity, exactly the hypothesis of the corpus theorem
it uses.

-- Ref: [leitner2026] folio/quantum-observable-universe/mass-theory/frobenius-codim-universal.md
-- Ref: [leitner2026] QOU.SchurWeyl.ocneanuWeight_conventionD_eq_zero_iff
-- Ref: [wenzl1988] Wenzl, "Hecke algebras of type A_n and subfactors",
--       Invent. Math. 92 (1988) 349–383.
-/

namespace QOU.MassTheory.CoCasimirSurviving

open Finset Matrix Classical

noncomputable section

set_option linter.unusedSectionVars false

variable {K : Type*} [Field K] {Λ : Type*} [Fintype Λ] [DecidableEq Λ]

/-- The Wedderburn model `Π_λ Mat_{d_λ}(K)` of a split semisimple algebra. -/
abbrev Blocks (K : Type*) {Λ : Type*} (d : Λ → ℕ) :=
  (μ : Λ) → Matrix (Fin (d μ)) (Fin (d μ)) K

variable {d : Λ → ℕ}

/-- The trace with block weights `w`: `τ(a) = Σ_λ w_λ · Tr(a_λ)`. -/
def tr (w : Λ → K) (a : Blocks K d) : K := ∑ μ, w μ * (a μ).trace

/-- The central idempotent of block `λ`. -/
def blockIdem (μ : Λ) : Blocks K d := Pi.single μ 1

/-- Membership in the radical of the trace form, stated block-wise: zero on every
surviving block. `mem_traceRadical_iff` proves this is the radical. -/
def InRadical (w : Λ → K) (a : Blocks K d) : Prop := ∀ μ, w μ ≠ 0 → a μ = 0

/-- `τ(p_λ) = w_λ · d_λ`. -/
theorem tr_blockIdem (w : Λ → K) (μ : Λ) :
    tr w (blockIdem μ : Blocks K d) = w μ * (d μ : K) := by
  unfold tr blockIdem
  rw [Finset.sum_eq_single μ]
  · simp [Matrix.trace_one]
  · intro ν _ hν
    simp [hν]
  · intro h; exact absurd (Finset.mem_univ μ) h

/-- **The radical of the trace form is the sum of the dead blocks.**

`(∀ b, τ(ab) = 0) ↔ a vanishes on every block with w_λ ≠ 0.`

The forward direction tests against matrix units: `τ(a · E^{(λ)}_{ji}) = w_λ · a_λ(i,j)`. -/
theorem mem_traceRadical_iff (w : Λ → K) (a : Blocks K d) :
    (∀ b : Blocks K d, tr w (a * b) = 0) ↔ InRadical w a := by
  constructor
  · intro h μ hw
    ext i j
    have key := h (Pi.single μ (Matrix.single j i 1))
    unfold tr at key
    rw [Finset.sum_eq_single μ] at key
    · simp only [Pi.mul_apply, Pi.single_eq_same] at key
      rw [Matrix.trace_mul_single, MulOpposite.op_one, one_smul] at key
      rcases mul_eq_zero.mp key with h1 | h1
      · exact absurd h1 hw
      · simpa using h1
    · intro ν _ hν
      simp [Pi.mul_apply, hν]
    · intro hμ; exact absurd (Finset.mem_univ μ) hμ
  · intro h b
    unfold tr
    refine Finset.sum_eq_zero fun μ _ => ?_
    by_cases hw : w μ = 0
    · simp [hw]
    · simp [Pi.mul_apply, h μ hw]

/-- The trace vanishes on the radical. -/
theorem tr_eq_zero_of_inRadical (w : Λ → K) {a : Blocks K d} (ha : InRadical w a) :
    tr w a = 0 := by
  have := (mem_traceRadical_iff w a).mpr ha 1
  simpa using this

/-- The radical is closed under subtraction (it is an ideal; this is all we need). -/
theorem inRadical_sub {w : Λ → K} {a b : Blocks K d}
    (ha : InRadical w a) (hb : InRadical w b) : InRadical w (a - b) := by
  intro μ hw
  simp [ha μ hw, hb μ hw]

/-- `τ` is additive. -/
theorem tr_add (w : Λ → K) (a b : Blocks K d) : tr w (a + b) = tr w a + tr w b := by
  unfold tr
  rw [← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun μ _ => ?_
  simp [Matrix.trace_add, mul_add]

/-- **`τ` factors through `A / rad τ`.** -/
theorem tr_eq_of_sub_mem_radical (w : Λ → K) {x y : Blocks K d}
    (h : InRadical w (x - y)) : tr w x = tr w y := by
  have h0 := tr_eq_zero_of_inRadical w h
  have : x = (x - y) + y := by abel
  rw [this, tr_add, h0, zero_add]

/-! ## The co-Casimir on the surviving blocks -/

/-- The surviving blocks: `τ(p_λ) ≠ 0`, i.e. `w_λ ≠ 0` (given `d_λ ≠ 0` in `K`). -/
def support (w : Λ → K) : Finset Λ := Finset.univ.filter (fun μ => w μ ≠ 0)

/-- Block coefficient of `C°`: `1/(dim_q(λ)·τ(p_λ))` on a surviving block, `0` on a dead one. -/
def coeff (w dq : Λ → K) (d : Λ → ℕ) (μ : Λ) : K :=
  if w μ = 0 then 0 else 1 / (dq μ * (w μ * (d μ : K)))

/-- **`C°`, the co-Casimir on the surviving blocks.**
`C° = Σ_{τ(p_λ) ≠ 0} p_λ / (dim_q(λ) · τ(p_λ))`. -/
def coCasimirSurv (w dq : Λ → K) : Blocks K d := fun μ => coeff w dq d μ • (1 : Matrix _ _ K)

/-- `C°` is central: it is a scalar on every block. -/
theorem coCasimirSurv_central (w dq : Λ → K) (b : Blocks K d) :
    coCasimirSurv w dq * b = b * coCasimirSurv w dq := by
  funext μ
  simp [coCasimirSurv, Pi.mul_apply]

/-- **`τ(C°) = Σ_{λ surviving} 1/dim_q(λ)`.** Needs `d_λ ≠ 0` in `K` and `dim_q(λ) ≠ 0`
on surviving blocks only; nothing is assumed about dead blocks. -/
theorem tr_coCasimirSurv (w dq : Λ → K) (hd : ∀ μ, (d μ : K) ≠ 0)
    (hdq : ∀ μ, w μ ≠ 0 → dq μ ≠ 0) :
    tr w (coCasimirSurv w dq : Blocks K d) = ∑ μ ∈ support w, 1 / dq μ := by
  unfold tr support
  rw [Finset.sum_filter]
  refine Finset.sum_congr rfl fun μ _ => ?_
  simp only [coCasimirSurv, Matrix.trace_smul, Matrix.trace_one, smul_eq_mul, coeff,
    Fintype.card_fin]
  by_cases hw : w μ = 0
  · simp [hw]
  · simp only [hw, if_false, ne_eq, not_false_eq_true, if_true]
    have h1 := hd μ
    have h2 := hdq μ hw
    field_simp

/-- **Well-defined on the quotient.** Any `x` with `x ≡ C° (mod rad τ)` has
`τ(x) = Σ_{surviving} 1/dim_q`. -/
theorem tr_of_lift (w dq : Λ → K) (hd : ∀ μ, (d μ : K) ≠ 0)
    (hdq : ∀ μ, w μ ≠ 0 → dq μ ≠ 0) {x : Blocks K d}
    (hx : InRadical w (x - coCasimirSurv w dq)) :
    tr w x = ∑ μ ∈ support w, 1 / dq μ := by
  rw [tr_eq_of_sub_mem_radical w hx, tr_coCasimirSurv w dq hd hdq]

/-- **Characterisation mod the radical.** A central element `Σ c_λ p_λ` agrees with `C°`
modulo `rad τ` iff it has the co-Casimir property `τ(c · p_λ) = 1/dim_q(λ)` on every
surviving block. The coefficients on dead blocks are free, i.e. they are not data. -/
theorem coCasimirSurv_unique_mod_radical (w dq : Λ → K) (hd : ∀ μ, (d μ : K) ≠ 0)
    (hdq : ∀ μ, w μ ≠ 0 → dq μ ≠ 0) (c : Λ → K) :
    InRadical w ((fun μ => c μ • (1 : Matrix (Fin (d μ)) (Fin (d μ)) K)) - coCasimirSurv w dq)
      ↔ ∀ μ, w μ ≠ 0 → c μ * (w μ * (d μ : K)) = 1 / dq μ := by
  constructor
  · intro h μ hw
    have hμ := congrFun (congrFun (h μ hw) ⟨0, Nat.pos_of_ne_zero
      (fun h0 => hd μ (by simp [h0]))⟩) ⟨0, Nat.pos_of_ne_zero (fun h0 => hd μ (by simp [h0]))⟩
    simp only [Pi.sub_apply, coCasimirSurv, coeff, hw, if_false, Matrix.sub_apply,
      Matrix.smul_apply, Matrix.one_apply_eq, smul_eq_mul, mul_one, Matrix.zero_apply,
      sub_eq_zero] at hμ
    rw [hμ]
    have h1 := hd μ
    have h2 := hdq μ hw
    field_simp
  · intro h μ hw
    have hc := h μ hw
    have h1 := hd μ
    have h2 := hdq μ hw
    have : c μ = 1 / (dq μ * (w μ * (d μ : K))) := by
      field_simp
      field_simp at hc
      linear_combination hc
    simp [coCasimirSurv, coeff, hw, this]

/-- **The formal sum is not a trace.** If some block dies, no central element `c` has
`τ(c · p_λ) = 1/dim_q(λ)` on *every* block. So `Σ_{all λ} 1/dim_q(λ)` is not `τ` of any
co-Casimir, however chosen. -/
theorem no_full_coCasimir (w dq : Λ → K) (hdq : ∀ μ, dq μ ≠ 0) (hdead : ∃ μ, w μ = 0) :
    ¬ ∃ c : Λ → K, ∀ μ, c μ * (w μ * (d μ : K)) = 1 / dq μ := by
  rintro ⟨c, hc⟩
  obtain ⟨μ, hμ⟩ := hdead
  have := hc μ
  rw [hμ, zero_mul, mul_zero] at this
  exact one_div_ne_zero (hdq μ) this.symm

/-- **Consistency with `frobenius_codim_universal`.** When no block dies, `C°` is the old
`C` and its trace is the old sum over all blocks. -/
theorem tr_coCasimirSurv_of_forall_ne_zero (w dq : Λ → K) (hd : ∀ μ, (d μ : K) ≠ 0)
    (hw : ∀ μ, w μ ≠ 0) (hdq : ∀ μ, dq μ ≠ 0) :
    tr w (coCasimirSurv w dq : Blocks K d) = ∑ μ, 1 / dq μ := by
  rw [tr_coCasimirSurv w dq hd (fun μ _ => hdq μ)]
  unfold support
  rw [Finset.filter_true_of_mem (fun μ _ => hw μ)]

/-- The production sum minus the surviving sum is the sum over the dead blocks. -/
theorem sum_all_sub_sum_support (w dq : Λ → K) :
    ∑ μ, 1 / dq μ - ∑ μ ∈ support w, 1 / dq μ
      = ∑ μ ∈ Finset.univ.filter (fun μ => w μ = 0), 1 / dq μ := by
  unfold support
  rw [sub_eq_iff_eq_add, add_comm]
  have := Finset.sum_filter_add_sum_filter_not Finset.univ (fun μ => w μ = 0) (fun μ => 1 / dq μ)
  rw [← this, add_comm]

/-! ## Convention D: the surviving blocks are the two-row partitions -/

section ConventionD

open QOU.SchurWeyl

/-- At `z_D = q³/(q²+1)` and generic `q`, a block survives iff `λ` has at most two rows. -/
theorem conventionD_support_iff (q : K) (hq : q ≠ 0) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ k : ℤ, k ≠ 0 → (q ^ 2 : K) ^ k ≠ 1) (μ : YoungDiagram) :
    ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) μ ≠ 0 ↔ μ.colLen 0 ≤ 2 := by
  rw [Ne, ocneanuWeight_conventionD_eq_zero_iff q hq hq21 hgen μ]
  omega

/-- **Term 4 at convention D, every `n`.** For any finite family `P` of Young diagrams
(e.g. all partitions of `3A`), with the convention-D weights,
`τ(C°) = Σ_{λ ∈ P, ℓ(λ) ≤ 2} 1/dim_q(λ)`. -/
theorem tr_coCasimirSurv_conventionD (q : K) (hq : q ≠ 0) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ k : ℤ, k ≠ 0 → (q ^ 2 : K) ^ k ≠ 1)
    (P : Finset YoungDiagram) (d : P → ℕ) (dq : P → K)
    (hd : ∀ μ, (d μ : K) ≠ 0) (hdq : ∀ μ : P, (μ : YoungDiagram).colLen 0 ≤ 2 → dq μ ≠ 0) :
    tr (fun μ : P => ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) (μ : YoungDiagram))
        (coCasimirSurv (d := d) (fun μ : P => ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) μ) dq)
      = ∑ μ ∈ Finset.univ.filter (fun μ : P => (μ : YoungDiagram).colLen 0 ≤ 2), 1 / dq μ := by
  rw [tr_coCasimirSurv _ dq hd
    (fun μ hw => hdq μ ((conventionD_support_iff q hq hq21 hgen μ).mp hw))]
  unfold support
  congr 1
  ext μ
  simp [conventionD_support_iff q hq hq21 hgen]

end ConventionD

/-! ## `n = 3`

Blocks `(3), (2,1), (1³)` with `dim_q = 1, [2]_q, 1`. Convention D kills `(1³)` and keeps
the other two (`WenzlWeight.discriminates_at_n_three`). -/

/-- **Term 4 at `n = 3` on the surviving blocks: `1 + 1/[2]_q`.** Production carries
`2 + 1/[2]_q`; the difference is exactly the dead block `(1³)`, whose `1/dim_q` is `1`. -/
theorem tr_coCasimirSurv_n3 (q : K) (w : Fin 3 → K) (d : Fin 3 → ℕ)
    (hd : ∀ μ, (d μ : K) ≠ 0) (hq : q + q⁻¹ ≠ 0)
    (h0 : w 0 ≠ 0) (h1 : w 1 ≠ 0) (h2 : w 2 = 0) :
    tr w (coCasimirSurv (d := d) w ![1, q + q⁻¹, 1]) = 1 + 1 / (q + q⁻¹) := by
  rw [tr_coCasimirSurv w _ hd (by
    intro μ _; fin_cases μ <;> simp [hq])]
  have : support w = {0, 1} := by
    ext μ; fin_cases μ <;> simp [support, h0, h1, h2]
  rw [this]
  simp

end

end QOU.MassTheory.CoCasimirSurviving
