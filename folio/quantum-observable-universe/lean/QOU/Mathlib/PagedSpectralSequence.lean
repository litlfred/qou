import QOU.Mathlib.SpectralSequence
import Mathlib.LinearAlgebra.Quotient.Basic
import Mathlib.Tactic

/-!
# QOU.Mathlib.PagedSpectralSequence — collapse that actually says something

Bean `qou-fngs`. `QOU/Mathlib/SpectralSequence.lean` has an `E_r`-page API whose
`CollapsesAt` predicate is weaker than its name, in two ways that file now
exhibits rather than asserts:

* `zero : ∀ c, cell c` is a **marked element**, not an additive zero, so
  `CollapsesAt` is satisfied by any constant differential —
  `constTrue_collapses` with `constTrue_differential_is_true`;
* there is **no page-turning law**, so pages at different `r` are unrelated
  types and `EInfinityCell` *defines* `E_∞` to be the `r₀` page —
  `eInfinity_eq_page_is_rfl` proves that equation by `rfl`, for any spectral
  sequence and any collapse proof.

This module supplies the missing structure. The three things the old API lacks
are exactly the three things a spectral sequence is:

1. **pages are `R`-modules**, so "the differential is zero" means the zero map
   rather than "equals a nominated element";
2. **`d ∘ d = 0`**, without which `ker ⊇ im` fails and the page quotient is not
   even well-posed;
3. **page-turning**, `E_{r+1} ≅ ker d_r ⧸ im d_r`, which is what makes the
   pages a *sequence* rather than an indexed family of unrelated objects.

With those, `page_stabilises_of_collapse` is a **theorem**: if every
differential from page `r₀` on is zero, the next page is isomorphic to this
one. In the old API the corresponding statement was `rfl`.

## Nothing here needed missing infrastructure

`LinearMap.ker`, `LinearMap.range`, `Submodule.comap` and module quotients are
all in Mathlib. It is the *general* spectral-sequence theory that is absent
(bean `qou-pan0`) — the minimal honest version is not. An earlier assessment on
this branch called this blocked on Mathlib; that was too pessimistic and is
corrected here.

## What this still does not do

It does not construct the Gröbner-filtration spectral sequence, which is the
whole content of the substrate axiom `S-GB-spectral-collapse`. It makes the
*claim* expressible: a real instance must supply modules, a differential
squaring to zero, and the page-turning isomorphism, none of which a `PUnit`
model can fake.

-- Ref: [leitner2026] quantum-observable-universe/eightfold-way
-/

namespace QOU.Mathlib.PagedSpectralSequence

open QOU.Mathlib.SpectralSequence

universe u v

/-- Source of the differential landing in `c`: `d_r : E_r^{p-r,q+r-1} → E_r^{p,q}`.
    Inverse to `CellIndex.next`. -/
def CellIndex.prev (c : CellIndex) : CellIndex :=
  { r := c.r, p := c.p - (c.r : ℤ), q := c.q + (c.r : ℤ) - 1 }

/-- The same bidegree on the next page. -/
def CellIndex.bump (c : CellIndex) : CellIndex :=
  { r := c.r + 1, p := c.p, q := c.q }

@[simp] theorem prev_r (c : CellIndex) : (CellIndex.prev c).r = c.r := rfl

@[simp] theorem bump_r (c : CellIndex) : (CellIndex.bump c).r = c.r + 1 := rfl

/-- `next ∘ prev = id`. Holds by arithmetic on `ℤ`, **not** by `rfl` — which is
    why the incoming differential needs the transport below rather than
    type-checking directly. -/
theorem next_prev (c : CellIndex) : CellIndex.next (CellIndex.prev c) = c := by
  obtain ⟨r, p, q⟩ := c
  have h1 : p - (r : ℤ) + (r : ℤ) = p := by ring
  have h2 : q + (r : ℤ) - 1 - (r : ℤ) + 1 = q := by ring
  simp [CellIndex.next, CellIndex.prev, h1, h2]

/-- Transport a page along an equality of cell indices. -/
def reindex {R : Type u} [CommRing R] {page : CellIndex → Type v}
    [∀ c, AddCommGroup (page c)] [∀ c, Module R (page c)] {c₁ c₂ : CellIndex}
    (h : c₁ = c₂) : page c₁ ≃ₗ[R] page c₂ := by
  subst h; exact LinearEquiv.refl R _

/-- The subobject of `ker d_c` cut out by the image of the incoming
    differential. Well-formed whether or not `im ⊆ ker`; `d_comp_d` is what
    makes it the intended quotient. -/
