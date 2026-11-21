/-
# B2 sub-piece (ii): S₅-equivariance ⇒ τ(Markov Gram) ∝ Hodge Gram

The α_EM B2 wall (`prop:em-coupling-bring-zero-mode`, epic `qou-6ufi`) is
`τ(Markov Gram) = c · Hodge Gram`. Option B (#4160) forced proportionality *from*
Schur; PR #4182 discharged its scalar-commutant hypothesis from irreducibility
(`MatrixSchurCommutant.commutant_scalar_of_irreducible`). The two remaining open
sub-pieces were (i) scalar-commutant [done, #4182] and **(ii) the τ-image is
S₅-equivariant on `std`**.

**CORRECTION (2026-07-25).** An earlier version of this file (merged in #4182)
framed (ii) as a *generator*-level intertwiner `ρH s * P = P * ρS s` between the
Hecke and S₅ actions and claimed `tauImage_proportional_hodge` "reduced" (ii).
**That framing was wrong: the generator-intertwiner is UNSATISFIABLE at
`q₀ ≠ 1`.** The Hecke generator `σ₁` on `std` has eigenvalues `q₀,q₀,q₀,−q₀⁻¹`
(trace `≈ 2.43`); an S₅ transposition has eigenvalues `1,−1,…` (trace `2`);
differing spectra ⇒ no conjugating `P` (`intertwiner_trace_eq`). So the old
conditional was true-but-vacuous, not a reduction (per "conditional-proved ≠
premise-established"). The correct τ-correspondence is the **Tits `*`-algebra
iso** `H₅(q₀) ≅ ℂ[S₅]` on the `(4,1)` block — a Skolem–Noether conjugator sending
`σᵢ` to a *non-generator* element — which this file does **not** yet formalize;
that remains the open work of (ii).

What this file now provides (sorry-free, `lean`-direct):

* `invariantForm_pullback` — **transport of an invariant form along an
  intertwiner** (true general linear algebra, reusable): `P` intertwines `ρH,ρS`
  and `M` is `ρH`-invariant ⇒ `Pᵀ * M * P` is `ρS`-invariant.
* `intertwiner_trace_eq` — **the obstruction**: a generator-intertwiner forces
  `trace (ρH s) = trace (ρS s)`; ruled out for Hecke/S₅ (`2.43 ≠ 2`).
* `tauImage_proportional_hodge` — the general-`P` assembly, explicitly flagged as
  **not** a reduction of (ii) (its `GeneratorIntertwiner` premise is the
  obstructed one).
* `HeckeSideS5Symmetry` + `markovGram_transports_to_hodge` — the **correct,
  SATISFIABLE** reduction: an S₅ action `ρS'` on the Hecke space leaving the Markov
  Gram invariant, conjugate to the geometric S₅. `ρS'` and `ρS` share the `(4,1)`
  character (no trace obstruction), so this premise CAN hold — it is the honest
  Tits-`*`-iso content. Given it, `Tᵀ · G_Markov · T = c • G_Hodge`.

STRICT (§"Axiomatization is NOT a Proof"): no `HeckeSideS5Symmetry` instance for
the actual τ is registered; sub-piece (ii) is honestly OPEN — the remaining input
is the existence of the Tits-transported S₅ symmetry with `T = τ` (the archimedean
functor). `1/(8π)` stays a phase-4 identification; nothing wired.

-- Ref: [leitner2026] prop:em-coupling-bring-zero-mode
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

/-- **A generator-level intertwiner** `P` between two actions `ρH`, `ρS`:
`ρH s * P = P * ρS s`, `P` invertible.

⚠ **This is NOT satisfiable for the (Hecke-generator, S₅-generator) actions on
`std` at `q₀ ≠ 1`** — see `intertwiner_trace_eq` below. The Hecke generator
`σᵢ` (eigenvalues `q₀,−q₀⁻¹`) is not conjugate to an S₅ transposition
(eigenvalues `1,−1`), so no such `P` exists. The *actual* τ-correspondence is the
**Tits `*`-algebra iso** `H₅(q₀) ≅ ℂ[S₅]` on the `(4,1)` block (a Skolem–Noether
conjugator sending `σᵢ` to a *non-generator* element), which this generator
structure does **not** model. Kept only to state the general pullback assembly
and to carry the obstruction lemma. -/
structure GeneratorIntertwiner (ρS ρH : G → Matrix n n k) where
  /-- The intertwiner matrix. -/
  P : Matrix n n k
  /-- `P` is invertible. -/
  isUnit : IsUnit P.det
  /-- Intertwining relation between the two generator actions. -/
  intertwines : ∀ s, ρH s * P = P * ρS s

/-- **Obstruction — a generator-intertwiner forces equal generator traces.** If
`P` is a unit intertwining `ρH` and `ρS`, then `(ρH s).trace = (ρS s).trace` for
every `s`, since `ρH s = P (ρS s) P⁻¹` is a conjugate.

This **rules out** a generator-intertwiner between the Hecke and S₅ actions on
`std`: the Hecke generator `σ₁` has `trace = 3q₀ − q₀⁻¹ ≈ 2.43` (eigenvalues
`q₀,q₀,q₀,−q₀⁻¹`), while an S₅ transposition on `std` has `trace = 2`
(fixed-points − 1). `2.43 ≠ 2`, so no `GeneratorIntertwiner` exists at `q₀ ≠ 1`.
Hence sub-piece (ii) is **not** a generator-intertwiner; the correct object is the
Tits `*`-iso conjugator (open). -/
theorem intertwiner_trace_eq {ρS ρH : G → Matrix n n k}
    (τ : GeneratorIntertwiner ρS ρH) (s : G) :
    (ρH s).trace = (ρS s).trace := by
  have hP : IsUnit τ.P.det := τ.isUnit
  have hconj : ρH s = τ.P * ρS s * τ.P⁻¹ := by
    have h := τ.intertwines s
    have h2 : (ρH s * τ.P) * τ.P⁻¹ = (τ.P * ρS s) * τ.P⁻¹ := by rw [h]
    rwa [Matrix.mul_assoc, Matrix.mul_nonsing_inv _ hP, Matrix.mul_one] at h2
  rw [hconj, Matrix.trace_mul_comm, ← Matrix.mul_assoc,
    Matrix.nonsing_inv_mul _ hP, Matrix.one_mul]

/-- **General pullback assembly** (NOT a reduction of sub-piece ii — see the
caveat). Given *any* `GeneratorIntertwiner` on `std`, S₅-irreducibility of `ρS`
(discharging scalar-commutant via `MatrixSchurCommutant`), a unit Hodge form
`G_H`, and invariance of the Hodge form (`ρS`) and the Markov Gram `G_M` (`ρH`),
the pulled-back Markov Gram `Pᵀ * G_M * P` is a scalar multiple of `G_H`.

⚠ **This does NOT reduce (ii)** for the actual Hecke/S₅ actions: by
`intertwiner_trace_eq` the hypothesis `GeneratorIntertwiner ρH ρS` is
**unsatisfiable** there (`trace σ₁ ≈ 2.43 ≠ 2`). The theorem is a true statement
about an *abstract* form-preserving intertwiner; the real τ-correspondence is the
Tits `*`-iso conjugator, which is **not** a `GeneratorIntertwiner` and is not
supplied here. STRICT: no instance for the actual τ is exhibited; `1/(8π)` stays
phase-4. -/
theorem tauImage_proportional_hodge [IsAlgClosed k] [Nonempty n]
    {ρS ρH : G → Matrix n n k}
    (hirr : IsIrreducibleRep ρS)
    (hρS : ∀ s, IsUnit (ρS s).det)
    (τ : GeneratorIntertwiner ρS ρH)
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

/-- **The Hecke-side S₅ symmetry — the correct, SATISFIABLE form of sub-piece (ii).**
Where `GeneratorIntertwiner` is obstructed (`intertwiner_trace_eq`), this posits
the honest object: an S₅ action `ρS'` **on the Hecke module space** under which the
Markov Gram is invariant, together with a conjugator `T` to the geometric S₅
action `ρS` (`ρS' s * T = T * ρS s`).

**This premise is satisfiable** (unlike the generator one): `ρS'` and `ρS` are both
the `(4,1)` S₅-irrep, so they share a character — the `intertwiner_trace_eq`
obstruction does NOT apply (`trace ρS' s = trace ρS s` holds), and a conjugating
`T` exists by Schur. And the Markov Gram admits such a `ρS'` because the Tits
`*`-iso realises the S₅ symmetry on `H₅(q₀)`'s `(4,1)` block (the Markov/`*`-form
is S₅-invariant for the Tits-transported action, NOT for the Hecke generators).
The OPEN categorical claim (no instance registered) is that the archimedean functor
τ realises `T` for the ACTUAL Markov form. -/
structure HeckeSideS5Symmetry (ρS : G → Matrix n n k) (G_Markov : Matrix n n k) where
  /-- The S₅ action on the Hecke module space (the Tits-transported action). -/
  ρS' : G → Matrix n n k
  /-- Conjugator to the geometric S₅ action. -/
  T : Matrix n n k
  /-- `T` conjugates `ρS'` to `ρS` (same `(4,1)` character ⇒ trace-consistent). -/
  intertwines : ∀ s, ρS' s * T = T * ρS s
  /-- The Markov Gram is invariant under the Hecke-side S₅ action `ρS'`. -/
  markov_inv : InvariantForm ρS' G_Markov

/-- **Sub-piece (ii), correctly reduced.** Given the Hecke-side S₅ symmetry of the
Markov Gram (conjugator `T` to the geometric S₅ action `ρS`), the irreducibility
of `ρS` (⇒ scalar commutant, #4182), and a unit Hodge form, the transported Markov
Gram `Tᵀ · G_Markov · T` is a scalar multiple of the Hodge form. This is the
genuine reduction the generator-intertwiner failed to be: its premise is
SATISFIABLE (`ρS'`, `ρS` share the `(4,1)` character, no trace obstruction).
STRICT: no `HeckeSideS5Symmetry` instance for the actual τ is registered; the
existence of the Tits-transported symmetry with `T = τ` is the honest open input. -/
theorem markovGram_transports_to_hodge [IsAlgClosed k] [Nonempty n]
    {ρS : G → Matrix n n k} (hirr : IsIrreducibleRep ρS)
    (hρS : ∀ s, IsUnit (ρS s).det)
    {G_Markov : Matrix n n k} (sym : HeckeSideS5Symmetry ρS G_Markov)
    {G_Hodge : Matrix n n k} (hHodge : IsUnit G_Hodge.det)
    (hHodge_inv : InvariantForm ρS G_Hodge) :
    ∃ c : k, (sym.T)ᵀ * G_Markov * sym.T = c • G_Hodge := by
  -- transport the Markov Gram along `T`: it becomes a `ρS`-invariant form
  have hpull : InvariantForm ρS ((sym.T)ᵀ * G_Markov * sym.T) :=
    invariantForm_pullback sym.intertwines sym.markov_inv
  have schur : ∀ A : Matrix n n k,
      (∀ s, A * (ρS s) = (ρS s) * A) → ∃ c : k, A = c • (1 : Matrix n n k) :=
    fun A hA => commutant_scalar_of_irreducible hirr hA
  exact invariantForm_proportional_of_commutantScalar hρS schur hHodge hHodge_inv hpull

end QOU.Archimedean.TauS5EquivarianceReduction
