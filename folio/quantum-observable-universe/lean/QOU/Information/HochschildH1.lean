import QOU.Information.OuterDerivationResidue
import Mathlib.Algebra.Algebra.Bilinear

/-!
# QOU.Information.HochschildH1 — first Hochschild cohomology `HH¹(A) = Der(A)/Inn(A)`

Mathlib's `Derivation R A M` is built for a **commutative** base algebra `A` acting
on a one-sided module `M`; it does not cover the noncommutative associative
`A`-bimodule derivations whose quotient by inner derivations is `HH¹(A)`. This
file supplies that infrastructure for any associative `R`-algebra `A`:

* `IsDerivation D` — the Leibniz predicate on `D : A →ₗ[R] A`;
* `derivationSubmodule` — the `R`-submodule `Der(A) ⊆ A →ₗ[R] A` of all derivations;
* `innerMap` / `innerDerivationSubmodule` — the inner derivations `Inn(A)` as the
  `R`-linear range of `x ↦ ad_x`;
* `inner_le_der : Inn(A) ≤ Der(A)`;
* `HH1 R A := Der(A) ⧸ Inn(A)` — the first Hochschild cohomology, as an `R`-module.

This makes precise the objects the P-vs-NP residue lives among (`OuterDerivationResidue`):
the decision residue is a **nonzero class in `HH1`**, and PROBE A's computation
`dim HH1(H₃(ζ)) = 1` (root of unity) vs `= 0` (generic) is a statement about this
very quotient. Generic `{R : CommRing} {A : Ring} [Algebra R A]`.  NOT sorry-free:
the file carries `sorry` (8 as of 2026-09-15), each with its `-- Ref:`; the header
claimed otherwise until then. -/

namespace QOU.Information

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]

/-- **`D` is a derivation** — the associative-algebra Leibniz rule. -/
def IsDerivation (D : A →ₗ[R] A) : Prop := ∀ a b : A, D (a * b) = D a * b + a * D b

variable (R A) in
/-- **The derivation submodule `Der(A) ⊆ A →ₗ[R] A` (sorry-free).**  Closed under
    `0`, `+`, and `R`-scalars — the scalar case uses `smul_mul_assoc` /
    `mul_smul_comm` (the algebra scalar slides through the product). -/
def derivationSubmodule : Submodule R (A →ₗ[R] A) where
  carrier := {D | IsDerivation D}
  zero_mem' := by intro a b; simp
  add_mem' := by
    intro D D' hD hD' a b
    simp only [LinearMap.add_apply, hD a b, hD' a b, add_mul, mul_add]
    abel
  smul_mem' := by
    intro r D hD a b
    simp only [LinearMap.smul_apply, hD a b, smul_add, smul_mul_assoc, mul_smul_comm]

theorem mem_derivationSubmodule {D : A →ₗ[R] A} :
    D ∈ derivationSubmodule R A ↔ IsDerivation D := Iff.rfl

variable (R A) in
/-- **Inner derivations as an `R`-linear map `x ↦ ad_x`.**  Built from the
    multiplication bilinear map, so it is linear in `x` for free; its range is the
    submodule `Inn(A)`. -/
def innerMap : A →ₗ[R] (A →ₗ[R] A) := LinearMap.mul R A - (LinearMap.mul R A).flip

@[simp] theorem innerMap_apply (x a : A) : innerMap R A x a = x * a - a * x := by
  simp [innerMap]

theorem innerMap_eq_innerDerivation (x : A) :
    innerMap R A x = innerDerivation (R := R) x := by
  ext a; simp

variable (R A) in
/-- **The inner-derivation submodule `Inn(A) ⊆ A →ₗ[R] A` (sorry-free).** -/
def innerDerivationSubmodule : Submodule R (A →ₗ[R] A) :=
  LinearMap.range (innerMap R A)

/-- **`ad_x` really is a derivation (sorry-free).** -/
theorem innerDerivation_isDerivation (x : A) :
    IsDerivation (innerDerivation (R := R) x) := innerDerivation_leibniz x

/-- **`Inn(A) ≤ Der(A)` (sorry-free).**  Every inner derivation is a derivation. -/
theorem inner_le_der :
    innerDerivationSubmodule R A ≤ derivationSubmodule R A := by
  rintro D ⟨x, rfl⟩
  rw [mem_derivationSubmodule, innerMap_eq_innerDerivation]
  exact innerDerivation_isDerivation x

variable (R A) in
/-- **The endomorphism space modulo inner derivations, `E/Inn(A)`.**  The ambient
    quotient in which `HH¹` is realized. (Working with this ambient quotient
    avoids the instance diamond that a linear-map-space *sub*quotient
    `↥Der ⧸ Inn` triggers; since `Inn ≤ Der` the image of `Der` here is
    canonically `Der/Inn`.) -/
abbrev DerivationQuotient : Type _ :=
  (A →ₗ[R] A) ⧸ innerDerivationSubmodule R A

variable (R A) in
/-- **First Hochschild cohomology `HH¹(A) = Der(A)/Inn(A)`**, realized as the
    **image of `Der(A)` in `E/Inn(A)`** — the home of the P-vs-NP decision
    residue. Because `Inn(A) ≤ Der(A)` (`inner_le_der`), this image is canonically
    the subquotient `Der/Inn`. -/
def HH1 : Submodule R (DerivationQuotient R A) :=
  (derivationSubmodule R A).map (innerDerivationSubmodule R A).mkQ

/-- **The class of a linear map in `E/Inn(A)`.**  For a *derivation* `D` this class
    lands in `HH1` (`hh1Class_mem_of_isDerivation`); the decision residue being
    nonzero (`res ≠ 0`) is exactly: some derivation at the fibre level `H_n(ζ)` has
    **nonzero** class — an outer derivation. (No such class is constructed here;
    PROBE A computes `dim HH1(H₃(ζ)) = 1`.) -/
noncomputable def hh1Class (D : A →ₗ[R] A) : DerivationQuotient R A :=
  (innerDerivationSubmodule R A).mkQ D

/-- **Inner derivations are exactly the trivial classes (sorry-free).**  If `D` is
    inner, its class in `E/Inn` vanishes — the quotient really does kill `Inn(A)`. -/
theorem hh1Class_eq_zero_of_inner (D : A →ₗ[R] A)
    (hD : D ∈ innerDerivationSubmodule R A) : hh1Class D = 0 := by
  rw [hh1Class, Submodule.mkQ_apply, Submodule.Quotient.mk_eq_zero]
  exact hD

/-- **A derivation's class lies in `HH¹` (sorry-free).**  The image of `Der(A)` in
    `E/Inn(A)` is exactly `HH1`, so every derivation contributes a class there. -/
theorem hh1Class_mem_of_isDerivation (D : A →ₗ[R] A) (hD : IsDerivation D) :
    hh1Class D ∈ HH1 R A :=
  Submodule.mem_map_of_mem ((mem_derivationSubmodule).2 hD)

/-- **An outer derivation is a nonzero `HH¹` class (sorry-free).**  Contrapositive
    packaging: if a derivation's class is nonzero it is **not** inner — the precise
    shape of the decision residue `res ≠ 0`. -/
theorem not_inner_of_hh1Class_ne_zero (D : A →ₗ[R] A)
    (h : hh1Class D ≠ 0) : D ∉ innerDerivationSubmodule R A :=
  fun hD => h (hh1Class_eq_zero_of_inner D hD)

end QOU.Information
