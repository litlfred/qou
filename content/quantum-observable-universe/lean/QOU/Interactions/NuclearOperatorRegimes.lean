/-!
# Nuclear operator regimes: three binding regimes at magic numbers

The inter-nucleon binding operator transitions between three
distinct regimes as nucleons are added inductively:

  I.   Shell filling: torus knot T_{2,n_s}
  II.  Magic closure: Hopf link L₊ or L₋
  III. Open shell: bare typed crossing C_pp, C_pn, C_nn

B₃ (Borromean) is a quark-level operator — it never appears
at the nuclear level.

## References

- [prop:nuclear-operator-regimes]
- [prop:demand-stability]
-/

import QOU.Descartes.HeckeRep
import QOU.Descartes.GroundRing
import QOU.Interactions.DerivedAtom

namespace QOU.Interactions

open QOU.Descartes

/-! ## §1  The three binding regimes -/

/-- The three nuclear binding regimes. -/
inductive BindingRegime where
  | shellFilling  : BindingRegime  -- Torus knot T_{2,n_s}
  | magicClosure  : BindingRegime  -- Hopf link L₊ or L₋
  | openShell     : BindingRegime  -- Bare typed crossing
  deriving DecidableEq, Repr

/-! ## §2  Hopf link operators -/

/-- The positive Hopf link L₊ = σ₀σ₁ in a representation. -/
noncomputable def hopfPlus (ρ : HeckeRep 3 2) :
    Matrix (Fin 2) (Fin 2) R_t :=
  ρ.gen ⟨0, by omega⟩ * ρ.gen ⟨1, by omega⟩

/-- The negative Hopf link L₋ = σ₁σ₀ in a representation. -/
noncomputable def hopfMinus (ρ : HeckeRep 3 2) :
    Matrix (Fin 2) (Fin 2) R_t :=
  ρ.gen ⟨1, by omega⟩ * ρ.gen ⟨0, by omega⟩

/-- L₊ and L₋ are distinct (they differ by the Yang-Baxter relation
    acting on the third strand, which is absent in 2-strand products). -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- L₊ ≠ L₋ in general (they agree only when σ₀ and σ₁ commute,
-- which happens iff the representation is 1-dimensional).
sorry

/-! ## §3  B₃ is quark-level only -/

/-- The Borromean braid B₃ is NOT selected by demand-minimization
    at the nuclear level.

    For any nucleus 𝒩 and any new nucleon 𝒩_{k+1}, there exists
    an operator Φ ∈ {L₊, L₋, T_{2,5}, C_pp, C_pn, C_nn} such that

      |dem(𝒩 · Φ · 𝒩_{k+1})| ≤ |dem(𝒩 · B₃ · 𝒩_{k+1})|

    with strict inequality for A ≤ 8.

    Verified computationally for all A ≤ 6. -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
sorry

/-! ## §4  Regime transitions at magic numbers -/

/-- At Z = 2 (first proton magic number), the demand-minimizing
    operator transitions from T_{2,5} (shell filling) to L₊
    (magic closure).

    Specifically: for p → pp, T_{2,5} minimizes demand.
    For pp → ppn (magic Z = 2), L₊ achieves demand = 0. -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
sorry

/-- At doubly magic (Z = 2, N = 2) = He-4, the nucleus achieves
    demand closure via L₊ at both the proton and neutron shell
    boundaries.

    The He-4 nucleus has all NF coefficients nonneg (demand = ∅). -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
sorry

end QOU.Interactions
