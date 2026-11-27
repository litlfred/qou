/-
# The jet is the derivative: `U(1) = 3·lk` for every three-strand word

Analytic half of `QOU.Observations.RingMassLinkingThreeStrand`. For the convention-D Hecke matrices
`r21a`, `r21b` and their inverses `inv21` (`QOU.QBeta.E0WeightCandidates`), the real matrix
function `q ↦ ρ_q(w)` has value `P w` and entrywise derivative `Q w` at `q = 1`
(`hasDerivAt_rhoR`). The ring mass
`m_q(w) = [2]³ q^{−2·wr} ((1 − 2/[2]²) q^{wr} + (1/[2]²) tr ρ_q(w))`
then has value `m0 w = 2^c` and derivative `m1 w` at `q = 1` (`hasDerivAt_massR`). With
`two_mul_m1` this gives `uAtOne_eq`: `U(1) = −m′(1)/m(1) = (3/2)·linkSum w = 3·lk`.
-/
import QOU.Observations.RingMassLinkingThreeStrand
import QOU.Nuclear.E0WeightCandidates
import Mathlib.Analysis.Calculus.Deriv.Inv
import Mathlib.Analysis.Calculus.Deriv.Pow
import Mathlib.Analysis.Calculus.Deriv.Mul
import Mathlib.Analysis.Calculus.Deriv.ZPow
import Mathlib.Tactic

namespace QOU.Transcendental.MassTheory.RingMassLinkingThreeStrand

open QOU.Observations.RingMassLinkingThreeStrand QOU.QBeta.WeightSpaceMarkov
  QOU.QBeta.E0WeightCandidates Matrix

/-- The Hecke matrix of a letter at real `q`. -/
noncomputable def genR (q : ℝ) (l : Letter) : Matrix (Fin 2) (Fin 2) ℝ :=
  if l.first then (if l.pos then r21a q else inv21 q (r21a q))
  else (if l.pos then r21b q else inv21 q (r21b q))

/-- `ρ_q(w)`. -/
noncomputable def rhoR (q : ℝ) : List Letter → Matrix (Fin 2) (Fin 2) ℝ
  | [] => 1
  | l :: w => genR q l * rhoR q w

/-- Integer matrices as real ones. -/
abbrev toR (M : Mat) : Matrix (Fin 2) (Fin 2) ℝ := M.map (Int.cast)

theorem genR_one (l : Letter) : genR 1 l = toR (rho l.gen) := by
  ext i j
  rcases l with ⟨_ | _, _ | _⟩ <;> fin_cases i <;> fin_cases j <;>
    simp [genR, Letter.gen, rho, r21a, r21b, inv21]

theorem hasDerivAt_genR (l : Letter) (i j : Fin 2) :
    HasDerivAt (fun q => genR q l i j) ((l.sgn : ℝ) * (1 : Matrix (Fin 2) (Fin 2) ℝ) i j) 1 := by
  have hinv : HasDerivAt (fun q : ℝ => q⁻¹) (-1) 1 := by
    simpa using hasDerivAt_inv (one_ne_zero : (1 : ℝ) ≠ 0)
  have hid : HasDerivAt (fun q : ℝ => q) 1 1 := hasDerivAt_id 1
  rcases l with ⟨_ | _, _ | _⟩ <;> fin_cases i <;> fin_cases j <;>
    simp [genR, Letter.sgn, r21a, r21b, inv21]
  all_goals first
    | exact hasDerivAt_const _ _
    | exact hid
    | exact hinv
    | simpa using hinv.neg
    | simpa using hinv.neg.sub (hid.sub hinv)

theorem rhoR_one (w : List Letter) : rhoR 1 w = toR (P w) := by
  induction w with
  | nil => ext i j; simp [rhoR, P, Matrix.one_apply]
  | cons l w ih =>
    rw [rhoR, P, ih, genR_one]
    ext i j; simp [toR, Matrix.mul_apply, Fin.sum_univ_two]

