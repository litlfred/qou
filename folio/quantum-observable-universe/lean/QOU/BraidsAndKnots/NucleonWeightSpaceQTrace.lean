import QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm

/-!
# The derived quantum-trace weighting of the two-term charge insertion

Setting as in `NucleonWeightSpaceTwoTerm`: level-2 Jimbo braiding, the proton-type `(2,1)` and
neutron-type `(1,2)` weight spaces of `(C²)^{⊗3}`, the Borromean nucleon `V³ = (σ₁σ₂⁻¹)³`.

**The weighting.** Convention D's Markov trace is the `U_q(sl₂)` quantum trace
`Tr(K^{⊗n} ·) / [2]_q^n` with `K = diag(q, q⁻¹)` per strand. On two strands this is checked
here against the one-crossing `Ř` (`qtrace_crossing_eq_zD`): `Tr(K⊗K Ř)/[2]_q² = q³/(q²+1)`,
the convention-D parameter `z_D`. Since `K^{⊗3}` acts on the `(2,1)` space as `q` and on the
`(1,2)` space as `q⁻¹` (`Kp`, `Kn`), the weight-space trace of an insertion `X` is

  `t_X(W_p) = q · tr(X_p V_p³) / [2]_q³`,   `t_X(W_n) = q⁻¹ · tr(X_n V_n³) / [2]_q³`.

**What is proved.**
* `deltaT_adjacent_raw_eq`: the pre-registered adjacent rule (`X = Q₁₂ + Q₂₃`, no subtraction)
  gives `(2q¹⁴−2q¹²−9q¹⁰+20q⁸−26q⁶+18q⁴−13q²+4) / (9q⁴(q²+1)³)`.
* `deltaT_adjacent_connected_eq`: with the static `(−2/9)·1` removed from the neutron insertion
  the difference is `(q−1)⁴(q+1)⁴(q²+2)(2q⁴+1) / (9q⁴(q²+1)³)`.
* `knkp_connected_eq` / `knkp_eq_qdim_div_three_mul_deltaT_connected`: the historical `KnKp`
  entry of the weighting menu, `q⁻¹·(1/3)tr_conn(n) − q·(1/3)tr_conn(p)`, is the connected
  derived difference times `[2]_q³/3`. It carries the derived weight and the classical
  normalisation `1/3` in place of the quantum dimension `[2]_q³`.
* `deltaT_allPairs_raw_eq` / `deltaT_allPairs_connected_eq_zero`: the permutation-complete
  insertion `Q₁₂ + Q₂₃ + Q₁₃` gives `P(q)/(3q⁴(q²+1)³)` with
  `P = q¹²−3q¹⁰+3q⁸−5q⁶+3q⁴−3q²+1`; its connected part is `0`.

The choice between the adjacent and the all-pairs insertion, between raw and connected, and the
overall sign of the mass contribution are not decided here. No numerical value enters.
-/

namespace QOU.BraidsAndKnots.NucleonWeightSpaceQTrace

open Matrix
open QOU.BraidsAndKnots.NucleonWeightSpaceTraces
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm

variable {R : Type*} [Field R]

/-! ## 1. The weighting on one crossing -/

/-- `K ⊗ K` on `C² ⊗ C²` in the basis `uu, ud, du, dd`. -/
def KK (q : R) : Matrix (Fin 4) (Fin 4) R := Matrix.diagonal ![q ^ 2, 1, 1, q⁻¹ ^ 2]

/-- The Jimbo crossing `Ř` on `C² ⊗ C²` in the basis `uu, ud, du, dd`. -/
def crossingR (q : R) : Matrix (Fin 4) (Fin 4) R :=
  !![q, 0, 0, 0; 0, 0, 1, 0; 0, 1, q - q⁻¹, 0; 0, 0, 0, q]

