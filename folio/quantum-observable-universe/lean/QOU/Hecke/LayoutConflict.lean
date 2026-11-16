/-
# Two disjoint intervals touch at one boundary — so a colour tube needs a
# non-contiguous layout

The `Delta_bind` arc's extensive-term deficit reduces to a counting statement,
and this file proves the counting.

`atom_braid_word_3A` lays `3A` strands out so that nucleon `k` owns
`{3k, 3k+1, 3k+2}` — three CONSECUTIVE positions. That contiguity is exactly what
makes the intra-nucleon crossings single Hecke generators. A *colour tube* — the
candidate mechanism for the missing factor of 3 — instead wants **three**
colour-matched couplings across each interface, each a single generator, on
pairwise non-adjacent supports so that `tr_M` factorises and `b -> b^3`.

`computations/qbeta/qbeta_layout_conflict_probe.py` shows exhaustively that no
ordering of the strands does both, at `A = 2` (720 orderings) and `A = 3`
(362 880). This file supplies the reason, for every `A`, in one lemma:

**two disjoint intervals of the integers are adjacent across at most one pair.**

So a contiguous layout admits at most ONE single-generator coupling per
interface, against the three a colour tube needs — and in the canonical layout
even that one joins colour 2 of nucleon `k` to colour 0 of nucleon `k+1`, i.e. it
is colour-MISMATCHED (`canonical_boundary_is_the_top_of_the_lower_block`).

## What is proved, and what is measurement

**Proved here:** the interval lemma and its specialisation to the `3k` layout.
Nothing about energies, and nothing that needs `q`.

**Measurement, and NOT proved here:** that the missing scale factor is `3.0075`
against the peak `B/A`, and that `tr_M` factorises over disjoint non-adjacent
blocks. Those are
`computations/qbeta/qbeta_strand_multiplicity_probe.py` and
`qbeta_disjoint_support_factorisation_probe.py`. This file says only that the
layout cannot supply three couplings — not what three couplings would be worth.
-/

import Mathlib.Data.Finset.Card
import Mathlib.Tactic

namespace QOU.Hecke.LayoutConflict

/-- The block of `C` consecutive positions starting at `p`. -/
def block (p C : ℕ) : Finset ℕ := Finset.Ico p (p + C)

lemma mem_block {p C x : ℕ} : x ∈ block p C ↔ p ≤ x ∧ x < p + C := by
  simp [block]

/-- **The whole obstruction.** If a block ends strictly below where the next one
starts, the only way a member of the first is adjacent to a member of the second
is at the single boundary pair: the top of the lower block and the bottom of the
upper one.

Two disjoint intervals on a line touch once. Everything else in this file is a
specialisation. -/
theorem adjacent_pair_unique {p q C D x y : ℕ}
    (hgap : p + C ≤ q) (hx : x ∈ block p C) (hy : y ∈ block q D)
    (hadj : y = x + 1) : x = p + C - 1 ∧ y = q := by
  rw [mem_block] at hx hy
  omega

/-! ## The canonical `3k` layout

`atom_braid_word_3A` puts nucleon `k` at `{3k, 3k+1, 3k+2}`. Consecutive nucleons
are then consecutive blocks with no gap, so the lemma applies with `p = 3k`,
`C = 3`, `q = 3(k+1)`.

A coupling across an interface is determined by its LOWER endpoint — the upper
one is forced to be `+1` — so everything below is stated in terms of that single
natural number, which keeps `Fin` numerals and `Prod` out of the proofs. -/

/-- Nucleon `k`'s strands in the canonical layout. -/
abbrev nucleonBlock (k : ℕ) : Finset ℕ := block (3 * k) 3

/-- Consecutive nucleon blocks are disjoint and correctly ordered. -/
lemma nucleon_gap (k : ℕ) : 3 * k + 3 ≤ 3 * (k + 1) := by omega

/-- `x` is the lower endpoint of a single-generator coupling across the interface
`(k, k+1)`: it lies in nucleon `k` and `x + 1` lies in nucleon `k+1`. -/
def IsCoupling (k x : ℕ) : Prop :=
  x ∈ nucleonBlock k ∧ x + 1 ∈ nucleonBlock (k + 1)

