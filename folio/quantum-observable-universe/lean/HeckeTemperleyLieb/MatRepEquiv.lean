import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Algebra.Algebra.Equiv
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse

/-!
# QOU.SchurWeyl.MatRepEquiv — equivalence of matrix representations, over any commutative ring

Extracted from `QOU/SchurWeyl/SeminormalInequivalence.lean` (bean `qou-j377`).

Nothing here mentions `ℝ`, a Hecke algebra, or a Young diagram: it is the general statement
that two matrix representations of one algebra are equivalent when an invertible change of
basis intertwines them, plus what that forces on scalars, conjugates, traces and dimensions.

It was living in the file with the largest `ℝ` surface in the Wedderburn cone, which
`scripts/check-sidecars.sh` flagged as a §7c mixed generic/archimedean file.  The flag
predates the general-field work — `MatRepEquiv` has been generic since it was written — but
it is exactly the shape §7c asks to be split, and moving it makes the remaining `ℝ` in
`SeminormalInequivalence` the only thing in that file.

`MatRepEquiv` had **no consumers outside** its original file, so this move breaks nothing;
the sixteen uses inside it now resolve through this import.
-/

namespace QOU.SchurWeyl

/-! ## Equivalence of matrix representations -/

/-- **Two matrix representations of one algebra are equivalent** when an invertible change of
basis intertwines them.

Stated with an explicit inverse pair `S`, `T` rather than `IsUnit S`, because the index types
`ι` and `κ` differ: `S : Matrix κ ι R` is not square, so `IsUnit` does not apply and the two
one-sided identities are separate data.  Both are needed — `S * T = 1` is what forces the
scalar comparison below, and `T * S = 1` is what makes this a symmetric notion. -/
def MatRepEquiv {R A ι κ : Type*} [CommRing R] [Semiring A] [Algebra R A]
    [Fintype ι] [DecidableEq ι] [Fintype κ] [DecidableEq κ]
    (ρ : A →ₐ[R] Matrix ι ι R) (ρ' : A →ₐ[R] Matrix κ κ R) : Prop :=
  ∃ (S : Matrix κ ι R) (T : Matrix ι κ R),
    S * T = 1 ∧ T * S = 1 ∧ ∀ x : A, ρ' x * S = S * ρ x

variable {R A ι κ : Type*} [CommRing R] [Semiring A] [Algebra R A]
  [Fintype ι] [DecidableEq ι] [Fintype κ] [DecidableEq κ]

/-- **A scalar value is an equivalence invariant.**  If `x` is sent to a scalar matrix by both
representations, the two scalars agree.

This is the whole force of centrality: a central element goes to a scalar in every irreducible
block, and equivalent blocks cannot disagree about which scalar.  `Nonempty κ` is needed and is
not a formality — over the empty index type every matrix is `1`, so any two scalars would be
indistinguishable. -/
theorem MatRepEquiv.scalar_eq [Nonempty κ] {ρ : A →ₐ[R] Matrix ι ι R} {ρ' : A →ₐ[R] Matrix κ κ R}
    (h : MatRepEquiv ρ ρ') {x : A} {c c' : R}
    (hc : ρ x = c • (1 : Matrix ι ι R)) (hc' : ρ' x = c' • (1 : Matrix κ κ R)) : c' = c := by
  obtain ⟨S, T, hST, _, hint⟩ := h
  have key : c' • S = c • S := by
    have hx := hint x
    rw [hc, hc'] at hx
    rwa [Matrix.smul_mul, Matrix.one_mul, Matrix.mul_smul, Matrix.mul_one] at hx
  have h2 : c' • (1 : Matrix κ κ R) = c • (1 : Matrix κ κ R) := by
    calc c' • (1 : Matrix κ κ R) = c' • (S * T) := by rw [hST]
      _ = (c' • S) * T := (Matrix.smul_mul c' S T).symm
      _ = (c • S) * T := by rw [key]
      _ = c • (S * T) := Matrix.smul_mul c S T
      _ = c • (1 : Matrix κ κ R) := by rw [hST]
  have := congrFun (congrFun h2 (Classical.arbitrary κ)) (Classical.arbitrary κ)
  simpa [Matrix.one_apply_eq] using this

/-- **An equivalence conjugates one representation into the other.**  The intertwining identity
`ρ' x * S = S * ρ x` becomes `ρ' x = S * ρ x * T` once `S * T = 1` is used on the right. -/
theorem MatRepEquiv.conj_eq {ρ : A →ₐ[R] Matrix ι ι R} {ρ' : A →ₐ[R] Matrix κ κ R}
    {S : Matrix κ ι R} {T : Matrix ι κ R} (hST : S * T = 1)
    (hint : ∀ x : A, ρ' x * S = S * ρ x) (x : A) : ρ' x = S * ρ x * T := by
  calc ρ' x = ρ' x * (S * T) := by rw [hST, Matrix.mul_one]
    _ = (ρ' x * S) * T := (Matrix.mul_assoc _ _ _).symm
    _ = (S * ρ x) * T := by rw [hint x]

/-- **The character is an equivalence invariant.**  `tr ρ'(x) = tr ρ(x)` for every `x`.

This is the workhorse for *un*conditional separation, and it is strictly stronger than
`scalar_eq`: it applies to every algebra element, not only those landing on scalars, so it can
compare whole spectra rather than one number.  Note it needs only `S * T = 1` and `T * S = 1` —
no genericity, no algebra structure beyond the intertwining. -/
theorem MatRepEquiv.trace_eq {ρ : A →ₐ[R] Matrix ι ι R} {ρ' : A →ₐ[R] Matrix κ κ R}
    (h : MatRepEquiv ρ ρ') (x : A) : (ρ' x).trace = (ρ x).trace := by
  obtain ⟨S, T, hST, hTS, hint⟩ := h
  calc (ρ' x).trace = (S * ρ x * T).trace := by rw [MatRepEquiv.conj_eq hST hint x]
    _ = (T * (S * ρ x)).trace := Matrix.trace_mul_comm _ _
    _ = ((T * S) * ρ x).trace := by rw [Matrix.mul_assoc]
    _ = (ρ x).trace := by rw [hTS, Matrix.one_mul]

/-- **Equivalent representations have equal dimension.**  The `x = 1` instance of `trace_eq`,
read through `CharZero` to land in `ℕ`. -/
theorem MatRepEquiv.card_eq [CharZero R] {ρ : A →ₐ[R] Matrix ι ι R} {ρ' : A →ₐ[R] Matrix κ κ R}
    (h : MatRepEquiv ρ ρ') : Fintype.card κ = Fintype.card ι := by
  have := h.trace_eq 1
  rw [map_one, map_one, Matrix.trace_one, Matrix.trace_one] at this
  exact_mod_cast this

end QOU.SchurWeyl
