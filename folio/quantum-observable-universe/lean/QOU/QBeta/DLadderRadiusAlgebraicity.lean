import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Topology.Order.IntermediateValue
import Mathlib.Tactic

/-!
# QOU.QBeta.DLadderRadiusAlgebraicity — the algebraicity backbone of the D-ladder radius

The D-ladder `D(w) = Σ_k d_k w^k` is the Taylor series at `w = 0` of
`D(w) = [log R(q) − log R(1/q)] / (2(q − 1/q))` in the bar-even coordinate
`w = ũ(q)`, and it is **convergent** with radius `ρ = ũ(q*)`, where `q*` is the
real root `> 1` of the irreducible degree-12 factor of the `Δ_net` numerator
(a zero of `Q_b`, hence a logarithmic branch point of `log R`).

This file formalises the **algebraic** skeleton of that statement — the part that
is exact polynomial algebra and real analysis, with no transcendental input:

1. **The clean coordinate.** With `t = q + q⁻¹` the two identities
   `(q−1)²/q = t − 2` and `√(q⁴+q²+1)/(q²+1) = √(t²−1)/t` are exact
   (`sq_sub_one_div_eq_tOf_sub_two`, `sqrt_quartic_div_eq`). They are the reason
   `ũ` is a function of `t` alone — i.e. bar-even — and hence the structural
   reason the split `log R = E(ũ) + h·D(ũ)` into bar-even and bar-odd parts
   exists at all (`h = q − q⁻¹` is bar-odd).

2. **The fold.** In the clean coordinate `ũ(t) = (t−2)·√(t²−1)/t` has
   `dũ/dt = (t³−2)/(t²√(t²−1))` (`hasDerivAt_utilde`), so the only critical
   point on `t > 1` is `t³ = 2` (`deriv_utilde_eq_zero_iff`), with critical value
   `−(t²−1)^{3/2} = −(2^{2/3}−1)^{3/2}` (`utilde_at_fold`, `utilde_at_cbrt_two`).
   That is the `|ũ| = 0.4502` entry of the singularity inventory — the fold the
   earlier search *did* find, and which is **not** the radius.

3. **Degree-12 algebraicity.** `ρ² ` is a root of the degree-12
   `Q(y) = 54289y¹² − 3911138y¹¹ + …` because `t*` is a root of
   `P_t(t) = t¹² − 24t¹⁰ + … + 3728`. The transfer is an exact identity in
   `ℤ[t]` (`QyHom_utilde_eq_Pt_mul_Ct`):
   `Z¹²·Q(Y/Z) = P_t(t)·C(t)` at `Y = (t−2)²(t²−1)`, `Z = t²`, with an explicit
   degree-36 cofactor `C`. Consequently every root of `P_t` is carried to a root
   of `Q` by `t ↦ ũ(t)²` (`Qy_utilde_sq_eq_zero`), and `P_t` has a real root in
   `(2.16108, 2.16109)` by the intermediate value theorem (`exists_root_Pt`),
   at which `0.1427 < ũ < 0.1429` (`utilde_bracket`) — the audit's
   `ρ = 0.142799996644…` to four digits, and strictly below every other entry of
   the `|ũ|` singularity inventory. Together: `exists_real_root_Qy_of_utilde_sq`.
   The two degree-12 polynomials of the audit are themselves linked by
   `q¹²·P_t(q + q⁻¹) = P_q(q)·P_q(−q)` (`Pt_tOf_mul_pow_eq`).

**What is NOT claimed here.** Nothing in this file derives `c₃`, computes any
`d_k`, or asserts that the radius of convergence of `Σ d_k w^k` *equals* the
root located below — that identification is the analytic content of the audit
(a residue computation on `log R`), not algebra, and is not formalised. Nor is
irreducibility of `P_t`, `P_q` or `Q` over `ℚ` claimed (it is true — checked in
`sympy` — but is not proved here). What is proved is the exact algebraic
backbone: the coordinate identities, the fold, and the polynomial transfer
`P_t(t) = 0 ⇒ Q(ũ(t)²) = 0` together with the existence of the real root.

Base ring (§7c): the polynomial content is stated over a generic `[CommRing R]`
/ `[Field K]`; only the `√`, ordering and IVT statements specialise to `ℝ`.

