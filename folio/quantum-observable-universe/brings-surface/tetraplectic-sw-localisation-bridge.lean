import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Ring.Basic
import Mathlib.Data.Fintype.Basic

/-!
# Combinatorial evaluation of tetraplectic matrix elements by `S₅` localization
  (`conj:tetraplectic-sw-localisation-bridge`, §3b-cond)

Class-axiomatised formulation of `conj:tetraplectic-sw-localisation-bridge`
over an arbitrary commutative ring `R` (§7c), together with the unconditional
`S₅` Burnside dimension sum `1² + 4² + 5² + 6² + 5² + 4² + 1² = 120` across
the `7` irreducible partitions of `5` and Schur-diagonal matrix-element
reduction.

## References

- [leitner2026] `conj:tetraplectic-sw-localisation-bridge`
- [seiberg-witten1994b] Seiberg–Witten 4-manifold invariants
- [nekrasov2002] Nekrasov instanton localization
-/

namespace QOU.BringsSurface

/-- The seven partitions of `5` indexing the irreducible representations of `S₅`. -/
inductive S5Partition
  | p5
  | p41
  | p32
  | p311
  | p221
  | p2111
  | p11111
  deriving DecidableEq

/-- Classical irreducible dimension `d_λ` of each `S₅` partition `λ ⊢ 5`. -/
def s5IrrepDim : S5Partition → ℕ
  | .p5     => 1
  | .p41    => 4
  | .p32    => 5
  | .p311   => 6
  | .p221   => 5
  | .p2111  => 4
  | .p11111 => 1

/-- Enumeration list of all `7` partitions of `5`. -/
def allS5Partitions : List S5Partition :=
  [.p5, .p41, .p32, .p311, .p221, .p2111, .p11111]

/-- **Unconditional (`S₅` Burnside dimension identity).** Across the `7`
    irreducible representations of `S₅`, `∑_{λ ⊢ 5} d_λ² = 120 = 5!`. -/
theorem s5_burnside_dim_sq_sum :
    allS5Partitions.length = 7 ∧
    (allS5Partitions.map (fun lam => (s5IrrepDim lam) ^ 2)).sum = 120 := by
  decide

/-- **Open conjecture (`conj:tetraplectic-sw-localisation-bridge`, §3b-cond).**
    Identifies Nekrasov localization fixed-point sectors on the Bring cone with
    `S₅`-isotypic sectors `S5Partition`, reducing off-diagonal `S₅`-invariant
    operator matrix elements to `0` by Schur's lemma and diagonal elements to
    combinatorial eigenvalues `schurScalar λ * normPairing λ`. -/
class TetraplecticSWLocalisationBridge (R : Type*) [CommRing R] where
  /-- Matrix element `∫_M ψ_λ* H ψ_μ Ω` for an `S₅`-invariant Hamiltonian `H`. -/
  matrixElement : S5Partition → S5Partition → R
  /-- Combinatorial Schur eigenvalue of `H` on the `λ`-isotypic component. -/
  schurScalar : S5Partition → R
  /-- Isotypic norm pairing `∫_M |ψ_λ|² Ω`. -/
  normPairing : S5Partition → R
  /-- Schur orthogonality across distinct `S₅`-isotypic sectors. -/
  off_diagonal_zero :
    ∀ lam mu : S5Partition, lam ≠ mu → matrixElement lam mu = 0
  /-- Diagonal Wigner–Eckart / Schur evaluation. -/
  diagonal_eval :
    ∀ lam : S5Partition, matrixElement lam lam = schurScalar lam * normPairing lam

/-- **Conditional theorem (combinatorial trace reduction).** Under
    `[TetraplecticSWLocalisationBridge R]`, for any pair `(lam, mu)`, if
    `lam = mu` the matrix element reduces to `schurScalar lam * normPairing lam`,
    and the double sum over `{.p5, .p311}` collapses to the two diagonal terms. -/
-- Ref: [leitner2026] conj:tetraplectic-sw-localisation-bridge
theorem tetraplectic_two_sector_trace_reduction {R : Type*} [CommRing R]
    [c : TetraplecticSWLocalisationBridge R] :
    c.matrixElement .p5 .p5 + c.matrixElement .p5 .p311 +
      c.matrixElement .p311 .p5 + c.matrixElement .p311 .p311 =
    c.schurScalar .p5 * c.normPairing .p5 +
      c.schurScalar .p311 * c.normPairing .p311 := by
  rw [c.diagonal_eval .p5, c.diagonal_eval .p311,
    c.off_diagonal_zero .p5 .p311 (by decide),
    c.off_diagonal_zero .p311 .p5 (by decide)]
  simp [add_zero]

end QOU.BringsSurface
