import QOU.FluidDynamics.q_ns_triad_raising_coupling

/-!
# QOU.FluidDynamics.q_ns_qlegendre_norm — the Haar norm of the little q-Legendre polynomials

Bean `qou-9obv` (GAP from `q_ns_triad_raising_coupling`). On the Cartan block `K[ζ]` of
`O_q(SU(2))`, `ζ = βγ`, the eigenpolynomials `p_n` of the q-Casimir are Haar-orthogonal
(`OqSU2LittleQJacobiBasis`). This file computes their norms in closed form.

## Result (over a field `K`, `q : Kˣ`, `P = q²` not a root of unity)

* `H_eq_prod`: for the monic polynomial `P_n = c_n⁻¹ p_n`,
  `h(P_n²) = Π_{k<n} P² z_k² (P z_k − 1)⁴ / ((P z_k² − 1)(P² z_k² − 1)²(P³ z_k² − 1))`,
  with `z_k = P^k`.
* `haarState_jacobiPoly_sq_eq`: `h(p_n²) = c_n² · (the same product)`.

With `p = q⁻²` the `k`-th factor is `p^{2n}(1 − p^n)⁴ / ((1 − p^{2n−1})(1 − p^{2n})²(1 − p^{2n+1}))`
at `n = k + 1`, so the product is the q-Pochhammer form
`q^{−2n} p^{n²} (p;p)_n⁴ (1 − p) / ((p;p)_{2n} (p;p)_{2n+1})` checked in exact arithmetic by
`computations/qns_little_qlegendre_norm_probe.py`. That last rearrangement is bookkeeping and is
not restated in Lean.

## Method (all algebraic)

1. `coeff_Lp`: the q-Casimir is lower bidiagonal on `K[X]`, so the eigen-equation gives the
   coefficient recursion `(lam n − lam j) a_j = subd j · a_{j+1}` (`mp_coeff_rel`).
2. `D_eq`, `E_eq`: the two coefficients below the top of `P_{m+1}` and `P_{m+2}`, in closed form.
3. `H_succ`: the three-term recurrence. `ζ P_{k+1} − P_{k+2} − b P_{k+1}` has degree `≤ k`, and
   Haar orthogonality gives `h(P_{k+1}²) = A_k · h(P_k²)`, with `A_k` read off those coefficients.
4. `alg_step`, `alg_zero`: `A_k` equals the closed factor (a rational-function identity).

No empirical value enters any proof. Sorry-free.

## Not established

* Positivity of the norms over an ordered field.
* The normalised raising coupling `C̃(r)²` of `q_ns_triad_raising_coupling` as a Lean
  statement. It now follows from `coupling_raise` and this file by substitution, and its decay
  `q^{−2r}` at fixed `q > 1` (non-uniform in `q`) is no longer conditional on an unproved norm.
  The substitution itself has not been written out in Lean.
* Part A of `conj:regularity-breakdown`.
-/

namespace QOU.FluidDynamics.QLegendreNorm

open Polynomial Finset
open QOU.AlgebraicSubstrate QOU.AlgebraicSubstrate.OqSU2
open QOU.FluidDynamics.TriadRaising

variable {K : Type*} [Field K] (q : Kˣ)

local notation "qi" => (((q⁻¹ : Kˣ) : K))

/-! ## Coefficients of `L` -/

theorem coeff_Lp (P : K[X]) (j : ℕ) :
    (Lp q P).coeff j = subd q j * P.coeff (j + 1) + lam q j * P.coeff j := by
  induction P using Polynomial.induction_on' with
  | add P Q hP hQ => rw [map_add, coeff_add, hP, hQ, coeff_add, coeff_add]; ring
  | monomial n c =>
    rw [Lp_monomial, coeff_smul, smul_eq_mul]
    rcases n with _ | k
    · rcases j with _ | j <;> simp [lapX, lam_zero]
    · simp only [lapX, coeff_add, coeff_C_mul, coeff_X_pow, coeff_monomial]
      by_cases h1 : j = k
      · subst h1; simp [mul_comm]
      · by_cases h2 : j = k + 1
        · subst h2; simp [mul_comm]
        · have h5 : k ≠ j := fun h => h1 h.symm
          have h4 : k + 1 ≠ j := by omega
          simp [h1, h2, h4, h5]

