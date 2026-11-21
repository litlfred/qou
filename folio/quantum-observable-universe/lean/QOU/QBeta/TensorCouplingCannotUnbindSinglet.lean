import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic

/-!
# The spin–space (tensor) coupling cannot fix the two-nucleon sign defect

`computations/probes/two_nucleon_sector_sign_probe.py` measures that the framework
**binds the diproton and the dineutron** (`+2.5416`, `+3.3069 MeV`) where nature has no
bound state, and over-binds the deuteron by 27.3 % (`+2.8328` vs `+2.2246`). Every
*interface-scalar* mechanism is already excluded in Lean — `single_crossing_binds`,
`t3_grading_cannot_unbind_pp`, the projector floor `μ₊ + μ₋ = 1`, the T-odd total
floor (`TwoChannelTotalBindingFloor`), and any *separable* space factor
(`InterfaceScalar.separable_interface_degenerate`). Bean `qou-vbyi` names the one
surviving shape: a **non-separable (S, L) coupling — the ³S₁–³D₁ tensor force**, "the only
route past the proved flavour-only degeneracy".

This file shows that route cannot fix the sign defect, and cannot fix the deuteron
either. Two invariants, each proved sorry-free.

## (A) The tensor operator acts as a scalar on the spin singlet — and that scalar is 0

By Pauli, in a relative S-wave the two-nucleon spin and isospin symmetries are opposite:
`pp` and `nn` (`T = 1`) are pure **spin singlets** (`S = 0`). The tensor operator is
`S₁₂(n̂) = 3 (σ₁·n̂)(σ₂·n̂) − σ₁·σ₂`. On the singlet `|s⟩ = |↑↓⟩ − |↓↑⟩`:

* `σ₁·σ₂ |s⟩ = −3 |s⟩`                    (`sigmaDot_mulVec_singlet`)
* `(σ₁·n)(σ₂·n) |s⟩ = −|n|² |s⟩`   for every `n`   (`nDotProd_mulVec_singlet`)
* hence `S₁₂(n) |s⟩ = 3(1 − |n|²) |s⟩`, which is **`0` on the unit sphere**
  (`tensorOp_mulVec_singlet`, `tensorOp_annihilates_singlet`).

The singlet is an **eigenvector** of both generators, so any coupling built from them has
**no off-diagonal element out of `S = 0`** — there is nothing for the tensor force to mix
the singlet with (equivalently: at `J = 0`, `S = 0` has no `L = 2` partner). The channel
where the sign defect lives is untouched, for every direction `n̂`.

## (B) Off-diagonal coupling only LOWERS the ground state

Where the tensor force *does* act — the triplet, mixing `³S₁` with `³D₁` — the coupled
`2×2` block `[[E_S, t], [t, E_D]]` has lower eigenvalue
`λ₋ = (E_S+E_D)/2 − √(((E_S−E_D)/2)² + t²)`, and

* `λ₋ ≤ E_S` always, `λ₋ < E_S` whenever `t ≠ 0`  (`lowerEigen_lt_left_of_ne`).

So tensor mixing makes the deuteron **strictly more bound** than the uncoupled `³S₁`. The
uncoupled channel is already 27.3 % over-bound; coupling moves it the wrong way.

## Verdict (scope-(b), invariants named above)

The non-separable (S, L) tensor coupling of `qou-vbyi` route 1 is a **dead end for both
`A = 2` defects**: it is identically zero on the singlet where `pp`/`nn` live, and it can
only deepen the triplet where the deuteron is already over-bound. This closes the "live
shape" that bean leaves open. It does **not** exclude unbinding as such — the writhe-
normalised even-negative stacked words `σ^{−2k}` do unbind (`SingleCrossingAlwaysBinds`
§scope), at 6–9× nature's magnitude — nor a change to the binding law itself.

## Base ring (§7c)

Part (A) is over `ℂ` because `σ_y` needs `√−1`; no ordering, no `Real.*` — it is exact
matrix algebra. Part (B) is over `ℝ` by nature (an ordering statement with `Real.sqrt`).

-- Ref: [leitner2026] computations/probes/two_nucleon_sector_sign_probe.py
-- Ref: [leitner2026] docs/audits/2026-08-16-two-nucleon-sector-final-state-eight-closures.md
-- Ref: [leitner2026] docs/audits/2026-08-31-1s0-target-rescope-and-what-it-does-not-excuse.md
-/

namespace QOU.QBeta.TensorCouplingSinglet

open Matrix

/-! ## (A) Two spin-½ particles: the tensor operator on the singlet -/

