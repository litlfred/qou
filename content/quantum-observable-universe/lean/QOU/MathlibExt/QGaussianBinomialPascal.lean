import QOU.MathlibExt.QPartitionCombinatorics
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-!
# QOU.MathlibExt.QGaussianBinomialPascal — q-Pascal + concrete Rogers–Szegő

Companion to `QPartitionCombinatorics` (bean `5ldf`, epic `08a2`). Supplies the **q-Pascal
recurrence** for the Gaussian binomial `qBinom`, the primitive that #2807's `qBinom` shipped
without, derived from the `qBracket_add` addition identity (#2817), and the **concrete
balanced Rogers–Szegő polynomial** `H_n(t;q) = Σ_k [n choose k]_q tᵏ`.

The q-Pascal rule is stated in the **`m`-parametrised** form (`n = k+1+m`) so every index is a
sum, never a `Nat` subtraction — the cleanest shape for downstream rewriting.

## Normalization caveat — balanced `H_n` does NOT instantiate `FollowsRogersSzego`

`QOU.Mass.BindingQHermiteOscillator.FollowsRogersSzego` (#2800) encodes the **standard**
three-term recurrence `H_{m+2} = (1+t)H_{m+1} − (1−q^{m+1})·t·H_m`. That holds for the
**standard** `(q;q)`-normalized Rogers–Szegő (`QOU.Machinery.QPochhammer.qBinomial`). The
`qBinom` here is the **balanced** `(qⁿ−q⁻ⁿ)/(q−q⁻¹)` binomial, whose q-Pascal carries `q^{±}`
factors; feeding it through the same derivation gives a **scaled-argument** q-difference
relation (mixing `H_n(t)` and `H_n(t/q)`), not the clean `(1−qⁿ)` 3-term. So the concrete
balanced `H_n` below is a faithful object with verified low-order values, but instantiating
the *standard* class needs the *standard* q-Pascal — a separate follow-on (bean `5ldf`).
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

open scoped BigOperators

/-- The **(balanced) Rogers–Szegő polynomial** value
`H_n(t;q) = Σ_{k=0}^n [n choose k]_q · tᵏ`, in the balanced `qBinom`. The q-oscillator /
continuous q-Hermite generating polynomial (balanced normalization — see the file's
normalization caveat). -/
noncomputable def rogersSzego (q t : ℝ) (n : ℕ) : ℝ :=
  ∑ k ∈ Finset.range (n + 1), qBinom q n k * t ^ k

/-- `H_0(t;q) = 1`. -/
theorem rogersSzego_zero (q t : ℝ) (hq : 1 < q) : rogersSzego q t 0 = 1 := by
  simp [rogersSzego, qBinom_zero_right hq]

/-- `H_1(t;q) = 1 + t` (the `n=1` binomials are both `1` in any normalization, so this is the
boundary value the even/odd-vanishing argument needs — at `t=−1`, `H_1 = 0`). -/
theorem rogersSzego_one (q t : ℝ) (hq : 1 < q) : rogersSzego q t 1 = 1 + t := by
  rw [rogersSzego, Finset.sum_range_succ, Finset.sum_range_one,
    qBinom_zero_right hq, qBinom_self hq]
  ring

/-- `H_2(t;q) = 1 + [2]_q·t + t²` with `[2]_q = q + q⁻¹` (balanced). The middle coefficient is
the balanced quantum integer — the first place balanced vs standard normalization differ
(`q+q⁻¹` here, `1+q` for the standard `(q;q)` Rogers–Szegő). -/
theorem rogersSzego_two (q t : ℝ) (hq : 1 < q) (hq0 : q ≠ 0) :
    rogersSzego q t 2 = 1 + (q + q⁻¹) * t + t ^ 2 := by
  have h2 : qBinom q 2 1 = q + q⁻¹ := by
    rw [qBinom]
    rw [show (2 : ℕ) - 1 = 1 from rfl, qFactorial_succ, qFactorial_succ,
      qBracket_two hq0 (q_sub_q_inv_ne_zero hq)]
    simp [qFactorial, qBracket_one (q_sub_q_inv_ne_zero hq)]
  rw [rogersSzego, Finset.sum_range_succ, Finset.sum_range_succ, Finset.sum_range_one,
    qBinom_zero_right hq, qBinom_self hq, h2]
  ring

end QOU.MathlibExt.QPartitionCombinatorics