/-! ## Monic little q-Legendre polynomials -/

/-- The monic polynomial `P_n = c_n⁻¹ p_n`. -/
noncomputable def mp (n : ℕ) : K[X] := ((jacobiPoly q n).coeff n)⁻¹ • jacobiPoly q n

/-- The Haar norm of the monic polynomial. -/
noncomputable def H (n : ℕ) : K := haarState q (ev q (mp q n) * ev q (mp q n))

theorem mp_mem (n : ℕ) : mp q n ∈ degreeLT K (n + 1) :=
  Submodule.smul_mem _ _ (jacobiPoly_mem q n)

theorem Lp_mp (n : ℕ) : Lp q (mp q n) = lam q n • mp q n := by
  rw [mp, map_smul, Lp_jacobiPoly, smul_comm]

theorem coeff_eq_zero_of_mem {P : K[X]} {n m : ℕ} (hP : P ∈ degreeLT K n) (h : n ≤ m) :
    P.coeff m = 0 :=
  (degree_lt_iff_coeff_zero _ _).mp (mem_degreeLT.mp hP) m (by exact_mod_cast h)

theorem mem_of_le {P : K[X]} {n m : ℕ} (hP : P ∈ degreeLT K n) (h : n ≤ m) :
    P ∈ degreeLT K m :=
  mem_degreeLT.mpr ((mem_degreeLT.mp hP).trans_le (by exact_mod_cast h))

/-- The eigen-equation, coefficient by coefficient. -/
theorem mp_coeff_rel (n j : ℕ) :
    (lam q n - lam q j) * (mp q n).coeff j = subd q j * (mp q n).coeff (j + 1) := by
  have h := congrArg (fun P => P.coeff j) (Lp_mp q n)
  simp only [coeff_Lp, coeff_smul, smul_eq_mul] at h
  linear_combination -h

variable (hp : ∀ m : ℕ, ((q : K) * q) ^ (m + 1) ≠ 1)
include hp

theorem mp_coeff_self (n : ℕ) : (mp q n).coeff n = 1 := by
  rw [mp, coeff_smul, smul_eq_mul, inv_mul_cancel₀ (coeff_jacobiPoly_ne_zero q hp n)]

/-- `h(P_n · Q) = 0` for `deg Q < n`. -/
theorem haar_mp_mul_eq_zero {n : ℕ} {Q : K[X]} (hQ : Q ∈ degreeLT K n) :
    haarState q (ev q (mp q n) * ev q Q) = 0 := by
  rw [mp, map_smul, smul_mul_assoc, map_smul,
    haarState_jacobiPoly_mul_eq_zero_of_mem q hp le_rfl hQ, smul_zero]

/-- `h(P_n · Q) = Q_n · H_n` for `deg Q ≤ n`. -/
theorem haar_mp_mul_top {n : ℕ} {Q : K[X]} (hQ : Q ∈ degreeLT K (n + 1)) :
    haarState q (ev q (mp q n) * ev q Q) = Q.coeff n * H q n := by
  have hc := coeff_jacobiPoly_ne_zero q hp n
  have hR : Q - Q.coeff n • mp q n ∈ degreeLT K n := by
    rw [mem_degreeLT, degree_lt_iff_coeff_zero]
    intro m hm
    have hm' : n ≤ m := by exact_mod_cast hm
    rcases Nat.lt_or_ge n m with h | h
    · rw [coeff_sub, coeff_smul, coeff_eq_zero_of_mem hQ h, coeff_eq_zero_of_mem (mp_mem q n) h,
        smul_zero, sub_zero]
    · have : m = n := by omega
      subst this
      rw [coeff_sub, coeff_smul, mp_coeff_self q hp, smul_eq_mul, mul_one, sub_self]
  have hQeq : Q = Q.coeff n • mp q n + (Q - Q.coeff n • mp q n) := by abel
  conv_lhs => rw [hQeq]
  rw [map_add, map_smul, mul_add, mul_smul_comm, map_add, map_smul,
    haar_mp_mul_eq_zero q hp hR, add_zero, smul_eq_mul, H]

