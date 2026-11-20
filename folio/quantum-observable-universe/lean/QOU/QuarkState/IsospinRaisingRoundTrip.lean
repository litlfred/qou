/-
# The neutron–proton flip on the Schur–Weyl dual side: the `T⁺` round trip

Bean `qou-99qc` (which functional is `ε` in `Q_β = |ε(Δ_S)|·E₀`), route R2/R5 of
2026-11-20, label C of `docs/audits/2026-11-20-qbeta-epsilon-is-ruled-not-derived.md` §9.

## Setting

`V = K²` with basis `u` (`T³ = +½`, `K u = q u`) and `d` (`T³ = −½`, `K d = q⁻¹ d`). On
`V ⊗ V` the Jimbo matrix `Ř` (`Rc` below) satisfies `(Ř − q)(Ř + q⁻¹) = 0` and commutes with
`Δ(K) = K⊗K`, `Δ(E) = E⊗K + 1⊗E`, `Δ(F) = F⊗1 + K⁻¹⊗F` (`Rc_comm_*`). On `V^{⊗3}`,
`σ₁ = Ř⊗1`, `σ₂ = 1⊗Ř` give `H₃(q)`. Since `σᵢ` commute with `Δ²(K)`, every Hecke element
preserves each weight space (charge): this is why no braid word, the `γγ` vertex included,
changes `T³` (the label-A and label-B flips of `FlavourDoubletFourStrands` are Hecke-internal,
so they preserve charge and cannot be `n ↔ p`, which changes charge by one).

The neutron weight space `W₋` (one `u`: basis `udd, dud, ddu`) and the proton weight space
`W₊` (two `u`: `duu, udu, uud`) are each three-dimensional. `sm1, sm2` (resp. `sp1, sp2`) are
`σ₁, σ₂` restricted to `W₋` (resp. `W₊`); `Eu : W₋ → W₊` and `Fd : W₊ → W₋` are `Δ²(E)` and
`Δ²(F)` restricted. All entries were read off the `8 × 8` model (probe
`computations/probes/qbeta_r253/r2_r5_isospin_round_trip_probe.py`, 16/16 exact); this file
re-proves every relation it uses on the restricted matrices.

## What is proved (generic `[Field K]`, no `ℝ`, no `sorry`)

* `Rc_quad`, `Rc_comm_K`, `Rc_comm_E`, `Rc_comm_F`: the Schur–Weyl commutation on `V ⊗ V`.
* `sm1_quad`, `sm2_quad`, `sm_braid` (and `sp*`): `W₋`, `W₊` are `H₃(q)`-modules.
* `Eu_sm1`, `Eu_sm2`, `Fd_sp1`, `Fd_sp2`: `T⁺`, `T⁻` intertwine the Hecke action.
* `FE_quad`: on `W₋`, `(T⁻T⁺ − [2]²)(T⁻T⁺ − 1) = 0` — eigenvalue `[2]²` on isospin `3/2`,
  `1` on isospin `½`.
* `trace_FE`, `trace_FE_J1`, `trace_FE_deltaS`, and the normalised
  `epsC_J1 : tr(T⁻T⁺ J)/tr(T⁻T⁺) = (q²+1)²/(q⁴+4q²+1) = [2]²/([2]²+2)`,
  `epsC_deltaS : tr(T⁻T⁺ Δ_S)/tr(T⁻T⁺) = −(h[2]/2)·(q²+1)²/(q⁴+4q²+1)`.
* `isospinHalf_deltaS`: the isospin-`½` part of the round trip does not see `Δ_S` at all,
  `tr(([2]² − T⁻T⁺)·T⁻T⁺·Δ_S) = 0`. With `chi21_deltaS` (`QBetaChiralityReduction`) this is
  the statement that `Δ_S` lives in the `(3)` (isospin `3/2`) block.
* `qtrace_J1`: the quantum trace over all of `V^{⊗3}` (weights `q^{2T³}`, i.e. closing every
  strand by pair creation and annihilation) gives `(q⁴+1)/(q²+1)²`, the convention-D `y₃`.

## What is NOT proved

That the decay channel's `ε` is this round trip. The file supplies one construction in which
`n → p` changes `T³` (label C); the posit is `n → p = T⁺`, and the normalisation `ε(1) = 1`
is the same convention as D, not derived. `E₀` stays posited. No number is wired.

