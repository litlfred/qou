/-
# Crossing ENERGY and crossing COUNT select the same word — except across writhe

Bean `qou-99qc`, live open item: what cost function fixes the crossing budget.

## The question this answers

`FrobeniusSelected B y cands cost w` is the corpus's selection structure, and
the cost it is instantiated with is the crossing **count**,
`fun w => (w.length : R)` (`frobeniusSelected_borromean`). The owner objected
(2026-09-14, verbatim): *"The selection rule shouldn't be minimum crossing... It
may be higher energy than a non-minimal crossing."* — i.e. swap the count for
the crossing **energy** `def:crossing-energy`.

`computations/qbeta/qbeta_crossing_energy_separates_the_gluon_probe.py` measured
that the two costs do disagree on the gluon dressing, and left open *when*.
These lemmas answer that exactly, from the corpus's own decomposition rather
than from a new principle.

## What is proved

`QOU.Braiding.crossingEnergy p m q = p·q − m·q⁻¹` splits (already in the corpus,
`crossingEnergy_split`) into

    symChannel  = (p − m) · (q + q⁻¹)/2      the WRITHE   — a braid invariant
    asymChannel = (p + m) · (q − q⁻¹)/2      the COUNT    — not invariant

and the whole answer follows from which multiplicity sits in which channel:

* `crossingEnergy_cancelling_pair` — a cancelling pair `(p,m) → (p+1,m+1)`
  leaves the writhe alone and raises the count by 2, so the energy rises by
  exactly `q − q⁻¹`, strictly positive for `1 < q`
  (`crossingEnergy_lt_of_cancelling_pair`). **So the energy is a function of the
  WORD, not of the braid element** — unlike the observable it would be used to
  select for.
* `energy_le_iff_count_le_of_writhe_eq` — at fixed writhe the energy ordering
  and the count ordering are the SAME ordering, as an `iff`. Swapping the cost
  therefore changes no selection within a fixed-writhe family.
* `crossingEnergy_sub_eq_writhe_term_of_count_eq` — at fixed count the two
  energies differ by exactly `(W₁ − W₂) · symmetricWeight q`.

**Consequence.** Crossing energy is crossing count plus a writhe correction. It
re-ranks candidates **iff** their writhes differ, and never otherwise. The
measured disagreement the probe found — `σ₁` versus `σ₁⁻¹`, tied at count 1 and
separated by energy — is precisely a writhe difference (`+1` against `−1`), and
by these lemmas that is the only way the two costs can ever disagree.

