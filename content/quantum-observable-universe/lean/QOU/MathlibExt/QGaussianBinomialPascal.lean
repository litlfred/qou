import QOU.MathlibExt.QPartitionCombinatorics

/-!
# QOU.MathlibExt.QGaussianBinomialPascal — q-Pascal + concrete Rogers–Szegő

Companion to `QPartitionCombinatorics` (bean `5ldf`, epic `08a2`). Supplies the **q-Pascal
recurrence** for the Gaussian binomial `qBinom`, the primitive that #2807's `qBinom` shipped
without, derived from the `qBracket_add` addition identity (#2817). This unlocks the concrete
Rogers–Szegő / continuous q-Hermite polynomials and lets them instantiate the abstract
`QOU.Mass.BindingQHermiteOscillator.FollowsRogersSzego` class (#2800).

The recurrence is stated in the **`m`-parametrised** form (`n = k+1+m`) so every index is a
sum, never a `Nat` subtraction — the cleanest shape for downstream rewriting.
-/

namespace QOU.MathlibExt.QPartitionCombinatorics

/-- **q-Pascal rule** for the Gaussian binomial (`q > 1`, `m`-parametrised, `n = k+1+m`):
`[k+m+2 choose k+1]_q = q^{m+1}·[k+1+m choose k]_q + q^{-(k+1)}·[k+1+m choose k+1]_q`.
Derived from `qBracket_add` via the `qFactorial` ratio — the recurrence behind the
Rogers–Szegő / continuous q-Hermite three-term relation. -/
theorem qBinom_pascal {q : ℝ} (hq : 1 < q) (k m : ℕ) :
    qBinom q (k + m + 2) (k + 1)
      = q ^ (m + 1) * qBinom q (k + 1 + m) k
        + q ^ (-((k : ℤ) + 1)) * qBinom q (k + 1 + m) (k + 1) := by
  have hq0 : q ≠ 0 := ne_of_gt (lt_trans zero_lt_one hq)
  have hFk : qFactorial q k ≠ 0 := qFactorial_ne_zero hq k
  have hFm : qFactorial q m ≠ 0 := qFactorial_ne_zero hq m
  have hBk : qBracket q (k + 1) ≠ 0 := qBracket_ne_zero hq (by omega)
  have hBm : qBracket q (m + 1) ≠ 0 := qBracket_ne_zero hq (by omega)
  -- Resolve the three Gaussian-binomial subtraction indices to their `m`-forms.
  have s1 : k + m + 2 - (k + 1) = m + 1 := by omega
  have s2 : k + 1 + m - k = m + 1 := by omega
  have s3 : k + 1 + m - (k + 1) = m := by omega
  -- Factorial successor relations.
  have e_km2 : qFactorial q (k + m + 2)
      = qBracket q (k + m + 2) * qFactorial q (k + m + 1) := by
    have h : k + m + 2 = (k + m + 1) + 1 := by omega
    rw [h, qFactorial_succ]
  have e_k1 : qFactorial q (k + 1) = qBracket q (k + 1) * qFactorial q k := qFactorial_succ q k
  have e_m1 : qFactorial q (m + 1) = qBracket q (m + 1) * qFactorial q m := qFactorial_succ q m
  -- The top bracket via `qBracket_add` (split `k+m+2 = (k+1)+(m+1)`).
  have e_add : qBracket q (k + m + 2)
      = q ^ (m + 1) * qBracket q (k + 1) + q ^ (-((k : ℤ) + 1)) * qBracket q (m + 1) := by
    have h := qBracket_add q hq0 (k + 1) (m + 1)
    have idx : k + 1 + (m + 1) = k + m + 2 := by omega
    rw [idx] at h
    rw [h]; push_cast; ring
  -- Unfold and reduce to a rational-function identity in the bracket/factorial atoms.
  unfold qBinom
  rw [s1, s2, s3, e_km2, e_k1, e_m1, e_add]
  field_simp
  ring_nf

end QOU.MathlibExt.QPartitionCombinatorics
