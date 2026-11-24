import Mathlib.Algebra.FreeAlgebra
import Mathlib.Algebra.RingQuot
import Mathlib.Tactic

/-!
# `QOU.SchurWeyl.HeckeAlgebra` — the Iwahori–Hecke algebra `H_n(q)` (bean SW-1)

Self-contained definition of the type-`A_{n-1}` Iwahori–Hecke algebra
`H_n(q)` for the quantum-Schur–Weyl program (epic bean SW, this file is
bean SW-1).  Mathlib has Coxeter groups but no Hecke algebra, so we build
it directly as a `RingQuot` of a free algebra.

## Convention

We follow the QOU Hecke–skein convention (AGENTS.md §7a):

* **quadratic** `(σ_i - q)(σ_i + q⁻¹) = 0`, equivalently
  `σ_i² = (q - q⁻¹)·σ_i + 1`;
* **braid** `σ_i σ_{i+1} σ_i = σ_{i+1} σ_i σ_{i+1}`;
* **far commutation** `σ_i σ_j = σ_j σ_i` for `|i - j| ≥ 2`.

To stay over a **generic** `CommRing K` (AGENTS.md §7c — start generic;
specialise only when forced) we carry the inverse of `q` as an explicit
scalar `qi : K` intended as `q⁻¹`.  The quadratic relation is then stated
in the inverse-free polynomial form

`σ_i² = (q - qi)·σ_i + (q·qi)·1`,

which specialises to the QOU form `σ_i² = (q - q⁻¹)·σ_i + 1` the moment
`qi = q⁻¹` (`q * qi = 1`).  No inverses appear in the defining ideal, so
`K` need only be a commutative ring; a `Field K` or `[Invertible q]` is
required only for the skein / units statements at the end.

## What is delivered here

* `Hecke K q qi n` — the algebra, as `RingQuot (HeckeRel …)`; carries the
  canonical (non-commutative) `Ring` and `Algebra K` structure.
* `σ i` — the generators; `σ_quadratic`, `σ_braid`, `σ_commute`,
  `σ_quadratic_factored` — the defining relations hold (sorry-free).
* **Universal property** (`Hecke.lift`, `lift_σ`, `hom_ext`): an algebra
  map `H_n(q) →ₐ[K] A` is *given* by any family `g : Fin (n-1) → A`
  satisfying the three relations, and is *uniquely determined* by the
  images of the generators.  This is the interface downstream reps
  (Hoefsmit, bean SW-4) consume: to build a representation it suffices to
  give matrices satisfying the Hecke relations.

The `n!`-dimensional `T_w`-basis (Matsumoto / Bott–Samelson) is *not*
claimed here — it is a separate, deep result.

Refs:
- [kassel1995] Ch. XII (Hecke algebras, Jones polynomial),
  https://doi.org/10.1007/978-1-4612-0783-2
-/

namespace QOU.SchurWeyl

open FreeAlgebra

/-- The defining relations of the type-`A_{n-1}` Iwahori–Hecke algebra on
    `n` generators `σ_0, …, σ_{n-1}`, as a `RingQuot` relation on
    `FreeAlgebra K (Fin n)`.  `qi` is the intended inverse of `q`. -/
inductive HeckeRel (K : Type*) [CommRing K] (q qi : K) (n : ℕ) :
    FreeAlgebra K (Fin n) → FreeAlgebra K (Fin n) → Prop where
  /-- `σ_i² = (q - qi)·σ_i + (q·qi)·1` (⇔ `(σ_i - q)(σ_i + qi) = 0`). -/
  | quadratic (i : Fin n) :
      HeckeRel K q qi n (ι K i * ι K i) ((q - qi) • ι K i + (q * qi) • 1)
  /-- `σ_i σ_{i+1} σ_i = σ_{i+1} σ_i σ_{i+1}`. -/
  | braid (i : Fin n) (hi : (i : ℕ) + 1 < n) :
      HeckeRel K q qi n
        (ι K i * ι K ⟨(i : ℕ) + 1, hi⟩ * ι K i)
        (ι K ⟨(i : ℕ) + 1, hi⟩ * ι K i * ι K ⟨(i : ℕ) + 1, hi⟩)
  /-- `σ_i σ_j = σ_j σ_i` for `|i - j| ≥ 2` (stated for `j + 2 ≤ i`; the
      generated congruence is symmetric). -/
  | commute (i j : Fin n) (h : (j : ℕ) + 2 ≤ (i : ℕ)) :
      HeckeRel K q qi n (ι K i * ι K j) (ι K j * ι K i)

