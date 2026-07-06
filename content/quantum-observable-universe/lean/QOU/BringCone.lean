import Mathlib.Algebra.Quaternion
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring

/-!
# Tetraplectic geometry of the Bring cone — the Reeb quaternionic twist

The affine cone of Bring's curve is a real 4-manifold; its 3-dimensional link
carries a 3-Sasakian (degenerate quaternionic-contact) structure whose Reeb
triad is modelled here on the real quaternion algebra `Quaternion ℝ`.

We take the three Reeb operators to be **right-multiplication** by the
imaginary units `i, j, k`.  Right-multiplication is used (rather than left) so
that the operators generate the correct `𝔰𝔲(2)` bracket with a `+2` structure
constant:

`[M_i, M_j] p = (p·i)·j − (p·j)·i = p·(ij) − p·(ji) = p·k − p·(−k) = 2·(p·k)`.

The three `reeb_twist_*` lemmas below discharge exactly this bracket
(`[M_i,M_j] = 2·M_k` and cyclic).  These are ordinary quaternion-algebra
identities — no manifold/measure theory is invoked, so the file imports only
`Mathlib.Algebra.Quaternion` plus `ring`.

Reference for the geometric interpretation (Reeb quaternionic twist on the
quaternionic-contact link): [manuscript] `bring_tetraplectic.md` §4.
-/

namespace QOU.Tetraplectic

/-- The tetraplectic Bring cone, modelled on the real quaternions. -/
abbrev BringCone : Type := Quaternion ℝ

/-- Reeb operator `M_i` — right-multiplication by the quaternionic unit `i`. -/
def reebM_i (p : BringCone) : BringCone := p * ⟨0, 1, 0, 0⟩
/-- Reeb operator `M_j` — right-multiplication by the quaternionic unit `j`. -/
def reebM_j (p : BringCone) : BringCone := p * ⟨0, 0, 1, 0⟩
/-- Reeb operator `M_k` — right-multiplication by the quaternionic unit `k`. -/
def reebM_k (p : BringCone) : BringCone := p * ⟨0, 0, 0, 1⟩

/-- Quaternionic twist `[M_i, M_j] = 2·M_k`. -/
theorem reeb_twist_ij (p : BringCone) :
    reebM_j (reebM_i p) - reebM_i (reebM_j p) = (2 : ℝ) • reebM_k p := by
  dsimp [reebM_i, reebM_j, reebM_k]
  ext <;> simp <;> ring

/-- Quaternionic twist `[M_j, M_k] = 2·M_i`. -/
theorem reeb_twist_jk (p : BringCone) :
    reebM_k (reebM_j p) - reebM_j (reebM_k p) = (2 : ℝ) • reebM_i p := by
  dsimp [reebM_i, reebM_j, reebM_k]
  ext <;> simp <;> ring

/-- Quaternionic twist `[M_k, M_i] = 2·M_j`. -/
theorem reeb_twist_ki (p : BringCone) :
    reebM_i (reebM_k p) - reebM_k (reebM_i p) = (2 : ℝ) • reebM_j p := by
  dsimp [reebM_i, reebM_j, reebM_k]
  ext <;> simp <;> ring

end QOU.Tetraplectic
