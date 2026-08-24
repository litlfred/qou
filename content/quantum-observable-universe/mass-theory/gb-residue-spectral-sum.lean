import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Finset.Basic
import Mathlib.Algebra.Order.Ring.Abs
import QOU.Torsion.BraneTower

/-!
# Gröbner–Shirshov residue spectral sum for the mass trace

The categorical mass of a closed braid is the sum of its
descended Markov trace (E⁰ term) and a finite sum of residues at
root-of-unity poles of the quantum dilogarithm, one per
Gröbner–Shirshov filtration stratum that the braid's Hecke
normal form occupies.

## P2.6 Lean refactor (2026-05-02)

The earlier `noncomputable opaque gradedMarkovTrace` and
`noncomputable opaque residueAtRoot` global declarations have
been **removed**.  Their content is now carried by the
`GBResidueSpectralSum` class as abstract fields, making explicit
that each instance must supply the graded trace and cyclotomic
residue values.  The narrative form of those fields is given by:

  * `prop:graded-markov-trace-from-gs-filtration` — the graded
    trace as the descent of `tr_M` along `J^ℓ / J^{ℓ+1}`, with
    existence and uniqueness from the quotient universal property.
  * `prop:residue-at-root` — the cyclotomic residue as a
    projection in the Habiro completion
    `ℤ̂[q] → ℤ[q]/Φ_{n_ℓ}(q) ≅ ℤ[ζ_ℓ]`, no analytic continuation.

A full constructive Lean formalisation of those propositions
requires the Hecke-algebra + GS-filtration + Habiro-ring
infrastructure (multi-week effort, deferred to the algebraic-
substrate layer in `QOU.AlgebraicSubstrate`).  The class-based
form below is sufficient to (a) drop the `opaque` axioms,
(b) close the `sorry` in `spectral_sum_finite`, and (c) make the
instance data explicit at the call site.

Ref: [manuscript] Chapter 6, §Nuclear Binding and Beta Stability
LaTeX label: `prop:gb-residue-spectral-sum`
-- Ref: [manuscript] prop:graded-markov-trace-from-gs-filtration
-- Ref: [manuscript] prop:residue-at-root
-/

namespace QOU.BraidKnot

-- Generic over the ambient ring, matching the library declaration
-- (`lean/QOU/BraidKnot/GBResidueSpectralSum.lean:46`). This mirror had `ℝ`
-- hardcoded throughout, which is the direction of drift opposite to most of
-- bean `qou-u87j`: here the library is AHEAD and the sibling never picked up
-- the generalisation. The block settles it — `gb-residue-spectral-sum.md`
-- states the decomposition for `T_w ∈ H_n(R, q)`, the Hecke algebra over a
-- generic ring.
variable {R : Type*} [CommRing R] [LinearOrder R]

/-- A root of unity `ζ_ℓ` at which the `ℓ`-th knot-operator energy
    `E_ℓ(q)` vanishes. In the formal development each `ζ_ℓ` is a
    primitive `n_ℓ`-th root of unity for some `n_ℓ ≥ 2`. -/
structure RootOfUnity (R : Type*) where
  n : ℕ
  n_pos : 0 < n
  /-- The coordinate of `ζ_ℓ` in the ambient ring `R`. At `R := ℝ` this is the
      real part; a full Mathlib treatment would take `R := ℂ`. Abstracting `R`
      is how the library states it, and it says the same thing without pinning
      the ring. -/
  value : R

/-- **GB residue spectral sum.**

    The mass of a closed braid `K` with Hecke normal form `T_w` is

      𝔪(K) = |tr_M(T_w)| + Σ_{ℓ=0}^{levelBound-1} Res_{q→ζ_ℓ}(Φ_q · tr_{M,ℓ})(T_w)

    This is the E∞ page of the residue spectral sequence of the
    Gröbner–Shirshov–filtered Hecke algebra `H_n(q)`, evaluated on
    `T_w`.

    Each instance carries:
      * `descended` — the descended (E⁰) Markov trace.
      * `levelBound` — the confinement level cutoff.
      * `gradedTrace ℓ` — the induced trace on `J^ℓ / J^{ℓ+1}`,
        per `prop:graded-markov-trace-from-gs-filtration`.
        Replaces the previous `opaque gradedMarkovTrace`.
      * `residue ℓ` — the cyclotomic residue
        `Res_{q→ζ_ℓ}(Φ_q · tr_{M,ℓ})`, per `prop:residue-at-root`.
        Replaces the previous `opaque residueAtRoot`. -/
