import QOU.Archimedean.RossoJonesTorusLink

/-!
# Rosso–Jones for torus links: the coprime and full-twist specialisations

`QOU.Archimedean.RossoJonesTorusLink` proves the weight-space traces of `γ^p` on `V^{⊗(n+1)}`
for every `p` (`T_gam_pow`):

    T_m(γ^p) = Σ_{j=0}^{m} rhoTr(j) − Σ_{j=0}^{m−1} rho'Tr(j),

with `rhoTr(j) = fix(j) q^{(n−j)(p−u)+(j−3)u}`, `rho'Tr(j) = fix(j) q^{(n−j−2)(p−u)+(j−1)u}`,
`u = pj/(n+1)`, and `fix(j) = fixCount n p j = C(d, j/e)` if `e ∣ j` and `0` otherwise
(`d = gcd(n+1, p)`, `e = (n+1)/d`).

This file records two specialisations of that general formula.

* **Coprime case** (`T_gam_mid_of_torusLink`, `middleWeightTraces_of_torusLink`). When
  `gcd(n+1, p) = 1`, `d = 1` and `e = n + 1`, so `fix(j) = 0` for `0 < j < n + 1`
  (`fixCount_mid_of_coprime`) and `fix(0) = 1` (`fixCount_zero`). Only `rhoTr(0) = q^{np}` and
  `rho'Tr(0) = q^{(n−2)p}` survive, which re-derives `RossoJonesMiddle.T_gam_mid`, hence
  `MiddleWeightTraces`, from the general formula rather than from the separate coprime argument.
* **Full twist** (`fixCount_full_twist`). When `p = (n + 1) k`, `d = n + 1` and `e = 1`: every
  state is fixed and `fix(j) = C(n + 1, j)`.

Over a generic field `R`, with `q ≠ 0`. Sorry-free.

-- Ref: [rosso-jones1993] Rosso–Jones, *J. Knot Theory Ramifications* 2 (1993)
-/

namespace QOU.Archimedean.RossoJonesGeneral

variable {R : Type*} [Field R] {q : R}

theorem fixCount_zero (n p : ℕ) : fixCount n p 0 = 1 := by
  simp [fixCount]

/-- For `gcd(n + 1, p) = 1` no middle-weight state is fixed by `rot^p`. -/
theorem fixCount_mid_of_coprime {n p j : ℕ} (hcop : Nat.Coprime (n + 1) p) (hj0 : 0 < j)
    (hj : j < n + 1) : fixCount n p j = 0 := by
  rw [fixCount, Nat.Coprime.gcd_eq_one hcop, Nat.div_one, if_neg]
  intro h
  exact absurd (Nat.le_of_dvd hj0 h) (by omega)

/-- **The full twist** `p = (n + 1) k`: every state is fixed, so `fix(j) = C(n + 1, j)`. -/
theorem fixCount_full_twist (n k j : ℕ) : fixCount n ((n + 1) * k) j = (n + 1).choose j := by
  rw [fixCount, Nat.gcd_mul_right_right, Nat.div_self (Nat.succ_pos n)]
  simp

/-- **The coprime case of `T_gam_pow`**: for `gcd(n + 1, p) = 1` and `0 < m < n + 1`, only the
`j = 0` terms survive, giving `T_m(γ^p) = q^{np} − (q^n q^{−2})^p`. -/
theorem T_gam_mid_of_torusLink (hq : q ≠ 0) (n p : ℕ) (hcop : Nat.Coprime (n + 1) p) :
    ∀ m, 0 < m → m < n + 1 → T (gam q n ^ p) m = q ^ (n * p) - (q ^ n * q⁻¹ ^ 2) ^ p := by
  intro m hm0 hm1
  rw [T_gam_pow hq]
  have hA : ∑ j ∈ Finset.range (m + 1), rhoTr q n p j = q ^ (n * p) := by
    rw [Finset.sum_eq_single 0]
    · simp [rhoTr, fixCount_zero, ← pow_mul, mul_comm n p]
    · intro j hj hj0
      rw [rhoTr, fixCount_mid_of_coprime hcop (Nat.pos_of_ne_zero hj0)
        (by simp at hj; omega)]
      simp
    · intro h; exact absurd (Finset.mem_range.mpr (Nat.succ_pos m)) h
  have hB : ∑ j ∈ Finset.range m, rho'Tr q n p j = (q ^ n * q⁻¹ ^ 2) ^ p := by
    rw [Finset.sum_eq_single 0]
    · simp [rho'Tr, fixCount_zero]
    · intro j hj hj0
      rw [rho'Tr, fixCount_mid_of_coprime hcop (Nat.pos_of_ne_zero hj0)
        (by simp at hj; omega)]
      simp
    · intro h; exact absurd (Finset.mem_range.mpr hm0) h
  rw [hA, hB]

/-- **`MiddleWeightTraces` for `gcd(n + 1, p) = 1`, re-derived from the torus-link formula.** -/
theorem middleWeightTraces_of_torusLink (hq : q ≠ 0) (n p : ℕ) (hcop : Nat.Coprime (n + 1) p) :
    MiddleWeightTraces q n p := by
  intro m hm0 hm1
  rw [T_gam_mid_of_torusLink hq n p hcop m hm0 hm1, mul_pow, ← pow_mul, ← pow_mul]
  have h2 : q ^ (2 * p) * q⁻¹ ^ (2 * p) = 1 := by
    rw [← mul_pow, mul_inv_cancel₀ hq, one_pow]
  calc q ^ (2 * p) * (q ^ (n * p) - q ^ (n * p) * q⁻¹ ^ (2 * p))
      = q ^ (2 * p) * q ^ (n * p) - q ^ (n * p) * (q ^ (2 * p) * q⁻¹ ^ (2 * p)) := by ring
    _ = q ^ (p * (n + 2)) - q ^ (p * n) := by
      rw [h2, mul_one, ← pow_add, mul_comm n p, show 2 * p + p * n = p * (n + 2) by ring]

end QOU.Archimedean.RossoJonesGeneral