omit hp in
theorem haar_comm (A B : K[X]) :
    haarState q (ev q A * ev q B) = haarState q (ev q B * ev q A) := by
  rw [← map_mul, ← map_mul, mul_comm]

omit hp in
theorem H_zero_aux : mp q 0 = 1 := by
  simp [mp, jacobiPoly]

omit hp in
theorem H_zero : H q 0 = 1 := by
  rw [H, H_zero_aux, map_one, one_mul, haarState_one]

/-- **The three-term step.** `H_{k+1} = A_k · H_k`, with `A_k` read off the top coefficients. -/
theorem H_succ (k : ℕ) :
    H q (k + 1) = ((X * mp q (k + 1)).coeff k - (mp q (k + 2)).coeff k -
      ((mp q (k + 1)).coeff k - (mp q (k + 2)).coeff (k + 1)) * (mp q (k + 1)).coeff k) *
        H q k := by
  set b := (mp q (k + 1)).coeff k - (mp q (k + 2)).coeff (k + 1)
  set Q := X * mp q (k + 1) - mp q (k + 2) - b • mp q (k + 1)
  have hX : ∀ {n : ℕ} {P : K[X]}, P ∈ degreeLT K n → X * P ∈ degreeLT K (n + 1) := by
    intro n P hP
    rw [mem_degreeLT, degree_lt_iff_coeff_zero]
    intro m hm
    have hm' : n + 1 ≤ m := by exact_mod_cast hm
    obtain ⟨t, rfl⟩ : ∃ t, m = t + 1 := ⟨m - 1, by omega⟩
    rw [coeff_X_mul]; exact coeff_eq_zero_of_mem hP (by omega)
  have hQ : Q ∈ degreeLT K (k + 1) := by
    rw [mem_degreeLT, degree_lt_iff_coeff_zero]
    intro m hm
    have hm' : k + 1 ≤ m := by exact_mod_cast hm
    simp only [Q, coeff_sub, coeff_smul, smul_eq_mul]
    rcases Nat.lt_or_ge (k + 2) m with h | h
    · obtain ⟨t, rfl⟩ : ∃ t, m = t + 1 := ⟨m - 1, by omega⟩
      rw [coeff_X_mul, coeff_eq_zero_of_mem (mp_mem q _) (by omega : k + 1 + 1 ≤ t),
        coeff_eq_zero_of_mem (mp_mem q _) (by omega : k + 2 + 1 ≤ t + 1),
        coeff_eq_zero_of_mem (mp_mem q _) (by omega : k + 1 + 1 ≤ t + 1)]
      ring
    · rcases (show m = k + 1 ∨ m = k + 2 by omega) with rfl | rfl
      · rw [coeff_X_mul, mp_coeff_self q hp]; simp only [b]; ring
      · rw [show k + 2 = (k + 1) + 1 by rfl, coeff_X_mul, mp_coeff_self q hp, mp_coeff_self q hp,
          coeff_eq_zero_of_mem (mp_mem q _) (le_refl (k + 1 + 1))]
        ring
  have hXk : X * mp q k ∈ degreeLT K (k + 1 + 1) := hX (mp_mem q k)
  have hXcoeff : (X * mp q k).coeff (k + 1) = 1 := by rw [coeff_X_mul, mp_coeff_self q hp]
  have e1 := haar_mp_mul_top q hp hXk
  rw [hXcoeff, one_mul] at e1
  rw [← e1, ← map_mul,
    show mp q (k + 1) * (X * mp q k) = mp q k * (Q + mp q (k + 2) + b • mp q (k + 1)) by
      simp only [Q]; ring,
    map_mul, map_add, map_add, map_smul, mul_add, mul_add, mul_smul_comm, map_add, map_add,
    map_smul, haar_mp_mul_top q hp hQ,
    haar_comm q (mp q k) (mp q (k + 2)),
    haar_mp_mul_eq_zero q hp (mem_of_le (mp_mem q k) (by omega : k + 1 ≤ k + 2)),
    haar_comm q (mp q k) (mp q (k + 1)),
    haar_mp_mul_eq_zero q hp (mp_mem q k)]
  simp only [Q, b, coeff_sub, coeff_smul, smul_eq_mul]
  ring

