import Mathlib.Tactic

/-!
# QOU.AppendixSurreals.BlowupCalculus

**Canonical declaration** for content block at
[`quantum-observable-universe/appendix-surreals/surreal-blowup-calculus.ts`](quantum-observable-universe/appendix-surreals/surreal-blowup-calculus.ts).

Formalises the manuscript **blow-up calculus**: write a divergent expression
`X(Λ)` with `Λ → ω` a named infinite surreal, subtract a counterterm `C(Λ)`
so that `X(ω) − C(ω)` is finite, and take the standard part to obtain the
renormalised real `X_ren := st(X(ω) − C(ω)) ∈ ℝ`.

## Needed infrastructure

Conway's `No` is the intended model, but the surreal cone is outside the
Mathlib subset available here, so the infrastructure the calculus actually
uses is axiomatised directly as a `BlowupField` typeclass: an ordered field
with a designated positive infinite element `ω`, its infinitesimal
`ε = ω⁻¹`, and a standard-part retraction `st` onto `ℝ`. A `BlowupCalculus`
datum over such a field is then a rigorous *conditional* construction — every
step is literal (the cutoff `ω` is a specific element, the counterterm a
specific function, the standard part a specific real). `No`, the hyperreals,
and the Levi-Civita field are models of `BlowupField`.
-/

namespace QOU.AppendixSurreals

/-- **Blow-up infrastructure.** An ordered field `K` with a named positive
    infinite element `omega` and a standard-part map `st : K → ℝ` that is
    additive, fixes the natural-number constants, and kills the infinitesimal
    `ε = omega⁻¹`. This is exactly the apparatus the surreal blow-up calculus
    relies on. -/
class BlowupField (K : Type*) [Field K] [LinearOrder K] [IsStrictOrderedRing K] where
  /-- The named infinite surreal `ω`. -/
  omega : K
  /-- `ω` exceeds every natural number — it is infinite. -/
  omega_infinite : ∀ n : ℕ, (n : K) < omega
  /-- The standard-part retraction onto `ℝ`. -/
  st : K → ℝ
  /-- `st` is additive on `K`. -/
  st_add : ∀ x y : K, st (x + y) = st x + st y
  /-- `st` fixes the natural-number constants. -/
  st_natCast : ∀ n : ℕ, st (n : K) = (n : ℝ)
  /-- The infinitesimal `ε = ω⁻¹` has standard part `0`. -/
  st_omega_inv : st (omega⁻¹) = 0

namespace BlowupField

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K] [BlowupField K]

/-- The infinitesimal `ε = 1/ω`. -/
def epsilon : K := (omega : K)⁻¹

/-- The infinitesimal has vanishing standard part. -/
@[simp] theorem st_epsilon : st (epsilon : K) = 0 := st_omega_inv

/-- `ω` is positive (it exceeds `0`). -/
theorem omega_pos : 0 < (omega : K) := by
  have h : ((0 : ℕ) : K) < omega := omega_infinite 0
  simpa using h

end BlowupField

/-- Data for a blow-up renormalisation over a `BlowupField K`.

    A `definition` carrier: the divergent expression `X` and counterterm `C`
    as functions of the cutoff, together with the renormalised real pinned to
    the standard part of `X(ω) − C(ω)`. -/
structure BlowupCalculus (K : Type*) [Field K] [LinearOrder K] [IsStrictOrderedRing K] [BlowupField K] where
  /-- The divergent expression as a function of the cutoff `Λ`. -/
  X : K → K
  /-- The counterterm as a function of the cutoff `Λ`. -/
  C : K → K
  /-- The renormalised real value. -/
  renormalised : ℝ
  /-- Defining identity: `X_ren = st(X(ω) − C(ω))`. -/
  renorm_def :
    renormalised = BlowupField.st (X BlowupField.omega - C BlowupField.omega)

-- Ref: [manuscript] quantum-observable-universe/appendix-surreals/surreal-blowup-calculus.ts

/-- When the counterterm cancels the divergence exactly down to a
    natural-number constant `n` — i.e. `X(ω) − C(ω) = n` — the renormalised
    value is that constant. The blow-up calculus at work. -/
theorem BlowupCalculus.renorm_of_natCast
    {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K] [BlowupField K]
    (B : BlowupCalculus K) (n : ℕ)
    (h : B.X BlowupField.omega - B.C BlowupField.omega = (n : K)) :
    B.renormalised = (n : ℝ) := by
  rw [B.renorm_def, h, BlowupField.st_natCast]

end QOU.AppendixSurreals
