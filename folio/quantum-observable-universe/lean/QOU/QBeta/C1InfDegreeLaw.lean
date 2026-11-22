/-
C1 ∞-side degree law: `deg_q(cₙ) = n²`.

The C1 operator `L1 = (q²x−1)σ² − (q−1)σ − (q−1)` solved at `∞` with
`f(x) = Σ cₙ x^{−n}` gives the exact recurrence

    c_{m+1} = c_m · f_m,   f_m = 1 + (q−1)qᵐ + (q−1)q^{2m},   c₀ = 1,

so `cₙ = ∏_{m<n} f_m`. This file proves `natDegree cₙ = n²` for ALL `n`.

Why it matters: that degree law is the evidence for the q-Gevrey slope-½
divergence of the ∞ formal solution — i.e. that it must be q-Borel/Laplace
summed — and the whole ∞-Stokes programme is downstream of it. It was
previously recorded only as "verified symbolically for n ≤ 9"
(`docs/audits/2026-08-01-c1-inf-formal-solution-qgevrey.md`).

Note the genuine content is the *no-cancellation* step: `natDegree` is
additive over a product only because `ℤ[X]` is a domain and each factor is
nonzero, and `natDegree f_m = 2m+1` requires that the top term survives. The
arithmetic half (`Σ_{m<n}(2m+1) = n²`) is the easy part and would assert
nothing about polynomials on its own.

The `m = 0` case is genuinely degenerate: `(q−1)qᵐ` and `(q−1)q^{2m}` collide
into `2(q−1)`, giving `f₀ = 2X − 1`. Its degree is still `2·0+1 = 1`, so the
formula is uniform, but its leading coefficient is `2` rather than `1`.

Base ring is `ℤ` (per §7c: this is pure algebra over a domain — no ordering,
no `Real.sqrt`, nothing archimedean; the substrate/archimedean wall is not
crossed here).

-- Ref: [leitner2026] docs/audits/2026-08-08-c1-inf-degree-law-proved.md
-/
import Mathlib.Algebra.Polynomial.Degree.Lemmas
import Mathlib.Tactic.ComputeDegree
import QOU.Mass.C1FormalSolutionGrowth
import QOU.MathlibExt.QBorelKernelLevel

namespace QOU.QBeta

open Polynomial Finset

/-- The recurrence factor `f_m = 1 + (X−1)Xᵐ + (X−1)X^{2m}` over `ℤ[X]`. -/
noncomputable def cFactor (m : ℕ) : Polynomial ℤ :=
  1 + (X - 1) * X ^ m + (X - 1) * X ^ (2 * m)

/-- The `∞`-side coefficient `cₙ = ∏_{m<n} f_m`, with `c₀ = 1`. -/
noncomputable def cCoeff (n : ℕ) : Polynomial ℤ :=
  ∏ m ∈ range n, cFactor m

@[simp] theorem cCoeff_zero : cCoeff 0 = 1 := by
  simp [cCoeff]

/-- The recurrence, as stated in the audit: `c_{m+1} = c_m · f_m`. -/
theorem cCoeff_succ (n : ℕ) : cCoeff (n + 1) = cCoeff n * cFactor n := by
  simp [cCoeff, prod_range_succ]

