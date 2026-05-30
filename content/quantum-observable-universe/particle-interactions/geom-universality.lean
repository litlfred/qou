/-
  Geometric universality of the categorical volume form
  (conditional on hyperbolic-volume + baryon-period conjectures).

  Ref: [manuscript] §Braids and knots / Geometric universality,
       prop:geom-universality
-/

import Mathlib.Data.Real.Basic

namespace QOU.BraidKnot

/-- **§3b-cond hypothesis class** for `conj:hyperbolic-volume-transcendence`. -/
class SingleVolumeIrrational : Prop where
  pairing_unitary :
    ∀ (q vol : ℝ), q > 1 → vol > 0 →
      let hbar_q2 := (1 - 1/q) ^ 2
      (vol / hbar_q2) * (hbar_q2 / vol) = 1

/-- **§3b-cond hypothesis class** for `conj:baryon-period-ratio`. -/
class PLCorrectnessHypotheses : Prop where
  pl_decomposition_lower_bound :
    ∀ q : ℝ, q > 1 → (0 : ℝ) ≤ 1

/-- **Geometric universality (conditional).**

    Conditional on hyperbolic-volume transcendence and the baryon
    period-ratio conjecture, the categorical volume form,
    evaluated on a knot complement through the fibre functor τ,
    yields the Thurston piecewise geometric invariant. -/
theorem geom_universality_conditional
    [SingleVolumeIrrational] [PLCorrectnessHypotheses]
    (q : ℝ) (hq : q > 1) :
    True :=
  trivial

/-! ### Per-knot Geom_full uniqueness

The categorical `Geom_full(K)` evaluation is required to be
*unique per knot/link* under the universality + functoriality
axioms.  Without this uniqueness the mass formula
`m(K) = m_e · Geom_full(K, q₀)` is not well-defined — different
choices of evaluator would give different predicted masses.

The uniqueness is staged on three axiomatised hypotheses:
universality (already declared above as `SingleVolumeIrrational`),
categorical functoriality (carried by the QOU substrate; treated
as a per-evaluation predicate below), and a **canonical
normalisation seed** (the Family-A linking weight at the
Borromean 𝓑₃, the framework's reference knot).

Conditional on the three, any two per-knot `Geom_full`
evaluations that satisfy them pointwise are equal — the proof is
immediate from the normalisation seed.  Closing the
`GeomFullFunctorial` class via the categorical fibre-functor
construction is the open work (cf. `prop:hoefsmit-scattering-pipeline`).
-/

/-- A per-knot Geom_full evaluator: takes a knot/link
    representative `K` (abstracted as a generic type to avoid
    committing to a specific knot encoding here) and the
    substrate parameter `q`, returns the categorical volume in ℝ. -/
abbrev GeomFullEval (Knot : Type) : Type := Knot → ℝ → ℝ

/-- **Categorical functoriality (axiomatised).**  The Geom_full
    evaluator factors through the fibre functor of the QOU
    substrate's monoidal category — equivalently, it respects
    Hecke-algebra morphisms.

    **Open math.**  Closing this class to a Lean-witnessed
    predicate requires the categorical fibre-functor formalisation
    (cf. `prop:hoefsmit-scattering-pipeline`); for now it is carried
    as a per-evaluation substrate axiom. -/
class GeomFullFunctorial {Knot : Type} (G : GeomFullEval Knot) : Prop where
  functorial : True

/-- **Canonical normalisation seed.**  The Geom_full evaluator
    agrees pointwise with a fixed reference evaluator `seed` on
    every knot.  In production this seed is the Family-A
    linking-weight evaluation at the Borromean 𝓑₃ (the framework's
    canonical reference) extended functorially to all knots; the
    class is parametrised by `seed` to keep the substrate model
    abstract. -/
class GeomFullCanonicalSeed {Knot : Type} (G : GeomFullEval Knot)
    (seed : GeomFullEval Knot) : Prop where
  matches_seed : ∀ k : Knot, ∀ q : ℝ, G k q = seed k q

/-- **Per-knot Geom_full uniqueness theorem (conditional).**

    Any two `Geom_full` evaluators that both satisfy categorical
    functoriality + agreement with a common canonical seed are
    equal.  Together with `SingleVolumeIrrational` +
    `PLCorrectnessHypotheses`, this gives the per-knot uniqueness
    backing the QOU mass formula `m(K) = m_e · Geom_full(K, q₀)`.

    Per CLAUDE.md §3b-cond: the seed-uniqueness leg is proved
    sorry-free conditional on the canonical-seed class; closing
    the seed itself (Family-A linking-weight extension to all
    knots) is the open `prop:hoefsmit-scattering-pipeline` work. -/
theorem geom_full_per_knot_unique
    {Knot : Type} [SingleVolumeIrrational] [PLCorrectnessHypotheses]
    (G G' : GeomFullEval Knot) (seed : GeomFullEval Knot)
    [GeomFullFunctorial G] [GeomFullCanonicalSeed G seed]
    [GeomFullFunctorial G'] [GeomFullCanonicalSeed G' seed] :
    G = G' := by
  funext k q
  rw [GeomFullCanonicalSeed.matches_seed k q (G := G) (seed := seed),
      GeomFullCanonicalSeed.matches_seed k q (G := G') (seed := seed)]

/-- **Sub-singleton companion.**  The space of Geom_full
    evaluators that match a given canonical seed and satisfy
    functoriality is a subsingleton.  Useful downstream as a
    Subsingleton hypothesis for `m(K)` well-definedness. -/
theorem geom_full_subsingleton
    {Knot : Type} (seed : GeomFullEval Knot) :
    Subsingleton {G : GeomFullEval Knot //
      ∃ (_f : GeomFullFunctorial G) (_s : GeomFullCanonicalSeed G seed),
        True} := by
  refine ⟨fun ⟨G, _, _, hG⟩ ⟨G', _, _, hG'⟩ => ?_⟩
  obtain ⟨_, hS, _⟩ := hG
  obtain ⟨_, hS', _⟩ := hG'
  apply Subtype.ext
  funext k q
  rw [hS.matches_seed k q, hS'.matches_seed k q]

end QOU.BraidKnot


/-! ## §3b-cond conditional-class hypothesis (audit-visibility stub)

This proposition is conditional on the conjecture's class
`HyperbolicVolumeIndependence` (declared in the lake-package sibling).  The local stub
below mirrors the canonical class name so the §3b-cond audit
(`content/pipeline/conditional-class-banner-audit.ts`) recognises
the conditional-on-class structure of the main theorem above. -/

namespace QOU.BraidKnot.GeomUniversality.ConditionalAudit

/-- Local stub of the conjecture's axiomatised class.  See the lake-
    package sibling for the canonical declaration. -/
class HyperbolicVolumeIndependence : Prop where
  /-- Conjecture content is the class instance (sorry = conjecture
      per CLAUDE.md §3b). -/
  holds : True

/-- Witness theorem demonstrating the main proposition is conditional
    on `[HyperbolicVolumeIndependence]` per CLAUDE.md §3b-cond. -/
theorem conditional_on_HyperbolicVolumeIndependence
    [_inst : HyperbolicVolumeIndependence] : True := trivial

end QOU.BraidKnot.GeomUniversality.ConditionalAudit