-- Ref: [jimbo1986] https://doi.org/10.1007/BF00400222 (q-Schur–Weyl duality)
-- Ref: [humphreys1990] §7.4 (Hecke algebra, generic q)
-/
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Data.Matrix.Mul
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Ring

namespace QOU.QuarkState.IsospinRaisingRoundTrip

open Matrix

variable {K : Type*} [Field K]

/-! ## `V ⊗ V`: basis `uu, ud, du, dd` -/

/-- Jimbo `Ř`: `uu ↦ q uu`, `ud ↦ du`, `du ↦ ud + h du`, `dd ↦ q dd` (columns = images). -/
def Rc (q : K) : Matrix (Fin 4) (Fin 4) K :=
  !![q, 0, 0, 0; 0, 0, 1, 0; 0, 1, q - q⁻¹, 0; 0, 0, 0, q]

/-- `Δ(K) = K ⊗ K`. -/
def dK (q : K) : Matrix (Fin 4) (Fin 4) K :=
  !![q ^ 2, 0, 0, 0; 0, 1, 0, 0; 0, 0, 1, 0; 0, 0, 0, q⁻¹ ^ 2]

/-- `Δ(E) = E ⊗ K + 1 ⊗ E` (`E d = u`). -/
def dE (q : K) : Matrix (Fin 4) (Fin 4) K :=
  !![0, 1, q, 0; 0, 0, 0, q⁻¹; 0, 0, 0, 1; 0, 0, 0, 0]

/-- `Δ(F) = F ⊗ 1 + K⁻¹ ⊗ F` (`F u = d`). -/
def dF (q : K) : Matrix (Fin 4) (Fin 4) K :=
  !![0, 0, 0, 0; q⁻¹, 0, 0, 0; 1, 0, 0, 0; 0, 1, q, 0]

section VV

variable {q : K} (hq : q ≠ 0)
include hq

theorem Rc_quad : (Rc q - q • 1) * (Rc q + q⁻¹ • 1) = 0 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Rc, Matrix.mul_apply, Fin.sum_univ_four, Matrix.one_apply] <;> field_simp <;> ring

theorem Rc_comm_K : Rc q * dK q = dK q * Rc q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Rc, dK, Matrix.mul_apply, Fin.sum_univ_four] <;> field_simp <;> ring

theorem Rc_comm_E : Rc q * dE q = dE q * Rc q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Rc, dE, Matrix.mul_apply, Fin.sum_univ_four] <;> field_simp <;> ring

theorem Rc_comm_F : Rc q * dF q = dF q * Rc q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Rc, dF, Matrix.mul_apply, Fin.sum_univ_four] <;> field_simp <;> ring

end VV

/-! ## The neutron and proton weight spaces of `V^{⊗3}` -/

/-- `σ₁` on `W₋` (basis `udd, dud, ddu`). -/
def sm1 (q : K) : Matrix (Fin 3) (Fin 3) K := !![0, 1, 0; 1, q - q⁻¹, 0; 0, 0, q]
/-- `σ₂` on `W₋`. -/
def sm2 (q : K) : Matrix (Fin 3) (Fin 3) K := !![q, 0, 0; 0, 0, 1; 0, 1, q - q⁻¹]
/-- `σ₁` on `W₊` (basis `duu, udu, uud`). -/
def sp1 (q : K) : Matrix (Fin 3) (Fin 3) K := !![q - q⁻¹, 1, 0; 1, 0, 0; 0, 0, q]
/-- `σ₂` on `W₊`. -/
def sp2 (q : K) : Matrix (Fin 3) (Fin 3) K := !![q, 0, 0; 0, q - q⁻¹, 1; 0, 1, 0]
/-- `T⁺ = Δ²(E) : W₋ → W₊`, the neutron-to-proton flip. -/
def Eu (q : K) : Matrix (Fin 3) (Fin 3) K := !![0, 1, q; 1, 0, 1; q⁻¹, 1, 0]
/-- `T⁻ = Δ²(F) : W₊ → W₋`. -/
def Fd (q : K) : Matrix (Fin 3) (Fin 3) K := !![0, 1, q⁻¹; 1, 0, 1; q, 1, 0]

