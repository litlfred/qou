/-
# The jet-filtration extensivity hypothesis is not satisfiable by `w`

`jet-filtration-binding-extensive` proves that the body-order binding

    B(A) = Σ_{n=2}^{A} m_e * a_D n * w n

is monotone non-decreasing in the cutoff `A`, **given** `m_e ≥ 0`, `a_D n ≥ 0`
and `w n ≥ 0` for every body order `n`. That proof is correct and is not in
question here. What this file records is where the hypothesis can and cannot
fail, because that decides whether the proposition applies to the physical case.

`bk-coordination-multiplicity` defines

    w n K = M n A * Vol n K

— a coordination **multiplicity** times a **hyperbolic volume**. Both are
non-negative by their nature (a count; a volume, zero on non-hyperbolic
components). So `w n ≥ 0` is **structural**: it cannot be the failing half.

Hence the hypothesis reduces to `a_D n ≥ 0`, and any measured sign alternation
in the body-order terms must be carried by `a_D` alone.

Measured, exactly and convention-invariantly (all 27 mirror conventions, from
the vendored AME2020 table), the binomial-basis body-order coefficients
`B(A) = Σ_k μ k * C(A,k)` alternate:

    μ₂ +2.22457   μ₃ +1.42622   μ₄ +9.24338
    μ₅ −55.77912  μ₆ +166.12507 μ₇ −373.24295

**The identification of `μ n` with `a_D n * w n` is NOT established here** — it is
the natural reading of "the n-body term", and it is the one thing that would
have to be checked to turn this into a refutation. Everything below is stated
conditionally on it, in the `_of_` style the repo reserves for exactly that.

No `sorry`.
-/
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Linarith

namespace QOU.Mass.JetFiltrationSignObstruction

variable {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]

/-- `w n = M n * Vol n`: a coordination multiplicity times a hyperbolic volume. -/
def wOf (M Vol : ℕ → R) (n : ℕ) : R := M n * Vol n

/-- **`w` is non-negative structurally**, from the non-negativity of a count and
of a volume. This is the half of the hypothesis that cannot fail. -/
theorem wOf_nonneg {M Vol : ℕ → R} (hM : ∀ n, 0 ≤ M n) (hV : ∀ n, 0 ≤ Vol n)
    (n : ℕ) : 0 ≤ wOf M Vol n :=
  mul_nonneg (hM n) (hV n)

/-- The body-order term. -/
def term (aD w : ℕ → R) (n : ℕ) : R := aD n * w n

/-- **A negative body-order term forces a negative `a_D`.** Since `w n ≥ 0` is
structural, an alternation observed in the product is carried by `a_D` alone:
the jet-filtration hypothesis fails in its `a_D` half, never its `w` half. -/
theorem aD_neg_of_term_neg {aD w : ℕ → R} {n : ℕ}
    (hw : 0 ≤ w n) (hterm : term aD w n < 0) : aD n < 0 := by
  by_contra h
  push_neg at h
  exact absurd (mul_nonneg h hw) (not_le.mpr hterm)

/-- **The hypothesis is not merely unverified but false, given one negative
term.** Stated in the `_of_` conditional style: IF some body-order term is
negative and `w` is structurally non-negative, THEN `∀ n, 0 ≤ aD n` fails. -/
theorem not_forall_aD_nonneg_of_term_neg {aD w : ℕ → R} {n : ℕ}
    (hw : 0 ≤ w n) (hterm : term aD w n < 0) : ¬ (∀ k, 0 ≤ aD k) := by
  intro hall
  exact absurd (hall n) (not_le.mpr (aD_neg_of_term_neg hw hterm))

/-- The extensivity conclusion itself needs every term non-negative; one
negative term breaks monotonicity of the partial sums at that order. -/
theorem partialSum_not_monotone_of_term_neg {aD w : ℕ → R} {n : ℕ}
    (hterm : term aD w n < 0) (S : R) :
    S + term aD w n < S := by
  linarith

/-- **Zero-baseline specialization of `partialSum_not_monotone_of_term_neg` (`qou-1w90`).**
When `term aD w n < 0`, `(0 : R) + term aD w n < 0`. -/
theorem partialSum_zero_lt_zero_of_term_neg {aD w : ℕ → R} {n : ℕ}
    (hterm : term aD w n < 0) :
    (0 : R) + term aD w n < 0 :=
  partialSum_not_monotone_of_term_neg hterm 0

end QOU.Mass.JetFiltrationSignObstruction
