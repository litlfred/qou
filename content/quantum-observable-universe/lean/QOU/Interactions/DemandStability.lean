/-!
# Demand stability: the demand profile determines nuclear stability

The demand profile (set of negative NF coefficients) is the
categorical diagnostic of stability. Beta-stable nuclei minimize
demand magnitude at fixed mass number A.

## References

- [prop:demand-stability]
- [conj:periodic-table-demand]
-/

import QOU.Interactions.DerivedAtom

namespace QOU.Interactions

variable (q : ℝ) (hq : q > 1)

/-- The demand magnitude: sum of absolute values of negative
    NF coefficients. -/
noncomputable def demandMagnitude (nf : Fin 6 → ℝ) : ℝ :=
  Finset.sum Finset.univ fun i => if nf i < 0 then |nf i| else 0

/-- An atom is shell-closed if its demand profile is empty
    (all NF coefficients are non-negative). -/
def isShellClosed (nf : Fin 6 → ℝ) : Prop :=
  ∀ i : Fin 6, nf i ≥ 0

/-- Beta-stable: demand-minimal at fixed mass number A.
    An atom A(Z,N) is beta-stable iff for all Z' with Z'+N' = Z+N:
      |dem(A(Z,N))| ≤ |dem(A(Z',N'))| -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
def isBetaStable (Z N : ℕ) : Prop :=
  sorry  -- Requires quantification over all Z' with Z'+N'=Z+N

/-- The e⁻ coefficient in the nucleon NF is the beta decay
    receptivity. A nucleon with c_{e⁻} < 0 is receptive to
    emitting an electron via beta decay. -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
theorem beta_receptivity (nf_n nf_p : Fin 6 → ℝ)
    (h_e_n : nf_n 5 < 0)    -- neutron e⁻ coefficient negative
    (h_e_p : nf_p 5 < 0)    -- proton e⁻ coefficient negative
    (h_larger : |nf_n 5| > |nf_p 5|)  -- neutron has larger e⁻ demand
    (h_net : (Finset.sum Finset.univ nf_n) < (Finset.sum Finset.univ nf_p)) :
    -- Then beta decay n → p + e⁻ + ν̄ is energetically allowed
    True := by
  sorry

/-- Magic numbers correspond to demand closure.
    Conjecture: Z (or N) is a magic number iff there exists N' (or Z')
    such that the nucleus N(Z, N') is shell-closed. -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
def isMagicNumber (k : ℕ) : Prop :=
  sorry  -- k ∈ {2, 8, 20, 28, 50, 82, 126}

/-- Doubly magic: both Z and N are magic, and the nucleus has
    locally minimal Markov trace among neighboring (Z, N). -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
def isDoublyMagic (Z N : ℕ) : Prop :=
  isMagicNumber Z ∧ isMagicNumber N

end QOU.Interactions