/-- Expanded normal form of the factor: `f_m = X^{2m+1} − X^{2m} + X^{m+1} − Xᵐ + 1`. -/
theorem cFactor_eq (m : ℕ) :
    cFactor m = X ^ (2 * m + 1) - X ^ (2 * m) + X ^ (m + 1) - X ^ m + 1 := by
  simp only [cFactor, sub_mul, one_mul, ← pow_succ']
  ring

/-- `f₀ = 2X − 1` — the degenerate case where the two `(X−1)` terms collide. -/
theorem cFactor_zero : cFactor 0 = 2 * X - 1 := by
  simp [cFactor]
  ring

/-- The factor is never the zero polynomial. -/
theorem cFactor_ne_zero (m : ℕ) : cFactor m ≠ 0 := by
  intro h
  have h1 : (cFactor m).coeff (2 * m + 1) = 0 := by rw [h]; simp
  rw [cFactor_eq] at h1
  simp [coeff_one, coeff_X_pow] at h1
  omega

/-- Each factor has degree exactly `2m + 1`, including the degenerate `m = 0`. -/
theorem cFactor_natDegree (m : ℕ) : (cFactor m).natDegree = 2 * m + 1 := by
  rcases Nat.eq_zero_or_pos m with rfl | hm
  · rw [cFactor_zero]
    compute_degree!
  · -- `m ≥ 1`: the exponents `m, 2m, m+1, 2m+1` are distinct with `2m+1`
    -- strictly largest, so the top term cannot cancel. These two
    -- disequalities are exactly that fact, and they are what fails at
    -- `m = 0` (where `2m = m`), handled in the branch above.
    have h1 : 2 * m ≠ m := by omega
    have h2 : 2 * m + 1 ≠ m := by omega
    rw [cFactor_eq]
    compute_degree!
    all_goals first | omega | simp [h1, h2]

/-- `cₙ` is never the zero polynomial — a product of nonzero factors in the
domain `ℤ[X]`. This is what licenses additivity of `natDegree` below. -/
theorem cCoeff_ne_zero (n : ℕ) : cCoeff n ≠ 0 :=
  prod_ne_zero_iff.mpr fun m _ => cFactor_ne_zero m

/-- **The degree law.** `natDegree cₙ = n²`, for every `n`. -/
theorem cCoeff_natDegree (n : ℕ) : (cCoeff n).natDegree = n ^ 2 := by
  induction n with
  | zero => simp
  | succ k ih =>
      rw [cCoeff_succ, natDegree_mul (cCoeff_ne_zero k) (cFactor_ne_zero k),
        ih, cFactor_natDegree]
      ring

/-!
### Bridge to `QOU.Mass.C1FormalSolutionGrowth`

`QOU.Mass.C1FormalSolutionGrowth.c1FormalDeg n` is *defined* as `∑_{m<n} (2m+1)`, and
`c1FormalDeg_eq_sq` proves it equals `n²`. That is a true statement about
natural numbers, but on its own it says nothing about the coefficients `cₙ` —
the name asserts "the C1 formal-solution degree" while nothing in that module
mentions `Polynomial` or the recurrence.

The lemma below is the missing link: the *actual* `natDegree` of the *actual*
coefficient polynomial equals that combinatorial quantity. It is what earns
`c1FormalDeg` its name, and it is the step that requires the domain structure
of `ℤ[X]` plus the no-cancellation fact — neither of which is available to a
pure-`Nat` argument.
-/

/-- **Bridge.** The genuine polynomial degree of `cₙ` is the combinatorial
`c1FormalDeg n`. This is what connects `QOU.Mass.C1FormalSolutionGrowth.c1FormalDeg` to the object it
is named for. -/
theorem cCoeff_natDegree_eq_c1FormalDeg (n : ℕ) :
    (cCoeff n).natDegree = QOU.Mass.C1FormalSolutionGrowth.c1FormalDeg n := by
  rw [cCoeff_natDegree, QOU.Mass.C1FormalSolutionGrowth.c1FormalDeg_eq_sq]

/-- The per-step increment, transported to the genuine degree: appending the
factor `f_n` raises the polynomial degree by exactly `2n+1`. -/
theorem cCoeff_natDegree_step (n : ℕ) :
    (cCoeff (n + 1)).natDegree = (cCoeff n).natDegree + (2 * n + 1) := by
  rw [cCoeff_natDegree, cCoeff_natDegree]
  ring

/-!
### S1: the ramified q-Borel growth budget

Stage S1 of `docs/audits/2026-08-08-w2-stokes-qborel-attack-plan.md`. The
*unramified* level-`d` q-Borel kernel cannot absorb `deg_q(cₙ) = n²` for any `d`
(budget `+n²/2` at `d=1`, worse for larger `d`). Ramifying first — `z = ζ²`, the
pullback forced by the non-integral slope ½ — puts the coefficient `cₘ` at index
`N = 2m`, against the **level-2** kernel exponent there.

The result is exact and *linear*: the leftover exponent is exactly `m`. Linear
(sub-quadratic) leftover is precisely the convergence condition, so this pairing
— ramification **then** level 2 — is the critical matching. That is the
quantitative reason RSZ's square roots `B₁,B₂` are forced rather than cosmetic.
-/

/-- **S1 budget, exactly.** At the ramified index `N = 2m`, the C1 coefficient
exponent exceeds the level-2 q-Borel kernel exponent by exactly `m`:
`m² = m(m−1) + m`. Linear leftover ⇒ the ramified transform converges, whereas
no unramified level absorbs the quadratic growth. -/
theorem ramified_qBorel_budget (m : ℕ) :
    (cCoeff m).natDegree
      = QOU.MathlibExt.QBorelKernel.qBorelExp 2 (2 * m) + m := by
  rw [cCoeff_natDegree, QOU.MathlibExt.QBorelKernel.qBorelExp_two_even]
  cases m with
  | zero => simp
  | succ k => simp only [Nat.succ_sub_one]; ring

end QOU.QBeta
