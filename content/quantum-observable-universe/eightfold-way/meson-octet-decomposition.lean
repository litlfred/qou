import Mathlib.Tactic

/-!
# QOU.Eightfold.MesonOctet — meson-nonet dimension shadow (`3 ⊗ 3̄ = 8 ⊕ 1`)

Backs `prop:meson-octet-decomposition` at the **dimension** level: the
fundamental ⊗ anti-fundamental of `gl_N` (dimension `N²`) splits as the adjoint
(octet, dimension `N² − 1`) ⊕ the singlet (dimension `1`), so at `N = 3` the
meson nonet is `9 = 8 + 1`.

This file proves only the dimension arithmetic — the block's stated
`(9 = 8 + 1)`.  The weight / quantum-number content and the rep-level
Clebsch–Gordan decomposition `𝟑 ⊗ 𝟑̄ = 𝟖 ⊕ 𝟏` are the genuine `SU(3)`
representation-theoretic content argued in the block (a Mathlib gap at the
rep level, like the baryon side in `QOU.Eightfold.RowCapObstruction`).
Bean `qou-8fl1` (T1).

Reference: Georgi, *Lie Algebras in Particle Physics*, §7
(`𝟑 ⊗ 𝟑̄ = 𝟖 ⊕ 𝟏`, adjoint ⊕ singlet).
-/

namespace QOU.Eightfold.MesonOctet

/-- Dimension of the fundamental ⊗ anti-fundamental of `gl_N`: `N · N = N²`. -/
def fundAntifundDim (N : ℕ) : ℕ := N * N

/-- Dimension of the adjoint representation of `su_N` (the traceless part of
    `gl_N`), i.e. `N² − 1`. -/
def adjointDim (N : ℕ) : ℕ := N * N - 1

/-- **Meson-nonet dimension shadow** (general `N ≥ 1`): the fundamental ⊗
    anti-fundamental splits as adjoint ⊕ singlet at the dimension level,
    `N² = (N² − 1) + 1`.  This is `dim(V ⊗ V*) = dim(adjoint) + dim(singlet)`. -/
theorem meson_nonet_dim (N : ℕ) (hN : 1 ≤ N) :
    fundAntifundDim N = adjointDim N + 1 := by
  unfold fundAntifundDim adjointDim
  have h : 0 < N * N := Nat.mul_pos hN hN
  omega

/-- At `N = 3`: `𝟑 ⊗ 𝟑̄ = 𝟖 ⊕ 𝟏` — nonet dimension `9`, octet (adjoint)
    dimension `8`, singlet dimension `1`, with `9 = 8 + 1`. -/
theorem meson_octet_at_three :
    fundAntifundDim 3 = 9 ∧ adjointDim 3 = 8
      ∧ fundAntifundDim 3 = adjointDim 3 + 1 := by
  refine ⟨by decide, by decide, by decide⟩

end QOU.Eightfold.MesonOctet
