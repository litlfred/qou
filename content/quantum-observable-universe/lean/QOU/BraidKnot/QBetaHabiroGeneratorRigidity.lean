import Mathlib.Tactic

/-!
# QOU.BraidKnot.QBetaHabiroGeneratorRigidity

**Formalize-first structural narrowing for the Q_β precision-ladder
flip-flop** (the recurring `c_k` wire / un-wire saga; see
`docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`).

## The gap this addresses

`QBetaCategoricalPrecisionLadder` fixes each rung coefficient `c_k` of
the Q_β precision ladder

  `Q_β = Q_base · ∏_{k ≥ 2} (1 + c_k · b^k · ℏ_q^{2k})`

behind its **own** conditional class — `QbetaC3StructuralFormClass`
(`c_3 = J_Hopf`), `QbetaC4StructuralFormClass` (`c_4 = J·b⁴`),
`QbetaC5StructuralFormClass` (`c_5 = -(b²+½)`), … . Each rung is an
**independent** degree of freedom: any one `c_k` can be re-fit without
touching the others. That independence *is* the flip-flop — it is what
lets `c_3` be wired at N=3 and un-wired later (#1452 ↔ #1479) with no
structural contradiction.

## What is proved here (and what is NOT)

The honest formalize-first move is to state the **rigidity that a single
fixed generator would impose**, WITHOUT deriving any `c_k` value. If the
whole tower is the `u`-expansion of ONE fixed simple ("single-pole",
`1/(1 − ρu)`) generator — the natural shape of a *fixed* categorical
Habiro element rather than a per-rung menu — then its coefficients obey
a **rank-1 / Casoratian law**: `c_{k+1} = ρ · c_k`, so every rung from
`k = 4` on is *forced* by `c_2` and `c_3` (`c_2 · c_4 = c_3²`). Fixing
the generator collapses the per-rung freedom to **two** parameters.

This file:

1. defines `SingleGeneratorLaw` (the rank-1 recurrence on the `c_k`);
2. proves it **forces every higher rung** from `(ρ, c_2)`
   (`single_generator_forces`) and hence makes the `2×2` Hankel /
   Casoratian minor vanish (`hankel_minor_vanishes`);
3. proves the contrapositive **flip-flop obstruction**: a non-vanishing
   Hankel minor certifies that NO single generator fits
   (`not_single_generator_of_hankel_ne`), with a rational witness showing
   the corpus's independently-fitted menu (`c_2 = -1, c_3 = -2, c_4 ≠ -4`)
   is not rank-1;
4. records the **open conjecture** — that the TRUE categorical tower is a
   single fixed bar-odd ("sinh partner") Habiro generator — as a
   content-bearing `Prop` class with **no instance**
   (`QBetaSingleHabiroGenerator`), and derives the conditional rigidity
   from it (`qbeta_ladder_rigid_of_single_generator`, §3b-cond).

**DISCIPLINE.** This derives NO `c_k` value (in particular says nothing
about `c_3 = -2` vs the empirical `-2.0693`); it wires NOTHING to
production; the generator's existence is an OPEN class with no instance.
It is the bar-odd mirror of the bar-even
`HabiroNewtonLadder.casoratian_eq_zero` (4₁ Newton nodes) and is a
scope-(a) structural statement about the *fitted menu*, not a scope-(b)
exclusion of any Habiro construction — producing the generator is exactly
the open target `probe-qbeta-habiro-element-search`.

Everything is over a generic base ring/field (§7c) — no `ℝ`, no `sorry`,
no `axiom`.
-/

namespace QOU.BraidKnot

variable {K : Type*}

/-- A **single-generator (rank-1) coefficient law** for a ladder
    coefficient sequence `c : ℕ → K`: from index `2` on, consecutive
    coefficients are in fixed ratio `ρ`,

      `c (k+1) = ρ · c k`   for all `k ≥ 2`.

    This is the hallmark of ONE fixed simple generator `1/(1 − ρu)`
    (a single pole), as opposed to independently chosen per-rung
    coefficients `c_2, c_3, c_4, …` — the current corpus situation, in
    which each `c_k` lives behind its own conditional class. -/
def SingleGeneratorLaw [Mul K] (c : ℕ → K) (ρ : K) : Prop :=
  ∀ k, 2 ≤ k → c (k + 1) = ρ * c k

/-- **Every higher rung is forced by `(ρ, c 2)`.** Under the single-
    generator law, `c (k+2) = ρ^k · c 2` for all `k`. So a single fixed
    generator has exactly **two** free parameters (`ρ` and `c 2`); once
    `c 2` and `c 3` are known, `ρ` is pinned (`ρ = c 3 / c 2` over a
    field) and every rung `k ≥ 4` is determined — no independent
    per-rung freedom survives. -/
theorem single_generator_forces [CommRing K] {c : ℕ → K} {ρ : K}
    (h : SingleGeneratorLaw c ρ) :
    ∀ k, c (k + 2) = ρ ^ k * c 2 := by
  intro k
  induction k with
  | zero => simp
  | succ n ih =>
      have hl : c (n + 3) = ρ * c (n + 2) := h (n + 2) (by omega)
      change c (n + 3) = ρ ^ (n + 1) * c 2
      rw [hl, ih]; ring

/-- **Rank-1 / Casoratian minor vanishes.** Under the single-generator
    law the `2×2` Hankel minor of `(c 2, c 3, c 4)` is zero:

      `c 2 · c 4 = c 3 ²`.

    This is the coefficient-sequence Casoratian — the bar-odd mirror of
    `HabiroNewtonLadder.casoratian_eq_zero` (which collapses the bar-even
    4₁ Newton-node Casoratian). It is the single checkable equation that
    "the tower comes from one fixed generator" imposes on the first three
    live rungs. -/
theorem hankel_minor_vanishes [CommRing K] {c : ℕ → K} {ρ : K}
    (h : SingleGeneratorLaw c ρ) :
    c 2 * c 4 = c 3 ^ 2 := by
  have h3 : c 3 = ρ * c 2 := h 2 (by norm_num)
  have h4 : c 4 = ρ * c 3 := h 3 (by norm_num)
  rw [h4, h3]; ring

/-- **Flip-flop obstruction (contrapositive).** A non-vanishing Hankel
    minor `c 2 · c 4 ≠ c 3²` certifies that NO single-generator ratio `ρ`
    reproduces the tower — the coefficients carry genuine per-rung freedom
    beyond a single fixed generator. This is the precise, checkable sense
    in which an independently-fitted `c_k` menu "can flip-flop". -/
theorem not_single_generator_of_hankel_ne [CommRing K] {c : ℕ → K}
    (hHank : c 2 * c 4 ≠ c 3 ^ 2) :
    ¬ ∃ ρ, SingleGeneratorLaw c ρ := by
  rintro ⟨ρ, h⟩
  exact hHank (hankel_minor_vanishes h)

/-- **Flip-flop witness (illustrative, over `ℚ`).** The corpus's
    independently fitted menu takes `c_2 = -1`, `c_3 = -2`, while every
    proposed `c_4` — the empirical Taylor `≈ -1.14`, the categorical
    `-2·b⁴ ≈ -1.13` at `q₀` (with `b = hoefsmitB q₀ < 1`, so `-2b⁴ ∈
    (-2,0)`) — is `≠ -4`. A single generator would FORCE `c_4 = c_3²/c_2 =
    -4`. Here we take the representative `c_4 = -1` (any value `≠ -4`
    works): the Hankel minor is `(-1)(-1) = 1 ≠ 4 = (-2)²`, so no single
    generator fits. This exhibits the per-rung freedom concretely; it
    asserts NO exact `c_4` value. -/
example : ¬ ∃ ρ : ℚ,
    SingleGeneratorLaw (fun k => if k = 2 then -1 else if k = 3 then -2 else -1) ρ := by
  apply not_single_generator_of_hankel_ne
  norm_num

/-- **OPEN: the Q_β tower is a single fixed bar-odd Habiro generator.**

    Content-bearing conjecture class (§3b). It asserts that the TRUE
    categorical tower coefficients `cTrue` come from ONE fixed generator —
    i.e. there is a ratio `ρ` for which the rank-1 / Casoratian law holds
    at every rung `k ≥ 2`. The intended `ρ` is the categorical bar-odd
    ("sinh partner") Habiro element dual to the bar-even `[2]_q` prefactor
    of α_EM (cf. `QBetaResidueHabiroDual`), whose existence is the open
    target `probe-qbeta-habiro-element-search`.

    **No instance is provided** — the open state is the absence of a proof
    term. The class asserts NOTHING about the VALUE of any `c_k` (in
    particular nothing about `c_3`); it asserts only that fixing the
    generator removes the per-rung freedom. Producing an instance would
    require deriving the generator, which is NOT done here. -/
class QBetaSingleHabiroGenerator [Mul K] (cTrue : ℕ → K) : Prop where
  /-- The tower is rank-1: some fixed ratio `ρ` governs every rung `k ≥ 2`. -/
  exists_single_generator : ∃ ρ : K, SingleGeneratorLaw cTrue ρ

/-- **Conditional rigidity (§3b-cond).** GIVEN the open single-generator
    class, the `2×2` Hankel / Casoratian minor of the true tower vanishes —
    `c 2 · c 4 = c 3²` — so every rung `k ≥ 4` is forced by `c 2` and
    `c 3`. Proved sorry-free FROM the class; derives no `c_k` value. This
    is the honest statement "fixing the generator eliminates the
    flip-flop": the per-rung classes of `QBetaCategoricalPrecisionLadder`
    would all collapse into the two parameters `(ρ, c 2)` of one fixed
    element. -/
theorem qbeta_ladder_rigid_of_single_generator [CommRing K]
    (cTrue : ℕ → K) [h : QBetaSingleHabiroGenerator cTrue] :
    cTrue 2 * cTrue 4 = cTrue 3 ^ 2 := by
  obtain ⟨ρ, hlaw⟩ := h.exists_single_generator
  exact hankel_minor_vanishes hlaw

end QOU.BraidKnot
