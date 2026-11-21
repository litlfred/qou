import QOU.Basic
import QOU.BraidKnot.HeckeAnyonicSubstrate
import QOU.BraidKnot.CrystalGraphRealization

/-!
# QOU.BraidKnot.KazhdanLusztigClassicalLimit — q → 1 classical limit (conjecture)

Class axiomatisation of the *statistics* half of
[conj:kazhdan-lusztig-classical-limit].

**What the narrative conjecture claims — three things:** as `q → 1` the KLR
canonical basis `{b_w}` of `H_n(R, q)` flattens to the Kazhdan–Lusztig basis
`{C_w}` of `ℤ[S_n]`; the resulting classical-limit functor is monoidal; and it
is compatible with the observation functor `τ`.

**What the class below states — one of them, weakly.** `kl_compatible_with_tau`
says that at `q = 1` a phase is `±1`. That is a consequence one would want
*from* τ-compatibility, not τ-compatibility; `τ` appears nowhere in the class
despite the field's name. Monoidality is not stated — there is no tensor
structure on either side to be monoidal about. And "flattens to the KL basis" is
not stated either: `KLBasisElt` is an arbitrary `Type u` with no
Kazhdan–Lusztig structure, so any type at all satisfies the signature.

This docstring used to assert all three (bean `qou-gmfz`). It now says which one
is carried, so the gap is visible from the top of the file rather than only from
the bean.

**Infrastructure now exists for the missing half.**
`QOU.Mathlib.KazhdanLusztigBasis` supplies `BarInvolution` and `KLBasis` — a
basis indexed by the group, every element bar-invariant — with
`nontrivial_of_klBasis` proving that a module carrying one cannot be trivial,
so `KLBasisElt := PUnit` cannot inhabit it for a nonempty index. All sorry-free.

It is **not** wired in here, and the reason is specific: requiring
`klBasis : KLBasis (Equiv.Perm (Fin n)) R _ _` needs an `n`, and this class
takes only `(R) (q) [HeckeAnyonicSubstrate] [CrystalGraphRealization]` — the
strand count is not in scope. Adding a `KLBasis` over an *unconstrained* index
would tighten the class (bar-invariance and basis structure become real
obligations) without ruling out the trivial model, since `KLBasisElt := PUnit`
still admits the rank-one module `R`. Pinning the index to `S_n` is what makes
the constraint bite, and that is the next step on `qou-gmfz`.

Takes `[HeckeAnyonicSubstrate R q]` and `[CrystalGraphRealization R q]`
as upstream inputs.

LaTeX: `\label{conj:kazhdan-lusztig-classical-limit}`

References:
- Kassel, C. (1995).
- Khovanov, M. & Lauda, A. D. (2009).
- Kashiwara, M. (1991).
- Lecouvey, C. (2007).
-/

namespace QOU.BraidKnot

universe u

/-- **Kazhdan–Lusztig classical limit (conjecture).**

    Encodes the `q → 1` specialisation of the KLR canonical basis to
    the Kazhdan–Lusztig basis of `ℤ[S_n]`, and the compatibility of
    this limit with the observation functor `τ`.  The
    `kl_compatible_with_tau` field is the conjectural input. -/
-- Ref: [kassel1995] Ch. X (Hecke algebras and Markov trace)
--      — Kassel, "Quantum Groups," Springer GTM 155, 1995.
--      DOI: 10.1007/978-1-4612-0783-2
-- Ref: [khovanovlauda2009] Khovanov & Lauda, "A diagrammatic approach to categorification of quantum groups," Repr. Theory 13 (2009), arXiv:0803.4121
-- Ref: [kashiwara1991] Kashiwara, "On crystal bases of the q-analogue of universal enveloping algebras," Duke Math. J. 63 (1991)
-- Ref: [lecouvey2007] Lecouvey, "Combinatorics of crystal graphs for the root systems of types A_n, B_n, C_n, D_n and G_2," Combinatorial Aspect of Integrable Systems (MSJ Memoirs 17, 2007)
class KazhdanLusztigClassicalLimit (R : Type u) [CommRing R] (q : R)
    [H : HeckeAnyonicSubstrate R q]
    [C : CrystalGraphRealization R q] where
  /-- Abstract type of Kazhdan–Lusztig basis elements `C_w ∈ ℤ[S_n]`. -/
  KLBasisElt : Type u
  /-- The `q → 1` classical-limit map `b_w ↦ C_w`. -/
  klMap : H.NormalForm → KLBasisElt
  /-- Statistical phase carried by a KL basis element under the observation
      functor `τ` (bosonic = `+1`, fermionic = `-1`).

      Valued in the **ground ring**, not in `ℤ`. The substrate this sits over
      is anyonic (`HeckeAnyonicSubstrate`), so the phase is generically a root
      of unity in `R`; typing it as `ℤ` and asserting `= ±1` made the
      conjecture true by construction, which is exactly what went wrong below. -/
  statSign : KLBasisElt → R
  /-- **The conjecture itself**: at the classical point `q = 1` the phase
      collapses to `±1` — Bose/Fermi only, no anyonic phase survives the
      limit. Plays the role of `sorry`.

      The `q = 1` hypothesis is load-bearing. Without it the field asserts the
      collapse at every `q`, including the generic anyonic ones where it is
      false, so it could only ever be discharged by a degenerate `statSign`. -/
  kl_compatible_with_tau : q = 1 → ∀ T : H.NormalForm,
    statSign (klMap T) = 1 ∨ statSign (klMap T) = -1

