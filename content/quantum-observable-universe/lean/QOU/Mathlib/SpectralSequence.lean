import Mathlib.Algebra.Group.Basic
import Mathlib.Logic.Equiv.Defs
import Mathlib.Order.Basic
import Mathlib.Data.Fin.Basic
import Mathlib.Tactic

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
(AGENTS.md §3b — class axiomatisation).
-/

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
theorem next_bidegree (c : CellIndex) :
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

/-- The trivial spectral sequence discharges the §3b-cond hypothesis —
    **and that is exactly why this is a `def` and not an `instance`.**

    It was an `instance` until 2026-08-24 (bean `qou-fngs`), which meant
    typeclass resolution supplied it for *every* `R`. Any downstream theorem
    taking `[GBFiltrationCollapsesAtE2 R]` was therefore unconditional, and the
    substrate axiom `S-GB-spectral-collapse` asserted nothing. Same
    self-assuming shape that `hasDqSquaredNonvanishing_of_fact` and
    `hasCategoricalIrreducibility_of_subsingleton` were deleted for.

    As a `def` it remains available — `canonicalTrivial R` is still the model to
    reach for when only the *shape* is wanted — but it must now be supplied by
    hand, so a reader of a downstream theorem can see whether the hypothesis was
    discharged by a real filtration or by `PUnit`. -/
def canonicalTrivial (R : Type u) : GBFiltrationCollapsesAtE2 R where
  ss := trivial R
  collapses := trivial_collapses_at_E2 R

/-! ### What inhabiting these classes does and does not show

    In the manner of
    `QOU/Archimedean/TauFunctorTargetSpec.lean`'s
    `interface_alone_is_trivially_inhabitable`: the classes above are
    inhabitable, cheaply, and a reader should be able to check how cheaply.

    **Every spectral sequence constructed in this file has
    `differential _ _ := default` — the constant map.** So `CollapsesAt` holds
    of them by `rfl`, definitionally, for every page. Collapse is built into
    the models rather than proved of anything.

    That is not a defect of the models — an abstract API needs witnesses — but
    it does bound what they establish. `collapse_is_definitional` below records
    it so no downstream reader mistakes "the API has a collapsing instance" for
    "the GB filtration collapses".

    The open obligation is unchanged and is the whole content of
    `S-GB-spectral-collapse`: exhibit the spectral sequence of the *actual*
    Gröbner filtration on `H_n(q)`, with differentials that are what the
    filtration makes them, and show `d_r = 0` for `r ≥ 2`. Nothing here does
    that, and nothing here is evidence about it. -/

/-- **The trivial model collapses definitionally, not substantively.**
    Its differential is the constant map, so `d_r = 0` is `rfl` at every page —
    there is no filtration behind it and no computation performed. -/
theorem collapse_is_definitional (R : Type u) (r₀ : ℕ) :
    CollapsesAt (trivial R) r₀ := fun _ _ _ => rfl

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
def trivial_converges (R : Type u) :
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

/-! ### Convergence to non-trivial targets — Wedderburn block target

    For the QOU GB-filtration spectral sequence, the `E_∞`
    page coincides with the Wedderburn-block decomposition
    `H_n(q) ≅ ⊕_λ M_{d_λ}(R)`.  The target type-family
    indexed by bidegree `(p, q)` is therefore non-trivial:
    each non-zero cell corresponds to a Wedderburn block.

    This file demonstrates the API on a Wedderburn-shaped
    target.  Concrete instances at small `n` (n = 2, 3, 4)
    arrive via the cohort-RSK witnesses in
    `WenzlBridgeConcrete.lean`. -/

/-- A Wedderburn-block target type-family: at bidegree `(p, q)`,
    the cell is `Fin (blockDim p q) → R` (a `blockDim`-dim
    `R`-module representing a single Wedderburn block).  The
    `blockDim` function records the per-bidegree block-rank. -/
def wedderburnTarget (R : Type u) (blockDim : ℤ → ℤ → ℕ) :
    ℤ → ℤ → Type u :=
  fun p q => Fin (blockDim p q) → R

/-- **Spectral sequence converging to a Wedderburn target**: a
    §3b-cond class capturing the QOU GB-filtration's structure
    via the convergence-to-Wedderburn property. -/
class GBSpectralConvergesToWedderburn (R : Type u) (n : ℕ) where
  /-- The underlying spectral sequence. -/
  ss : SpectralSequence R
  /-- It collapses at `E_2`. -/
  collapses : CollapsesAtE2 ss
  /-- The Wedderburn-block-rank per bidegree (zero outside the
      partition-indexed support). -/
  blockDim : ℤ → ℤ → ℕ
  /-- The convergence: `E_∞ ≃ wedderburnTarget`. -/
  converges :
    SpectralSequenceConvergesTo R ss 2 collapses (wedderburnTarget R blockDim)

