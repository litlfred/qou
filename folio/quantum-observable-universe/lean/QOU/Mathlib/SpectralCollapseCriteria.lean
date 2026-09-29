import QOU.Mathlib.BarGradedCollapse
import QOU.QuantumObservableUniverse.SelfDualSES
import Mathlib.Tactic

/-!
# QOU.Mathlib.SpectralCollapseCriteria — collapse you can check, and a legacy bridge

Bean `qou-fngs`. The spectral-sequence arc had reached an honest impasse worth
naming: **the machinery is proved and nothing instantiates it.** An audit on
2026-08-24 found fifteen classes across the corpus asserting a spectral or
collapse property with **zero instances** between them, and `PagedSS` itself
deliberately shipped without a witness.

Zero instances is better than a trivial one — nothing false is proved — but it
also means nothing is proved. Two things are missing, and this file supplies
both.

## 1. Parity checked on one side instead of two

`BarGradedCollapse.collapses_of_parity_mismatch` proves collapse from a
grading, but demands the source be *purely even* **and** the target *purely
odd* — two independent claims about every element of every page.

The content here is `isAntiSelfDual_image_of_selfDual`: if the differential
**anticommutes** with an involution, `⋆ ∘ d = − d ∘ ⋆`, then evenness of the
source *implies* oddness of the image. Anticommutation is a property of a map,
testable on generators; so the parity obligation drops from two sides to one
side plus a map identity.

Be clear about what that is and is not. It is bookkeeping, not a weakening of
the mathematics: `collapses_of_anticommuting_involution` still needs a parity
hypothesis on the target, and with both sides even the statement reduces to
`d = −d`, which is 2-torsion-freeness doing the work. The gain is that one of
the two page-wide hypotheses is replaced by a check on `d`.

The involution the corpus already has is the bar involution `q ↦ q⁻¹`, and
`SelfDualSES` records that its even/odd parts are the `±1` eigenspaces of an
involution — the same structure as `⋆_q`. So this is applicable, in principle,
to the object the substrate axiom is about.

## 2. A bridge, so the legacy hypothesis can be discharged honestly

`SpectralSequence.GBFiltrationCollapsesAtE2` was an `instance` until it was
demoted (`collapse_is_definitional`), because a `PUnit` model satisfied it and
made every downstream theorem unconditional. Demoting it stopped the laundering
but left `canonicalTrivial` as the *only* way to supply it — so a real
filtration had no route in.

`legacyOfPaged` is that route: a `PagedSS` with `Collapses` yields the legacy
class. Downstream consumers of `[GBFiltrationCollapsesAtE2 R]` are unchanged,
and a reader can now tell a genuine discharge from a decorative one by which
constructor was used.

## What this still does not do

It does not construct the Gröbner-filtration spectral sequence, and it does not
verify the anticommutation hypothesis for it. It converts "assume it collapses"
into "exhibit an anticommuting involution", which is a smaller and *checkable*
obligation — not a discharged one. Saying otherwise would repeat the defect
this file exists downstream of.

-- Ref: [manuscript] quantum-observable-universe/eightfold-way
-/

namespace QOU.Mathlib.SpectralCollapseCriteria

open QOU.Mathlib.SpectralSequence QOU.Mathlib.PagedSpectralSequence
open QOU.SelfDualSES

universe u v

variable {R : Type u} [CommRing R] {page : CellIndex → Type v}
    [∀ c, AddCommGroup (page c)] [∀ c, Module R (page c)]

/-- **Anticommutation turns evenness of the source into oddness of the image.**

    This is the reusable content of the file: `⋆(d x) = −d(⋆x)`, so if `x` is
    fixed by the source involution then `d x` is negated by the target's. One
    page-wide parity hypothesis is thereby replaced by a check on the map. -/
theorem isAntiSelfDual_image_of_selfDual
    {M N : Type v} [AddCommGroup M] [Module R M] [AddCommGroup N] [Module R N]
    {iM : Involution R M} {iN : Involution R N} {d : M →ₗ[R] N}
    (hanti : ∀ x, iN.star (d x) = -d (iM.star x))
    {x : M} (hx : IsSelfDual iM x) :
    IsAntiSelfDual iN (d x) := by
  show iN.star (d x) = -d x
  rw [hanti x, hx]