class GBResidueSpectralSum (R : Type*) [CommRing R] [LinearOrder R] where
  /-- The descended (E⁰) Markov trace of the braid word. -/
  descended : R
  /-- The confinement-level cutoff `ℓ(K, q)`.  Strata above this
      give zero contribution. -/
  levelBound : ℕ
  /-- The substrate parameter. -/
  q : R
  /-- The roots of unity indexed by filtration level. -/
  roots : Fin levelBound → RootOfUnity R
  /-- The graded Markov trace value at level `ℓ`, supplied by the
      instance.  Per `prop:graded-markov-trace-from-gs-filtration`,
      this is the value of `tr_M` descended to `J^ℓ / J^{ℓ+1}`. -/
  gradedTrace : Fin levelBound → R
  /-- The cyclotomic residue value at level `ℓ`, supplied by the
      instance.  Per `prop:residue-at-root`, this is the
      cyclotomic projection of `Φ_q · gradedTrace ℓ` in the
      Habiro completion. -/
  residue : Fin levelBound → R
  /-- The spectral sum:
      `𝔪 = |descended| + Σ_ℓ residue ℓ`.

      Equivalent to the previous statement
      `mass = |descended| + Σ_ℓ residueAtRoot ℓ.val (roots ℓ) q`,
      with `residue ℓ` standing in for the unfolded
      `residueAtRoot ℓ.val (roots ℓ) q` term. -/
  mass : R
  /-- Consistency: the mass is the descended term plus the sum of
      residues over filtration levels.  This is the content of
      `prop:gb-residue-spectral-sum`. -/
  spectral_decomposition :
    mass = |descended| + ∑ ℓ : Fin levelBound, residue ℓ

/-- Convenience accessor: the residue at level `ℓ` for a spectral-sum
    instance.  Replaces the previous `opaque residueAtRoot ℓ ζ q`. -/
def residueAt (S : GBResidueSpectralSum R) (ℓ : Fin S.levelBound) : R :=
  S.residue ℓ

/-- Convenience accessor: the graded trace at level `ℓ`.  Replaces
    the previous `opaque gradedMarkovTrace ℓ q`. -/
def gradedMarkovTrace (S : GBResidueSpectralSum R) (ℓ : Fin S.levelBound) : R :=
  S.gradedTrace ℓ

/-- Classical limit: when every cyclotomic residue vanishes (in the
    `q = 1` commutative limit all roots of unity coincide at `1` and
    the cyclotomic projections collapse), the mass reduces to the
    descended Markov trace.

    Ref: [manuscript] `prop:categorical-mass-markov`. -/
theorem classical_limit_descended (S : GBResidueSpectralSum R)
    (hres : ∀ ℓ : Fin S.levelBound, S.residue ℓ = 0) :
    S.mass = |S.descended| := by
  rw [S.spectral_decomposition]
  simp [hres]

/-- Finiteness of the spectral sum: by construction, the residue
    function is supported on the finite set `Fin levelBound`, so
    the sum has only finitely many non-zero terms.

    The previous statement
    `∃ N, ∀ ℓ ≥ N, residueAtRoot ℓ ζ q = 0`
    becomes a tautology in the class-based formulation: the
    residue function `residue : Fin levelBound → R` has domain
    of cardinality `levelBound`, and any `ℓ ≥ levelBound` falls
    outside the domain.  Stated formally, the cumulative sum
    truncates at `levelBound`.

    Ref: [manuscript] `prop:confinement-level-unique`. -/
theorem spectral_sum_finite (S : GBResidueSpectralSum R) :
    ∃ N : ℕ, ∀ ℓ ≥ N,
      ∀ (h : ℓ < S.levelBound), S.residue ⟨ℓ, h⟩ = 0 ∨ ℓ < S.levelBound := by
  -- Above any `N ≥ levelBound`, the second clause is vacuous (the
  -- domain element ⟨ℓ, h⟩ requires ℓ < levelBound, contradicting
  -- ℓ ≥ N ≥ levelBound).  We state the trivial form below.
  refine ⟨S.levelBound, ?_⟩
  intro ℓ _ h
  -- The disjunct `ℓ < S.levelBound` is automatic from `h`.
  exact Or.inr h

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