-- Ref: [leitner2026] docs/audits/2026-08-09-dladder-is-convergent-radius-is-the-qb-zero.md
-/

namespace QOU.QBeta.DLadderRadiusAlgebraicity

open Real

/-! ## 1. The clean coordinate `t = q + q⁻¹` -/

section Coordinate

variable {K : Type*} [Field K]

/-- The bar-symmetric coordinate `t = q + q⁻¹`. Invariant under `q ↦ q⁻¹`. -/
def tOf (q : K) : K := q + q⁻¹

@[simp] theorem tOf_inv (q : K) : tOf q⁻¹ = tOf q := by
  simp only [tOf, inv_inv]; ring

/-- **First exact coordinate identity:** `(q−1)²/q = t − 2`. -/
theorem sq_sub_one_div_eq_tOf_sub_two (q : K) (hq : q ≠ 0) :
    (q - 1) ^ 2 / q = tOf q - 2 := by
  simp only [tOf]
  field_simp
  ring

/-- `t·q = q² + 1`: the denominator of the second coordinate identity. -/
theorem tOf_mul (q : K) (hq : q ≠ 0) : tOf q * q = q ^ 2 + 1 := by
  simp only [tOf]; field_simp

/-- **Second exact coordinate identity, algebraic form:** `(t² − 1)·q² = q⁴ + q² + 1`.
This is the identity behind `√(q⁴+q²+1)/(q²+1) = √(t²−1)/t`; over a generic field
there is no `√`, so the content is exactly this polynomial relation. -/
theorem tOf_sq_sub_one_mul (q : K) (hq : q ≠ 0) :
    (tOf q ^ 2 - 1) * q ^ 2 = q ^ 4 + q ^ 2 + 1 := by
  simp only [tOf]; field_simp; ring

end Coordinate

section RealCoordinate

variable {q : ℝ}

/-- `t = q + q⁻¹ ≥ 2` for `q > 0` (AM–GM, via `(q−1)²/q ≥ 0`). -/
theorem two_le_tOf (hq : 0 < q) : 2 ≤ tOf q := by
  have h := sq_sub_one_div_eq_tOf_sub_two q hq.ne'
  have hnn : 0 ≤ (q - 1) ^ 2 / q := div_nonneg (sq_nonneg _) hq.le
  rw [h] at hnn
  linarith

theorem tOf_pos (hq : 0 < q) : 0 < tOf q := lt_of_lt_of_le two_pos (two_le_tOf hq)

