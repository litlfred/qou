/-
  Proof of the end-to-end atom-knot mass derivation (categorical form).

  After the pre-Archimedean / post-Archimedean simplification
  (Yekutieli at finite slices + GB spectral sequence collapse at E_2),
  the proof is a SINGLE categorical pipeline pre-Archimedean,
  terminated by the Archimedean realization functor.

  No asymptotic content (no Reeb density, no Mostow + Gromov, no
  volume-conjecture identification) enters the derivation.

  Refs: conj:atom-knot-mass-derivation, prop:gb-spectral-sequence,
        prop:spectral-sequence-collapse, prop:wedderburn-trace-identity,
        thm:jones-markov-trace, prop:archimedean-realization-functor.
-/

import Mathlib.Data.Real.Basic
import Mathlib.Data.Rat.Defs
import Mathlib.Data.Fintype.Fin
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

namespace QOU.BraidKnot

open Finset

/-! ## Abstract carriers for the atom-knot mass pipeline

The end-to-end derivation is *irreducibly abstract* over the
(un-formalised) categorical pipeline `T_w ↦ tr_M(T_w) ↦ B(𝔥)`.  Rather
than fake a proof (the old `: True := trivial` bodies), each leg is
**named** as a `Prop` over the minimal data it relates (playbook
pattern C, §3b "naming is not a logical claim").  A proof awaits the
GB-spectral-sequence + Wedderburn + Archimedean-functor
infrastructure. -/

/-- Categorical pipeline datum for a canonical word `T_w`: the
    Wedderburn block index set `Λ`, the Wenzl weights `y_λ ∈ ℚ`, the
    `q`-Murnaghan–Nakayama characters `χ_λ ∈ ℚ`, and the resulting
    Markov-trace value `traceVal ∈ ℚ`. -/
structure CategoricalLeg (T_w : Type*) where
  /-- Number of Wedderburn blocks (partitions `λ ⊢ n`). -/
  blocks : ℕ
  /-- Wenzl weights `y_λ(q)` (rational at the substrate slice). -/
  y : Fin blocks → ℚ
  /-- `q`-Murnaghan–Nakayama characters `χ_λ(T_w)`. -/
  χ : Fin blocks → ℚ
  /-- The Markov trace value `tr_M(T_w) ∈ ℚ(q)` at the slice. -/
  traceVal : ℚ

/-- **Categorical leg → finite-sum Markov trace.**

    From the GB-filtered structure of `T_w`, the GB spectral sequence
    collapses at `E_2` (Hecke quadratic), so the `E_∞` page is the
    Wedderburn decomposition and the Markov trace is the finite
    Frobenius pairing `tr_M(T_w) = Σ_λ y_λ(q) χ_λ(T_w)`.

    Named here as the `Prop` asserting that the leg's `traceVal` equals
    this finite sum (pattern C); the structural derivation
    (Yekutieli finite slice + `E_2` collapse + Wenzl + `q`-MN) is the
    open categorical input.

    Ref: [leitner2026] prop:gb-spectral-sequence +
         prop:spectral-sequence-collapse +
         prop:e-infinity-page-identifications. -/
def categorical_leg_to_markov_trace {T_w : Type*} (L : CategoricalLeg T_w) : Prop :=
  L.traceVal = ∑ i, L.y i * L.χ i

/-- Archimedean realization datum: the categorical leg, the SDP
    multiplicity `ρ ∈ ℕ_{>0}`, the electron mass scale `m_e`, the
    realified trace value `traceAtQ0 = ι(traceVal)|_{q = q_0} ∈ ℝ`, and
    the resulting mass `B ∈ ℝ` in MeV. -/
structure ArchimedeanRealization (T_w : Type*) where
  /-- The categorical leg producing `tr_M(T_w) ∈ ℚ(q)`. -/
  leg : CategoricalLeg T_w
  /-- SDP multiplicity `ρ` of `T_w`'s solution in Wedderburn. -/
  ρ : ℕ
  /-- `ρ` is positive (`ρ ∈ ℕ_{>0}`). -/
  ρ_pos : 0 < ρ
  /-- Electron mass scale `m_e` (MeV). -/
  m_e : ℝ
  /-- The Archimedean realization `ι(tr_M(T_w))|_{q = q_0} ∈ ℝ`. -/
  traceAtQ0 : ℝ
  /-- The realised mass `B(𝔥) ∈ ℝ` (MeV). -/
  B : ℝ

/-- **Archimedean realization ℚ(q) → ℝ at `q = q_0`.**

    `M(𝔥) = ρ · tr_M(T_w) ∈ ℚ(q)`, then
    `B(𝔥) := m_e · ρ · ι(tr_M(T_w))|_{q = q_0} ∈ ℝ` (MeV).

    Named as the `Prop` relating the realised mass `B` to the
    electron scale, the SDP multiplicity, and the realified trace
    (pattern C).  Ref: [leitner2026] prop:archimedean-realization-functor. -/
def archimedean_realization_to_mev {T_w : Type*}
    (A : ArchimedeanRealization T_w) : Prop :=
  A.B = A.m_e * (A.ρ : ℝ) * A.traceAtQ0

/-- **Post-Archimedean naming (BORROWED, optional, NOT in derivation).**

    For hyperbolic `K = ^T_w`, conventional 3-manifold theory names
    `B(𝔥)/(ρ · m_e)` as `Vol_hyp(K)`, justified post-Archimedean by the
    volume conjecture [kashaev1997], [murakami-murakami2001], Mostow
    rigidity [mostow1968], and the Gromov norm [gromov1982],
    [thurston1978].  All three are borrowed theorems on the
    post-functor side; none is used in the QOU mass derivation.

    Named as the `Prop` asserting the naming identity
    `volName · (ρ · m_e) = B` (pattern C); the borrowed-theorem content
    is the optional input. -/
def post_archimedean_naming_borrowed {K : Type*}
    (A : ArchimedeanRealization K) (volName : ℝ) : Prop :=
  volName * ((A.ρ : ℝ) * A.m_e) = A.B

/-- **The full proof of `conj:atom-knot-mass-derivation`.**

    The end-to-end claim is the conjunction of the two derivation legs:
    the categorical leg (finite-sum Markov trace) and the Archimedean
    realization (MeV mass).  The post-Archimedean naming is *optional*
    (not part of the derivation) and is therefore not a conjunct.

    Named as a `Prop` over the realization datum (pattern C): the
    pipeline `T_w ↦ tr_M(T_w) ∈ ℚ(q) ↦ B(𝔥) ∈ ℝ` holds.  A proof
    awaits the categorical + Archimedean-functor infrastructure. -/
def atom_knot_mass_derivation_proof {T_w : Type*}
    (A : ArchimedeanRealization T_w) : Prop :=
  categorical_leg_to_markov_trace A.leg ∧ archimedean_realization_to_mev A

end QOU.BraidKnot
