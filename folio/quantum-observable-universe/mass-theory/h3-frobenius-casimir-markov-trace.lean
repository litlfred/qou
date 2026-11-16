import Mathlib.Tactic
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Data.Rat.Defs

/-!
# The Frobenius Casimir of `H_3(q)` and its Markov trace

Standalone file (namespace `QOU.MassCore.H3FrobeniusCasimir`).

Conventions (repo `jones-markov-trace.md`):
* `σ_i² = h σ_i + 1` with `h = q - q⁻¹` (eigenvalues `q`, `-q⁻¹`);
* Ocneanu / Markov trace `tr^z`: `tr 1 = 1`, `tr (x σ_2) = z tr x` for `x ∈ H_2`;
* convention D: `z_D = q³/(q²+1)`.

`H_3(q)` over a field `K` is modelled by its left regular representation on
`K⁶` with basis `T_w`, `w ∈ S_3`, ordered
`[1, σ₁, σ₂, σ₁σ₂, σ₂σ₁, σ₁σ₂σ₁]`.  Left multiplication by `σ₁`, `σ₂` is the
standard rule `T_s T_w = T_{sw}` (if `ℓ(sw) > ℓ(w)`), `= h T_w + T_{sw}` (else).

Main results:
* `sigma1_quad`, `sigma2_quad`, `braid`: the Hecke relations hold for the maps.
* `tr_comm`, `tr_markov`: `tr^z` is a trace with the Markov property.
* `casimir_coords`: the Casimir (handle) element of the canonical symmetrising
  form `τ₀(T_w) = δ_{w,1}`, `C₀ = Σ_w T_w T_{w⁻¹}`, in coordinates.
* `casimir_central`: `C₀` commutes with `σ₁, σ₂`.
* `tr_casimir`: `tr^z(C₀)` as an explicit rational function of `(q, z)`.
* `tr_casimir_D`: `tr^{z_D}(C₀) = [3]-type closed form`.
* `tr_casimir_D_ne`: it is **not** `2 + 1/[2]_q` (at `q = 1`, `K = ℚ`).
* `markov_weights`: `tr^z = Σ_λ y_λ(z) χ_λ` with explicit `y_λ`, and
  `y_{(1,1,1)}(z_D) = 0`.
* `inv_qdim_sum_three`: `Σ_{λ ⊢ 3} 1/dim_q λ = 2 + 1/[2]_q` (q-hook dims
  `1, [2]_q, 1`), and the D-surviving sum is `1 + 1/[2]_q`.
-/

namespace QOU.MassCore.H3FrobeniusCasimir

set_option maxHeartbeats 1000000

variable {K : Type*} [Field K]

/-- coordinates of an element of `H_3(q)` in the basis
`[1, σ₁, σ₂, σ₁σ₂, σ₂σ₁, σ₁σ₂σ₁]`. -/
abbrev V (K : Type*) := Fin 6 → K

/-- `h = q - q⁻¹`. -/
def hh (q : K) : K := q - q⁻¹

/-- left multiplication by `σ₁`. -/
def L1 (q : K) (x : V K) : V K :=
  ![x 1, x 0 + hh q * x 1, x 3, x 2 + hh q * x 3, x 5, x 4 + hh q * x 5]

/-- left multiplication by `σ₂`. -/
def L2 (q : K) (x : V K) : V K :=
  ![x 2, x 4, x 0 + hh q * x 2, x 5, x 1 + hh q * x 4, x 3 + hh q * x 5]

/-- left multiplication by the basis element `T_w`, `w` indexed by `Fin 6`. -/
def LT (q : K) : Fin 6 → V K → V K
  | 0 => id
  | 1 => L1 q
  | 2 => L2 q
  | 3 => fun x => L1 q (L2 q x)
  | 4 => fun x => L2 q (L1 q x)
  | 5 => fun x => L1 q (L2 q (L1 q x))

/-- basis vector. -/
def b (i : Fin 6) : V K := Pi.single i 1

/-- the algebra product `x * y = Σ_w x_w T_w y`. -/
def mul (q : K) (x y : V K) : V K := ∑ i : Fin 6, x i • LT q i y

