import QOU.Braiding.WeakVertexT35TraceClosedForm
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

/-!
# Non-Volume Frobenius/Schur Boson Ratios on `T(2,4)`, `T(3,5)`, and `T(2,6)` (`qou-vexf`)

Formalizes Gate 2 (`qou-vexf` follow-up on PR `#9198` `WeakScaleFactorisation` and `#9204`) over a
generic field `K` (§7c: zero `ℝ`, zero empirical literals, zero `sorry`):

1. **Exact Convention-D Ocneanu–Markov Traces on `H₂(q)` (`T(2,4) = σ₀⁴`, `T(2,6) = σ₀⁶`).**
   With `z_D(q) = q³ / (q² + 1)` (`WeakVertexT35.zD`), the unique two-row (`SU(2)`) Wedderburn
   weights on `H₂(q) ≅ K_{(2)} ⊕ K_{(1,1)}` satisfying `tr_M(1) = 1` and `tr_M(σ₀) = z_D(q)` are
   `y_{(2)}^D = (q⁴ + q² + 1) / (q² + 1)²` and `y_{(1,1)}^D = q² / (q² + 1)²`. They agree
   identically with Hecke normal-form reduction `σ₀⁴ = (h³ + 2h) σ₀ + (h² + 1)`
   (`ocneanuD2_sigma0_pow4_eq_hecke`) and yield closed forms for `T(2,4)` and `T(2,6)`.

2. **4-Strand Realization `T(4,2) = (σ₀σ₁σ₂)² ∈ H₄(q)` & Markov Stabilization Invariance.**
   On `H₄(q)`, the `SU(2)` Temperley–Lieb quotient retains `(4)`, `(3,1)`, and `(2,2)`
   (`y4_partition_of_unity`), satisfies the exact five-block Schur–Plancherel identity
   `∑_{λ ⊢ 4} f_λ / c_λ(q) = 1` (`h4_schur_plancherel_sum_eq_one`), and obeys two-step positive
   Markov stabilization `tr_M^D((σ₀σ₁σ₂)²) = z_D(q)² · tr_M^D(σ₀⁴)` (`traceT42H4_eq_zD_sq_mul_T24`),
   so the link-stabilized functional `z_D^{-(n-1)} tr_M^D` is strictly strand-rank invariant
   (`linkStabilized_T42_eq_T24`).

3. **Tree-Level Weinberg Ratios `sin²θ_W = 1 - (M_W / M_Z)²` Without Fitted Parameters.**
   Connecting directly to `WeakVertexT35.weakVertexTrace` (`tr_M^D((σ₀σ₁)⁵)` in `H₃(q)`):
   - Cross-rank `(T(2,4) ∈ H₂, T(3,5) ∈ H₃)` ratios depend strongly on the `H_n` Schur carrier:
     at `q = 1`, raw Markov gives `sin²θ_W = -15`, Poincaré–Schur `M3a` gives `-7/9`, and
     irrep-by-irrep Wenzl–Higman Schur `M4` gives `17/81` (`weinbergSinSq_M4_T24_T35_one`).
   - Same-rank 2-component boson-triplet `(T(2,4), T(2,6)) ⊂ H₂(q)` cancels every `H₂`-level
     prefactor (`z_D`, `c_{(2)}`, `[2]_q!/q²`, `ℏ_q⁻²`) identically (`weinbergSinSq_scale_invariant`),
     collapsing `M1`–`M3c` to `M_W / M_Z = q²(q¹⁰ + q⁸ + q⁶ + 1) / (q¹⁴ + q¹² + q¹⁰ + 1)` with
     custodial unbroken-limit `sin²θ_W(1) = 0` (`weinbergSinSq_T24_T26_one`).

-- Ref: [leitner2026] beans qou-vexf, qou-qzvs
-- Ref: [wenzl1988] Hecke algebras of type A_n and subfactors
-- Ref: [geckpfeiffer2000] Characters of Finite Coxeter Groups and Iwahori–Hecke Algebras, Ch. 8–9
-/

