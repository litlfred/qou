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

-- Ref: [manuscript] docs/audits/2026-08-08-c1-inf-degree-law-proved.md
-/
import Mathlib.Algebra.Polynomial.Degree.Lemmas
import Mathlib.Tactic.ComputeDegree

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

end QOU.QBeta
