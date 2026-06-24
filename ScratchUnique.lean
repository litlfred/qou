import Mathlib.Tactic
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Algebra.Group.Finsupp

abbrev R_t := LaurentPolynomial ℤ

noncomputable def test_expr : R_t :=
  LaurentPolynomial.T (-2) - LaurentPolynomial.T 2 - (LaurentPolynomial.T 2 - LaurentPolynomial.T 6) + (-LaurentPolynomial.T (-6)) +
  (LaurentPolynomial.T (-2) - LaurentPolynomial.T (-6)) + LaurentPolynomial.T (-10)

theorem test_eval (h : test_expr = 0) : False := by
  unfold test_expr at h
  change ((Finsupp.single (-2) 1 : ℤ →₀ ℤ) - (Finsupp.single 2 1 : ℤ →₀ ℤ) - ((Finsupp.single 2 1 : ℤ →₀ ℤ) - (Finsupp.single 6 1 : ℤ →₀ ℤ)) + (- (Finsupp.single (-6) 1 : ℤ →₀ ℤ)) +
          ((Finsupp.single (-2) 1 : ℤ →₀ ℤ) - (Finsupp.single (-6) 1 : ℤ →₀ ℤ)) + (Finsupp.single (-10) 1 : ℤ →₀ ℤ) = (0 : ℤ →₀ ℤ)) at h
  have h_eval := congrArg (fun f : ℤ →₀ ℤ => f 6) h
  simp at h_eval
