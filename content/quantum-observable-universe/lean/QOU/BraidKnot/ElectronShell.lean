/-!
# Electron Shell

An electron shell of multiplicity `Z` around a nucleon-level atom
is a cabling `H_A(q) ↪ H_{A+Z}(q)` plus an SDP-selected binding
subword `W_bind ∈ BraidWord (A+Z)`. Binding multiplicity `μ(S, q)`
counts the active dual blocks of the confinement SDP; `μ ≥ 2` at
magic `Z ∈ {2, 10, 18, 36, 54, 86}` (noble gas) is the
multi-operator regime.

## References

- [def:electron-shell]
- [prop:confinement-sdp]
-/

import QOU.BraidKnot.ConfinedParticle

namespace QOU.BraidKnot

open QOU.Descartes

/-- **Electron shell.** Cabled-strand representation: `Z` electrons
    added as extra strands in `H_{A+Z}(q)` with binding subword
    drawn from the confinement-SDP active support.

    The `bindingWord` lives in `BraidWord nStrandsTotal` where
    `nStrandsTotal = A + nElectrons`. -/
-- Ref: [manuscript] braids-and-knots/electron-shell
structure ElectronShell where
  /-- The nucleus particle the shell is attached to. -/
  nucleus : ConfinedParticle
  /-- Number `Z` of electrons in the shell. -/
  nElectrons : ℕ
  /-- Total strand count `A + Z` after cabling. -/
  nStrandsTotal : ℕ
  /-- Cabling consistency: `nStrandsTotal = nucleus.coarseStrands + nElectrons`. -/
  cabling : nStrandsTotal = nucleus.coarseStrands + nElectrons
  /-- Canonical binding subword as a formal Hecke word in the
      cabled algebra. -/
  bindingWord : BraidWord nStrandsTotal

/-- Binding multiplicity `μ(S, q)` — cardinality of the active dual
    support of the confinement SDP at `q`. `μ = 1` is the
    single-block regime; `μ ≥ 2` is the multi-operator regime that
    obtains at noble-gas `Z ∈ {2, 10, 18, 36, 54, 86}`. -/
-- Ref: [manuscript] particle-interactions/confinement-sdp
opaque bindingMultiplicity : ElectronShell → R_q → ℕ

/-- The set of noble-gas electron magic numbers. -/
-- Ref: [manuscript] braids-and-knots/shell-closure-stability
def nobleGasMagic : Finset ℕ := ({2, 10, 18, 36, 54, 86} : Finset ℕ)

/-- **Multi-operator regime at noble-gas `Z`.** For any shell `S`
    with `nElectrons ∈ nobleGasMagic` and `q` in the generic locus,
    the binding multiplicity satisfies `μ(S, q) ≥ 2`. This is the
    computational content of `electron-shell-ilp` witnesses
    (electrons alternate between `σ_0⁻¹` and `σ_1⁻¹`). -/
-- Ref: [manuscript] braids-and-knots/electron-shell
-- Ref: [boyd-vandenberghe-2004] https://doi.org/10.1017/CBO9780511804441
axiom noble_gas_multi_operator
    (S : ElectronShell) (q : R_q)
    (h : S.nElectrons ∈ nobleGasMagic) :
    bindingMultiplicity S q ≥ 2

end QOU.BraidKnot
