/-
# B2 sub-piece (ii): S₅-equivariance ⇒ τ(Markov Gram) ∝ Hodge Gram

The α_EM B2 wall (`prop:em-coupling-bring-zero-mode`, epic `qou-6ufi`) is
`τ(Markov Gram) = c · Hodge Gram`. Option B (#4160) forced proportionality *from*
Schur; PR #4182 discharged its scalar-commutant hypothesis from irreducibility
(`MatrixSchurCommutant.commutant_scalar_of_irreducible`). The two remaining open
sub-pieces were (i) scalar-commutant [done, #4182] and **(ii) the τ-image is
S₅-equivariant on `std`**. This file formalizes the *logical role* of (ii): it
proves that S₅-equivariance of the τ-map (an intertwiner between the Hecke and
S₅ actions on `std`) is EXACTLY what turns the Markov Gram into an S₅-invariant
form, which then — with (i) + Schur — is `∝` the Hodge Gram.

Two results (sorry-free, `lean`-direct):

* `invariantForm_pullback` — **transport of an invariant form along an
  intertwiner.** If `P` intertwines two representations (`ρH s * P = P * ρS s`)
  and `M` is `ρH`-invariant, then `Pᵀ * M * P` is `ρS`-invariant. (No
  invertibility needed for this direction.)
* `tauImage_proportional_hodge` — **the (ii)⇒proportionality assembly.** Given a
  `TauStdIntertwiner` (the τ-map on `std`), the `ρS = S₅`-irreducibility (⇒
  scalar commutant, via #4182), a unit Hodge form, and the two invariant forms,
  the pulled-back Markov Gram `Pᵀ · G_M · P` is `= c • G_H` for some scalar `c`.

**The open categorical input, made precise and NOT fabricated (STRICT,
§"Axiomatization is NOT a Proof").** The hypothesis is a `TauStdIntertwiner`:
an invertible `P` with `ρH s * P = P * ρS s`. Existence of *some* such `P` is
standard (Tits deformation: `H₅(q)` is semisimple and its `(4,1)` block is the
abstract irreducible `(4,1)`, ≅ the S₅ `(4,1)`). The genuinely-open claim is that
the QOU **archimedean functor τ** *is* such an intertwiner on `std` — a statement
about the actual categorical/archimedean functor, not a matrix identity. **No
`TauStdIntertwiner` instance for the actual τ is registered**; this file proves
only the conditional. `1/(8π)` stays a phase-4 identification; nothing is wired.

-- Ref: [manuscript] prop:em-coupling-bring-zero-mode
-- Ref: [serre1977] Linear Representations of Finite Groups (Schur; Tits deformation)
-/
import QOU.Archimedean.SchurInvariantFormProportional
import QOU.Archimedean.MatrixSchurCommutant

namespace QOU.Archimedean.TauS5EquivarianceReduction

open Matrix
open QOU.Archimedean.SchurInvariantFormProportional
open QOU.Archimedean.MatrixSchurCommutant

variable {n : Type*} [Fintype n] [DecidableEq n] {k : Type*} [Field k]
variable {G : Type*}

omit [DecidableEq n] in
/-- **Transport of an invariant form along an intertwiner.** If `P` intertwines
`ρH` and `ρS` (`ρH s * P = P * ρS s`) and `M` is a `ρH`-invariant form, then
`Pᵀ * M * P` is a `ρS`-invariant form. This is the linear-algebra content of
"an S₅-equivariant τ carries the Markov Gram to an S₅-invariant form." -/
theorem invariantForm_pullback {ρS ρH : G → Matrix n n k} {P : Matrix n n k}
    (hP : ∀ s, ρH s * P = P * ρS s) {M : Matrix n n k}
    (hM : InvariantForm ρH M) :
    InvariantForm ρS (Pᵀ * M * P) := by
  intro s
  -- transpose of the intertwiner: `(ρS s)ᵀ * Pᵀ = Pᵀ * (ρH s)ᵀ`
  have hPt : (ρS s)ᵀ * Pᵀ = Pᵀ * (ρH s)ᵀ := by
    rw [← Matrix.transpose_mul, ← Matrix.transpose_mul, hP s]
  calc (ρS s)ᵀ * (Pᵀ * M * P) * (ρS s)
      = ((ρS s)ᵀ * Pᵀ) * M * (P * (ρS s)) := by
        simp only [Matrix.mul_assoc]
    _ = (Pᵀ * (ρH s)ᵀ) * M * (ρH s * P) := by rw [hPt, ← hP s]
    _ = Pᵀ * ((ρH s)ᵀ * M * (ρH s)) * P := by simp only [Matrix.mul_assoc]
    _ = Pᵀ * M * P := by rw [hM s]

/-- **The τ-map on the `std` block (the open categorical input of sub-piece ii).**
An invertible `P` intertwining the Hecke action `ρH` and the S₅ action `ρS`:
`ρH s * P = P * ρS s`. Existence of some such `P` is standard (Tits deformation);
the OPEN claim is that the QOU archimedean functor τ realizes it. No instance for
the actual τ is registered here. -/
structure TauStdIntertwiner (ρS ρH : G → Matrix n n k) where
  /-- The intertwiner matrix (the τ-map restricted to `std`). -/
  P : Matrix n n k
  /-- `P` is invertible (the τ-map is an isomorphism on the block). -/
  isUnit : IsUnit P.det
  /-- Intertwining relation between the two generator actions. -/
  intertwines : ∀ s, ρH s * P = P * ρS s

/-- **Sub-piece (ii) ⇒ proportionality.** Given the τ-intertwiner on `std`, the
irreducibility of the S₅ action `ρS` (which discharges the scalar-commutant
hypothesis via #4182), a unit Hodge form `G_H`, and the invariance of both the
Hodge form (for `ρS`) and the Markov Gram `G_M` (for `ρH`), the τ-image of the
Markov Gram `Pᵀ * G_M * P` is a scalar multiple of the Hodge form.

STRICT: `τ` here is the `TauStdIntertwiner` *hypothesis*; no instance for the
actual archimedean functor is exhibited. This is the §3b-cond conditional result
— rigorous modulo the single named categorical input. -/
theorem tauImage_proportional_hodge [IsAlgClosed k] [Nonempty n]
    {ρS ρH : G → Matrix n n k}
    (hirr : IsIrreducibleRep ρS)
    (hρS : ∀ s, IsUnit (ρS s).det)
    (τ : TauStdIntertwiner ρS ρH)
    {G_H G_M : Matrix n n k} (hHodge : IsUnit G_H.det)
    (hHodge_inv : InvariantForm ρS G_H) (hMarkov_inv : InvariantForm ρH G_M) :
    ∃ c : k, (τ.P)ᵀ * G_M * τ.P = c • G_H := by
  -- the pulled-back Markov Gram is a `ρS`-invariant form
  have hpull : InvariantForm ρS ((τ.P)ᵀ * G_M * τ.P) :=
    invariantForm_pullback τ.intertwines hMarkov_inv
  -- discharge the Schur scalar-commutant hypothesis from irreducibility (#4182)
  have schur : ∀ A : Matrix n n k,
      (∀ s, A * (ρS s) = (ρS s) * A) → ∃ c : k, A = c • (1 : Matrix n n k) :=
    fun A hA => commutant_scalar_of_irreducible hirr hA
  -- two `ρS`-invariant forms on an irreducible rep are proportional (#4160)
  exact invariantForm_proportional_of_commutantScalar hρS schur hHodge hHodge_inv hpull

end QOU.Archimedean.TauS5EquivarianceReduction