namespace QOU.StandardModel.TorusLinkElectroweakSchurRatio

open QOU.Braiding.WeakVertexT35

variable {K : Type*} [Field K]

/-! ## Section 1: Convention-D Ocneanu–Markov Trace on `H₂(q)` (`T(2,4)` and `T(2,6)`) -/

/-- Convention-D Wedderburn weight `y_{(2)}^D(q) = (q⁴ + q² + 1) / (q² + 1)²` on `H₂(q)`. -/
def y2Triv (q : K) : K := (q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2

/-- Convention-D Wedderburn weight `y_{(1,1)}^D(q) = q² / (q² + 1)²` on `H₂(q)`. -/
def y2Sign (q : K) : K := q ^ 2 / (q ^ 2 + 1) ^ 2

/-- Convention-D Wedderburn trace functional on `H₂(q)` applied to eigenvalues `(a, b)`. -/
def ocneanuD2 (q a b : K) : K := y2Triv q * a + y2Sign q * b

/-- Closed-form Convention-D Markov trace of `T(2,4) = σ₀⁴ ∈ H₂(q)`. -/
def traceT24H2 (q : K) : K :=
  (q ^ 10 + q ^ 8 + q ^ 6 + 1) / (q ^ 2 * (q ^ 2 + 1) ^ 2)

/-- Closed-form Convention-D Markov trace of `T(2,6) = σ₀⁶ ∈ H₂(q)`. -/
def traceT26H2 (q : K) : K :=
  (q ^ 14 + q ^ 12 + q ^ 10 + 1) / (q ^ 4 * (q ^ 2 + 1) ^ 2)

theorem ocneanuD2_basis_one (q : K) (h2 : q ^ 2 + 1 ≠ 0) :
    ocneanuD2 q 1 1 = 1 := by
  unfold ocneanuD2 y2Triv y2Sign
  field_simp
  ring

theorem ocneanuD2_basis_sigma0 (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    ocneanuD2 q q (-q⁻¹) = zD q := by
  unfold ocneanuD2 y2Triv y2Sign zD
  field_simp
  ring

/-- Hecke normal-form consistency: `ocneanuD2` on `σ₀⁴` agrees with `(h³ + 2h) z_D + (h² + 1)`. -/
theorem ocneanuD2_sigma0_pow4_eq_hecke (q : K) (hq0 : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    ocneanuD2 q (q ^ 4) ((q⁻¹) ^ 4) =
      ((hq q) ^ 3 + 2 * hq q) * zD q + ((hq q) ^ 2 + 1) := by
  unfold ocneanuD2 y2Triv y2Sign zD hq
  field_simp [hq0, h2]
  ring

theorem traceT24H2_eq (q : K) (hq0 : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    ocneanuD2 q (q ^ 4) ((q⁻¹) ^ 4) = traceT24H2 q := by
  unfold ocneanuD2 y2Triv y2Sign traceT24H2
  field_simp [hq0, h2]

theorem traceT26H2_eq (q : K) (hq0 : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    ocneanuD2 q (q ^ 6) ((q⁻¹) ^ 6) = traceT26H2 q := by
  unfold ocneanuD2 y2Triv y2Sign traceT26H2
  field_simp [hq0, h2]

theorem traceT24H2_one (h2 : (2 : K) ≠ 0) : traceT24H2 (1 : K) = 1 := by
  unfold traceT24H2
  have h11 : (1 : K) ^ 2 + 1 = 2 := by ring
  rw [h11]
  field_simp [h2]
  ring

theorem traceT26H2_one (h2 : (2 : K) ≠ 0) : traceT26H2 (1 : K) = 1 := by
  unfold traceT26H2
  have h11 : (1 : K) ^ 2 + 1 = 2 := by ring
  rw [h11]
  field_simp [h2]
  ring

/-! ## Section 2: `H₄(q)` 4-Strand Realization `T(4,2) = (σ₀σ₁σ₂)²` & Schur–Plancherel Laws -/

/-- Convention-D Wedderburn weight `y_{(4)}^D(q)` on `H₄(q)`. -/
def y4Triv (q : K) : K := (q ^ 8 + q ^ 6 + q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 4

/-- Convention-D Wedderburn weight `y_{(3,1)}^D(q)` on `H₄(q)`. -/
def y4Refl (q : K) : K := q ^ 2 * (q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 4

/-- Convention-D Wedderburn weight `y_{(2,2)}^D(q)` on `H₄(q)`. -/
def y4TwoTwo (q : K) : K := q ^ 4 / (q ^ 2 + 1) ^ 4

/-- Closed-form Convention-D Markov trace of `T(4,2) = (σ₀σ₁σ₂)² ∈ H₄(q)`
(`χ_{(4)} = q⁶`, `χ_{(3,1)} = -q²`, `χ_{(2,2)} = 2`). -/
def traceT42H4 (q : K) : K :=
  y4Triv q * q ^ 6 + y4Refl q * (-q ^ 2) + y4TwoTwo q * 2

theorem y4_partition_of_unity (q : K) (h2 : q ^ 2 + 1 ≠ 0) :
    y4Triv q + 3 * y4Refl q + 2 * y4TwoTwo q = 1 := by
  unfold y4Triv y4Refl y4TwoTwo
  field_simp
  ring

/-- **Two-step Markov stabilization identity:** `tr_M^D((σ₀σ₁σ₂)²) = z_D(q)² · tr_M^D(σ₀⁴)`. -/
theorem traceT42H4_eq_zD_sq_mul_T24 (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    traceT42H4 q = zD q ^ 2 * traceT24H2 q := by
  unfold traceT42H4 y4Triv y4Refl y4TwoTwo zD traceT24H2
  field_simp
  ring

/-- **Link-stabilized strand-rank invariance:** `z_D⁻³ tr_M^D(β_{4,2}) = z_D⁻¹ tr_M^D(β_{2,4})`. -/
theorem linkStabilized_T42_eq_T24 (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    traceT42H4 q / zD q ^ 3 = traceT24H2 q / zD q := by
  have hz : zD q ≠ 0 := div_ne_zero (pow_ne_zero 3 hq) h2
  rw [traceT42H4_eq_zD_sq_mul_T24 q hq h2]
  field_simp [hz]

/-- Balanced `q`-integer `[k]_q` for `k = 2, 3, 4` and Wenzl–Geck–Pfeiffer Schur elements on `H₂, H₃, H₄`. -/
def qInt2 (q : K) : K := q + q⁻¹
def qInt3 (q : K) : K := q ^ 2 + 1 + (q⁻¹) ^ 2
def qInt4 (q : K) : K := q ^ 3 + q + q⁻¹ + (q⁻¹) ^ 3

def c2Triv (q : K) : K := q * qInt2 q
def c2Sign (q : K) : K := q⁻¹ * qInt2 q
def c3Triv (q : K) : K := q ^ 3 * qInt2 q * qInt3 q
def c3Std (q : K) : K := qInt3 q
def c4Triv (q : K) : K := q ^ 6 * qInt2 q * qInt3 q * qInt4 q
def c4Refl (q : K) : K := q ^ 2 * qInt4 q * qInt2 q
def c4TwoTwo (q : K) : K := qInt3 q * qInt2 q ^ 2
def c4TwoOneOne (q : K) : K := (q⁻¹) ^ 2 * qInt4 q * qInt2 q
def c4Sign (q : K) : K := (q⁻¹) ^ 6 * qInt2 q * qInt3 q * qInt4 q

/-- **Exact Plancherel Schur partition of unity on `H₄(q)`:**
`1/c_{(4)} + 3/c_{(3,1)} + 2/c_{(2,2)} + 3/c_{(2,1,1)} + 1/c_{(1⁴)} = 1`. -/
theorem h4_schur_plancherel_sum_eq_one (q : K) (hq : q ≠ 0)
    (h2 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (h4 : q ^ 4 + 1 ≠ 0) :
    1 / c4Triv q + 3 / c4Refl q + 2 / c4TwoTwo q + 3 / c4TwoOneOne q + 1 / c4Sign q = 1 := by
  have hqi2 : qInt2 q ≠ 0 := by
    intro hz; apply h2
    have hm : q * qInt2 q = q ^ 2 + 1 := by unfold qInt2; field_simp
    rw [hz, mul_zero] at hm; exact hm.symm
  have hqi3 : qInt3 q ≠ 0 := by
    intro hz; apply h3
    have hm : q ^ 2 * qInt3 q = q ^ 4 + q ^ 2 + 1 := by unfold qInt3; field_simp
    rw [hz, mul_zero] at hm; exact hm.symm
  have hqi4 : qInt4 q ≠ 0 := by
    intro hz; apply mul_ne_zero h2 h4
    have hm : q ^ 3 * qInt4 q = (q ^ 2 + 1) * (q ^ 4 + 1) := by unfold qInt4; field_simp; ring
    rw [hz, mul_zero] at hm; exact hm.symm
  unfold c4Triv c4Refl c4TwoTwo c4TwoOneOne c4Sign
  field_simp [hq, hqi2, hqi3, hqi4]
  unfold qInt2 qInt3 qInt4
  field_simp [hq]
  ring

/-! ## Section 3: Implied Tree-Level Weinberg Ratios `sin²θ_W = 1 - (M_W / M_Z)²` -/

/-- Tree-level Weinberg ratio `sin²θ_W = 1 - (M_W / M_Z)²`. -/
def weinbergSinSq (mW mZ : K) : K := 1 - (mW / mZ) ^ 2

/-- **Common-prefactor invariance:** scaling both `mW` and `mZ` by any nonzero carrier factor `S`
leaves `sin²θ_W` strictly unchanged. -/
theorem weinbergSinSq_scale_invariant (S mW mZ : K) (hS : S ≠ 0) :
    weinbergSinSq (S * mW) (S * mZ) = weinbergSinSq mW mZ := by
  unfold weinbergSinSq
  rw [mul_div_mul_left mW mZ hS]

/-- Raw Markov `M1` Weinberg ratio on `(W = T(2,4) ∈ H₂, Z = T(3,5) ∈ H₃)` equals `-15` at `q = 1`. -/
theorem weinbergSinSq_M1_T24_T35_one (h2 : (2 : K) ≠ 0) :
    weinbergSinSq (traceT24H2 (1 : K)) (weakVertexTrace (1 : K)) = -15 := by
  rw [traceT24H2_one h2, weakVertexTrace_one]
  unfold weinbergSinSq
  field_simp
  ring

/-- Poincaré–Schur `M3a` Weinberg ratio on `(T(2,4) ∈ H₂, T(3,5) ∈ H₃)` equals `-7/9` at `q = 1`. -/
theorem weinbergSinSq_M3a_T24_T35_one (h2 : (2 : K) ≠ 0) (h3 : (3 : K) ≠ 0) :
    weinbergSinSq (traceT24H2 (1 : K) * c2Triv (1 : K))
        (weakVertexTrace (1 : K) * c3Triv (1 : K)) = -7 / 9 := by
  have h6ne : (6 : K) ≠ 0 := by rw [show (6 : K) = 2 * 3 by ring]; exact mul_ne_zero h2 h3
  have h9ne : (9 : K) ≠ 0 := by rw [show (9 : K) = 3 * 3 by ring]; exact mul_ne_zero h3 h3
  rw [traceT24H2_one h2, weakVertexTrace_one]
  unfold weinbergSinSq c2Triv c3Triv qInt2 qInt3
  have hnum : (1 : K) * (1 * (1 + 1⁻¹)) / (1 / 4 * (1 ^ 3 * (1 + 1⁻¹) * (1 ^ 2 + 1 + 1⁻¹ ^ 2))) = 4 / 3 := by
    simp only [one_pow, inv_one, one_mul]
    rw [show (1 : K) + 1 = 2 by ring, show (2 : K) + 1 = 3 by ring, show (4 : K) = 2 * 2 by ring]
    field_simp [h2, h3, h6ne]
  rw [hnum]
  rw [show (9 : K) = 3 * 3 by ring]
  field_simp [h3, h9ne]
  ring

/-- Irrep-by-irrep Wenzl–Higman Schur functional `M4` on `T(2,4) ∈ H₂` and `T(3,5) ∈ H₃`. -/
def schurIrrepT24H2 (q : K) : K :=
  c2Triv q * y2Triv q * q ^ 4 + c2Sign q * y2Sign q * (q⁻¹) ^ 4

noncomputable def schurIrrepT35H3 (q : K) : K :=
  c3Triv q * yTriv q * q ^ 10 + c3Std q * yStd q * (-1)

/-- **Classical `q = 1` value of irrep-weighted Schur `M4` on `(T(2,4), T(3,5))` is `17/81`.** -/
theorem weinbergSinSq_M4_T24_T35_one (h2 : (2 : K) ≠ 0) (h3 : (3 : K) ≠ 0) :
    weinbergSinSq (schurIrrepT24H2 (1 : K)) (schurIrrepT35H3 (1 : K)) = 17 / 81 := by
  have ht24 : schurIrrepT24H2 (1 : K) = 2 := by
    unfold schurIrrepT24H2 c2Triv c2Sign y2Triv y2Sign qInt2
    simp only [one_pow, inv_one, one_mul, mul_one]
    rw [show (1 : K) + 1 = 2 by ring]
    field_simp [h2]
    ring
  have ht35 : schurIrrepT35H3 (1 : K) = 9 / 4 := by
    unfold schurIrrepT35H3 c3Triv c3Std yTriv yStd qInt2 qInt3
    simp only [one_pow, inv_one, one_mul, mul_one]
    rw [show (1 : K) + 1 = 2 by ring, show (2 : K) + 1 = 3 by ring, show (4 : K) = 2 ^ 2 by ring]
    field_simp [h2]
    ring
  rw [ht24, ht35]
  unfold weinbergSinSq
  rw [show (81 : K) = 3 ^ 4 by ring, show (9 : K) = 3 ^ 2 by ring, show (4 : K) = 2 ^ 2 by ring]
  field_simp [h2, h3]
  ring

/-- **Same-rank EW-triplet mass ratio `M(T(2,4)) / M(T(2,6))` in `H₂(q)` (`M1`–`M3c` universal):**
collapses to `q²(q¹⁰ + q⁸ + q⁶ + 1) / (q¹⁴ + q¹² + q¹⁰ + 1)`. -/
theorem ratioT24OverT26_eq (q : K) (hq0 : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (_hden : q ^ 14 + q ^ 12 + q ^ 10 + 1 ≠ 0) :
    traceT24H2 q / traceT26H2 q =
      q ^ 2 * (q ^ 10 + q ^ 8 + q ^ 6 + 1) / (q ^ 14 + q ^ 12 + q ^ 10 + 1) := by
  unfold traceT24H2 traceT26H2
  field_simp [hq0, h2]

/-- **Custodial unbroken-`SU(2)` limit on `(T(2,4), T(2,6)) ⊂ H₂(q)`:** `sin²θ_W(1) = 0`. -/
theorem weinbergSinSq_T24_T26_one (h2 : (2 : K) ≠ 0) :
    weinbergSinSq (traceT24H2 (1 : K)) (traceT26H2 (1 : K)) = 0 := by
  rw [traceT24H2_one h2, traceT26H2_one h2]
  unfold weinbergSinSq
  simp

end QOU.StandardModel.TorusLinkElectroweakSchurRatio