/-! ## The top coefficients in closed form -/

omit hp in
theorem jk_inv_mul (k : ℕ) :
    jk (qi * qi) k * ((q : K) * q) ^ k * ((q : K) * q - 1) =
      (q : K) * q * (((q : K) * q) ^ k - 1) := by
  have hA := jk_mul_sub_one (qi * qi) k
  have hqi : qi * (q : K) = 1 := by simp
  have hr : (qi * qi) ^ k * ((q : K) * q) ^ k = 1 := by
    rw [← mul_pow]; rw [show qi * qi * ((q : K) * q) = (qi * q) * (qi * q) by ring, hqi]; simp
  have hrp : (qi * qi) * ((q : K) * q) = 1 := by
    rw [show qi * qi * ((q : K) * q) = (qi * q) * (qi * q) by ring, hqi, one_mul]
  linear_combination (-(((q : K) * q) ^ (k + 1))) * hA +
    (jk (qi * qi) k * ((q : K) * q) ^ k) * hrp + (-((q : K) * q)) * hr

omit hp in
theorem P_ne_zero : (q : K) * q ≠ 0 := mul_ne_zero q.ne_zero q.ne_zero

theorem pow_sub_one_ne (a : ℕ) : ((q : K) * q) ^ (a + 1) - 1 ≠ 0 :=
  sub_ne_zero.mpr (hp a)

omit hp in
theorem lam_eq (m : ℕ) (hp1 : (q : K) * q - 1 ≠ 0) :
    lam q m = (q : K) * q * (((q : K) * q) ^ m - 1) * (((q : K) * q) ^ (m + 1) - 1) /
      (((q : K) * q - 1) ^ 2 * ((q : K) * q) ^ m) := by
  rw [eq_div_iff (mul_ne_zero (pow_ne_zero _ hp1) (pow_ne_zero _ (P_ne_zero q))), ← mul_assoc]
  exact lam_mul_eq q m

omit hp in
theorem subd_eq (m : ℕ) (hp1 : (q : K) * q - 1 ≠ 0) :
    subd q m = (q : K) * (((q : K) * q) ^ (m + 1) - 1) ^ 2 /
      (((q : K) * q - 1) ^ 2 * ((q : K) * q) ^ m) := by
  have hP := P_ne_zero q
  rw [eq_div_iff (mul_ne_zero (pow_ne_zero _ hp1) (pow_ne_zero _ hP))]
  have h1 := jk_inv_mul q (m + 1)
  have h2 := jk_mul_sub_one ((q : K) * q) (m + 1)
  apply mul_left_cancel₀ hP
  unfold subd
  rw [pow_succ] at h1 h2 ⊢
  linear_combination ((q : K) * jk ((q : K) * q) (m + 1) * ((q : K) * q - 1)) * h1 +
    ((q : K) * ((q : K) * q) * (((q : K) * q) ^ m * ((q : K) * q) - 1)) * h2

/-! ## The closed forms, as rational functions of `P = q²` and `z = P^m` -/

/-- `D_m / q`, the scaled top-but-one coefficient of `P_{m+1}`. -/
noncomputable def dx (P z : K) : K := (P * z - 1) ^ 2 / ((P - 1) * (P ^ 2 * z ^ 2 - 1))

/-- `E_m / q²`, the scaled top-but-two coefficient of `P_{m+2}`. -/
noncomputable def ex (P z : K) : K :=
  P * (P ^ 2 * z - 1) ^ 2 * (P * z - 1) ^ 2 /
    ((P - 1) * (P ^ 4 * z ^ 2 - 1) * (P ^ 2 - 1) * (P ^ 3 * z ^ 2 - 1))

