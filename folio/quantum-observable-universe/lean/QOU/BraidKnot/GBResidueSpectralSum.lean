import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Finset.Basic
import Mathlib.Algebra.Order.Ring.Abs
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

## Base ring (AGENTS.md §7c)

Pre-archimedean.  The decomposition `𝔪 = |tr_M| + Σ_ℓ Res_ℓ`, the
classical limit, and the `Fin levelBound` cardinality statement are
identities in **any** linearly ordered commutative ring `R`
(`[CommRing R] [LinearOrder R]`); only the order is used, and that
only to give `|·|` a meaning.  No completeness, no `Real.*`, no
archimedean axiom appears.  The archimedean content — the actual
MeV mass, the descended Markov-trace value, and the cyclotomic
residues of `Φ_q` at `ζ_ℓ` — is carried entirely by an *instance*,
built at `R := ℝ` from the crystal-basis witness (see
`fromCrystalData` below).  This is the §7c prescription: the generic
construction stays here, the ℝ realisation consumes it via
`(R := ℝ)`.

Ref: [leitner2026] Chapter 6, §Nuclear Binding and Beta Stability
LaTeX label: `prop:gb-residue-spectral-sum`
-- Ref: [leitner2026] prop:graded-markov-trace-from-gs-filtration
-- Ref: [leitner2026] prop:residue-at-root
-/

namespace QOU.BraidKnot

variable {R : Type*} [CommRing R] [LinearOrder R]

/-- A root of unity `ζ_ℓ` at which the `ℓ`-th knot-operator energy
    `E_ℓ(q)` vanishes.  `value` is the coordinate of `ζ_ℓ` in the
    ambient ring `R` (at `R := ℝ`, its real part; a full Mathlib
    treatment would take `R := ℂ`). -/
structure RootOfUnity (R : Type*) where
  n : ℕ
  n_pos : 0 < n
  value : R

/-- **GB residue spectral sum.**

    The mass of a closed braid `K` with Hecke normal form `T_w` is

      𝔪(K) = |tr_M(T_w)| + Σ_{ℓ=0}^{levelBound-1} Res_{q→ζ_ℓ}(Φ_q · tr_{M,ℓ})(T_w)

    The class field structure replaces the previous `opaque
    gradedMarkovTrace` and `opaque residueAtRoot` declarations:
    each instance must supply the graded trace and cyclotomic
    residue values explicitly. -/
class GBResidueSpectralSum (R : Type*) [CommRing R] [LinearOrder R] where
  /-- The descended (E⁰) Markov trace of the braid word. -/
  descended : R
  /-- The confinement-level cutoff. -/
  levelBound : ℕ
  /-- The substrate parameter. -/
  q : R
  /-- The roots of unity indexed by filtration level. -/
  roots : Fin levelBound → RootOfUnity R
  /-- The graded Markov trace at level `ℓ`, supplied by the instance.
      Per `prop:graded-markov-trace-from-gs-filtration`. -/
  gradedTrace : Fin levelBound → R
  /-- The cyclotomic residue at level `ℓ`, supplied by the instance.
      Per `prop:residue-at-root`. -/
  residue : Fin levelBound → R
  /-- The spectral sum: `𝔪 = |descended| + Σ_ℓ residue ℓ`. -/
  mass : R
  /-- Consistency: the mass is the descended term plus the sum of
      residues over filtration levels. -/
  spectral_decomposition :
    mass = |descended| + ∑ ℓ : Fin levelBound, residue ℓ

/-- Convenience accessor: residue at level `ℓ`. -/
def residueAt (S : GBResidueSpectralSum R)
    (ℓ : Fin S.levelBound) : R :=
  S.residue ℓ

/-- Convenience accessor: graded trace at level `ℓ`. -/
def gradedMarkovTrace (S : GBResidueSpectralSum R)
    (ℓ : Fin S.levelBound) : R :=
  S.gradedTrace ℓ

/-- Classical limit: when every cyclotomic residue vanishes, the
    mass reduces to the descended trace magnitude. -/
-- Ref: [leitner2026] `prop:categorical-mass-markov`
theorem classical_limit_descended
    (S : GBResidueSpectralSum R)
    (hres : ∀ ℓ : Fin S.levelBound, S.residue ℓ = 0) :
    S.mass = |S.descended| := by
  rw [S.spectral_decomposition]
  simp [hres]

/-- The total cyclotomic residue sum equals the excess of `S.mass` over the descended
    contribution `|S.descended|`. -/
theorem residue_sum_eq_mass_sub_abs_descended
    (S : GBResidueSpectralSum R) :
    (∑ ℓ : Fin S.levelBound, S.residue ℓ) = S.mass - |S.descended| := by
  rw [S.spectral_decomposition]
  exact (add_sub_cancel_left |S.descended| (∑ ℓ : Fin S.levelBound, S.residue ℓ)).symm

/-- When the descended trace is non-negative (`0 ≤ S.descended`), the spectral decomposition
    expresses `S.mass` directly as `S.descended + ∑ ℓ, S.residue ℓ`. -/
theorem mass_eq_descended_add_residues_of_nonneg [AddLeftMono R]
    (S : GBResidueSpectralSum R) (hd : 0 ≤ S.descended) :
    S.mass = S.descended + ∑ ℓ : Fin S.levelBound, S.residue ℓ := by
  rw [S.spectral_decomposition, abs_of_nonneg hd]

/-- When the descended trace is non-positive (`S.descended ≤ 0`), the spectral decomposition
    expresses `S.mass` as `-S.descended + ∑ ℓ, S.residue ℓ`. -/
theorem mass_eq_neg_descended_add_residues_of_nonpos [AddLeftMono R]
    (S : GBResidueSpectralSum R) (hd : S.descended ≤ 0) :
    S.mass = -S.descended + ∑ ℓ : Fin S.levelBound, S.residue ℓ := by
  rw [S.spectral_decomposition, abs_of_nonpos hd]

/-- **GB residue spectral sum proposition.**  Conditional on a
    `[GBResidueSpectralSum]` instance, the spectral decomposition
    holds. -/
-- Ref: [leitner2026] `prop:gb-residue-spectral-sum`
theorem gb_residue_spectral_sum (R : Type*) [CommRing R] [LinearOrder R]
    [s : GBResidueSpectralSum R] :
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
theorem spectral_sum_finite (S : GBResidueSpectralSum R) :
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
    holds by `rfl`.

    This is the §7c realisation point: instantiating at `R := ℝ`
    with the crystal-basis witness values is what puts the
    (otherwise generic) decomposition on the archimedean side. -/
def fromCrystalData
    (descended : R) (levelBound : ℕ) (q : R)
    (roots : Fin levelBound → RootOfUnity R)
    (gradedTrace residue : Fin levelBound → R) :
    GBResidueSpectralSum R where
  descended := descended
  levelBound := levelBound
  q := q
  roots := roots
  gradedTrace := gradedTrace
  residue := residue
  mass := |descended| + ∑ ℓ : Fin levelBound, residue ℓ
  spectral_decomposition := rfl

end QOU.BraidKnot
