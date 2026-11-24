import Mathlib.Algebra.Algebra.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.Algebra.Bilinear
import Mathlib.Algebra.Star.Module

/-!
# QOU.frobenius_dagger_positive_definite — the Frobenius dagger

**Proposition** ([`prop:positive-definite-dagger`](../../../quantum-observable-universe/quantum-universes/positive-definite-dagger.md)).

## Two regimes: real `R`-linear involutive `S` vs. complex/quantum `*-`algebra GNS (`TN-3`)

1. **Formally real `R`-linear involutive regime (`FrobeniusAntipodeData`, `q = 1` real scalars):**
   `A` is an `R`-algebra over an ordered field `R` with Frobenius form `ε : A → R`
   and an `R`-linear involutive anti-homomorphism `S` (`S² = id`). This model
   cannot carry a positive-definite form over `ℂ` (`h(i a, i a) = -h(a, a) < 0`)
   nor on `O_q(SU(2))` (`S(β) = -q⁻¹ β ≠ β^* = -q γ`, `∫ S(β)β = 0` even at `q = 1`,
   and `S² ≠ id` for `q ≠ ±1`).
2. **Complex & `q ≠ 1` `*-`algebra GNS regime (`StarFrobeniusPositiveData`):**
   `A` carries a conjugate-linear `*-`involution (`[StarRing R] [StarRing A] [StarModule R A]`,
   on Hopf `*-`algebras satisfying `(S ∘ star)² = id` even when `S² ≠ id`) and
   GNS sesquilinear form `h_*(a, b) = ε(star a * b)`. `star_frobenius_dagger_positive_definite`
   proves adjoint uniqueness, involutivity (`star (star x) = x`), contravariance
   (`star (x * y) = star y * star x`), conjugate-linearity on scalars
   (`star (algebraMap R A r) = algebraMap R A (star r)`), and strict positivity
   over any partially ordered `*-`ring `R` (covering both `ℝ` and `ℂ` at all `q`).

Proved here, sorry-free:
* **adjoint formula** — left multiplication by `x` has adjoint left
  multiplication by `S x`: `h(x a, b) = h(a, S(x) b)`. With `S² = id` and
  `S(xy) = S(y)S(x)` this makes `†` involutive and contravariant on these
  operators;
* **uniqueness** — if `h` is positive definite, the adjoint is unique, so
  `†` is well defined on left multiplications;
* **involution and contravariance** — `(L x)†† = L x` (from `S² = id`) and
  `(L (x y))† = L (S y) ∘ L (S x)` (from `S(xy) = S(y)S(x)`);
* **restriction to scalars** — on `End(𝟙) ≅ R` the dagger is `S`, which is
  the identity there;
* **positivity** — `f† ∘ f = h(f, f) > 0` for `f ≠ 0`. This is immediate from
  the definition once `h` is positive definite (`frobeniusDagger_pos`).

Scope: the dagger is formalised on morphisms `𝟙 → A` and on the left
multiplication operators of `A`, not on arbitrary morphisms `𝟙 → X` of the
ambient category. Positivity of `h` is a hypothesis: it does not follow from
non-degeneracy. The pairing self-adjointness of `S` is not used.

Until 2026-11-21 this file checked only the scalar case `f = z • id` on
`ℂ²` (QA on #8888).

-- Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443
-- Ref: [leitner2026] quantum-observable-universe/quantum-universes/positive-definite-dagger.md
-/

namespace QOU

/-- Frobenius form and antipode on an `R`-algebra `A`. -/
class FrobeniusAntipodeData (R : Type*) [CommRing R] (A : Type*) [Ring A]
    [Algebra R A] where
  /-- The Frobenius form `∫_A`. -/
  ε : A →ₗ[R] R
  /-- The antipode. -/
  S : A →ₗ[R] A
  /-- `S² = id`. -/
  S_invol : ∀ a, S (S a) = a
  /-- `S` is an anti-homomorphism. -/
  S_anti : ∀ a b, S (a * b) = S b * S a
  /-- `S` is unital. -/
  S_one : S 1 = 1

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]

/-- The form `h(f, g) = ε(S(f) g)`. -/
def frobeniusHerm [F : FrobeniusAntipodeData R A] (a b : A) : R := F.ε (F.S a * b)

