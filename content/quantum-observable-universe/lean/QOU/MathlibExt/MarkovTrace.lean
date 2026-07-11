import QOU.Archimedean.HeckeRep
import Mathlib.LinearAlgebra.Matrix.Trace

/-!
# Markov Trace on Hecke-Algebra Representations

The **Markov trace** on `H_n(q)` is the linear functional that turns a
braid word into its Jones–Markov invariant.  On a fixed finite-dimensional
matrix representation `ρ : HeckeRep n d` (over the ground ring
`R_t = ℤ[t, t⁻¹]`, see `QOU.Archimedean.HeckeRep`) the *representation
character*

  `tr_ρ(w) = (ρ.eval w).trace`   (= `HeckeRep.character ρ w`)

is the un-normalised, single-irrep shadow of the Markov trace.  This file
proves the two structural properties every Markov-type trace inherits from
the ordinary matrix trace, on the concrete `HeckeRep` framework:

1. **Trace property** `tr(AB) = tr(BA)` — lifted to braid words as
   `tr_ρ(v ++ w) = tr_ρ(w ++ v)` (`character_append_comm`), i.e. the
   character is a *class function* / cyclic-word invariant.
2. **Conjugation invariance for the standard generators**
   `tr_ρ(σ_i · A · σ_i⁻¹) = tr_ρ(A)` and the `σ_i⁻¹`-conjugate
   (`character_conj_gen` / `character_conj_genInv`).

The enabling lemma is `HeckeRep.eval_append`: braid-word evaluation is a
monoid homomorphism from list concatenation to matrix multiplication.  It
was previously missing from `HeckeRep.lean` and is the structural bridge
that lets the ordinary-matrix `trace_mul_comm` speak about braid words.

## Scope / honesty note

`HeckeRep.character` is the trace **on one representation**; the full
Jones–Markov trace is the `y_λ`-weighted sum over the Wedderburn blocks
`λ ⊢ n` (see `QOU.Mathlib.HeckeAlgebra.MarkovTrace` for the abstract
uniqueness class, and `QOU.Braiding.HnMarkovTrace.MarkovTraceTower` for the
tower axioms).  What is proved here is the *cyclic / conjugation* structure
those weighted traces inherit block-by-block — not the normalisation
`tr_M(1) = 1` nor the Markov peel axiom, which are representation-independent
and live in those files.

## References

- [jones1987] V. Jones, Hecke algebra representations of braid groups and
  link polynomials, Ann. of Math. 126 (1987) 335-388.
- [murphy1992] G. Murphy, On the representation theory of the symmetric
  groups and associated Hecke algebras.
-/

namespace QOU.MathlibExt.MarkovTrace

open QOU.Archimedean Matrix

/-! ## §1  Conjugation invariance of the matrix trace (QOU-free)

A one-line consequence of cyclicity that Mathlib does not package under a
convenient name.  It is the algebraic core of the Markov trace's
class-function property. -/

/-- **Trace of a two-sided conjugate.**  If `N · M = 1` then
    `tr(M · A · N) = tr(A)` for any square matrix `A`.

    With `N = M⁻¹` this is the usual similarity-invariance
    `tr(M A M⁻¹) = tr(A)`; stated with a bare left-inverse hypothesis so it
    applies to the Hecke generator/inverse pair, which are two-sided inverses
    of each other but only a *one*-sided hypothesis is needed here.

    TODO upstream: `Mathlib.LinearAlgebra.Matrix.Trace` — companion to
    `Matrix.trace_mul_comm` / `Matrix.trace_mul_cycle`. -/
theorem trace_conj_of_mul_eq_one {R : Type*} [CommRing R] {m : Type*}
    [Fintype m] [DecidableEq m] {M N A : Matrix m m R} (h : N * M = 1) :
    (M * A * N).trace = A.trace := by
  rw [Matrix.trace_mul_comm, ← Matrix.mul_assoc, h, Matrix.one_mul]

/-! ## §2  Braid-word evaluation is a homomorphism -/

variable {n d : ℕ}

/-- **Evaluation is a monoid homomorphism.**  Evaluating the concatenation
    of two braid words is the product of their evaluations:
    `ρ.eval (v ++ w) = ρ.eval v * ρ.eval w`.

    This is the structural fact that makes `HeckeRep.character` behave like a
    trace on the braid monoid.  Proved by induction on the first word. -/
theorem HeckeRep.eval_append (ρ : HeckeRep n d) (v w : BraidWord n) :
    ρ.eval (v ++ w) = ρ.eval v * ρ.eval w := by
  induction v with
  | nil => simp [HeckeRep.eval]
  | cons hd tl ih =>
    obtain ⟨i, b⟩ := hd
    cases b <;>
      simp only [List.cons_append, HeckeRep.eval, ih, Matrix.mul_assoc]

