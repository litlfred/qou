import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Finset.Basic
import QOU.BraidKnot.ConfinementLevel

/-!
# QOU.BraidKnot.GBResidueSpectralSum — Gröbner–Shirshov residue spectral sum

The categorical mass of a closed braid is the sum of its descended
Markov trace (E⁰ term) and a finite sum of residues at root-of-unity
poles of the quantum dilogarithm, one per Gröbner–Shirshov
filtration stratum that the braid's Hecke normal form occupies.

**Conditional-class axiomatisation** (AGENTS.md §3b).  The
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

/-- **Finiteness (cardinality form).**

    The spectral sum `∑ ℓ : Fin S.levelBound, S.residue ℓ` is
    a sum over a `Finset` of cardinality `S.levelBound`, hence
    finite by Mathlib's standard finite-sum machinery.

    Note: this is the *algebraic* finiteness — the index set
    `Fin S.levelBound` has cardinality `S.levelBound` by
    construction, so the sum has at most `S.levelBound`
    non-zero terms.  The *substantive* claim of
    `conj:gs-spectral-sum-finite` — that `S.levelBound` truly
    equals the confinement level `ℓ(K, q_0)` of the underlying
    braid, so that any analytic extension of `S.residue` to
    `ℕ` vanishes above the cutoff — is the conjectural part
    and is not formalised here; see the `.md` narrative under
    "Why a conjecture and not a theorem". -/
theorem spectral_sum_finite (S : GBResidueSpectralSum) :
    (Finset.univ : Finset (Fin S.levelBound)).card = S.levelBound := by
  simp

/-! ## Constructing instances from crystal-basis data

A concrete `GBResidueSpectralSum` is determined by the data
`(descended, levelBound, q, roots, gradedTrace, residue)`; the
`mass` and `spectral_decomposition` fields are then forced.  The
constructor below packages this fact and is the post-class
analogue of "discharging" the previous `opaque` declarations: any
caller that supplies the data gets a concrete instance with no
residual abstraction.

The intended source of the data is the crystal-basis derivation
witness `term7-alpha5-crystal-derivation.witness.json` (per
`prop:term7-shell-correction`), which supplies per-atom and
per-level structural values from Schur–Weyl + Wedderburn +
categorical R-matrix action evaluated at the crystal limit
`q → 0`.  The corresponding compute-side derivation chain is
`term7-s-crystal-4he.derivation.json`. -/

/-- Construct a `GBResidueSpectralSum` from explicit per-level
    data.  The `mass` field is forced to the canonical decomposition
    `|descended| + Σ_ℓ residue ℓ`, and `spectral_decomposition`
    holds by `rfl`. -/
def GBResidueSpectralSum.fromCrystalData
    (descended : ℝ) (levelBound : ℕ) (q : ℝ)
    (roots : Fin levelBound → RootOfUnity)
    (gradedTrace residue : Fin levelBound → ℝ) :
    GBResidueSpectralSum where
  descended := descended
  levelBound := levelBound
  q := q
  roots := roots
  gradedTrace := gradedTrace
  residue := residue
  mass := |descended| + ∑ ℓ : Fin levelBound, residue ℓ
  spectral_decomposition := rfl

end QOU.BraidKnot
