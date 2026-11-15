import QOU.IwahoriHecke.JonesNormalForm
import Mathlib.Algebra.FreeAlgebra
import Mathlib.Algebra.RingQuot

/-!
# QOU.IwahoriHecke.MarkovTransfer — Markov traces agree across Hecke-family algebras

`QOU.IwahoriHecke.JonesNormalForm.markov_unique` compares two Markov traces on **one**
algebra. This file compares Markov traces on **different** algebras. It does so through
the presented algebra `Pres N a b`: the free `R`-algebra on `N` generators modulo the
type-`A` relations `sᵢ² = a·sᵢ + b`, braid and far commutation. That algebra is generated
by its generators (`adjoin_pgen_eq_top`). It maps to every algebra carrying a
`HeckeFamily N a b s` (`lift`). So a Markov trace on any such algebra pulls back to a
Markov trace on `Pres N a b`, and uniqueness there gives:

* `markov_transfer` — for two algebras `A`, `B` with Hecke families `sA`, `sB` (same `N`,
  `a`, `b`) and Markov traces `tA`, `tB` with the same `z`, `tA (lift x) = tB (lift x)` for
  every element `x` of the presented algebra.
* `markov_transfer_cox` — in particular the Markov trace of every power of the Coxeter
  element `γ_r = s₀ s₁ ⋯ s_{r-2}` (`r ≤ N + 1`), i.e. of the `(r, s)` torus braid, is the
  same number in every Hecke-family algebra.

So the Rosso–Jones value `tr_M(γ_r^s)` is a function of `(a, b, z, r, s)` alone. To prove a
closed form for it at a given `r`, it is enough to compute it in **one** algebra that
carries a Markov trace, e.g. a sum of matrix representations. This is how
`QOU.Archimedean.RossoJonesH4` does `r = 4`. This file does **not** prove the closed form
for general `r`. That still needs a Markov trace whose value on `γ_r^s` can be computed for
every `r`, for example the Temperley–Lieb standard modules `W_{r,j}` with weights `[j+1]`
and the eigenvalues of `γ_r` on each. None of that is formalised (bean `qou-q425`).

Sorry-free; axioms `propext`, `Classical.choice`, `Quot.sound`.
-/

namespace QOU.IwahoriHecke.JonesNormalForm

variable {R : Type*} [CommRing R] (N : ℕ) (a b : R)

/-- The type-`A` Hecke relations on the free algebra on `N` generators. -/
inductive PresRel : FreeAlgebra R (Fin N) → FreeAlgebra R (Fin N) → Prop
  | quad (i : Fin N) :
      PresRel (FreeAlgebra.ι R i * FreeAlgebra.ι R i) (a • FreeAlgebra.ι R i + b • 1)
  | braid (i j : Fin N) (h : j.val = i.val + 1) :
      PresRel (FreeAlgebra.ι R i * FreeAlgebra.ι R j * FreeAlgebra.ι R i)
        (FreeAlgebra.ι R j * FreeAlgebra.ι R i * FreeAlgebra.ι R j)
  | comm (i j : Fin N) (h : i.val + 2 ≤ j.val) :
      PresRel (FreeAlgebra.ι R i * FreeAlgebra.ι R j) (FreeAlgebra.ι R j * FreeAlgebra.ι R i)

/-- The presented Hecke algebra with quadratic relation `s² = a s + b`. -/
abbrev Pres := RingQuot (PresRel N a b)

/-- Its generators, ℕ-indexed (`0` from `N` on). -/
noncomputable def pgen (i : ℕ) : Pres N a b :=
  if h : i < N then RingQuot.mkAlgHom R (PresRel N a b) (FreeAlgebra.ι R ⟨i, h⟩) else 0

theorem pgen_of_lt {i : ℕ} (h : i < N) :
    pgen N a b i = RingQuot.mkAlgHom R (PresRel N a b) (FreeAlgebra.ι R ⟨i, h⟩) := by
  simp [pgen, h]