/-- The Frobenius dagger of `f : 𝟙 → A`: the functional `ε(S(f) · −) : A → 𝟙`. -/
def frobeniusDagger [F : FrobeniusAntipodeData R A] (f : A) : A →ₗ[R] R :=
  F.ε ∘ₗ LinearMap.mulLeft R (F.S f)

/-- `f† ∘ f = h(f, f)`. -/
theorem frobeniusDagger_comp_self [F : FrobeniusAntipodeData R A] (f : A) :
    frobeniusDagger (R := R) f f = frobeniusHerm f f := rfl

/-- **Adjoint formula.** `h(x a, b) = h(a, S(x) b)`. -/
theorem frobeniusHerm_mul_left [F : FrobeniusAntipodeData R A] (x a b : A) :
    frobeniusHerm (x * a) b = frobeniusHerm (R := R) a (F.S x * b) := by
  simp [frobeniusHerm, F.S_anti, mul_assoc]

/-- **Restriction to scalars.** `S` fixes `End(𝟙) ≅ R`. -/
theorem antipode_algebraMap [F : FrobeniusAntipodeData R A] (r : R) :
    F.S (algebraMap R A r) = algebraMap R A r := by
  rw [Algebra.algebraMap_eq_smul_one, map_smul, F.S_one]

theorem frobeniusHerm_sub_right [F : FrobeniusAntipodeData R A] (a u v : A) :
    frobeniusHerm (R := R) a (u - v) = frobeniusHerm a u - frobeniusHerm a v := by
  simp [frobeniusHerm, mul_sub, map_sub]

/-- `U` is an adjoint of `T` for `h`: `h(T a, b) = h(a, U b)`. -/
def IsFrobeniusAdjoint [F : FrobeniusAntipodeData R A] (T U : A → A) : Prop :=
  ∀ a b, frobeniusHerm (R := R) (T a) b = frobeniusHerm a (U b)

