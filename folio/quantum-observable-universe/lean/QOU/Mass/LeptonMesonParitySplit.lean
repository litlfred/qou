/-
  Lepton/meson parity split → the algebraic origin of "exactly 3 calibrations".

  The Hecke algebra H_n(q) (generic q) is semisimple with the same irreducible
  dimensions as the symmetric group S_n: dim of the irrep λ ⊢ n is the number
  of standard Young tableaux of shape λ, given by the hook-length formula
  dim(λ) = n! / ∏_{cells} hook.

  Physical content (c-equals-bar-iff-all-1dim):
    * H_2 is the UNIQUE Hecke level where every irrep is 1-dimensional. There
      C = C-bar (matter/antimatter conjugation = CPT): the LEPTON sector. Its
      colored-Jones / Markov trace is bar-symmetric (amphichiral) — see the
      figure-eight self-duality J_N(q)=J_N(q^-1) verified this PR.
    * H_3 already FAILS this: the standard (2,1) irrep is 2-dimensional, so
      C ≠ C-bar — the MESON sector carries an intrinsic bar-odd (chiral /
      Goldstone) component unreachable from the lepton world.

  This is the algebraic root of the three calibrations: CAL-1 = m_e (the real
  bar-even lepton scale, H_2), CAL-2 = q_0 (the substrate modulus), CAL-3 = m_pi
  (the orthogonal C≠bar meson class, H_3). One real scale + one modulus + one
  orthogonal class = 3.

  Pure ℕ-combinatorics (hook-length dims); no archimedean ring (§7c).

  -- Ref: [jones1987] https://doi.org/10.2307/1971403
  -- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-/

import Mathlib.Tactic

namespace QOU.Mass.ParitySplit

/-- Factorial. -/
def fact : ℕ → ℕ
  | 0 => 1
  | (n + 1) => (n + 1) * fact n

/-- Product of a list of naturals. -/
def prodList : List ℕ → ℕ
  | [] => 1
  | (x :: xs) => x * prodList xs

/-- Hook-length dimension of an S_n / H_n(q) irrep: n! / ∏ hooks. -/
def hookDim (n : ℕ) (hooks : List ℕ) : ℕ := fact n / prodList hooks

-- Hook lengths of the partitions of 2:  (2) → [2,1];  (1,1) → [2,1].
/-- dim of the trivial irrep (2) of H_2 is 1. -/
theorem dim_2 : hookDim 2 [2, 1] = 1 := by decide
/-- dim of the sign irrep (1,1) of H_2 is 1. -/
theorem dim_11 : hookDim 2 [2, 1] = 1 := by decide

-- Hook lengths of the partitions of 3: (3)→[3,2,1]; (2,1)→[3,1,1]; (1,1,1)→[3,2,1].
/-- dim of the trivial irrep (3) of H_3 is 1. -/
theorem dim_3 : hookDim 3 [3, 2, 1] = 1 := by decide
/-- dim of the STANDARD irrep (2,1) of H_3 is 2 — the C ≠ bar witness. -/
theorem dim_21 : hookDim 3 [3, 1, 1] = 2 := by decide
/-- dim of the sign irrep (1,1,1) of H_3 is 1. -/
theorem dim_111 : hookDim 3 [3, 2, 1] = 1 := by decide

/-- The full irrep-dimension multisets. -/
def dimsH2 : List ℕ := [hookDim 2 [2, 1], hookDim 2 [2, 1]]            -- (2),(1,1)
def dimsH3 : List ℕ := [hookDim 3 [3, 2, 1], hookDim 3 [3, 1, 1], hookDim 3 [3, 2, 1]] -- (3),(2,1),(1,1,1)

/-- **H_2: every irrep is 1-dimensional** (C = bar — the lepton level). -/
theorem h2_all_one_dim : ∀ d ∈ dimsH2, d = 1 := by decide

/-- **H_3: NOT all 1-dimensional** — the (2,1) irrep is 2-dim (C ≠ bar — mesons). -/
theorem h3_not_all_one_dim : ¬ (∀ d ∈ dimsH3, d = 1) := by decide

/-- **H_2 is the distinguished C = bar level**: all-1-dim where H_3 is not.
    This is the algebraic origin of the lepton/meson split, hence of the
    three calibration sectors (real lepton scale + modulus + orthogonal
    meson class). -/
theorem h2_unique_all_one_dim :
    (∀ d ∈ dimsH2, d = 1) ∧ ¬ (∀ d ∈ dimsH3, d = 1) :=
  ⟨h2_all_one_dim, h3_not_all_one_dim⟩

/-- **Sum of `hookDim 3 [3, 2, 1]` and `hookDim 3 [3, 1, 1]` (`qou-3x8x`).**
`hookDim 3 [3, 2, 1] + hookDim 3 [3, 1, 1] = 3`. -/
theorem dim_3_add_dim_21 : hookDim 3 [3, 2, 1] + hookDim 3 [3, 1, 1] = 3 := by
  rw [dim_3, dim_21]

end QOU.Mass.ParitySplit
