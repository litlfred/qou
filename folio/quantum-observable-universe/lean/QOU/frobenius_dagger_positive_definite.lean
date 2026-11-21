import Mathlib.Algebra.Algebra.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.Algebra.Bilinear

/-!
# QOU.frobenius_dagger_positive_definite — the Frobenius dagger

**Proposition** ([`prop:positive-definite-dagger`](../../../quantum-observable-universe/quantum-universes/positive-definite-dagger.md)).

Model. `A` is an `R`-algebra with Frobenius form `ε : A → R` and an antipode
`S` that is `R`-linear, involutive (`S² = id`), an anti-homomorphism and
unital. A morphism `f : 𝟙 → A` is an element `f ∈ A`, and its dagger is the
functional `f† = ε(S(f) · −)`. The form is `h(f, g) = ε(S(f) g)`, so
`f† ∘ f = h(f, f)` by definition (`frobeniusDagger_comp_self`).

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

end QOU