/-- The **Iwahori–Hecke algebra** `H_n(q)` of type `A_{n-1}`. -/
def Hecke (K : Type*) [CommRing K] (q qi : K) (n : ℕ) : Type _ :=
  RingQuot (HeckeRel K q qi n)

namespace Hecke

variable (K : Type*) [CommRing K] (q qi : K) (n : ℕ)

noncomputable instance : Ring (Hecke K q qi n) :=
  inferInstanceAs (Ring (RingQuot (HeckeRel K q qi n)))

noncomputable instance : Algebra K (Hecke K q qi n) :=
  inferInstanceAs (Algebra K (RingQuot (HeckeRel K q qi n)))

/-- The canonical algebra map from the free algebra onto `H_n(q)`. -/
noncomputable def mk : FreeAlgebra K (Fin n) →ₐ[K] Hecke K q qi n :=
  RingQuot.mkAlgHom K (HeckeRel K q qi n)

/-- The generator `σ_i ∈ H_n(q)`. -/
noncomputable def σ (i : Fin n) : Hecke K q qi n := mk K q qi n (ι K i)

/-- **The quadratic relation holds in `H` (sorry-free):**
    `σ_i² = (q - qi)·σ_i + (q·qi)·1`. -/
theorem σ_quadratic (i : Fin n) :
    σ K q qi n i * σ K q qi n i = (q - qi) • σ K q qi n i + (q * qi) • 1 := by
  have h := RingQuot.mkAlgHom_rel (S := K) (HeckeRel.quadratic (q := q) (qi := qi) i)
  simpa only [σ, mk, map_mul, map_add, map_smul, map_one] using h

/-- **The braid relation holds in `H` (sorry-free):**
    `σ_i σ_{i+1} σ_i = σ_{i+1} σ_i σ_{i+1}`. -/
theorem σ_braid (i : Fin n) (hi : (i : ℕ) + 1 < n) :
    σ K q qi n i * σ K q qi n ⟨(i : ℕ) + 1, hi⟩ * σ K q qi n i
      = σ K q qi n ⟨(i : ℕ) + 1, hi⟩ * σ K q qi n i * σ K q qi n ⟨(i : ℕ) + 1, hi⟩ := by
  have h := RingQuot.mkAlgHom_rel (S := K) (HeckeRel.braid (q := q) (qi := qi) i hi)
  simpa only [σ, mk, map_mul] using h

/-- **The commutation relation holds in `H` (sorry-free):**
    `σ_i σ_j = σ_j σ_i` for `j + 2 ≤ i`. -/
theorem σ_commute (i j : Fin n) (h : (j : ℕ) + 2 ≤ (i : ℕ)) :
    σ K q qi n i * σ K q qi n j = σ K q qi n j * σ K q qi n i := by
  have hr := RingQuot.mkAlgHom_rel (S := K) (HeckeRel.commute (q := q) (qi := qi) i j h)
  simpa only [σ, mk, map_mul] using hr

/-- The quadratic relation in factored form: `(σ_i - q)(σ_i + qi) = 0`. -/
theorem σ_quadratic_factored (i : Fin n) :
    (σ K q qi n i - q • 1) * (σ K q qi n i + qi • 1) = 0 := by
  have hq := σ_quadratic K q qi n i
  have hcross : σ K q qi n i * (qi • (1 : Hecke K q qi n)) = qi • σ K q qi n i := by
    rw [mul_smul_comm, mul_one]
  have hqσ : (q • (1 : Hecke K q qi n)) * σ K q qi n i = q • σ K q qi n i := by
    rw [smul_mul_assoc, one_mul]
  have hprod : (q • (1 : Hecke K q qi n)) * (qi • 1) = (q * qi) • 1 := by
    rw [smul_mul_assoc, one_mul, smul_smul]
  rw [mul_add, sub_mul, sub_mul, hcross, hqσ, hprod, hq]
  simp only [sub_smul]; abel

