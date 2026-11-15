import Mathlib.Analysis.ODE.Gronwall
import Mathlib.Analysis.SpecialFunctions.ExpDeriv
import Mathlib.Analysis.Complex.RealDeriv
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic.Module
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Topology.Algebra.Module.FiniteDimension

/-!
# Drinfeld–Kohno for two strands, proved

The Knizhnik–Zamolodchikov (KZ) connection for `𝔰𝔩₂` on two points with
fundamental fibres `V = ℂ²` is `dF = λ Ω dlog(z₁ − z₂) F` on `V ⊗ V`, where `Ω`
is the split Casimir `e ⊗ f + f ⊗ e + ½ h ⊗ h`. In the relative coordinate
`w = z₁ − z₂`, along the half-turn `w(t) = w₀ e^{iπt}` that exchanges the two
points, `w'(t)/w(t) = iπ` (`halfTurn_logDeriv`), so the KZ equation becomes the
constant-coefficient system `F' = (iπλ) Ω F` on `t ∈ [0, 1]`.

This file solves that system, proves the solution unique, and identifies the
exchange operator (transport followed by the flip of the two factors) with the
Jimbo R-matrix: it is `e^{-iπλ/2}` times a conjugate of `Ř(q)`, `q = e^{iπλ}`,
by a conjugator that preserves total weight. So the weighted trace
`Tr((K ⊗ K) ·)` of every two-strand braid is the same on both sides, up to the
writhe scalar. This holds for every complex `λ` with `q² + 1 ≠ 0`, in
particular at the purely imaginary coupling that gives a real `q > 1`.

Scope: two strands only. The `n`-strand theorem (Kohno 1987, Thm 1.2.8 and
Remark 1.3.14) is cited elsewhere, not proved here.

Basis order of `V ⊗ V`: `0 = ↑↑, 1 = ↑↓, 2 = ↓↑, 3 = ↓↓`.
-/

open Matrix Set

namespace QOU.Mass.KohnoTwoPoint

/-! ## Algebraic part, over any field -/

section Algebra

variable {R : Type*} [Field R] [CharZero R]

/-- The split Casimir `Ω = e⊗f + f⊗e + ½ h⊗h` on `V ⊗ V`. -/
def casimir : Matrix (Fin 4) (Fin 4) R :=
  !![1/2, 0, 0, 0;
     0, -1/2, 1, 0;
     0, 1, -1/2, 0;
     0, 0, 0, 1/2]

/-- The projector onto the antisymmetric (singlet) line. -/
def antiProj : Matrix (Fin 4) (Fin 4) R :=
  !![0, 0, 0, 0;
     0, 1/2, -1/2, 0;
     0, -1/2, 1/2, 0;
     0, 0, 0, 0]

/-- The flip `x ⊗ y ↦ y ⊗ x`. -/
def flip : Matrix (Fin 4) (Fin 4) R :=
  !![1, 0, 0, 0;
     0, 0, 1, 0;
     0, 1, 0, 0;
     0, 0, 0, 1]

/-- The Jimbo R-matrix `Ř(q)` of `U_q(𝔰𝔩₂)` on `V ⊗ V`
(eigenvalue `q` on the triplet, `-q⁻¹` on the singlet). -/
def rCheck (q : R) : Matrix (Fin 4) (Fin 4) R :=
  !![q, 0, 0, 0;
     0, 0, 1, 0;
     0, 1, q - q⁻¹, 0;
     0, 0, 0, q]

/-- The weight operator `K ⊗ K`, `K = diag(1, q²)`. -/
def weightKK (q : R) : Matrix (Fin 4) (Fin 4) R :=
  Matrix.diagonal ![1, q ^ 2, q ^ 2, q ^ 4]

/-- The weight-preserving conjugator: identity on `↑↑` and `↓↓`, and on the
weight-zero block it sends the classical eigenvectors `↑↓ ± ↓↑` to the
`q`-eigenvectors of `Ř`. -/
def conj (q : R) : Matrix (Fin 4) (Fin 4) R :=
  !![1, 0, 0, 0;
     0, 1, 0, 0;
     0, (q - q⁻¹)/2, (q + q⁻¹)/2, 0;
     0, 0, 0, 1]

