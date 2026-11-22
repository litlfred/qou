import QOU.Hecke.IwahoriHecke
import QOU.SchurWeyl.HeckeAlgebra
import QOU.MassTheory.HeckeSectorRep

/-!
# QOU.Hecke.HeckeModelsBridge — the three presented Hecke models are one algebra

The corpus carries three presentations of the type-`A` Iwahori–Hecke algebra by generators and
relations, each a `RingQuot` of a free algebra:

| model | generators | quadratic relation |
|---|---|---|
| `QOU.Hecke.IwahoriHecke K q n` | `Fin n` | `T² = (q − 1)·T + q` (T-form) |
| `QOU.SchurWeyl.Hecke K q qi n` | `Fin n` | `σ² = (q − qi)·σ + (q·qi)` |
| `QOU.MassTheory.HeckeSectorRep.Hn (n+1) q qi` | `{i // i + 1 < n + 1}` | `σ² = (q − qi)·σ + 1` |
| `QOU.MassTheory.HeckeSectorRep.Hecke q qi` | `ℕ` (all strands) | `σ² = (q − qi)·σ + 1` |

This file proves that they are the same algebra, by explicit `K`-algebra maps.

* `iwahoriEquivQiOne` — `IwahoriHecke K q n ≃ₐ SchurWeyl.Hecke K q 1 n`. The T-form is the
  two-parameter form at `qi = 1`, relation for relation.
* `rescale` / `rescaleEquiv` — for a unit `c`, `σ ↦ c·σ` identifies the two-parameter algebra at
  `(q, qi)` with the one at `(c·q, c·qi)`.
* `iwahoriEquivSigma` — `IwahoriHecke K (s·s) n ≃ₐ SchurWeyl.Hecke K s si n` when `s·si = 1`:
  the T-form at `q_T = s²` is the σ-form at `s`, with `T = s·σ`.
* `sectorEquiv` — `SchurWeyl.Hecke K q qi n ≃ₐ HeckeSectorRep.Hn (n+1) q qi` when `q·qi = 1`.
* `toInfinite` — `SchurWeyl.Hecke K q qi n →ₐ HeckeSectorRep.Hecke q qi`, `σᵢ ↦ σᵢ`, and it is
  `Hn.toHecke ∘ sectorEquiv`.

## What is not claimed

`toInfinite` is not proved injective here. Injectivity of `H_n → H_{n+1}` is
`QOU.SchurWeyl.heckeIncl_injective` (generic `q`); the colimit statement for the `ℕ`-indexed
algebra is not assembled.

The legacy linear-algebra layer `QOU.HeckeAlgebra.HeckeElement n` (a Euclidean space with an
`opaque` multiplication) is not a presentation and has no map to or from these; it is not touched.

## Base ring (§7c)

Generic `[CommRing K]`. No ordering, no `ℝ`.
-/

namespace QOU.Hecke.ModelsBridge

open FreeAlgebra

variable (K : Type*) [CommRing K]

/-! ## 1. T-form is the two-parameter form at `qi = 1` -/

section TForm

variable (q : K) (n : ℕ)

/-- `σᵢ ↦ σᵢ`, from the T-form to the two-parameter form at `qi = 1`. -/
noncomputable def iwahoriToQiOne : IwahoriHecke K q n →ₐ[K] QOU.SchurWeyl.Hecke K q 1 n :=
  RingQuot.liftAlgHom K ⟨FreeAlgebra.lift K (QOU.SchurWeyl.Hecke.σ K q 1 n), by
    intro x y h
    induction h with
    | quadratic i =>
        simp only [map_mul, map_add, map_smul, map_one, FreeAlgebra.lift_ι_apply]
        simpa only [mul_one] using QOU.SchurWeyl.Hecke.σ_quadratic K q 1 n i
    | braid i hi =>
        simp only [map_mul, FreeAlgebra.lift_ι_apply]
        exact QOU.SchurWeyl.Hecke.σ_braid K q 1 n i hi
    | commute i j hij =>
        simp only [map_mul, FreeAlgebra.lift_ι_apply]
        exact QOU.SchurWeyl.Hecke.σ_commute K q 1 n i j hij⟩

