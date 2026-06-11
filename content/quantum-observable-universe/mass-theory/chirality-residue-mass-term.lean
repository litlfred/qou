import Mathlib.Algebra.Algebra.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Finset.Basic


/-!
# Chirality / non-chirality split of the mass tower

By partitioning the unified curvature-rank mass tower by the
signed-content predicate `c_λ = 0` (chirality) vs `c_λ ≠ 0`
(non-chirality), every stratum decomposes:

  𝔪_{q,K}(T) = 𝔪^chir_{q,K}(T) + 𝔪^¬chir_{q,K}(T).

The chirality cells are exactly those Wedderburn blocks satisfying
`D_q²(λ) = 0` in the q-Dirac cell scanner — the gauge-invariant
background per `prop:confinement-categorical`.

-- Ref: [manuscript] prop:chirality-residue-mass-term
-/

namespace QOU.WedderburnMass

/-- Signed Young content of a partition `λ`: `c_λ = Σ_{(i,j) ∈ λ}(j − i)`. -/
def signed_content (lam : List ℕ) : ℤ :=
  (List.range lam.length).foldl (fun acc i =>
    let row_len := lam.get? i |>.getD 0
    acc + (List.range row_len).foldl (fun a j =>
      a + (j : ℤ) - (i : ℤ)) 0) 0

/-- Chirality predicate: `c_λ = 0`. -/
def is_chirality (lam : List ℕ) : Prop :=
  signed_content lam = 0

/-- **Mass tower split.**  For any predicate `P` on partitions, the
    mass tower decomposes as the sum over `P λ` plus the sum over
    `¬ P λ`.  When `P = is_chirality`, this gives the chirality /
    non-chirality split. -/
theorem mass_tower_split_by_predicate
    {R : Type*} [CommRing R]
    (n : ℕ) (P : List ℕ → Prop) [DecidablePred P]
    (alpha : ℕ → R) (m_lambda : List ℕ → R)
    (parts : Finset (List ℕ)) :
    ∑ λ ∈ parts, alpha (λ.length - 1) * m_lambda λ
      =
    ∑ λ ∈ parts.filter P, alpha (λ.length - 1) * m_lambda λ
    + ∑ λ ∈ parts.filter (fun λ => ¬ P λ), alpha (λ.length - 1) * m_lambda λ
    := by
  -- Ref: [manuscript] prop:chirality-residue-mass-term, Step 1.
  -- Structural refinement; no analytic content beyond the unified
  -- mass formula proposition.
  simpa using
    (Finset.sum_filter_add_sum_filter_not
      (s := parts)
      (p := P)
      (f := fun lam => alpha (lam.length - 1) * m_lambda lam)).symm

/-- **Chirality residue is the predicate split with `P = is_chirality`.** -/
def chirality_residue
    {R : Type*} [CommRing R]
    (alpha : ℕ → R) (m_lambda : List ℕ → R)
    (parts : Finset (List ℕ)) : R :=
  ∑ λ ∈ parts.filter (fun λ => signed_content λ = 0),
    alpha (λ.length - 1) * m_lambda λ

end QOU.WedderburnMass
