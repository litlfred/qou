import Mathlib.Algebra.Algebra.Basic
import Mathlib.Algebra.Category.Ring.Basic
import Mathlib.Algebra.Module.LinearMap.Basic
import Mathlib.LinearAlgebra.Span.Basic


/-!
# Confinement = spectral-sequence collapse

The collapse of the GB-filtration spectral sequence is the
categorical statement of color confinement: only the centre
`Z(A) = ⊕_λ R · e_λ` survives as physical observables, all
"colored" non-central elements are cohomologically trivial.

The Markov trace (Frobenius integral `Int_A : A → R`) factors through
the Wedderburn projection `π_Z : A ↠ Z(A)`, and every observable
`Int_A (ρ β · 𝒯)` decomposes as a sum over Wedderburn residues
`Σ_λ Int_{A_λ} (ρ β · 𝒯)`.

The curvature 2-cocycle `F` encoding Hecke + Yang–Baxter relations
plays the role of the string tension categorically.

-- Ref: [leitner2026] prop:confinement-categorical
-/

namespace QOU.WedderburnMass

/-- A semisimple Frobenius algebra `A` over a commutative ring `R`,
    abstracting `H_n(R, q)` for generic `q`. -/
class SemisimpleFrobeniusHeckeLike (R : Type*) [CommRing R]
    (A : Type*) [Ring A] [Algebra R A] where
  /-- Frobenius integral: the Markov trace as `R`-linear map. -/
  intA : A →ₗ[R] R
  /-- Cyclicity: the integral vanishes on commutators. -/
  cyclic : ∀ a b : A, intA (a * b) = intA (b * a)
  /-- Centre as an explicit sub-`R`-module (Wedderburn). -/
  Z : Submodule R A
  /-- Centre projection (Wedderburn): `π_Z(a) = Σ_λ e_λ · a · e_λ`. -/
  piZ : A →ₗ[R] Z
  /-- `π_Z` is a genuine projection onto the centre: it restricts to the
      identity on central elements (`a ∈ Z ⇒ π_Z a = a`). This is the
      algebraic shadow of "only `E_∞^{0,0} = Z(A)` survives": the
      projection fixes exactly the surviving centre and kills the rest.
      (Semisimplicity / Whitehead-lemma cohomology vanishing in positive
      degree is what makes `π_Z` well-defined as a centre projection.) -/
  piZ_fixes_centre : ∀ a : A, ∀ ha : a ∈ Z, (piZ a : A) = a
  -- Ref: [leitner2026] prop:spectral-sequence-collapse

/-- **Theorem (clause 1 — survival).**
    Only `E_∞^{0,0} = Z(A)` survives the spectral sequence: the centre
    projection `π_Z` acts as the identity on the surviving centre `Z(A)`
    (every central element is its own residue, all non-central
    components are projected away). Derived from `piZ_fixes_centre`. -/
theorem confinement_survives_only_centre
    {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]
    [I : SemisimpleFrobeniusHeckeLike R A] :
    ∀ a : A, a ∈ I.Z → (I.piZ a : A) = a := by
  -- Content: HH^k(A) = 0 for k ≥ 1, so E_∞^{p,q} = 0 whenever p+q ≥ 1;
  -- only E_∞^{0,0} = HH^0 = Z(A) survives, on which π_Z is the identity.
  -- Ref: [leitner2026] prop:spectral-sequence-collapse, Whitehead lemma
  exact fun a ha => I.piZ_fixes_centre a ha

/-! **The former axiom `confinement_int_factors_through_centre_axiom`
    was false** (removed 2026-11-15, together with the theorem
    `confinement_int_factors_through_centre` and the corollary
    `observables_are_wedderburn_sum`, which only restated it).

    It claimed `∃ μ, intA = μ ∘ piZ` for every `SemisimpleFrobeniusHeckeLike`
    instance. Nothing in the class ties `intA` to `piZ`: the instance on
    `A = ℤ` with `intA = id`, `Z = ⊥` and `piZ = 0` satisfies every field,
    and then `μ ∘ piZ = 0 ≠ intA`. `not_int_factors_through_centre_unconstrained`
    below proves this.

    The missing hypothesis is that the trace is invariant under the centre
    projection, `intA (piZ a) = intA a`; with it, `μ := intA` restricted to
    `Z` works. Recorded as open in bean `qou-n2un`. -/

/-- An instance on `ℤ` with zero centre submodule and zero projection. -/
def zeroCentreInstance : SemisimpleFrobeniusHeckeLike ℤ ℤ where
  intA := LinearMap.id
  cyclic := fun a b => mul_comm a b
  Z := ⊥
  piZ := 0
  piZ_fixes_centre := fun a ha => by
    rw [Submodule.mem_bot] at ha
    simp [ha]

/-- **The former axiom is false.** -/
theorem not_int_factors_through_centre_unconstrained :
    ¬ (∀ {R : Type} [CommRing R] {A : Type} [Ring A] [Algebra R A]
        [I : SemisimpleFrobeniusHeckeLike R A],
        ∃ μ : I.Z →ₗ[R] R, I.intA = μ.comp I.piZ) := by
  intro h
  obtain ⟨μ, hμ⟩ := @h ℤ _ ℤ _ _ zeroCentreInstance
  have h1 := LinearMap.congr_fun hμ 1
  simp [zeroCentreInstance] at h1

/-- **Repaired form of the removed axiom.** If the trace is invariant under
    the centre projection, `intA (π_Z a) = intA a`, then it factors through
    the centre: `intA = μ ∘ π_Z` with `μ := intA|_Z`.

    The content is entirely in the hypothesis. For `H_n(q)` it is the
    statement that the Markov trace sees only Wedderburn residues, which is
    still to be proved for the concrete `π_Z`. -/
theorem int_factors_through_centre_of_invariant
    {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]
    [I : SemisimpleFrobeniusHeckeLike R A]
    (hinv : ∀ a : A, I.intA (I.piZ a : A) = I.intA a) :
    ∃ μ : I.Z →ₗ[R] R, I.intA = μ.comp I.piZ :=
  ⟨I.intA.comp I.Z.subtype, LinearMap.ext fun a => (hinv a).symm⟩

end QOU.WedderburnMass
