/-
Copyright (c) 2026 litlfred. All rights reserved.

# The `(|u|+|v|)` weight is bounded below by 1, so it transfers Poincaré for free

Gap `qou-k5r5`, epic `qou-x631`. Formalize-first (AGENTS.md §"Formalize-first probe
discipline"): the structural claim is proved here before any wide numerical search.

## The problem this addresses

`M₁ = Cov_Planch(Σ□h, ω₃) > 0` is reduced (Fulman exchangeable pair) to edge sums over the
Plancherel up-down chain against the measure

    dμ(λ, λ*) = π(λ) · J(λ, λ*) · (|u| + |v|)

where `u` is the content of the removed cell and `v` the content of the added cell. Both
surviving routes (`M₁ > 0` directly, and the Cauchy-Schwarz relaxation `Q < P`) want control
of `Σ dμ (Δf)²`, i.e. a **Poincaré inequality for this weighted Dirichlet form**. The corpus
has a Dirichlet-form treatment of the *unweighted* conductance and nothing for the weighted
one (measured: zero hits for Poincaré / log-Sobolev / conductance across `docs/`,
`computations/`, `.beans/`, `content/`).

The obstacle everyone expects is that `(|u| + |v|)` might **vanish**, degenerating the form.
It cannot, and that is the content of this file.

## The combinatorial core

`|u| + |v| = 0` forces `u = v = 0`: the removed and added cells would both sit on the main
diagonal. That requires one diagonal to carry **both** a removable and an addable corner,
and `no_removable_addable_same_diagonal` proves no partition does.

The proof is three cases on the two row indices, using only that row lengths are antitone:

* same row — `lam i = i + c + 1` and `lam i = i + c` contradict outright;
* removable above addable — antitone forces the addable row to be the very next one, whose
  length the removable condition caps at `i + c`, against its own value `i + 1 + c`;
* removable below addable — antitone forces the opposite order, contradicting the case.

No Durfee square, no hook lengths, no `Nat` subtraction: contents are carried in `ℤ`.

## What transfers, and it is free

With `1 ≤ w e` on every edge, `weighted_ge_unweighted` gives `Σ w e (Δf e)² ≥ Σ (Δf e)²`, so
`poincare_transfer` carries **any** Poincaré inequality for the unweighted up-down chain to
the weighted form **with the same constant** — no loss, no extra hypothesis.

## 🛑 SCOPE — what this does NOT do, and it is the load-bearing half

A Poincaré inequality lower-bounds a **quadratic** form `E(f, f)`. `M₁ = E(A, Σh)` is
**bilinear**, and the live sufficient condition `Q < P` needs

* a LOWER bound on `P = E(A)` — which this supplies, and
* an UPPER bound on `Q = E(D)` — which it does **not**.

Poincaré bounds both `P` and `Q` from *below*. So this removes the degeneracy worry and
makes the weighted form a legitimate Dirichlet form, and it **does not close the gap**. The
measured `P/Q ≈ 2.24` is a structural fact about the joint law of `(g, Δm)`, not something a
one-sided bound reaches. `qou-k5r5` stays OPEN.

Nor does this file supply the unweighted gap itself: `poincare_transfer` takes it as a
hypothesis, because the corpus does not have it either (the recorded eigenvalues `τ₁ = 2/n`,
`τ₃ = 3/n` are for named eigenfunctions, not a spectral gap over all of `L²`).

§7c: the transfer half is generic — `[Field R] [LinearOrder R] [IsStrictOrderedRing R]`, no
`ℝ` — and the combinatorial core is pure `ℤ`/`ℕ` arithmetic with no archimedean construct.
(`LinearOrderedField` is deprecated in this Mathlib and is no longer a class; the three-way
binder is its replacement, not a weakening.)

-- Ref: [leitner2026] .beans/qou-k5r5, docs/audits/2026-07-24-covariance-kernel-route1-exchangeable-pair.md
-/

import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic

namespace QOU.MassTheory.WeightedDirichletPoincare

open Finset

/-! ### The combinatorial core: no diagonal carries both a removable and an addable corner -/

/-- A partition is carried by its antitone row-length function `lam : ℕ → ℕ`. -/
def Antitone' (lam : ℕ → ℕ) : Prop := ∀ i, lam (i + 1) ≤ lam i

/-- `lam` is antitone as a function of the row index (the weakly-decreasing condition,
iterated). -/
theorem antitone_of_step {lam : ℕ → ℕ} (h : Antitone' lam) {i j : ℕ} (hij : i ≤ j) :
    lam j ≤ lam i := by
  induction j with
  | zero => simp [Nat.le_zero.mp hij]
  | succ k ih =>
    rcases Nat.lt_or_ge i (k + 1) with hlt | hge
    · exact le_trans (h k) (ih (Nat.lt_succ_iff.mp hlt))
    · simp [Nat.le_antisymm hge hij]

/-- **Removable corner on diagonal `c`, at row `i`.**

The cell `(i, lam i - 1)` is the last of its row and nothing sits below it in that column;
its content is `c`, which in `ℤ` reads `lam i = i + c + 1`. -/
def Removable (lam : ℕ → ℕ) (i : ℕ) (c : ℤ) : Prop :=
  (lam i : ℤ) = (i : ℤ) + c + 1 ∧ (lam (i + 1) : ℤ) ≤ (i : ℤ) + c

/-- **Addable corner on diagonal `c`, at row `i`.**

A new cell may be placed at `(i, lam i)`; its content is `c`, i.e. `lam i = i + c`. -/
def Addable (lam : ℕ → ℕ) (i : ℕ) (c : ℤ) : Prop :=
  (lam i : ℤ) = (i : ℤ) + c

/-- **THE COMBINATORIAL CORE.** No partition has a removable corner and an addable corner on
the **same diagonal**.

This is what stops the edge weight `(|u| + |v|)` from vanishing: `|u| + |v| = 0` would put
both the removed and the added cell on the diagonal `c = 0`, which this forbids. -/
theorem no_removable_addable_same_diagonal {lam : ℕ → ℕ} (hmono : Antitone' lam)
    {i i' : ℕ} {c : ℤ} (hr : Removable lam i c) (ha : Addable lam i' c) : False := by
  obtain ⟨hri, hrb⟩ := hr
  rcases lt_trichotomy i i' with hlt | heq | hgt
  · -- removable strictly above addable: antitone pins `i' = i + 1`, then the two
    -- conditions on row `i + 1` disagree by exactly 1.
    have hle : lam i' ≤ lam i := antitone_of_step hmono (le_of_lt hlt)
    have hleZ : ((lam i' : ℤ)) ≤ (lam i : ℤ) := by exact_mod_cast hle
    rw [ha, hri] at hleZ
    have hi' : i' = i + 1 := by omega
    subst hi'
    rw [ha] at hrb
    omega
  · subst heq; rw [ha] at hri; omega
  · -- removable strictly below addable: antitone forces the reverse order.
    have hle : lam i ≤ lam i' := antitone_of_step hmono (le_of_lt hgt)
    have hleZ : ((lam i : ℤ)) ≤ (lam i' : ℤ) := by exact_mod_cast hle
    rw [ha, hri] at hleZ
    omega

/-- **The edge weight is at least 1.** Two distinct integer contents cannot both be zero, so
`1 ≤ |u| + |v|`. Combined with `no_removable_addable_same_diagonal`, which is what rules out
`u = v = 0` on an actual up-down edge. -/
theorem one_le_weight {u v : ℤ} (h : u ≠ v) : 1 ≤ |u| + |v| := by
  rcases eq_or_ne u 0 with hu | hu
  · subst hu
    have hv : v ≠ 0 := fun hv => h (by simp [hv])
    have h1 : 1 ≤ |v| := by
      rcases lt_or_gt_of_ne hv with h' | h'
      · rw [abs_of_neg h']; omega
      · rw [abs_of_pos h']; omega
    simp only [abs_zero, zero_add]
    exact h1
  · have h1 : 1 ≤ |u| := by
      rcases lt_or_gt_of_ne hu with h' | h'
      · rw [abs_of_neg h']; omega
      · rw [abs_of_pos h']; omega
    have h2 : (0 : ℤ) ≤ |v| := abs_nonneg v
    omega

/-! ### The transfer: a weight bounded below by 1 dominates the unweighted form -/

variable {ι R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- The weighted Dirichlet energy `Σ_e w e · (d e)²`, with `d e` the increment across edge
`e`. -/
def weightedEnergy (s : Finset ι) (w d : ι → R) : R := ∑ e ∈ s, w e * (d e) ^ 2

/-- The unweighted Dirichlet energy `Σ_e (d e)²`. -/
def energy (s : Finset ι) (d : ι → R) : R := ∑ e ∈ s, (d e) ^ 2

/-- **A weight bounded below by 1 dominates.** No structure on the graph is used: only
`1 ≤ w e` edgewise and `(d e)² ≥ 0`. -/
theorem weighted_ge_unweighted (s : Finset ι) (w d : ι → R) (hw : ∀ e ∈ s, 1 ≤ w e) :
    energy s d ≤ weightedEnergy s w d := by
  refine Finset.sum_le_sum fun e he => ?_
  have hsq : (0 : R) ≤ (d e) ^ 2 := sq_nonneg _
  calc (d e) ^ 2 = 1 * (d e) ^ 2 := (one_mul _).symm
    _ ≤ w e * (d e) ^ 2 := mul_le_mul_of_nonneg_right (hw e he) hsq

/-- **Poincaré transfer, at no loss of constant.**

If the *unweighted* form satisfies a Poincaré inequality `gap · V ≤ energy`, and every edge
weight is at least 1, then the *weighted* form satisfies the same inequality with the **same**
`gap`. This is the statement the `(|u|+|v|)`-weighted Fulman measure needed. -/
theorem poincare_transfer (s : Finset ι) (w d : ι → R) (gap V : R)
    (hw : ∀ e ∈ s, 1 ≤ w e) (hpoincare : gap * V ≤ energy s d) :
    gap * V ≤ weightedEnergy s w d :=
  le_trans hpoincare (weighted_ge_unweighted s w d hw)

/-! ### Anti-vacuity — both hypotheses are load-bearing -/

/-- **`1 ≤ w` is load-bearing.** A single edge with weight `1/2` and increment `1` has
weighted energy strictly below the unweighted energy, so the domination is false without the
bound. -/
theorem weighted_lt_unweighted_of_small_weight :
    ∃ (s : Finset (Fin 1)) (w d : Fin 1 → ℚ),
      weightedEnergy s w d < energy s d := by
  refine ⟨Finset.univ, fun _ => 1/2, fun _ => 1, ?_⟩
  norm_num [weightedEnergy, energy]

/-- **The inequality is not an equality.** The weight genuinely inflates the form when it
exceeds 1 — so `weighted_ge_unweighted` is not secretly `rfl`. -/
theorem energy_lt_weighted_of_large_weight :
    ∃ (s : Finset (Fin 1)) (w d : Fin 1 → ℚ),
      (∀ e ∈ s, 1 ≤ w e) ∧ energy s d < weightedEnergy s w d := by
  refine ⟨Finset.univ, fun _ => 3, fun _ => 1, ?_, ?_⟩
  · intro e _; norm_num
  · norm_num [weightedEnergy, energy]

/-- **The combinatorial core is not vacuous**: removable and addable corners both exist, just
never on one diagonal. The staircase-free partition `lam = (2, 1, 0, 0, …)` has a removable
corner at row `0` on diagonal `c = 1` and an addable corner at row `0` on diagonal `c = 2`. -/
theorem removable_and_addable_exist :
    ∃ (lam : ℕ → ℕ), Antitone' lam ∧ Removable lam 0 1 ∧ Addable lam 0 2 := by
  refine ⟨fun i => if i = 0 then 2 else if i = 1 then 1 else 0, ?_, ?_, ?_⟩
  · intro i
    rcases i with _ | _ | k <;> simp
  · constructor <;> norm_num [Removable]
  · norm_num [Addable]

end QOU.MassTheory.WeightedDirichletPoincare
