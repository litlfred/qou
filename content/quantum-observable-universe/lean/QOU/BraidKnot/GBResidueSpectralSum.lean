import Mathlib.Algebra.BigOperators.Basic
import Mathlib.Data.Finset.Basic
import QOU.BraidKnot.ConfinementLevel

/-!
# QOU.BraidKnot.GBResidueSpectralSum — Gröbner–Shirshov residue spectral sum

The categorical mass of a closed braid is the sum of its descended
Markov trace (E⁰ term) and a finite sum of residues at root-of-unity
poles of the quantum dilogarithm, one per Gröbner–Shirshov
filtration stratum that the braid's Hecke normal form occupies.

**Conditional-class axiomatisation** (CLAUDE.md §3b).  The
`gradedMarkovTrace` and `residueAtRoot` opaques are now class
fields of `GBResidueSpectralSum`; concrete instances supply the
graded trace and cyclotomic residue values.

**Formal-chain version.**  Lives under `lean/QOU/` and is compiled
by `lake build`.  The co-located documentation stub at
`braids-and-knots/gb-residue-spectral-sum.lean` mirrors this.

Ref: [manuscript] Chapter 6, §Nuclear Binding and Beta Stability
LaTeX label: `prop:gb-residue-spectral-sum`
-- Ref: [manuscript] prop:graded-markov-trace-from-gs-filtration
-- Ref: [manuscript] prop:residue-at-root
-/

namespace QOU.BraidKnot

/-- A root of unity `ζ_ℓ` at which the `ℓ`-th knot-operator energy
    `E_ℓ(q)` vanishes. -/
structure RootOfUnity where
  n : ℕ
  n_pos : 0 < n
  value : ℝ  -- real part; full Mathlib version uses `Complex`

/-- **GB residue spectral sum.**

    The mass of a closed braid `K` with Hecke normal form `T_w` is

      𝔪(K) = |tr_M(T_w)| + Σ_{ℓ=0}^{levelBound-1} Res_{q→ζ_ℓ}(Φ_q · tr_{M,ℓ})(T_w)

    The class field structure replaces the previous `opaque
    gradedMarkovTrace` and `opaque residueAtRoot` declarations:
    each instance must supply the graded trace and cyclotomic
    residue values explicitly. -/
class GBResidueSpectralSum where
  /-- The descended (E⁰) Markov trace of the braid word. -/
  descended : ℝ
  /-- The confinement-level cutoff. -/
  levelBound : ℕ
  /-- The substrate parameter. -/
  q : ℝ
  /-- The roots of unity indexed by filtration level. -/
  roots : Fin levelBound → RootOfUnity
  /-- The graded Markov trace at level `ℓ`, supplied by the instance.
      Per `prop:graded-markov-trace-from-gs-filtration`. -/
  gradedTrace : Fin levelBound → ℝ
  /-- The cyclotomic residue at level `ℓ`, supplied by the instance.
      Per `prop:residue-at-root`. -/
  residue : Fin levelBound → ℝ
  /-- The spectral sum: `𝔪 = |descended| + Σ_ℓ residue ℓ`. -/
  mass : ℝ
  /-- Consistency: the mass is the descended term plus the sum of
      residues over filtration levels. -/
  spectral_decomposition :
    mass = |descended| + ∑ ℓ : Fin levelBound, residue ℓ

/-- Convenience accessor: residue at level `ℓ`. -/
def GBResidueSpectralSum.residueAt (S : GBResidueSpectralSum)
    (ℓ : Fin S.levelBound) : ℝ :=
  S.residue ℓ

/-- Convenience accessor: graded trace at level `ℓ`. -/
def GBResidueSpectralSum.gradedMarkovTrace (S : GBResidueSpectralSum)
    (ℓ : Fin S.levelBound) : ℝ :=
  S.gradedTrace ℓ

/-- Classical limit: when every cyclotomic residue vanishes, the
    mass reduces to the descended Markov trace.

    Ref: [manuscript] `prop:categorical-mass-markov`. -/
theorem GBResidueSpectralSum.classical_limit_descended
    (S : GBResidueSpectralSum)
    (hres : ∀ ℓ : Fin S.levelBound, S.residue ℓ = 0) :
    S.mass = |S.descended| := by
  rw [S.spectral_decomposition]
  simp [hres]

/-- **GB residue spectral sum proposition.**  Conditional on a
    `[GBResidueSpectralSum]` instance, the spectral decomposition
    holds. -/
-- Ref: [manuscript] `prop:gb-residue-spectral-sum`
theorem gb_residue_spectral_sum [s : GBResidueSpectralSum] :
    s.mass = |s.descended| + ∑ ℓ : Fin s.levelBound, s.residue ℓ :=
  s.spectral_decomposition

end QOU.BraidKnot
