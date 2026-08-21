/-
  **Restriction of a multivariate polynomial to a line**, and the chain rule that makes it
  useful.

  Bean `qou-sq3h`.  ⚠ Mathlib-style, Mathlib imports only, no QOU dependency: liftable
  verbatim.

  ═══ WHY THIS EXISTS ═══

  `QOU.Mathlib.MvGenWronskian` proves that an independent family has a non-zero generalized
  Wronskian, but produces one with **unbounded operator order**, and the two computations
  `mvGenWronskian_pow_five_six` / `..._constantCoeff` there show the proof technique cannot
  do better: it concludes "non-zero" from "non-zero at the origin", and bounded-order
  Wronskians can vanish at the origin.

  Roth's lemma needs the bounded-order version.  The classical route to it does not go
  through coefficients at all — it restricts to a **generic line** `t ↦ a + t·c`, where the
  *univariate* criterion (`QOU.Mathlib.GenWronskian`, `genWronskian_eq_zero_iff`) applies and
  already carries the order bound, since its operators are `dⁱ/dtⁱ`.

  This file supplies the restriction and the bridge that transports derivatives across it.

  ═══ THE BRIDGE ═══

  `derivative_lineRestrict` says `d/dt (f(a + tc)) = (Dᶜf)(a + tc)` where
  `Dᶜ = ∑ᵢ cᵢ ∂ᵢ`.  The point is the **order**: `Dᶜ` has order exactly one, so `dⁱ/dtⁱ`
  pulls back to `(Dᶜ)ⁱ` of order exactly `i` — the bound comes for free from the univariate
  side rather than having to be engineered.

  ⚠ `Dᶜ` is a *linear combination* of monomial operators, not a monomial operator, so a
  multilinear expansion is still needed before the result lands in the
  `D : Fin m → List σ` shape `mvGenWronskian` takes.  That expansion, and the genericity
  argument (`MvPolynomial.funext` gives it over an infinite integral domain), are what remain.

  `Fintype σ` is required only so that `Dᶜ` is a finite sum; Roth's setting has finitely
  many variables.
-/
import Mathlib.Algebra.MvPolynomial.PDeriv
import Mathlib.Algebra.MvPolynomial.CommRing
import Mathlib.Algebra.Polynomial.Derivative

namespace MvPolynomial

/-- Restriction of a multivariate polynomial to the line `t ↦ a + t·c`. -/
noncomputable def lineRestrict {σ K : Type*} [CommRing K] (a c : σ → K) :
    MvPolynomial σ K →ₐ[K] Polynomial K :=
  aeval (fun i => Polynomial.C (a i) + Polynomial.C (c i) * Polynomial.X)

variable {σ K : Type*} [CommRing K]

@[simp] theorem lineRestrict_X (a c : σ → K) (j : σ) :
    lineRestrict a c (X j) = Polynomial.C (a j) + Polynomial.C (c j) * Polynomial.X := by
  simp [lineRestrict]

@[simp] theorem lineRestrict_C (a c : σ → K) (r : K) :
    lineRestrict a c (C r) = Polynomial.C r := by
  simp [lineRestrict]

/-- The **directional derivative** `Dᶜ = ∑ᵢ cᵢ ∂ᵢ` — an operator of order one, which is the
whole reason it is worth naming. -/
noncomputable def dirDeriv [Fintype σ] (c : σ → K) (f : MvPolynomial σ K) : MvPolynomial σ K :=
  ∑ i, C (c i) * pderiv i f

@[simp] theorem dirDeriv_C [Fintype σ] (c : σ → K) (r : K) : dirDeriv c (C r) = 0 := by
  simp [dirDeriv]

theorem dirDeriv_add [Fintype σ] (c : σ → K) (f g : MvPolynomial σ K) :
    dirDeriv c (f + g) = dirDeriv c f + dirDeriv c g := by
  simp [dirDeriv, mul_add, Finset.sum_add_distrib]