theorem pres_heckeFamily : HeckeFamily N a b (pgen N a b) where
  quad i hi := by
    rw [pgen_of_lt N a b hi, ← map_mul, RingQuot.mkAlgHom_rel R (PresRel.quad ⟨i, hi⟩)]
    simp
  braid i hi := by
    rw [pgen_of_lt N a b (show i < N by omega), pgen_of_lt N a b hi, ← map_mul, ← map_mul,
      ← map_mul, ← map_mul,
      RingQuot.mkAlgHom_rel R (PresRel.braid ⟨i, by omega⟩ ⟨i + 1, hi⟩ rfl)]
  comm i j hij hj := by
    rw [pgen_of_lt N a b (show i < N by omega), pgen_of_lt N a b hj, ← map_mul, ← map_mul,
      RingQuot.mkAlgHom_rel R (PresRel.comm ⟨i, by omega⟩ ⟨j, hj⟩ hij)]

theorem image_pgen : pgen N a b '' Set.Iio N
    = RingQuot.mkAlgHom R (PresRel N a b) '' Set.range (FreeAlgebra.ι R) := by
  ext x
  constructor
  · rintro ⟨i, hi, rfl⟩
    exact ⟨_, ⟨⟨i, hi⟩, rfl⟩, (pgen_of_lt N a b hi).symm⟩
  · rintro ⟨_, ⟨i, rfl⟩, rfl⟩
    exact ⟨i, i.isLt, pgen_of_lt N a b i.isLt⟩

theorem adjoin_pgen_eq_top : Algebra.adjoin R (pgen N a b '' Set.Iio N) = ⊤ := by
  rw [image_pgen, Algebra.adjoin_image, FreeAlgebra.adjoin_range_ι, Algebra.map_top,
    AlgHom.range_eq_top]
  exact RingQuot.mkAlgHom_surjective R _

variable {N a b}
variable {A : Type*} [Ring A] [Algebra R A] {s : ℕ → A}

/-- The map from the presented algebra to any algebra carrying a Hecke family. -/
noncomputable def lift (hs : HeckeFamily N a b s) : Pres N a b →ₐ[R] A :=
  RingQuot.liftAlgHom R ⟨FreeAlgebra.lift R (fun i : Fin N => s i), by
    intro x y h
    cases h with
    | quad i => simp [hs.quad i i.isLt]
    | braid i j hij =>
      simp only [map_mul, FreeAlgebra.lift_ι_apply]
      have hj : (j : ℕ) = i + 1 := hij
      rw [hj]
      exact hs.braid i (by omega)
    | comm i j hij =>
      simp only [map_mul, FreeAlgebra.lift_ι_apply]
      exact hs.comm i j hij j.isLt⟩

theorem lift_pgen (hs : HeckeFamily N a b s) {i : ℕ} (hi : i < N) :
    lift hs (pgen N a b i) = s i := by
  rw [pgen_of_lt N a b hi, lift, RingQuot.liftAlgHom_mkAlgHom_apply, FreeAlgebra.lift_ι_apply]

theorem lift_mem_adjoin (hs : HeckeFamily N a b s) {k : ℕ} (hk : k ≤ N) {x : Pres N a b}
    (hx : x ∈ Algebra.adjoin R (pgen N a b '' Set.Iio k)) :
    lift hs x ∈ Algebra.adjoin R (s '' Set.Iio k) := by
  have himg : (lift hs) '' (pgen N a b '' Set.Iio k) = s '' Set.Iio k := by
    rw [Set.image_image]
    refine Set.image_congr fun i hi => lift_pgen hs ?_
    exact lt_of_lt_of_le (Set.mem_Iio.mp hi) hk
  rw [← himg, Algebra.adjoin_image]
  exact ⟨x, hx, rfl⟩

/-- A Markov trace on `A` pulls back to a Markov trace on the presented algebra. -/
theorem pullback_markov (hs : HeckeFamily N a b s) (z : R) (t : A →ₗ[R] R)
    (hmark : ∀ k, k < N → ∀ x ∈ Algebra.adjoin R (s '' Set.Iio k), t (x * s k) = z * t x) :
    ∀ k, k < N → ∀ x ∈ Algebra.adjoin R (pgen N a b '' Set.Iio k),
      (t ∘ₗ (lift hs).toLinearMap) (x * pgen N a b k)
        = z * (t ∘ₗ (lift hs).toLinearMap) x := by
  intro k hk x hx
  simp only [LinearMap.coe_comp, Function.comp_apply, AlgHom.toLinearMap_apply, map_mul,
    lift_pgen hs hk]
  exact hmark k hk _ (lift_mem_adjoin hs hk.le hx)