/-- **The jet is the derivative**: `∂_q ρ_q(w)|_{q=1} = Q w`, entrywise. -/
theorem hasDerivAt_rhoR (w : List Letter) (i k : Fin 2) :
    HasDerivAt (fun q => rhoR q w i k) ((toR (Q w)) i k) 1 := by
  induction w generalizing i k with
  | nil =>
    simpa [rhoR, Q] using hasDerivAt_const (1 : ℝ) ((1 : Matrix (Fin 2) (Fin 2) ℝ) i k)
  | cons l w ih =>
    have h0 := (hasDerivAt_genR l i 0).mul (ih 0 k)
    have h1 := (hasDerivAt_genR l i 1).mul (ih 1 k)
    have := h0.add h1
    simp only [rhoR, Matrix.mul_apply, Fin.sum_univ_two]
    convert this using 1
    rw [genR_one, rhoR_one]
    simp only [Q, toR, Matrix.map_apply, Matrix.add_apply, Matrix.smul_apply, smul_eq_mul,
      Matrix.mul_apply, Fin.sum_univ_two, Matrix.one_apply, Int.cast_add, Int.cast_mul]
    fin_cases i <;> simp <;> ring

theorem hasDerivAt_traceR (w : List Letter) :
    HasDerivAt (fun q => (rhoR q w).trace) ((Q w).trace : ℝ) 1 := by
  have := (hasDerivAt_rhoR w 0 0).add (hasDerivAt_rhoR w 1 1)
  simp only [Matrix.trace_fin_two]
  convert this using 1
  simp [toR]

/-- The ring mass of `w` at real `q`. -/
noncomputable def massR (w : List Letter) (q : ℝ) : ℝ :=
  (q + q⁻¹) ^ 3 * q ^ (-2 * writhe w) *
    ((1 - 2 / (q + q⁻¹) ^ 2) * q ^ writhe w + 1 / (q + q⁻¹) ^ 2 * (rhoR q w).trace)

theorem massR_one (w : List Letter) : massR w 1 = m0 w := by
  unfold massR m0
  rw [rhoR_one]
  simp [toR, Matrix.trace_fin_two]
  norm_num
  ring

/-- **The ring mass has derivative `m1 w` at `q = 1`.** -/
theorem hasDerivAt_massR (w : List Letter) : HasDerivAt (massR w) (m1 w) 1 := by
  have hb : HasDerivAt (fun q : ℝ => q + q⁻¹) 0 1 := by
    have := (hasDerivAt_id (1 : ℝ)).add (hasDerivAt_inv (one_ne_zero : (1 : ℝ) ≠ 0))
    simpa using this
  have hb3 := hb.pow 3
  have hb2 := hb.pow 2
  have hb2ne : ((1 : ℝ) + 1⁻¹) ^ 2 ≠ 0 := by norm_num
  have hy21 := (hasDerivAt_const (1 : ℝ) (1 : ℝ)).div hb2 hb2ne
  have hy3 := (hasDerivAt_const (1 : ℝ) (1 : ℝ)).sub ((hasDerivAt_const (1 : ℝ) (2 : ℝ)).div hb2 hb2ne)
  have hz := hasDerivAt_zpow (-2 * writhe w) (1 : ℝ) (Or.inl one_ne_zero)
  have hzw := hasDerivAt_zpow (writhe w) (1 : ℝ) (Or.inl one_ne_zero)
  have ht := hasDerivAt_traceR w
  have := (hb3.mul hz).mul ((hy3.mul hzw).add (hy21.mul ht))
  unfold massR
  convert this using 1
  simp [toR, Matrix.trace_fin_two, m1, rhoR_one]
  push_cast
  ring

/-- **`U(1) = −m′(1)/m(1) = (3/2)·linkSum = 3·lk`** for every three-strand word. -/
theorem uAtOne_eq (w : List Letter) :
    -(deriv (massR w) 1) / massR w 1 = 3 / 2 * (linkSum w : ℝ) := by
  rw [(hasDerivAt_massR w).deriv, massR_one]
  have h2 := two_mul_m1 w
  have hpos : (0 : ℝ) < m0 w := by
    rw [m0_eq]; push_cast; positivity
  rw [div_eq_iff hpos.ne']
  have : (2 : ℝ) * m1 w = -3 * m0 w * linkSum w := by exact_mod_cast h2
  linarith

end QOU.Transcendental.MassTheory.RingMassLinkingThreeStrand