/-!
## Universal property

`H_n(q)` is the free `K`-algebra on generators satisfying the Hecke
relations.  Concretely: any target algebra map is *built* from a family
of images that satisfy the relations (`lift`), and two algebra maps out
of `H_n(q)` agreeing on the generators are equal (`hom_ext`).
-/

section UniversalProperty

variable {A : Type*} [Ring A] [Algebra K A]

/-- The free-algebra map `FreeAlgebra.lift K g` respects the Hecke
    relations, provided the images `g i` satisfy them.  This is the
    `RingQuot.liftAlgHom` side condition, extracted so both `lift` and
    `lift_σ` can name it. -/
theorem lift_respects (g : Fin n → A)
    (hquad : ∀ i, g i * g i = (q - qi) • g i + (q * qi) • 1)
    (hbraid : ∀ (i : Fin n) (hi : (i : ℕ) + 1 < n),
      g i * g ⟨(i : ℕ) + 1, hi⟩ * g i
        = g ⟨(i : ℕ) + 1, hi⟩ * g i * g ⟨(i : ℕ) + 1, hi⟩)
    (hcomm : ∀ (i j : Fin n), (j : ℕ) + 2 ≤ (i : ℕ) → g i * g j = g j * g i) :
    ∀ ⦃x y : FreeAlgebra K (Fin n)⦄, HeckeRel K q qi n x y →
      FreeAlgebra.lift K g x = FreeAlgebra.lift K g y := by
  intro x y h
  induction h with
  | quadratic i =>
      simp only [map_mul, map_add, map_smul, map_one, FreeAlgebra.lift_ι_apply]
      exact hquad i
  | braid i hi =>
      simp only [map_mul, FreeAlgebra.lift_ι_apply]
      exact hbraid i hi
  | commute i j hij =>
      simp only [map_mul, FreeAlgebra.lift_ι_apply]
      exact hcomm i j hij

/-- **Universal property (existence).**  Given a family `g : Fin n → A`
    of images satisfying the three Hecke relations, there is an algebra
    map `H_n(q) →ₐ[K] A` sending each generator `σ_i` to `g i`. -/
noncomputable def lift (g : Fin n → A)
    (hquad : ∀ i, g i * g i = (q - qi) • g i + (q * qi) • 1)
    (hbraid : ∀ (i : Fin n) (hi : (i : ℕ) + 1 < n),
      g i * g ⟨(i : ℕ) + 1, hi⟩ * g i
        = g ⟨(i : ℕ) + 1, hi⟩ * g i * g ⟨(i : ℕ) + 1, hi⟩)
    (hcomm : ∀ (i j : Fin n), (j : ℕ) + 2 ≤ (i : ℕ) → g i * g j = g j * g i) :
    Hecke K q qi n →ₐ[K] A :=
  RingQuot.liftAlgHom K ⟨FreeAlgebra.lift K g,
    lift_respects K q qi n g hquad hbraid hcomm⟩

/-- **Universal property (computation rule).**  `lift` sends `σ_i` to
    `g i`. -/
@[simp]
theorem lift_σ (g : Fin n → A)
    (hquad : ∀ i, g i * g i = (q - qi) • g i + (q * qi) • 1)
    (hbraid : ∀ (i : Fin n) (hi : (i : ℕ) + 1 < n),
      g i * g ⟨(i : ℕ) + 1, hi⟩ * g i
        = g ⟨(i : ℕ) + 1, hi⟩ * g i * g ⟨(i : ℕ) + 1, hi⟩)
    (hcomm : ∀ (i j : Fin n), (j : ℕ) + 2 ≤ (i : ℕ) → g i * g j = g j * g i)
    (i : Fin n) :
    lift K q qi n g hquad hbraid hcomm (σ K q qi n i) = g i :=
  (RingQuot.liftAlgHom_mkAlgHom_apply K (FreeAlgebra.lift K g)
      (lift_respects K q qi n g hquad hbraid hcomm) (ι K i)).trans
    (FreeAlgebra.lift_ι_apply g i)

