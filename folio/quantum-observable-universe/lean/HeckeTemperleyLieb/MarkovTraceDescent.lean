import HeckeTemperleyLieb.MarkovTraceUnique

/-!
# QOU.SchurWeyl.MarkovTraceDescent — a Markov trace descends to a subring

Let `φ : R → L` be an injective ring map into a commutative ring `L`, and let `U` be a Markov trace
family on the Hecke tower over `L` at parameters `(φ q, φ qi, φ z)`. Then the values of `U` on the
image of the Hecke tower over `R` lie in `φ(R)`, so `U` restricts to a Markov trace family over `R`
at `(q, qi, z)` (`MarkovTraceFamily.descend`).

The proof is the induction of `markovTrace_unique`: the coset family spans `H_{m+1}` over `R`, a
coset word is either `ι(w)` or `ι(w)·σ_m·ι(t)`, and the Markov property sends the second to
`z · tr(t w)`. So every trace value is an `R`-polynomial in `z` and the values on `H_0 = R`.

This is how the Ocneanu trace at `z_D = q³/(q²+1)`, built over a field by the seminormal form,
is seen to be defined over `ℤ[q, q⁻¹, (q²+1)⁻¹]`.

Base ring: generic `[CommRing R] [CommRing L]`. Nothing archimedean.
-/

namespace QOU.SchurWeyl
namespace HeckeCoset

open Hecke HeckeInclusion

variable {R : Type*} [CommRing R] {L : Type*} [CommRing L] (φ : R →+* L)

/-- `Hecke L (φ q) (φ qi) n` as an `R`-algebra, through `φ`. -/
noncomputable instance baseAlgebra (q qi : R) (n : ℕ) :
    Algebra R (Hecke L (φ q) (φ qi) n) :=
  ((algebraMap L (Hecke L (φ q) (φ qi) n)).comp φ).toAlgebra' fun c x => Algebra.commutes (φ c) x

theorem baseAlgebra_algebraMap (q qi : R) (n : ℕ) (r : R) :
    algebraMap R (Hecke L (φ q) (φ qi) n) r = algebraMap L (Hecke L (φ q) (φ qi) n) (φ r) := rfl

/-- **Base change** `H_n(R; q) → H_n(L; φ q)`, `σ_i ↦ σ_i`. -/
noncomputable def baseMap (q qi : R) (n : ℕ) :
    Hecke R q qi n →ₐ[R] Hecke L (φ q) (φ qi) n :=
  Hecke.lift R q qi n (σ L (φ q) (φ qi) n)
    (fun i => by
      rw [σ_quadratic, Algebra.smul_def, Algebra.smul_def, Algebra.smul_def, Algebra.smul_def,
        baseAlgebra_algebraMap, baseAlgebra_algebraMap]
      simp only [map_sub, map_mul])
    (fun i hi => σ_braid L (φ q) (φ qi) n i hi)
    (fun i j h => σ_commute L (φ q) (φ qi) n i j h)

@[simp] theorem baseMap_σ (q qi : R) (n : ℕ) (i : Fin n) :
    baseMap φ q qi n (σ R q qi n i) = σ L (φ q) (φ qi) n i :=
  Hecke.lift_σ R q qi n _ _ _ _ i

theorem baseMap_algebraMap (q qi : R) (n : ℕ) (r : R) :
    baseMap φ q qi n (algebraMap R (Hecke R q qi n) r)
      = algebraMap L (Hecke L (φ q) (φ qi) n) (φ r) :=
  (baseMap φ q qi n).commutes r

