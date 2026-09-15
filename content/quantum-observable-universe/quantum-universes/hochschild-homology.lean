import QOU.Information.CocenterTraceFactor

/-!
# Hochschild homology: the degree-zero group as the cocenter

Sibling of `def:hochschild-homology`. The definition block introduces the Hochschild
homology `HH_•(A)` of an associative algebra `A` over a commutative ring `R` (Loday,
Ch. 1); this file carries the part that is formalised in the corpus, which is the
degree-zero group and the one property of it that the paper uses.

* `HochschildZero R A = A / [A, A]`, the cocenter, re-exported from
  `QOU.Information.cocenter` (the commutator submodule is the `R`-span of the
  `a·b − b·a`).
* `hochschildClass` sends `a` to its class; `hochschildClass_mul_comm` is the
  degree-zero trace property `[ab] = [ba]`, which is what makes every cyclic
  functional factor through `HH_0` (`traceOnHochschildZero`, from
  `QOU.Information.traceCocenter`).

The higher groups `HH_n`, the Connes operator `B` and the HKR isomorphism are cited
in the block (`rem:hkr-theorem`), not formalised. Base ring generic (§7c).

-- Ref: [loday-1998] https://doi.org/10.1007/978-3-662-11389-9
-/

namespace QOU.QuantumUniverses

open QOU.Machinery.BilinearTrace (IsCyclic)

variable (R : Type*) [CommRing R] (A : Type*) [Ring A] [Algebra R A]

/-- **Hochschild homology in degree zero**: the cocenter `HH_0(A) = A / [A, A]`. -/
abbrev HochschildZero : Type _ := QOU.Information.cocenter R A

/-- The class of `a` in `HH_0(A)`. -/
def hochschildClass (a : A) : HochschildZero R A :=
  Submodule.Quotient.mk a

variable {R A}

/-- **The degree-zero trace property (sorry-free).** `[a·b] = [b·a]` in `HH_0(A)`,
because `a·b − b·a` generates the commutator submodule. -/
theorem hochschildClass_mul_comm (a b : A) :
    hochschildClass R A (a * b) = hochschildClass R A (b * a) := by
  unfold hochschildClass
  rw [Submodule.Quotient.eq]
  exact Submodule.subset_span ⟨a, b, rfl⟩

/-- A cyclic functional `τ` (`τ(ab) = τ(ba)`) descends to `HH_0(A)`: the trace is a
function of the Hochschild class alone. -/
noncomputable def traceOnHochschildZero (τ : A →ₗ[R] R) (hτ : IsCyclic (⇑τ)) :
    HochschildZero R A →ₗ[R] R :=
  QOU.Information.traceCocenter τ hτ

@[simp] theorem traceOnHochschildZero_class (τ : A →ₗ[R] R) (hτ : IsCyclic (⇑τ)) (a : A) :
    traceOnHochschildZero τ hτ (hochschildClass R A a) = τ a :=
  rfl

end QOU.QuantumUniverses