variable {B : Type*} [Ring B] [Algebra R B] {s' : ℕ → B}

/-- **Markov transfer.** Two normalised, cyclic Markov traces with the same `z`, on two
algebras carrying Hecke families with the same `(N, a, b)`, take the same value on the image
of every element of the presented algebra. -/
theorem markov_transfer (hs : HeckeFamily N a b s) (hs' : HeckeFamily N a b s') (z : R)
    (t : A →ₗ[R] R) (ht1 : t 1 = 1) (hcyc : ∀ x y : A, t (x * y) = t (y * x))
    (hmark : ∀ k, k < N → ∀ x ∈ Algebra.adjoin R (s '' Set.Iio k), t (x * s k) = z * t x)
    (t' : B →ₗ[R] R) (ht1' : t' 1 = 1) (hcyc' : ∀ x y : B, t' (x * y) = t' (y * x))
    (hmark' : ∀ k, k < N → ∀ x ∈ Algebra.adjoin R (s' '' Set.Iio k), t' (x * s' k) = z * t' x)
    (x : Pres N a b) : t (lift hs x) = t' (lift hs' x) := by
  have h := markov_unique_of_adjoin_eq_top (pres_heckeFamily N a b) (adjoin_pgen_eq_top N a b) z
    (t ∘ₗ (lift hs).toLinearMap) (t' ∘ₗ (lift hs').toLinearMap)
    (by simp [ht1]) (by intro x y; simp [hcyc]) (pullback_markov hs z t hmark)
    (by simp [ht1']) (by intro x y; simp [hcyc']) (pullback_markov hs' z t' hmark')
  exact LinearMap.congr_fun h x

/-- The Coxeter element `γ_r = s₀ s₁ ⋯ s_{r-2}` (`cox s n = s₀ ⋯ s_{n-1}`). -/
def cox {M : Type*} [Monoid M] (s : ℕ → M) : ℕ → M
  | 0 => 1
  | n + 1 => cox s n * s n

theorem lift_cox (hs : HeckeFamily N a b s) {n : ℕ} (hn : n ≤ N) :
    lift hs (cox (pgen N a b) n) = cox s n := by
  induction n with
  | zero => simp [cox]
  | succ m ih => rw [cox, cox, map_mul, ih (by omega), lift_pgen hs (by omega)]

/-- **Torus braids.** The Markov trace of `(s₀ ⋯ s_{n-1})^p` (the `(n+1, p)` torus braid)
is the same in every Hecke-family algebra, for every Markov trace with the same `z`. -/
theorem markov_transfer_cox (hs : HeckeFamily N a b s) (hs' : HeckeFamily N a b s') (z : R)
    (t : A →ₗ[R] R) (ht1 : t 1 = 1) (hcyc : ∀ x y : A, t (x * y) = t (y * x))
    (hmark : ∀ k, k < N → ∀ x ∈ Algebra.adjoin R (s '' Set.Iio k), t (x * s k) = z * t x)
    (t' : B →ₗ[R] R) (ht1' : t' 1 = 1) (hcyc' : ∀ x y : B, t' (x * y) = t' (y * x))
    (hmark' : ∀ k, k < N → ∀ x ∈ Algebra.adjoin R (s' '' Set.Iio k), t' (x * s' k) = z * t' x)
    {n : ℕ} (hn : n ≤ N) (p : ℕ) : t (cox s n ^ p) = t' (cox s' n ^ p) := by
  have h := markov_transfer hs hs' z t ht1 hcyc hmark t' ht1' hcyc' hmark' (cox (pgen N a b) n ^ p)
  rwa [map_pow (lift hs), map_pow (lift hs'), lift_cox hs hn, lift_cox hs' hn] at h

end QOU.IwahoriHecke.JonesNormalForm