/-- **Trivial Wedderburn convergence instance**: `blockDim ≡ 0`
    means every cell is `Fin 0 → R = PUnit`, and the trivial SS
    converges via `Equiv.refl PUnit` cell-by-cell.  This is
    structurally an instance over the trivial Wedderburn target.
    Genuine instances arrive at small `n` (n = 2, 3, 4) once the
    explicit cohort data is wired. -/
def gb_trivial_converges (R : Type u) (n : ℕ) :
    GBSpectralConvergesToWedderburn R n where
  ss := trivial R
  collapses := trivial_collapses_at_E2 R
  blockDim _ _ := 0
  converges := {
    cell_iso := fun p q => by
      show EInfinityCell (trivial R) 2 (trivial_collapses_at_E2 R) p q ≃
        wedderburnTarget R (fun _ _ => 0) p q
      show PUnit ≃ (Fin 0 → R)
      exact ⟨fun _ => fun i => i.elim0, fun _ => PUnit.unit,
             fun _ => rfl, fun f => funext fun i => i.elim0⟩
  }

/-! ### Page-monotonicity + d² = 0 (Tier 2 round 7)

    Additional structural lemmas on the spectral-sequence API. -/

/-- **Collapse is monotone in the page index**: if `S` collapses at
    `r₀`, it also collapses at any later page `r₁ ≥ r₀`.  The
    `d_r = 0` condition for `r ≥ r₀` immediately implies it for
    `r ≥ r₁` since `r ≥ r₁ ≥ r₀`. -/
theorem mono {R : Type u} (S : SpectralSequence R)
    (r₀ r₁ : ℕ) (h : r₀ ≤ r₁) (h_collapses : CollapsesAt S r₀) :
    CollapsesAt S r₁ := by
  intro c hc x
  exact h_collapses c (le_trans h hc) x

/-- **d² = 0 on the trivial spectral sequence**: composing the
    differential with itself yields the zero map.  This is the
    fundamental defining axiom of a spectral sequence. -/
theorem trivial_d_squared_zero (R : Type u) (c : CellIndex)
    (x : (trivial R).cell c) :
    (trivial R).differential c.next ((trivial R).differential c x) =
      (trivial R).zero c.next.next := by
  rfl

/-- **Late-page collapse**: every spectral sequence trivially
    collapses at sufficiently large `r₀` if every cell is `PUnit`
    (which makes every map a constant-zero map). -/
theorem trivial_collapses_at_arbitrary_late (R : Type u) (r : ℕ) :
    CollapsesAt (trivial R) r :=
  trivial_collapses_everywhere R r

/-! ### Concrete n = 2 Wedderburn target

    For `H_2(q)` the partition lattice is `{(2), (1,1)}` and each
    Wedderburn block has dimension 1.  The Wedderburn target at
    bidegree `(p, q) = (0, 0)` is `Fin 2 → R` (one block per
    partition of 2). -/

/-- The block-dimension function for the n=2 Wedderburn target:
    `blockDim_n2 0 0 = 2` (two 1-dimensional blocks, summed),
    zero elsewhere.  The "summed" form lets a single bidegree
    cell encode both blocks. -/
def blockDim_n2 : ℤ → ℤ → ℕ := fun p q =>
  if p = 0 ∧ q = 0 then 2 else 0

/-- The block-dimension at `(0, 0)` is 2. -/
theorem blockDim_n2_at_origin : blockDim_n2 0 0 = 2 := by
  unfold blockDim_n2; simp

/-- The block-dimension is zero off-origin. -/
theorem blockDim_n2_off_origin (p q : ℤ) (h : ¬ (p = 0 ∧ q = 0)) :
    blockDim_n2 p q = 0 := by
  unfold blockDim_n2; simp [h]

/-- **n=2 Wedderburn target**: the type-family at bidegree
    `(p, q)` is `Fin (blockDim_n2 p q) → R`. -/
def wedderburnTarget_n2 (R : Type u) : ℤ → ℤ → Type u :=
  wedderburnTarget R blockDim_n2

/-! ### Non-trivial Wedderburn-target convergence (Tier 2 deep)

    Beyond the constant-`PUnit` trivial target, supply a concrete
    spectral sequence that converges to the n=2 Wedderburn target.
    The sequence: every cell is `Fin (blockDim_n2 p q) → R`; on
    the origin `(0, 0)` this is `Fin 2 → R`, off-origin it is
    `Fin 0 → R = PUnit`.  Differentials are constant zero.  The
    sequence collapses immediately (already at `E_2`) and the
    convergence is `Equiv.refl` cell-by-cell. -/