def incoming {R : Type u} [CommRing R] {page : CellIndex → Type v}
    [∀ c, AddCommGroup (page c)] [∀ c, Module R (page c)]
    (d : ∀ c, page c →ₗ[R] page (CellIndex.next c)) (c : CellIndex) :
    Submodule R (LinearMap.ker (d c)) :=
  Submodule.comap (LinearMap.ker (d c)).subtype
    (LinearMap.range
      ((reindex (R := R) (page := page) (next_prev c)).toLinearMap.comp
        (d (CellIndex.prev c))))

/-- **A spectral sequence with the laws that make collapse mean something.**

    Pages are `R`-modules; the differential is `R`-linear and squares to zero;
    and `turn` is the page-turning isomorphism `E_{r+1} ≅ ker d_r ⧸ im d_r`.

    The `page` family and its module structure are *parameters* rather than
    fields, which keeps the laws free of the `@`-instance gymnastics that
    bundling would force. -/
structure PagedSS (R : Type u) [CommRing R] (page : CellIndex → Type v)
    [∀ c, AddCommGroup (page c)] [∀ c, Module R (page c)] where
  /-- The differential `d_r : E_r^{p,q} → E_r^{p+r,q-r+1}`. -/
  d : ∀ c, page c →ₗ[R] page (CellIndex.next c)
  /-- `d ∘ d = 0`. Absent from the old API, and without it the page quotient
      below is not well-posed. -/
  d_comp_d : ∀ c, (d (CellIndex.next c)).comp (d c) = 0
  /-- **Page-turning**: `E_{r+1}^{p,q} ≅ ker d_r ⧸ im d_r`. This is the law
      that makes the pages a sequence. -/
  turn : ∀ c, page (CellIndex.bump c) ≃ₗ[R]
    (LinearMap.ker (d c)) ⧸ incoming d c

variable {R : Type u} [CommRing R] {page : CellIndex → Type v}
    [∀ c, AddCommGroup (page c)] [∀ c, Module R (page c)]

/-- Collapse at `r₀`: every differential from page `r₀` on is the **zero map**
    — not "equals a nominated element". -/
def Collapses (S : PagedSS R page) (r₀ : ℕ) : Prop :=
  ∀ c : CellIndex, r₀ ≤ c.r → S.d c = 0

/-- **The theorem the old API could not state.**

    If `S` collapses at `r₀` then at every cell of page `r ≥ r₀` the next page
    is isomorphic to this one. In `QOU/Mathlib/SpectralSequence.lean` the
    corresponding claim was `eInfinity_eq_page_is_rfl` — true by definition,
    for every spectral sequence, collapsing or not.

    The proof is the content of collapse: `d_c = 0` makes the kernel
    everything, and `d_{prev c} = 0` makes the incoming image nothing, so the
    quotient is the page itself. -/
theorem page_stabilises_of_collapse (S : PagedSS R page) (r₀ : ℕ)
    (hcol : Collapses S r₀) (c : CellIndex) (hc : r₀ ≤ c.r) :
    Nonempty (page (CellIndex.bump c) ≃ₗ[R] page c) := by
  have hd : S.d c = 0 := hcol c hc
  have hprev : S.d (CellIndex.prev c) = 0 := hcol _ (by simpa using hc)
  have hker : LinearMap.ker (S.d c) = ⊤ := by rw [hd]; exact LinearMap.ker_zero
  have him : incoming S.d c = ⊥ := by
    simp only [incoming, hprev, LinearMap.comp_zero, LinearMap.range_zero,
      Submodule.comap_bot, Submodule.ker_subtype]
  exact ⟨(S.turn c).trans ((Submodule.quotEquivOfEqBot _ him).trans
    ((LinearEquiv.ofEq _ _ hker).trans Submodule.topEquiv))⟩

/-! ### No trivial witness is shipped, deliberately

    The structure is inhabitable — take every page to be the zero module, `d`
    the zero map, and `turn` the unique isomorphism between zero modules. That
    is *not* provided as a named `def` here.

    The reason is the defect this file exists to repair. In
    `QOU/Mathlib/SpectralSequence.lean` a trivial witness was reachable, first
    by `inferInstance` and then by name, and it was cited as though the
    substrate axiom had been discharged. A named trivial model is a thing
    downstream code reaches for; leaving it unnamed costs a genuine instance
    nothing (it supplies its own modules) and costs a decorative one the two
    lines it would have leaned on.

    What a real instance must supply, and what no `PUnit` model can fake:
    module structure on every page, an `R`-**linear** differential squaring to
    zero, and an isomorphism onto the actual subquotient. -/

end QOU.Mathlib.PagedSpectralSequence
