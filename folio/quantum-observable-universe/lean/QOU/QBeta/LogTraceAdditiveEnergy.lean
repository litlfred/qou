import Mathlib.Analysis.SpecialFunctions.Log.Basic
import QOU.MathlibExt.DisjointBlockTraceLaw

/-!
# Route L: the log-trace energy `E_κ = κ · log |tr|` is additive where `tr` is multiplicative

Bean `qou-99qc`, route L (owner-selected 2026-11-21). P1 (#8681), P2 (#8680) and P3 (#8682)
stopped at one wall: the Markov-trace mass channel `E ∝ |tr| · [N]_q!/q^N` is
**multiplicative** on split and one-strand (connected-sum) words, so the energy of a composite
is not the sum of the energies of its parts. This file proves the elementary half of the remedy
and nothing more:

* `logEnergy_mul` / `logEnergy_list_prod`: `κ · log |·|` turns a product of non-zero traces into
  a sum. This is `Real.log_mul`; it is recorded so the consumers below have a name.
* `logEnergy_tr_mul_adjoin_gen`: for **any** `MarkovTrace` over `ℝ`, an element `a` of level `n`
  and any polynomial `b` in the single generator `g n` (a one-strand join: clasp, trefoil, …),
  the log-energy of `a * b` is the sum of the two. **Unconditional**: it rests on
  `DisjointBlockTrace.tr_mul_adjoin_gen`, which is proved from the Markov axioms alone.
* `logEnergy_disjoint_of_towerSpan`: the same for every `b` in the shifted subalgebra
  (disjoint blocks), **conditional** on the unproved tower hypothesis `TowerSpan`
  (`DisjointBlockTraceLaw.lean`), which is why the name carries `_of_towerSpan`.
* `crossTerm_eq_log_ratio`: on a word that does not factorise, the energy defect is
  `κ · log |tr W / (tr a · tr b)|` — the log of the ratio P1/P2 called the cross term.
* `logEnergy_qsq_ratio`: P3's index character has `χ(p) = q² χ(n)`, so the log-energy
  difference is `κ · 2 log q`.
* `no_kappa_for_index_character`: P3's sign problem **survives** the log. With `q > 1` the
  p-over-n shift `2 log q` and the electron's `3 log q` have the same sign, so no real `κ`
  makes the proton lighter than the neutron while giving the electron positive energy.
* `markov_log_signs`: for Markov traces `0 < t_e < 1` and `0 < t_n < t_p · t_e` (the hypotheses
  the probe verifies exactly for the P2 words), the decay balance
  `κ (log t_n − log t_p − log t_e)` is positive **iff** `κ < 0`, and the electron's
  `κ log t_e` is positive **iff** `κ < 0`. So the two orderings agree with each other, and both
  require the sign **opposite** to the corpus binding convention `B = −α log μ`, `α = E₀ > 0`
  (state energy `+α log tr`).

## What this file does NOT do

It does **not** fix `κ`. Additivity is a property of `log`; it is invariant under `κ ↦ c κ`,
so no amount of additivity can select a scale or a sign. The corpus's `α = E₀` (B_sym) is a
named normalisation, and its free-energy reading has no energy spectrum
(`QOU.Mass.FreeEnergySigned`). Calling `κ · log |tr|` an energy is the route's premise, not a
result. Ground field `ℝ` throughout, because `Real.log` is archimedean (AGENTS.md §7c); the
multiplicativity inputs are the generic-ring theorems of `DisjointBlockTraceLaw.lean`.

-- Ref: [leitner2026] bean qou-99qc (route L); Jones 1987 (`jones1987`) for multiplicativity
-- of the Markov trace under connected sum, of which `tr_mul_adjoin_gen` is the one-strand case.
-/

namespace QOU.QBeta.LogTraceAdditiveEnergy

open QOU.MathlibExt.DisjointBlockTrace

/-- The log-trace energy with scale `κ`. -/
noncomputable def logEnergy (κ t : ℝ) : ℝ := κ * Real.log |t|

/-- `κ · log |·|` is additive on a product of two non-zero values. -/
theorem logEnergy_mul (κ a b : ℝ) (ha : a ≠ 0) (hb : b ≠ 0) :
    logEnergy κ (a * b) = logEnergy κ a + logEnergy κ b := by
  unfold logEnergy
  rw [abs_mul, Real.log_mul (abs_ne_zero.mpr ha) (abs_ne_zero.mpr hb)]
  ring

/-- The identity strand (`tr 1 = 1`) carries zero log-energy for every `κ`. -/
theorem logEnergy_one (κ : ℝ) : logEnergy κ 1 = 0 := by
  simp [logEnergy]

/-- Additivity over a finite list of non-zero factors. -/
theorem logEnergy_list_prod (κ : ℝ) :
    ∀ l : List ℝ, (∀ t ∈ l, t ≠ 0) → logEnergy κ l.prod = (l.map (logEnergy κ)).sum
  | [], _ => by simp [logEnergy_one]
  | t :: l, h => by
    have ht : t ≠ 0 := h t (by simp)
    have hl : ∀ s ∈ l, s ≠ 0 := fun s hs => h s (by simp [hs])
    have hp : l.prod ≠ 0 := List.prod_ne_zero (fun h0 => hl 0 h0 rfl)
    rw [List.prod_cons, logEnergy_mul κ t _ ht hp, logEnergy_list_prod κ l hl]
    simp

/-- **The cross term is a log ratio.** On any word, the log-energy defect against two pieces is
`κ · log |tr W / (tr a · tr b)|`. It vanishes exactly when `|tr W| = |tr a · tr b|`. -/
theorem crossTerm_eq_log_ratio (κ tW a b : ℝ) (hW : tW ≠ 0) (ha : a ≠ 0) (hb : b ≠ 0) :
    logEnergy κ tW - (logEnergy κ a + logEnergy κ b) = κ * Real.log |tW / (a * b)| := by
  rw [← logEnergy_mul κ a b ha hb]
  unfold logEnergy
  rw [abs_div, Real.log_div (abs_ne_zero.mpr hW) (abs_ne_zero.mpr (mul_ne_zero ha hb))]
  ring

section Markov

variable {A : Type*} [Ring A] [Algebra ℝ A] (T : QOU.MathlibExt.OcneanuTrace.MarkovTrace ℝ A)

/-- **One-strand joins: the log-energy is additive, unconditionally.** For `a` at level `n` and
`b` any polynomial in the single generator `g n`, with non-zero traces. -/
theorem logEnergy_tr_mul_adjoin_gen (κ : ℝ) (n : ℕ) (h : ℝ)
    (hq : T.g n * T.g n = h • T.g n + 1) (a : A) (ha : a ∈ T.H n)
    (b : A) (hb : b ∈ Algebra.adjoin ℝ ({T.g n} : Set A))
    (ha0 : T.tr a ≠ 0) (hb0 : T.tr b ≠ 0) :
    logEnergy κ (T.tr (a * b)) = logEnergy κ (T.tr a) + logEnergy κ (T.tr b) := by
  rw [tr_mul_adjoin_gen T n h hq a ha b hb]
  exact logEnergy_mul κ _ _ ha0 hb0

/-- The cross term of a one-strand join is zero. -/
theorem crossTerm_adjoin_gen_eq_zero (κ : ℝ) (n : ℕ) (h : ℝ)
    (hq : T.g n * T.g n = h • T.g n + 1) (a : A) (ha : a ∈ T.H n)
    (b : A) (hb : b ∈ Algebra.adjoin ℝ ({T.g n} : Set A))
    (ha0 : T.tr a ≠ 0) (hb0 : T.tr b ≠ 0) :
    logEnergy κ (T.tr (a * b)) - (logEnergy κ (T.tr a) + logEnergy κ (T.tr b)) = 0 := by
  rw [logEnergy_tr_mul_adjoin_gen T κ n h hq a ha b hb ha0 hb0]
  ring

/-- **Disjoint blocks, conditional on `TowerSpan`.** Every `b` in the subalgebra generated by the
generators at levels `≥ n`. The hypothesis `TowerSpan T` is unproved for the Hecke tower. -/
theorem logEnergy_disjoint_of_towerSpan [TowerSpan T]
    (hquad : ∀ m : ℕ, ∃ h : ℝ, T.g m * T.g m = h • T.g m + 1)
    (κ : ℝ) (n : ℕ) (a : A) (ha : a ∈ T.H n) (b : A) (hb : b ∈ shifted T n)
    (ha0 : T.tr a ≠ 0) (hb0 : T.tr b ≠ 0) :
    logEnergy κ (T.tr (a * b)) = logEnergy κ (T.tr a) + logEnergy κ (T.tr b) := by
  rw [disjointBlock_of_towerSpan T hquad n a ha b hb]
  exact logEnergy_mul κ _ _ ha0 hb0

end Markov

/-- **P3's index character.** If `χ(p) = q² χ(n)` with `q > 0`, `χ(n) ≠ 0`, the log-energy
difference is `κ · 2 log q`. -/
theorem logEnergy_qsq_ratio (κ q c : ℝ) (hq : 0 < q) (hc : c ≠ 0) :
    logEnergy κ (q ^ 2 * c) - logEnergy κ c = κ * (2 * Real.log q) := by
  have hq2 : q ^ 2 ≠ 0 := pow_ne_zero 2 hq.ne'
  rw [logEnergy_mul κ _ _ hq2 hc]
  unfold logEnergy
  rw [abs_of_pos (pow_pos hq 2), Real.log_pow]
  push_cast
  ring

/-- **P3's sign problem survives the log.** With `q > 1`, no `κ` makes the proton (index
character `q²` above the neutron) lighter, `κ · 2 log q < 0`, while giving the electron (index
character `q³`) positive energy, `κ · 3 log q > 0`. -/
theorem no_kappa_for_index_character (q : ℝ) (hq : 1 < q) :
    ¬ ∃ κ : ℝ, κ * (2 * Real.log q) < 0 ∧ 0 < κ * (3 * Real.log q) := by
  rintro ⟨κ, h1, h2⟩
  have hl : 0 < Real.log q := Real.log_pos hq
  rcases lt_trichotomy κ 0 with hk | hk | hk
  · nlinarith
  · subst hk; simp at h1
  · nlinarith

