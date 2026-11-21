/-
Copyright (c) 2026 litlfred. All rights reserved.

# The even (C1/mass) face is the faithful classical carrier — and the graded split is canonical

Companion to [`OddDecayWeightParity.lean`](OddDecayWeightParity.lean). That file
proved the **odd** (GGM/decay, sinh, bar-odd) face of the q-cubic graded split
(`qCubicGradedSplit`, PR #4140, bean `qou-jqof`) has a **null** q=1 (classical)
shadow. This file proves the complementary, positive half about the **even**
(C1/mass, cosh, bar-even) face:

1. `evenFace_carries_shadow` — for a split `qCubic = e + o` with `e` bar-EVEN
   (`σ e = e`) and `o` bar-ODD (`σ o = −o`), every bar-compatible evaluation `φ`
   into a characteristic-`≠ 2` field satisfies `φ(qCubic) = φ(e)`: the even face
   carries the entire classical value. (General bar-odd `o` — not only the
   `g·γ` cross-term form of the odd file.)
2. `oddFace_shadow_null` — the same evaluation kills the odd face, `φ(o) = 0`:
   the decay face is classically inert.
3. `parity_decomposition_unique` — **the graded split is canonical.** Over a
   characteristic-`≠ 2` field, if `qCubic = e + o = e' + o'` with `e, e'`
   bar-even and `o, o'` bar-odd, then `e = e'` and `o = o'`. The even/odd
   (mass/decay) decomposition is **unique**, matching the canonical block
   structure of the super-Berezinian split — the classical mass content has a
   single well-defined home.
4. `evenFace_shadow_faithful` — an immediate corollary: the even face's classical
   shadow is independent of the chosen split; it is an invariant of `qCubic`.

Everything reduces to the `QOU.QBeta` bar-parity algebra
(`bar_even_and_odd_two_mul_eq_zero`, `shadow_carried_by_even_part`,
`fixed_eval_two_mul_kills_bar_odd`) — the T3-2 shadow machinery — specialized to
the graded split. No archimedean construct: generic `{R : Type*} [CommRing R]`
with an abstract bar involution `σ : R →+* R`, char-`≠ 2` supplied as `(2 : F) ≠ 0`
on a `Field` target only where cancellation is needed (§7c).

**Honest scope.** Like the odd companion, these are *necessary conditions /
structural facts* about any derivation of the open wall `q_cubic = C1` — the
classical mass content lives on the (uniquely determined) even face — **not** a
derivation of it. No `c_k` value, no registry tier, nothing wired. `qou-jqof`
stays open.

Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-07-25-odd-face-parity-constraint.md
-- Ref: [ramis-sauloy-zhang2013] q-difference formal classification / Stokes
-/
import QOU.QBeta.OddDecayWeightParity

namespace QOU.QBeta.EvenFaceMassShadow

variable {R : Type*} [CommRing R] (σ : R →+* R)

/-- **Bar-evenness of the even/mass (C1) face.** Abbreviation matching the
    bar-even cosh profile: `σ e = e`. The bar-fixed locus is a subring
    (`ZBarParity.bar_fixed_add/mul/pow`), so a C1 kernel assembled from bar-even
    atoms by ring operations stays on this face. -/
def IsEvenFace (e : R) : Prop := σ e = e

/-- **The even face carries the whole classical shadow.** For the graded split
    `qCubic = e + o` with `e` bar-even and `o` bar-odd, every bar-compatible
    evaluation `φ` (`φ ∘ σ = φ`) into a characteristic-`≠ 2` field gives
    `φ(qCubic) = φ(e)`. The nonzero classical mass content is sourced entirely by
    the even (C1/cosh) face. -/
theorem evenFace_carries_shadow {S : Type*} [Field S]
    (φ : R →+* S) (hcomm : φ.comp σ = φ)
    (qCubic e o : R) (hsplit : qCubic = e + o)
    (he : IsEvenFace σ e) (ho : σ o = -o) (h2 : (2 : S) ≠ 0) :
    φ qCubic = φ e :=
  QOU.QBeta.shadow_carried_by_even_part σ φ hcomm qCubic e o hsplit he ho h2

/-- **The odd face is classically inert.** The bar-odd decay face `o` is
    annihilated by every bar-compatible evaluation into a characteristic-`≠ 2`
    field: `φ(o) = 0`. (The `2·φ(o) = 0` division-free form is
    `oddWeight_shadow_zero`.) -/
theorem oddFace_shadow_null {S : Type*} [Field S]
    (φ : R →+* S) (hcomm : φ.comp σ = φ)
    (o : R) (ho : σ o = -o) (h2 : (2 : S) ≠ 0) :
    φ o = 0 := by
  have h := QOU.QBeta.fixed_eval_two_mul_kills_bar_odd σ φ hcomm o ho
  exact (mul_eq_zero.mp h).resolve_left h2

/-- **The graded split is canonical (unique).** Over a characteristic-`≠ 2`
    field `F`, if `qCubic = e + o = e' + o'` with `e, e'` bar-even and `o, o'`
    bar-odd, then `e = e'` and `o = o'`. Proof: the difference `e − e' = o' − o`
    is simultaneously bar-even (LHS) and bar-odd (RHS), hence `2·(e − e') = 0`,
    so `e = e'` in characteristic `≠ 2`; the odd parts then agree by
    cancellation. The even/odd (mass/decay) decomposition of the q-cubic has a
    single well-defined home — the structural counterpart of the super-Berezinian
    block-diagonalization. -/
theorem parity_decomposition_unique {F : Type*} [Field F] (σF : F →+* F)
    (qCubic e o e' o' : F)
    (hsplit : qCubic = e + o) (hsplit' : qCubic = e' + o')
    (he : σF e = e) (ho : σF o = -o) (he' : σF e' = e') (ho' : σF o' = -o')
    (h2 : (2 : F) ≠ 0) :
    e = e' ∧ o = o' := by
  -- The difference d = e − e' equals o' − o.
  have hd : e - e' = o' - o := by
    have hqq : e + o = e' + o' := by rw [← hsplit, hsplit']
    linear_combination hqq
  -- d is bar-even (difference of bar-even) and bar-odd (difference of bar-odd).
  have hd_even : σF (e - e') = e - e' := by rw [map_sub, he, he']
  have hd_odd : σF (e - e') = -(e - e') := by
    rw [hd, map_sub, ho', ho]; ring
  -- Both parities force d = 0 in characteristic ≠ 2.
  have hde : e - e' = 0 :=
    QOU.QBeta.bar_even_ne_bar_odd_of_ne_zero σF (e - e') hd_even hd_odd h2
  have hee : e = e' := by linear_combination hde
  refine ⟨hee, ?_⟩
  -- With the even parts equal, the odd parts agree by cancelling in the split.
  have hoo : e + o = e' + o' := by rw [← hsplit, hsplit']
  rw [hee] at hoo
  linear_combination hoo

/-- **The even face's classical shadow is a split-independent invariant.**
    Corollary of canonicity: if `qCubic = e + o = e' + o'` are two even/odd
    splits over a characteristic-`≠ 2` field, then `φ(e) = φ(e')` for every ring
    hom `φ` — the classical mass value read off the even face does not depend on
    how the split was presented. -/
theorem evenFace_shadow_faithful {F S : Type*} [Field F] [CommRing S]
    (σF : F →+* F) (φ : F →+* S)
    (qCubic e o e' o' : F)
    (hsplit : qCubic = e + o) (hsplit' : qCubic = e' + o')
    (he : σF e = e) (ho : σF o = -o) (he' : σF e' = e') (ho' : σF o' = -o')
    (h2 : (2 : F) ≠ 0) :
    φ e = φ e' := by
  have := parity_decomposition_unique σF qCubic e o e' o'
    hsplit hsplit' he ho he' ho' h2
  rw [this.1]

end QOU.QBeta.EvenFaceMassShadow
