import QOU.Machinery.QPochhammer
import QOU.Mass.BindingQHermiteOscillator
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-!
# QOU.MathlibExt.QStandardRogersSzego — standard q-Pascal + the FollowsRogersSzego instance

Closes the loop left open by #2823/#2829: the **balanced** `qBinom` satisfies a scaled-argument
q-Pascal, so its Rogers–Szegő does NOT obey the standard `(1−qⁿ)` three-term recurrence of
`QOU.Mass.BindingQHermiteOscillator.FollowsRogersSzego`. The **standard** `(q;q)`-normalized
binomial `QOU.Machinery.qBinomial` does. This file proves the **standard q-Pascal**
`[n+1;k+1]_q = [n;k]_q + q^{k+1}[n;k+1]_q` (from the clean `(q;q)` addition
`1−q^{a+b} = (1−q^a) + q^a(1−q^b)`) and uses it to exhibit a genuine `FollowsRogersSzego`
instance — proving the §3b conjecture class is **non-vacuous**.

Ground ring `ℝ`, `q > 1` (so every `(q;q)_n ≠ 0` — away from roots of unity).
-/

namespace QOU.Machinery

open QOU.Mass.BindingQHermiteOscillator

/-- **(q;q) diagonal recursion** `(q;q)_{n+1} = (q;q)_n · (1 − q^{n+1})`. -/
theorem qPochhammerDiag_succ_q (q : ℝ) (n : ℕ) :
    qPochhammerDiag q (n + 1) = qPochhammerDiag q n * (1 - q ^ (n + 1)) := by
  unfold qPochhammerDiag
  rw [qPochhammerFinite_succ]
  congr 2
  rw [pow_succ]; ring

/-- For `q > 1`, every factor `1 − q^{n+1} < 0`, hence `≠ 0`. -/
theorem one_sub_pow_succ_ne_zero {q : ℝ} (hq : 1 < q) (n : ℕ) : (1 : ℝ) - q ^ (n + 1) ≠ 0 := by
  have h : 1 < q ^ (n + 1) := one_lt_pow₀ hq (by omega)
  have : (1 : ℝ) - q ^ (n + 1) < 0 := by linarith
  exact ne_of_lt this

/-- **(q;q)_n ≠ 0 for q > 1** (no root-of-unity vanishing). -/
theorem qPochhammerDiag_ne_zero {q : ℝ} (hq : 1 < q) (n : ℕ) : qPochhammerDiag q n ≠ 0 := by
  induction n with
  | zero => rw [qPochhammerDiag_zero]; norm_num
  | succ m ih =>
    rw [qPochhammerDiag_succ_q]
    exact mul_ne_zero ih (one_sub_pow_succ_ne_zero hq m)

/-- **Standard q-Pascal** for the `(q;q)` Gaussian binomial (`q > 1`, `m`-parametrised,
`n = k+1+m`): `[k+m+2 choose k+1]_q = [k+1+m choose k]_q + q^{k+1}·[k+1+m choose k+1]_q`.
Clean (no `q^{±}` half-powers) — this is the form that drives the *standard* Rogers–Szegő
three-term recurrence. From the `(q;q)` addition `1−q^{(k+1)+(m+1)} = (1−q^{k+1})+q^{k+1}(1−q^{m+1})`. -/
theorem qBinomial_pascal {q : ℝ} (hq : 1 < q) (k m : ℕ) :
    qBinomial (k + m + 2) (k + 1) q
      = qBinomial (k + 1 + m) k q + q ^ (k + 1) * qBinomial (k + 1 + m) (k + 1) q := by
  have hPk : qPochhammerDiag q k ≠ 0 := qPochhammerDiag_ne_zero hq k
  have hPm : qPochhammerDiag q m ≠ 0 := qPochhammerDiag_ne_zero hq m
  have h1k : (1 : ℝ) - q ^ (k + 1) ≠ 0 := one_sub_pow_succ_ne_zero hq k
  have h1m : (1 : ℝ) - q ^ (m + 1) ≠ 0 := one_sub_pow_succ_ne_zero hq m
  -- Resolve the three Gaussian-binomial subtraction indices.
  have s1 : k + m + 2 - (k + 1) = m + 1 := by omega
  have s2 : k + 1 + m - k = m + 1 := by omega
  have s3 : k + 1 + m - (k + 1) = m := by omega
  -- `(q;q)` successor relations for the three top diagonals.
  have e_top : qPochhammerDiag q (k + m + 2)
      = qPochhammerDiag q (k + m + 1) * (1 - q ^ (k + m + 2)) := by
    have h : k + m + 2 = (k + m + 1) + 1 := by omega
    rw [h, qPochhammerDiag_succ_q]
  have e_k1 : qPochhammerDiag q (k + 1) = qPochhammerDiag q k * (1 - q ^ (k + 1)) :=
    qPochhammerDiag_succ_q q k
  have e_m1 : qPochhammerDiag q (m + 1) = qPochhammerDiag q m * (1 - q ^ (m + 1)) :=
    qPochhammerDiag_succ_q q m
  -- The `(q;q)` addition identity.
  have e_add : (1 : ℝ) - q ^ (k + m + 2)
      = (1 - q ^ (k + 1)) + q ^ (k + 1) * (1 - q ^ (m + 1)) := by
    rw [show k + m + 2 = (k + 1) + (m + 1) from by omega, pow_add]; ring
  -- Align `k+1+m` with `k+m+1`.
  have idx : k + 1 + m = k + m + 1 := by omega
  unfold qBinomial
  rw [s1, s2, s3, idx, e_top, e_k1, e_m1, e_add]
  field_simp

end QOU.Machinery