/-- **The vanishing criterion.**

    A differential that anticommutes with an involution, from a purely
    self-dual page to a purely self-dual page, is zero.

    No sleight of hand: with both sides fixed the two facts are `d x = ⋆(d x)`
    and `⋆(d x) = −d x`, so `d x = −d x` and 2-torsion-freeness finishes. The
    honest description is that anticommutation supplies the *second* of the two
    parity facts `BarGradedCollapse.map_eq_zero_of_parity_mismatch` demands as
    a hypothesis. -/
theorem eq_zero_of_anticommuting_involution
    {M N : Type v} [AddCommGroup M] [Module R M] [AddCommGroup N] [Module R N]
    (iM : Involution R M) (iN : Involution R N) (d : M →ₗ[R] N)
    (hanti : ∀ x, iN.star (d x) = -d (iM.star x))
    (hfixM : ∀ x, iM.star x = x)
    (hfixN : ∀ y : N, iN.star y = y)
    (htors : ∀ y : N, y + y = 0 → y = 0) :
    d = 0 := by
  ext x
  refine eq_zero_of_selfDual_and_antiSelfDual iN (hfixN _) ?_ htors
  exact isAntiSelfDual_image_of_selfDual hanti (hfixM x)

/-- **Collapse from an anticommuting involution.**

    A `PagedSS` whose pages carry involutions, whose differentials anticommute
    with them, and whose pages from `r₀` on are pointwise fixed, collapses at
    `r₀`.

    The "pointwise fixed" hypothesis is what remains to be verified for the
    Gröbner filtration; it is stated as a hypothesis rather than assumed,
    which is the whole difference between this and `GBFiltrationCollapsesAtE2`. -/
theorem collapses_of_anticommuting_involution
    (S : PagedSS R page) (r₀ : ℕ)
    (i : ∀ c, Involution R (page c))
    (hanti : ∀ c x, (i (CellIndex.next c)).star (S.d c x) = -S.d c ((i c).star x))
    (hfix : ∀ c, ∀ x : page c, (i c).star x = x)
    (htors : ∀ c, ∀ y : page c, y + y = 0 → y = 0) :
    Collapses S r₀ := by
  intro c _
  exact eq_zero_of_anticommuting_involution (i c) (i (CellIndex.next c)) (S.d c)
    (hanti c) (hfix c) (hfix _) (htors _)

/-- **The payoff**: such a spectral sequence stabilises from `r₀` on. -/
theorem page_stabilises_of_anticommuting_involution
    (S : PagedSS R page) (r₀ : ℕ)
    (i : ∀ c, Involution R (page c))
    (hanti : ∀ c x, (i (CellIndex.next c)).star (S.d c x) = -S.d c ((i c).star x))
    (hfix : ∀ c, ∀ x : page c, (i c).star x = x)
    (htors : ∀ c, ∀ y : page c, y + y = 0 → y = 0)
    (c : CellIndex) (hc : r₀ ≤ c.r) :
    Nonempty (page (CellIndex.bump c) ≃ₗ[R] page c) :=
  page_stabilises_of_collapse S r₀
    (collapses_of_anticommuting_involution S r₀ i hanti hfix htors) c hc

/-! ### Collapse from bounded support — no Gröbner input required -/

/-- **Bounded support forces collapse.**

    If every page vanishes outside the filtration window `0 ≤ p ≤ N`, the
    spectral sequence collapses at `N + 1`.

    The argument is the standard one and it uses no property of the filtration
    beyond its width. `d_r` shifts `p` by `r`, so once `r > N` the differential
    out of any surviving cell lands at `p + r > N`, outside the window, where
    the target is zero. Cells already outside the window have zero *source*.
    Either way the map is zero.

    **This is the theorem the corpus's mass formula actually needs.**
    `prop:phi-q-categorical-truncation` states that the brane-tower sum
    truncates at `k⋆`, the maximum GB-depth among the support partitions, and
    that "truncation at any deeper level yields the identical categorical
    value" — a boundedness claim. Boundedness is weaker than
    `S-GB-spectral-collapse` and, as this shows, it is *provable* rather than
    assumed.

    What it does **not** give is collapse at `E_2` specifically: it yields
    collapse at `N + 1`, where `N` is the window width. The mass formula needs
    `k⋆` to be the max GB-depth rather than something larger, so the strong
    form is still an assertion. Do not read this as discharging it. -/
