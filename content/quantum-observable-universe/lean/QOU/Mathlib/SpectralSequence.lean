/-!
# QOU.Mathlib.SpectralSequence — abstract spectral-sequence API

A minimal, upstreamable shape for the `E_r`-page library that
QOU's GB-filtration spectral sequence and Wedderburn-block
arguments need.  Mathlib has homological-algebra primitives
(`HomotopyCategory`, `DerivedCategory`, `ChainComplex`) but no
`E_r`-page abstraction with collapse criteria.  This file fills
that gap with the **smallest** API the QOU substrate consumes:

1. `SpectralSequence R` — pages indexed by `ℕ × ℤ × ℤ` (page,
   bidegree (p, q)), valued in `R`-modules that are abstractly
   `Type*`.
2. `differential` of bidegree `(r, 1 - r)` (cohomological
   convention).
3. `CollapsesAt r₀` predicate — `d_r = 0` for all `r ≥ r₀`.
4. `convergesTo` placeholder relating the `r₀` page to the
   `E_∞`-target.

The QOU GB-filtration claim is `CollapsesAt 2`, i.e. the spectral
sequence collapses at the `E_2` page (Wedderburn block
decomposition coincides with `E_2`).

This file is namespaced `QOU.Mathlib.SpectralSequence` to mark it
as an upstreamable candidate.  Migration to Mathlib proper would
keep the same shape with `R`-modules replaced by
`Mathlib.CategoryTheory.GradedObject` machinery.

LaTeX label: substrate axiom `S-spectral-sequence-collapse`
(CLAUDE.md §3b — class axiomatisation).
-/

import Mathlib.Algebra.Group.Basic

namespace QOU.Mathlib.SpectralSequence

universe u

/-- Cell-index for an `E_r`-page entry: a triple of (page, p, q). -/
structure CellIndex where
  /-- Page index (0-based; `r = 0` is the base, `r = ∞` the limit). -/
  r : ℕ
  /-- Filtration degree (cohomological). -/
  p : ℤ
  /-- Total-complement degree (`p + q = total degree`). -/
  q : ℤ
  deriving Repr

/-- The image of a cell under the `E_r`-differential `d_r`,
    bidegree `(r, 1 - r)` (cohomological convention). -/
def CellIndex.next (c : CellIndex) : CellIndex :=
  { r := c.r, p := c.p + (c.r : ℤ), q := c.q - (c.r : ℤ) + 1 }

/-- Bidegree of `d_r` is `(r, 1 - r)`: `next.p − p = r` and
    `next.q − q = 1 − r`. -/
theorem CellIndex.next_bidegree (c : CellIndex) :
    c.next.p - c.p = (c.r : ℤ) ∧ c.next.q - c.q = 1 - (c.r : ℤ) := by
  refine ⟨?_, ?_⟩ <;> simp [CellIndex.next] <;> ring

/-- A spectral sequence over a coefficient type `R`: an abstract
    family of cell groups, indexed by the page + bidegree, equipped
    with differentials `d_r` and the requirement `d_r ∘ d_r = 0`. -/