/-- **Markov-trace signs.** For `0 < t_e < 1`, `0 < t_n`, `0 < t_p` and `t_n < t_p · t_e`:
the decay balance `κ (log t_n − log t_p − log t_e)` is positive iff `κ < 0`, and the electron's
log-energy `κ log t_e` is positive iff `κ < 0`. The probe checks the four hypotheses exactly
for the P2 words (`nuc11` p, n; `e⁻ = σ₀³`). -/
theorem markov_log_signs (κ te tn tp : ℝ) (he0 : 0 < te) (he1 : te < 1) (hn : 0 < tn)
    (hp : 0 < tp) (hnp : tn < tp * te) :
    (0 < κ * (Real.log tn - Real.log tp - Real.log te) ↔ κ < 0) ∧
      (0 < κ * Real.log te ↔ κ < 0) := by
  have hle : Real.log te < 0 := Real.log_neg he0 he1
  have hD : Real.log tn - Real.log tp - Real.log te < 0 := by
    have := Real.log_lt_log hn hnp
    rw [Real.log_mul hp.ne' he0.ne'] at this
    linarith
  constructor
  · constructor
    · intro h
      by_contra hk
      push_neg at hk
      nlinarith
    · intro hk; nlinarith
  · constructor
    · intro h
      by_contra hk
      push_neg at hk
      nlinarith
    · intro hk; nlinarith

end QOU.QBeta.LogTraceAdditiveEnergy