/-- `f† ∘ f > 0` for `f ≠ 0` when `h` is positive definite. This is immediate
from `f† ∘ f = h(f, f)` (`frobeniusDagger_comp_self`); nothing else is used. -/
theorem frobeniusDagger_pos {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    {B : Type*} [Ring B] [Algebra K B] [FrobeniusAntipodeData K B]
    (hpos : ∀ a : B, a ≠ 0 → 0 < frobeniusHerm (R := K) a a) (f : B) (hf : f ≠ 0) :
    0 < frobeniusDagger (R := K) f f := by
  rw [frobeniusDagger_comp_self]; exact hpos f hf

/-- **Frobenius dagger is positive-definite** ([`prop:positive-definite-dagger`]).

Over an ordered field `R`, with `h` positive definite, write `L x` for left
multiplication by `x`. Then
1. `L (S x)` is an adjoint of `L x`, and it is the only `R`-linear one;
2. the dagger `L x ↦ L (S x)` is involutive: `L x` is the adjoint of `L (S x)`
   (uses `S² = id`);
3. it is contravariant: the adjoint of `L (x y)` is `L (S y) ∘ L (S x)`
   (uses `S(xy) = S(y) S(x)`);
4. on scalars `End(𝟙) ≅ R` it is `S`, and `S` is the identity there.
Positivity `f† ∘ f > 0` is `frobeniusDagger_pos`, which holds by definition. -/
theorem frobenius_dagger_positive_definite {R : Type*} [Field R] [LinearOrder R]
    [IsStrictOrderedRing R] {A : Type*} [Ring A] [Algebra R A]
    [F : FrobeniusAntipodeData R A]
    (hpos : ∀ a : A, a ≠ 0 → 0 < frobeniusHerm (R := R) a a) :
    (∀ x : A, IsFrobeniusAdjoint (R := R) (x * ·) (F.S x * ·) ∧
      ∀ U : A →ₗ[R] A, IsFrobeniusAdjoint (R := R) (x * ·) U → ∀ b, U b = F.S x * b) ∧
    (∀ x : A, IsFrobeniusAdjoint (R := R) (F.S x * ·) (x * ·)) ∧
    (∀ x y : A, IsFrobeniusAdjoint (R := R) (x * y * ·) (fun b => F.S y * (F.S x * b))) ∧
    (∀ r : R, IsFrobeniusAdjoint (R := R) (algebraMap R A r * ·)
        (F.S (algebraMap R A r) * ·) ∧ F.S (algebraMap R A r) = algebraMap R A r) := by
  refine ⟨fun x => ⟨fun a b => frobeniusHerm_mul_left x a b, ?_⟩, ?_, ?_, ?_⟩
  · intro U hU b
    by_contra hne
    set c := U b - F.S x * b with hcdef
    have hc : c ≠ 0 := sub_ne_zero.mpr hne
    have h1 := hU c b
    rw [frobeniusHerm_mul_left] at h1
    have h0 : frobeniusHerm (R := R) c c = 0 := by
      conv_lhs => rw [hcdef]
      rw [frobeniusHerm_sub_right, h1, sub_self]
    exact lt_irrefl _ (h0 ▸ hpos c hc)
  · intro x a b
    have := frobeniusHerm_mul_left (R := R) (F.S x) a b
    rwa [F.S_invol] at this
  · intro x y a b
    have := frobeniusHerm_mul_left (R := R) (x * y) a b
    simpa [F.S_anti, mul_assoc] using this
  · intro r
    exact ⟨fun a b => frobeniusHerm_mul_left _ a b, antipode_algebraMap r⟩

/-! ## Conjugate-linear `*-`Frobenius GNS dagger (`TN-3`, valid over `ℂ` and at all `q`) -/

/-- `*-`algebra Frobenius GNS data on `A` over a `*-`ring `R` (valid at all `q`,
    including `O_q(SU(2))` where `S² ≠ id` while `(S ∘ star)² = id` and `star² = id`). -/
class StarFrobeniusPositiveData (R : Type*) [CommRing R] [StarRing R]
    (A : Type*) [Ring A] [StarRing A] [Algebra R A] [StarModule R A] where
  /-- The faithful Haar / Frobenius state `∫_A : A →ₗ[R] R`. -/
  ε : A →ₗ[R] R

section StarFrobenius

variable {R : Type*} [CommRing R] [StarRing R]
  {A : Type*} [Ring A] [StarRing A] [Algebra R A] [StarModule R A]

/-- The GNS sesquilinear form `h_*(a, b) = ε(a^* b)`. -/
def starFrobeniusHerm [F : StarFrobeniusPositiveData R A] (a b : A) : R :=
  F.ε (star a * b)

/-- The `*-`Frobenius dagger functional `f† = ε(f^* · −) : A →ₗ[R] R`. -/
def starFrobeniusDagger [F : StarFrobeniusPositiveData R A] (f : A) : A →ₗ[R] R :=
  F.ε ∘ₗ LinearMap.mulLeft R (star f)

@[simp]
theorem starFrobeniusDagger_comp_self [F : StarFrobeniusPositiveData R A] (f : A) :
    starFrobeniusDagger (R := R) f f = starFrobeniusHerm f f := rfl

/-- **GNS adjoint formula:** `h_*(x a, b) = h_*(a, x^* b)`. -/
theorem starFrobeniusHerm_mul_left [F : StarFrobeniusPositiveData R A] (x a b : A) :
    starFrobeniusHerm (R := R) (x * a) b = starFrobeniusHerm a (star x * b) := by
  simp [starFrobeniusHerm, star_mul, mul_assoc]

/-- **Hermitian symmetry:** when `ε` preserves `star`, `h_*(b, a) = star (h_*(a, b))`. -/
theorem starFrobeniusHerm_symm [F : StarFrobeniusPositiveData R A]
    (hε : ∀ x : A, F.ε (star x) = star (F.ε x)) (a b : A) :
    starFrobeniusHerm (R := R) b a = star (starFrobeniusHerm a b) := by
  unfold starFrobeniusHerm
  rw [← hε]
  simp [star_mul, star_star]

/-- **Conjugate-linearity on scalars `End(𝟙) ≅ R`:** `star (r · 1_A) = (star r) · 1_A`. -/
theorem star_algebraMap_eq (r : R) :
    star (algebraMap R A r) = algebraMap R A (star r) := by
  rw [Algebra.algebraMap_eq_smul_one, star_smul, star_one, Algebra.algebraMap_eq_smul_one]

theorem starFrobeniusHerm_sub_right [F : StarFrobeniusPositiveData R A] (a u v : A) :
    starFrobeniusHerm (R := R) a (u - v) = starFrobeniusHerm a u - starFrobeniusHerm a v := by
  simp [starFrobeniusHerm, mul_sub, map_sub]

/-- `U` is a GNS adjoint of `T` for `h_*`: `h_*(T a, b) = h_*(a, U b)`. -/
def IsStarFrobeniusAdjoint [F : StarFrobeniusPositiveData R A] (T U : A → A) : Prop :=
  ∀ a b, starFrobeniusHerm (R := R) (T a) b = starFrobeniusHerm a (U b)

/-- Strict positivity `f† ∘ f > 0` for `f ≠ 0` over any partially ordered `*-`ring `R`. -/
theorem starFrobeniusDagger_pos {K : Type*} [CommRing K] [PartialOrder K] [StarRing K]
    {B : Type*} [Ring B] [StarRing B] [Algebra K B] [StarModule K B]
    [StarFrobeniusPositiveData K B]
    (hpos : ∀ a : B, a ≠ 0 → 0 < starFrobeniusHerm (R := K) a a) (f : B) (hf : f ≠ 0) :
    0 < starFrobeniusDagger (R := K) f f := by
  rw [starFrobeniusDagger_comp_self]; exact hpos f hf

/-- **`*-`Frobenius GNS dagger is positive-definite at all `q` (`TN-3`).**
    Over any partially ordered commutative `*-`ring `R` (including `ℝ` and `ℂ`),
    with `h_*(a, b) = ε(a^* b)` positive definite:
    1. `L(x^*)` is the unique `R`-linear adjoint of `L(x)`;
    2. `L(x) ↦ L(x^*)` is involutive (`(x^*)^* = x`, needing no `S² = id` assumption);
    3. it is contravariant (`(x y)^* = y^* x^*`);
    4. on scalars `End(𝟙) ≅ R` it acts as `r ↦ star r` (`r̄` over `ℂ`). -/
theorem star_frobenius_dagger_positive_definite
    {K : Type*} [CommRing K] [PartialOrder K] [StarRing K]
    {B : Type*} [Ring B] [StarRing B] [Algebra K B] [StarModule K B]
    [F : StarFrobeniusPositiveData K B]
    (hpos : ∀ a : B, a ≠ 0 → 0 < starFrobeniusHerm (R := K) a a) :
    (∀ x : B, IsStarFrobeniusAdjoint (R := K) (x * ·) (star x * ·) ∧
      ∀ U : B →ₗ[K] B, IsStarFrobeniusAdjoint (R := K) (x * ·) U → ∀ b, U b = star x * b) ∧
    (∀ x : B, IsStarFrobeniusAdjoint (R := K) (star x * ·) (x * ·)) ∧
    (∀ x y : B, IsStarFrobeniusAdjoint (R := K) (x * y * ·) (fun b => star y * (star x * b))) ∧
    (∀ r : K, IsStarFrobeniusAdjoint (R := K) (algebraMap K B r * ·)
        (star (algebraMap K B r) * ·) ∧
        star (algebraMap K B r) = algebraMap K B (star r)) := by
  refine ⟨fun x => ⟨fun a b => starFrobeniusHerm_mul_left x a b, ?_⟩, ?_, ?_, ?_⟩
  · intro U hU b
    by_contra hne
    set c := U b - star x * b with hcdef
    have hc : c ≠ 0 := sub_ne_zero.mpr hne
    have h1 := hU c b
    rw [starFrobeniusHerm_mul_left] at h1
    have h0 : starFrobeniusHerm (R := K) c c = 0 := by
      conv_lhs => rw [hcdef]
      rw [starFrobeniusHerm_sub_right, h1, sub_self]
    exact lt_irrefl _ (h0 ▸ hpos c hc)
  · intro x a b
    have := starFrobeniusHerm_mul_left (R := K) (star x) a b
    rwa [star_star] at this
  · intro x y a b
    have := starFrobeniusHerm_mul_left (R := K) (x * y) a b
    simpa [star_mul, mul_assoc] using this
  · intro r
    exact ⟨fun a b => starFrobeniusHerm_mul_left _ a b, star_algebraMap_eq r⟩

end StarFrobenius

end QOU