/-- The tower inclusion over `L`, viewed as an `R`-algebra map. -/
noncomputable def inclR (q qi : R) (n : ℕ) :
    Hecke L (φ q) (φ qi) n →ₐ[R] Hecke L (φ q) (φ qi) (n + 1) :=
  { (heckeIncl L (φ q) (φ qi) n).toRingHom with
    commutes' := fun r => (heckeIncl L (φ q) (φ qi) n).commutes (φ r) }

/-- Base change commutes with the tower inclusion. -/
theorem baseMap_heckeIncl (q qi : R) (n : ℕ) (x : Hecke R q qi n) :
    baseMap φ q qi (n + 1) (heckeIncl R q qi n x)
      = heckeIncl L (φ q) (φ qi) n (baseMap φ q qi n x) := by
  have h : (baseMap φ q qi (n + 1)).comp (heckeIncl R q qi n)
      = (inclR φ q qi n).comp (baseMap φ q qi n) := by
    apply Hecke.hom_ext
    intro i
    simp only [AlgHom.comp_apply, heckeIncl_σ, baseMap_σ]
    exact (heckeIncl_σ L (φ q) (φ qi) n i).symm
  exact congrArg (fun f => f x) h

variable {φ}

/-- **Integrality.** Every value of `U` on the image of the `R`-tower lies in `φ(R)`. -/
theorem MarkovTraceFamily.tr_baseMap_mem_range {q qi z : R}
    (U : MarkovTraceFamily L (φ q) (φ qi) (φ z)) :
    ∀ (n : ℕ) (x : Hecke R q qi n), U.tr n (baseMap φ q qi n x) ∈ φ.range := by
  intro n
  induction n with
  | zero =>
      intro x
      have hx : x ∈ Submodule.span R
          (Set.range (cosetFam (K := R) (q := q) (qi := qi) 0)) := by
        rw [span_cosetFam_eq_top]; trivial
      induction hx using Submodule.span_induction with
      | mem y hy =>
          obtain ⟨p, rfl⟩ := hy
          show U.tr 0 (baseMap φ q qi 0 1) ∈ φ.range
          rw [map_one, U.tr_one]; exact ⟨1, map_one φ⟩
      | zero => rw [map_zero, map_zero]; exact ⟨0, map_zero φ⟩
      | add a b _ _ ha hb =>
          rw [map_add, map_add]; exact φ.range.add_mem ha hb
      | smul c a _ ha =>
          rw [Algebra.smul_def, map_mul, baseMap_algebraMap, ← Algebra.smul_def,
            map_smul, smul_eq_mul]
          exact φ.range.mul_mem ⟨c, rfl⟩ ha
  | succ m ih =>
      intro x
      have hx : x ∈ Submodule.span R
          (Set.range (cosetFam (K := R) (q := q) (qi := qi) (m + 1))) := by
        rw [span_cosetFam_eq_top]; trivial
      induction hx using Submodule.span_induction with
      | mem y hy =>
          obtain ⟨p, rfl⟩ := hy
          rw [cosetFam_succ]
          rcases Nat.eq_zero_or_pos (p.2 : ℕ) with h0 | hp
          · rw [h0, descProd_zero, mul_one, baseMap_heckeIncl, U.tr_incl]
            exact ih _
          · obtain ⟨t, ht⟩ := descProd_eq_last_mul_incl (K := R) (q := q) (qi := qi) m
              (p.2 : ℕ) hp (by have := p.2.isLt; omega)
            rw [ht, map_mul (baseMap φ q qi (m + 1)), map_mul (baseMap φ q qi (m + 1)),
              baseMap_heckeIncl, baseMap_heckeIncl, baseMap_σ, U.tr_coset,
              ← map_mul (baseMap φ q qi m)]
            exact φ.range.mul_mem ⟨z, rfl⟩ (ih _)
      | zero => rw [map_zero, map_zero]; exact ⟨0, map_zero φ⟩
      | add a b _ _ ha hb =>
          rw [map_add, map_add]; exact φ.range.add_mem ha hb
      | smul c a _ ha =>
          rw [Algebra.smul_def, map_mul, baseMap_algebraMap, ← Algebra.smul_def,
            map_smul, smul_eq_mul]
          exact φ.range.mul_mem ⟨c, rfl⟩ ha

theorem MarkovTraceFamily.tr_baseMap_smul {q qi z : R}
    (U : MarkovTraceFamily L (φ q) (φ qi) (φ z)) (n : ℕ) (c : R) (x : Hecke R q qi n) :
    U.tr n (baseMap φ q qi n (c • x)) = φ c * U.tr n (baseMap φ q qi n x) := by
  rw [Algebra.smul_def, map_mul, baseMap_algebraMap, ← Algebra.smul_def, map_smul, smul_eq_mul]

/-- The descended trace value: the unique `r : R` with `φ r = U.tr n (baseMap x)`. -/
noncomputable def MarkovTraceFamily.descVal {q qi z : R}
    (U : MarkovTraceFamily L (φ q) (φ qi) (φ z)) (n : ℕ) (x : Hecke R q qi n) : R :=
  (U.tr_baseMap_mem_range n x).choose

theorem MarkovTraceFamily.descVal_spec {q qi z : R}
    (U : MarkovTraceFamily L (φ q) (φ qi) (φ z)) (n : ℕ) (x : Hecke R q qi n) :
    φ (U.descVal n x) = U.tr n (baseMap φ q qi n x) :=
  (U.tr_baseMap_mem_range n x).choose_spec

/-- **Descent.** A Markov trace family over `L` at `(φ q, φ qi, φ z)`, with `φ` injective, gives a
Markov trace family over `R` at `(q, qi, z)`, characterised by `φ ∘ tr_R = tr_L ∘ baseMap`
(`descend_spec`). -/
noncomputable def MarkovTraceFamily.descend {q qi z : R} (hφ : Function.Injective φ)
    (U : MarkovTraceFamily L (φ q) (φ qi) (φ z)) : MarkovTraceFamily R q qi z where
  tr n :=
    { toFun := U.descVal n
      map_add' := fun a b => hφ (by
        rw [map_add, U.descVal_spec, U.descVal_spec, U.descVal_spec, map_add, map_add])
      map_smul' := fun c a => hφ (by
        rw [RingHom.id_apply, smul_eq_mul, map_mul, U.descVal_spec, U.descVal_spec,
          U.tr_baseMap_smul]) }
  tr_one n := hφ (by
    show φ (U.descVal n 1) = φ 1
    rw [U.descVal_spec, map_one (baseMap φ q qi n), map_one φ, U.tr_one])
  tr_cyclic n x y := hφ (by
    show φ (U.descVal n (x * y)) = φ (U.descVal n (y * x))
    rw [U.descVal_spec, U.descVal_spec, map_mul (baseMap φ q qi n), map_mul (baseMap φ q qi n),
      U.tr_cyclic])
  tr_incl n x := hφ (by
    show φ (U.descVal (n + 1) (heckeIncl R q qi n x)) = φ (U.descVal n x)
    rw [U.descVal_spec, U.descVal_spec, baseMap_heckeIncl, U.tr_incl])
  tr_markov n x := hφ (by
    show φ (U.descVal (n + 1) (heckeIncl R q qi n x * σ R q qi (n + 1) (Fin.last n)))
      = φ (z * U.descVal n x)
    rw [U.descVal_spec, map_mul (baseMap φ q qi (n + 1)), baseMap_heckeIncl, baseMap_σ,
      U.tr_markov, map_mul, U.descVal_spec])

theorem MarkovTraceFamily.descend_spec {q qi z : R} (hφ : Function.Injective φ)
    (U : MarkovTraceFamily L (φ q) (φ qi) (φ z)) (n : ℕ) (x : Hecke R q qi n) :
    φ ((U.descend hφ).tr n x) = U.tr n (baseMap φ q qi n x) :=
  U.descVal_spec n x

end HeckeCoset
end QOU.SchurWeyl