section Singlet

/-- Basis order `|↑↑⟩, |↑↓⟩, |↓↑⟩, |↓↓⟩` (particle 1 first). `σ_x ⊗ 1`. -/
def s1x : Matrix (Fin 4) (Fin 4) ℂ := !![0,0,1,0; 0,0,0,1; 1,0,0,0; 0,1,0,0]
/-- `σ_y ⊗ 1`. -/
def s1y : Matrix (Fin 4) (Fin 4) ℂ :=
  !![0,0,-Complex.I,0; 0,0,0,-Complex.I; Complex.I,0,0,0; 0,Complex.I,0,0]
/-- `σ_z ⊗ 1`. -/
def s1z : Matrix (Fin 4) (Fin 4) ℂ := !![1,0,0,0; 0,1,0,0; 0,0,-1,0; 0,0,0,-1]
/-- `1 ⊗ σ_x`. -/
def s2x : Matrix (Fin 4) (Fin 4) ℂ := !![0,1,0,0; 1,0,0,0; 0,0,0,1; 0,0,1,0]
/-- `1 ⊗ σ_y`. -/
def s2y : Matrix (Fin 4) (Fin 4) ℂ :=
  !![0,-Complex.I,0,0; Complex.I,0,0,0; 0,0,0,-Complex.I; 0,0,Complex.I,0]
/-- `1 ⊗ σ_z`. -/
def s2z : Matrix (Fin 4) (Fin 4) ℂ := !![1,0,0,0; 0,-1,0,0; 0,0,1,0; 0,0,0,-1]

/-- The spin singlet `|↑↓⟩ − |↓↑⟩` (unnormalised). -/
def singlet : Fin 4 → ℂ := ![0, 1, -1, 0]

/-- `σ₁·σ₂`. -/
noncomputable def sigmaDot : Matrix (Fin 4) (Fin 4) ℂ := s1x * s2x + s1y * s2y + s1z * s2z

/-- `σ₁·n` for a direction `n = (n₁, n₂, n₃)`. -/
def nDot1 (n₁ n₂ n₃ : ℂ) : Matrix (Fin 4) (Fin 4) ℂ := n₁ • s1x + n₂ • s1y + n₃ • s1z
/-- `σ₂·n`. -/
def nDot2 (n₁ n₂ n₃ : ℂ) : Matrix (Fin 4) (Fin 4) ℂ := n₁ • s2x + n₂ • s2y + n₃ • s2z

/-- The tensor operator `S₁₂(n) = 3 (σ₁·n)(σ₂·n) − σ₁·σ₂`. -/
noncomputable def tensorOp (n₁ n₂ n₃ : ℂ) : Matrix (Fin 4) (Fin 4) ℂ :=
  (3 : ℂ) • (nDot1 n₁ n₂ n₃ * nDot2 n₁ n₂ n₃) - sigmaDot

/-- **`σ₁·σ₂` acts as `−3` on the singlet.** -/
theorem sigmaDot_mulVec_singlet : sigmaDot.mulVec singlet = (-3 : ℂ) • singlet := by
  ext k
  fin_cases k <;>
    simp [sigmaDot, s1x, s1y, s1z, s2x, s2y, s2z, singlet, Matrix.mulVec, dotProduct,
      Matrix.vecHead, Matrix.vecTail, Fin.sum_univ_four, Complex.I_mul_I] <;> ring

/-- **`(σ₁·n)(σ₂·n)` acts as `−|n|²` on the singlet, for every `n`.** -/
theorem nDotProd_mulVec_singlet (n₁ n₂ n₃ : ℂ) :
    (nDot1 n₁ n₂ n₃ * nDot2 n₁ n₂ n₃).mulVec singlet
      = (-(n₁ ^ 2 + n₂ ^ 2 + n₃ ^ 2)) • singlet := by
  ext k
  fin_cases k <;>
    simp [nDot1, nDot2, s1x, s1y, s1z, s2x, s2y, s2z, singlet, Matrix.mulVec, dotProduct,
      Matrix.vecHead, Matrix.vecTail, Matrix.mul_apply, Fin.sum_univ_four] <;>
    ring_nf <;> simp [Complex.I_sq] <;> ring