/-- `σᵢ ↦ σᵢ`, from the two-parameter form at `qi = 1` back to the T-form. -/
noncomputable def qiOneToIwahori : QOU.SchurWeyl.Hecke K q 1 n →ₐ[K] IwahoriHecke K q n :=
  QOU.SchurWeyl.Hecke.lift K q 1 n (IwahoriHecke.σ K q n)
    (fun i => by simpa only [mul_one] using IwahoriHecke.σ_quadratic K q n i)
    (fun i hi => IwahoriHecke.σ_braid K q n i hi)
    (fun i j hij => IwahoriHecke.σ_commute K q n i j hij)

theorem iwahoriToQiOne_σ (i : Fin n) :
    iwahoriToQiOne K q n (IwahoriHecke.σ K q n i) = QOU.SchurWeyl.Hecke.σ K q 1 n i :=
  (RingQuot.liftAlgHom_mkAlgHom_apply K _ _ (ι K i)).trans (FreeAlgebra.lift_ι_apply _ i)

theorem qiOneToIwahori_σ (i : Fin n) :
    qiOneToIwahori K q n (QOU.SchurWeyl.Hecke.σ K q 1 n i) = IwahoriHecke.σ K q n i :=
  QOU.SchurWeyl.Hecke.lift_σ K q 1 n _ _ _ _ i

/-- Two algebra maps out of the T-form algebra that agree on the generators are equal. -/
theorem iwahori_hom_ext {A : Type*} [Ring A] [Algebra K A]
    {φ ψ : IwahoriHecke K q n →ₐ[K] A}
    (h : ∀ i, φ (IwahoriHecke.σ K q n i) = ψ (IwahoriHecke.σ K q n i)) : φ = ψ := by
  have key : φ.comp (IwahoriHecke.mk K q n) = ψ.comp (IwahoriHecke.mk K q n) := by
    apply FreeAlgebra.hom_ext
    funext i
    simpa only [AlgHom.comp_apply, IwahoriHecke.σ] using h i
  ext z
  obtain ⟨x, rfl⟩ := RingQuot.mkAlgHom_surjective K (QOU.Hecke.HeckeRel K q n) z
  exact AlgHom.congr_fun key x

/-- **The T-form algebra is the two-parameter algebra at `qi = 1`.** -/
noncomputable def iwahoriEquivQiOne :
    IwahoriHecke K q n ≃ₐ[K] QOU.SchurWeyl.Hecke K q 1 n :=
  AlgEquiv.ofAlgHom (iwahoriToQiOne K q n) (qiOneToIwahori K q n)
    (QOU.SchurWeyl.Hecke.hom_ext K q 1 n fun i => by
      simp only [AlgHom.comp_apply, AlgHom.id_apply, qiOneToIwahori_σ, iwahoriToQiOne_σ])
    (iwahori_hom_ext K q n fun i => by
      simp only [AlgHom.comp_apply, AlgHom.id_apply, iwahoriToQiOne_σ, qiOneToIwahori_σ])

end TForm

/-! ## 2. Rescaling the generators -/

section Rescale

variable {K} (n : ℕ)

/-- `σ'ᵢ ↦ c·σᵢ`, from parameters `(q', qi') = (c·q, c·qi)` to `(q, qi)`: if `σ` satisfies the
relations at `(q, qi)`, then `c·σ` satisfies them at `(c·q, c·qi)`. -/
noncomputable def rescale (c q qi q' qi' : K) (hq : q' = c * q) (hqi : qi' = c * qi) :
    QOU.SchurWeyl.Hecke K q' qi' n →ₐ[K] QOU.SchurWeyl.Hecke K q qi n :=
  QOU.SchurWeyl.Hecke.lift K q' qi' n (fun i => c • QOU.SchurWeyl.Hecke.σ K q qi n i)
    (fun i => by
      subst hq hqi
      rw [smul_mul_smul_comm, QOU.SchurWeyl.Hecke.σ_quadratic K q qi n i]
      simp only [smul_add, smul_smul]
      congr 1 <;> congr 1 <;> ring)
    (fun i hi => by
      have h := QOU.SchurWeyl.Hecke.σ_braid K q qi n i hi
      simp only [smul_mul_assoc, mul_smul_comm, smul_smul, h])
    (fun i j hij => by
      have h := QOU.SchurWeyl.Hecke.σ_commute K q qi n i j hij
      simp only [smul_mul_assoc, mul_smul_comm, smul_smul, h])

