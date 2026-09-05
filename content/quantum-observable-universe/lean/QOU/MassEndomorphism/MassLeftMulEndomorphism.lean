import Mathlib.Algebra.Algebra.Bilinear
import Mathlib.Algebra.Module.End

/-!
# QOU.MassEndomorphism.MassLeftMulEndomorphism — the element *is* an endomorphism

The chapter names its central object "the mass endomorphism", yet the Hecke
mass element `Φ_mass(β) ∈ H_n(R, q)` is an **element** of the Hecke algebra,
not a map (see `MassEndomorphismConjecture.lean`, where `Phi_mass : A`).  This
file supplies the minimal, always-available bridge that earns the name: the
**faithful left-regular representation** of a unital `R`-algebra.

For any unital `R`-algebra `A`, an element `a : A` acts by left multiplication
`L_a = LinearMap.mulLeft R a : Module.End R A`, and the map `a ↦ L_a` is
**injective** (evaluate at `1`: `L_a 1 = a`).  So every Hecke mass element is
faithfully a genuine module endomorphism `A → A`.

This is the Frobenius-algebra sense of "element as endomorphism"
(Kock, *Frobenius Algebras and 2D TQFT*), and it is the sense that holds
unconditionally, because `a ↦ L_a` is injective.

A second sense is `q`-Schur–Weyl, and it is **weaker, not sharper**: the arrow
`H_n(q) ↠ End_{U_q 𝔰𝔩_N}(V^⊗ⁿ)` (Jimbo) is a **surjection**, an isomorphism
only when `N ≥ n`.  Below that its kernel is the span of the blocks with more
than `N` rows, so a Hecke element in the kernel maps to the *zero* endomorphism
of `V^⊗ⁿ` — it is not "literally an endomorphism" of it in any faithful sense.
This framework runs at `N = 2` (convention D) with `n = 3A`, where the image is
`TL_n(q) = End_{U_q 𝔰𝔩₂}(V^⊗ⁿ)`, of dimension `Catalan(n)` against
`dim H_n = n!` — a kernel of dimension `n! - Catalan(n)` = 1, 10, 78, 588,
4611, 38890 at `n = 3..8`.  See `QOU.QBeta.TraceBlindSector` (which states the
`TL_n` identification) and `QOU.QuantumObservableUniverses.QSchurWeyl` (which
correctly says *the image of* `H_n(q)`).

> **Trace caveat (NOT proved here — deliberately).**  The Markov trace
> `tr_M : A → R` is the **quantum** trace (Ocneanu weights / ribbon twist),
> **not** the regular-representation trace `tr(L_a)`.  So this file proves only
> that the element *is* an endomorphism (faithfulness); it does **not** claim
> `tr_M(a) = LinearMap.trace R A (L_a)`.  The identification of `tr_M` with the
> quantum trace of the mass endomorphism is the Reshetikhin–Turaev long-knot
> statement, cited in the narrative, not formalised here.

-- Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443
-- Ref: [jimbo1986] https://doi.org/10.1007/BF00704588
LaTeX label: `def:mass-left-mul-endomorphism`
-/

namespace QOU.MassEndomorphism

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]

/-- **The mass element as a genuine endomorphism.**  Left multiplication by
    `a : A` (in particular by the Hecke mass element `Φ_mass(β)`) is a module
    endomorphism `A → A`.  This is the object the chapter calls "the mass
    endomorphism". -/
def massLeftMul (a : A) : Module.End R A := LinearMap.mulLeft R a

@[simp] theorem massLeftMul_apply (a x : A) : massLeftMul (R := R) a x = a * x :=
  rfl

/-- Evaluating the endomorphism at `1` recovers the element. -/
@[simp] theorem massLeftMul_one (a : A) : massLeftMul (R := R) a 1 = a := by
  simp

/-- **Faithfulness.**  The regular representation `a ↦ L_a` is injective, so the
    Hecke mass element is *faithfully* realised as a module endomorphism — the
    name "mass endomorphism" is honest under this identification. -/
theorem massLeftMul_injective :
    Function.Injective (fun a : A => massLeftMul (R := R) a) := by
  intro a b h
  have h1 : massLeftMul (R := R) a 1 = massLeftMul (R := R) b 1 :=
    congrArg (fun f : Module.End R A => f 1) h
  simpa using h1

end QOU.MassEndomorphism
