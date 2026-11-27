/-
  A pair energy is ZERO on a one-letter word, and that makes the shortest
  operator a global minimiser — so `min E` over a mixed-length catalogue is
  decided by construction rather than by the physics.

  WHY THIS FILE EXISTS. `qbeta_knot_operator_ilp_ohara_cost_probe.py` measured
  that the O'Hara cost's optimum over a 340-operator catalogue sits at `E = 0`,
  attained by the two 1-crossing operators, and reported it as "a STRUCTURAL
  property of a pair kernel, not a numerical accident". That was an
  observation, not a theorem. The owner asked whether it is proved. It was not.
  It is now, and in the general form rather than for the measured instance.

  THE CONTENT, and it is deliberately stated for an ARBITRARY kernel `K`:

  * `pairEnergy_singleton` — a one-letter word has no pairs, so the sum is
    empty and the energy is `0`. Definitionally, for every `K`.
  * `pairEnergy_nonneg` — if every pair term is non-negative then so is the
    total.
  * `pairEnergy_singleton_le` — the two together: under non-negativity, a
    one-letter word is a GLOBAL minimiser over every word whatsoever. This is
    the "rewards short operators" claim, proved.
  * `exists_singleton_minimiser` — the form that bites on a selection program:
    any catalogue containing a singleton has its minimum at that singleton, so
    the program cannot select anything longer.

  WHAT THIS DOES AND DOES NOT SAY.

  It says a pair energy cannot, on its own, select among operators of DIFFERENT
  lengths — the shortest wins for free. It says nothing against using one at
  FIXED length, which is where the measured probe found it does discriminate
  (8/38/96 feasible operators at lengths 2/3/4, narrowed to one cyclic orbit
  and its mirror). The two facts are complementary, not in tension: the same
  emptiness that makes the singleton free is what makes the kernel sensitive to
  where letters sit once there are at least two of them.

  It also does NOT say the O'Hara kernel is non-negative — that is a property
  of `tr_M` on letter pairs at the substrate anchor, measured (0 of 144
  feasible operators had `E < 0`) and not proved here. The theorems are stated
  WITH non-negativity as a hypothesis for exactly that reason.

  🛑 NOT PROVED HERE: that the corpus's `E_pair` is this `pairEnergy` (it is,
  by construction, but the bridge is a definition-unfolding in Python, not in
  Lean); that `tr_M(w_i w_j) ≥ 0` on the feasible set; and anything about
  whether the continuum `E_cat` shares the property.

  Sorry-free. No `axiom`, no conditional class, no `native_decide`.

  -- Ref: [leitner2026] computations/qbeta/qbeta_knot_operator_ilp_ohara_cost_probe.py
  -- Ref: [leitner2026] computations/qbeta/qbeta_ecat_pair_kernel_probe.py
  -- Ref: [leitner2026] QOU/QBeta/LetterSumBlindness.lean
-/
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

namespace QOU.Mass.PairEnergyRewardsShort

variable {α : Type*}

/-- Pairs of a head letter with each later letter, carrying the separation.
Mirrors the probe's `E_pair` inner loop and
`QBeta.ECatProbeAssertions.headPairs`. -/
def headPairs (K : α → α → ℕ → ℝ) (x : α) : List α → ℕ → ℝ
  | [], _ => 0
  | y :: ys, d => K x y d + headPairs K x ys (d + 1)

/-- The discretised pair energy: a sum over ordered pairs of the word. -/
def pairEnergy (K : α → α → ℕ → ℝ) : List α → ℝ
  | [] => 0
  | x :: xs => headPairs K x xs 1 + pairEnergy K xs

@[simp] theorem pairEnergy_nil (K : α → α → ℕ → ℝ) : pairEnergy K [] = 0 := rfl

/-- **A one-letter word has no pairs, so its pair energy is exactly `0`** — for
every kernel, definitionally. This is the fact the probe observed. -/
@[simp] theorem pairEnergy_singleton (K : α → α → ℕ → ℝ) (x : α) :
    pairEnergy K [x] = 0 := by
  simp [pairEnergy, headPairs]

theorem headPairs_nonneg {K : α → α → ℕ → ℝ} (hK : ∀ a b d, 0 ≤ K a b d)
    (x : α) : ∀ (ys : List α) (d : ℕ), 0 ≤ headPairs K x ys d
  | [], _ => le_refl 0
  | y :: ys, d => by
      have := headPairs_nonneg hK x ys (d + 1)
      have hxy := hK x y d
      simp only [headPairs]
      linarith

/-- A pair energy built from a non-negative kernel is non-negative. -/
theorem pairEnergy_nonneg {K : α → α → ℕ → ℝ} (hK : ∀ a b d, 0 ≤ K a b d) :
    ∀ w : List α, 0 ≤ pairEnergy K w
  | [] => le_refl 0
  | x :: xs => by
      have h1 := headPairs_nonneg hK x xs 1
      have h2 := pairEnergy_nonneg hK xs
      simp only [pairEnergy]
      linarith

/-- **"Rewards short operators", proved.**

Under a non-negative kernel, a one-letter word is a GLOBAL minimiser of the
pair energy — it attains `0` and nothing can go below `0`. So minimising a pair
energy over a catalogue of mixed lengths selects a shortest operator for a
reason that has nothing to do with the operator: the sum is empty. -/
theorem pairEnergy_singleton_le {K : α → α → ℕ → ℝ} (hK : ∀ a b d, 0 ≤ K a b d)
    (x : α) (w : List α) : pairEnergy K [x] ≤ pairEnergy K w := by
  rw [pairEnergy_singleton]
  exact pairEnergy_nonneg hK w

/-- The form that bites on a selection program: if the catalogue contains ANY
one-letter word, the program's optimum is `0` and is attained there, whatever
else the catalogue holds.

This is why the measured degeneracy is structural. It is also exactly why the
honest comparison is at FIXED length, where every candidate has the same number
of pairs and the kernel's separation-dependence is what decides. -/
theorem exists_singleton_minimiser {K : α → α → ℕ → ℝ} (hK : ∀ a b d, 0 ≤ K a b d)
    (cat : List (List α)) (x : α) (hmem : [x] ∈ cat) :
    ∃ w₀ ∈ cat, pairEnergy K w₀ = 0 ∧ ∀ w ∈ cat, pairEnergy K w₀ ≤ pairEnergy K w :=
  ⟨[x], hmem, pairEnergy_singleton K x,
    fun w _ => pairEnergy_singleton_le hK x w⟩

/-- Contrapositive, and the useful one for design: if a pair energy is to
select something LONGER than one letter, the kernel must take a negative value
somewhere. Stated as the exact obstruction rather than as advice. -/
theorem neg_kernel_of_nonsingleton_minimiser {K : α → α → ℕ → ℝ}
    (x : α) (w : List α) (hlt : pairEnergy K w < pairEnergy K [x]) :
    ¬ (∀ a b d, 0 ≤ K a b d) := by
  intro hK
  exact absurd hlt (not_lt.mpr (pairEnergy_singleton_le hK x w))

end QOU.Mass.PairEnergyRewardsShort
