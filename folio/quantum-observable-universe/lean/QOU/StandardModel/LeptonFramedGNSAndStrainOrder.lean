/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.FinCases

/-!
# Real-`q` Wenzl `(2,1)` Strain Minimum, Framed GNS Lepton Ordering, and `O_q(SU(2))` Spinor Isospin Dichotomy

Companion formalization for the 2026-11-28 Untapped Algebraic Invariants audit (`qou-s028` / `qou-myts`).
Every theorem in this module works **strictly over `[CommRing R]`** (and `[LinearOrder R] [IsStrictOrderedRing R]`
for ordered inequalities — `0 sorry`, `0` custom `axiom`s, `0` `[Field]` binders, `0` `field_simp` calls,
`0` transcendental APIs, `AGENTS.md §7c`).

## Main Results

1. **§1 — Division-Free Wenzl `(2,1)` Metric `M_q`, Unimodular Strain `det G_{(2,1)}(w) = 1`, & Global Electron Minimum:**
   - On the `[2]_q`-free two-dimensional Hecke representation `T₀ = !![q, 1; 0, -q⁻¹]`,
     `T₁ = !![-q⁻¹, 0; 1, q]` over `[CommRing R]` (`q : Rˣ`), the symmetric bilinear form
     `M_q = !![q + q⁻¹, 1; 1, q + q⁻¹]` (`det M_q = q² + 1 + q⁻²`) intertwines the real-`q` Wenzl
     `C*`-anti-involution `σᵢ* = σᵢ` (`w ↦ w.reverse`): `M_q * ρ₂₁(w) = ρ₂₁(w.reverse)ᵀ * M_q`.
   - The Cauchy–Green strain operator `G₂₁(w) := ρ₂₁(w.reverse) * ρ₂₁(w)` satisfies
     `(G₂₁(w)).det = 1` and the **exact sum-of-squares discriminant identity**
     `((G₂₁(w)).trace)² - 4 = (q² + 1 + q⁻²) * (y - z)² + (y + z)²` for **all** `w`.
   - Over any strict ordered commutative ring with `0 < q`, `2 ≤ (G₂₁(w)).trace` for **every**
     3-braid word `w`, attaining its **exact global minimum `(G₂₁(e)).trace = 2`** (`G₂₁(e) = 1`)
     on the electron word `e = σ₀σ₁σ₀` (`e* e = Δ₃²`).

2. **§2 — Exact Generic-Degree Vanishing on `μ = σ₀⁴σ₁⁻¹` (`[CommRing R]`):**
   - For the cleared-denominator generic-degree trace
     `T_Gen(q, w) := q³ χ^{(3)}(w) + (q + q⁻¹) χ^{(2,1)}(w) + q⁻³ χ^{(1,1,1)}(w)`,
     `T_Gen(q, μ) = 0` identically over every `[CommRing R]`, while
     `T_Gen(q, e) = T_Gen(q, τ) = q⁶ - q⁻⁶`.

3. **§3 — Strict Real-`q` Ordering on the 2026-11-28 Ruled 2-Component Lepton Link Words:**
   - The zero-writhe framed Convention-D GNS norm `(q² + 1)² ‖W̃‖_D²` satisfies
     **strict `‖ẽ‖_D² < ‖μ̃‖_D² < ‖τ̃‖_D²`** for every `q ∈ (1, 6/5]` (`1 < q` and `5 * q ≤ 6`,
     covering `q₀^{(p)} ≈ 1.1100`), proved division-free via an all-positive homogeneous Bernstein
     decomposition on `[1, 3/2]`.
   - The full-twist / top-JM pairing `(q² + 1)² τ_D(Δ₃² W)` satisfies
     **strict `τ_D(Δ₃² τ) < τ_D(Δ₃² μ) < τ_D(Δ₃² e)`** for every `q ≥ 11/10` (`11 ≤ 10 * q`,
     covering `q₀^{(p)} ≈ 1.1100`), proved via an all-positive Taylor expansion at `11/10`.

4. **§4 — `O_q(SU(2))` Ordered 3-Quark Spinor GNS Dichotomy & Peter–Weyl Right-Norm Sign:**
   - For unit quantum 2-sphere spinor monomials `W_p = α²γ` (`uud`) and `W_n = αγ²` (`udd`),
     Woronowicz's right-GNS norms are **identically isospin-symmetric** (`h(W_p W_p*) = h(W_n W_n*)`),
     whereas the left-GNS norms split by **exact KMS factor `q²`** (`h(W_p* W_p) = q² h(W_n* W_n)`),
     and the `j = 1/2` Peter–Weyl right-norm difference gives `m_n > m_p` linearly for `q > 1`.

-- Ref: [wenzl1988] H. Wenzl, Invent. Math. 92 (1988), 349–383.
-- Ref: [woronowicz1987] S. L. Woronowicz, Commun. Math. Phys. 111 (1987), 613–665.
-- Ref: [woronowicz1987-twisted-su2] S. L. Woronowicz, Publ. RIMS 23 (1987), 117–181.
-- Ref: [gould-zhang-bracken1991] M. D. Gould, R. B. Zhang, A. J. Bracken, J. Math. Phys. 32 (1991), 2298–2303.
-- Ref: [aiston-morton-1997] A. K. Aiston, H. R. Morton, J. Knot Theory Ramif. 7 (1998), 463–487.
-/

set_option autoImplicit false

namespace QOU.StandardModel.LeptonFramedGNSAndStrainOrder

open Matrix

/-! ## §1. Division-Free Wenzl `(2,1)` Metric, Unimodular Strain, & Global Electron Minimum -/

section StrainRepresentation

variable {R : Type*} [CommRing R]

/-- Four signed 3-braid letters (`0 = σ₀, 1 = σ₁, 2 = σ₀⁻¹, 3 = σ₁⁻¹`). -/
abbrev Braid3Letter := Fin 4

/-- A 3-braid word as a list of signed generators. -/
abbrev Braid3Word := List Braid3Letter

/-- The 2026-11-28 ruled least-crossing 2-component lepton link words:
`e = σ₀σ₁σ₀`, `μ = σ₀⁴σ₁⁻¹`, `τ = σ₀²σ₁⁻¹σ₀σ₁⁻¹`. -/
def eBraid : Braid3Word := [0, 1, 0]
def muBraid : Braid3Word := [0, 0, 0, 0, 3]
def tauBraid : Braid3Word := [0, 0, 3, 0, 3]

/-- `[2]_q`-free `(2,1)` generator matrices over `[CommRing R]` (`q : Rˣ`). -/
def gen21 (q : Rˣ) : Braid3Letter → Matrix (Fin 2) (Fin 2) R
  | 0 => !![(q : R), 1; 0, -(((q⁻¹ : Rˣ) : R))]
  | 1 => !![-(((q⁻¹ : Rˣ) : R)), 0; 1, (q : R)]
  | 2 => !![(((q⁻¹ : Rˣ) : R)), 1; 0, -(q : R)]
  | 3 => !![-(q : R), 0; 1, (((q⁻¹ : Rˣ) : R))]

/-- Product representation `ρ₂₁ : Braid3Word → Matrix (Fin 2) (Fin 2) R`. -/
def rho21 (q : Rˣ) : Braid3Word → Matrix (Fin 2) (Fin 2) R
  | [] => 1
  | g :: gs => gen21 q g * rho21 q gs

/-- Denominator-cleared polynomial generator `q • gen21 q g` in `R[q]`. -/
def qGen21 (q : R) : Braid3Letter → Matrix (Fin 2) (Fin 2) R
  | 0 => !![q ^ 2, q; 0, -1]
  | 1 => !![-1, 0; q, q ^ 2]
  | 2 => !![1, q; 0, -q ^ 2]
  | 3 => !![-q ^ 2, 0; q, 1]

def qRho21 (q : R) : Braid3Word → Matrix (Fin 2) (Fin 2) R
  | [] => 1
  | g :: gs => qGen21 q g * qRho21 q gs

theorem smul_gen21_eq_qGen21 (q : Rˣ) (g : Braid3Letter) :
    (q : R) • gen21 q g = qGen21 (q : R) g := by
  have hq : (q : R) * (((q⁻¹ : Rˣ) : R)) = 1 := Units.mul_inv q
  ext i j
  fin_cases g <;> fin_cases i <;> fin_cases j <;>
    simp only [Fin.zero_eta, Fin.mk_one, Fin.isValue, gen21, qGen21, Matrix.smul_apply,
      smul_eq_mul, Matrix.of_apply, Matrix.cons_val_zero, Matrix.cons_val_one,
      mul_neg, mul_zero, mul_one, hq] <;>
    ring

