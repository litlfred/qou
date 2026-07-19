/-
Copyright (c) 2026 litlfred. All rights reserved.

# A fixed two-term Habiro generator makes the Q_β `c_k` tower rigid

**The formalize-first rigor link behind the four-session `c_3` wire/un-wire
flip-flop** (`docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`;
history table in `docs/coordination/1ppq-qbeta.md`).

The on-`main` block `prop:q-beta-c-k-recursion-from-habiro-q-difference` *posits*
a depth-`d` linear recurrence on the ladder Taylor coefficients
`c_n = [u^n](Q_β/Q_A)`, and `prop:qbeta-ck-recursion-kernel-constraints`
(`QBetaCKRecursionKernelConstraints.lean`) *constrains* that kernel
(`depth ≥ 2`, `a_2 = c_2 = -1`, `a_1 = -c_3`, `a_1` bar-odd, the C13 refutation).
What neither file proves is the **rigidity that motivates the whole picture**:
that *fixing one categorical generator* (a Habiro-type two-term rational element,
numerator over the bar-even denominator `[2]_q` of `QBetaResidueHabiroDual.lean`)
**forces** the recurrence and pins the *entire* `c_k` tower with **zero remaining
freedom** — so "re-choosing `c_3` this session" is a category error, not a
modelling choice.

This file supplies that link, over a **generic `CommRing R`** (AGENTS.md §7c;
no archimedean data, no `q_0`, no `ℝ`), as elementary finite-sum algebra:

* `conv_unique` — the Cauchy-product ("`P = Q * c`") equation has **at most one**
  solution `c` once `Q 0` is a unit. Uniqueness of the holonomic tower.
* `two_term_tail_recurrence` — a two-term generator (denominator degree `≤ 2`,
  numerator degree `≤ 1`) *forces* the depth-2 recurrence
  `Q₀·c_n + Q₁·c_{n-1} + Q₂·c_{n-2} = 0` for `n ≥ 2`. The recurrence is a
  **consequence** of rationality, not an ansatz.
* `c3_not_free` — the anti-flip-flop crux: once `(P,Q)` is fixed,
  `Q₀·c_3 + Q₁·c_2 + Q₂·c_1 = 0`, so `c_3` is a **dependent** quantity, not a
  free per-session fit.
* `c2_eq_neg_one_of_anchor` — with the proved anchor `Q₂ = Q₀` (encoding the
  Taylor-exact `a_2 = c_2 = -1` rung) and the ladder seed `c_0 = 1, c_1 = 0`,
  the tower recovers `c_2 = -1`. The **proved** rung falls out; `c_3` does not.
* `two_term_generator_rigid` — two coefficient towers arising from the **same**
  fixed generator `(P,Q)` are **equal**. Fixing the generator removes all
  freedom.

## What is NOT here (honesty / anti-laundering — AGENTS.md §"Axiomatization is
## NOT a Proof", §"flip-flop guard")

