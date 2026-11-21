import QOU.BraidKnot.ConfinedParticle

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

namespace QOU.BraidKnot

open QOU.Archimedean

/-- **Electron shell.** Cabled-strand representation: `Z` electrons
    added as extra strands in `H_{A+Z}(q)` with binding subword
    drawn from the confinement-SDP active support.

    The `bindingWord` lives in `BraidWord nStrandsTotal` where
    `nStrandsTotal = A + nElectrons`. -/
-- Ref: [leitner2026] braids-and-knots/electron-shell
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

/-- Binding multiplicity data — class-supplied evaluation of
    `μ(S, q)` (cardinality of the active dual support of the
    confinement SDP at `q`). `μ = 1` is the single-block regime;
    `μ ≥ 2` is the multi-operator regime that obtains at noble-gas
    `Z ∈ {2, 10, 18, 36, 54, 86}`. -/
-- Ref: [leitner2026] particle-interactions/confinement-sdp
class HasBindingMultiplicity (S : ElectronShell) where
  /-- The multiplicity `μ(S, q)`. -/
  mu : R_q → ℕ

/-- Binding multiplicity accessor, backed by `HasBindingMultiplicity`. -/
def bindingMultiplicity (S : ElectronShell) [h : HasBindingMultiplicity S]
    (q : R_q) : ℕ :=
  h.mu q

/-- The set of noble-gas electron magic numbers. -/
-- Ref: [leitner2026] braids-and-knots/shell-closure-stability
def nobleGasMagic : Finset ℕ := ({2, 10, 18, 36, 54, 86} : Finset ℕ)

/-- **Noble-gas multi-operator regime — typeclass (Pattern 4).**

    Witnesses `μ(S, q) ≥ 2` for a *specific* shell `S` whose
    electron count lies in `nobleGasMagic`. The computational
    content is supplied by the `electron-shell-ilp` witnesses
    (alternating-`σ_0⁻¹`/`σ_1⁻¹` packings); a class lets each
    caller bind to the witness for the specific `(S, q)` it cares
    about, rather than asserting a universal SDP property. -/
-- Ref: [leitner2026] braids-and-knots/electron-shell
-- Ref: [boyd-vandenberghe-2004] §5.2.3 (Slater's condition) + §5.3
--      (strong duality for convex problems) + §5.5 (KKT optimality)
class NobleGasMultiOperator
    (S : ElectronShell) [HasBindingMultiplicity S] (q : R_q)
    (_h : S.nElectrons ∈ nobleGasMagic) : Prop where
  /-- Binding multiplicity at noble-gas `Z` is at least 2. -/
  multi : bindingMultiplicity S q ≥ 2

/-- **Default instance from a `Fact` witness on the multiplicity**.
    When `Fact (bindingMultiplicity S q ≥ 2)` is in scope (e.g. from
    a numerical SDP solver providing the integer witness), the
    NobleGasMultiOperator instance follows directly. -/
instance nobleGasMultiOperator_of_fact
    (S : ElectronShell) [HasBindingMultiplicity S] (q : R_q)
    (h : S.nElectrons ∈ nobleGasMagic)
    [hf : Fact (bindingMultiplicity S q ≥ 2)] :
    NobleGasMultiOperator S q h :=
  ⟨hf.out⟩

/-- **Multi-operator regime at noble-gas `Z`** (per-instance form).
    Backed by `NobleGasMultiOperator`.

    **Assumed, not derived here** — the body projects
    `NobleGasMultiOperator.multi`, so the multiplicity inequality
    `bindingMultiplicity S q ≥ 2` is carried as a context-class hypothesis
    (§3b-conditional, derivation pending), not derived below.
    Boyd–Vandenberghe is cited for the convex-duality / KKT background of the
    multi-operator regime, not for a proof performed here; since `S` and `q`
    are arbitrary, this projection may not be converted to a global `axiom`. -/
-- Ref: [leitner2026] braids-and-knots/electron-shell
-- Ref: [boyd-vandenberghe-2004] §5.2.3 (Slater's condition) + §5.3
--      (strong duality for convex problems) + §5.5 (KKT optimality)
theorem noble_gas_multi_operator
    (S : ElectronShell) [HasBindingMultiplicity S] (q : R_q)
    (h : S.nElectrons ∈ nobleGasMagic)
    [hi : NobleGasMultiOperator S q h] :
    bindingMultiplicity S q ≥ 2 :=
  hi.multi

end QOU.BraidKnot