namespace KazhdanLusztigClassicalLimit

/-- Unconditional consequence: every normal form's classical-limit
    statistic is bosonic or fermionic — no exotic statistics survive
    the `q → 1` collapse. -/
-- Ref: [leitner2026] braids-and-knots/kazhdan-lusztig-classical-limit
theorem statSign_klMap_pm_one
    {R : Type u} [CommRing R] {q : R}
    [H : HeckeAnyonicSubstrate R q]
    [C : CrystalGraphRealization R q]
    [K : KazhdanLusztigClassicalLimit R q]
    (hq : q = 1) (T : H.NormalForm) :
    K.statSign (K.klMap T) = 1 ∨ K.statSign (K.klMap T) = -1 :=
  K.kl_compatible_with_tau hq T

/-- **Conditional theorem (squared statistic is `+1`).**

    Conditional on `[KazhdanLusztigClassicalLimit R q]`: the squared
    statistical sign of any classical-limit image is `+1` — i.e. the
    classical limit yields ℤ/2-statistics (bosons/fermions only),
    never higher-order anyonic phases. -/
-- Ref: [leitner2026] braids-and-knots/kazhdan-lusztig-classical-limit
theorem statSign_sq_eq_one
    {R : Type u} [CommRing R] {q : R}
    [H : HeckeAnyonicSubstrate R q]
    [C : CrystalGraphRealization R q]
    [K : KazhdanLusztigClassicalLimit R q]
    (hq : q = 1) (T : H.NormalForm) :
    K.statSign (K.klMap T) * K.statSign (K.klMap T) = 1 := by
  rcases K.kl_compatible_with_tau hq T with h | h
  · rw [h]; ring
  · rw [h]; ring

/-- **The trivial model — a `def`, not an `instance`, and not "faithful".**

    Its docstring said *"Faithful instance. Carries the explicit research-grade
    conjecture as a sorry."* Neither half was true. There is no `sorry`: it sets
    `KLBasisElt := PUnit` and `statSign _ := 1`, so `kl_compatible_with_tau` is
    discharged by `Or.inl rfl` on `1 = 1`. Every classical limit is bosonic
    because there is one basis element and it was declared bosonic. A `sorry`
    would at least be visible to `#print axioms`; this was not.

    As an unconditional `instance` it made `statSign_klMap_pm_one` and
    `statSign_sq_eq_one` unconditional theorems about a one-element KL basis.

    **The class was defective too, and has been repaired.** As written,
    `kl_compatible_with_tau` was `∀ T, statSign (klMap T) = 1 ∨ … = -1` beside a
    sibling field `statSign_pm_one : ∀ b, statSign b = 1 ∨ statSign b = -1`. The
    conjecture was therefore `statSign_pm_one (klMap T)` — derivable in *every*
    instance, degenerate or not, so the class asserted nothing even given real
    data. Verified by substitution: both downstream theorems compile unchanged
    with the sibling in place of the conjectural field.

    The cause was the typing. `statSign` landed in `ℤ`, and `statSign_pm_one`
    then *axiomatised* the very collapse the conjecture claims to establish —
    "only ±1" was true by fiat, leaving no room for an anyonic phase to fail to
    collapse. `statSign` now lands in the ground ring `R`, where a root of unity
    can live, `statSign_pm_one` is gone (it was the conjecture wearing an
    axiom's clothes), and `kl_compatible_with_tau` is guarded by `q = 1`. It now
    says something that can fail: at the classical point the phase is `±1`,
    and away from it nothing is claimed.

    Still not stated by any field, and still owed: that the `q → 1` limit of the
    KLR canonical basis *is* the Kazhdan–Lusztig basis, and that the limit
    functor is monoidal. Those need `τ` and the KL basis as independent data;
    this repair makes the statistics field honest, not the whole conjecture.

    Demoted the same way as `ConfinementGradingCorrespondence.canonical`
    (bean `qou-fngs`). Nothing consumed it: the class has no users outside this
    file. -/
def canonical (R : Type u) [CommRing R] (q : R)
    [H : HeckeAnyonicSubstrate R q]
    [C : CrystalGraphRealization R q] :
    KazhdanLusztigClassicalLimit R q where
  KLBasisElt := PUnit
  klMap _ := PUnit.unit
  statSign _ := 1
  -- Ref: [leitner2026] conj:kazhdan-lusztig-classical-limit (§3b-cond conjectural class;
  --      discharged here by `statSign _ := 1`, not by a `sorry` and not by the conjecture)
  kl_compatible_with_tau _ _ := Or.inl rfl

end KazhdanLusztigClassicalLimit

end QOU.BraidKnot