/-- `Tr(K⊗K Ř) / [2]_q² = q³/(q²+1)`: the quantum trace on one crossing is the convention-D
Markov parameter `z_D`. -/
theorem qtrace_crossing_eq_zD (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    trace (KK q * crossingR q) / (q + q⁻¹) ^ 2 = q ^ 3 / (q ^ 2 + 1) := by
  have h2 : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp
  rw [h2]
  simp [KK, crossingR, Matrix.trace, Fin.sum_univ_four, Matrix.mul_apply, Matrix.diagonal]
  field_simp
  ring

/-! ## 2. Weight-space traces under the quantum-trace weighting -/

private theorem qdim_eq (q : R) (hq : q ≠ 0) : (q + q⁻¹) ^ 3 = (q ^ 2 + 1) ^ 3 / q ^ 3 := by
  field_simp

/-- The pre-registered adjacent rule (raw insertion). -/
theorem deltaT_adjacent_raw_eq (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (h3 : (3 : R) ≠ 0) :
    (trace (Kn q * ((Q12n + Q23n) * borromeanV3B q)) -
        trace (Kp q * ((Q12p + Q23p) * borromeanV3A q))) / (q + q⁻¹) ^ 3 =
      (2 * q ^ 14 - 2 * q ^ 12 - 9 * q ^ 10 + 20 * q ^ 8 - 26 * q ^ 6 + 18 * q ^ 4
          - 13 * q ^ 2 + 4) / (9 * q ^ 4 * (q ^ 2 + 1) ^ 3) := by
  have h9 : (9 : R) = 3 * 3 := by ring
  rw [Kn, Kp, Matrix.smul_mul, Matrix.smul_mul, Matrix.one_mul, Matrix.one_mul,
    Matrix.trace_smul, Matrix.trace_smul, smul_eq_mul, smul_eq_mul,
    trace_QAdjn_borromeanV3 q hq h3, trace_QAdjp_borromeanV3 q hq h3, qdim_eq q hq]
  rw [h9]; field_simp; ring

/-- The connected adjacent insertion: static `(−2/9)·1` removed from the neutron side. -/
theorem deltaT_adjacent_connected_eq (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (h3 : (3 : R) ≠ 0) :
    (q⁻¹ * (trace ((Q12n + Q23n) * borromeanV3B q) + (2 / 9 : R) * trace (borromeanV3B q)) -
        q * trace ((Q12p + Q23p) * borromeanV3A q)) / (q + q⁻¹) ^ 3 =
      (q - 1) ^ 4 * (q + 1) ^ 4 * (q ^ 2 + 2) * (2 * q ^ 4 + 1) /
        (9 * q ^ 4 * (q ^ 2 + 1) ^ 3) := by
  have h9 : (9 : R) = 3 * 3 := by ring
  rw [trace_QAdjn_borromeanV3_connected q hq h3, trace_QAdjp_borromeanV3 q hq h3, qdim_eq q hq]
  rw [h9]; field_simp; ring

/-- Closed form of the historical `KnKp` entry on the connected traces (with its `1/3`). -/
theorem knkp_connected_eq (q : R) (hq : q ≠ 0) (h3 : (3 : R) ≠ 0) :
    q⁻¹ * ((1 / 3 : R) * (trace ((Q12n + Q23n) * borromeanV3B q) +
          (2 / 9 : R) * trace (borromeanV3B q))) -
        q * ((1 / 3 : R) * trace ((Q12p + Q23p) * borromeanV3A q)) =
      (q - 1) ^ 4 * (q + 1) ^ 4 * (q ^ 2 + 2) * (2 * q ^ 4 + 1) / (27 * q ^ 7) := by
  have h9 : (9 : R) = 3 * 3 := by ring
  have h27 : (27 : R) = 3 * 3 * 3 := by ring
  rw [trace_QAdjn_borromeanV3_connected q hq h3, trace_QAdjp_borromeanV3 q hq h3]
  rw [h9, h27]; field_simp; ring

/-- `KnKp = ([2]_q³ / 3) · Δt_derived^{conn}`: the menu entry carries the derived weight with
the normalisation `1/3` in place of `1/[2]_q³`. -/
theorem knkp_eq_qdim_div_three_mul_deltaT_connected (q : R) (hq : q ≠ 0)
    (hq2 : q ^ 2 + 1 ≠ 0) (h3 : (3 : R) ≠ 0) :
    q⁻¹ * ((1 / 3 : R) * (trace ((Q12n + Q23n) * borromeanV3B q) +
          (2 / 9 : R) * trace (borromeanV3B q))) -
        q * ((1 / 3 : R) * trace ((Q12p + Q23p) * borromeanV3A q)) =
      (q + q⁻¹) ^ 3 / 3 *
        ((q⁻¹ * (trace ((Q12n + Q23n) * borromeanV3B q) +
              (2 / 9 : R) * trace (borromeanV3B q)) -
            q * trace ((Q12p + Q23p) * borromeanV3A q)) / (q + q⁻¹) ^ 3) := by
  rw [knkp_connected_eq q hq h3, deltaT_adjacent_connected_eq q hq hq2 h3, qdim_eq q hq]
  have h9 : (9 : R) = 3 * 3 := by ring
  have h27 : (27 : R) = 3 * 3 * 3 := by ring
  rw [h9, h27]; field_simp

/-- The permutation-complete insertion `Q₁₂ + Q₂₃ + Q₁₃` (raw). -/
theorem deltaT_allPairs_raw_eq (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (h3 : (3 : R) ≠ 0) :
    (trace (Kn q * ((Q12n + Q23n + Q13n) * borromeanV3B q)) -
        trace (Kp q * ((Q12p + Q23p + Q13p) * borromeanV3A q))) / (q + q⁻¹) ^ 3 =
      (q ^ 12 - 3 * q ^ 10 + 3 * q ^ 8 - 5 * q ^ 6 + 3 * q ^ 4 - 3 * q ^ 2 + 1) /
        (3 * q ^ 4 * (q ^ 2 + 1) ^ 3) := by
  rw [QPairN_eq_sum h3, QPairP_eq_sum, QPairN, QPairP, Kn, Kp]
  simp only [Matrix.smul_mul, Matrix.one_mul, Matrix.zero_mul, Matrix.mul_zero,
    Matrix.trace_smul, Matrix.trace_zero, smul_eq_mul]
  rw [trace_borromeanV3B q hq, qdim_eq q hq]
  field_simp; ring

/-- The connected part of the permutation-complete insertion vanishes on `V³`. -/
theorem deltaT_allPairs_connected_eq_zero (q : R) (h3 : (3 : R) ≠ 0) :
    q⁻¹ * (trace ((Q12n + Q23n + Q13n) * borromeanV3B q) + (1 / 3 : R) * trace (borromeanV3B q)) -
        q * trace ((Q12p + Q23p + Q13p) * borromeanV3A q) = 0 := by
  rw [QPairN_eq_sum h3, QPairP_eq_sum, QPairN, QPairP]
  simp only [Matrix.smul_mul, Matrix.one_mul, Matrix.zero_mul, Matrix.trace_smul,
    Matrix.trace_zero, smul_eq_mul]
  ring

end QOU.BraidsAndKnots.NucleonWeightSpaceQTrace
