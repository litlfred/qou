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
(b) discharge the proof obligation in `spectral_sum_finite`, and
(c) make the instance data explicit at the call site.

Corrected 2026-09-04 (bean `qou-tmmt`): clause (b) said "close the
unproved placeholder in `spectral_sum_finite`", which was accurate about
the placeholder disappearing and misleading about what replaced it. What
the class-based form actually produced was a statement with a free
disjunct — `… = 0 ∨ ℓ < levelBound`, discharged by `Or.inr h` on the
hypothesis itself — which held for every instance and asserted nothing.
The statement is repaired below and (b) is now true for the first time.
The word for an unproved placeholder is also removed from this sentence:
the `wall-side-proof` checker matches it inside comments, and it was
reporting this file as carrying one when the code has none.

Ref: [leitner2026] Chapter 6, §Nuclear Binding and Beta Stability
LaTeX label: `prop:gb-residue-spectral-sum`
-- Ref: [leitner2026] prop:graded-markov-trace-from-gs-filtration
-- Ref: [leitner2026] prop:residue-at-root
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
  /-- The graded trace value at level `ℓ`, **supplied freely by the instance**.

      *Intended* meaning, per `prop:graded-markov-trace-from-gs-filtration`: the
      value of `tr_M` descended to `J^ℓ / J^{ℓ+1}`.  **That is not encoded here** —
      no field relates this to `tr_M`, to the filtration, or to `descended`, so an
      instance may supply any function at all.  Encoding it needs the
      GS-filtration infrastructure the module header defers. -/
  gradedTrace : Fin levelBound → R
  /-- The residue value at level `ℓ`, **supplied freely by the instance**.

      *Intended* meaning, per `prop:residue-at-root`: the cyclotomic projection of
      `Φ_q · gradedTrace ℓ` in the Habiro completion.  **That is not encoded here** —
      in particular nothing relates `residue` to `gradedTrace`, despite the prose,
      so the two are independent data.  Encoding it needs the Habiro-ring
      infrastructure the module header defers. -/
  residue : Fin levelBound → R
  /-- The spectral sum:
      `𝔪 = |descended| + Σ_ℓ residue ℓ`.

      Equivalent to the previous statement
      `mass = |descended| + Σ_ℓ residueAtRoot ℓ.val (roots ℓ) q`,
      with `residue ℓ` standing in for the unfolded
      `residueAtRoot ℓ.val (roots ℓ) q` term. -/
  mass : R
  /-- Consistency: the mass is the descended term plus the sum of residues over
      filtration levels.  This is the content of `prop:gb-residue-spectral-sum`, and
      the **only** `Prop` field of the class.

      Note what it does and does not buy.  It constrains `mass` — but `mass` is
      itself a free field, so any tuple inhabits the class: choose the six data
      fields freely, set `mass := |descended| + ∑ residue ℓ`, and discharge this by
      `rfl`.  So it fixes one field relative to the others rather than constraining
      anything outside the class. -/
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

    Ref: [leitner2026] `prop:categorical-mass-markov`. -/
theorem classical_limit_descended (S : GBResidueSpectralSum R)
    (hres : ∀ ℓ : Fin S.levelBound, S.residue ℓ = 0) :
    S.mass = |S.descended| := by
  rw [S.spectral_decomposition]
  simp [hres]

/-- The residue extended to **every** level, by zero above the confinement
    bound. This is the object the finiteness claim is about: `residue` alone is
    a function on `Fin levelBound`, so "vanishes above the bound" cannot even be
    stated for it. -/
def GBResidueSpectralSum.residueAtLevel (S : GBResidueSpectralSum R) (l : ℕ) : R :=
  if h : l < S.levelBound then S.residue ⟨l, h⟩ else 0

/-- **Finiteness of the spectral sum.** The extended residue vanishes at every
    level at or above the confinement bound, so the sum has finitely many
    non-zero terms.

    ## Restated 2026-09-04 (bean `qou-tmmt`) — the previous statement was vacuous

    It read

        ∃ N, ∀ ℓ ≥ N, ∀ (h : ℓ < S.levelBound),
          S.residue ⟨ℓ, h⟩ = 0 ∨ ℓ < S.levelBound

    and was proved by `exact Or.inr h` — **the right disjunct is the hypothesis
    `h` itself**. So it held for every `S` and every `residue` whatsoever, with
    any `N` at all, and asserted nothing about vanishing or finiteness. Its own
    docstring recorded the cause: the block's actual claim,
    `∃ N, ∀ ℓ ≥ N, residueAtRoot ℓ ζ q = 0`, was described as becoming "a
    tautology in the class-based formulation", and the free disjunct was added
    to make it provable rather than the statement being repaired.

    It is not a tautology — it is a statement about a function on `ℕ`, and
    `residue : Fin levelBound → R` is not one. With the zero-extension above,
    the block's original claim goes through directly, and the extension is what
    the prose meant by "strata above this give zero contribution".

    ## What this does NOT establish

    The vanishing proved here is of the **canonical zero-extension**, which is
    what makes finiteness statable at all. It is not the conjectural claim, and
    the library twin `QOU.BraidKnot.spectral_sum_finite` in
    `lean/QOU/BraidKnot/GBResidueSpectralSum.lean` states that correctly: the
    substantive content of `conj:gs-spectral-sum-finite` is that `levelBound`
    *truly equals* the confinement level `ℓ(K, q₀)` of the underlying braid, so
    that any **analytic** extension of `residue` to `ℕ` vanishes above the
    cutoff. Nothing here bears on that. Extending by zero and then observing
    that the extension is zero would be circular if offered as evidence for it.

    Note also that the library twin carries the *same declaration name* in the
    same namespace while proving a different statement — there,
    `card (univ : Finset (Fin levelBound)) = levelBound`, the algebraic
    finiteness. A content-block sibling is outside the Lake glob so the two do
    not collide at build time, but `gs-spectral-sum-finite.ts` resolves its
    `lean.ref` to the library one, not to this. Recorded in bean `qou-tmmt`.

    Ref: [leitner2026] `prop:confinement-level-unique`. -/
theorem spectral_sum_finite (S : GBResidueSpectralSum R) :
    ∃ N : ℕ, ∀ l : ℕ, N ≤ l → S.residueAtLevel l = 0 := by
  refine ⟨S.levelBound, fun l hl => ?_⟩
  unfold GBResidueSpectralSum.residueAtLevel
  rw [dif_neg (Nat.not_lt.mpr hl)]

/-- The spectral sum may be taken over the extended residue on the initial
    segment `Fin levelBound` without change — the extension agrees with
    `residue` everywhere it is defined. -/
theorem spectral_decomposition_extended (S : GBResidueSpectralSum R) :
    S.mass = |S.descended| + ∑ l : Fin S.levelBound, S.residueAtLevel l.val := by
  rw [S.spectral_decomposition]
  congr 1
  refine Finset.sum_congr rfl fun l _ => ?_
  unfold GBResidueSpectralSum.residueAtLevel
  rw [dif_pos l.isLt]

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