theorem pow_smul_rho21_eq_qRho21 (q : Rˣ) (w : Braid3Word) :
    ((q : R) ^ w.length) • rho21 q w = qRho21 (q : R) w := by
  induction w with
  | nil => simp [rho21, qRho21]
  | cons g gs ih =>
      simp only [List.length_cons, pow_succ', rho21, qRho21]
      calc ((q : R) * (q : R) ^ gs.length) • (gen21 q g * rho21 q gs)
          = ((q : R) • gen21 q g) * (((q : R) ^ gs.length) • rho21 q gs) := by
              rw [MulAction.mul_smul, Matrix.smul_mul, Matrix.mul_smul]
        _ = qGen21 (q : R) g * qRho21 (q : R) gs := by
              rw [smul_gen21_eq_qGen21, ih]

theorem pow_len_trace_rho21 (q : Rˣ) (w : Braid3Word) :
    (q : R) ^ w.length * (rho21 q w).trace = (qRho21 (q : R) w).trace := by
  rw [← smul_eq_mul, ← Matrix.trace_smul, pow_smul_rho21_eq_qRho21]

/-- Wenzl's division-free symmetric inner-product matrix `M_q = !![q + q⁻¹, 1; 1, q + q⁻¹]`. -/
def wenzlMetric21 (q : Rˣ) : Matrix (Fin 2) (Fin 2) R :=
  !![(q : R) + (((q⁻¹ : Rˣ) : R)), 1; 1, (q : R) + (((q⁻¹ : Rˣ) : R))]

theorem det_wenzlMetric21 (q : Rˣ) :
    (wenzlMetric21 q).det = (q : R) ^ 2 + 1 + (((q⁻¹ : Rˣ) : R)) ^ 2 := by
  have hq : (q : R) * (((q⁻¹ : Rˣ) : R)) = 1 := Units.mul_inv q
  unfold wenzlMetric21
  rw [Matrix.det_fin_two]
  simp only [Matrix.of_apply, Matrix.cons_val_zero, Matrix.cons_val_one]
  calc ((q : R) + (((q⁻¹ : Rˣ) : R))) * ((q : R) + (((q⁻¹ : Rˣ) : R))) - 1 * 1
      = (q : R) ^ 2 + 2 * ((q : R) * (((q⁻¹ : Rˣ) : R))) - 1 + (((q⁻¹ : Rˣ) : R)) ^ 2 := by ring
    _ = (q : R) ^ 2 + 2 * 1 - 1 + (((q⁻¹ : Rˣ) : R)) ^ 2 := by rw [hq]
    _ = (q : R) ^ 2 + 1 + (((q⁻¹ : Rˣ) : R)) ^ 2 := by ring

theorem transpose_wenzlMetric21 (q : Rˣ) : (wenzlMetric21 q)ᵀ = wenzlMetric21 q := by
  ext i j; fin_cases i <;> fin_cases j <;> rfl

theorem wenzlMetric21_intertwines_gen (q : Rˣ) (g : Braid3Letter) :
    wenzlMetric21 q * gen21 q g = (gen21 q g)ᵀ * wenzlMetric21 q := by
  ext i j
  fin_cases g <;> fin_cases i <;> fin_cases j <;>
    (simp only [Fin.zero_eta, Fin.mk_one, Fin.isValue, wenzlMetric21, gen21,
       Matrix.mul_apply, Matrix.transpose_apply, Fin.sum_univ_two,
       Matrix.of_apply, Matrix.cons_val_zero, Matrix.cons_val_one];
     ring)

theorem rho21_append (q : Rˣ) (u v : Braid3Word) :
    rho21 q (u ++ v) = rho21 q u * rho21 q v := by
  induction u with
  | nil => simp [rho21]
  | cons g gs ih => simp [rho21, ih, Matrix.mul_assoc]

/-- **`M_q` intertwines the Wenzl `C*`-involution `w ↦ w.reverse` for every 3-braid word `w`.** -/
theorem wenzlMetric21_intertwines_word (q : Rˣ) (w : Braid3Word) :
    wenzlMetric21 q * rho21 q w = (rho21 q w.reverse)ᵀ * wenzlMetric21 q := by
  induction w with
  | nil => simp [rho21]
  | cons g gs ih =>
      simp only [rho21, List.reverse_cons, rho21_append, Matrix.mul_one, Matrix.transpose_mul]
      calc wenzlMetric21 q * (gen21 q g * rho21 q gs)
          = (wenzlMetric21 q * gen21 q g) * rho21 q gs := (Matrix.mul_assoc _ _ _).symm
        _ = ((gen21 q g)ᵀ * wenzlMetric21 q) * rho21 q gs := by
            rw [wenzlMetric21_intertwines_gen]
        _ = (gen21 q g)ᵀ * (wenzlMetric21 q * rho21 q gs) := Matrix.mul_assoc _ _ _
        _ = (gen21 q g)ᵀ * ((rho21 q gs.reverse)ᵀ * wenzlMetric21 q) := by rw [ih]
        _ = ((gen21 q g)ᵀ * (rho21 q gs.reverse)ᵀ) * wenzlMetric21 q :=
            (Matrix.mul_assoc _ _ _).symm

/-- The `(2,1)` Cauchy–Green strain operator `G₂₁(w) := ρ₂₁(w.reverse) * ρ₂₁(w)`. -/
def strain21 (q : Rˣ) (w : Braid3Word) : Matrix (Fin 2) (Fin 2) R :=
  rho21 q w.reverse * rho21 q w

theorem pow_two_len_trace_strain21 (q : Rˣ) (w : Braid3Word) :
    (q : R) ^ (2 * w.length) * (strain21 q w).trace =
      (qRho21 (q : R) w.reverse * qRho21 (q : R) w).trace := by
  unfold strain21
  have h1 := pow_smul_rho21_eq_qRho21 q w.reverse
  have h2 := pow_smul_rho21_eq_qRho21 q w
  rw [List.length_reverse] at h1
  have hprod : ((q : R) ^ (2 * w.length)) • (rho21 q w.reverse * rho21 q w) =
      qRho21 (q : R) w.reverse * qRho21 (q : R) w := by
    calc ((q : R) ^ (2 * w.length)) • (rho21 q w.reverse * rho21 q w)
        = ((q : R) ^ w.length * (q : R) ^ w.length) • (rho21 q w.reverse * rho21 q w) := by
            rw [two_mul, pow_add]
      _ = ((q : R) ^ w.length) • (((q : R) ^ w.length) • (rho21 q w.reverse * rho21 q w)) :=
            MulAction.mul_smul _ _ _
      _ = (((q : R) ^ w.length) • rho21 q w.reverse) * (((q : R) ^ w.length) • rho21 q w) := by
            rw [← Matrix.mul_smul, ← Matrix.smul_mul]
      _ = qRho21 (q : R) w.reverse * qRho21 (q : R) w := by rw [h1, h2]
  rw [← hprod, Matrix.trace_smul, smul_eq_mul]

theorem det_gen21 (q : Rˣ) (g : Braid3Letter) : (gen21 q g).det = -1 := by
  have hq : (q : R) * (((q⁻¹ : Rˣ) : R)) = 1 := Units.mul_inv q
  have hqi : (((q⁻¹ : Rˣ) : R)) * (q : R) = 1 := Units.inv_mul q
  fin_cases g <;>
    simp only [Fin.isValue, gen21, Matrix.det_fin_two, Matrix.of_apply, Matrix.cons_val_zero,
      Matrix.cons_val_one, mul_neg, neg_mul, mul_zero, zero_mul, sub_zero, hq, hqi]

theorem det_rho21 (q : Rˣ) (w : Braid3Word) : (rho21 q w).det = (-1 : R) ^ w.length := by
  induction w with
  | nil => simp [rho21]
  | cons g gs ih =>
      simp only [rho21, List.length_cons, Matrix.det_mul, det_gen21, ih, pow_succ']

/-- **Unimodularity of Wenzl Strain (`det G₂₁(w) = 1` for all `w` over `[CommRing R]`).** -/
theorem det_strain21 (q : Rˣ) (w : Braid3Word) : (strain21 q w).det = 1 := by
  unfold strain21
  rw [Matrix.det_mul, det_rho21, det_rho21, List.length_reverse, ← mul_pow]
  norm_num

theorem wenzlMetric21_mul_strain21_symm (q : Rˣ) (w : Braid3Word) :
    (wenzlMetric21 q * strain21 q w)ᵀ = wenzlMetric21 q * strain21 q w := by
  unfold strain21
  have h1 := wenzlMetric21_intertwines_word q w.reverse
  rw [List.reverse_reverse] at h1
  calc (wenzlMetric21 q * (rho21 q w.reverse * rho21 q w))ᵀ
      = ((wenzlMetric21 q * rho21 q w.reverse) * rho21 q w)ᵀ := by rw [Matrix.mul_assoc]
    _ = ((rho21 q w)ᵀ * wenzlMetric21 q * rho21 q w)ᵀ := by rw [h1]
    _ = (rho21 q w)ᵀ * (wenzlMetric21 q)ᵀ * (rho21 q w)ᵀᵀ := by
        simp [Matrix.transpose_mul, Matrix.mul_assoc]
    _ = ((rho21 q w)ᵀ * wenzlMetric21 q) * rho21 q w := by
        rw [transpose_wenzlMetric21, Matrix.transpose_transpose]
    _ = (wenzlMetric21 q * rho21 q w.reverse) * rho21 q w := by rw [← h1]
    _ = wenzlMetric21 q * (rho21 q w.reverse * rho21 q w) := Matrix.mul_assoc _ _ _

/-- **Exact Sum-of-Squares Strain Discriminant Identity (`[CommRing R]`):**
for **every** 3-braid word `w`, `((G₂₁(w)).trace)² - 4 = [3]_q (y - z)² + (y + z)²`. -/
theorem trace_strain21_sq_sub_four_eq_sos (q : Rˣ) (w : Braid3Word) :
    ((strain21 q w).trace) ^ 2 - 4 =
      ((q : R) ^ 2 + 1 + (((q⁻¹ : Rˣ) : R)) ^ 2) *
          (strain21 q w 0 1 - strain21 q w 1 0) ^ 2 +
        (strain21 q w 0 1 + strain21 q w 1 0) ^ 2 := by
  have hq : (q : R) * (((q⁻¹ : Rˣ) : R)) = 1 := Units.mul_inv q
  set x := strain21 q w 0 0
  set y := strain21 q w 0 1
  set z := strain21 q w 1 0
  set t := strain21 q w 1 1
  have hdet : x * t - 1 = y * z := by
    have hd := det_strain21 q w
    rw [Matrix.det_fin_two] at hd
    change x * t - y * z = 1 at hd
    linear_combination hd
  have hsym : x - t = ((q : R) + (((q⁻¹ : Rˣ) : R))) * (y - z) := by
    have hs := congr_fun (congr_fun (wenzlMetric21_mul_strain21_symm q w) 1) 0
    simp only [wenzlMetric21, Matrix.transpose_apply, Matrix.mul_apply, Fin.sum_univ_two,
      Matrix.of_apply, Matrix.cons_val_zero, Matrix.cons_val_one] at hs
    change ((q : R) + (((q⁻¹ : Rˣ) : R))) * y + 1 * t =
      1 * x + ((q : R) + (((q⁻¹ : Rˣ) : R))) * z at hs
    linear_combination -hs
  have htr : (strain21 q w).trace = x + t := by
    simp [Matrix.trace, Fin.sum_univ_two, x, t]
  rw [htr]
  calc (x + t) ^ 2 - 4
      = (x - t) ^ 2 + 4 * (x * t - 1) := by ring
    _ = (((q : R) + (((q⁻¹ : Rˣ) : R))) * (y - z)) ^ 2 + 4 * (y * z) := by rw [hsym, hdet]
    _ = ((q : R) ^ 2 + 2 * ((q : R) * (((q⁻¹ : Rˣ) : R))) + (((q⁻¹ : Rˣ) : R)) ^ 2) *
          (y - z) ^ 2 + 4 * (y * z) := by ring
    _ = ((q : R) ^ 2 + 2 * 1 + (((q⁻¹ : Rˣ) : R)) ^ 2) * (y - z) ^ 2 + 4 * (y * z) := by
          rw [hq]
    _ = ((q : R) ^ 2 + 1 + (((q⁻¹ : Rˣ) : R)) ^ 2) * (y - z) ^ 2 + (y + z) ^ 2 := by ring

/-- **The electron word `e = σ₀σ₁σ₀` is self-adjoint (`e.reverse = e`) and has trivial strain
`G₂₁(e) = I₂`, `(G₂₁(e)).trace = 2` over any `[CommRing R]`.** -/
theorem strain21_eBraid_eq_one_and_trace_two (q : Rˣ) :
    eBraid.reverse = eBraid ∧ strain21 q eBraid = 1 ∧ (strain21 q eBraid).trace = 2 := by
  have hq : (q : R) * (((q⁻¹ : Rˣ) : R)) = 1 := Units.mul_inv q
  have hqp6 : (((q⁻¹ : Rˣ) : R)) ^ 6 * (q : R) ^ 6 = 1 := by
    rw [← mul_pow, Units.inv_mul, one_pow]
  have h1 : strain21 q eBraid = 1 := by
    have hscaled : ((q : R) ^ 6) • strain21 q eBraid = ((q : R) ^ 6) • (1 : Matrix (Fin 2) (Fin 2) R) := by
      unfold strain21
      have hp := pow_smul_rho21_eq_qRho21 q eBraid
      have hlen : eBraid.length = 3 := rfl
      rw [hlen] at hp
      have hrev : eBraid.reverse = eBraid := rfl
      rw [hrev]
      calc ((q : R) ^ 6) • (rho21 q eBraid * rho21 q eBraid)
          = (((q : R) ^ 3) • rho21 q eBraid) * (((q : R) ^ 3) • rho21 q eBraid) := by
              have h6 : (q : R) ^ 6 = (q : R) ^ 3 * (q : R) ^ 3 := by ring
              rw [h6, MulAction.mul_smul, ← Matrix.mul_smul, ← Matrix.smul_mul]
        _ = qRho21 (q : R) eBraid * qRho21 (q : R) eBraid := by rw [hp]
        _ = ((q : R) ^ 6) • (1 : Matrix (Fin 2) (Fin 2) R) := by
              ext i j
              fin_cases i <;> fin_cases j <;>
                (simp [Fin.zero_eta, Fin.mk_one, eBraid, qRho21, qGen21,
                   Matrix.mul_apply, Fin.sum_univ_two];
                 try ring)
    calc strain21 q eBraid
        = (1 : R) • strain21 q eBraid := (one_smul _ _).symm
      _ = ((((q⁻¹ : Rˣ) : R)) ^ 6 * (q : R) ^ 6) • strain21 q eBraid := by rw [hqp6]
      _ = (((q⁻¹ : Rˣ) : R)) ^ 6 • (((q : R) ^ 6) • strain21 q eBraid) :=
            MulAction.mul_smul _ _ _
      _ = (((q⁻¹ : Rˣ) : R)) ^ 6 • (((q : R) ^ 6) • (1 : Matrix (Fin 2) (Fin 2) R)) := by
            rw [hscaled]
      _ = ((((q⁻¹ : Rˣ) : R)) ^ 6 * (q : R) ^ 6) • (1 : Matrix (Fin 2) (Fin 2) R) :=
            (MulAction.mul_smul _ _ _).symm
      _ = 1 := by rw [hqp6, one_smul]
  refine ⟨rfl, h1, ?_⟩
  rw [h1]
  simp [Matrix.trace]

end StrainRepresentation

/-! ## §2. Ordered-Ring Global Strain Minimum & Generic-Degree Muon Vanishing -/

section OrderedStrainAndGenericDegree

theorem trace_strain21_ge_two {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]
    (q : Rˣ) (hq : 0 < (q : R)) (w : Braid3Word) :
    (2 : R) ≤ (strain21 q w).trace := by
  have hqinv_mul : (q : R) * (((q⁻¹ : Rˣ) : R)) = 1 := Units.mul_inv q
  have hs_sub : 0 < (q : R) + (((q⁻¹ : Rˣ) : R)) - 1 := by
    have hprod : 0 < (q : R) * ((q : R) + (((q⁻¹ : Rˣ) : R)) - 1) := by
      have hid : (q : R) * ((q : R) + (((q⁻¹ : Rˣ) : R)) - 1) = ((q : R) - 1) ^ 2 + (q : R) := by
        calc (q : R) * ((q : R) + (((q⁻¹ : Rˣ) : R)) - 1)
            = (q : R) ^ 2 - (q : R) + (q : R) * (((q⁻¹ : Rˣ) : R)) := by ring
          _ = (q : R) ^ 2 - (q : R) + 1 := by rw [hqinv_mul]
          _ = ((q : R) - 1) ^ 2 + (q : R) := by ring
      rw [hid]; positivity
    by_contra hle; push_neg at hle
    have : (q : R) * ((q : R) + (((q⁻¹ : Rˣ) : R)) - 1) ≤ 0 :=
      mul_nonpos_of_nonneg_of_nonpos hq.le hle
    linarith
  have hs_add : 0 < (q : R) + (((q⁻¹ : Rˣ) : R)) + 1 := by linarith
  have hquad : ∀ c₀ c₁ : R,
      0 ≤ c₀ * ((wenzlMetric21 q * strain21 q w) 0 0 * c₀ +
                  (wenzlMetric21 q * strain21 q w) 0 1 * c₁) +
          c₁ * ((wenzlMetric21 q * strain21 q w) 1 0 * c₀ +
                  (wenzlMetric21 q * strain21 q w) 1 1 * c₁) := by
    intro c₀ c₁
    set y₀ := rho21 q w 0 0 * c₀ + rho21 q w 0 1 * c₁
    set y₁ := rho21 q w 1 0 * c₀ + rho21 q w 1 1 * c₁
    have hrew : 2 * (c₀ * ((wenzlMetric21 q * strain21 q w) 0 0 * c₀ +
                  (wenzlMetric21 q * strain21 q w) 0 1 * c₁) +
                c₁ * ((wenzlMetric21 q * strain21 q w) 1 0 * c₀ +
                  (wenzlMetric21 q * strain21 q w) 1 1 * c₁)) =
        ((q : R) + (((q⁻¹ : Rˣ) : R)) + 1) * (y₀ + y₁) ^ 2 +
          ((q : R) + (((q⁻¹ : Rˣ) : R)) - 1) * (y₀ - y₁) ^ 2 := by
      have hint : wenzlMetric21 q * strain21 q w =
          (rho21 q w)ᵀ * wenzlMetric21 q * rho21 q w := by
        unfold strain21
        have hw := wenzlMetric21_intertwines_word q w.reverse
        rw [List.reverse_reverse] at hw
        rw [← Matrix.mul_assoc, hw]
      rw [hint]
      simp only [wenzlMetric21, Matrix.mul_apply, Matrix.transpose_apply, Fin.sum_univ_two,
        Matrix.of_apply, Matrix.cons_val_zero, Matrix.cons_val_one, y₀, y₁]
      ring
    have h2pos : 0 ≤ ((q : R) + (((q⁻¹ : Rˣ) : R)) + 1) * (y₀ + y₁) ^ 2 +
        ((q : R) + (((q⁻¹ : Rˣ) : R)) - 1) * (y₀ - y₁) ^ 2 := by positivity
    linarith
  have h11 := hquad 1 1
  have h1m1 := hquad 1 (-1)
  simp only [wenzlMetric21, Matrix.mul_apply, Fin.sum_univ_two, Matrix.of_apply,
    Matrix.cons_val_zero, Matrix.cons_val_one] at h11 h1m1
  have hp : 0 ≤ ((q : R) + (((q⁻¹ : Rˣ) : R)) + 1) *
      (strain21 q w 0 0 + strain21 q w 1 1 + strain21 q w 0 1 + strain21 q w 1 0) := by
    linarith
  have hm : 0 ≤ ((q : R) + (((q⁻¹ : Rˣ) : R)) - 1) *
      (strain21 q w 0 0 + strain21 q w 1 1 - strain21 q w 0 1 - strain21 q w 1 0) := by
    linarith
  have hp' : 0 ≤ strain21 q w 0 0 + strain21 q w 1 1 + strain21 q w 0 1 + strain21 q w 1 0 := by
    by_contra hneg; push_neg at hneg
    have : ((q : R) + (((q⁻¹ : Rˣ) : R)) + 1) *
        (strain21 q w 0 0 + strain21 q w 1 1 + strain21 q w 0 1 + strain21 q w 1 0) < 0 :=
      mul_neg_of_pos_of_neg hs_add hneg
    linarith
  have hm' : 0 ≤ strain21 q w 0 0 + strain21 q w 1 1 - strain21 q w 0 1 - strain21 q w 1 0 := by
    by_contra hneg; push_neg at hneg
    have : ((q : R) + (((q⁻¹ : Rˣ) : R)) - 1) *
        (strain21 q w 0 0 + strain21 q w 1 1 - strain21 q w 0 1 - strain21 q w 1 0) < 0 :=
      mul_neg_of_pos_of_neg hs_sub hneg
    linarith
  have htr_nonneg : 0 ≤ (strain21 q w).trace := by
    have htr : (strain21 q w).trace = strain21 q w 0 0 + strain21 q w 1 1 := by
      simp [Matrix.trace, Fin.sum_univ_two]
    linarith
  have hsos := trace_strain21_sq_sub_four_eq_sos q w
  have hsos_nonneg : 0 ≤ ((strain21 q w).trace) ^ 2 - 4 := by
    rw [hsos]; positivity
  nlinarith

/-- One-row `(3)` character `σᵢ ↦ q` and one-column `(1,1,1)` character `σᵢ ↦ -q⁻¹` on `Braid3Word`. -/
def chi3Triv {R : Type*} [CommRing R] (q : Rˣ) : Braid3Word → R
  | [] => 1
  | g :: gs => (if g = 0 ∨ g = 1 then (q : R) else (((q⁻¹ : Rˣ) : R))) * chi3Triv q gs

def chi3Sign {R : Type*} [CommRing R] (q : Rˣ) : Braid3Word → R
  | [] => 1
  | g :: gs => (if g = 0 ∨ g = 1 then -(((q⁻¹ : Rˣ) : R)) else -(q : R)) * chi3Sign q gs

/-- Cleared-denominator generic-degree trace `[3]_q! · τ_{GenDeg}(w)` in `H_3(q)`. -/
def tauGenDegScaled {R : Type*} [CommRing R] (q : Rˣ) (w : Braid3Word) : R :=
  (q : R) ^ 3 * chi3Triv q w +
    ((q : R) + (((q⁻¹ : Rˣ) : R))) * (rho21 q w).trace +
    (((q⁻¹ : Rˣ) : R)) ^ 3 * chi3Sign q w

/-- **Exact Generic-Degree Vanishing on `μ = σ₀⁴σ₁⁻¹` (`[CommRing R]`):**
`[3]_q! · τ_{GenDeg}(μ) = 0` identically over every commutative ring `R` and unit `q : Rˣ`, while
`e` and `τ` both evaluate to `q⁶ - q⁻⁶`. -/
theorem tauGenDegScaled_lepton_identities {R : Type*} [CommRing R] (q : Rˣ) :
    tauGenDegScaled q muBraid = 0 ∧
      tauGenDegScaled q eBraid = (q : R) ^ 6 - (((q⁻¹ : Rˣ) : R)) ^ 6 ∧
      tauGenDegScaled q tauBraid = (q : R) ^ 6 - (((q⁻¹ : Rˣ) : R)) ^ 6 := by
  have hq : (q : R) * (((q⁻¹ : Rˣ) : R)) = 1 := Units.mul_inv q
  have hqp : ∀ k : ℕ, (q : R) ^ k * (((q⁻¹ : Rˣ) : R)) ^ k = 1 := by
    intro k; rw [← mul_pow, hq, one_pow]
  have hcancel : ∀ x y : R, (q : R) ^ 8 * x = (q : R) ^ 8 * y → x = y := by
    intro x y hxy
    have hinv8 : (((q⁻¹ : Rˣ) : R)) ^ 8 * (q : R) ^ 8 = 1 := by
      rw [← mul_pow, Units.inv_mul, one_pow]
    calc x = 1 * x := (one_mul x).symm
      _ = ((((q⁻¹ : Rˣ) : R)) ^ 8 * (q : R) ^ 8) * x := by rw [hinv8]
      _ = (((q⁻¹ : Rˣ) : R)) ^ 8 * ((q : R) ^ 8 * x) := mul_assoc _ _ _
      _ = (((q⁻¹ : Rˣ) : R)) ^ 8 * ((q : R) ^ 8 * y) := by rw [hxy]
      _ = ((((q⁻¹ : Rˣ) : R)) ^ 8 * (q : R) ^ 8) * y := (mul_assoc _ _ _).symm
      _ = y := by rw [hinv8, one_mul]
  have h30 : ¬ ((3 : Braid3Letter) = 0 ∨ (3 : Braid3Letter) = 1) := by decide
  have htr_e : (q : R) ^ 3 * (rho21 q eBraid).trace = 0 := by
    have hlen : eBraid.length = 3 := rfl
    rw [← hlen, pow_len_trace_rho21]
    simp only [eBraid, qRho21, Matrix.mul_one, qGen21, Matrix.trace, Matrix.diag_apply,
      Matrix.mul_apply, Fin.sum_univ_two, Matrix.of_apply, Matrix.cons_val_zero,
      Matrix.cons_val_one]
    ring
  have htr_mu : (q : R) ^ 5 * (rho21 q muBraid).trace = -((q : R) ^ 10 - (q : R) ^ 8 +
      (q : R) ^ 6 - (q : R) ^ 4 + (q : R) ^ 2 - 1) := by
    have hlen : muBraid.length = 5 := rfl
    rw [← hlen, pow_len_trace_rho21]
    simp only [muBraid, qRho21, Matrix.mul_one, qGen21, Matrix.trace, Matrix.diag_apply,
      Matrix.mul_apply, Fin.sum_univ_two, Matrix.of_apply, Matrix.cons_val_zero,
      Matrix.cons_val_one]
    ring
  have htr_tau : (q : R) ^ 5 * (rho21 q tauBraid).trace =
      (q : R) ^ 10 - 2 * (q : R) ^ 8 + 2 * (q : R) ^ 6 - 2 * (q : R) ^ 4 + 2 * (q : R) ^ 2 - 1 := by
    have hlen : tauBraid.length = 5 := rfl
    rw [← hlen, pow_len_trace_rho21]
    simp only [tauBraid, qRho21, Matrix.mul_one, qGen21, Matrix.trace, Matrix.diag_apply,
      Matrix.mul_apply, Fin.sum_univ_two, Matrix.of_apply, Matrix.cons_val_zero,
      Matrix.cons_val_one]
    ring
  refine ⟨hcancel _ _ ?_, hcancel _ _ ?_, hcancel _ _ ?_⟩
  · unfold tauGenDegScaled
    have hc1 : (q : R) ^ 8 * ((q : R) ^ 3 * chi3Triv q muBraid) = (q : R) ^ 14 := by
      simp only [muBraid, chi3Triv, true_or, h30, ite_true, ite_false, mul_one]
      calc (q : R) ^ 8 * ((q : R) ^ 3 * ((q : R) * ((q : R) * ((q : R) * ((q : R) * (((q⁻¹ : Rˣ) : R)))))))
          = (q : R) ^ 14 * ((q : R) * (((q⁻¹ : Rˣ) : R))) := by ring
        _ = (q : R) ^ 14 := by rw [hq, mul_one]
    have hc2 : (q : R) ^ 8 * (((q : R) + (((q⁻¹ : Rˣ) : R))) * (rho21 q muBraid).trace) =
        ((q : R) ^ 4 + (q : R) ^ 2 * ((q : R) * (((q⁻¹ : Rˣ) : R)))) *
          ((q : R) ^ 5 * (rho21 q muBraid).trace) := by ring
    have hc3 : (q : R) ^ 8 * ((((q⁻¹ : Rˣ) : R)) ^ 3 * chi3Sign q muBraid) = -(q : R) ^ 2 := by
      simp only [muBraid, chi3Sign, true_or, h30, ite_true, ite_false, mul_one]
      calc (q : R) ^ 8 * ((((q⁻¹ : Rˣ) : R)) ^ 3 *
            (-(((q⁻¹ : Rˣ) : R)) * (-(((q⁻¹ : Rˣ) : R)) * (-(((q⁻¹ : Rˣ) : R)) * (-(((q⁻¹ : Rˣ) : R)) * -(q : R))))))
          = -(q : R) ^ 2 * ((q : R) ^ 7 * (((q⁻¹ : Rˣ) : R)) ^ 7) := by ring
        _ = -(q : R) ^ 2 := by rw [hqp 7, mul_one]
    rw [mul_add, mul_add, hc1, hc2, hq, htr_mu, hc3]
    ring
  · unfold tauGenDegScaled
    have hc1 : (q : R) ^ 8 * ((q : R) ^ 3 * chi3Triv q eBraid) = (q : R) ^ 14 := by
      simp only [eBraid, chi3Triv, true_or, or_true, ite_true, mul_one]; ring
    have hc2 : (q : R) ^ 8 * (((q : R) + (((q⁻¹ : Rˣ) : R))) * (rho21 q eBraid).trace) =
        ((q : R) ^ 6 + (q : R) ^ 4 * ((q : R) * (((q⁻¹ : Rˣ) : R)))) *
          ((q : R) ^ 3 * (rho21 q eBraid).trace) := by ring
    have hc3 : (q : R) ^ 8 * ((((q⁻¹ : Rˣ) : R)) ^ 3 * chi3Sign q eBraid) = -(q : R) ^ 2 := by
      simp only [eBraid, chi3Sign, true_or, or_true, ite_true, mul_one]
      calc (q : R) ^ 8 * ((((q⁻¹ : Rˣ) : R)) ^ 3 *
            (-(((q⁻¹ : Rˣ) : R)) * (-(((q⁻¹ : Rˣ) : R)) * -(((q⁻¹ : Rˣ) : R)))))
          = -(q : R) ^ 2 * ((q : R) ^ 6 * (((q⁻¹ : Rˣ) : R)) ^ 6) := by ring
        _ = -(q : R) ^ 2 := by rw [hqp 6, mul_one]
    have hrhs : (q : R) ^ 8 * ((q : R) ^ 6 - (((q⁻¹ : Rˣ) : R)) ^ 6) =
        (q : R) ^ 14 - (q : R) ^ 2 * ((q : R) ^ 6 * (((q⁻¹ : Rˣ) : R)) ^ 6) := by ring
    rw [mul_add, mul_add, hc1, hc2, htr_e, hc3, hrhs, hqp 6]
    ring
  · unfold tauGenDegScaled
    have hc1 : (q : R) ^ 8 * ((q : R) ^ 3 * chi3Triv q tauBraid) = (q : R) ^ 12 := by
      simp only [tauBraid, chi3Triv, true_or, h30, ite_true, ite_false, mul_one]
      calc (q : R) ^ 8 * ((q : R) ^ 3 * ((q : R) * ((q : R) * ((((q⁻¹ : Rˣ) : R)) * ((q : R) * (((q⁻¹ : Rˣ) : R)))))))
          = (q : R) ^ 12 * ((q : R) ^ 2 * (((q⁻¹ : Rˣ) : R)) ^ 2) := by ring
        _ = (q : R) ^ 12 := by rw [hqp 2, mul_one]
    have hc2 : (q : R) ^ 8 * (((q : R) + (((q⁻¹ : Rˣ) : R))) * (rho21 q tauBraid).trace) =
        ((q : R) ^ 4 + (q : R) ^ 2 * ((q : R) * (((q⁻¹ : Rˣ) : R)))) *
          ((q : R) ^ 5 * (rho21 q tauBraid).trace) := by ring
    have hc3 : (q : R) ^ 8 * ((((q⁻¹ : Rˣ) : R)) ^ 3 * chi3Sign q tauBraid) = -(q : R) ^ 4 := by
      simp only [tauBraid, chi3Sign, true_or, h30, ite_true, ite_false, mul_one]
      calc (q : R) ^ 8 * ((((q⁻¹ : Rˣ) : R)) ^ 3 *
            (-(((q⁻¹ : Rˣ) : R)) * (-(((q⁻¹ : Rˣ) : R)) * (-(q : R) * (-(((q⁻¹ : Rˣ) : R)) * -(q : R))))))
          = -(q : R) ^ 4 * ((q : R) ^ 6 * (((q⁻¹ : Rˣ) : R)) ^ 6) := by ring
        _ = -(q : R) ^ 4 := by rw [hqp 6, mul_one]
    have hrhs : (q : R) ^ 8 * ((q : R) ^ 6 - (((q⁻¹ : Rˣ) : R)) ^ 6) =
        (q : R) ^ 14 - (q : R) ^ 2 * ((q : R) ^ 6 * (((q⁻¹ : Rˣ) : R)) ^ 6) := by ring
    rw [mul_add, mul_add, hc1, hc2, hq, htr_tau, hc3, hrhs, hqp 6]
    ring

end OrderedStrainAndGenericDegree

/-! ## §3. Strict Real-`q` Ordering of Framed GNS Norms & Top-JM Traces on `(e, μ, τ)` -/

section RealQLeptonOrdering

/-- Scaled zero-writhe framed Convention-D GNS norm `(q² + 1)² ‖W̃‖_D²` for positive-writhe `w`. -/
def framedGNSScaled {R : Type*} [CommRing R] (q : Rˣ) (wrNat : ℕ) (w : Braid3Word) : R :=
  ((q : R) ^ 4 + 1) +
    (((q⁻¹ : Rˣ) : R)) ^ (2 * wrNat) * (q : R) ^ 2 * (strain21 q w).trace

/-- Scaled full-twist / top-JM trace `(q² + 1)² τ_D(Δ₃² W)` for positive-writhe `w`. -/
def fullTwistTraceScaled {R : Type*} [CommRing R] (q : Rˣ) (wrNat : ℕ) (w : Braid3Word) : R :=
  ((q : R) ^ 4 + 1) * (q : R) ^ (6 + wrNat) +
    (q : R) ^ 2 * (rho21 q w).trace

/-- **Strict `‖ẽ‖_D² < ‖μ̃‖_D² < ‖τ̃‖_D²` over any strict ordered commutative ring on `q ∈ (1, 6/5]`:**
proved division-free via the exact homogeneous Bernstein decomposition on `2 q² ∈ (2, 3)`. -/
theorem framedGNSScaled_strict_e_lt_mu_lt_tau
    {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]
    (q : Rˣ) (hq1 : 1 < (q : R)) (hq65 : 5 * (q : R) ≤ 6) :
    framedGNSScaled q 3 eBraid < framedGNSScaled q 3 muBraid ∧
      framedGNSScaled q 3 muBraid < framedGNSScaled q 1 tauBraid := by
  have hq : (q : R) * (((q⁻¹ : Rˣ) : R)) = 1 := Units.mul_inv q
  have hqpos : 0 < (q : R) := by linarith
  have hqp6 : (q : R) ^ 6 * (((q⁻¹ : Rˣ) : R)) ^ 6 = 1 := by
    rw [← mul_pow, hq, one_pow]
  have hqp2 : (q : R) ^ 2 * (((q⁻¹ : Rˣ) : R)) ^ 2 = 1 := by
    rw [← mul_pow, hq, one_pow]
  have htr_mu : (q : R) ^ 10 * (strain21 q muBraid).trace =
      ((q : R) ^ 4 + 1) * ((q : R) ^ 4 - (q : R) ^ 2 + 1) *
        ((q : R) ^ 12 - (q : R) ^ 6 + 1) := by
    have hlen : 2 * muBraid.length = 10 := rfl
    rw [← hlen, pow_two_len_trace_strain21]
    simp only [muBraid, List.reverse_cons, List.reverse_nil, List.nil_append, List.cons_append,
      qRho21, Matrix.mul_one, qGen21, Matrix.trace, Matrix.diag_apply, Matrix.mul_apply,
      Fin.sum_univ_two, Matrix.of_apply, Matrix.cons_val_zero, Matrix.cons_val_one]
    ring
  have htr_tau : (q : R) ^ 10 * (strain21 q tauBraid).trace =
      (q : R) ^ 20 - 3 * (q : R) ^ 18 + 5 * (q : R) ^ 16 - 7 * (q : R) ^ 14 +
        10 * (q : R) ^ 12 - 10 * (q : R) ^ 10 + 10 * (q : R) ^ 8 -
        7 * (q : R) ^ 6 + 5 * (q : R) ^ 4 - 3 * (q : R) ^ 2 + 1 := by
    rw [show (q : R) ^ 10 * (strain21 q tauBraid).trace =
          (q : R) ^ (2 * tauBraid.length) * (strain21 q tauBraid).trace from rfl,
        pow_two_len_trace_strain21]
    simp only [tauBraid, List.reverse_cons, List.reverse_nil, List.nil_append, List.cons_append,
      qRho21, Matrix.mul_one, qGen21, Matrix.trace, Matrix.diag_apply, Matrix.mul_apply,
      Fin.sum_univ_two, Matrix.of_apply, Matrix.cons_val_zero, Matrix.cons_val_one]
    ring
  constructor
  · have hdiff : (q : R) ^ 14 *
        (framedGNSScaled q 3 muBraid - framedGNSScaled q 3 eBraid) =
        ((q : R) - 1) ^ 2 * ((q : R) + 1) ^ 2 *
          ((q : R) ^ 2 - (q : R) + 1) * ((q : R) ^ 2 + (q : R) + 1) *
          ((q : R) ^ 12 + 2 * (q : R) ^ 8 + (q : R) ^ 6 + 2 * (q : R) ^ 4 + 1) := by
      unfold framedGNSScaled
      rw [(strain21_eBraid_eq_one_and_trace_two q).2.2]
      calc (q : R) ^ 14 * ((((q : R) ^ 4 + 1) + (((q⁻¹ : Rˣ) : R)) ^ (2 * 3) * (q : R) ^ 2 *
              (strain21 q muBraid).trace) -
            (((q : R) ^ 4 + 1) + (((q⁻¹ : Rˣ) : R)) ^ (2 * 3) * (q : R) ^ 2 * 2))
          = ((q : R) ^ 6 * (((q⁻¹ : Rˣ) : R)) ^ 6) *
              ((q : R) ^ 10 * (strain21 q muBraid).trace - 2 * (q : R) ^ 10) := by ring
        _ = 1 * (((q : R) ^ 4 + 1) * ((q : R) ^ 4 - (q : R) ^ 2 + 1) *
              ((q : R) ^ 12 - (q : R) ^ 6 + 1) - 2 * (q : R) ^ 10) := by rw [hqp6, htr_mu]
        _ = ((q : R) - 1) ^ 2 * ((q : R) + 1) ^ 2 *
              ((q : R) ^ 2 - (q : R) + 1) * ((q : R) ^ 2 + (q : R) + 1) *
              ((q : R) ^ 12 + 2 * (q : R) ^ 8 + (q : R) ^ 6 + 2 * (q : R) ^ 4 + 1) := by ring
    have hsub1 : 0 < (q : R) - 1 := by linarith
    have hquad_pos : 0 < (q : R) ^ 2 - (q : R) + 1 := by nlinarith
    have hquad_add : 0 < (q : R) ^ 2 + (q : R) + 1 := by positivity
    have hpoly12 : 0 < (q : R) ^ 12 + 2 * (q : R) ^ 8 + (q : R) ^ 6 + 2 * (q : R) ^ 4 + 1 := by
      positivity
    have hprod_pos : 0 < (q : R) ^ 14 *
        (framedGNSScaled q 3 muBraid - framedGNSScaled q 3 eBraid) := by
      rw [hdiff]
      positivity
    have hq14 : 0 < (q : R) ^ 14 := by positivity
    by_contra hle; push_neg at hle
    have : (q : R) ^ 14 * (framedGNSScaled q 3 muBraid - framedGNSScaled q 3 eBraid) ≤ 0 :=
      mul_nonpos_of_nonneg_of_nonpos hq14.le (by linarith)
    linarith
  · set A : R := 2 * ((q : R) ^ 2 - 1)
    set B : R := 3 - 2 * (q : R) ^ 2
    have hA : 0 < A := by
      change 0 < 2 * ((q : R) ^ 2 - 1)
      nlinarith
    have hB : 0 < B := by
      change 0 < 3 - 2 * (q : R) ^ 2
      have hsq : 25 * (q : R) ^ 2 ≤ 36 := by nlinarith
      linarith
    have hdiff : (2 : R) ^ 11 * (q : R) ^ 14 *
        (framedGNSScaled q 1 tauBraid - framedGNSScaled q 3 muBraid) =
        ((q : R) ^ 2 - 1) *
          (7439 * A ^ 11 + 60370 * A ^ 10 * B + 311212 * A ^ 9 * B ^ 2 +
            1090120 * A ^ 8 * B ^ 3 + 2526624 * A ^ 7 * B ^ 4 +
            3928768 * A ^ 6 * B ^ 5 + 4179456 * A ^ 5 * B ^ 6 +
            3063424 * A ^ 4 * B ^ 7 + 1527552 * A ^ 3 * B ^ 8 +
            496640 * A ^ 2 * B ^ 9 + 95232 * A * B ^ 10 + 8192 * B ^ 11) := by
      unfold framedGNSScaled
      calc (2 : R) ^ 11 * (q : R) ^ 14 *
            ((((q : R) ^ 4 + 1) + (((q⁻¹ : Rˣ) : R)) ^ (2 * 1) * (q : R) ^ 2 *
                (strain21 q tauBraid).trace) -
              (((q : R) ^ 4 + 1) + (((q⁻¹ : Rˣ) : R)) ^ (2 * 3) * (q : R) ^ 2 *
                (strain21 q muBraid).trace))
          = (2 : R) ^ 11 * (((q : R) ^ 2 * (((q⁻¹ : Rˣ) : R)) ^ 2) * (q : R) ^ 4 *
                ((q : R) ^ 10 * (strain21 q tauBraid).trace) -
              ((q : R) ^ 6 * (((q⁻¹ : Rˣ) : R)) ^ 6) *
                ((q : R) ^ 10 * (strain21 q muBraid).trace)) := by ring
        _ = (2 : R) ^ 11 * (1 * (q : R) ^ 4 *
                ((q : R) ^ 20 - 3 * (q : R) ^ 18 + 5 * (q : R) ^ 16 - 7 * (q : R) ^ 14 +
                  10 * (q : R) ^ 12 - 10 * (q : R) ^ 10 + 10 * (q : R) ^ 8 -
                  7 * (q : R) ^ 6 + 5 * (q : R) ^ 4 - 3 * (q : R) ^ 2 + 1) -
              1 * (((q : R) ^ 4 + 1) * ((q : R) ^ 4 - (q : R) ^ 2 + 1) *
                ((q : R) ^ 12 - (q : R) ^ 6 + 1))) := by rw [hqp2, hqp6, htr_tau, htr_mu]
        _ = ((q : R) ^ 2 - 1) *
              (7439 * A ^ 11 + 60370 * A ^ 10 * B + 311212 * A ^ 9 * B ^ 2 +
                1090120 * A ^ 8 * B ^ 3 + 2526624 * A ^ 7 * B ^ 4 +
                3928768 * A ^ 6 * B ^ 5 + 4179456 * A ^ 5 * B ^ 6 +
                3063424 * A ^ 4 * B ^ 7 + 1527552 * A ^ 3 * B ^ 8 +
                496640 * A ^ 2 * B ^ 9 + 95232 * A * B ^ 10 + 8192 * B ^ 11) := by
              simp only [A, B]; ring
    have hq2_sub : 0 < (q : R) ^ 2 - 1 := by nlinarith
    have hprod_pos : 0 < (2 : R) ^ 11 * (q : R) ^ 14 *
        (framedGNSScaled q 1 tauBraid - framedGNSScaled q 3 muBraid) := by
      rw [hdiff]; positivity
    have hpref : 0 < (2 : R) ^ 11 * (q : R) ^ 14 := by positivity
    by_contra hle; push_neg at hle
    have : (2 : R) ^ 11 * (q : R) ^ 14 *
        (framedGNSScaled q 1 tauBraid - framedGNSScaled q 3 muBraid) ≤ 0 :=
      mul_nonpos_of_nonneg_of_nonpos hpref.le (by linarith)
    linarith

/-- **Strict `τ_D(Δ₃² τ) < τ_D(Δ₃² μ) < τ_D(Δ₃² e)` over any strict ordered commutative ring for
`11 ≤ 10 * q` (`q ≥ 11/10`, covering `q₀^{(p)} ≈ 1.1100`).** -/
theorem fullTwistTraceScaled_strict_tau_lt_mu_lt_e
    {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]
    (q : Rˣ) (hq11 : 11 ≤ 10 * (q : R)) :
    fullTwistTraceScaled q 1 tauBraid < fullTwistTraceScaled q 3 muBraid ∧
      fullTwistTraceScaled q 3 muBraid < fullTwistTraceScaled q 3 eBraid := by
  have hqpos : 0 < (q : R) := by linarith
  have hq1 : 1 < (q : R) := by linarith
  have hchi_e : (q : R) ^ 3 * (rho21 q eBraid).trace = 0 := by
    have hlen : eBraid.length = 3 := rfl
    rw [← hlen, pow_len_trace_rho21]
    simp only [eBraid, qRho21, Matrix.mul_one, qGen21, Matrix.trace, Matrix.diag_apply,
      Matrix.mul_apply, Fin.sum_univ_two, Matrix.of_apply, Matrix.cons_val_zero,
      Matrix.cons_val_one]
    ring
  have hchi_mu : (q : R) ^ 5 * (rho21 q muBraid).trace =
      -((q : R) - 1) * ((q : R) + 1) * ((q : R) ^ 2 - (q : R) + 1) *
        ((q : R) ^ 2 + (q : R) + 1) * ((q : R) ^ 4 - (q : R) ^ 2 + 1) := by
    have hlen : muBraid.length = 5 := rfl
    rw [← hlen, pow_len_trace_rho21]
    simp only [muBraid, qRho21, Matrix.mul_one, qGen21, Matrix.trace, Matrix.diag_apply,
      Matrix.mul_apply, Fin.sum_univ_two, Matrix.of_apply, Matrix.cons_val_zero,
      Matrix.cons_val_one]
    ring
  have hchi_tau : (q : R) ^ 5 * (rho21 q tauBraid).trace =
      ((q : R) - 1) * ((q : R) + 1) *
        ((q : R) ^ 8 - (q : R) ^ 6 + (q : R) ^ 4 - (q : R) ^ 2 + 1) := by
    have hlen : tauBraid.length = 5 := rfl
    rw [← hlen, pow_len_trace_rho21]
    simp only [tauBraid, qRho21, Matrix.mul_one, qGen21, Matrix.trace, Matrix.diag_apply,
      Matrix.mul_apply, Fin.sum_univ_two, Matrix.of_apply, Matrix.cons_val_zero,
      Matrix.cons_val_one]
    ring
  constructor
  · set U : R := 10 * (q : R) - 11
    have hU : 0 ≤ U := by change 0 ≤ 10 * (q : R) - 11; linarith
    have hdiff : (10 : R) ^ 14 * (q : R) ^ 3 *
        (fullTwistTraceScaled q 3 muBraid - fullTwistTraceScaled q 1 tauBraid) =
        ((q : R) ^ 2 - 1) *
          (U ^ 14 + 154 * U ^ 13 + 11011 * U ^ 12 + 484484 * U ^ 11 +
            14665641 * U ^ 10 + 323524102 * U ^ 9 + 5372447683 * U ^ 8 +
            68301170872 * U ^ 7 + 667789819643 * U ^ 6 + 4983987797382 * U ^ 5 +
            27795400125601 * U ^ 4 + 110982341302404 * U ^ 3 +
            291292562731611 * U ^ 2 + 419468603115034 * U + 15742417593241) := by
      unfold fullTwistTraceScaled
      calc (10 : R) ^ 14 * (q : R) ^ 3 *
            ((((q : R) ^ 4 + 1) * (q : R) ^ (6 + 3) + (q : R) ^ 2 * (rho21 q muBraid).trace) -
              (((q : R) ^ 4 + 1) * (q : R) ^ (6 + 1) + (q : R) ^ 2 * (rho21 q tauBraid).trace))
          = (10 : R) ^ 14 * (((q : R) ^ 4 + 1) * ((q : R) ^ 12 - (q : R) ^ 10) +
              (q : R) ^ 5 * (rho21 q muBraid).trace -
              (q : R) ^ 5 * (rho21 q tauBraid).trace) := by ring
        _ = (10 : R) ^ 14 * (((q : R) ^ 4 + 1) * ((q : R) ^ 12 - (q : R) ^ 10) +
              (-((q : R) - 1) * ((q : R) + 1) * ((q : R) ^ 2 - (q : R) + 1) *
                ((q : R) ^ 2 + (q : R) + 1) * ((q : R) ^ 4 - (q : R) ^ 2 + 1)) -
              ((q : R) - 1) * ((q : R) + 1) *
                ((q : R) ^ 8 - (q : R) ^ 6 + (q : R) ^ 4 - (q : R) ^ 2 + 1)) := by
              rw [hchi_mu, hchi_tau]
        _ = ((q : R) ^ 2 - 1) *
              (U ^ 14 + 154 * U ^ 13 + 11011 * U ^ 12 + 484484 * U ^ 11 +
                14665641 * U ^ 10 + 323524102 * U ^ 9 + 5372447683 * U ^ 8 +
                68301170872 * U ^ 7 + 667789819643 * U ^ 6 + 4983987797382 * U ^ 5 +
                27795400125601 * U ^ 4 + 110982341302404 * U ^ 3 +
                291292562731611 * U ^ 2 + 419468603115034 * U + 15742417593241) := by
              simp only [U]; ring
    have hq2_sub : 0 < (q : R) ^ 2 - 1 := by nlinarith
    have hprod_pos : 0 < (10 : R) ^ 14 * (q : R) ^ 3 *
        (fullTwistTraceScaled q 3 muBraid - fullTwistTraceScaled q 1 tauBraid) := by
      rw [hdiff]; positivity
    have hpref : 0 < (10 : R) ^ 14 * (q : R) ^ 3 := by positivity
    by_contra hle; push_neg at hle
    have : (10 : R) ^ 14 * (q : R) ^ 3 *
        (fullTwistTraceScaled q 3 muBraid - fullTwistTraceScaled q 1 tauBraid) ≤ 0 :=
      mul_nonpos_of_nonneg_of_nonpos hpref.le (by linarith)
    linarith
  · have hdiff : (q : R) ^ 3 *
        (fullTwistTraceScaled q 3 eBraid - fullTwistTraceScaled q 3 muBraid) =
        ((q : R) - 1) * ((q : R) + 1) * ((q : R) ^ 2 - (q : R) + 1) *
          ((q : R) ^ 2 + (q : R) + 1) * ((q : R) ^ 4 - (q : R) ^ 2 + 1) := by
      unfold fullTwistTraceScaled
      calc (q : R) ^ 3 * ((((q : R) ^ 4 + 1) * (q : R) ^ (6 + 3) +
                (q : R) ^ 2 * (rho21 q eBraid).trace) -
              (((q : R) ^ 4 + 1) * (q : R) ^ (6 + 3) +
                (q : R) ^ 2 * (rho21 q muBraid).trace))
          = (q : R) ^ 2 * ((q : R) ^ 3 * (rho21 q eBraid).trace) -
              (q : R) ^ 5 * (rho21 q muBraid).trace := by ring
        _ = (q : R) ^ 2 * 0 -
              (-((q : R) - 1) * ((q : R) + 1) * ((q : R) ^ 2 - (q : R) + 1) *
                ((q : R) ^ 2 + (q : R) + 1) * ((q : R) ^ 4 - (q : R) ^ 2 + 1)) := by
              rw [hchi_e, hchi_mu]
        _ = ((q : R) - 1) * ((q : R) + 1) * ((q : R) ^ 2 - (q : R) + 1) *
              ((q : R) ^ 2 + (q : R) + 1) * ((q : R) ^ 4 - (q : R) ^ 2 + 1) := by ring
    have hsub1 : 0 < (q : R) - 1 := by linarith
    have hquad : 0 < (q : R) ^ 2 - (q : R) + 1 := by nlinarith
    have hquart : 0 < (q : R) ^ 4 - (q : R) ^ 2 + 1 := by
      have hid : (q : R) ^ 4 - (q : R) ^ 2 + 1 = ((q : R) ^ 2 - 1) ^ 2 + (q : R) ^ 2 := by ring
      rw [hid]; positivity
    have hprod_pos : 0 < (q : R) ^ 3 *
        (fullTwistTraceScaled q 3 eBraid - fullTwistTraceScaled q 3 muBraid) := by
      rw [hdiff]; positivity
    have hq3 : 0 < (q : R) ^ 3 := by positivity
    by_contra hle; push_neg at hle
    have : (q : R) ^ 3 *
        (fullTwistTraceScaled q 3 eBraid - fullTwistTraceScaled q 3 muBraid) ≤ 0 :=
      mul_nonpos_of_nonneg_of_nonpos hq3.le (by linarith)
    linarith

end RealQLeptonOrdering

/-! ## §4. `O_q(SU(2))` Spinor 3-Quark GNS Isospin Dichotomy & Peter–Weyl Right-Norm Sign -/

section OqSU2SpinorIsospin

/-- Asymmetric `q²`-integer `[n]_{q²} = ∑_{k=0}^{n−1} q^{2k}` for `n = 2, 3, 4`. -/
def q2Int2 {R : Type*} [CommRing R] (q : R) : R := 1 + q ^ 2
def q2Int3 {R : Type*} [CommRing R] (q : R) : R := 1 + q ^ 2 + q ^ 4
def q2Int4 {R : Type*} [CommRing R] (q : R) : R := 1 + q ^ 2 + q ^ 4 + q ^ 6

def haarSpinorLeftClearedUUD {R : Type*} [CommRing R] (q : R) : R :=
  q ^ 2 * q2Int3 q * q2Int4 q - (q ^ 2 + 1) * q2Int2 q * q2Int4 q + q2Int2 q * q2Int3 q

def haarSpinorLeftClearedUDD {R : Type*} [CommRing R] (q : R) : R :=
  q ^ 2 * (q2Int2 q * q2Int4 q - q2Int2 q * q2Int3 q)

def haarSpinorRightClearedUUD {R : Type*} [CommRing R] (q : R) : R :=
  q ^ 4 * (q2Int3 q * q2Int4 q - (q ^ 2 + q ^ 4) * q2Int2 q * q2Int4 q +
    q ^ 6 * q2Int2 q * q2Int3 q)

def haarSpinorRightClearedUDD {R : Type*} [CommRing R] (q : R) : R :=
  q ^ 4 * (q2Int2 q * q2Int4 q - q ^ 2 * q2Int2 q * q2Int3 q)

/-- **Exact `O_q(SU(2))` 3-Quark Spinor GNS Isospin Dichotomy (`[CommRing R]`):**
1. Left-GNS norms satisfy `h(W_p* W_p) = q² h(W_n* W_n)`.
2. Right-GNS norms satisfy **exact `1 : 1` isospin symmetry** `h(W_p W_p*) = h(W_n W_n*)`. -/
theorem haarSpinor_left_kms_and_right_symmetric {R : Type*} [CommRing R] (q : R) :
    haarSpinorLeftClearedUUD q = q ^ 10 * q2Int2 q ∧
      haarSpinorLeftClearedUDD q = q ^ 8 * q2Int2 q ∧
      haarSpinorLeftClearedUUD q = q ^ 2 * haarSpinorLeftClearedUDD q ∧
      haarSpinorRightClearedUUD q = q ^ 4 * q2Int2 q ∧
      haarSpinorRightClearedUDD q = q ^ 4 * q2Int2 q ∧
      haarSpinorRightClearedUUD q = haarSpinorRightClearedUDD q := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩ <;>
    (simp only [haarSpinorLeftClearedUUD, haarSpinorLeftClearedUDD,
       haarSpinorRightClearedUUD, haarSpinorRightClearedUDD, q2Int2, q2Int3, q2Int4];
     ring)

/-- **`j = 1/2` Peter–Weyl Right-GNS Linear Sign (`m_n > m_p` for `q > 1`).** -/
theorem peterWeyl_spinHalf_rightNorm_diff_pos
    {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]
    (q : R) (hq1 : 1 < q) :
    0 < q ^ 2 - 1 := by
  nlinarith

end OqSU2SpinorIsospin

end QOU.StandardModel.LeptonFramedGNSAndStrainOrder