* **No `c_3` value.** Nothing below evaluates `c_3`, identifies it with
  `J_Hopf(1) = -2`, or asserts Taylor-exactness. `c_3 = -(Q₁c_2 + Q₂c_1)/Q₀` is
  pinned *relative to a fixed generator*; its numeric value needs the archimedean
  evaluation at `q_0`, which lives at the observable level (cheat sheet §"Im(q)
  fibre vs observable") and is deliberately absent.
* **No wiring.** Production wires only `c_2` (`QBetaCategoricalPrecisionLadder.lean`
  DISCIPLINE note); this file changes no dashboard and no registry tier.
* **The sole open input is the generator's existence**, recorded as the *defined,
  not asserted* predicate `FixedTwoTermGeneratorConjecture c` (no instance, no
  proof). The capstone `two_term_generator_rigid` is a genuine **conditional**
  result (§3b-cond): *if* such a fixed generator exists, *then* the tower is
  rigid. That the on-`main` ladder `cos(Φ(u))` (transcendental, not rational)
  admits such a fixed two-term rational generator reproducing production Q_β at
  `q_0` is **open** — the SW-residue / Hoefsmit-`H₃(q)` kernel frontier
  (`docs/scope/2026-06-05-qbeta-residue-a-klr-crystal-kernel-scope.md`).

LaTeX label: `prop:qbeta-generator-rigidity`

## References
- Open kernel ansatz: `prop:q-beta-c-k-recursion-from-habiro-q-difference`.
- Kernel constraints (depth ≥ 2, `a_2 = -1`, `a_1 = -c_3`): PR #1900,
  `QBetaCKRecursionKernelConstraints.lean`.
- Bar-odd `[2]_q`-denominator residue element (the fixed generator's shape):
  `prop:qbeta-residue-habiro-dual`, `QBetaResidueHabiroDual.lean`.
- Flip-flop canonical framing: `docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`.
-- Ref: [habiro2008] https://doi.org/10.1007/s00222-008-0142-x
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.GroupWithZero.Units.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.LinearCombination

namespace QOU.QBeta

open Finset

variable {R : Type*} [CommRing R]

/-- The Cauchy product `(Q * c)_n = ∑_{j≤n} Q_j · c_{n-j}` — the coefficient-level
meaning of the rational generating function `c = P / Q`, i.e. `P = Q * c`. -/
def convCoeff (Q c : ℕ → R) (n : ℕ) : R :=
  ∑ j ∈ range (n + 1), Q j * c (n - j)

/-- **Uniqueness of the holonomic tower.** If `Q 0` is a unit, the convolution
equation `Q * c = Q * c'` (both sides the same numerator `P`) forces `c = c'`.
Pure strong induction: peeling the `j = 0` term isolates `Q₀·c_n`, and every
other term references a strictly smaller index handled by the hypothesis. -/
theorem conv_unique {Q c c' : ℕ → R} (hQ0 : IsUnit (Q 0))
    (h : ∀ n, convCoeff Q c n = convCoeff Q c' n) : c = c' := by
  funext n
  induction n using Nat.strong_induction_on with
  | _ n ih =>
    have hn := h n
    unfold convCoeff at hn
    rw [sum_range_succ', sum_range_succ'] at hn
    simp only [Nat.sub_zero] at hn
    have hsum : (∑ i ∈ range n, Q (i + 1) * c (n - (i + 1)))
              = ∑ i ∈ range n, Q (i + 1) * c' (n - (i + 1)) := by
      refine sum_congr rfl (fun i hi => ?_)
      have hlt : n - (i + 1) < n := by
        have := mem_range.mp hi; omega
      rw [ih (n - (i + 1)) hlt]
    rw [hsum] at hn
    have hcancel : Q 0 * c n = Q 0 * c' n := add_left_cancel hn
    exact hQ0.mul_right_injective hcancel

/-- `c` is generated by a **fixed two-term rational element** `P / Q`:
denominator degree `≤ 2` (two-term, the `[2]_q`-shape), numerator degree `≤ 1`,
and `Q 0` a unit. This is a *property* of `(c, P, Q)`; no `c_k` value is fixed. -/
def IsTwoTermGenerator (c P Q : ℕ → R) : Prop :=
  IsUnit (Q 0) ∧ (∀ j, 2 < j → Q j = 0) ∧ (∀ n, convCoeff Q c n = P n)
    ∧ (∀ m, 1 < m → P m = 0)

/-- General tail recurrence: with numerator degree `≤ dP` and denominator degree
`≤ dQ`, the coefficients satisfy `∑_{j≤dQ} Q_j · c_{n-j} = 0` for every
`n > dP` with `n ≥ dQ`. The extra high-`j` terms vanish by `Q j = 0`. -/
theorem tail_recurrence {P Q c : ℕ → R} {dP dQ : ℕ}
    (hP : ∀ m, dP < m → P m = 0) (hQ : ∀ j, dQ < j → Q j = 0)
    (hconv : ∀ n, convCoeff Q c n = P n) {n : ℕ} (hn : dP < n) (hnq : dQ ≤ n) :
    (∑ j ∈ range (dQ + 1), Q j * c (n - j)) = 0 := by
  have h1 : (∑ j ∈ range (n + 1), Q j * c (n - j)) = 0 := by
    have := hconv n; unfold convCoeff at this; rw [this]; exact hP n hn
  have hsub : range (dQ + 1) ⊆ range (n + 1) := by
    intro x hx; rw [mem_range] at hx ⊢; omega
  have hzero : ∀ j ∈ range (n + 1), j ∉ range (dQ + 1) → Q j * c (n - j) = 0 := by
    intro j _ hj'
    rw [mem_range] at hj'
    rw [hQ j (by omega), zero_mul]
  rw [sum_subset hsub hzero]; exact h1

/-- **A fixed two-term generator forces the depth-2 recurrence.** For every
`n ≥ 2`, `Q₀·c_n + Q₁·c_{n-1} + Q₂·c_{n-2} = 0`. The recurrence is a
*consequence* of rationality, not the on-`main` ansatz. -/
theorem two_term_tail_recurrence {P Q c : ℕ → R}
    (h : IsTwoTermGenerator c P Q) {n : ℕ} (hn : 2 ≤ n) :
    Q 0 * c n + Q 1 * c (n - 1) + Q 2 * c (n - 2) = 0 := by
  obtain ⟨_, hQdeg, hconv, hPdeg⟩ := h
  have hrec := tail_recurrence (dP := 1) (dQ := 2) hPdeg hQdeg hconv
    (by omega : (1 : ℕ) < n) hn
  simpa [sum_range_succ, Nat.sub_zero, add_assoc] using hrec

/-- **The anti-flip-flop crux.** Once the generator `(P,Q)` is fixed, `c_3` obeys
`Q₀·c_3 + Q₁·c_2 + Q₂·c_1 = 0` — a *dependent* quantity tied to `c_1, c_2` and the
fixed generator, **not** a free per-session fit. No `c_3` value is asserted. -/
theorem c3_not_free {P Q c : ℕ → R} (h : IsTwoTermGenerator c P Q) :
    Q 0 * c 3 + Q 1 * c 2 + Q 2 * c 1 = 0 :=
  two_term_tail_recurrence h (by norm_num)

/-- The **proved** rung falls out. With the anchor `Q₂ = Q₀` (which encodes the
Taylor-exact `a_2 = c_2 = -1` kernel rung) and the ladder seed `c_0 = 1, c_1 = 0`,
the fixed generator recovers `c_2 = -1`. `c_3` is *not* recovered — it needs
`Q₁`, the open bar-odd datum. -/
theorem c2_eq_neg_one_of_anchor {P Q c : ℕ → R} (h : IsTwoTermGenerator c P Q)
    (hanchor : Q 2 = Q 0) (h0 : c 0 = 1) (h1 : c 1 = 0) : c 2 = -1 := by
  have hrec := two_term_tail_recurrence h (le_refl 2)
  simp only [show (2 : ℕ) - 1 = 1 from rfl, show (2 : ℕ) - 2 = 0 from rfl,
    h0, h1, hanchor] at hrec
  have hcancel : Q 0 * c 2 = Q 0 * (-1) := by linear_combination hrec
  exact h.1.mul_right_injective hcancel

/-- **Generator rigidity — fixing `(P,Q)` removes all freedom.** Two coefficient
towers `c, c'` arising from the *same* fixed two-term generator `(P,Q)` are equal.
This is the formal content of "you cannot re-choose `c_3` once the categorical
generator is fixed". -/
theorem two_term_generator_rigid {P Q c c' : ℕ → R}
    (h : IsTwoTermGenerator c P Q) (h' : IsTwoTermGenerator c' P Q) : c = c' := by
  obtain ⟨hQ0, _, hconv, _⟩ := h
  obtain ⟨_, _, hconv', _⟩ := h'
  refine conv_unique hQ0 (fun n => ?_)
  rw [hconv, hconv']

/-- **The sole open input**, recorded as a *defined, not asserted* predicate
(§3b-tax primary conjecture; no instance, no proof anywhere in the corpus): that
the ladder tower `c` admits a fixed two-term rational generator whose denominator
carries the proved `c_2 = -1` anchor `Q₂ = Q₀`. That the transcendental on-`main`
generator `cos(Φ(u))` realizes such a rational element reproducing production
`Q_β` at `q_0` is the open kernel frontier — this file proves the rigidity that
*would* follow, never that the generator exists. -/
def FixedTwoTermGeneratorConjecture (c : ℕ → R) : Prop :=
  ∃ P Q : ℕ → R, IsTwoTermGenerator c P Q ∧ Q 2 = Q 0

end QOU.QBeta
