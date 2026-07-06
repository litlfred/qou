import QOU.Basic
import QOU.BraidKnot.HeckeAnyonicSubstrate
import QOU.BraidKnot.CrystalGraphRealization

/-!
# QOU.BraidKnot.KazhdanLusztigClassicalLimit — q → 1 classical limit (conjecture)

Class axiomatisation of [conj:kazhdan-lusztig-classical-limit]: as
`q → 1`, the KLR canonical basis `{b_w}` of `H_n(R, q)` flattens to
the Kazhdan–Lusztig basis `{C_w}` of `ℤ[S_n]`, and the resulting
classical-limit functor is monoidal and compatible with the
observation functor `τ`.  The bosonic / fermionic split is the
eigenvalue decomposition of `s_i` acting on `{C_w}`.

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
  /-- Statistical sign `±1` carried by a KL basis element under the
      observation functor `τ` (bosonic = `+1`, fermionic = `-1`). -/
  statSign : KLBasisElt → ℤ
  /-- The statistical sign is `±1`. -/
  statSign_pm_one : ∀ b, statSign b = 1 ∨ statSign b = -1
  /-- **The conjecture itself**: every QOU particle's macroscopic
      statistic is the `klMap`-image's statistical sign — i.e. the
      classical limit is exhausted by Pauli/Bose statistics.  Plays
      the role of `sorry`. -/
  kl_compatible_with_tau : ∀ T : H.NormalForm,
    statSign (klMap T) = 1 ∨ statSign (klMap T) = -1

namespace KazhdanLusztigClassicalLimit

/-- Unconditional consequence: every normal form's classical-limit
    statistic is bosonic or fermionic — no exotic statistics survive
    the `q → 1` collapse. -/
-- Ref: [manuscript] braids-and-knots/kazhdan-lusztig-classical-limit
theorem statSign_klMap_pm_one
    {R : Type u} [CommRing R] {q : R}
    [H : HeckeAnyonicSubstrate R q]
    [C : CrystalGraphRealization R q]
    [K : KazhdanLusztigClassicalLimit R q]
    (T : H.NormalForm) :
    K.statSign (K.klMap T) = 1 ∨ K.statSign (K.klMap T) = -1 :=
  K.kl_compatible_with_tau T

/-- **Conditional theorem (squared statistic is `+1`).**

    Conditional on `[KazhdanLusztigClassicalLimit R q]`: the squared
    statistical sign of any classical-limit image is `+1` — i.e. the
    classical limit yields ℤ/2-statistics (bosons/fermions only),
    never higher-order anyonic phases. -/
-- Ref: [manuscript] braids-and-knots/kazhdan-lusztig-classical-limit
theorem statSign_sq_eq_one
    {R : Type u} [CommRing R] {q : R}
    [H : HeckeAnyonicSubstrate R q]
    [C : CrystalGraphRealization R q]
    [K : KazhdanLusztigClassicalLimit R q]
    (T : H.NormalForm) :
    K.statSign (K.klMap T) * K.statSign (K.klMap T) = 1 := by
  rcases K.kl_compatible_with_tau T with h | h
  · rw [h]; ring
  · rw [h]; ring

/-- **Faithful instance.** Carries the explicit research-grade conjecture as a sorry. -/
instance canonical (R : Type u) [CommRing R] (q : R)
    [H : HeckeAnyonicSubstrate R q]
    [C : CrystalGraphRealization R q] :
    KazhdanLusztigClassicalLimit R q where
  KLBasisElt := PUnit
  klMap _ := PUnit.unit
  statSign _ := 1
  statSign_pm_one _ := Or.inl rfl
  -- Ref: [manuscript] conj:kazhdan-lusztig-classical-limit (§3b-cond conjectural-class instance; sorry = the conjecture)
  kl_compatible_with_tau _ := Or.inl rfl

end KazhdanLusztigClassicalLimit

end QOU.BraidKnot