/-- Its inverse, when `q + q⁻¹ ≠ 0`. -/
def conjInv (q : R) : Matrix (Fin 4) (Fin 4) R :=
  !![1, 0, 0, 0;
     0, 1, 0, 0;
     0, -(q - q⁻¹)/(q + q⁻¹), 2/(q + q⁻¹), 0;
     0, 0, 0, 1]

lemma antiProj_mul_self : (antiProj : Matrix (Fin 4) (Fin 4) R) * antiProj = antiProj := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [antiProj, Matrix.mul_apply, Fin.sum_univ_four] <;> norm_num

lemma casimir_eq : (casimir : Matrix (Fin 4) (Fin 4) R) = (1/2 : R) • 1 - (2 : R) • antiProj := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [casimir, antiProj] <;> norm_num

lemma flip_eq : (flip : Matrix (Fin 4) (Fin 4) R) = 1 - (2 : R) • antiProj := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [flip, antiProj] <;> norm_num

/-- On `ℂ² ⊗ ℂ²` the split Casimir is the flip minus one half. This is why the
`n`-point KZ residues are `s_{ij} − ½` in the symmetric-group algebra
(content block `def:kz-connection-sl2`). -/
lemma casimir_eq_flip :
    (casimir : Matrix (Fin 4) (Fin 4) R) = flip - (1/2 : R) • 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [casimir, flip] <;> norm_num

lemma qq_ne {q : R} (hq0 : q ≠ 0) (hq : q ^ 2 + 1 ≠ 0) : q + q⁻¹ ≠ 0 := by
  intro h
  apply hq
  have : q * (q + q⁻¹) = q ^ 2 + 1 := by field_simp
  rw [← this, h, mul_zero]

lemma conj_mul_conjInv {q : R} (hq0 : q ≠ 0) (hq : q ^ 2 + 1 ≠ 0) :
    conj q * conjInv q = 1 := by
  have h := qq_ne hq0 hq
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [conj, conjInv, Matrix.mul_apply, Fin.sum_univ_four] <;> field_simp <;> ring

lemma conjInv_mul_conj {q : R} (hq0 : q ≠ 0) (hq : q ^ 2 + 1 ≠ 0) :
    conjInv q * conj q = 1 := by
  have h := qq_ne hq0 hq
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [conj, conjInv, Matrix.mul_apply, Fin.sum_univ_four] <;> field_simp <;> ring

/-- The conjugator preserves total weight: it commutes with `K ⊗ K`. -/
lemma conj_commute_weight (q : R) : conj q * weightKK q = weightKK q * conj q := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [conj, weightKK, Matrix.mul_apply, Matrix.diagonal] <;> ring

/-- The classical exchange shape `q·P_sym − q⁻¹·P_anti`, written with `P_anti`. -/
def classicalExchange (q : R) : Matrix (Fin 4) (Fin 4) R :=
  q • (1 - antiProj) - q⁻¹ • antiProj

/-- **Algebraic core.** `Ř(q) · S = S · (q P_sym − q⁻¹ P_anti)`. -/
theorem rCheck_mul_conj {q : R} (hq0 : q ≠ 0) :
    rCheck q * conj q = conj q * classicalExchange q := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [rCheck, conj, classicalExchange, antiProj, Matrix.mul_apply, Fin.sum_univ_four] <;>
    field_simp <;> ring

theorem classicalExchange_eq_conj {q : R} (hq0 : q ≠ 0) (hq : q ^ 2 + 1 ≠ 0) :
    classicalExchange q = conjInv q * rCheck q * conj q := by
  rw [Matrix.mul_assoc, rCheck_mul_conj hq0, ← Matrix.mul_assoc, conjInv_mul_conj hq0 hq,
    Matrix.one_mul]

