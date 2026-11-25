import Mathlib.Data.Matrix.Mul
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-!
# Discrete-exterior-calculus identities of the q-Navier–Stokes system

Ref: [leitner2026] Ch. 7, `def:q-navier-stokes` (`fluid-dynamics/q-navier-stokes.md`);
[mohamed2016dec] Mohamed–Hirani–Samtaney, *Discrete exterior calculus discretization
of incompressible Navier–Stokes equations over surface simplicial meshes*,
arXiv:1508.01166, §3.3 (pp. 10–16) and §5 (pp. 29–32).

This file states, over a finite 2-complex with unit Hodge stars, the structural
identities that the q-Navier–Stokes system of `def:q-navier-stokes` inherits once
its operators `d_q`, `δ_q`, `Δ_q` are realised as a cochain complex
`C⁰ →d₀ C¹ →d₁ C²` with `δ := dᵀ`. Everything is stated for an arbitrary
coefficient ring `R` and arbitrary finite index types (bean `qou-50hi`); the
ordered statements need an ordered field. Nothing here uses `ℝ`, `q₀`, or a metric.

What is proved (all sorry-free):

* `pairing_adjoint` — discrete Stokes / the adjunction `⟨d v, w⟩ = ⟨v, dᵀ w⟩`.
* `pressure_orth_of_divFree` — incompressibility `δ v = 0` makes the pressure
  gradient drop out of the energy.
* `exact_orth_coexact` — Hodge orthogonality `im d₀ ⊥ im d₁ᵀ`.
* `dirichlet_form` — `⟨v, Δ₁ v⟩ = |δ v|² + |d v|²`.
* `energy_equality` — for the semi-discrete system
  `v̇ = −B(v) − d₀ p − ν Δ₁ v` with a skew advection `⟨v, B(v)⟩ = 0` and
  `δ v = 0`: `⟨v, v̇⟩ = −ν |d₁ v|²`. This is the exact energy equality
  `dE/dt = −ν·Ω` (enstrophy `Ω = |ω|²`, `ω = d₁ v`), with no closure.
* `vorticity_equation` — `d₁ Δ₁ = Δ₂ d₁`, so the pressure drops out of the
  vorticity equation and `ω̇ = −d₁ B − ν Δ₂ ω`.