theorem dirDeriv_mul_X [Fintype σ] [DecidableEq σ] (c : σ → K) (f : MvPolynomial σ K) (j : σ) :
    dirDeriv c (f * X j) = X j * dirDeriv c f + f * C (c j) := by
  have hexp : ∀ i : σ, C (c i) * pderiv i (f * X j)
      = X j * (C (c i) * pderiv i f) + f * (C (c i) * pderiv i (X j)) := by
    intro i
    rw [Derivation.leibniz]
    simp only [smul_eq_mul]
    ring
  have hsum : ∑ i, C (c i) * pderiv i (X j : MvPolynomial σ K) = C (c j) := by
    rw [Finset.sum_eq_single j]
    · rw [pderiv_X_self, mul_one]
    · intro i _ hij
      rw [pderiv_X_of_ne (Ne.symm hij), mul_zero]
    · intro h
      exact absurd (Finset.mem_univ j) h
  simp only [dirDeriv, hexp, Finset.sum_add_distrib, ← Finset.mul_sum, hsum]

/-- **Chain rule for restriction to a line:** `d/dt (f(a + tc)) = (Dᶜf)(a + tc)`.

Mathlib has no chain rule for `aeval`, so this goes by induction on `f`; the multiplicative
step is the only one with content. -/
theorem derivative_lineRestrict [Fintype σ] [DecidableEq σ] (a c : σ → K)
    (f : MvPolynomial σ K) :
    Polynomial.derivative (lineRestrict a c f) = lineRestrict a c (dirDeriv c f) := by
  induction f using MvPolynomial.induction_on with
  | C r => simp
  | add p q hp hq => simp [dirDeriv_add, hp, hq]
  | mul_X p j hp =>
    have hdX : Polynomial.derivative
        (Polynomial.C (a j) + Polynomial.C (c j) * Polynomial.X) = Polynomial.C (c j) := by
      simp
    have hLHS : Polynomial.derivative (lineRestrict a c (p * X j))
        = lineRestrict a c (dirDeriv c p)
            * (Polynomial.C (a j) + Polynomial.C (c j) * Polynomial.X)
          + lineRestrict a c p * Polynomial.C (c j) := by
      rw [map_mul, lineRestrict_X, Polynomial.derivative_mul, hp, hdX]
    have hRHS : lineRestrict a c (dirDeriv c (p * X j))
        = (Polynomial.C (a j) + Polynomial.C (c j) * Polynomial.X)
            * lineRestrict a c (dirDeriv c p)
          + lineRestrict a c p * Polynomial.C (c j) := by
      rw [dirDeriv_mul_X, map_add, map_mul, map_mul, lineRestrict_X, lineRestrict_C]
    rw [hLHS, hRHS]
    ring

/-- **The iterated chain rule.**  `dⁱ/dtⁱ` on the restriction is `(Dᶜ)ⁱ` upstairs — and
`(Dᶜ)ⁱ` has order exactly `i`, which is the order bound the univariate Wronskian needs. -/
theorem iterate_derivative_lineRestrict [Fintype σ] [DecidableEq σ] (a c : σ → K)
    (k : ℕ) (f : MvPolynomial σ K) :
    Polynomial.derivative^[k] (lineRestrict a c f) = lineRestrict a c ((dirDeriv c)^[k] f) := by
  induction k generalizing f with
  | zero => simp
  | succ n ih =>
    rw [Function.iterate_succ_apply, Function.iterate_succ_apply, derivative_lineRestrict, ih]

/-! ### Next

With the bridge in place, `qou-sq3h` needs:

1. **Genericity** — for a suitable `(a, c)` the restrictions `t ↦ fⱼ(a + tc)` of a
   `K`-independent family stay `K`-independent. `MvPolynomial.funext` (infinite integral
   domain) supplies the input; the work is applying it to the finitely many combinations
   that must survive.
2. **The pullback** — `lineRestrict` is an `AlgHom`, so it commutes with `det`, giving
   `genWronskian (lineRestrict ∘ f) = lineRestrict (det ((Dᶜ)ⁱ fⱼ))`. With (1) and the
   univariate criterion, the right-hand side is non-zero.
3. **Multilinear expansion** — `(Dᶜ)ⁱ` is a linear combination of monomial operators of
   order `i`; expanding `det` over those exhibits a non-zero *bounded-order*
   `mvGenWronskian`.

Step 2 is the only one that needs both this file and `QOU.Mathlib.GenWronskian`, so it
belongs in a file importing both rather than here. -/

end MvPolynomial