/-- **Universal property (uniqueness).**  Two algebra maps out of
    `H_n(q)` that agree on every generator `σ_i` are equal.  Combined with
    `lift`/`lift_σ`, this exhibits `H_n(q)` as the algebra presented by the
    generators `σ_i` modulo the Hecke relations. -/
theorem hom_ext {φ ψ : Hecke K q qi n →ₐ[K] A}
    (h : ∀ i, φ (σ K q qi n i) = ψ (σ K q qi n i)) : φ = ψ := by
  have key : φ.comp (mk K q qi n) = ψ.comp (mk K q qi n) := by
    apply FreeAlgebra.hom_ext
    funext i
    simpa only [AlgHom.comp_apply, mk, σ] using h i
  ext z
  obtain ⟨x, rfl⟩ := RingQuot.mkAlgHom_surjective K (HeckeRel K q qi n) z
  exact AlgHom.congr_fun key x

end UniversalProperty

/-!
## Skein form and units (require `q` invertible)

With `qi` a genuine inverse of `q` the quadratic relation becomes the QOU
canonical form `σ_i² = (q - q⁻¹)·σ_i + 1`, and each generator is a unit —
so the braid group maps into `H_n(q)ˣ` (the Hecke representation of
braids).  This is the only place inverses of `q` are used.
-/

section Units

/-- **Skein / canonical QOU form of the quadratic relation:**
    when `q * qi = 1`, `σ_i² = (q - qi)·σ_i + 1`. -/
theorem σ_quadratic_qou (hqi : q * qi = 1) (i : Fin n) :
    σ K q qi n i * σ K q qi n i = (q - qi) • σ K q qi n i + (1 : Hecke K q qi n) := by
  have h := σ_quadratic K q qi n i
  rw [hqi, one_smul] at h
  exact h

/-- The explicit inverse of a generator: `σ_i⁻¹ = σ_i - (q - qi)·1`, read
    off `σ_i(σ_i - (q - qi)) = q·qi = 1`. -/
noncomputable def σInv (i : Fin n) : Hecke K q qi n :=
  σ K q qi n i - (q - qi) • 1

/-- `σ_i · σ_i⁻¹ = 1` when `q * qi = 1` (sorry-free). -/
theorem σ_mul_σInv (hqi : q * qi = 1) (i : Fin n) :
    σ K q qi n i * σInv K q qi n i = 1 := by
  have hq := σ_quadratic K q qi n i
  rw [hqi, one_smul] at hq
  simp only [σInv, mul_sub, mul_smul_comm, mul_one, hq]
  abel

/-- `σ_i⁻¹ · σ_i = 1` when `q * qi = 1` (sorry-free). -/
theorem σInv_mul_σ (hqi : q * qi = 1) (i : Fin n) :
    σInv K q qi n i * σ K q qi n i = 1 := by
  have hq := σ_quadratic K q qi n i
  rw [hqi, one_smul] at hq
  simp only [σInv, sub_mul, smul_mul_assoc, one_mul, hq]
  abel

/-- **The generators are units (sorry-free).**  When `q * qi = 1` each
    `σ_i` is a unit of `H_n(q)`, so the braid group maps into `H_n(q)ˣ`
    (the Hecke representation of braids). -/
noncomputable def σUnit (hqi : q * qi = 1) (i : Fin n) : (Hecke K q qi n)ˣ where
  val := σ K q qi n i
  inv := σInv K q qi n i
  val_inv := σ_mul_σInv K q qi n hqi i
  inv_val := σInv_mul_σ K q qi n hqi i

theorem isUnit_σ (hqi : q * qi = 1) (i : Fin n) : IsUnit (σ K q qi n i) :=
  ⟨σUnit K q qi n hqi i, rfl⟩

end Units

end Hecke

end QOU.SchurWeyl
