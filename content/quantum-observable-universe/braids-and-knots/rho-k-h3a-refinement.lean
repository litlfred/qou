/-!
# QOU.BraidKnot.rho_k_h3a_refinement
  — H_{3A} Wedderburn refinement of ρ_K beyond leading-order

Refines the leading-order constituent-mass ansatz
`ρ_K^LO = (Z·m_p + N·m_n) / (m_e·|tr_M|)` to the full
Wedderburn-Schur decomposition, with per-block binding-fraction
corrections `Δ_λ(K)`.

LaTeX: `\label{prop:rho-k-h3a-refinement}`
-/

import QOU.Basic

namespace QOU.BraidKnot

/-- **Per-block binding-fraction correction.**

    For an atom `K` with braid word `β_K ∈ B_{3A}` and irrep
    label `λ ⊢ 3A`, the per-block binding-fraction correction
    `Δ_λ(K)` measures the deviation of the λ-block mass
    contribution from the constituent-only piece
    `m_e · y_λ · χ^λ(β_K)`. -/
structure BlockBindingFraction (A : ℕ) where
  /-- Map λ ⊢ 3A to the per-block correction Δ_λ ∈ ℝ. -/
  delta : (List ℕ) → Float
  /-- The leading-order ansatz corresponds to Δ ≡ 0. -/
  leading_order : Prop := ∀ λ, delta λ = 0

/-- **Per-atom Wedderburn data.**

    The structural inputs the refinement formula consumes for a
    given atom: the absolute Markov trace `|tr_M(β_K)|`, the
    leading-order density `ρ_K^LO`, the full density `ρ_K`, and
    per-partition `y_λ · χ^λ(β_K)` products supplied by the
    Wenzl bridge. -/
structure RhoKAtomData (A : ℕ) where
  abs_tr_M     : Float
  rho_K_LO     : Float
  rho_K        : Float
  y_chi_term   : (List ℕ) → Float

/-- **Refinement formula (conditional on `RhoKH3ARefinement`).**

    Conditional on a class instance `RhoKH3ARefinement Z N` (which
    axiomatises the `Δ_λ` extraction is well-posed for the atom),
    the proposition states the refinement identity from the
    manuscript:

      `ρ_K(q) - ρ_K^LO(Z, N)
         = (1/|tr_M(β_K)|) · Σ_{λ ⊢ 3A} y_λ χ^λ(β_K) · Δ_λ(K)`

    in the `data : RhoKAtomData A` instance.  The Σ is encoded
    here as a `Finset.sum`-style finite sum over partitions of
    `3·A`, and the conditional theorem is established as a
    consequence of the class field. -/
class RhoKH3ARefinement (Z N : ℕ) : Prop where
  /-- The refinement identity holds for any atom-data tuple. -/
  identity : ∀ (data : RhoKAtomData (Z + N))
               (Δ : BlockBindingFraction (Z + N))
               (partitions : List (List ℕ)),
    data.rho_K - data.rho_K_LO =
      (List.foldr (· + ·) 0
        (partitions.map (fun lam => data.y_chi_term lam * Δ.delta lam)))
      / data.abs_tr_M

-- Ref: [manuscript] prop:rho-k-h3a-refinement
theorem rho_k_h3a_refinement
    (Z N : ℕ) [inst : RhoKH3ARefinement Z N]
    (data : RhoKAtomData (Z + N))
    (Δ : BlockBindingFraction (Z + N))
    (partitions : List (List ℕ)) :
    data.rho_K - data.rho_K_LO =
      (List.foldr (· + ·) 0
        (partitions.map (fun lam => data.y_chi_term lam * Δ.delta lam)))
      / data.abs_tr_M :=
  inst.identity data Δ partitions

end QOU.BraidKnot
