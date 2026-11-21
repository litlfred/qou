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
* **restriction to scalars** — `S` fixes `End(𝟙) ≅ R`;
* **uniqueness** — if `h` is positive definite, the adjoint is unique, so
  `†` is well defined;
* **positivity** — if `h` is positive definite, `f† ∘ f > 0` for `f ≠ 0`.

Positivity of `h` is a hypothesis, as in the `.md`: it does not follow from
non-degeneracy. The `.md`'s "self-adjoint for the pairing" hypothesis is not
needed for these statements.

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

/-- **Frobenius dagger is positive-definite** ([`prop:positive-definite-dagger`]).

Over an ordered field, if `h` is positive definite then
1. left multiplication by `x` has adjoint left multiplication by `S x`;
2. that adjoint is unique: any `R`-linear `U` with `h(x a, b) = h(a, U b)` is
   `b ↦ S(x) b`;
3. `S` fixes the scalars `End(𝟙) ≅ R`;
4. `f† ∘ f > 0` for every `f ≠ 0`. -/
theorem frobenius_dagger_positive_definite {R : Type*} [Field R] [LinearOrder R]
    [IsStrictOrderedRing R] {A : Type*} [Ring A] [Algebra R A]
    [F : FrobeniusAntipodeData R A]
    (hpos : ∀ a : A, a ≠ 0 → 0 < frobeniusHerm (R := R) a a) :
    (∀ x a b : A, frobeniusHerm (R := R) (x * a) b = frobeniusHerm a (F.S x * b)) ∧
    (∀ (x : A) (U : A →ₗ[R] A),
        (∀ a b, frobeniusHerm (R := R) (x * a) b = frobeniusHerm a (U b)) →
        ∀ b, U b = F.S x * b) ∧
    (∀ r : R, F.S (algebraMap R A r) = algebraMap R A r) ∧
    (∀ f : A, f ≠ 0 → 0 < frobeniusDagger (R := R) f f) := by
  refine ⟨frobeniusHerm_mul_left, ?_, antipode_algebraMap, fun f hf => hpos f hf⟩
  intro x U hU b
  by_contra hne
  set c := U b - F.S x * b with hcdef
  have hc : c ≠ 0 := sub_ne_zero.mpr hne
  have h1 := hU c b
  rw [frobeniusHerm_mul_left] at h1
  have h0 : frobeniusHerm (R := R) c c = 0 := by
    conv_lhs => rw [hcdef]
    rw [frobeniusHerm_sub_right, h1, sub_self]
  exact lt_irrefl _ (h0 ▸ hpos c hc)

end QOU