/-- **The tensor operator acts as the scalar `3(1 − |n|²)` on the singlet.** The singlet is
an eigenvector for every direction — there is no off-diagonal element out of `S = 0`. -/
theorem tensorOp_mulVec_singlet (n₁ n₂ n₃ : ℂ) :
    (tensorOp n₁ n₂ n₃).mulVec singlet
      = (3 * (1 - (n₁ ^ 2 + n₂ ^ 2 + n₃ ^ 2))) • singlet := by
  unfold tensorOp
  rw [Matrix.sub_mulVec, Matrix.smul_mulVec, nDotProd_mulVec_singlet,
    sigmaDot_mulVec_singlet]
  ext k
  fin_cases k <;> simp [singlet] <;> ring

/-- **On the unit sphere the tensor operator annihilates the singlet.** The `pp` / `nn`
channels — pure spin singlets by Pauli in an S-wave — are untouched by any tensor
coupling, for every direction `n̂`. -/
theorem tensorOp_annihilates_singlet (n₁ n₂ n₃ : ℂ) (hn : n₁ ^ 2 + n₂ ^ 2 + n₃ ^ 2 = 1) :
    (tensorOp n₁ n₂ n₃).mulVec singlet = 0 := by
  rw [tensorOp_mulVec_singlet, hn]
  simp

end Singlet

/-! ## (B) Off-diagonal coupling only lowers the ground state (2×2 interlacing) -/

section Interlacing

/-- The lower eigenvalue of the real symmetric block `[[a, t], [t, b]]`. -/
noncomputable def lowerEigen (a b t : ℝ) : ℝ :=
  (a + b) / 2 - Real.sqrt (((a - b) / 2) ^ 2 + t ^ 2)

/-- `λ₋` is a root of the characteristic polynomial `(a − λ)(b − λ) − t² = 0`. -/
theorem lowerEigen_is_eigenvalue (a b t : ℝ) :
    (a - lowerEigen a b t) * (b - lowerEigen a b t) - t ^ 2 = 0 := by
  unfold lowerEigen
  have h0 : (0:ℝ) ≤ ((a - b) / 2) ^ 2 + t ^ 2 := by positivity
  have hs := Real.sq_sqrt h0
  nlinarith [hs]

/-- `λ₋ ≤ a`: the coupled ground level never sits above the uncoupled `³S₁` level. -/
theorem lowerEigen_le_left (a b t : ℝ) : lowerEigen a b t ≤ a := by
  unfold lowerEigen
  have h0 : (0:ℝ) ≤ ((a - b) / 2) ^ 2 + t ^ 2 := by positivity
  have h1 : |(a - b) / 2| ≤ Real.sqrt (((a - b) / 2) ^ 2 + t ^ 2) := by
    rw [← Real.sqrt_sq_eq_abs]
    exact Real.sqrt_le_sqrt (by nlinarith)
  have h2 : (b - a) / 2 ≤ |(a - b) / 2| := by
    rw [show (b - a) / 2 = -((a - b) / 2) by ring]
    exact neg_le_abs _
  linarith

/-- **Strict interlacing.** With any nonzero coupling `t`, the coupled ground level is
**strictly below** the uncoupled level `a` — tensor mixing binds the deuteron *harder*.
Since the uncoupled `³S₁` is already 27.3 % over-bound, the coupling moves it the wrong
way. -/
theorem lowerEigen_lt_left_of_ne (a b t : ℝ) (ht : t ≠ 0) : lowerEigen a b t < a := by
  unfold lowerEigen
  have hpos : 0 < t ^ 2 := by positivity
  have h1 : |(a - b) / 2| < Real.sqrt (((a - b) / 2) ^ 2 + t ^ 2) := by
    rw [← Real.sqrt_sq_eq_abs]
    exact Real.sqrt_lt_sqrt (by positivity) (by linarith)
  have h2 : (b - a) / 2 ≤ |(a - b) / 2| := by
    rw [show (b - a) / 2 = -((a - b) / 2) by ring]
    exact neg_le_abs _
  linarith

/-- The symmetric statement: `λ₋ < b` too, so the coupled ground level lies strictly
below **both** uncoupled levels. -/
theorem lowerEigen_lt_right_of_ne (a b t : ℝ) (ht : t ≠ 0) : lowerEigen a b t < b := by
  unfold lowerEigen
  have hpos : 0 < t ^ 2 := by positivity
  have h1 : |(a - b) / 2| < Real.sqrt (((a - b) / 2) ^ 2 + t ^ 2) := by
    rw [← Real.sqrt_sq_eq_abs]
    exact Real.sqrt_lt_sqrt (by positivity) (by linarith)
  have h2 : (a - b) / 2 ≤ |(a - b) / 2| := le_abs_self _
  linarith

end Interlacing

end QOU.QBeta.TensorCouplingSinglet