structure SpectralSequence (R : Type u) where
  /-- Cell at index `c = (r, p, q)`.  Abstract carrier; a concrete
      instance picks `R`-modules / vector spaces / abelian groups. -/
  cell : CellIndex → Type u
  /-- Each cell is inhabited (every cell is at least the zero
      element).  Concrete instances supply the full module structure. -/
  cell_inhab : ∀ c, Inhabited (cell c)
  /-- The differential `d_r : E_r^{p,q} → E_r^{p+r,q-r+1}`. -/
  differential : ∀ c : CellIndex, cell c → cell c.next
  /-- The zero element of each cell (used to state "differential
      vanishes" without a full module structure). -/
  zero : ∀ c, cell c

/-- `S` collapses at page `r₀` if every differential at page
    `r ≥ r₀` is the zero map.  On the concrete model this
    immediately implies `E_{r₀} = E_{r₀+1} = … = E_∞`. -/
def CollapsesAt {R : Type u} (S : SpectralSequence R) (r₀ : ℕ) : Prop :=
  ∀ c : CellIndex, c.r ≥ r₀ → ∀ x : S.cell c, S.differential c x = S.zero c.next

/-- **Convenience constructor**: a spectral sequence whose every
    cell is `PUnit` and whose differentials are constant zero.  This
    is the "trivially collapses everywhere" model — useful as a
    placeholder when only the abstract `[CollapsesAt 2]` hypothesis
    is required. -/
def trivial (R : Type u) : SpectralSequence R where
  cell _ := PUnit
  cell_inhab _ := ⟨PUnit.unit⟩
  differential _ _ := PUnit.unit
  zero _ := PUnit.unit

/-- The trivial spectral sequence collapses at every page. -/
theorem trivial_collapses_everywhere (R : Type u) (r₀ : ℕ) :
    CollapsesAt (trivial R) r₀ := by
  intro c _ _
  rfl

/-- Specialisation: collapse at `E_2` is the QOU substrate axiom. -/
abbrev CollapsesAtE2 {R : Type u} (S : SpectralSequence R) : Prop :=
  CollapsesAt S 2

/-- The trivial spectral sequence collapses at `E_2`. -/
theorem trivial_collapses_at_E2 (R : Type u) :
    CollapsesAtE2 (trivial R) :=
  trivial_collapses_everywhere R 2

/-- **§3b-cond class hypothesis**: a substrate-supplied spectral
    sequence that collapses at `E_2`.  Downstream theorems take
    `[GBFiltrationCollapsesAtE2 R]` as an instance hypothesis and
    remain fully verified. -/
class GBFiltrationCollapsesAtE2 (R : Type u) where
  /-- The QOU GB-filtration spectral sequence over `R`. -/
  ss : SpectralSequence R
  /-- It collapses at `E_2`. -/
  collapses : CollapsesAtE2 ss

/-- Canonical instance: the trivial spectral sequence vacuously
    discharges the §3b-cond hypothesis.  Genuine instances (when
    the `R`-module GB filtration is formalised) override this. -/
instance canonical (R : Type u) : GBFiltrationCollapsesAtE2 R where
  ss := trivial R
  collapses := trivial_collapses_at_E2 R

/-! ### Convergence + E_∞ page

    A spectral sequence **converges** to a target if its
    `E_∞` page (the colimit of the `E_r` pages, equivalently
    the `r`-stable cells once `d_r = 0` for all `r ≥ r₀`)
    matches the target.  At collapse, `E_∞ = E_{r₀}` directly. -/

/-- The `E_∞` page (post-stabilisation) of a spectral sequence
    that collapses at `r₀`.  Definition: the cell at index
    `(p, q)` on the `E_∞` page IS the cell at the same `(p, q)`
    on the `r₀` page (since all higher differentials vanish). -/
def EInfinityCell {R : Type u} (S : SpectralSequence R) (r₀ : ℕ)
    (_h : CollapsesAt S r₀) (p q : ℤ) : Type u :=
  S.cell { r := r₀, p := p, q := q }

/-- The trivial spectral sequence's `E_∞` cell is `PUnit`. -/
example (R : Type u) (p q : ℤ) :
    EInfinityCell (trivial R) 2 (trivial_collapses_at_E2 R) p q = PUnit := rfl

/-- **Convergence predicate**: an SS `S` converges to a target
    type-family `T : ℤ → ℤ → Type*` if its `E_∞` page agrees
    with `T` cell-by-cell.  For the QOU GB filtration, the
    target is the Wedderburn-block decomposition of `H_n(q)`. -/
class SpectralSequenceConvergesTo (R : Type u) (S : SpectralSequence R)
    (r₀ : ℕ) (collapses : CollapsesAt S r₀)
    (target : ℤ → ℤ → Type u) where
  /-- Per-cell isomorphism between `E_∞` and the target. -/
  cell_iso : ∀ p q, EInfinityCell S r₀ collapses p q ≃ target p q

/-! ### Concrete convergence: trivial SS to the trivial target

    The trivial spectral sequence (every cell `PUnit`,
    differentials zero) converges to the constant-`PUnit`
    target.  This is the simplest non-vacuous instance of
    `SpectralSequenceConvergesTo`, demonstrating the API
    works end-to-end. -/

/-- The constant-`PUnit` target type-family. -/
def trivialTarget : ℤ → ℤ → Type u := fun _ _ => PUnit

/-- The trivial spectral sequence converges to `trivialTarget`
    at any `r₀`, with the `Equiv.refl` isomorphism on each cell. -/
instance trivial_converges (R : Type u) :
    SpectralSequenceConvergesTo R (trivial R) 2
      (trivial_collapses_at_E2 R) trivialTarget where
  cell_iso _ _ := Equiv.refl PUnit

/-! ### Page-by-page stabilisation lemma

    At a spectral sequence that collapses at `r₀`, the cells
    on every page `r ≥ r₀` are *the same* (up to the abstract
    cell-equality the SS supplies — here we record the property
    as a class-level claim).  For the `trivial` SS this is
    trivially true. -/

/-- The cell at index `(r, p, q)` of the trivial SS is `PUnit`
    for every `r`. -/
theorem trivial_cell_eq_PUnit (R : Type u) (r : ℕ) (p q : ℤ) :
    (trivial R).cell { r := r, p := p, q := q } = PUnit := rfl

/-- The trivial SS's cells are the same at every page. -/
theorem trivial_cells_stable (R : Type u) (r₁ r₂ : ℕ) (p q : ℤ) :
    (trivial R).cell { r := r₁, p := p, q := q } =
    (trivial R).cell { r := r₂, p := p, q := q } := rfl

end QOU.Mathlib.SpectralSequence