/-- The weighted trace of every power of the classical exchange equals that of
`Ř(q)`, because the conjugator preserves weight. -/
theorem trace_weight_classicalExchange_pow {q : R} (hq0 : q ≠ 0) (hq : q ^ 2 + 1 ≠ 0)
    (k : ℕ) :
    trace (weightKK q * classicalExchange q ^ k) = trace (weightKK q * rCheck q ^ k) := by
  have hpow : classicalExchange q ^ k = conjInv q * rCheck q ^ k * conj q := by
    induction k with
    | zero => simp [conjInv_mul_conj hq0 hq]
    | succ k ih =>
      rw [pow_succ, ih, classicalExchange_eq_conj hq0 hq, pow_succ]
      simp only [Matrix.mul_assoc]
      rw [← Matrix.mul_assoc (conj q) (conjInv q), conj_mul_conjInv hq0 hq, Matrix.one_mul]
  have hcomm' : weightKK q * conjInv q = conjInv q * weightKK q := by
    have h1 := conj_commute_weight q
    calc weightKK q * conjInv q
        = conjInv q * conj q * (weightKK q * conjInv q) := by
          rw [conjInv_mul_conj hq0 hq, Matrix.one_mul]
      _ = conjInv q * (conj q * weightKK q) * conjInv q := by simp only [Matrix.mul_assoc]
      _ = conjInv q * (weightKK q * conj q) * conjInv q := by rw [h1]
      _ = conjInv q * weightKK q * (conj q * conjInv q) := by simp only [Matrix.mul_assoc]
      _ = conjInv q * weightKK q := by rw [conj_mul_conjInv hq0 hq, Matrix.mul_one]
  rw [hpow]
  have hre : weightKK q * (conjInv q * rCheck q ^ k * conj q) =
      conjInv q * (weightKK q * rCheck q ^ k) * conj q := by
    rw [← Matrix.mul_assoc, ← Matrix.mul_assoc, hcomm']; simp only [Matrix.mul_assoc]
  rw [hre, Matrix.trace_mul_comm, ← Matrix.mul_assoc, conj_mul_conjInv hq0 hq, Matrix.one_mul]

/-- **The Hecke quadratic of the classical exchange.** `q P_sym − q⁻¹ P_anti` has the two
eigenvalues `q` and `−q⁻¹`, so `(β − q)(β + q⁻¹) = 0`. This is the relation the corpus
calls the "curvature" `F(σ) = σ² − (q − q⁻¹)σ − 1`; here it is an eigenvalue relation. -/
theorem classicalExchange_hecke {q : R} (hq : q ≠ 0) :
    (classicalExchange q - q • (1 : Matrix (Fin 4) (Fin 4) R)) *
      (classicalExchange q + q⁻¹ • 1) = 0 := by
  have h1 : classicalExchange q - q • (1 : Matrix (Fin 4) (Fin 4) R) =
      -(q + q⁻¹) • antiProj := by
    unfold classicalExchange; module
  have h2 : classicalExchange q + q⁻¹ • (1 : Matrix (Fin 4) (Fin 4) R) =
      (q + q⁻¹) • (1 - antiProj) := by
    unfold classicalExchange; module
  rw [h1, h2, smul_mul_smul_comm, Matrix.mul_sub, Matrix.mul_one, antiProj_mul_self,
    sub_self, smul_zero]

end Algebra

/-! ## Analytic part, over ℂ: the KZ transport along the half-turn -/

section Analysis

/-- Along the half-turn `w(t) = w₀ e^{iπt}`, the logarithmic derivative is `iπ`,
so `λ Ω dlog w` pulls back to `(iπλ) Ω dt`. -/
lemma halfTurn_logDeriv (w₀ : ℂ) (t : ℝ) :
    HasDerivAt (fun s : ℝ => w₀ * Complex.exp (Complex.I * Real.pi * s))
      ((Complex.I * Real.pi) * (w₀ * Complex.exp (Complex.I * Real.pi * t))) t := by
  have h : HasDerivAt (fun z : ℂ => w₀ * Complex.exp (Complex.I * Real.pi * z))
      (w₀ * (Complex.exp (Complex.I * Real.pi * t) * (Complex.I * Real.pi))) (t : ℂ) := by
    have := ((hasDerivAt_id (t : ℂ)).const_mul (Complex.I * Real.pi)).cexp
    simpa using this.const_mul w₀
  have := h.comp_ofReal
  convert this using 1
  ring

/-- The explicit KZ transport: `F(t)x = e^{ct/2} x + (e^{-3ct/2} − e^{ct/2}) P_anti x`,
i.e. `exp(ctΩ)` written through `Ω = ½ − 2 P_anti`. -/
noncomputable def transport (c : ℂ) (t : ℝ) (x : Fin 4 → ℂ) : Fin 4 → ℂ :=
  Complex.exp (c * t / 2) • x +
    (Complex.exp (-3 * c * t / 2) - Complex.exp (c * t / 2)) • (antiProj *ᵥ x)

lemma casimir_mulVec_transport (c : ℂ) (t : ℝ) (x : Fin 4 → ℂ) :
    casimir *ᵥ transport c t x =
      (Complex.exp (c * t / 2) / 2) • x +
        ((-3/2) * Complex.exp (-3 * c * t / 2) - (1/2) * Complex.exp (c * t / 2)) •
          (antiProj *ᵥ x) := by
  have hP : (antiProj : Matrix (Fin 4) (Fin 4) ℂ) *ᵥ (antiProj *ᵥ x) = antiProj *ᵥ x := by
    rw [Matrix.mulVec_mulVec, antiProj_mul_self]
  rw [casimir_eq, transport]
  simp only [Matrix.sub_mulVec, Matrix.smul_mulVec, Matrix.one_mulVec,
    Matrix.mulVec_add, Matrix.mulVec_smul, hP]
  ext i
  simp only [Pi.add_apply, Pi.sub_apply, Pi.smul_apply, smul_eq_mul]
  ring

/-- The transport solves the KZ system `F' = c Ω F`. -/
lemma transport_hasDerivAt (c : ℂ) (x : Fin 4 → ℂ) (t : ℝ) :
    HasDerivAt (fun s => transport c s x) (c • (casimir *ᵥ transport c t x)) t := by
  have e1 : HasDerivAt (fun s : ℝ => Complex.exp (c * s / 2))
      (Complex.exp (c * t / 2) * (c / 2)) t := by
    have : HasDerivAt (fun z : ℂ => Complex.exp (c * z / 2))
        (Complex.exp (c * t / 2) * (c / 2)) (t : ℂ) := by
      have := (((hasDerivAt_id (t : ℂ)).const_mul c).div_const 2).cexp
      simpa using this
    exact this.comp_ofReal
  have e2 : HasDerivAt (fun s : ℝ => Complex.exp (-3 * c * s / 2))
      (Complex.exp (-3 * c * t / 2) * (-3 * c / 2)) t := by
    have : HasDerivAt (fun z : ℂ => Complex.exp (-3 * c * z / 2))
        (Complex.exp (-3 * c * t / 2) * (-3 * c / 2)) (t : ℂ) := by
      have := (((hasDerivAt_id (t : ℂ)).const_mul (-3 * c)).div_const 2).cexp
      simpa using this
    exact this.comp_ofReal
  have h := (e1.smul_const x).add ((e2.sub e1).smul_const (antiProj *ᵥ x))
  rw [casimir_mulVec_transport]
  convert h using 1
  ext i
  simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul]
  ring