/-- The norm ratio `H_{k+1} / H_k`, at `z = P^k`:
`P² z² (P z − 1)⁴ / ((P z² − 1)(P² z² − 1)²(P³ z² − 1))`. -/
noncomputable def nf (P z : K) : K :=
  P ^ 2 * z ^ 2 * (P * z - 1) ^ 4 /
    ((P * z ^ 2 - 1) * (P ^ 2 * z ^ 2 - 1) ^ 2 * (P ^ 3 * z ^ 2 - 1))

local notation "PP" => ((q : K) * q)

theorem pw_ne (m a b : ℕ) (h : 0 < a + m * b) : PP ^ a * (PP ^ m) ^ b - 1 ≠ 0 := by
  rw [← pow_mul, ← pow_add]
  obtain ⟨c, hc⟩ := Nat.exists_eq_add_of_lt h
  rw [hc, zero_add]
  exact pow_sub_one_ne q hp c

theorem hp1 : (q : K) * q - 1 ≠ 0 := by
  have := pow_sub_one_ne q hp 0; rwa [zero_add, pow_one] at this

theorem lam_succ_sub (m : ℕ) :
    lam q (m + 1) - lam q m =
      (PP ^ 2 * (PP ^ m) ^ 2 - 1) / ((PP - 1) * PP ^ m) := by
  have h1 := hp1 q hp
  have hz : PP ^ m ≠ 0 := pow_ne_zero _ (P_ne_zero q)
  have hP := P_ne_zero q
  rw [lam_eq q _ h1, lam_eq q _ h1]
  simp only [pow_succ]
  generalize PP ^ m = z at hz ⊢
  generalize (q : K) * q = P at hz h1 hP ⊢
  field_simp
  ring

theorem lam_add_two_sub (m : ℕ) :
    lam q (m + 2) - lam q m =
      (PP + 1) * (PP ^ 3 * (PP ^ m) ^ 2 - 1) / ((PP - 1) * PP * PP ^ m) := by
  have h1 := hp1 q hp
  have hz : PP ^ m ≠ 0 := pow_ne_zero _ (P_ne_zero q)
  have hP := P_ne_zero q
  rw [lam_eq q _ h1, lam_eq q _ h1]
  simp only [pow_succ]
  generalize PP ^ m = z at hz ⊢
  generalize (q : K) * q = P at hz h1 hP ⊢
  field_simp
  ring

omit hp in
theorem dx_mul (P z : K) :
    dx P (z * P) = (P ^ 2 * z - 1) ^ 2 / ((P - 1) * (P ^ 4 * z ^ 2 - 1)) := by
  unfold dx; ring

theorem D_eq (m : ℕ) : (mp q (m + 1)).coeff m = q * dx PP (PP ^ m) := by
  have h1 := hp1 q hp
  have hP := P_ne_zero q
  have hz : PP ^ m ≠ 0 := pow_ne_zero _ hP
  have a2 := pw_ne q hp m 2 2 (by omega)
  have r := mp_coeff_rel q (m + 1) m
  rw [mp_coeff_self q hp, lam_succ_sub q hp, mul_one] at r
  have hden : (PP ^ 2 * (PP ^ m) ^ 2 - 1) / ((PP - 1) * PP ^ m) ≠ 0 :=
    div_ne_zero a2 (mul_ne_zero h1 hz)
  rw [eq_div_of_mul_eq hden ((mul_comm _ _).trans r), subd_eq q m h1, dx, pow_succ PP m]
  generalize PP ^ m = z at hz a2 ⊢
  generalize (q : K) * q = P at hz h1 hP a2 ⊢
  field_simp