* `harmonic_circulation` — circulation along a harmonic 1-cochain
  (`d₁ h = 0`, `δ h = 0`) changes only through advection: pressure and viscosity
  never touch it. On a closed genus-`g` surface there are `2g` such directions
  (`dim ker Δ₁ = 8` on the Bring {5,4} map, exact rank, PR #9428).
* `total_circulation_zero`, `mass_conservation` — the exact discrete
  conservation laws of Mohamed et al. §5, from `1ᵀ d₁ = 0` and `d₀ 1 = 0`.
* `enstrophy_decay_of_spectral_gap` — **conditional on a spectral-gap
  hypothesis**, named in the lemma: under the linear (Stokes) part, enstrophy
  decays at rate `≥ 2νλ`. The gap value itself is not proved here; on the Bring
  map it is `λ₁(Δ₂) = 5 − √5` from an exact characteristic polynomial (probe
  `computations/probes/bring54_cochain_complex_probe.py`, PR #9428).

What is NOT claimed: nothing here is about 3D regularity. A finite complex gives
a finite-dimensional ODE; the Clay problem is untouched.

The viscosity section (`nuQ`) records two exact facts about `ν_q = ½(1 − q⁻¹)`
for bean `qou-0nqs`: it equals Nelson's diffusion constant `ℏ_q/(2m)` at the
mass `m = 1` that the corpus's own quantum pressure `Q_q` uses
(`nelson_consistency`), and in the substrate layer it is `O(q − 1)`
(`nuQ_one_add_le`), so identifying the Bredberg–Keeler–Lysov–Strominger
expansion parameter with `q − 1` puts the viscous term one order above the
advective one (Euler at leading order). Neither fact derives `ν_q`.
-/

namespace QOU.FluidDynamics.DEC

open Matrix

section Algebraic

variable {R : Type*} [CommRing R]
variable {V E F : Type*} [Fintype V] [Fintype E] [Fintype F]

/-- A 2-complex `C⁰ →d₀ C¹ →d₁ C²` over `R` with unit Hodge stars
(`δ := dᵀ`). `dd : d₁ d₀ = 0` is the cochain-complex axiom. -/
structure Complex2 (R V E F : Type*) [CommRing R] [Fintype E] where
  d0 : Matrix E V R
  d1 : Matrix F E R
  dd : d1 * d0 = 0

namespace Complex2

variable (C : Complex2 R V E F)

/-- Hodge Laplacian on 1-cochains, `Δ₁ = d₀ d₀ᵀ + d₁ᵀ d₁`. -/
def lap1 : Matrix E E R := C.d0 * C.d0ᵀ + C.d1ᵀ * C.d1

/-- Hodge Laplacian on 2-cochains of a 2-complex (top degree), `Δ₂ = d₁ d₁ᵀ`. -/
def lap2 : Matrix F F R := C.d1 * C.d1ᵀ

/-- Codifferential `δ v = d₀ᵀ v` (the discrete divergence, up to sign). -/
def divg (v : E → R) : V → R := C.d0ᵀ *ᵥ v

/-- Vorticity `ω = d₁ v`. -/
def vort (v : E → R) : F → R := C.d1 *ᵥ v

/-- Discrete Stokes / adjunction: `⟨A v, w⟩ = ⟨v, Aᵀ w⟩`. -/
theorem pairing_adjoint {m n : Type*} [Fintype m] [Fintype n]
    (A : Matrix m n R) (v : n → R) (w : m → R) :
    (A *ᵥ v) ⬝ᵥ w = v ⬝ᵥ (Aᵀ *ᵥ w) := by
  rw [dotProduct_mulVec, vecMul_transpose]

/-- Incompressibility `δ v = 0` removes the pressure gradient from the energy. -/
theorem pressure_orth_of_divFree (v : E → R) (p : V → R)
    (hinc : C.divg v = 0) : v ⬝ᵥ (C.d0 *ᵥ p) = 0 := by
  rw [dotProduct_comm, pairing_adjoint]
  simp [divg] at hinc
  simp [hinc]

/-- Hodge orthogonality: exact 1-cochains are orthogonal to coexact ones. -/
theorem exact_orth_coexact (p : V → R) (w : F → R) :
    (C.d0 *ᵥ p) ⬝ᵥ (C.d1ᵀ *ᵥ w) = 0 := by
  rw [dotProduct_comm, pairing_adjoint, transpose_transpose, mulVec_mulVec, C.dd]
  simp

/-- The Dirichlet form of `Δ₁`: `⟨v, Δ₁ v⟩ = |δ v|² + |d₁ v|²`. -/
theorem dirichlet_form (v : E → R) :
    v ⬝ᵥ (C.lap1 *ᵥ v) = C.divg v ⬝ᵥ C.divg v + C.vort v ⬝ᵥ C.vort v := by
  have h1 : v ⬝ᵥ (C.d0 *ᵥ (C.d0ᵀ *ᵥ v)) = (C.d0ᵀ *ᵥ v) ⬝ᵥ (C.d0ᵀ *ᵥ v) := by
    rw [dotProduct_comm, pairing_adjoint]
  have h2 : v ⬝ᵥ (C.d1ᵀ *ᵥ (C.d1 *ᵥ v)) = (C.d1 *ᵥ v) ⬝ᵥ (C.d1 *ᵥ v) := by
    rw [dotProduct_comm, pairing_adjoint, transpose_transpose]
  rw [lap1, add_mulVec, dotProduct_add, ← mulVec_mulVec, ← mulVec_mulVec, h1, h2]
  rfl

/-- The quadratic form of `Δ₂`: `⟨w, Δ₂ w⟩ = |d₁ᵀ w|²`. -/
theorem lap2_form (w : F → R) :
    w ⬝ᵥ (C.lap2 *ᵥ w) = (C.d1ᵀ *ᵥ w) ⬝ᵥ (C.d1ᵀ *ᵥ w) := by
  rw [lap2, ← mulVec_mulVec, dotProduct_comm, pairing_adjoint]

/-- **Energy equality** for the semi-discrete q-NS system
`v̇ = −B − d₀ p − ν Δ₁ v` with skew advection `⟨v, B⟩ = 0` and `δ v = 0`:
`⟨v, v̇⟩ = −ν |d₁ v|²`, i.e. `dE/dt = −ν·Ω` exactly. -/
theorem energy_equality (v vdot B : E → R) (p : V → R) (ν : R)
    (hNS : vdot = -B - C.d0 *ᵥ p - ν • (C.lap1 *ᵥ v))
    (hskew : v ⬝ᵥ B = 0) (hinc : C.divg v = 0) :
    v ⬝ᵥ vdot = -ν * (C.vort v ⬝ᵥ C.vort v) := by
  have hp := C.pressure_orth_of_divFree v p hinc
  have hD := C.dirichlet_form v
  rw [hinc] at hD
  simp only [zero_dotProduct, zero_add] at hD
  rw [hNS, dotProduct_sub, dotProduct_sub, dotProduct_neg, dotProduct_smul, hskew, hp, hD,
    smul_eq_mul]
  ring

/-- `d₁ Δ₁ = Δ₂ d₁` (uses `d₁ d₀ = 0`). -/
theorem d1_lap1 : C.d1 * C.lap1 = C.lap2 * C.d1 := by
  simp only [lap1, lap2, Matrix.mul_add, ← Matrix.mul_assoc, C.dd, Matrix.zero_mul, zero_add]

/-- **Vorticity equation**: pressure drops out and
`ω̇ = −d₁ B − ν Δ₂ ω`. -/
theorem vorticity_equation (v vdot B : E → R) (p : V → R) (ν : R)
    (hNS : vdot = -B - C.d0 *ᵥ p - ν • (C.lap1 *ᵥ v)) :
    C.vort vdot = -C.vort B - ν • (C.lap2 *ᵥ C.vort v) := by
  simp only [vort, hNS, mulVec_sub, mulVec_neg, mulVec_smul, mulVec_mulVec, C.dd, d1_lap1,
    zero_mulVec, sub_zero]

/-- A harmonic 1-cochain (`d₁ h = 0`, `δ h = 0`) is a steady Stokes solution. -/
theorem lap1_harmonic (h : E → R) (hc : C.vort h = 0) (hcc : C.divg h = 0) :
    C.lap1 *ᵥ h = 0 := by
  simp only [vort, divg] at hc hcc
  simp [lap1, add_mulVec, ← mulVec_mulVec, hc, hcc]

/-- `Δ₁` is symmetric. -/
theorem lap1_transpose : C.lap1ᵀ = C.lap1 := by
  simp [lap1, transpose_add, transpose_mul]

/-- **Harmonic circulation**: along a harmonic 1-cochain `h` the circulation
`⟨h, v⟩` changes only through advection; pressure and viscosity drop out. -/
theorem harmonic_circulation (v vdot B h : E → R) (p : V → R) (ν : R)
    (hNS : vdot = -B - C.d0 *ᵥ p - ν • (C.lap1 *ᵥ v))
    (hc : C.vort h = 0) (hcc : C.divg h = 0) :
    h ⬝ᵥ vdot = -(h ⬝ᵥ B) := by
  have hp : h ⬝ᵥ (C.d0 *ᵥ p) = 0 := C.pressure_orth_of_divFree h p hcc
  have hl : h ⬝ᵥ (C.lap1 *ᵥ v) = 0 := by
    rw [dotProduct_comm, pairing_adjoint, lap1_transpose, C.lap1_harmonic h hc hcc]
    simp
  rw [hNS, dotProduct_sub, dotProduct_sub, dotProduct_neg, dotProduct_smul, hp, hl]
  simp

/-- **Total circulation vanishes** on a closed oriented surface (`1ᵀ d₁ = 0`):
`Σ_f ω_f = 0` for every velocity. -/
theorem total_circulation_zero (hclosed : C.d1ᵀ *ᵥ (fun _ => (1 : R)) = 0) (v : E → R) :
    (fun _ => (1 : R)) ⬝ᵥ C.vort v = 0 := by
  rw [vort, dotProduct_comm, pairing_adjoint, hclosed, dotProduct_zero]

/-- **Mass conservation** for the continuity equation `ρ̇ = −δ J` on a complex
whose constants are closed (`d₀ 1 = 0`): `Σ_x ρ̇_x = 0`. -/
theorem mass_conservation (hconst : C.d0 *ᵥ (fun _ => (1 : R)) = 0)
    (J : E → R) (ρdot : V → R) (hcont : ρdot = -C.divg J) :
    (fun _ => (1 : R)) ⬝ᵥ ρdot = 0 := by
  rw [hcont, dotProduct_neg, divg, ← pairing_adjoint, hconst, zero_dotProduct, neg_zero]

/-- **Enstrophy equality** under the linear (Stokes) part:
`⟨ω, ω̇⟩ = −ν |d₁ᵀ ω|²` when `B = 0`. -/
theorem enstrophy_equality_stokes (v vdot : E → R) (p : V → R) (ν : R)
    (hNS : vdot = -(C.d0 *ᵥ p) - ν • (C.lap1 *ᵥ v)) :
    C.vort v ⬝ᵥ C.vort vdot = -ν * ((C.d1ᵀ *ᵥ C.vort v) ⬝ᵥ (C.d1ᵀ *ᵥ C.vort v)) := by
  have h := C.vorticity_equation v vdot 0 p ν (by rw [hNS]; simp)
  simp only [vort, mulVec_zero, neg_zero, zero_sub] at h ⊢
  rw [h, dotProduct_neg, dotProduct_smul, C.lap2_form, smul_eq_mul]
  ring

end Complex2

end Algebraic

section Ordered

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
variable {V E F : Type*} [Fintype V] [Fintype E] [Fintype F]
theorem dotProduct_self_nonneg' {n : Type*} [Fintype n] (w : n → K) : 0 ≤ w ⬝ᵥ w := by
  simp only [dotProduct]
  exact Finset.sum_nonneg (fun i _ => mul_self_nonneg (w i))

namespace Complex2

variable (C : Complex2 K V E F)

/-- Energy is non-increasing for `ν ≥ 0` (from `energy_equality`). -/
theorem energy_nonincreasing (v vdot B : E → K) (p : V → K) (ν : K) (hν : 0 ≤ ν)
    (hNS : vdot = -B - C.d0 *ᵥ p - ν • (C.lap1 *ᵥ v))
    (hskew : v ⬝ᵥ B = 0) (hinc : C.divg v = 0) :
    v ⬝ᵥ vdot ≤ 0 := by
  rw [C.energy_equality v vdot B p ν hNS hskew hinc]
  have := dotProduct_self_nonneg' (C.vort v)
  nlinarith

/-- **Enstrophy decay, conditional on a spectral gap of `Δ₂` on the
mean-zero 2-cochains** (hypothesis `hgap`, not proved here; on the Bring {5,4}
map `λ = 5 − √5`, exact, PR #9428). On a closed oriented surface every
vorticity has mean zero, so under the Stokes part
`⟨ω, ω̇⟩ ≤ −ν λ |ω|²`. -/
theorem enstrophy_decay_of_spectral_gap (gap ν : K) (hν : 0 ≤ ν)
    (hclosed : C.d1ᵀ *ᵥ (fun _ => (1 : K)) = 0)
    (hgap : ∀ w : F → K, (fun _ => (1 : K)) ⬝ᵥ w = 0 →
      gap * (w ⬝ᵥ w) ≤ w ⬝ᵥ (C.lap2 *ᵥ w))
    (v vdot : E → K) (p : V → K)
    (hNS : vdot = -(C.d0 *ᵥ p) - ν • (C.lap1 *ᵥ v)) :
    C.vort v ⬝ᵥ C.vort vdot ≤ -(ν * gap) * (C.vort v ⬝ᵥ C.vort v) := by
  have hg := hgap (C.vort v) (C.total_circulation_zero hclosed v)
  have hq := C.lap2_form (C.vort v)
  rw [C.enstrophy_equality_stokes v vdot p ν hNS, ← hq]
  nlinarith [mul_le_mul_of_nonneg_left hg hν]

end Complex2

end Ordered

section Viscosity

/-- Substrate grain `ℏ_q = 1 − q⁻¹` (`def:substrate-parameter`). -/
def hbarQ {K : Type*} [Field K] (q : K) : K := 1 - q⁻¹

/-- The q-NS kinematic viscosity as *introduced* in `def:q-navier-stokes`:
`ν_q = ½(1 − q⁻¹)`. This file does not derive it. -/
def nuQ {K : Type*} [Field K] (q : K) : K := (1 - q⁻¹) / 2

theorem nuQ_eq_half_hbarQ {K : Type*} [Field K] (q : K) : nuQ q = hbarQ q / 2 := rfl

theorem nuQ_eq {K : Type*} [Field K] (q : K) (hq : q ≠ 0) :
    nuQ q = (q - 1) / (2 * q) := by
  unfold nuQ; field_simp

/-- **Nelson consistency.** The quantum pressure of `def:q-navier-stokes` is
`Q_q = −½ ℏ_q² Δ√ρ/√ρ`, i.e. Madelung's `−(ℏ²/2m) Δ√ρ/√ρ` at `m = 1`. Nelson's
diffusion constant at that mass is `D = ℏ_q/(2m) = ℏ_q/2 = ν_q`, and the
Madelung coefficient is `2D²`. So `ν_q` is the *same* number as the Nelson
diffusion constant the corpus's `Q_q` already fixes. This is consistency of one
parameter between two terms, not a derivation that `D` acts as a viscosity: in
Nelson's theory `D` drives an osmotic term of an inviscid fluid. -/
theorem nelson_consistency {K : Type*} [Field K] (q : K) (h2 : (2 : K) ≠ 0) :
    hbarQ q ^ 2 / 2 = 2 * nuQ q ^ 2 := by
  unfold hbarQ nuQ; field_simp

/-- In the substrate layer `ν_q` is `O(q − 1)`: for `q = 1 + ε`, `ε ≥ 0`,
`ν_q ≤ ε/2`. Under the Bredberg–Keeler–Lysov–Strominger scaling
(`v ~ ε`, `∂ᵢ ~ ε`, `∂ₜ ~ ε²`, arXiv:1101.2451 §3) the advective terms are
`O(ε³)` and the viscous term is `ν·O(ε³)`; with `ε := q − 1` the viscous term is
`O(ε⁴)`, so the leading order is incompressible **Euler**, not Navier–Stokes. -/
theorem nuQ_one_add_le {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    (ε : K) (hε : 0 ≤ ε) : nuQ (1 + ε) ≤ ε / 2 := by
  have h1 : (0 : K) < 1 + ε := by linarith
  rw [nuQ_eq (1 + ε) h1.ne', div_le_div_iff₀ (by positivity) (by norm_num)]
  nlinarith

/-- Physical layer (`def:qns-unit-layers`): `ν_phys = c_q ν_q = 1/(2q)` with
`c_q = 1/(q − 1)`. It tends to `½`, so in that layer the viscosity is `O(1)` in
`q − 1`, which is the shape Bredberg et al. need (`ν = r_c` fixed). -/
theorem nuPhys_eq {K : Type*} [Field K] (q : K) (hq : q ≠ 0) (hq1 : q - 1 ≠ 0) :
    (q - 1)⁻¹ * nuQ q = 1 / (2 * q) := by
  rw [nuQ_eq q hq]; field_simp

end Viscosity

end QOU.FluidDynamics.DEC