theorem collapses_of_bounded_support (S : PagedSS R page) (N : ℕ)
    (hzero : ∀ c : CellIndex, (c.p < 0 ∨ (N : ℤ) < c.p) → Subsingleton (page c)) :
    Collapses S (N + 1) := by
  intro c hc
  by_cases hout : c.p < 0 ∨ (N : ℤ) < c.p
  · -- outside the window: the source is zero
    haveI := hzero c hout
    ext x
    -- the SOURCE is zero, so `x = 0` and the map sends it to `0`
    rw [Subsingleton.elim x 0, map_zero]
    simp
  · -- inside the window: `p + r` leaves it, so the target is zero
    push_neg at hout
    obtain ⟨hlo, hhi⟩ := hout
    have hr : (N : ℤ) + 1 ≤ (c.r : ℤ) := by exact_mod_cast hc
    have htarget : (N : ℤ) < (CellIndex.next c).p := by
      show (N : ℤ) < c.p + (c.r : ℤ)
      omega
    haveI := hzero (CellIndex.next c) (Or.inr htarget)
    ext x
    exact Subsingleton.elim _ _

/-- The legacy class, discharged from **boundedness alone** when the window is
    narrow enough to put collapse at `E_2` — that is, `N ≤ 1`.

    Narrow, but not empty, and it is the first discharge of
    `GBFiltrationCollapsesAtE2` in this corpus that is neither `PUnit` nor an
    assumption. -/
theorem collapses_two_of_bounded_support (S : PagedSS R page) (N : ℕ) (hN : N ≤ 1)
    (hzero : ∀ c : CellIndex, (c.p < 0 ∨ (N : ℤ) < c.p) → Subsingleton (page c)) :
    Collapses S 2 := by
  intro c hc
  exact collapses_of_bounded_support S N hzero c (by omega)

/-! ### The legacy bridge

    Restricted to `page : CellIndex → Type u`: the old `SpectralSequence R`
    declares `cell : CellIndex → Type u` in `R`'s own universe, so a page
    family at an independent level `v` cannot be presented in it at all. -/

section Legacy

variable {pageU : CellIndex → Type u}
    [∀ c, AddCommGroup (pageU c)] [∀ c, Module R (pageU c)]

/-- A `PagedSS` presented in the old `SpectralSequence` shape.

    The old API carries no module structure — a cell is a bare type with a
    nominated `zero` element — so this forgets structure rather than adding
    any. It exists so that a *real* spectral sequence can reach the downstream
    theorems that were written against the old class. -/
def toLegacy (S : PagedSS R pageU) : SpectralSequence R where
  cell c := ULift.{u} (pageU c)
  cell_inhab _ := ⟨⟨0⟩⟩
  differential c x := ⟨S.d c x.down⟩
  zero _ := ⟨0⟩

/-- Collapse transfers to the legacy predicate. -/
theorem toLegacy_collapsesAt (S : PagedSS R pageU) (r₀ : ℕ) (h : Collapses S r₀) :
    CollapsesAt (toLegacy S) r₀ := by
  intro c hc x
  show (⟨S.d c x.down⟩ : ULift _) = ⟨0⟩
  rw [h c hc]
  rfl

/-- **The honest discharge.** A real `PagedSS` collapsing at `E_2` supplies
    `GBFiltrationCollapsesAtE2` — the hypothesis downstream theorems take.

    Compare `canonicalTrivial`, which supplies the same class from `PUnit`.
    Both are `def`s and neither is an instance, so a reader of a downstream
    theorem can see which was used; the point of this one is that there is now
    something to see. -/
def legacyOfPaged (S : PagedSS R pageU) (h : Collapses S 2) :
    GBFiltrationCollapsesAtE2 R where
  ss := toLegacy S
  collapses := toLegacy_collapsesAt S 2 h

end Legacy

end QOU.Mathlib.SpectralCollapseCriteria