/-- `h = q − q⁻¹`. -/
def hh (q : K) : K := q - q⁻¹
/-- `[2] = q + q⁻¹`. -/
def b2 (q : K) : K := q + q⁻¹

/-- `Δ_S = 𝓑_n − 𝓑_p` on `W₋`, with `𝓑_p = σ₁(σ₂ − h/2)`, `𝓑_n = (σ₁ − h/2)(σ₂ − h)`. -/
def deltaS (q : K) : Matrix (Fin 3) (Fin 3) K :=
  (sm1 q - (hh q / 2) • 1) * (sm2 q - hh q • 1) - sm1 q * (sm2 q - (hh q / 2) • 1)

/-- The chirality grading `J = (σ₁ + σ₁⁻¹)/[2] = (2σ₁ − h)/[2]` on `W₋`. -/
def J1m (q : K) : Matrix (Fin 3) (Fin 3) K := (b2 q)⁻¹ • ((2 : K) • sm1 q - hh q • 1)
/-- The same on `W₊`. -/
def J1p (q : K) : Matrix (Fin 3) (Fin 3) K := (b2 q)⁻¹ • ((2 : K) • sp1 q - hh q • 1)

section Weight

variable {q : K} (hq : q ≠ 0)
include hq

theorem sm1_quad : (sm1 q - q • 1) * (sm1 q + q⁻¹ • 1) = 0 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [sm1, Matrix.mul_apply, Fin.sum_univ_three, Matrix.one_apply] <;> field_simp <;> ring

theorem sm2_quad : (sm2 q - q • 1) * (sm2 q + q⁻¹ • 1) = 0 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [sm2, Matrix.mul_apply, Fin.sum_univ_three, Matrix.one_apply] <;> field_simp <;> ring

theorem sm_braid : sm1 q * sm2 q * sm1 q = sm2 q * sm1 q * sm2 q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [sm1, sm2, Matrix.mul_apply, Fin.sum_univ_three] <;> field_simp <;> ring

theorem sp1_quad : (sp1 q - q • 1) * (sp1 q + q⁻¹ • 1) = 0 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [sp1, Matrix.mul_apply, Fin.sum_univ_three, Matrix.one_apply] <;> field_simp <;> ring

theorem sp2_quad : (sp2 q - q • 1) * (sp2 q + q⁻¹ • 1) = 0 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [sp2, Matrix.mul_apply, Fin.sum_univ_three, Matrix.one_apply] <;> field_simp <;> ring

theorem sp_braid : sp1 q * sp2 q * sp1 q = sp2 q * sp1 q * sp2 q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [sp1, sp2, Matrix.mul_apply, Fin.sum_univ_three] <;> field_simp <;> ring

/-- `T⁺` intertwines `σ₁`. -/
theorem Eu_sm1 : Eu q * sm1 q = sp1 q * Eu q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Eu, sm1, sp1, Matrix.mul_apply, Fin.sum_univ_three] <;> field_simp <;> ring

/-- `T⁺` intertwines `σ₂`. -/
theorem Eu_sm2 : Eu q * sm2 q = sp2 q * Eu q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Eu, sm2, sp2, Matrix.mul_apply, Fin.sum_univ_three] <;> field_simp <;> ring

/-- `T⁻` intertwines `σ₁`. -/
theorem Fd_sp1 : Fd q * sp1 q = sm1 q * Fd q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Fd, sm1, sp1, Matrix.mul_apply, Fin.sum_univ_three] <;> field_simp <;> ring

/-- `T⁻` intertwines `σ₂`. -/
theorem Fd_sp2 : Fd q * sp2 q = sm2 q * Fd q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Fd, sm2, sp2, Matrix.mul_apply, Fin.sum_univ_three] <;> field_simp <;> ring

/-- On `W₋`, `T⁻T⁺` has eigenvalues `[2]²` (isospin `3/2`) and `1` (isospin `½`). -/
theorem FE_quad :
    (Fd q * Eu q - (b2 q) ^ 2 • 1) * (Fd q * Eu q - 1) = 0 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [Fd, Eu, b2, Matrix.mul_apply, Fin.sum_univ_three, Matrix.one_apply] <;>
    field_simp <;> ring

