import QOU.BraidKnot.KazhdanLusztigClassicalLimit

/-!
# `conj:lusztig-canonical-basis-q-eq-1` — the conditionality is now in the type

Sibling for content block
[`conj:lusztig-canonical-basis-q-eq-1`](lusztig-canonical-basis-q-eq-1.md).

## What this file used to be, and the two things wrong with it

```lean
class LusztigCanonicalBasisQEq1 where
  holds : Prop
```

Two defects, and the second is the one a detector could not see:

1. `⟨True⟩` inhabits it, so it asserted nothing (`qou-hprp`).
2. **The block's title says *"conditional on `conj:kazhdan-lusztig-classical-limit`"*
   and the type said no such thing.** That is the criterion
   `proof-dependent-conjecture-not-conditional` (AGENTS.md §3b-tax): prose declares
   a dependency, the signature does not carry it, and the derived primary/dependent
   graph therefore classified this as a *primary* conjecture — a root — when it is a
   dependent one. The `[KazhdanLusztigClassicalLimit R q]` binder below **is** the
   dependency edge.

## What is assumed

The upstream class already supplies `H.NormalForm`, `KLBasisElt` and the
classical-limit map `klMap : NormalForm → KLBasisElt`. It axiomatises the
*statistics* half of the `q → 1` limit. This block is the *decategorification*
half, so it is stated over those same objects rather than over new ones.

* `klMap_bijective` — at `q = 1` the classical-limit map is a **bijection**. The
  block says the crystal *"decategorifies **to** the Lusztig canonical basis"*: a
  map that missed part of the basis would not be a decategorification onto it, and
  one that collapsed two normal forms would lose the count. Bijectivity is what
  "to" means here, and it is the conjecture.
* `mult_nonneg`, `mult_diag` — the KL structure constants at `q = 1` are
  *"integer multiplicities"*: non-negative, and `1` on the diagonal
  (`P_{w,w} = 1`). Non-negativity is Kazhdan–Lusztig positivity, classical for
  Weyl groups (Elias–Williamson in general); it is cited, not conjectured, and it
  is the same positivity the corpus already leans on in the Option-E PROBE-4 prune.

`mult` is a **parameter**, so the class is a hypothesis about the caller's
structure constants rather than about ones an instance chose for itself.

## What is derived — including one result neither class has alone

`canonicalBasis_statSign_pm_one` is the payoff and the reason the binder earns its
place. Upstream gives `statSign (klMap T) = ±1` for every normal form `T` — i.e. on
the **image** of `klMap`. Surjectivity here extends that to **every** canonical
basis element. Neither class states it; the composite does. That is what a
§3b-cond conditional result is supposed to look like.

Also derived: `klMap` is injective and surjective at `q = 1`, each canonical basis
element has a **unique** normal form over it, and the diagonal multiplicity is
positive.

## What is NOT formalised here, stated rather than implied

- **No Kazhdan–Lusztig polynomials.** `mult` is an abstract `ℤ`-valued function of
  two basis elements standing for `P_{y,w}(1)`. Nothing here constructs `P_{y,w}`,
  Bruhat order, or `ℤ[S_n]`; Mathlib has no KL polynomials.
- **No crystal.** The `q → 0` Kashiwara side of the block's limit-duality square,
  and the `q → ∞` reverse limit, appear nowhere below. Only the `q = 1` vertex is
  stated.
- **"Structure constants" is asserted, not exhibited.** That `mult` *are* the
  structure constants of the decategorification — as opposed to an arbitrary
  non-negative array with unit diagonal — is not stated, because nothing here has a
  product to be structure constants of.
- **The isospin and Type-B folding paragraphs are untouched.**

## References
- [kazhdan-lusztig1979] Kazhdan–Lusztig, "Representations of Coxeter groups and Hecke algebras".
- [lusztig1990] Lusztig, "Canonical bases arising from quantized enveloping algebras".
- [kashiwara1991] Kashiwara, "On crystal bases of the q-analogue of universal enveloping algebras".
-/

set_option autoImplicit false

namespace QOU.BraidsAndKnots

open QOU.BraidKnot

universe u

/-- **Lusztig canonical basis at `q = 1`**, conditional on
`KazhdanLusztigClassicalLimit`.

The `[K : KazhdanLusztigClassicalLimit R q]` binder is the dependency the block's
own title declares and the previous carrier's type did not have. -/
-- Ref: [kazhdan-lusztig1979] Kazhdan, Lusztig, "Representations of Coxeter groups and Hecke algebras"
-- Ref: [lusztig1990] Lusztig, "Canonical bases arising from quantized enveloping algebras"
-- Ref: [leitner2026] conj:lusztig-canonical-basis-q-eq-1
class LusztigCanonicalBasisQEq1 (R : Type u) [CommRing R] (q : R)
    [H : HeckeAnyonicSubstrate R q]
    [C : CrystalGraphRealization R q]
    [K : KazhdanLusztigClassicalLimit R q]
    (mult : K.KLBasisElt → K.KLBasisElt → ℤ) : Prop where
  /-- At `q = 1` the classical-limit map is a bijection: the crystal
      decategorifies *onto* the canonical basis, without collapsing. -/
  klMap_bijective : q = 1 → Function.Bijective K.klMap
  /-- Kazhdan–Lusztig positivity: the multiplicities are non-negative. -/
  mult_nonneg : q = 1 → ∀ y w, 0 ≤ mult y w
  /-- `P_{w,w}(1) = 1`. -/
  mult_diag : q = 1 → ∀ w, mult w w = 1

namespace LusztigCanonicalBasisQEq1

variable {R : Type u} [CommRing R] {q : R}
  [H : HeckeAnyonicSubstrate R q]
  [C : CrystalGraphRealization R q]
  [K : KazhdanLusztigClassicalLimit R q]
  {mult : K.KLBasisElt → K.KLBasisElt → ℤ}

/-- Every canonical basis element comes from exactly one normal form. -/
theorem exists_unique_normalForm [L : LusztigCanonicalBasisQEq1 R q mult]
    (hq : q = 1) (Cw : K.KLBasisElt) :
    ∃! T : H.NormalForm, K.klMap T = Cw := by
  obtain ⟨hinj, hsurj⟩ := L.klMap_bijective hq
  obtain ⟨T, hT⟩ := hsurj Cw
  exact ⟨T, hT, fun T' hT' => hinj (hT'.trans hT.symm)⟩

/-- **The composite result: no exotic statistics anywhere on the canonical basis.**

`KazhdanLusztigClassicalLimit` gives `statSign = ±1` on the *image* of `klMap`.
Surjectivity here carries it to *every* basis element. Neither conjecture states
this on its own. -/
theorem canonicalBasis_statSign_pm_one [L : LusztigCanonicalBasisQEq1 R q mult]
    (hq : q = 1) (Cw : K.KLBasisElt) :
    K.statSign Cw = 1 ∨ K.statSign Cw = -1 := by
  obtain ⟨_, hsurj⟩ := L.klMap_bijective hq
  obtain ⟨T, hT⟩ := hsurj Cw
  -- The upstream conjecture's own consequence, applied at `T`, then transported
  -- along `hT`.
  have := KazhdanLusztigClassicalLimit.statSign_klMap_pm_one hq T
  rwa [hT] at this

/-- The diagonal multiplicity is strictly positive. -/
theorem mult_diag_pos [L : LusztigCanonicalBasisQEq1 R q mult]
    (hq : q = 1) (w : K.KLBasisElt) :
    0 < mult w w := by
  rw [L.mult_diag hq w]; norm_num

end LusztigCanonicalBasisQEq1

end QOU.BraidsAndKnots