So the objection to the count is NOT answered by the energy, and
`isLeast_energy_iff_isLeast_count_of_writhe_eq` closes it: the energy's only
admissible descent to the braid element — its minimum over the class — IS
count-minimisation. A genuine upgrade must be a functional that is not a
function of `(p, m)` at all. An embedding
energy (O'Hara / Möbius via the Bring surface) is such a functional; that is the
structural reason the owner's proposed direction is the right class, and it is
not built.

## Scope

Statements about the two cost functionals, nothing else. They do **not** select
a word, do **not** adopt or retire either cost, and do **not** touch the
observable — per AGENTS.md §NO FITTING a cost is never chosen by which candidate
it lands on. The companion probe reports Q_β per candidate as a consequence, and
it is an input to nothing here.

Verified with `lean -DautoImplicit=false -s 65536` via the library sweep (a bare
`lean` is a weaker check — AGENTS.md).
-/

import QOU.Braiding.crossing_energy_channels

namespace QOU.Mass.CrossingEnergySelectionEqualsCount

open QOU.Braiding

/-- The corpus split, restated here so the file is self-contained:
`crossingEnergy = symChannel + asymChannel`. -/
theorem crossingEnergy_split (p m : ℕ) (q : ℝ) :
    crossingEnergy p m q = symChannel p m q + asymChannel p m q := by
  simp only [crossingEnergy, symChannel, asymChannel, symmetricWeight,
    antisymmetricWeight]
  ring

/-- `symChannel` reads only the writhe `p − m`. -/
theorem symChannel_eq_of_writhe_eq {p₁ m₁ p₂ m₂ : ℕ} (q : ℝ)
    (hw : (p₁ : ℝ) - m₁ = (p₂ : ℝ) - m₂) :
    symChannel p₁ m₁ q = symChannel p₂ m₂ q := by
  simp only [symChannel, hw]

/-- `asymChannel` reads only the crossing count `p + m`. -/
theorem asymChannel_eq_of_count_eq {p₁ m₁ p₂ m₂ : ℕ} (q : ℝ)
    (hc : (p₁ : ℝ) + m₁ = (p₂ : ℝ) + m₂) :
    asymChannel p₁ m₁ q = asymChannel p₂ m₂ q := by
  simp only [asymChannel, hc]

/-- Equal writhe **and** equal count force equal energy: the forced tie. -/
theorem crossingEnergy_eq_of_writhe_and_count_eq {p₁ m₁ p₂ m₂ : ℕ} (q : ℝ)
    (hw : (p₁ : ℝ) - m₁ = (p₂ : ℝ) - m₂)
    (hc : (p₁ : ℝ) + m₁ = (p₂ : ℝ) + m₂) :
    crossingEnergy p₁ m₁ q = crossingEnergy p₂ m₂ q := by
  rw [crossingEnergy_split, crossingEnergy_split,
    symChannel_eq_of_writhe_eq q hw, asymChannel_eq_of_count_eq q hc]

/-- Inserting a cancelling pair fixes the writhe and raises the count by two,
so the energy rises by exactly `q − q⁻¹`. -/
theorem crossingEnergy_cancelling_pair (p m : ℕ) (q : ℝ) :
    crossingEnergy (p + 1) (m + 1) q = crossingEnergy p m q + (q - q⁻¹) := by
  simp only [crossingEnergy]
  push_cast
  ring

/-- For a substrate parameter `1 < q` the gap `q − q⁻¹` is strictly positive. -/
theorem sub_inv_pos {q : ℝ} (hq : 1 < q) : 0 < q - q⁻¹ := by
  have hq0 : (0 : ℝ) < q := lt_trans zero_lt_one hq
  have : q⁻¹ < 1 := by
    rw [inv_lt_one_iff₀]
    exact Or.inr hq
  linarith

/-- **The energy is a word functional, not a braid invariant.** A cancelling
pair changes no braid element and no Markov trace, and strictly raises the
energy. -/
theorem crossingEnergy_lt_of_cancelling_pair (p m : ℕ) {q : ℝ} (hq : 1 < q) :
    crossingEnergy p m q < crossingEnergy (p + 1) (m + 1) q := by
  rw [crossingEnergy_cancelling_pair]
  linarith [sub_inv_pos hq]

/-- **At fixed writhe the two costs are the same ordering.** Stated as an `iff`,
so it says the orderings coincide rather than merely agreeing one way. -/
theorem energy_le_iff_count_le_of_writhe_eq {p₁ m₁ p₂ m₂ : ℕ} {q : ℝ}
    (hq : 1 < q) (hw : (p₁ : ℝ) - m₁ = (p₂ : ℝ) - m₂) :
    crossingEnergy p₁ m₁ q ≤ crossingEnergy p₂ m₂ q
      ↔ (p₁ : ℝ) + m₁ ≤ (p₂ : ℝ) + m₂ := by
  have hpos := sub_inv_pos hq
  rw [crossingEnergy_split, crossingEnergy_split,
    symChannel_eq_of_writhe_eq q hw]
  simp only [asymChannel, antisymmetricWeight]
  constructor
  · intro h
    have h2 : ((p₁ : ℝ) + m₁) * (q - q⁻¹) ≤ ((p₂ : ℝ) + m₂) * (q - q⁻¹) := by
      linarith
    exact le_of_mul_le_mul_right (by linarith [h2]) hpos
  · intro h
    have : ((p₁ : ℝ) + m₁) * (q - q⁻¹) ≤ ((p₂ : ℝ) + m₂) * (q - q⁻¹) :=
      mul_le_mul_of_nonneg_right h (le_of_lt hpos)
    linarith

/-- **At fixed count the two energies differ by exactly the writhe term.** This
is the whole of the disagreement between the costs. -/
theorem crossingEnergy_sub_eq_writhe_term_of_count_eq {p₁ m₁ p₂ m₂ : ℕ} (q : ℝ)
    (hc : (p₁ : ℝ) + m₁ = (p₂ : ℝ) + m₂) :
    crossingEnergy p₁ m₁ q - crossingEnergy p₂ m₂ q
      = (((p₁ : ℝ) - m₁) - ((p₂ : ℝ) - m₂)) * symmetricWeight q := by
  rw [crossingEnergy_split, crossingEnergy_split,
    asymChannel_eq_of_count_eq q hc]
  simp only [symChannel]
  ring

/-! ## The admissible descent of the energy IS the crossing count

`crossingEnergy_lt_of_cancelling_pair` says the energy is a word functional, so
it does not descend to the braid element. A word functional has exactly one
canonical descent — its extremum over the fibre — and here that extremum is
computable, because the writhe is constant on a braid class while the count is
not.

`isLeast_energy_iff_isLeast_count_of_writhe_eq` is the consequence, over any
finite family of presentations sharing a writhe (which every braid class is):
**the energy-minimal presentation is exactly the count-minimal one.** So making
the energy admissible turns it *into* the crossing-count cost it was proposed to
replace, up to an additive invariant.

This is why the Bring embedding is the load-bearing part of the owner's
proposal rather than an implementation detail. The corpus's own
`QOU.MobiusEnergy.ClassicalMobiusEnergy` is likewise a functional of an
EMBEDDING — its docstring says so outright, *"this structure holds no
isotopy-class data"* — so it inherits the same defect, and what repairs it is
either the FHW minimiser or a canonical embedding. The Bring surface is the
candidate canonical embedding. Without one, swapping in an embedding energy
swaps one presentation-dependent cost for another. -/

/-- **The energy-minimal presentation is the count-minimal one.** Over any
finite nonempty family of presentations sharing a writhe — which is what a
braid class is, the writhe being invariant — minimising `crossingEnergy` and
minimising the crossing count are the same problem. -/
theorem isLeast_energy_iff_isLeast_count_of_writhe_eq {q : ℝ} (hq : 1 < q)
    (S : Finset (ℕ × ℕ))
    (hw : ∀ a ∈ S, ∀ b ∈ S, (a.1 : ℝ) - a.2 = (b.1 : ℝ) - b.2)
    {x : ℕ × ℕ} (hx : x ∈ S) :
    (∀ y ∈ S, crossingEnergy x.1 x.2 q ≤ crossingEnergy y.1 y.2 q)
      ↔ (∀ y ∈ S, (x.1 : ℝ) + x.2 ≤ (y.1 : ℝ) + y.2) := by
  constructor
  · intro h y hy
    exact (energy_le_iff_count_le_of_writhe_eq hq (hw x hx y hy)).mp (h y hy)
  · intro h y hy
    exact (energy_le_iff_count_le_of_writhe_eq hq (hw x hx y hy)).mpr (h y hy)

end QOU.Mass.CrossingEnergySelectionEqualsCount