/-! ## §3  The Markov trace and its trace property -/

/-- The **Markov trace of a braid word** on a representation `ρ`: the matrix
    trace of the evaluated word.  Definitionally equal to
    `HeckeRep.character ρ w`; named here to make the trace-functional role
    explicit.  Maps `H_n(q) → R_t` (through the chosen representation). -/
noncomputable def markovTrace (ρ : HeckeRep n d) (w : BraidWord n) : R_t :=
  ρ.character w

@[simp] theorem markovTrace_eq_character (ρ : HeckeRep n d) (w : BraidWord n) :
    markovTrace ρ w = ρ.character w := rfl

/-- **Trace property `tr(AB) = tr(BA)`** at the matrix level, on the
    representation ground ring.  Restatement of `Matrix.trace_mul_comm`. -/
theorem trace_mul_comm (A B : Matrix (Fin d) (Fin d) R_t) :
    (A * B).trace = (B * A).trace := Matrix.trace_mul_comm A B

/-- **Cyclic invariance of the Markov trace** (the `tr(ab) = tr(ba)` property
    at the level of braid words): the character is unchanged under cyclic
    rotation of the word,
    `tr_ρ(v ++ w) = tr_ρ(w ++ v)`.

    This is the *class-function* property — the character depends only on the
    conjugacy class of the braid, not the specific word. -/
theorem character_append_comm (ρ : HeckeRep n d) (v w : BraidWord n) :
    ρ.character (v ++ w) = ρ.character (w ++ v) := by
  unfold HeckeRep.character
  rw [HeckeRep.eval_append, HeckeRep.eval_append, Matrix.trace_mul_comm]

/-- `markovTrace` form of `character_append_comm`. -/
theorem markovTrace_append_comm (ρ : HeckeRep n d) (v w : BraidWord n) :
    markovTrace ρ (v ++ w) = markovTrace ρ (w ++ v) :=
  character_append_comm ρ v w

/-! ## §4  Conjugation invariance for the standard generators

The Markov trace is invariant under conjugation by any braid generator: the
Jones–Markov trace is a *trace* on `H_n(q)`, so `tr(σ_i x σ_i⁻¹) = tr(x)`.
On a representation this reduces, via `eval_append`, to matrix similarity
invariance (`trace_conj_of_mul_eq_one`) using the generator/inverse
relations `σ_i · σ_i⁻¹ = 1 = σ_i⁻¹ · σ_i` (`HeckeRep.gen_mul_genInv` /
`HeckeRep.genInv_mul_gen`). -/

/-- **Conjugation by a generator `σ_i` preserves the trace** at the matrix
    level: `tr(σ_i · A · σ_i⁻¹) = tr(A)`. -/
theorem trace_conj_gen (ρ : HeckeRep n d) (i : Fin (n - 1))
    (A : Matrix (Fin d) (Fin d) R_t) :
    (ρ.gen i * A * ρ.genInv i).trace = A.trace :=
  trace_conj_of_mul_eq_one (ρ.genInv_mul_gen i)

/-- **Conjugation by a generator inverse `σ_i⁻¹` preserves the trace**:
    `tr(σ_i⁻¹ · A · σ_i) = tr(A)`. -/
theorem trace_conj_genInv (ρ : HeckeRep n d) (i : Fin (n - 1))
    (A : Matrix (Fin d) (Fin d) R_t) :
    (ρ.genInv i * A * ρ.gen i).trace = A.trace :=
  trace_conj_of_mul_eq_one (ρ.gen_mul_genInv i)

/-- **Generator-conjugation invariance of the Markov trace on braid words.**
    Prepending `σ_i` and appending `σ_i⁻¹` to a word `w` leaves the
    representation character unchanged:
    `tr_ρ((i,+) :: (w ++ [(i,−)])) = tr_ρ(w)`.

    This is the word-level statement of `trace_conj_gen`, obtained by
    evaluating the singleton generators via `eval_append`. -/
theorem character_conj_word (ρ : HeckeRep n d) (i : Fin (n - 1))
    (w : BraidWord n) :
    ρ.character ((i, true) :: (w ++ [(i, false)])) = ρ.character w := by
  unfold HeckeRep.character
  -- Definitional: `List.append` recurses on its first argument, so both
  -- sides normalise to `(i, true) :: (w ++ [(i, false)])`.
  have hsplit : (i, true) :: (w ++ [(i, false)])
      = ([(i, true)] ++ w) ++ [(i, false)] := rfl
  rw [hsplit, HeckeRep.eval_append, HeckeRep.eval_append]
  -- `eval [(i,true)] = σ_i`, `eval [(i,false)] = σ_i⁻¹`
  simp only [HeckeRep.eval, Matrix.mul_one]
  exact trace_conj_gen ρ i (ρ.eval w)

end QOU.MathlibExt.MarkovTrace