/-- index of `w⁻¹`. -/
def invIdx : Fin 6 → Fin 6
  | 0 => 0 | 1 => 1 | 2 => 2 | 3 => 4 | 4 => 3 | 5 => 5

/-- values `tr^z(T_w)` of the Ocneanu trace. -/
def tval (q z : K) : Fin 6 → K := ![1, z, z, z ^ 2, z ^ 2, hh q * z ^ 2 + z]

/-- the Ocneanu/Markov trace with parameter `z`. -/
def tr (q z : K) (x : V K) : K := ∑ i : Fin 6, x i * tval q z i

/-- convention D. -/
def zD (q : K) : K := q ^ 3 / (q ^ 2 + 1)

/-! ### Hecke relations -/

theorem sigma1_quad (q : K) (x : V K) :
    L1 q (L1 q x) = hh q • L1 q x + x := by
  funext i; fin_cases i <;> simp [L1] <;> ring

theorem sigma2_quad (q : K) (x : V K) :
    L2 q (L2 q x) = hh q • L2 q x + x := by
  funext i; fin_cases i <;> simp [L2] <;> ring

theorem braid (q : K) (x : V K) :
    L1 q (L2 q (L1 q x)) = L2 q (L1 q (L2 q x)) := by
  funext i; fin_cases i <;> simp [L1, L2] <;> ring

/-- the basis vectors multiply as expected: `T_w · 1 = T_w` (sanity check). -/
theorem LT_one (q : K) (i : Fin 6) : LT q i (b 0) = b i := by
  fin_cases i <;> funext j <;> fin_cases j <;> simp [LT, L1, L2, b]

/-! ### The trace -/

theorem mul_b (q : K) (i : Fin 6) (y : V K) : mul q (b i) y = LT q i y := by
  unfold mul b
  rw [Finset.sum_eq_single i]
  · simp
  · intro j _ hj; simp [Pi.single_apply, hj]
  · simp

/-- `tr^z` is a trace on basis elements: `tr(T_v T_w) = tr(T_w T_v)`. -/
theorem tr_comm (q z : K) (i j : Fin 6) :
    tr q z (mul q (b i) (b j)) = tr q z (mul q (b j) (b i)) := by
  rw [mul_b, mul_b]
  fin_cases i <;> fin_cases j <;>
    simp [tr, b, Fin.sum_univ_succ, LT, L1, L2, tval, Pi.single_apply] <;> ring

/-- Markov property: `tr(x σ₂) = z tr(x)` for `x ∈ H_2 = span{1, σ₁}`. -/
theorem tr_markov (q z a c : K) :
    tr q z (mul q (a • b 0 + c • b 1) (b 2)) = z * tr q z (a • b 0 + c • b 1) := by
  simp [tr, mul, b, Fin.sum_univ_succ, LT, L1, L2, tval, Pi.single_apply]; ring

/-- `T_{w⁻¹}` is the `τ₀`-dual basis: `τ₀(T_v T_{w⁻¹}) = δ_{v,w}`
(`τ₀` = coefficient of `T_1`). -/
theorem tau0_dual (q : K) (hq : q ≠ 0) (i j : Fin 6) :
    (mul q (b i) (b (invIdx j))) 0 = if i = j then 1 else 0 := by
  rw [mul_b]
  fin_cases i <;> fin_cases j <;>
    simp [b, LT, L1, L2, invIdx, Pi.single_apply, hh] <;>
    field_simp <;> ring

/-! ### The Casimir element of `(H_3, τ₀)` -/

/-- `C₀ = Σ_w T_w T_{w⁻¹}`. -/
def C0 (q : K) : V K := ∑ i : Fin 6, mul q (b i) (b (invIdx i))

theorem casimir_coords (q : K) :
    C0 q = ![6, 3 * hh q, 3 * hh q, hh q ^ 2, hh q ^ 2, hh q ^ 3 + 3 * hh q] := by
  funext j; fin_cases j <;>
    simp [C0, mul, b, Fin.sum_univ_succ, LT, L1, L2, invIdx, Pi.single_apply] <;> ring