theorem rescale_σ (c q qi q' qi' : K) (hq : q' = c * q) (hqi : qi' = c * qi) (i : Fin n) :
    rescale n c q qi q' qi' hq hqi (QOU.SchurWeyl.Hecke.σ K q' qi' n i)
      = c • QOU.SchurWeyl.Hecke.σ K q qi n i :=
  QOU.SchurWeyl.Hecke.lift_σ K q' qi' n _ _ _ _ i

/-- **Rescaling by a unit is an isomorphism.** For `c·ci = 1`, the two-parameter algebra at
`(q, qi)` is isomorphic to the one at `(q', qi') = (c·q, c·qi)`, by `σᵢ ↦ ci·σ'ᵢ` (inverse
`σ'ᵢ ↦ c·σᵢ`). -/
noncomputable def rescaleEquiv (c ci q qi q' qi' : K) (hc : c * ci = 1)
    (hq : q' = c * q) (hqi : qi' = c * qi) :
    QOU.SchurWeyl.Hecke K q qi n ≃ₐ[K] QOU.SchurWeyl.Hecke K q' qi' n :=
  have hc' : ci * c = 1 := by rw [mul_comm]; exact hc
  have hq' : q = ci * q' := by rw [hq, ← mul_assoc, hc', one_mul]
  have hqi' : qi = ci * qi' := by rw [hqi, ← mul_assoc, hc', one_mul]
  AlgEquiv.ofAlgHom (rescale n ci q' qi' q qi hq' hqi') (rescale n c q qi q' qi' hq hqi)
    (QOU.SchurWeyl.Hecke.hom_ext K q' qi' n fun i => by
      simp only [AlgHom.comp_apply, AlgHom.id_apply, rescale_σ, map_smul, smul_smul, hc,
        one_smul])
    (QOU.SchurWeyl.Hecke.hom_ext K q qi n fun i => by
      simp only [AlgHom.comp_apply, AlgHom.id_apply, rescale_σ, map_smul, smul_smul, hc',
        one_smul])

end Rescale

/-! ## 3. T-form at `s²` is the σ-form at `s` -/

/-- **`IwahoriHecke K (s·s) n ≃ₐ SchurWeyl.Hecke K s si n` when `s·si = 1`.** The T-form generator
is sent to `s·σ`. -/
noncomputable def iwahoriEquivSigma (s si : K) (hs : s * si = 1) (n : ℕ) :
    IwahoriHecke K (s * s) n ≃ₐ[K] QOU.SchurWeyl.Hecke K s si n :=
  (iwahoriEquivQiOne K (s * s) n).trans
    (rescaleEquiv n si s (s * s) 1 s si (by rw [mul_comm si s, hs])
      (by rw [← mul_assoc, mul_comm si s, hs, one_mul]) (by rw [mul_one]))

theorem iwahoriEquivSigma_σ (s si : K) (hs : s * si = 1) (n : ℕ) (i : Fin n) :
    iwahoriEquivSigma K s si hs n (IwahoriHecke.σ K (s * s) n i)
      = s • QOU.SchurWeyl.Hecke.σ K s si n i := by
  simp only [iwahoriEquivSigma, AlgEquiv.trans_apply, iwahoriEquivQiOne, rescaleEquiv,
    AlgEquiv.ofAlgHom_apply, iwahoriToQiOne_σ, rescale_σ]

/-! ## 4. The sector algebras of PR #9126 -/

section Sector

open QOU.MassTheory.HeckeSectorRep

variable {K} (q qi : K) (hqi : q * qi = 1) (n : ℕ)

/-- `σᵢ ↦ σᵢ`, from `SchurWeyl.Hecke K q qi n` to `Hn (n+1) q qi`. -/
noncomputable def toHn : QOU.SchurWeyl.Hecke K q qi n →ₐ[K] Hn (n + 1) q qi :=
  QOU.SchurWeyl.Hecke.lift K q qi n
    (fun i => RingQuot.mkAlgHom K (HeckeRelN (n + 1) q qi) (ι K ⟨i.1, by omega⟩))
    (fun i => by
      have e := RingQuot.mkAlgHom_rel K (@HeckeRelN.quad K _ (n + 1) q qi ⟨i.1, by omega⟩)
      rw [hqi, one_smul]
      simpa only [map_mul, map_add, map_smul, map_one] using e)
    (fun i hi => by
      have e := RingQuot.mkAlgHom_rel K
        (@HeckeRelN.braid K _ (n + 1) q qi ⟨i.1, by omega⟩ ⟨i.1 + 1, by omega⟩ rfl)
      simpa only [map_mul] using e)
    (fun i j hij => by
      have e := RingQuot.mkAlgHom_rel K
        (@HeckeRelN.comm K _ (n + 1) q qi ⟨j.1, by omega⟩ ⟨i.1, by omega⟩ hij)
      simpa only [map_mul] using e.symm)

/-- `σᵢ ↦ σᵢ`, from `Hn (n+1) q qi` back to `SchurWeyl.Hecke K q qi n`. -/
noncomputable def ofHn : Hn (n + 1) q qi →ₐ[K] QOU.SchurWeyl.Hecke K q qi n :=
  RingQuot.liftAlgHom K ⟨FreeAlgebra.lift K
      (fun i => QOU.SchurWeyl.Hecke.σ K q qi n ⟨i.1, by have := i.2; omega⟩), by
    intro x y h
    cases h with
    | quad i =>
        simp only [map_mul, map_add, map_smul, map_one, FreeAlgebra.lift_ι_apply]
        rw [QOU.SchurWeyl.Hecke.σ_quadratic, hqi, one_smul]
    | braid i j hj =>
        simp only [map_mul, FreeAlgebra.lift_ι_apply]
        have hi : i.1 + 1 < n := by have := j.2; omega
        have hj' : (⟨j.1, by have := j.2; omega⟩ : Fin n) = ⟨i.1 + 1, hi⟩ := Fin.ext hj
        rw [hj']
        exact QOU.SchurWeyl.Hecke.σ_braid K q qi n ⟨i.1, by omega⟩ hi
    | comm i k h =>
        simp only [map_mul, FreeAlgebra.lift_ι_apply]
        exact (QOU.SchurWeyl.Hecke.σ_commute K q qi n _ _ h).symm⟩

theorem toHn_σ (i : Fin n) :
    toHn q qi hqi n (QOU.SchurWeyl.Hecke.σ K q qi n i)
      = RingQuot.mkAlgHom K (HeckeRelN (n + 1) q qi) (ι K ⟨i.1, by omega⟩) :=
  QOU.SchurWeyl.Hecke.lift_σ K q qi n _ _ _ _ i

theorem ofHn_mk (i : {i : ℕ // i + 1 < n + 1}) :
    ofHn q qi hqi n (RingQuot.mkAlgHom K (HeckeRelN (n + 1) q qi) (ι K i))
      = QOU.SchurWeyl.Hecke.σ K q qi n ⟨i.1, by have := i.2; omega⟩ :=
  (RingQuot.liftAlgHom_mkAlgHom_apply K _ _ (ι K i)).trans (FreeAlgebra.lift_ι_apply _ i)

/-- **`SchurWeyl.Hecke K q qi n ≃ₐ Hn (n+1) q qi`** for `q·qi = 1`. -/
noncomputable def sectorEquiv : QOU.SchurWeyl.Hecke K q qi n ≃ₐ[K] Hn (n + 1) q qi :=
  AlgEquiv.ofAlgHom (toHn q qi hqi n) (ofHn q qi hqi n)
    (by
      ext z
      simp only [Function.comp_apply, AlgHom.comp_apply, AlgHom.id_apply, ofHn_mk, toHn_σ])
    (QOU.SchurWeyl.Hecke.hom_ext K q qi n fun i => by
      simp only [AlgHom.comp_apply, AlgHom.id_apply, toHn_σ, ofHn_mk])

/-- `σᵢ ↦ σᵢ`, from `SchurWeyl.Hecke K q qi n` into the all-strands algebra of PR #9126. -/
noncomputable def toInfinite : QOU.SchurWeyl.Hecke K q qi n →ₐ[K] Hecke q qi :=
  (Hn.toHecke (n + 1) q qi).comp (toHn q qi hqi n)

theorem toInfinite_σ (i : Fin n) :
    toInfinite q qi hqi n (QOU.SchurWeyl.Hecke.σ K q qi n i) = gen q qi i.1 := by
  simp only [toInfinite, AlgHom.comp_apply, toHn_σ]
  have := Hn.toHecke_gen (K := K) (n + 1) q qi i.1 (by omega)
  simpa [Hn.gen, show i.1 + 1 < n + 1 by omega] using this

end Sector

end QOU.Hecke.ModelsBridge