/-- `Δ_S = (h²/2) − (h/2)(σ₁ + σ₂)` on `W₋`, written out. -/
theorem deltaS_eq (h2 : (2 : K) ≠ 0) :
    deltaS q = !![-(hh q) / (2 * q), -(hh q) / 2, 0; -(hh q) / 2, 0, -(hh q) / 2;
      0, -(hh q) / 2, -(hh q) * q / 2] := by
  unfold deltaS sm1 sm2 hh
  simp only [Matrix.one_fin_three, Matrix.smul_of, Matrix.smul_vec3, Matrix.of_sub_of,
    Matrix.of_add_of, Matrix.mul_fin_three]
  ext i j; fin_cases i <;> fin_cases j <;> simp <;> field_simp <;> ring

theorem trace_FE : trace (Fd q * Eu q) = (q ^ 4 + 4 * q ^ 2 + 1) / q ^ 2 := by
  simp only [Matrix.trace_fin_three]
  simp [Fd, Eu, Matrix.mul_apply, Fin.sum_univ_three]
  field_simp; ring

theorem trace_FE_J1 (hb : b2 q ≠ 0) :
    trace (Fd q * Eu q * J1m q) = (q ^ 2 + 1) ^ 2 / q ^ 2 := by
  have hb' : q ^ 2 + 1 ≠ 0 := by
    intro h; apply hb; unfold b2; field_simp; linear_combination h
  simp only [Matrix.trace_fin_three]
  simp [Fd, Eu, J1m, sm1, hh, b2, Matrix.mul_apply,
    Fin.sum_univ_three, Matrix.one_apply]
  field_simp; ring

theorem trace_FE_deltaS (h2 : (2 : K) ≠ 0) :
    trace (Fd q * Eu q * deltaS q) = -(hh q * b2 q / 2) * ((q ^ 2 + 1) ^ 2 / q ^ 2) := by
  rw [deltaS_eq hq h2]
  simp only [Matrix.trace_fin_three]
  simp [Fd, Eu, hh, b2, Matrix.mul_apply, Fin.sum_univ_three]
  field_simp; ring

/-- **Label C, the normalised `T⁺` round trip, on the chirality grading.** -/
theorem epsC_J1 (hb : b2 q ≠ 0) (hD : q ^ 4 + 4 * q ^ 2 + 1 ≠ 0) :
    trace (Fd q * Eu q * J1m q) / trace (Fd q * Eu q) =
      (q ^ 2 + 1) ^ 2 / (q ^ 4 + 4 * q ^ 2 + 1) := by
  rw [trace_FE_J1 hq hb, trace_FE hq]
  field_simp

/-- **Label C on `Δ_S`**: `ε_C(Δ_S) = −(h[2]/2)·y₃^C`. -/
theorem epsC_deltaS (h2 : (2 : K) ≠ 0) (hD : q ^ 4 + 4 * q ^ 2 + 1 ≠ 0) :
    trace (Fd q * Eu q * deltaS q) / trace (Fd q * Eu q) =
      -(hh q * b2 q / 2) * ((q ^ 2 + 1) ^ 2 / (q ^ 4 + 4 * q ^ 2 + 1)) := by
  rw [trace_FE_deltaS hq h2, trace_FE hq]
  field_simp

/-- The proton side gives the same: `tr_{W₊}(T⁺T⁻ J)/tr_{W₊}(T⁺T⁻) = y₃^C`. -/
theorem epsC_J1_from_p (hb : b2 q ≠ 0) (hD : q ^ 4 + 4 * q ^ 2 + 1 ≠ 0) :
    trace (Eu q * Fd q * J1p q) / trace (Eu q * Fd q) =
      (q ^ 2 + 1) ^ 2 / (q ^ 4 + 4 * q ^ 2 + 1) := by
  have hb' : q ^ 2 + 1 ≠ 0 := by
    intro h; apply hb; unfold b2; field_simp; linear_combination h
  have h1 : trace (Eu q * Fd q * J1p q) = (q ^ 2 + 1) ^ 2 / q ^ 2 := by
    simp only [Matrix.trace_fin_three]
    simp [Fd, Eu, J1p, sp1, hh, b2, Matrix.mul_apply,
      Fin.sum_univ_three, Matrix.one_apply]
    field_simp; ring
  have h2 : trace (Eu q * Fd q) = (q ^ 4 + 4 * q ^ 2 + 1) / q ^ 2 := by
    simp only [Matrix.trace_fin_three]
    simp [Fd, Eu, Matrix.mul_apply, Fin.sum_univ_three]
    field_simp; ring
  rw [h1, h2]; field_simp

