/-
# The duality intertwiner IS an invariant sesquilinear form, and it normalises Hermitian

Formalises the two steps of `computations/ptolemy/ptolemy_duality_hermitian_form.py`
that are THEOREMS.  The third step of that probe -- reading the SIGNATURE, which is
what makes `sigma = complex conjugation` do any work -- is archimedean and is not
formalised here; see the `## Scope` note at the bottom, which says so explicitly
rather than letting the file's silence imply more than it proves.

Everything below is over a general `CommRing R` with an arbitrary ring endomorphism
`sigma`.  Nothing needs `sigma` to be complex conjugation, nothing needs `R` to be a
field, and nothing needs an embedding into `C`.  That generality is the POINT: it
localises exactly which part of the story is algebra (all of it, down here) and which
part needs the archimedean place (the signature, up there).

`QOU.Eightfold` is the home of the corpus's real-structure arc
(`AmphichiralHolonomyIsSelfDual`, `ObstructionClassForcesComplexType`,
`SymSquareHolonomyIsRealType`), which is where this belongs.
-/
import Mathlib.Data.Matrix.Basic
import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic.Ring

namespace QOU.Eightfold

open Matrix

variable {R : Type*} [CommRing R] {n : Type*}

/-- **STEP 1 — the intertwiner relation is an invariant-form relation.**

The duality datum is an invertible `A` with `A * sigma(M) * A⁻¹ = (Mᵀ)⁻¹` for every
group element `M` in the image of the representation.  Written without the inverse of
`A`, and with `Minv` standing for `(Mᵀ)⁻¹`, that is `A * sigma(M) = Minv * A`.

This lemma is the one line of rearrangement that turns it into
`Mᵀ * A * sigma(M) = A`, i.e. into the statement that the sesquilinear form
`H(v, w) = vᵀ A sigma(w)` is invariant under `v, w ↦ M v, M w`.

No hypothesis on `sigma` at all -- not even additivity is used beyond its being a
ring hom, and involutivity is NOT needed here.  The content is entirely that
`Mᵀ * Minv = 1`. -/
theorem invariantForm_of_intertwiner [Fintype n] [DecidableEq n]
    (σ : R →+* R) (A M Minv : Matrix n n R)
    (hMinv : Mᵀ * Minv = 1)
    (h : A * M.map σ = Minv * A) :
    Mᵀ * A * M.map σ = A := by
  calc Mᵀ * A * M.map σ = Mᵀ * (A * M.map σ) := by rw [Matrix.mul_assoc]
    _ = Mᵀ * (Minv * A) := by rw [h]
    _ = (Mᵀ * Minv) * A := by rw [Matrix.mul_assoc]
    _ = 1 * A := by rw [hMinv]
    _ = A := Matrix.one_mul A

/-- **STEP 2a — Hilbert 90, constructively, for a norm-one scalar.**

If `sigma` is an involution and `N(c) = sigma c * c = 1`, then `c` is a ratio
`d / sigma d`, and a witness `d` is produced rather than merely asserted to exist:
`d := x + c * sigma x` works for every `x`.

This is the classical Hilbert-90 argument for a degree-2 extension, and it is the
step that makes the Hermitian normalisation below CONSTRUCTIVE.  Note the conclusion
is stated as `sigma d * c = d`, which is the form the matrix lemma consumes, and
which avoids having to know `d ≠ 0` to state it.  Nondegeneracy of `d` is a separate
matter and is exactly what the caller must check. -/
theorem hilbert90_witness (σ : R →+* R) (hσ : ∀ x, σ (σ x) = x)
    (c x : R) (hc : σ c * c = 1) :
    σ (x + c * σ x) * c = x + c * σ x := by
  have hexp : σ (x + c * σ x) = σ x + σ c * x := by
    rw [map_add, map_mul, hσ]
  rw [hexp]
  have hsplit : (σ x + σ c * x) * c = σ x * c + (σ c * c) * x := by ring
  rw [hsplit, hc, one_mul]
  ring

