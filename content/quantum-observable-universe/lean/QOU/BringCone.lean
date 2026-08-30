import Mathlib.Algebra.Quaternion
import Mathlib.Tactic.Ring

/-!
# Tetraplectic geometry of the Bring cone — the Reeb quaternionic twist

The affine cone of Bring's curve is a real 4-manifold; its 3-dimensional link
carries a 3-Sasakian (degenerate quaternionic-contact) structure whose Reeb
triad is modelled here on the quaternion algebra `Quaternion R`.

We take the three Reeb operators to be **right-multiplication** by the
imaginary units `i, j, k`.  Right-multiplication is used (rather than left) so
that the operators generate the correct `𝔰𝔲(2)` bracket with a `+2` structure
constant:

`[M_i, M_j] p = (p·i)·j − (p·j)·i = p·(ij) − p·(ji) = p·k − p·(−k) = 2·(p·k)`.

The three `reeb_twist_*` lemmas below discharge exactly this bracket
(`[M_i,M_j] = 2·M_k` and cyclic).  These are **pure quaternion-algebra
identities** — no ordering, radical, or other archimedean construct is used —
so per the §7c base-ring convention they are stated over a generic
`{R : Type*} [CommRing R]`, with `BringCone` naming the geometric object.  The
archimedean specialization `Quaternion ℝ` for the actual quaternionic-contact
geometry is left to the consumer; nothing here forces `Mathlib.Data.Real.Basic`
into the dependency cone.

Reference for the geometric interpretation (Reeb quaternionic twist on the
quaternionic-contact link): [manuscript] `lem:bring-cone-reeb-quaternionic-twist`
(brings-surface §Spectral resolvents and gauge structures), with the SU(2)
reading and its scope limits in `rem:tetraplectic-su2-gauge-reading`.
-/

namespace QOU.Tetraplectic

variable {R : Type*} [CommRing R]

/-- The tetraplectic Bring cone, modelled on the quaternions over `R`. -/
abbrev BringCone (R : Type*) [CommRing R] := Quaternion R

/-- Reeb operator `M_i` — right-multiplication by the quaternionic unit `i`. -/
def reebM_i (p : BringCone R) : BringCone R := p * ⟨0, 1, 0, 0⟩
/-- Reeb operator `M_j` — right-multiplication by the quaternionic unit `j`. -/
def reebM_j (p : BringCone R) : BringCone R := p * ⟨0, 0, 1, 0⟩
/-- Reeb operator `M_k` — right-multiplication by the quaternionic unit `k`. -/
def reebM_k (p : BringCone R) : BringCone R := p * ⟨0, 0, 0, 1⟩

/-- Quaternionic twist `[M_i, M_j] = 2·M_k`. -/
theorem reeb_twist_ij (p : BringCone R) :
    reebM_j (reebM_i p) - reebM_i (reebM_j p) = (2 : R) • reebM_k p := by
  dsimp [reebM_i, reebM_j, reebM_k]
  ext <;> simp <;> ring

/-- Quaternionic twist `[M_j, M_k] = 2·M_i`. -/
theorem reeb_twist_jk (p : BringCone R) :
    reebM_k (reebM_j p) - reebM_j (reebM_k p) = (2 : R) • reebM_i p := by
  dsimp [reebM_i, reebM_j, reebM_k]
  ext <;> simp <;> ring

/-- Quaternionic twist `[M_k, M_i] = 2·M_j`. -/
theorem reeb_twist_ki (p : BringCone R) :
    reebM_i (reebM_k p) - reebM_k (reebM_i p) = (2 : R) • reebM_j p := by
  dsimp [reebM_i, reebM_j, reebM_k]
  ext <;> simp <;> ring

end QOU.Tetraplectic
