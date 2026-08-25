import QOU.Information.CocenterTraceFactor
import Mathlib.Algebra.Algebra.Bilinear

/-!
# QOU.Information.OuterDerivationResidue — the residue is an OUTER derivation

`HH₁(A) = Der(A) / Inn(A)` — the first Hochschild cohomology is derivations
modulo *inner* ones. The merged `CocenterTraceFactor` localized the magnitude
axis at `HH₀ = A/[A,A]` and proved any decision separator is a **non-trace**.
This file takes the next structural step on the *decision* axis: it identifies
what an `HH₁` class concretely is and shows the inner part is trace-blind, so the
**residue** `res` — if nonzero — is carried by an **outer** derivation.

## The bridge to the merged cocenter

An **inner derivation** `ad_x : a ↦ x·a − a·x` has image inside the commutator
submodule `[A,A]` (`innerDerivation_mem_commutator`). Since a cyclic functional
(`BilinearTrace.IsCyclic`) kills `[A,A]` (`commutatorSubmodule_le_ker_of_trace`,
merged), **every inner derivation is trace-blind**
(`trace_comp_innerDerivation_eq_zero`). So the inner part of `HH₁` is exactly the
part the magnitude/trace tower already sees and discards; a *decision* class must
be the complementary **outer** part `Der(A)/Inn(A)`.

## Where this sits in the P-vs-NP wall

At generic `q` the Hecke algebra `H_n(q)` is semisimple, and a semisimple algebra
has **no outer derivations** (first Whitehead lemma / separability: every
derivation is inner), so `HH₁(H_n(q)) = 0` — no residue can live there. The
residue can therefore only appear at the **root-of-unity / fibre level**, where
`H_n(ζ)` is non-semisimple and outer derivations can exist. `IsInnerDerivation`
and the outer-residue question are stated honestly here as the *definition* of the
search target; **no instance is fabricated** (whether the Bring-level `H_n(ζ)`
carries the required outer derivation is exactly the open `res ≠ 0` — PROBE A).

Base ring generic `{R : Type*} [CommRing R]` (§7c). -/

namespace QOU.Information

open QOU.Machinery.BilinearTrace (IsCyclic)

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]

/-- The **inner derivation** `ad_x : a ↦ x·a − a·x`, as an `R`-linear map. Built
    from `mulLeft x − mulRight x`, so linearity is free. -/
def innerDerivation (x : A) : A →ₗ[R] A :=
  LinearMap.mulLeft R x - LinearMap.mulRight R x

@[simp] theorem innerDerivation_apply (x a : A) :
    innerDerivation (R := R) x a = x * a - a * x := by
  simp [innerDerivation]

/-- **The inner-derivation image lands in `[A,A]` (sorry-free).**  `x·a − a·x` is a
    generator of the commutator submodule. -/
theorem innerDerivation_mem_commutator (x a : A) :
    innerDerivation (R := R) x a ∈ commutatorSubmodule R A := by
  rw [innerDerivation_apply]
  exact Submodule.subset_span ⟨x, a, rfl⟩

/-- **`ad_x` is a derivation (Leibniz rule, sorry-free).**  The defining identity
    of `HH₁`'s inner cocycles: `ad_x(a·b) = ad_x(a)·b + a·ad_x(b)`. -/
theorem innerDerivation_leibniz (x a b : A) :
    innerDerivation (R := R) x (a * b)
      = innerDerivation (R := R) x a * b + a * innerDerivation (R := R) x b := by
  simp only [innerDerivation_apply]
  noncomm_ring

/-- **Every inner derivation is trace-blind (sorry-free).**  For a cyclic
    functional `τ` (`BilinearTrace.IsCyclic`), `τ (ad_x a) = 0`: the inner part of
    `HH₁` lies in `ker τ = [A,A]`, so it is invisible to the entire magnitude/trace
    tower. This is the `HH₁`-level companion of `trace_eq_of_sub_mem_commutator`. -/
theorem trace_comp_innerDerivation_eq_zero (τ : A →ₗ[R] R) (hτ : IsCyclic (⇑τ))
    (x a : A) : τ (innerDerivation (R := R) x a) = 0 := by
  have hmem : innerDerivation (R := R) x a ∈ LinearMap.ker τ :=
    commutatorSubmodule_le_ker_of_trace τ hτ (innerDerivation_mem_commutator x a)
  rwa [LinearMap.mem_ker] at hmem

/-! ### The residue is the OUTER part — the open search target -/

/-- **`D` is an inner derivation** iff it equals `ad_x` for some `x`.  The
    complement — an `R`-linear derivation *not* of this form — is an **outer**
    derivation, i.e. a nonzero class in `HH₁ = Der/Inn`. The decision residue,
    if nonzero, is such an outer class. -/
def IsInnerDerivation (D : A →ₗ[R] A) : Prop := ∃ x : A, D = innerDerivation (R := R) x

/-- **Inner derivations compose to zero with every trace (sorry-free).**  Packaged
    at the level of the functional: `τ ∘ ad_x = 0` as a linear map, for cyclic `τ`.
    A *decision* functional must therefore be sensitive to an **outer** derivation —
    it cannot be a trace (`not_trace_of_separates_commutator`, merged), and the
    derivation it sees cannot be inner. That conjunction — a non-trace functional
    detecting an outer derivation at the fibre level `H_n(ζ)` — is the precise open
    content of `res ≠ 0`. No instance is asserted here. -/
theorem traceComp_innerDerivation_eq_zero (τ : A →ₗ[R] R) (hτ : IsCyclic (⇑τ))
    (x : A) : τ ∘ₗ innerDerivation (R := R) x = 0 := by
  ext a
  simpa using trace_comp_innerDerivation_eq_zero τ hτ x a

end QOU.Information