theorem E_eq (m : ℕ) : (mp q (m + 2)).coeff m = q * q * ex PP (PP ^ m) := by
  have h1 := hp1 q hp
  have hP := P_ne_zero q
  have hz : PP ^ m ≠ 0 := pow_ne_zero _ hP
  have a3 := pw_ne q hp m 3 2 (by omega)
  have a4 := pw_ne q hp m 4 2 (by omega)
  have h2 : PP ^ 2 - 1 ≠ 0 := by
    have := pow_sub_one_ne q hp 1; rwa [show 1 + 1 = 2 from rfl] at this
  have hP1 : PP + 1 ≠ 0 := by
    intro h0; apply h2; linear_combination (PP - 1) * h0
  have r := mp_coeff_rel q (m + 2) m
  have hD : (mp q (m + 2)).coeff (m + 1) = q * dx PP (PP ^ m * PP) := by
    rw [← pow_succ]; exact D_eq q hp (m + 1)
  rw [lam_add_two_sub q hp, hD, dx_mul] at r
  have hden : (PP + 1) * (PP ^ 3 * (PP ^ m) ^ 2 - 1) / ((PP - 1) * PP * PP ^ m) ≠ 0 :=
    div_ne_zero (mul_ne_zero hP1 a3) (mul_ne_zero (mul_ne_zero h1 hP) hz)
  rw [eq_div_of_mul_eq hden ((mul_comm _ _).trans r), subd_eq q m h1, ex, pow_succ PP m,
    show ∀ X Y B C : K, (q : K) * X / Y * ((q : K) * B) / C = q * q * (X / Y * B / C) from
      fun X Y B C => by ring]
  congr 1
  generalize PP ^ m = z at hz a3 a4 ⊢
  generalize (q : K) * q = P at hz h1 hP a3 a4 h2 hP1 ⊢
  field_simp
  ring

/-! ## The rational identities -/

omit hp in
theorem alg_step (P z : K) (h1 : P - 1 ≠ 0) (h2 : P ^ 2 - 1 ≠ 0)
    (b3 : P ^ 3 * z ^ 2 - 1 ≠ 0) (b4 : P ^ 4 * z ^ 2 - 1 ≠ 0)
    (b5 : P ^ 5 * z ^ 2 - 1 ≠ 0) (b6 : P ^ 6 * z ^ 2 - 1 ≠ 0) :
    P * (ex P z - ex P (z * P) - (dx P (z * P) - dx P (z * P * P)) * dx P (z * P)) =
      nf P (z * P) := by
  unfold ex dx nf
  rw [show P ^ 4 * (z * P) ^ 2 - 1 = P ^ 6 * z ^ 2 - 1 by ring,
    show P ^ 3 * (z * P) ^ 2 - 1 = P ^ 5 * z ^ 2 - 1 by ring,
    show P ^ 2 * (z * P) ^ 2 - 1 = P ^ 4 * z ^ 2 - 1 by ring,
    show P ^ 2 * (z * P * P) ^ 2 - 1 = P ^ 6 * z ^ 2 - 1 by ring,
    show P * (z * P) ^ 2 - 1 = P ^ 3 * z ^ 2 - 1 by ring]
  generalize hd3 : P ^ 3 * z ^ 2 - 1 = d3 at *
  generalize hd4 : P ^ 4 * z ^ 2 - 1 = d4 at *
  generalize hd5 : P ^ 5 * z ^ 2 - 1 = d5 at *
  generalize hd6 : P ^ 6 * z ^ 2 - 1 = d6 at *
  generalize he2 : P ^ 2 - 1 = e2 at *
  generalize he1 : P - 1 = e1 at *
  field_simp
  subst hd3 hd4 hd5 hd6 he2 he1
  ring

omit hp in
theorem alg_zero (P : K) (h1 : P - 1 ≠ 0) (h2 : P ^ 2 - 1 ≠ 0) (h3 : P ^ 3 - 1 ≠ 0)
    (h4 : P ^ 4 - 1 ≠ 0) :
    P * (0 - ex P 1 - (dx P 1 - dx P P) * dx P 1) = nf P 1 := by
  unfold ex dx nf
  simp only [one_pow, mul_one]
  rw [show P ^ 2 * P ^ 2 - 1 = P ^ 4 - 1 by ring]
  generalize hd3 : P ^ 3 - 1 = d3 at *
  generalize hd4 : P ^ 4 - 1 = d4 at *
  generalize he2 : P ^ 2 - 1 = e2 at *
  generalize he1 : P - 1 = e1 at *
  field_simp
  subst hd3 hd4 he2 he1
  ring