theorem casimir_central (q : K) :
    mul q (b 1) (C0 q) = mul q (C0 q) (b 1) ∧
    mul q (b 2) (C0 q) = mul q (C0 q) (b 2) := by
  rw [casimir_coords]
  constructor <;> funext j <;> fin_cases j <;>
    simp [mul, b, Fin.sum_univ_succ, LT, L1, L2, Pi.single_apply] <;> ring

/-- **Markov trace of the Frobenius Casimir, generic `z`.** -/
theorem tr_casimir (q z : K) (hq : q ≠ 0) :
    tr q z (C0 q) =
      (q ^ 8 * z ^ 2 + q ^ 7 * z + q ^ 6 * z ^ 2 + 6 * q ^ 5 * z - 4 * q ^ 4 * z ^ 2
        + 6 * q ^ 4 - 6 * q ^ 3 * z + q ^ 2 * z ^ 2 - q * z + z ^ 2) / q ^ 4 := by
  rw [casimir_coords]
  simp [tr, Fin.sum_univ_succ, tval, hh]
  field_simp
  ring

/-- **Markov trace of the Frobenius Casimir, convention D.** -/
theorem tr_casimir_D (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    tr q (zD q) (C0 q) =
      (q ^ 4 + q ^ 2 + 1) * (q ^ 6 + q ^ 4 + q ^ 2 + 5) / (q ^ 2 + 1) ^ 2 := by
  rw [tr_casimir q _ hq, zD]
  field_simp
  ring

/-- Difference from the claimed value `2 + 1/[2]_q`, as a rational function. -/
theorem tr_casimir_D_sub (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    tr q (zD q) (C0 q) - (2 + 1 / (q + q⁻¹)) =
      (q ^ 10 + 2 * q ^ 8 + 3 * q ^ 6 + 5 * q ^ 4 - q ^ 3 + 2 * q ^ 2 - q + 3)
        / (q ^ 2 + 1) ^ 2 := by
  have h2' : q + q⁻¹ ≠ 0 := by
    intro h; apply h2
    have : q * (q + q⁻¹) = q ^ 2 + 1 := by field_simp
    rw [← this, h, mul_zero]
  rw [tr_casimir_D q hq h2]
  field_simp
  ring

/-- The identity `tr_M(C_Frob) = 2 + 1/[2]_q` fails for the Frobenius Casimir:
at `q = 1` over `ℚ` the trace is `6` for every `z` (group algebra `ℚ[S₃]`,
where `C₀ = 6·1`), while `2 + 1/[2]_1 = 5/2`. -/
theorem tr_casimir_q1 (z : ℚ) : tr 1 z (C0 1) = 6 := by
  rw [tr_casimir 1 z one_ne_zero]; ring

theorem tr_casimir_D_ne :
    tr (1 : ℚ) (zD 1) (C0 1) ≠ 2 + 1 / ((1 : ℚ) + (1 : ℚ)⁻¹) := by
  rw [tr_casimir_q1]; norm_num

/-! ### Markov weights and the convention-D row cap -/

/-- characters of the three irreducibles on the basis `T_w`. -/
def chiTriv (q : K) : Fin 6 → K := ![1, q, q, q ^ 2, q ^ 2, q ^ 3]
def chiSign (q : K) : Fin 6 → K := ![1, -q⁻¹, -q⁻¹, q⁻¹ ^ 2, q⁻¹ ^ 2, -q⁻¹ ^ 3]
def chiRefl (q : K) : Fin 6 → K := ![2, hh q, hh q, -1, -1, 0]

/-- `[3]_q`-type denominator `(q²+q+1)(q²-q+1) = q⁴+q²+1`. -/
def d3 (q : K) : K := q ^ 4 + q ^ 2 + 1

def yTriv (q z : K) : K := (q * z + 1) * (q ^ 3 * z + q * z + 1) / ((q ^ 2 + 1) * d3 q)
def yRefl (q z : K) : K := q * (q - z) * (q * z + 1) / d3 q
def ySign (q z : K) : K := q ^ 2 * (z - q) * (q ^ 2 * z + z - q ^ 3) / ((q ^ 2 + 1) * d3 q)

/-- `tr^z = y_(3) χ_(3) + y_(2,1) χ_(2,1) + y_(1,1,1) χ_(1,1,1)` on every basis element. -/
theorem markov_weights (q z : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (h3 : d3 q ≠ 0)
    (i : Fin 6) :
    tval q z i = yTriv q z * chiTriv q i + yRefl q z * chiRefl q i + ySign q z * chiSign q i := by
  have h2' : 1 + q ^ 2 ≠ 0 := by rwa [add_comm]
  have h3' : 1 + q ^ 2 + q ^ 4 ≠ 0 := by
    intro h; apply h3; unfold d3; linear_combination h
  have h3u : q ^ 4 + q ^ 2 + 1 ≠ 0 := h3
  have h2u : q ^ 2 + 1 ≠ 0 := h2
  have hD : q ^ 2 * (q ^ 2 + 1) + 1 ≠ 0 := by
    intro h; apply h3u; linear_combination h
  fin_cases i <;>
    simp [tval, yTriv, yRefl, ySign, chiTriv, chiRefl, chiSign, hh] <;>
    field_simp <;> unfold d3 <;> ring

/-- Convention D kills the sign block: `y_(1,1,1)(z_D) = 0`. -/
theorem ySign_D (q : K) (h2 : q ^ 2 + 1 ≠ 0) : ySign q (zD q) = 0 := by
  have : q ^ 2 * zD q + zD q - q ^ 3 = 0 := by
    unfold zD; field_simp; ring
  simp [ySign, this]

theorem yTriv_D (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (h3 : d3 q ≠ 0) :
    yTriv q (zD q) = (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2 := by
  have h2' : 1 + q ^ 2 ≠ 0 := by rwa [add_comm]
  have h3' : 1 + q ^ 2 + q ^ 4 ≠ 0 := by
    intro h; apply h3; unfold d3; linear_combination h
  have h3u : q ^ 4 + q ^ 2 + 1 ≠ 0 := h3
  have h2u : q ^ 2 + 1 ≠ 0 := h2
  have hD : q ^ 2 * (q ^ 2 + 1) + 1 ≠ 0 := by
    intro h; apply h3u; linear_combination h
  simp only [yTriv, zD]; field_simp; unfold d3; ring

theorem yRefl_D (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (h3 : d3 q ≠ 0) :
    yRefl q (zD q) = q ^ 2 / (q ^ 2 + 1) ^ 2 := by
  have h2' : 1 + q ^ 2 ≠ 0 := by rwa [add_comm]
  have h3' : 1 + q ^ 2 + q ^ 4 ≠ 0 := by
    intro h; apply h3; unfold d3; linear_combination h
  have h3u : q ^ 4 + q ^ 2 + 1 ≠ 0 := h3
  have h2u : q ^ 2 + 1 ≠ 0 := h2
  have hD : q ^ 2 * (q ^ 2 + 1) + 1 ≠ 0 := by
    intro h; apply h3u; linear_combination h
  simp only [yRefl, zD]; field_simp; unfold d3; ring

/-- Consistency: `tr^z(C₀) = Σ_λ c_λ d_λ · d_λ y_λ(z)` with Schur elements
`c_(3) = (q²+1)d3`, `c_(2,1) = d3/q²`, `c_(1,1,1) = (q²+1)d3/q⁶` (so `C₀` acts on
the block `λ` by `c_λ d_λ`). -/
theorem tr_casimir_blocks (q z : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (h3 : d3 q ≠ 0) :
    tr q z (C0 q) =
      (q ^ 2 + 1) * d3 q * yTriv q z + (d3 q / q ^ 2) * 4 * yRefl q z
        + ((q ^ 2 + 1) * d3 q / q ^ 6) * ySign q z := by
  rw [tr_casimir q z hq]
  have h2' : 1 + q ^ 2 ≠ 0 := by rwa [add_comm]
  have h3' : 1 + q ^ 2 + q ^ 4 ≠ 0 := by
    intro h; apply h3; unfold d3; linear_combination h
  have h3u : q ^ 4 + q ^ 2 + 1 ≠ 0 := h3
  have h2u : q ^ 2 + 1 ≠ 0 := h2
  have hD : q ^ 2 * (q ^ 2 + 1) + 1 ≠ 0 := by
    intro h; apply h3u; linear_combination h
  simp only [yTriv, yRefl, ySign]
  field_simp
  ring

/-! ### Schur elements of the canonical form and the inverse-q-dimension sum -/

/-- `τ₀(T_w) = δ_{w,1}`. -/
def tau0val : Fin 6 → K := ![1, 0, 0, 0, 0, 0]

/-- Schur elements of `τ₀`: `τ₀ = Σ_λ χ_λ / c_λ` with
`c_(3) = (q²+1)d3 = q³[3]_q!`, `c_(2,1) = d3/q² = [3]_q`, `c_(1,1,1) = (q²+1)d3/q⁶ = q⁻³[3]_q!`,
i.e. `c_λ = q^{κ(λ)} ∏_{hooks} [h]_q` (`κ` = content sum). -/
theorem tau0_schur (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (h3 : d3 q ≠ 0) (i : Fin 6) :
    tau0val i = chiTriv q i / ((q ^ 2 + 1) * d3 q) + chiRefl q i * q ^ 2 / d3 q
      + chiSign q i * q ^ 6 / ((q ^ 2 + 1) * d3 q) := by
  fin_cases i <;>
    simp [tau0val, chiTriv, chiRefl, chiSign, hh] <;>
    field_simp <;> unfold d3 <;> ring

/-- The honest Frobenius reading of `Σ_{λ ⊢ 3} 1/dim_q λ`: it is
`Σ_λ q^{-κ(λ)} c_λ / [3]_q!`, the sum of the bar-symmetrised Schur elements of
the canonical form divided by `[3]_q! = [2]_q [3]_q`; equivalently
`dim_q λ = [3]_q! / (q^{-κ(λ)} c_λ)` is the balanced generic degree.  Stated with
`[2]_q = (q²+1)/q`, `[3]_q = d3/q²`. -/
theorem inv_qdim_eq_schur_sum (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (h3 : d3 q ≠ 0) :
    (q⁻¹ ^ 3 * ((q ^ 2 + 1) * d3 q) + d3 q / q ^ 2 + q ^ 3 * ((q ^ 2 + 1) * d3 q / q ^ 6))
        / (((q ^ 2 + 1) / q) * (d3 q / q ^ 2))
      = 2 + 1 / ((q ^ 2 + 1) / q) := by
  field_simp
  ring

/-! ### The inverse-q-dimension sum -/

/-- `Σ_{λ ⊢ 3} 1/dim_q λ` with q-hook dimensions `dim_q(3) = dim_q(1,1,1) = 1`,
`dim_q(2,1) = [2]_q = q + q⁻¹`. -/
theorem inv_qdim_sum_three (q : K) :
    1 / 1 + 1 / (q + q⁻¹) + 1 / 1 = 2 + 1 / (q + q⁻¹) := by ring

/-- Under convention D only `(3)` and `(2,1)` survive. -/
theorem inv_qdim_sum_three_D (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    1 / 1 + 1 / (q + q⁻¹) = (q ^ 2 + q + 1) / (q ^ 2 + 1) := by
  have : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp
  rw [this]; field_simp; ring

/-- The tautology behind the repo's `C_{dim_q}`: whatever the nonzero block
traces `t_λ`, the central element `Σ_λ e_λ / (dim_q λ · t_λ)` has trace
`Σ_λ 1/dim_q λ`.  No property of the Frobenius structure is used. -/
theorem cdimq_tautology {ι : Type*} [Fintype ι] (dq t : ι → K) (ht : ∀ i, t i ≠ 0) :
    ∑ i, (1 / (dq i * t i)) * t i = ∑ i, 1 / dq i := by
  refine Finset.sum_congr rfl fun i _ => ?_
  by_cases hd : dq i = 0
  · simp [hd]
  · field_simp [ht i]

end QOU.MassCore.H3FrobeniusCasimir

