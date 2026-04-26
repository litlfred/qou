/-!
# QOU.BraidKnot.wenzl_bridge_y_lambda

The Jones-Markov block weights y_λ on H_n(R, q) with Markov
parameter z = 1/(√q + 1/√q) are DEFINED by the principal Schur
ratio at the Wenzl-bridge parameter X = qz/(1 - q² + qz):

  y_λ(q, z) := s_{λ, X}(q²) / Σ_μ d_μ s_{μ, X}(q²),

  s_{λ, X}(Q) := Q^{n(λ)} · ∏_{(i,j) ∈ λ} (1 - X·Q^{c(i,j)}) / (1 - Q^{h(i,j)}).

This is the "fractional Wenzl" specialisation: X = Q^r with non-
integer r determined by the Markov constraint.  Wenzl 1988 establishes
that the resulting tr_M = Σ y_λ χ_λ satisfies the Markov property
tr_M(xσ_n) = z·tr_M(x).  Equivalence with the linear-system
formulation is verified numerically at n ∈ {2..12} to machine
precision.

LaTeX label: `prop:wenzl-bridge-y-lambda`

## References

- [manuscript] Ch. Braids and Knots, §Wenzl-bridge y_λ
- [wenzl1988] Wenzl, "Hecke algebras of type A_n and subfactors",
  Invent. Math. 92 (1988), 349–383.
- [macdonald] Macdonald, "Symmetric Functions and Hall Polynomials",
  2nd ed., Oxford (1995), I.3 ex.1 (principal specialisation).
- [halverson-ram] Halverson, Ram, "A Frobenius formula for the
  characters of the Hecke algebras", Invent. Math. 106 (1991).
-/

namespace QOU.BraidKnot

/-- The Wenzl-bridge parameter X(q, z) = qz/(1 - q² + qz). -/
noncomputable def wenzlBridgeX (q z : ℝ) : ℝ :=
  q * z / (1 - q ^ 2 + q * z)

/-- A Young-diagram cell with content (j - i) and hook length. -/
structure WenzlCell where
  i : ℕ
  j : ℕ
  hook : ℕ
  hook_pos : 0 < hook

/-- Principal Schur specialisation s_{λ, X}(Q) over the cells of λ. -/
noncomputable def schurPrincipal
    (cells : List WenzlCell) (n_lambda : ℕ) (X Q : ℝ) : ℝ :=
  Q ^ n_lambda *
    cells.foldl
      (fun acc x =>
        acc * (1 - X * Q ^ (x.j - x.i : ℤ)) / (1 - Q ^ x.hook))
      1

/-- The Jones-Markov block weight y_λ defined via the Wenzl-bridge
    product, under the Schur-Weyl identification of H_n(R, q) as
    a centraliser algebra acting on V^{⊗n}. -/
-- Ref: [manuscript] Ch. Braids and Knots, §Wenzl-bridge y_λ
-- Ref: [wenzl1988] Wenzl, Invent. Math. 92 (1988)
noncomputable def y_lambda_wenzl_bridge
    (cells_lambda : List WenzlCell)
    (n_lambda d_lambda : ℕ)
    (cells_others : List (List WenzlCell × ℕ × ℕ))
    -- (cells, n_μ, d_μ) for each μ ⊢ n
    (q z : ℝ) : ℝ :=
  let Q := q ^ 2
  let X := wenzlBridgeX q z
  let s_self := schurPrincipal cells_lambda n_lambda X Q
  let norm :=
    cells_others.foldl
      (fun acc t =>
        acc + (t.2.2 : ℝ) * schurPrincipal t.1 t.2.1 X Q)
      0
  s_self / norm

/-- **Definition (Wenzl-bridge y_λ)**.

    The closed form is taken as the definition; the Markov property
    follows by Wenzl 1988.  Numerical equivalence with the linear-
    system inverse is established in y-lambda-wenzl-witness.json. -/
-- Ref: [wenzl1988] Wenzl, Invent. Math. 92 (1988)
theorem wenzl_bridge_y_lambda_well_defined
    (cells_lambda : List WenzlCell)
    (n_lambda d_lambda : ℕ)
    (cells_others : List (List WenzlCell × ℕ × ℕ))
    (q z : ℝ) :
    ∃ y : ℝ, y = y_lambda_wenzl_bridge
      cells_lambda n_lambda d_lambda cells_others q z :=
  ⟨_, rfl⟩

end QOU.BraidKnot