/-! ## The norm -/

theorem step_factor (k : ℕ) : H q (k + 1) = nf PP (PP ^ k) * H q k := by
  have h1 := hp1 q hp
  have h2 : PP ^ 2 - 1 ≠ 0 := by
    have := pow_sub_one_ne q hp 1; rwa [show 1 + 1 = 2 from rfl] at this
  rw [H_succ q hp k]
  congr 1
  rcases k with _ | n
  · have h3 : PP ^ 3 - 1 ≠ 0 := by
      have := pow_sub_one_ne q hp 2; rwa [show 2 + 1 = 3 from rfl] at this
    have h4 : PP ^ 4 - 1 ≠ 0 := by
      have := pow_sub_one_ne q hp 3; rwa [show 3 + 1 = 4 from rfl] at this
    have e1 : (mp q (0 + 1)).coeff 0 = q * dx PP 1 := by
      have := D_eq q hp 0; rwa [pow_zero] at this
    have e2 : (mp q (0 + 2)).coeff 0 = q * q * ex PP 1 := by
      have := E_eq q hp 0; rwa [pow_zero] at this
    have e3 : (mp q (0 + 2)).coeff (0 + 1) = q * dx PP PP := by
      have := D_eq q hp 1; rwa [pow_one] at this
    rw [coeff_X_mul_zero, e1, e2, e3, pow_zero, ← alg_zero PP h1 h2 h3 h4]
    ring
  · have b := fun a (ha : 0 < a) => pw_ne q hp n a 2 (by omega)
    have f1 : (mp q (n + 1 + 1)).coeff n = q * q * ex PP (PP ^ n) := E_eq q hp n
    have f2 : (mp q (n + 1 + 2)).coeff (n + 1) = q * q * ex PP (PP ^ n * PP) := by
      have := E_eq q hp (n + 1); rwa [pow_succ] at this
    have f3 : (mp q (n + 1 + 1)).coeff (n + 1) = q * dx PP (PP ^ n * PP) := by
      have := D_eq q hp (n + 1); rwa [pow_succ] at this
    have f4 : (mp q (n + 1 + 2)).coeff (n + 1 + 1) = q * dx PP (PP ^ n * PP * PP) := by
      have := D_eq q hp (n + 2); rwa [pow_succ, pow_succ] at this
    rw [coeff_X_mul, f1, f2, f3, f4, pow_succ PP n,
      ← alg_step PP (PP ^ n) h1 h2 (b 3 (by omega)) (b 4 (by omega)) (b 5 (by omega))
        (b 6 (by omega))]
    ring

/-- **The little q-Legendre Haar norm (monic), in closed form.**
`h(P_n²) = Π_{k<n} P²z_k²(Pz_k − 1)⁴ / ((Pz_k² − 1)(P²z_k² − 1)²(P³z_k² − 1))`, with
`P = q²` and `z_k = P^k`. -/
theorem H_eq_prod (n : ℕ) : H q n = ∏ k ∈ range n, nf PP (PP ^ k) := by
  induction n with
  | zero => rw [H_zero, prod_range_zero]
  | succ n ih => rw [step_factor q hp n, ih, prod_range_succ, mul_comm]

/-- The same norm for the eigenpolynomial `p_n = c_n P_n` itself. -/
theorem haarState_jacobiPoly_sq_eq (n : ℕ) :
    haarState q (ev q (jacobiPoly q n) * ev q (jacobiPoly q n)) =
      ((jacobiPoly q n).coeff n) ^ 2 * ∏ k ∈ range n, nf PP (PP ^ k) := by
  have hc := coeff_jacobiPoly_ne_zero q hp n
  rw [← H_eq_prod q hp, H, mp, map_smul, smul_mul_assoc, mul_smul_comm, map_smul, map_smul,
    smul_eq_mul, smul_eq_mul]
  field_simp

end QOU.FluidDynamics.QLegendreNorm