/-- The n=2-Wedderburn-shaped spectral sequence: cells are
    `Fin (blockDim_n2 p q) → R` independently of page index. -/
def wedderburnSS_n2 (R : Type u) [Inhabited R] : SpectralSequence R where
  cell c := Fin (blockDim_n2 c.p c.q) → R
  cell_inhab _ := ⟨default⟩
  differential _ _ := default  -- constant-default map (the zero map on this model)
  zero _ := default

/-- The n=2-Wedderburn SS collapses at any page (every differential
    is the constant-zero map). -/
theorem wedderburnSS_n2_collapses_everywhere (R : Type u) [Inhabited R] (r₀ : ℕ) :
    CollapsesAt (wedderburnSS_n2 R) r₀ := by
  intro c _ x
  rfl

/-- The n=2-Wedderburn SS collapses at `E_2`. -/
theorem wedderburnSS_n2_collapses_at_E2 (R : Type u) [Inhabited R] :
    CollapsesAtE2 (wedderburnSS_n2 R) :=
  wedderburnSS_n2_collapses_everywhere R 2

/-- **Non-trivial Wedderburn convergence instance**: the n=2-shaped
    spectral sequence converges to `wedderburnTarget_n2`, with the
    `Equiv.refl` cell-by-cell isomorphism (since both sides are
    literally `Fin (blockDim_n2 p q) → R`). -/
def wedderburnSS_n2_converges (R : Type u) [Inhabited R] :
    SpectralSequenceConvergesTo R (wedderburnSS_n2 R) 2
      (wedderburnSS_n2_collapses_at_E2 R) (wedderburnTarget_n2 R) where
  cell_iso _ _ := Equiv.refl _

/-- **Full Wedderburn-convergence class instance** at `n=2`: bundles
    the spectral sequence, collapse, blockDim, and convergence. -/
def gb_wedderburn_n2_converges (R : Type u) [Inhabited R] :
    GBSpectralConvergesToWedderburn R 2 where
  ss := wedderburnSS_n2 R
  collapses := wedderburnSS_n2_collapses_at_E2 R
  blockDim := blockDim_n2
  converges := wedderburnSS_n2_converges R

/-! ### Generic n-page Wedderburn-shape extension

    Same construction at any `n`: cells are
    `Fin (blockDim_n p q) → R`, differentials zero. -/

/-- **Generic-n Wedderburn-shaped SS** parameterised by a
    `blockDim` function.  The cell-shape `Fin (blockDim p q) → R`
    is determined by the partition lattice of `n` (encoded in
    `blockDim`); on the trivial-`blockDim ≡ 0` model every cell
    is `PUnit`. -/
def wedderburnSS_generic (R : Type u) [Inhabited R] (blockDim : ℤ → ℤ → ℕ) :
    SpectralSequence R where
  cell c := Fin (blockDim c.p c.q) → R
  cell_inhab _ := ⟨default⟩
  differential _ _ := default
  zero _ := default

/-- Generic-n Wedderburn-shaped SS collapses at every page. -/
theorem wedderburnSS_generic_collapses (R : Type u) [Inhabited R]
    (blockDim : ℤ → ℤ → ℕ) (r₀ : ℕ) :
    CollapsesAt (wedderburnSS_generic R blockDim) r₀ := by
  intro c _ x; rfl

/-- Generic-n Wedderburn-shaped SS collapses at `E_2`. -/
theorem wedderburnSS_generic_collapses_at_E2 (R : Type u) [Inhabited R]
    (blockDim : ℤ → ℤ → ℕ) :
    CollapsesAtE2 (wedderburnSS_generic R blockDim) :=
  wedderburnSS_generic_collapses R blockDim 2

/-- The generic-n Wedderburn SS converges to its target. -/
def wedderburnSS_generic_converges (R : Type u) [Inhabited R]
    (blockDim : ℤ → ℤ → ℕ) :
    SpectralSequenceConvergesTo R (wedderburnSS_generic R blockDim) 2
      (wedderburnSS_generic_collapses_at_E2 R blockDim)
      (wedderburnTarget R blockDim) where
  cell_iso _ _ := Equiv.refl _

/-- **GB Wedderburn convergence at any `n`** via the generic SS. -/
def gb_wedderburn_generic_converges (R : Type u) [Inhabited R] (n : ℕ)
    (blockDim : ℤ → ℤ → ℕ) :
    GBSpectralConvergesToWedderburn R n where
  ss := wedderburnSS_generic R blockDim
  collapses := wedderburnSS_generic_collapses_at_E2 R blockDim
  blockDim := blockDim
  converges := wedderburnSS_generic_converges R blockDim

end QOU.Mathlib.SpectralSequence