lemma transport_zero (c : ℂ) (x : Fin 4 → ℂ) : transport c 0 x = x := by
  simp [transport]

/-- **Uniqueness.** Any solution of `F' = c Ω F` on `[0,1]` with `F(0) = x`
equals the explicit transport there. -/
theorem kz_solution_unique (c : ℂ) (x : Fin 4 → ℂ) (F : ℝ → Fin 4 → ℂ)
    (hF : ∀ t, HasDerivAt F (c • (casimir *ᵥ F t)) t) (h0 : F 0 = x) :
    EqOn F (fun t => transport c t x) (Icc 0 1) := by
  let L : (Fin 4 → ℂ) →L[ℂ] (Fin 4 → ℂ) :=
    LinearMap.toContinuousLinearMap (c • Matrix.toLin' casimir)
  have hL : ∀ y, L y = c • (casimir *ᵥ y) := by
    intro y; simp [L]
  have hv : ∀ t ∈ Ico (0:ℝ) 1, LipschitzOnWith ‖L‖₊ (fun y : Fin 4 → ℂ => c • (casimir *ᵥ y)) univ := by
    intro t _
    have := L.lipschitz.lipschitzOnWith (s := univ)
    simpa [hL] using this
  apply ODE_solution_unique_of_mem_Icc_right (v := fun (_ : ℝ) (y : Fin 4 → ℂ) => c • (casimir *ᵥ y))
    (s := fun _ => univ) hv
  · exact (continuous_iff_continuousAt.2 fun t => (hF t).continuousAt).continuousOn
  · exact fun t _ => (hF t).hasDerivWithinAt
  · exact fun _ _ => mem_univ _
  · exact (continuous_iff_continuousAt.2 fun t =>
      (transport_hasDerivAt c x t).continuousAt).continuousOn
  · exact fun t _ => (transport_hasDerivAt c x t).hasDerivWithinAt
  · exact fun _ _ => mem_univ _
  · simp [h0, transport_zero]

/-- The KZ half-monodromy matrix: transport over `[0,1]` at `c = iπλ`. -/
noncomputable def halfMonodromy (c : ℂ) : Matrix (Fin 4) (Fin 4) ℂ :=
  Complex.exp (c / 2) • (1 : Matrix (Fin 4) (Fin 4) ℂ) +
    (Complex.exp (-3 * c / 2) - Complex.exp (c / 2)) • antiProj

lemma transport_one (c : ℂ) (x : Fin 4 → ℂ) : transport c 1 x = halfMonodromy c *ᵥ x := by
  simp [transport, halfMonodromy, Matrix.add_mulVec, Matrix.smul_mulVec]

/-- **Two-strand Drinfeld–Kohno.** The KZ exchange operator `flip · Hol` equals
`e^{-c/2}` times the classical exchange at `q = e^{c}`, hence `e^{-c/2}` times a
weight-preserving conjugate of the Jimbo `Ř(q)`. -/
theorem exchange_eq_classical (c : ℂ) :
    flip * halfMonodromy c = Complex.exp (-c / 2) • classicalExchange (Complex.exp c) := by
  have hq : Complex.exp c ≠ 0 := Complex.exp_ne_zero c
  have e1 : Complex.exp (-c / 2) * Complex.exp c = Complex.exp (c / 2) := by
    rw [← Complex.exp_add]; ring_nf
  have e2 : Complex.exp (-c / 2) * (Complex.exp c)⁻¹ = Complex.exp (-3 * c / 2) := by
    rw [← Complex.exp_neg, ← Complex.exp_add]; ring_nf
  rw [flip_eq, halfMonodromy, classicalExchange]
  have hP : (antiProj : Matrix (Fin 4) (Fin 4) ℂ) * antiProj = antiProj := antiProj_mul_self
  ext i j
  have := congrArg (fun M => M i j) hP
  simp only [Matrix.mul_apply, Fin.sum_univ_four] at this
  simp only [Matrix.sub_mul, Matrix.mul_add, Matrix.one_mul, Matrix.mul_smul, Matrix.smul_mul,
    Matrix.mul_one, hP, Matrix.sub_apply, Matrix.add_apply, Matrix.smul_apply, smul_eq_mul,
    Matrix.one_apply]
  rw [← e1, ← e2]
  ring

theorem exchange_eq_conj_rCheck (c : ℂ) (hq : Complex.exp c ^ 2 + 1 ≠ 0) :
    flip * halfMonodromy c =
      Complex.exp (-c / 2) •
        (conjInv (Complex.exp c) * rCheck (Complex.exp c) * conj (Complex.exp c)) := by
  rw [exchange_eq_classical, classicalExchange_eq_conj (Complex.exp_ne_zero c) hq]

/-- **Weighted trace.** For every two-strand braid `σ^k`, the weighted trace of
the KZ monodromy equals that of the Jimbo R-matrix, times the writhe scalar
`e^{-kc/2}`. -/
theorem trace_weight_exchange_pow (c : ℂ) (hq : Complex.exp c ^ 2 + 1 ≠ 0) (k : ℕ) :
    trace (weightKK (Complex.exp c) * (flip * halfMonodromy c) ^ k) =
      Complex.exp (-c / 2) ^ k *
        trace (weightKK (Complex.exp c) * rCheck (Complex.exp c) ^ k) := by
  rw [exchange_eq_classical, smul_pow, Matrix.mul_smul, Matrix.trace_smul, smul_eq_mul,
    trace_weight_classicalExchange_pow (Complex.exp_ne_zero c) hq]

/-- At a real `q > 1` the hypothesis `q² + 1 ≠ 0` holds, so the theorem applies
at the purely imaginary coupling `λ = ln q / (iπ)` (`c = iπλ = ln q`). -/
lemma real_q_admissible (q : ℝ) (hq : 1 < q) :
    Complex.exp (Real.log q : ℂ) ^ 2 + 1 ≠ 0 := by
  have hpos : (0 : ℝ) < q := by linarith
  rw [← Complex.ofReal_exp, Real.exp_log hpos]
  have : ((q : ℂ) ^ 2 + 1) = ((q ^ 2 + 1 : ℝ) : ℂ) := by push_cast; ring
  rw [this, Complex.ofReal_ne_zero]
  positivity

/-- **The KZ exchange satisfies the Hecke quadratic** — derived from the flat connection,
not assumed. With `q = e^c` (`c = iπλ`), `β = e^{c/2} · P · Hol` obeys
`(β − q)(β + q⁻¹) = 0`, equivalently `β² = (q − q⁻¹)β + 1`. -/
theorem exchange_hecke (c : ℂ) :
    (Complex.exp (c / 2) • (flip * halfMonodromy c) - Complex.exp c • 1) *
      (Complex.exp (c / 2) • (flip * halfMonodromy c) + (Complex.exp c)⁻¹ • 1) = 0 := by
  have hβ : Complex.exp (c / 2) • (flip * halfMonodromy c) = classicalExchange (Complex.exp c) := by
    rw [exchange_eq_classical, smul_smul, ← Complex.exp_add]
    have : c / 2 + -c / 2 = 0 := by ring
    rw [this, Complex.exp_zero, one_smul]
  rw [hβ]
  exact classicalExchange_hecke (Complex.exp_ne_zero c)


/-- The normalised KZ exchange `β = e^{c/2} · P · Hol` on `V ⊗ V`. -/
noncomputable def kzExchange (c : ℂ) : Matrix (Fin 4) (Fin 4) ℂ :=
  Complex.exp (c / 2) • (flip * halfMonodromy c)

/-- **The Hecke quadratic, expanded, as the monodromy relation of the KZ exchange.**
`β² = (q − q⁻¹) β + 1` with `q = e^c`. This is the form of the field
`QOU.Mass.HeckeMonodromy.quad`, here *derived* from the flat connection on two points. -/
theorem kzExchange_quad (c : ℂ) :
    kzExchange c * kzExchange c =
      (Complex.exp c - (Complex.exp c)⁻¹) • kzExchange c + 1 := by
  have h := exchange_hecke c
  rw [← kzExchange] at h
  have hq : Complex.exp c * (Complex.exp c)⁻¹ = 1 := mul_inv_cancel₀ (Complex.exp_ne_zero c)
  have e : (kzExchange c - Complex.exp c • 1) * (kzExchange c + (Complex.exp c)⁻¹ • 1) =
      kzExchange c * kzExchange c - (Complex.exp c - (Complex.exp c)⁻¹) • kzExchange c
        - (Complex.exp c * (Complex.exp c)⁻¹) • (1 : Matrix (Fin 4) (Fin 4) ℂ) := by
    simp only [sub_mul, mul_add, Matrix.smul_mul, Matrix.mul_smul, Matrix.one_mul,
      Matrix.mul_one, smul_smul, sub_smul]
    rw [mul_comm (Complex.exp c)⁻¹ (Complex.exp c)]
    abel
  rw [e, hq, one_smul, sub_eq_zero] at h
  rw [← h]
  abel

/-- **The classical shadow is the flip, an involution.** At `c = 0` (`q = 1`, no deformation)
the KZ exchange is the transposition of the two points: the shadow involution
`QOU.Mass.HeckeMonodromy.shadow_involution`, here at the specialisation `c = 0`. -/
theorem kzExchange_zero : kzExchange 0 = flip := by
  simp [kzExchange, halfMonodromy]

theorem flip_mul_flip : (flip : Matrix (Fin 4) (Fin 4) ℂ) * flip = 1 := by
  rw [flip_eq]
  have h := (antiProj_mul_self : (antiProj : Matrix (Fin 4) (Fin 4) ℂ) * antiProj = antiProj)
  simp only [sub_mul, mul_sub, Matrix.one_mul, Matrix.mul_one, Matrix.smul_mul,
    Matrix.mul_smul, smul_smul, h]
  module

/-- The shadow involution of `QOU.Mass.HeckeMonodromy` for the two-point KZ exchange:
at `q = 1` the exchange squares to the identity. -/
theorem kzExchange_shadow_involution : kzExchange 0 * kzExchange 0 = 1 := by
  rw [kzExchange_zero, flip_mul_flip]

end Analysis

end QOU.Mass.KohnoTwoPoint
