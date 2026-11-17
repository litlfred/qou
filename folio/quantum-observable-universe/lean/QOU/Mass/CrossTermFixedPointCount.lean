import Mathlib.GroupTheory.Perm.Fin
import Mathlib.Data.Fintype.Pi
import Mathlib.Data.Fintype.Card

/-!
# The order-zero cross term is a fixed-point count (Burnside), read as a groupoid cardinality

Route C, step 1, of the 2026-09-05 binding-gap survey (bean `qou-8uxw`). The T1 probe
(`interleaving_cross_term_q_adic_order_probe.py`, bean `qou-212w`) measured that at `q = 1`,
`z = 1/2`, the Markov trace on `ℚS₄` is `tr(w) = 2^{c(w) − 4}` with `c(w)` the number of cycles,
so the unnormalised cross term at `q = 1` is `2^{c(interleaved)} − 2^{c(sequential)} = 2 − 8 = −6`.

Groupoidification (Baez–Hoffnung–Walker) reads a character of a permutation representation as a
**count of fixed points** — the cardinality of the fixed-point set of `w` acting on colourings
`Fin 4 → Fin 2`, i.e. the degroupoidified span `X ← X^w → X`. That is exactly `2^{c(w)}`: a
colouring is `w`-invariant iff it is constant on each cycle. This file pins the two instances by
finite computation — the one place `decide` is the honest tool (a 16-element search, twice):

    interleaved  w = s₀ s₁ s₀ s₂ s₁   — a 4-cycle — fixes  2 colourings
    sequential   w = s₀² s₁² s₂ = s₂  — a transposition — fixes 8 colourings

so the `q = 1` cross term is `2 − 8 = −6` fixed colourings, matching `[2]_q⁴·Δ |_{q=1} = −6`.

The `q`-deformation of this count is the μ-weighted quantum trace on `V^{⊗4}` (the 16-dim
spin-½ route of `markov_trace_n4_interleaved_cross_term_probe.py`), which degenerates to the
ordinary trace of the permutation matrix — the fixed-point count — at `q = 1`. That degeneration
is checked exactly in the probe; here only the classical counts are formalised.

-- Ref: [leitner2026] computations/probes/interleaving_cross_term_closures_probe.py
-- Ref: [baez-hoffnung-walker2010-groupoidification] https://arxiv.org/abs/0908.4305
-/

namespace QOU.Mass.CrossTermFixedPointCount

open Equiv

/-- The adjacent transposition `s_i = (i, i+1)` on four strands. -/
def s (i : Fin 3) : Perm (Fin 4) := swap i.castSucc i.succ

/-- The permutation of the interleaved word `s₀ s₁ s₀ s₂ s₁` (a 4-cycle). -/
def interleaved : Perm (Fin 4) := s 0 * s 1 * s 0 * s 2 * s 1

/-- The permutation of the sequential word `s₀² s₁² s₂` (the transposition `s₂`). -/
def sequential : Perm (Fin 4) := s 0 * s 0 * (s 1 * s 1) * s 2

/-- The number of `w`-invariant two-colourings of the four strands: the fixed-point count of
`w` on `Fin 4 → Fin 2`, i.e. the character of the permutation representation on `V^{⊗4}`,
`dim V = 2`, at `w`. -/
def fixedColourings (w : Perm (Fin 4)) : ℕ :=
  (Finset.univ.filter fun c : Fin 4 → Fin 2 => ∀ i, c (w i) = c i).card

/-- The interleaved word's permutation fixes exactly `2 = 2^1` colourings: it is a 4-cycle. -/
theorem fixedColourings_interleaved : fixedColourings interleaved = 2 := by decide

/-- The sequential word's permutation fixes exactly `8 = 2^3` colourings: it is a transposition. -/
theorem fixedColourings_sequential : fixedColourings sequential = 8 := by decide

/-- **The order-zero cross term is a fixed-point-count difference**: `2 − 8 = −6`, the value of
the unnormalised cross term `[2]_q⁴·Δ` at `q = 1` measured in the T1 probe. -/
theorem crossTerm_q_one_eq_fixedPoint_diff :
    (fixedColourings interleaved : ℤ) - fixedColourings sequential = -6 := by
  rw [fixedColourings_interleaved, fixedColourings_sequential]; norm_num

/-- The sequential word's permutation is the single transposition `s₂` (the two squares cancel). -/
theorem sequential_eq_s2 : sequential = s 2 := by decide


/-- **Fixed-point counts of the identity and adjacent generators (`qou-8uxw`).**
The identity fixes all `2^4 = 16` two-colourings, while each adjacent transposition
`s_i` has `3` cycles and fixes `2^3 = 8` two-colourings. -/
theorem fixedColourings_one_and_generators :
    fixedColourings 1 = 16 ∧
      fixedColourings (s 0) = 8 ∧
      fixedColourings (s 1) = 8 ∧
      fixedColourings (s 2) = 8 := by decide

/-- **Cycle-order structure of `interleaved` and `sequential` (`qou-8uxw`).**
The 4-cycle `interleaved` has order 4 (`interleaved ^ 4 = 1`, `interleaved ^ 2 ≠ 1`),
its square `interleaved ^ 2` is a product of two disjoint transpositions fixing `2^2 = 4`
colourings, and `sequential` is an involution (`sequential ^ 2 = 1`). -/
theorem interleaved_and_sequential_orders_and_sq_fixedColourings :
    interleaved ^ 4 = 1 ∧
      interleaved ^ 2 ≠ 1 ∧
      sequential ^ 2 = 1 ∧
      fixedColourings (interleaved ^ 2) = 4 := by decide

end QOU.Mass.CrossTermFixedPointCount
