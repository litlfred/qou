import Mathlib.Tactic
import Mathlib.Analysis.Real.Hyperreal

/-!
# QOU.AppendixSurreals.BlowupCalculus

**Canonical declaration** for content block at
[`quantum-observable-universe/appendix-surreals/surreal-blowup-calculus.ts`](quantum-observable-universe/appendix-surreals/surreal-blowup-calculus.ts).

Formalises the manuscript **blow-up calculus**: write a divergent expression
`X(Λ)` with `Λ → ω` a named infinite surreal, subtract a counterterm `C(Λ)`
so that `X(ω) − C(ω)` is finite, and take the standard part to obtain the
renormalised real `X_ren := st(X(ω) − C(ω)) ∈ ℝ`.

## Infrastructure — now with a real model (bean `zkst`)

The apparatus is the `BlowupField` typeclass: an ordered field with a
designated positive infinite element `ω`, its infinitesimal `ε = ω⁻¹`, and a
standard-part retraction `st` onto `ℝ`.

**De-axiomatisation (2026-07-06).** This is no longer a free axiom: Mathlib's
hyperreals `ℝ*` are a genuine `BlowupField` instance (`instBlowupFieldHyperreal`
below), so the whole calculus is realisable, not merely conditional. Building
this model also **corrected a latent over-idealisation**: the original
`st_add` was stated *unconditionally*, but no real model satisfies that — the
standard part is additive only on *finite* elements (`st(ω + 1) = 0 ≠ st ω +
st 1 = 1`). `st_add` is now conditioned on an `IsFinite` predicate, matching
`Hyperreal.st_add`; the renormalised value `st(X(ω) − C(ω))` is meaningful
exactly because the counterterm makes `X(ω) − C(ω)` finite.
-/

namespace QOU.AppendixSurreals

/-- **Blow-up infrastructure.** An ordered field `K` with a named positive
    infinite element `omega`, a finiteness predicate `IsFinite`, and a
    standard-part map `st : K → ℝ` that is additive *on finite elements*,
    fixes the natural-number constants, and kills the infinitesimal
    `ε = omega⁻¹`. -/
class BlowupField (K : Type*) [Field K] [LinearOrder K] [IsStrictOrderedRing K] where
  /-- The named infinite surreal `ω`. -/
  omega : K
  /-- `ω` exceeds every natural number — it is infinite. -/
  omega_infinite : ∀ n : ℕ, (n : K) < omega
  /-- The standard-part retraction onto `ℝ`. -/
  st : K → ℝ
  /-- Finiteness predicate (an element with a well-defined standard part). -/
  IsFinite : K → Prop
  /-- `st` is additive **on finite elements** (it is *not* globally additive;
      no real model of a non-archimedean field is). -/
  st_add : ∀ x y : K, IsFinite x → IsFinite y → st (x + y) = st x + st y
  /-- `st` fixes the natural-number constants. -/
  st_natCast : ∀ n : ℕ, st (n : K) = (n : ℝ)
  /-- Natural-number constants are finite. -/
  natCast_isFinite : ∀ n : ℕ, IsFinite (n : K)
  /-- The infinitesimal `ε = ω⁻¹` has standard part `0`. -/
  st_omega_inv : st (omega⁻¹) = 0
  /-- The infinitesimal `ε = ω⁻¹` is finite. -/
  omega_inv_isFinite : IsFinite (omega⁻¹)

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

-- Ref: [leitner2026] quantum-observable-universe/appendix-surreals/surreal-blowup-calculus.ts

/-- When the counterterm cancels the divergence exactly down to a
    natural-number constant `n` — i.e. `X(ω) − C(ω) = n` — the renormalised
    value is that constant. The blow-up calculus at work. -/
theorem renorm_of_natCast
    {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K] [BlowupField K]
    (B : BlowupCalculus K) (n : ℕ)
    (h : B.X BlowupField.omega - B.C BlowupField.omega = (n : K)) :
    B.renormalised = (n : ℝ) := by
  rw [B.renorm_def, h, BlowupField.st_natCast]

/-- **De-axiomatisation (bean `zkst`): the hyperreals `ℝ*` are a genuine
    `BlowupField`.** Every field is a Mathlib theorem — `ω = Hyperreal.omega`
    is infinite (`infinitePos_omega`), `st = Hyperreal.st` is additive on the
    finite (`¬ Infinite`) elements (`Hyperreal.st_add`), fixes real constants
    (`st_id_real`), and kills `ε = ω⁻¹` (`infinitesimal_epsilon`). So the
    blow-up calculus is realisable, not merely axiomatic. -/
noncomputable instance instBlowupFieldHyperreal : BlowupField ℝ* where
  omega := Hyperreal.omega
  omega_infinite n := by
    have h : ((n : ℝ) : ℝ*) < Hyperreal.omega := Hyperreal.infinitePos_omega (n : ℝ)
    exact_mod_cast h
  st := Hyperreal.st
  IsFinite x := ¬ x.Infinite
  st_add _ _ hx hy := Hyperreal.st_add hx hy
  st_natCast n := by
    have h : Hyperreal.st ((n : ℝ) : ℝ*) = (n : ℝ) := Hyperreal.st_id_real (n : ℝ)
    exact_mod_cast h
  natCast_isFinite n := by
    have h : ¬ (((n : ℝ) : ℝ*)).Infinite := (Hyperreal.isSt_refl_real (n : ℝ)).not_infinite
    exact_mod_cast h
  st_omega_inv := by
    have hωε : (Hyperreal.omega)⁻¹ = Hyperreal.epsilon := by
      rw [← Hyperreal.inv_epsilon, inv_inv]
    rw [hωε]
    exact Hyperreal.IsSt.st_eq Hyperreal.infinitesimal_epsilon
  omega_inv_isFinite := by
    have hωε : (Hyperreal.omega)⁻¹ = Hyperreal.epsilon := by
      rw [← Hyperreal.inv_epsilon, inv_inv]
    rw [hωε]
    exact Hyperreal.infinitesimal_epsilon.not_infinite

end QOU.AppendixSurreals