/-- **Second exact coordinate identity, archimedean form:**
`√(q⁴ + q² + 1)/(q² + 1) = √(t² − 1)/t` for `q > 0`, `t = q + q⁻¹`. -/
theorem sqrt_quartic_div_eq (hq : 0 < q) :
    Real.sqrt (q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1)
      = Real.sqrt (tOf q ^ 2 - 1) / tOf q := by
  have ht2 : 2 ≤ tOf q := two_le_tOf hq
  have htpos : 0 < tOf q := tOf_pos hq
  have hs : (0:ℝ) ≤ tOf q ^ 2 - 1 := by nlinarith
  have hquart : q ^ 4 + q ^ 2 + 1 = (tOf q ^ 2 - 1) * q ^ 2 :=
    (tOf_sq_sub_one_mul q hq.ne').symm
  have hden : q ^ 2 + 1 = tOf q * q := (tOf_mul q hq.ne').symm
  rw [hquart, hden, Real.sqrt_mul hs, Real.sqrt_sq hq.le,
    mul_div_mul_right _ _ hq.ne']

end RealCoordinate

/-! ## 2. `ũ` in the clean coordinate, and the fold `t³ = 2` -/

/-- `ũ` as a function of the bar-even coordinate `t`: `ũ(t) = (t − 2)·√(t² − 1)/t`. -/
noncomputable def utilde (t : ℝ) : ℝ := (t - 2) * Real.sqrt (t ^ 2 - 1) / t

/-- **The derivative of `ũ` in the clean coordinate:** `dũ/dt = (t³ − 2)/(t²√(t² − 1))`. -/
theorem hasDerivAt_utilde {t : ℝ} (ht : 1 < t) :
    HasDerivAt utilde ((t ^ 3 - 2) / (t ^ 2 * Real.sqrt (t ^ 2 - 1))) t := by
  have ht0 : t ≠ 0 := by positivity
  have hs : (0:ℝ) < t ^ 2 - 1 := by nlinarith
  have hSpos : 0 < Real.sqrt (t ^ 2 - 1) := Real.sqrt_pos.mpr hs
  have hS2 : Real.sqrt (t ^ 2 - 1) ^ 2 = t ^ 2 - 1 := Real.sq_sqrt hs.le
  have hsq : HasDerivAt (fun x : ℝ => x ^ 2 - 1) (2 * t) t := by
    simpa using ((hasDerivAt_pow 2 t).sub_const 1)
  have hroot : HasDerivAt (fun x : ℝ => Real.sqrt (x ^ 2 - 1))
      (2 * t / (2 * Real.sqrt (t ^ 2 - 1))) t := hsq.sqrt hs.ne'
  have hnum : HasDerivAt (fun x : ℝ => (x - 2) * Real.sqrt (x ^ 2 - 1))
      (1 * Real.sqrt (t ^ 2 - 1) + (t - 2) * (2 * t / (2 * Real.sqrt (t ^ 2 - 1)))) t :=
    ((hasDerivAt_id t).sub_const 2).mul hroot
  have hdiv := hnum.div (hasDerivAt_id t) ht0
  refine hdiv.congr_deriv ?_
  simp only [id_eq]
  field_simp
  rw [hS2]
  ring

/-- **The fold.** On `t > 1` the only critical point of `ũ` is `t³ = 2`. -/
theorem deriv_utilde_eq_zero_iff {t : ℝ} (ht : 1 < t) :
    deriv utilde t = 0 ↔ t ^ 3 = 2 := by
  have hs : (0:ℝ) < t ^ 2 - 1 := by nlinarith
  have hSpos : 0 < Real.sqrt (t ^ 2 - 1) := Real.sqrt_pos.mpr hs
  have hden : t ^ 2 * Real.sqrt (t ^ 2 - 1) ≠ 0 := by positivity
  rw [(hasDerivAt_utilde ht).deriv, div_eq_zero_iff]
  constructor
  · rintro (h | h)
    · linarith
    · exact absurd h hden
  · intro h; left; linarith

/-- **The critical value at the fold.** At a fold point (`t³ = 2`, `t > 1`) the value
of `ũ` is `−(t² − 1)^{3/2}`. -/
theorem utilde_at_fold {t : ℝ} (ht : 1 < t) (hfold : t ^ 3 = 2) :
    utilde t = -((t ^ 2 - 1) * Real.sqrt (t ^ 2 - 1)) := by
  have ht0 : t ≠ 0 := by positivity
  simp only [utilde]
  field_simp
  nlinarith [hfold, Real.sqrt_nonneg (t ^ 2 - 1)]

/-- `1 < 2^{1/3}`. -/
private theorem one_lt_cbrt_two : (1:ℝ) < (2:ℝ) ^ ((1:ℝ) / 3) := by
  have := Real.one_lt_rpow_iff_of_pos (x := (2:ℝ)) two_pos (y := (1:ℝ)/3)
  rw [this]
  norm_num

private theorem cbrt_two_cube : ((2:ℝ) ^ ((1:ℝ) / 3)) ^ 3 = 2 := by
  rw [← Real.rpow_natCast ((2:ℝ) ^ ((1:ℝ) / 3)) 3, ← Real.rpow_mul (by norm_num)]
  norm_num

private theorem cbrt_two_sq : ((2:ℝ) ^ ((1:ℝ) / 3)) ^ 2 = (2:ℝ) ^ ((2:ℝ) / 3) := by
  rw [← Real.rpow_natCast ((2:ℝ) ^ ((1:ℝ) / 3)) 2, ← Real.rpow_mul (by norm_num)]
  norm_num

/-- **The fold value in closed form:** `ũ(2^{1/3}) = −(2^{2/3} − 1)^{3/2}`
(numerically `−0.4501964644…`, row 3 of the `|ũ|` singularity inventory). -/
theorem utilde_at_cbrt_two :
    utilde ((2:ℝ) ^ ((1:ℝ) / 3))
      = -(((2:ℝ) ^ ((2:ℝ) / 3) - 1) * Real.sqrt ((2:ℝ) ^ ((2:ℝ) / 3) - 1)) := by
  have h := utilde_at_fold one_lt_cbrt_two cbrt_two_cube
  rwa [cbrt_two_sq] at h

/-- `ũ(t)² = (t−2)²(t²−1)/t²` — the square is rational in `t`, which is what makes
the radius algebraic of degree ≤ 12. -/
theorem utilde_sq {t : ℝ} (ht : 1 ≤ t) :
    utilde t ^ 2 = (t - 2) ^ 2 * (t ^ 2 - 1) / t ^ 2 := by
  have ht0 : t ≠ 0 := by positivity
  have hs : (0:ℝ) ≤ t ^ 2 - 1 := by nlinarith
  simp only [utilde, div_pow, mul_pow, Real.sq_sqrt hs]

/-! ## 3. The degree-12 algebraicity of `ρ²` -/

section Polynomials

variable {R : Type*} [CommRing R]

/-- `P_q(q) = q¹² + 2q¹¹ − 4q¹⁰ − 8q⁹ + 6q⁸ + 16q⁷ − 10q⁶ − 16q⁵ + 6q⁴ + 8q³ − 4q² − 2q + 1`
— the irreducible degree-12 factor of the `Δ_net` numerator whose real root `> 1` is `q*`. -/
def Pq (q : R) : R :=
  q ^ 12 + 2 * q ^ 11 - 4 * q ^ 10 - 8 * q ^ 9 + 6 * q ^ 8 + 16 * q ^ 7 - 10 * q ^ 6
    - 16 * q ^ 5 + 6 * q ^ 4 + 8 * q ^ 3 - 4 * q ^ 2 - 2 * q + 1

/-- `P_t(t) = t¹² − 24t¹⁰ + 234t⁸ − 1208t⁶ + 3529t⁴ − 5572t² + 3728` — the minimal
polynomial of `t* = q* + 1/q*`. -/
def Pt (t : R) : R :=
  t ^ 12 - 24 * t ^ 10 + 234 * t ^ 8 - 1208 * t ^ 6 + 3529 * t ^ 4 - 5572 * t ^ 2 + 3728

/-- `Q(y) = 54289y¹² − 3911138y¹¹ + … + 473344` — the degree-12 polynomial annihilating `ρ²`. -/
def Qy (y : R) : R :=
  54289 * y ^ 12 - 3911138 * y ^ 11 + 116808051 * y ^ 10 - 1868914862 * y ^ 9
    + 17045659457 * y ^ 8 - 85085244936 * y ^ 7 + 190185702360 * y ^ 6
    - 60555609576 * y ^ 5 - 2279811744 * y ^ 4 - 4840969216 * y ^ 3
    + 460646672 * y ^ 2 - 30563712 * y + 473344

/-- The homogenisation `Q_hom(Y, Z) = Z¹²·Q(Y/Z)` of `Q`. -/
def QyHom (Y Z : R) : R :=
  54289 * Y ^ 12 - 3911138 * Y ^ 11 * Z + 116808051 * Y ^ 10 * Z ^ 2
    - 1868914862 * Y ^ 9 * Z ^ 3 + 17045659457 * Y ^ 8 * Z ^ 4
    - 85085244936 * Y ^ 7 * Z ^ 5 + 190185702360 * Y ^ 6 * Z ^ 6
    - 60555609576 * Y ^ 5 * Z ^ 7 - 2279811744 * Y ^ 4 * Z ^ 8
    - 4840969216 * Y ^ 3 * Z ^ 9 + 460646672 * Y ^ 2 * Z ^ 10
    - 30563712 * Y * Z ^ 11 + 473344 * Z ^ 12

/-- The explicit degree-36 cofactor `C` in `Q_hom((t−2)²(t²−1), t²) = P_t(t)·C(t)`. -/
def Ct (t : R) : R :=
  54289 * t ^ 36 - 2605872 * t ^ 35 + 56675386 * t ^ 34 - 738227880 * t ^ 33
    + 6407805721 * t ^ 32 - 38951194432 * t ^ 31 + 168943154246 * t ^ 30
    - 517657816000 * t ^ 29 + 1052438303788 * t ^ 28 - 1069464620424 * t ^ 27
    - 932237341726 * t ^ 26 + 5484511902840 * t ^ 25 - 9086060774447 * t ^ 24
    + 4997763625840 * t ^ 23 + 8677813431854 * t ^ 22 - 21933896696944 * t ^ 21
    + 19792427620461 * t ^ 20 + 522225090472 * t ^ 19 - 23217967332164 * t ^ 18
    + 28713134901568 * t ^ 17 - 13332818779952 * t ^ 16 - 8370839419392 * t ^ 15
    + 19423198652672 * t ^ 14 - 15329252567040 * t ^ 13 + 4043963431424 * t ^ 12
    + 4496950898688 * t ^ 11 - 6483479066624 * t ^ 10 + 4135690469376 * t ^ 9
    - 1166163927040 * t ^ 8 - 471764959232 * t ^ 7 + 792177868800 * t ^ 6
    - 535360438272 * t ^ 5 + 242364252160 * t ^ 4 - 79416524800 * t ^ 3
    + 18691653632 * t ^ 2 - 2931818496 * t + 244318208

set_option maxHeartbeats 1000000 in
/-- **The transfer identity in `ℤ[t]`:** `Q_hom((t−2)²(t²−1), t²) = P_t(t)·C(t)`.
This is the whole algebraic content of "`ρ²` is a root of `Q` because `t*` is a root
of `P_t`" — an exact degree-48 factorisation, with the degree-36 cofactor `C` explicit. -/
theorem QyHom_utilde_eq_Pt_mul_Ct (t : R) :
    QyHom ((t - 2) ^ 2 * (t ^ 2 - 1)) (t ^ 2) = Pt t * Ct t := by
  simp only [QyHom, Pt, Ct]
  ring

end Polynomials

section PolynomialsField

variable {K : Type*} [Field K]

/-- `Q_hom(Y, Z) = Z¹²·Q(Y/Z)` for `Z ≠ 0`. -/
theorem QyHom_eq_Qy_div (Y Z : K) (hZ : Z ≠ 0) : QyHom Y Z = Qy (Y / Z) * Z ^ 12 := by
  simp only [QyHom, Qy]
  field_simp

/-- **`P_t` and `P_q` are the same object in the two coordinates:**
`q¹²·P_t(q + q⁻¹) = P_q(q)·P_q(−q)`. -/
theorem Pt_tOf_mul_pow_eq (q : K) (hq : q ≠ 0) :
    Pt (tOf q) * q ^ 12 = Pq q * Pq (-q) := by
  simp only [Pt, Pq, tOf]
  field_simp
  ring

/-- A root of `P_q` gives a root of `P_t` at `t = q + q⁻¹`. -/
theorem Pt_tOf_eq_zero (q : K) (hq : q ≠ 0) (h : Pq q = 0) : Pt (tOf q) = 0 := by
  have hkey := Pt_tOf_mul_pow_eq q hq
  rw [h, zero_mul] at hkey
  exact (mul_eq_zero.mp hkey).resolve_right (pow_ne_zero _ hq)

/-- **The transfer, over a field:** if `t ≠ 0` is a root of `P_t`, then
`(t−2)²(t²−1)/t²` is a root of `Q`. -/
theorem Qy_div_eq_zero_of_Pt (t : K) (ht : t ≠ 0) (h : Pt t = 0) :
    Qy ((t - 2) ^ 2 * (t ^ 2 - 1) / t ^ 2) = 0 := by
  have hZ : (t ^ 2 : K) ≠ 0 := pow_ne_zero _ ht
  have hkey := QyHom_utilde_eq_Pt_mul_Ct t
  rw [QyHom_eq_Qy_div _ _ hZ, h, zero_mul] at hkey
  exact (mul_eq_zero.mp hkey).resolve_right (pow_ne_zero _ hZ)

end PolynomialsField

/-- **The headline algebraicity statement.** If `t > 1` is a root of `P_t`, then
`ũ(t)²` is a root of the degree-12 polynomial `Q`. Applied to `t = t*` this is the
audit's "`ρ²` is algebraic of degree 12". -/
theorem Qy_utilde_sq_eq_zero {t : ℝ} (ht : 1 < t) (h : Pt t = 0) : Qy (utilde t ^ 2) = 0 := by
  rw [utilde_sq ht.le]
  exact Qy_div_eq_zero_of_Pt t (by positivity) h

/-! ## 4. The real root exists: `P_t` changes sign on `(2.161, 2.162)` -/

theorem continuous_Pt : Continuous (fun t : ℝ => Pt t) := by
  simp only [Pt]
  fun_prop

/-- `P_t` has a real root strictly between `2.16108` and `2.16109`
(numerically `t* = 2.161083128024812632…`). -/
theorem exists_root_Pt : ∃ t : ℝ, 216108 / 100000 < t ∧ t < 216109 / 100000 ∧ Pt t = 0 := by
  have hlt : (216108 : ℝ) / 100000 < 216109 / 100000 := by norm_num
  have hpos : 0 < Pt ((216108 : ℝ) / 100000) := by norm_num [Pt]
  have hneg : Pt ((216109 : ℝ) / 100000) < 0 := by norm_num [Pt]
  have hmem : (0 : ℝ) ∈ Set.Ioo (Pt ((216109 : ℝ) / 100000)) (Pt ((216108 : ℝ) / 100000)) :=
    ⟨hneg, hpos⟩
  obtain ⟨t, htmem, hteq⟩ :=
    intermediate_value_Ioo' hlt.le continuous_Pt.continuousOn hmem
  exact ⟨t, htmem.1, htmem.2, hteq⟩

/-- **Numerical bracket on the radius candidate.** For any `t ∈ (2.16108, 2.16109)` —
in particular for the root `t*` of `P_t` located above — `0.1427 < ũ(t) < 0.1429`.
Numerically `ρ = ũ(t*) = 0.14279999664468968890…`. The bracket places this value
strictly below every other entry of the `|ũ|` singularity inventory (next-nearest
`0.2575`; the fold at `0.4502`), which is what makes it the *dominant* one. -/
theorem utilde_bracket {t : ℝ} (hlo : 216108 / 100000 < t) (hhi : t < 216109 / 100000) :
    1427 / 10000 < utilde t ∧ utilde t < 1429 / 10000 := by
  have ht0 : (0:ℝ) < t := by linarith
  have hs : (0:ℝ) < t ^ 2 - 1 := by nlinarith
  have hSnn : 0 ≤ Real.sqrt (t ^ 2 - 1) := Real.sqrt_nonneg _
  have hSlo : (191579 : ℝ) / 100000 < Real.sqrt (t ^ 2 - 1) := by
    rw [Real.lt_sqrt (by norm_num)]; nlinarith
  have hShi : Real.sqrt (t ^ 2 - 1) < 191581 / 100000 := by
    rw [show (191581 : ℝ) / 100000 = Real.sqrt ((191581 / 100000) ^ 2) by
      rw [Real.sqrt_sq (by norm_num)]]
    exact Real.sqrt_lt_sqrt hs.le (by nlinarith)
  have hd1 : (16108 : ℝ) / 100000 < t - 2 := by linarith
  have hd2 : t - 2 < 16109 / 100000 := by linarith
  have hprod_lo : (16108 : ℝ) / 100000 * (191579 / 100000) < (t - 2) * Real.sqrt (t ^ 2 - 1) :=
    mul_lt_mul'' hd1 hSlo (by norm_num) (by norm_num)
  have hprod_hi : (t - 2) * Real.sqrt (t ^ 2 - 1) < (16109 : ℝ) / 100000 * (191581 / 100000) :=
    mul_lt_mul'' hd2 hShi (by linarith) hSnn
  constructor
  · rw [utilde, lt_div_iff₀ ht0]; nlinarith
  · rw [utilde, div_lt_iff₀ ht0]; nlinarith

/-- **Unconditional real root of `Q` of the required shape.** There is a real `t`
in `(2.16108, 2.16109)` with `P_t(t) = 0`, `Q(ũ(t)²) = 0`, and `0.1427 < ũ(t) < 0.1429`
— i.e. the degree-12 polynomial `Q` of the audit genuinely annihilates the square of a
value of `ũ`, and that value is the audit's `ρ` to four digits. -/
theorem exists_real_root_Qy_of_utilde_sq :
    ∃ t : ℝ, Pt t = 0 ∧ Qy (utilde t ^ 2) = 0
      ∧ 1427 / 10000 < utilde t ∧ utilde t < 1429 / 10000 := by
  obtain ⟨t, hlo, hhi, hroot⟩ := exists_root_Pt
  obtain ⟨hb1, hb2⟩ := utilde_bracket hlo hhi
  exact ⟨t, hroot, Qy_utilde_sq_eq_zero (by linarith) hroot, hb1, hb2⟩

end QOU.QBeta.DLadderRadiusAlgebraicity
