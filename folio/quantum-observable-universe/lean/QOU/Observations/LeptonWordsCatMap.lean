import QOU.Observations.LeptonChargeClassTrace

/-!
# The lepton words through the cat map `L = σ₀σ₁⁻¹`

Thread "Derive the muon mass relation" (2026-11-28), answering the owner's question whether
`4₁` acts on the muon word. Current words (owner's tap, PR #9908): `e = σ₀σ₁σ₀` (Hopf),
`μ = σ₀⁴σ₁⁻¹` (T(2,4)), `τ = σ₀²σ₁⁻¹σ₀σ₁⁻¹` (Whitehead); `4₁ = (σ₀σ₁⁻¹)²` is neutral.

Under `B₃ → SL(2, ℤ)` (`LeptonChargeClassTrace.imgZ`):
* `img_L`: `L = σ₀σ₁⁻¹ ↦ [[2,1],[1,1]]`, Arnold's cat map; `4₁ = L²` is its mapping torus.
* `mu_word_eq`, `tau_word_eq`: as words, `μ = σ₀³ · L` and `τ = σ₀ · L²`, so `τ` contains
  the `4₁` word exactly, while `μ` contains one `L`.
* `tau_ne_mu_mul_fig8`: the images satisfy `img τ ≠ img μ · img 4₁`, so `τ` is not `μ`
  multiplied by `4₁` (and `img τ ≠ img 4₁ · img μ`).
* Images and traces: `e ↦ [[0,1],[−1,0]]` (tr 0), `μ ↦ [[5,4],[1,1]]` (tr 6),
  `τ ↦ [[8,5],[3,2]]` (tr 10), `4₁ ↦ [[5,3],[3,2]]` (tr 7).

So braid multiplication by `4₁` is not the generation step. Connected sum (knot convolution,
#9824), under which volumes add, is a different operation and is not treated here.
-/

namespace QOU.Observations.LeptonWordsCatMap

open QOU.Observations.LeptonChargeClassTrace

abbrev Word := List (Fin 2 × Bool)

def sig0 : Word := [(0, true)]
def wL : Word := [(0, true), (1, false)]
def wE : Word := [(0, true), (1, true), (0, true)]
def wMu : Word := [(0, true), (0, true), (0, true), (0, true), (1, false)]
def wTau : Word := [(0, true), (0, true), (1, false), (0, true), (1, false)]
def wFig8 : Word := wL ++ wL

theorem mu_word_eq : wMu = sig0 ++ sig0 ++ sig0 ++ wL := rfl
theorem tau_word_eq : wTau = sig0 ++ wFig8 := rfl

theorem imgZ_append (v w : Word) : imgZ (v ++ w) = imgZ v * imgZ w := by
  induction v with
  | nil => simp [imgZ]
  | cons x v ih => obtain ⟨i, s⟩ := x; simp [imgZ, ih, Matrix.mul_assoc]

theorem img_L : imgZ wL = !![2, 1; 1, 1] := by
  ext a b; fin_cases a <;> fin_cases b <;>
    simp [wL, imgZ, genZ, Matrix.mul_apply, Fin.sum_univ_two]

theorem img_E : imgZ wE = !![0, 1; -1, 0] := by
  ext a b; fin_cases a <;> fin_cases b <;>
    simp [wE, imgZ, genZ, Matrix.mul_apply, Fin.sum_univ_two]

theorem img_Mu : imgZ wMu = !![5, 4; 1, 1] := by
  ext a b; fin_cases a <;> fin_cases b <;>
    simp [wMu, imgZ, genZ, Matrix.mul_apply, Fin.sum_univ_two]

theorem img_Tau : imgZ wTau = !![8, 5; 3, 2] := by
  ext a b; fin_cases a <;> fin_cases b <;>
    simp [wTau, imgZ, genZ, Matrix.mul_apply, Fin.sum_univ_two]

theorem img_Fig8 : imgZ wFig8 = !![5, 3; 3, 2] := by
  rw [wFig8, imgZ_append, img_L]
  ext a b; fin_cases a <;> fin_cases b <;> simp [Matrix.mul_apply, Fin.sum_univ_two]

theorem traces :
    Matrix.trace (imgZ wE) = 0 ∧ Matrix.trace (imgZ wMu) = 6 ∧
    Matrix.trace (imgZ wTau) = 10 ∧ Matrix.trace (imgZ wFig8) = 7 := by
  rw [img_E, img_Mu, img_Tau, img_Fig8]
  simp [Matrix.trace_fin_two]

/-- `τ` is not `μ · 4₁`, nor `4₁ · μ`, in `SL(2, ℤ)`. -/
theorem tau_ne_mu_mul_fig8 :
    imgZ wTau ≠ imgZ wMu * imgZ wFig8 ∧ imgZ wTau ≠ imgZ wFig8 * imgZ wMu := by
  rw [img_Tau, img_Mu, img_Fig8]
  constructor <;> intro h <;>
    have := congrFun (congrFun h 0) 0 <;>
    simp [Matrix.mul_apply, Fin.sum_univ_two] at this

end QOU.Observations.LeptonWordsCatMap
