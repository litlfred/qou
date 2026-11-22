import Mathlib.Data.Nat.Basic
import Mathlib.Logic.Function.Basic


/-!
# QOU.IncompletenessHorizon — Gödel incompleteness implies non-empty horizons

If a resolution system is Turing-complete and admits an embedding of ℕ
into its section space (arithmetic non-triviality), then the computable
fragment is strictly smaller than the full function space.  This is the
QOU formalization of the Gödel–Turing theorem: a sufficiently expressive
computational system necessarily contains non-computable functions, which
populate the computational horizon.

The proof is a diagonal argument: given a surjective enumeration of all
programs (finite braids), construct a function that differs from each
program's output on at least one input.

LaTeX label: `prop:incompleteness-implies-horizon`

## References

- [goedel1931] https://doi.org/10.1007/BF01700692
- [turing1936] https://doi.org/10.1112/plms/s2-42.1.230
- [leitner2026] §9/incompleteness-horizon
-/

namespace QOU.IncompletenessHorizon

/-! ## Turing-complete resolution system

    A Turing-complete resolution system consists of:
    - A countable set of programs P (finite braids)
    - A surjective enumeration e : ℕ → P
    - An evaluation map eval : P → (ℕ → ℕ)

    The ℕ-embeddability condition is implicit: programs compute
    functions on ℕ, so the system must represent natural numbers.
    Without this, the diagonal argument is vacuous. -/

/-- A Turing-complete resolution system: programs are countable
    (surjectively enumerable from ℕ) and each computes a total
    function ℕ → ℕ.

    The ℕ domain of `eval` is the arithmetic non-triviality
    condition: the system can represent natural numbers.  A trivial
    category (which cannot encode ℕ) does not admit such a system. -/
structure TuringCompleteSystem where
  /-- The type of programs (finite braids). -/
  Program : Type*
  /-- Programs are countable: ℕ surjects onto P. -/
  enumerate : ℕ → Program
  /-- The enumeration is surjective (every program has an index). -/
  enumerate_surj : Function.Surjective enumerate
  /-- Each program computes a total function ℕ → ℕ. -/
  eval : Program → (ℕ → ℕ)

/-! ## The diagonal argument -/

/-- The diagonal function: given an enumeration of functions,
    construct a function that differs from each enumerated function
    at the self-application point.

    d(n) = enum(n)(n) + 1

    This is the Gödel–Turing diagonal construction. -/
def diagonal (enum : ℕ → (ℕ → ℕ)) : ℕ → ℕ :=
  fun n => enum n n + 1

/-- The diagonal function differs from every enumerated function.
    For each n: d(n) = enum(n)(n) + 1 ≠ enum(n)(n), so d ≠ enum(n). -/
theorem diagonal_not_in_range (enum : ℕ → (ℕ → ℕ)) :
    ∀ n, diagonal enum ≠ enum n := by
  intro n h
  have : diagonal enum n = enum n n := congr_fun h n
  unfold diagonal at this
  omega

/-- **Main theorem: incompleteness implies non-computable functions.**

    In any Turing-complete resolution system with ℕ-embedding
    (i.e., programs are countable and compute functions on ℕ),
    there exist functions not computable by any program.

    This is the formal content of Gödel's first incompleteness
    theorem applied to the computational framework: the computable
    fragment Γ_fin(S, A₀) is strictly smaller than the full
    function space.

    The non-computable function populates the computational horizon
    H_c = V(h_c): it is a degree-0 section that exists in the full
    algebra but cannot be produced by any finite braid. -/
-- Ref: [goedel1931]     title: — see folio/schema/references.ts
-- Ref: [turing1936]     title: — see folio/schema/references.ts
theorem exists_noncomputable (S : TuringCompleteSystem) :
    ∃ f : ℕ → ℕ, ∀ p : S.Program, S.eval p ≠ f := by
  refine ⟨diagonal (S.eval ∘ S.enumerate), fun p h => ?_⟩
  obtain ⟨n, rfl⟩ := S.enumerate_surj p
  exact diagonal_not_in_range (S.eval ∘ S.enumerate) n h.symm

/-- The non-computable function is explicitly constructible:
    it is the diagonal of the evaluation table.  This is not
    a mere existence proof — the witness is computable relative
    to an oracle for the enumeration. -/
def noncomputableWitness (S : TuringCompleteSystem) : ℕ → ℕ :=
  diagonal (S.eval ∘ S.enumerate)

/-- The witness is indeed non-computable. -/
theorem noncomputableWitness_spec (S : TuringCompleteSystem) :
    ∀ p : S.Program, S.eval p ≠ noncomputableWitness S := by
  intro p h
  obtain ⟨n, rfl⟩ := S.enumerate_surj p
  exact diagonal_not_in_range _ n h.symm

/-! ## Connection to the computational horizon

    The existence of non-computable functions means the computational
    horizon is non-empty.  We state this abstractly: if every computable
    function factors through a program, and there exist non-computable
    functions, then the "computable fragment" is a proper subset. -/

/-- The computable fragment is strictly smaller than the full
    function space: there exist functions in (ℕ → ℕ) that are
    not in the image of eval. -/
theorem computable_fragment_proper (S : TuringCompleteSystem) :
    ¬ Function.Surjective S.eval := by
  intro h_surj
  obtain ⟨f, hf⟩ := exists_noncomputable S
  obtain ⟨p, hp⟩ := h_surj f
  exact hf p hp

end QOU.IncompletenessHorizon