/-- **The isospin-`½` part of the round trip does not see `Δ_S`.** -/
theorem isospinHalf_deltaS (h2 : (2 : K) ≠ 0) :
    trace (((b2 q) ^ 2 • 1 - Fd q * Eu q) * (Fd q * Eu q) * deltaS q) = 0 := by
  rw [deltaS_eq hq h2]
  simp only [Matrix.trace_fin_three]
  simp [Fd, Eu, hh, b2, Matrix.mul_apply, Fin.sum_univ_three, Matrix.one_apply]
  field_simp; ring

/-- The quantum trace over all of `V^{⊗3}`, weights `q^{2T³}`: `uuu` and `ddd` are lines on
which every `σ` acts by `q`, so `J = 1` there. -/
def qtr (xuuu : K) (Xp Xm : Matrix (Fin 3) (Fin 3) K) (xddd : K) : K :=
  q ^ 3 * xuuu + q * trace Xp + q⁻¹ * trace Xm + q⁻¹ ^ 3 * xddd

omit hq in
/-- On `uuu` the grading `J = (2q − h)/[2]` is `1`. -/
theorem J_on_top (hq : q ≠ 0) (hb : b2 q ≠ 0) : (b2 q)⁻¹ * (2 * q - hh q) = 1 := by
  unfold b2 hh at *
  rw [show 2 * q - (q - q⁻¹) = q + q⁻¹ by ring]
  exact inv_mul_cancel₀ hb

theorem trace_J1m (hb : b2 q ≠ 0) : trace (J1m q) = 1 := by
  have hb' : q ^ 2 + 1 ≠ 0 := by
    intro h; apply hb; unfold b2; field_simp; linear_combination h
  simp only [Matrix.trace_fin_three]
  simp [J1m, sm1, hh, b2]
  field_simp; ring

theorem trace_J1p (hb : b2 q ≠ 0) : trace (J1p q) = 1 := by
  have hb' : q ^ 2 + 1 ≠ 0 := by
    intro h; apply hb; unfold b2; field_simp; linear_combination h
  simp only [Matrix.trace_fin_three]
  simp [J1p, sp1, hh, b2]
  field_simp; ring

/-- **The full quantum trace is convention D**: closing every strand (pair creation and
annihilation) gives `y₃ = (q⁴+1)/(q²+1)²`, the ruled label-A value. -/
theorem qtrace_J1 (hb : b2 q ≠ 0) :
    qtr (q := q) 1 (J1p q) (J1m q) 1 / qtr (q := q) 1 1 1 1 =
      (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2 := by
  have hb' : q ^ 2 + 1 ≠ 0 := by
    intro h; apply hb; unfold b2; field_simp; linear_combination h
  have h1 : trace (1 : Matrix (Fin 3) (Fin 3) K) = 3 := by
    simp
  have hn : qtr (q := q) 1 (J1p q) (J1m q) 1 = (q ^ 2 + 1) * (q ^ 4 + 1) / q ^ 3 := by
    simp only [qtr]; rw [trace_J1p hq hb, trace_J1m hq hb]; field_simp
    try ring
  have hd : qtr (q := q) 1 1 1 1 = (q ^ 2 + 1) ^ 3 / q ^ 3 := by
    simp only [qtr]; rw [h1]; field_simp
    try ring
  rw [hn, hd]; field_simp

end Weight

end QOU.QuarkState.IsospinRaisingRoundTrip

#print axioms QOU.QuarkState.IsospinRaisingRoundTrip.Rc_comm_E
#print axioms QOU.QuarkState.IsospinRaisingRoundTrip.Eu_sm1
#print axioms QOU.QuarkState.IsospinRaisingRoundTrip.FE_quad
#print axioms QOU.QuarkState.IsospinRaisingRoundTrip.epsC_J1
#print axioms QOU.QuarkState.IsospinRaisingRoundTrip.epsC_deltaS
#print axioms QOU.QuarkState.IsospinRaisingRoundTrip.epsC_J1_from_p
#print axioms QOU.QuarkState.IsospinRaisingRoundTrip.isospinHalf_deltaS
#print axioms QOU.QuarkState.IsospinRaisingRoundTrip.qtrace_J1