/-- **The canonical layout's one boundary joins the TOP of nucleon `k` to the
BOTTOM of nucleon `k+1`** — position `3k+2` to position `3k+3`. Reading positions
within a nucleon as colours `0, 1, 2`, that is colour `2` to colour `0`: the one
available coupling is colour-MISMATCHED, before any question of how many there
are. -/
theorem canonical_boundary_is_the_top_of_the_lower_block {k x : ℕ}
    (h : IsCoupling k x) : x = 3 * k + 2 := by
  obtain ⟨hx, hy⟩ := h
  have := adjacent_pair_unique (nucleon_gap k) hx hy rfl
  omega

/-- And there is at most one such coupling per interface — against the three a
colour tube needs. This is the general-`A` statement the exhaustive search
verifies at `A = 2, 3`. -/
theorem at_most_one_coupling_per_interface {k x₁ x₂ : ℕ}
    (h₁ : IsCoupling k x₁) (h₂ : IsCoupling k x₂) : x₁ = x₂ := by
  rw [canonical_boundary_is_the_top_of_the_lower_block h₁,
      canonical_boundary_is_the_top_of_the_lower_block h₂]

/-- A colour tube needs `C` distinct couplings across one interface. For `C ≥ 2`
that is strictly more than the layout admits, so **no contiguous layout carries a
colour tube** — for any number of colours above one, hence in particular for
three. -/
theorem contiguous_layout_cannot_carry_a_colour_tube
    {C : ℕ} (hC : 2 ≤ C) {k : ℕ} (x : Fin C → ℕ)
    (hx : ∀ i, IsCoupling k (x i)) (hinj : Function.Injective x) : False := by
  have h0 : (0 : ℕ) < C := by omega
  have h1 : (1 : ℕ) < C := by omega
  have heq : x ⟨0, h0⟩ = x ⟨1, h1⟩ :=
    at_most_one_coupling_per_interface (hx _) (hx _)
  have := hinj heq
  simp [Fin.ext_iff] at this

/-! ## Colour mismatch at the unique boundary and `A - 1` collinearity (`bean qou-0c19`)

In the canonical `3k` block layout, reading strand positions modulo `3` as intra-block
colour indices `{0, 1, 2}`, the unique boundary coupling `x = 3k + 2` pairs colour `2`
of block `k` with colour `0` of block `k + 1` (`canonical_coupling_colour_mismatch`).
Moreover, across `A` blocks `{0, …, A - 1}` there are `A - 1` adjacent interfaces, so
any linear combination of `A` and the interface count `A - 1` collapses to a single
affine function of `A` (`interface_count_collinear_with_mass_number`). -/

/-- **Colour mismatch of the unique canonical coupling (`bean qou-0c19`).**
Every single-generator coupling `x` between `nucleonBlock k` and `nucleonBlock (k + 1)`
has lower colour index `x % 3 = 2` and upper colour index `(x + 1) % 3 = 0`, so the
two coupled strands never share the same colour index modulo `3`. -/
theorem canonical_coupling_colour_mismatch {k x : ℕ} (h : IsCoupling k x) :
    x % 3 = 2 ∧ (x + 1) % 3 = 0 ∧ x % 3 ≠ (x + 1) % 3 := by
  have hx : x = 3 * k + 2 := canonical_boundary_is_the_top_of_the_lower_block h
  refine ⟨?_, ?_, ?_⟩
  · omega
  · omega
  · omega

/-- **Collinearity of the linear-chain interface count `A - 1` with `A` (`bean qou-0c19`).**
Adding a term proportional to the interface count `A - 1` to an affine function
`α * A + β` produces another affine function of `A` with slope `α + γ` and intercept
`β - γ`, introducing zero independent linear degrees of freedom. -/
theorem interface_count_collinear_with_mass_number (α β γ A : ℚ) :
    α * A + β + γ * (A - 1) = (α + γ) * A + (β - γ) := by
  ring

end QOU.Hecke.LayoutConflict
