import Mathlib.LinearAlgebra.Matrix.Symmetric
import Mathlib.LinearAlgebra.Matrix.Notation

/-!
# QOU.Archimedean.frobenius_gram_matrix — explicit Markov-Frobenius Gram matrix

**Proposition** ([`prop:frobenius-gram-matrix`](../../../quantum-observable-universe/archimedean-universe/frobenius-gram-matrix.md)).

*The `6 × 6` Gram matrix `G_{ij} = tr_M(b_i · b_j)` over the NF basis
`{γ, σ₀, σ₁, L₊, L₋, e⁻}` in `H₃(q)` is the symmetric matrix*

```
G =
  ⎛ 1    z    z    z²    z²    z³ ⎞
  ⎜ z   hz+1  z²  hz²+z  z³   g₁₅ ⎟
  ⎜ z   z²  hz+1  z³   hz²+z  g₁₅ ⎟
  ⎜ z² hz²+z  z³  g₁₅   g₃₄   g₃₅ ⎟
  ⎜ z²  z³  hz²+z g₃₄   g₁₅   g₃₅ ⎟
  ⎝ z³ g₁₅  g₁₅  g₃₅   g₃₅   g₅₅ ⎠
```

*where (using `h = q − q⁻¹` for the Hecke parameter and `z` for the
Markov parameter `z = 1/(q^{1/2} + q^{−1/2})`)*

```
g₁₅ = h·z³ + z²
g₃₄ = h·z³ + h·z + 1
g₃₅ = h²·z³ + 2h·z² + z
g₅₅ = (h³ + h)·z³ + 2h²·z² + 2h·z + 1
```

The Lean side records the matrix as an explicit
`Matrix (Fin 6) (Fin 6) R` over a generic ring `R` carrying two
distinguished elements `h, z` (the Hecke and Markov parameters
respectively).  Three immediate facts are stated:

  1. The matrix is symmetric (`Matrix.IsSymm`).
  2. The (0, 0) entry is `1` (Markov-trace of the identity).
  3. The full matrix is recorded as a top-level `def`.

Each of (1) and (2) is a concrete equality discharged by direct
computation (`decide`/`rfl`/`ring`); the symmetry is by definition of
the matrix entries.

-- Ref: [leitner2026] quantum-observable-universe/archimedean-universe/frobenius-gram-matrix.md
-/

namespace QOU.Archimedean

open Matrix

variable {R : Type*} [CommRing R] (h z : R)

/-- The Markov–Frobenius `6 × 6` Gram matrix on the NF basis
    `{γ, σ₀, σ₁, L₊, L₋, e⁻}` of `H₃(q)`, parameterised by
    `h = q − q⁻¹` (Hecke parameter) and `z = 1 / (q^{1/2} + q^{−1/2})`
    (Markov parameter).  Entries are polynomial in `h` and `z`.

    See [`prop:frobenius-gram-matrix`] for the categorical
    derivation; entries are read off the Skein decomposition of
    each product `b_i · b_j` plus the Markov-trace evaluation. -/
noncomputable def frobeniusGramMatrix : Matrix (Fin 6) (Fin 6) R :=
  let g15 := h * z ^ 3 + z ^ 2
  let g34 := h * z ^ 3 + h * z + 1
  let g35 := h ^ 2 * z ^ 3 + 2 * h * z ^ 2 + z
  let g55 := (h ^ 3 + h) * z ^ 3 + 2 * h ^ 2 * z ^ 2 + 2 * h * z + 1
  !![ 1,           z,           z,           z ^ 2,       z ^ 2,       z ^ 3 ;
      z,           h * z + 1,   z ^ 2,       h * z ^ 2 + z, z ^ 3,     g15   ;
      z,           z ^ 2,       h * z + 1,   z ^ 3,       h * z ^ 2 + z, g15 ;
      z ^ 2,       h * z ^ 2 + z, z ^ 3,     g15,         g34,         g35   ;
      z ^ 2,       z ^ 3,       h * z ^ 2 + z, g34,       g15,         g35   ;
      z ^ 3,       g15,         g15,         g35,         g35,         g55   ]

/-- **Top-left entry**: `G[0,0] = tr_M(γ · γ) = tr_M(1) = 1`.

    This is the Markov-trace normalisation `tr_M(1) = 1`, recorded
    here as a direct entry of the matrix. -/
-- Ref: [leitner2026] quantum-observable-universe/archimedean-universe/frobenius-gram-matrix.md
theorem frobeniusGramMatrix_zero_zero :
    (frobeniusGramMatrix h z : Matrix (Fin 6) (Fin 6) R) 0 0 = 1 := by
  simp [frobeniusGramMatrix]

/-- **Matrix symmetry**: the Gram matrix is symmetric, reflecting the
    Frobenius-pairing property `tr_M(a · b) = tr_M(b · a)` (Markov-
    trace cyclicity).

    Each off-diagonal pair is identical by construction, so the
    proof is by index-case analysis. -/
-- Ref: [leitner2026] quantum-observable-universe/archimedean-universe/frobenius-gram-matrix.md
theorem frobeniusGramMatrix_isSymm :
    (frobeniusGramMatrix h z : Matrix (Fin 6) (Fin 6) R).IsSymm := by
  ext i j
  fin_cases i <;> fin_cases j <;> rfl

/-- **Proposition** (statement bundle):
    The matrix is well-defined and the (0, 0) entry coincides with
    `1` (Markov-trace normalisation). -/
-- Ref: [leitner2026] quantum-observable-universe/archimedean-universe/frobenius-gram-matrix.md
theorem frobenius_gram_matrix :
    (frobeniusGramMatrix h z : Matrix (Fin 6) (Fin 6) R) 0 0 = 1 :=
  frobeniusGramMatrix_zero_zero h z

end QOU.Archimedean