/-- **STEP 2b — the Hermitian normalisation.**

Write `A† := (Aᵀ).map sigma`.  The form `H(v,w) = vᵀ A sigma(w)` is sigma-Hermitian
exactly when `A† = A`.

Schur gives `A† = c • A` for a scalar `c` (the invariant form is unique up to a
scalar, so `A†`, being invariant too, is a multiple of `A`).  Given any `d` with
`sigma d * c = d` -- which `hilbert90_witness` supplies -- the rescaled matrix
`d • A` is Hermitian on the nose.

No hypothesis that `d ≠ 0`: the identity holds regardless, and it is the caller's
job to pick an `x` making the witness nonzero.  That is honest about where the work
is: existence of a NONDEGENERATE Hermitian representative needs `d ≠ 0`, which is a
genericity statement, not an identity. -/
theorem hermitian_of_hilbert90_witness
    (σ : R →+* R) (A : Matrix n n R) (c d : R)
    (hA : (Aᵀ).map σ = c • A) (hd : σ d * c = d) :
    (((d • A))ᵀ).map σ = d • A := by
  have htr : ((d • A))ᵀ = d • Aᵀ := Matrix.transpose_smul d A
  have hmap : (d • Aᵀ).map σ = σ d • (Aᵀ).map σ := by
    ext i j
    simp [Matrix.map_apply, Matrix.smul_apply, map_mul]
  calc (((d • A))ᵀ).map σ = (d • Aᵀ).map σ := by rw [htr]
    _ = σ d • (Aᵀ).map σ := hmap
    _ = σ d • (c • A) := by rw [hA]
    _ = (σ d * c) • A := by rw [smul_smul]
    _ = d • A := by rw [hd]

/-- **STEP 2, assembled.**  From an intertwiner whose `dagger` is a scalar multiple
of itself, and an involutive `sigma`, a Hermitian representative is produced.

The norm-one condition `sigma c * c = 1` is not assumed here -- it is DERIVED in the
probe by applying `dagger` twice -- but it is what makes the Hilbert-90 witness
available, so it appears as a hypothesis. -/
theorem hermitian_representative
    (σ : R →+* R) (hσ : ∀ x, σ (σ x) = x)
    (A : Matrix n n R) (c x : R)
    (hA : (Aᵀ).map σ = c • A) (hc : σ c * c = 1) :
    ((((x + c * σ x) • A))ᵀ).map σ = (x + c * σ x) • A :=
  hermitian_of_hilbert90_witness σ A c _ hA (hilbert90_witness σ hσ c x hc)

/-!
## Scope — what this file does NOT prove

Stated here rather than left to inference, because the interesting claim is the one
that is missing.

1. **No signature.**  Everything above holds for ANY ring endomorphism `sigma`, so
   nothing above singles out complex conjugation.  What conjugation supplies is an
   archimedean invariant: under an embedding `K ↪ ℂ` at which `sigma` acts as
   conjugation, `dagger` becomes the conjugate transpose, the Hermitian matrix has
   real eigenvalues, and a SIGNATURE `(p, q)` exists.  For an abstract involution
   there is no signature.  That step is measured -- `(2,1)` at every embedding on
   all four exact points the corpus holds -- and is not formalised here.

2. **No derivation that `sigma` MUST be conjugation.**  The probe measures that the
   winning automorphism is conjugation; this file explains what such a `sigma` gives
   you once you have it.  The implication in the other direction is open.

3. **No connection to the categorical Lagrangian `ℒ_q`.**  Measured 2026-09-14
   across all six corpus-grep paths: the corpus's reality/conjugation arc and its
   Lagrangian arc do not touch anywhere -- zero matches in either direction.  In
   particular `ψ* = ∫_A ∘ S(ψ)` puts the antipode `S` inside `ℒ_q`, but the QOU
   Frobenius–Hopf substrate nowhere asserts `S² = id`, so `S` is not known to be an
   involution and this file's `hσ` hypothesis has no supplier upstream.

-/

end QOU.Eightfold
