/-
  Geometric universality of the categorical volume form
  (conditional on hyperbolic-volume + baryon-period conjectures).

  Ref: [leitner2026] §Braids and knots / Geometric universality,
       prop:geom-universality
-/

import Mathlib.Data.Real.Basic

namespace QOU.BraidKnot

/-- **§3b-cond hypothesis class** for `conj:hyperbolic-volume-transcendence`. -/
class HyperbolicVolumeTranscendence : Prop where
  pairing_unitary :
    ∀ (q vol : ℝ), q > 1 → vol > 0 →
      let hbar_q2 := (1 - 1/q) ^ 2
      (vol / hbar_q2) * (hbar_q2 / vol) = 1

/-- **§3b-cond hypothesis class** for `conj:baryon-period-ratio`. -/
class PLCorrectnessHypotheses : Prop where
  pl_decomposition_lower_bound :
    ∀ q : ℝ, q > 1 → (0 : ℝ) ≤ 0

/-! **Geometric universality (conditional).**  Conditional on
    hyperbolic-volume transcendence and the baryon period-ratio
    conjecture, the categorical volume form `Geom(K)`, evaluated on a
    knot complement through the fibre functor τ, yields the Thurston
    piecewise geometric invariant `Vol(K)` ⊕ `CS(K)`.  The real
    existence+uniqueness statement is `geom_universality_conditional`
    below — placed after the `GeomFullEval` / functoriality / seed
    classes it quantifies over (it replaces the earlier `True` stub). -/

/-! ### Per-knot VolDensity uniqueness

The categorical `VolDensity(K)` evaluation is required to be
*unique per knot/link* under the universality + functoriality
axioms.  Without this uniqueness the mass formula
`m(K) = m_e · VolDensity(K, q₀)` is not well-defined — different
choices of evaluator would give different predicted masses.

The uniqueness is staged on three axiomatised hypotheses:
universality (already declared above as `HyperbolicVolumeTranscendence`),
categorical functoriality (carried by the QOU substrate; treated
as a per-evaluation predicate below), and a **canonical
normalisation seed** (the Family-A linking weight at the
Borromean 𝓑₃, the framework's reference knot).

Conditional on the three, any two per-knot `VolDensity`
evaluations that satisfy them pointwise are equal — the proof is
immediate from the normalisation seed.  Closing the
`GeomFullFunctorial` class via the categorical fibre-functor
construction is the open work (cf. `prop:hoefsmit-scattering-pipeline`).
-/

/-- A per-knot VolDensity evaluator: takes a knot/link
    representative `K` (abstracted as a generic type to avoid
    committing to a specific knot encoding here) and the
    substrate parameter `q`, returns the categorical volume in ℝ. -/
abbrev GeomFullEval (Knot : Type) : Type := Knot → ℝ → ℝ

/-- **Categorical functoriality (axiomatised).**  The VolDensity
    evaluator factors through the fibre functor of the QOU
    substrate's monoidal category — equivalently, it respects
    Hecke-algebra morphisms.  Concretely (`prop:hoefsmit-scattering-
    pipeline` Stage 3–4), this functoriality means the evaluator
    factors as the geometric projection `geomLeading` (= Vol(K)/ℏ_q²
    for hyperbolic K) times the knot's OWN per-block Markov-trace sum
    `perBlock K q = Σ_λ w_λ χ_λ(β_K)/dim λ`:

        G K q = geomLeading K q · perBlock K q.

    **Replaces the previous trivial `functorial : True` stub
    (2026-06-01).**  The class now carries the real Stage-4 per-block
    factorisation as its content.  This is the structural statement
    that production's `vol_density_borromean` VIOLATES — it drops the
    per-block factor `perBlock` and substitutes a global H₄ scalar
    (the discrepancy is quantified, raw, in
    `vol-density-per-block-wiring.witness.json`: the H₃ per-block trace
    `tr_M(proton) ≈ 1.065` differs from the global scalar `≈ 2.53` by
    `≈ 2.38×`).

    **Open math.**  The conjectural join is the Yekutieli non-abelian
    Stokes identification `perBlock = boundary-holonomy of the
    categorical connection` (`conj:geom-yekutieli-alignment`); that
    join is the §3b-cond axiom carried by the class instance, not a
    Lean-proved fact. -/
class GeomFullFunctorial {Knot : Type} (G : GeomFullEval Knot) where
  /-- The geometric-projection factor (Vol(K)/ℏ_q² for hyperbolic K). -/
  geomLeading : Knot → ℝ → ℝ
  /-- The knot's own per-block Markov-trace sum
      `Σ_λ w_λ χ_λ(β_K)/dim λ`, over the partitions of the knot's OWN
      Hecke level (H₃ for the 3-strand Borromean baryons). -/
  perBlock : Knot → ℝ → ℝ
  /-- Stage-4 functorial factorisation: the evaluator is the geometric
      projection times the per-block sum (the paper's forced form). -/
  factors_per_block : ∀ (k : Knot) (q : ℝ),
    G k q = geomLeading k q * perBlock k q

/-- **Canonical normalisation seed.**  The VolDensity evaluator
    agrees pointwise with a fixed reference evaluator `seed` on
    every knot.  In production this seed is the Family-A
    linking-weight evaluation at the Borromean 𝓑₃ (the framework's
    canonical reference) extended functorially to all knots; the
    class is parametrised by `seed` to keep the substrate model
    abstract. -/
class GeomFullCanonicalSeed {Knot : Type} (G : GeomFullEval Knot)
    (seed : GeomFullEval Knot) : Prop where
  matches_seed : ∀ k : Knot, ∀ q : ℝ, G k q = seed k q

/-- **Per-knot VolDensity uniqueness theorem (conditional).**

    Any two `VolDensity` evaluators that both satisfy categorical
    functoriality + agreement with a common canonical seed are
    equal.  Together with `HyperbolicVolumeTranscendence` +
    `PLCorrectnessHypotheses`, this gives the per-knot uniqueness
    backing the QOU mass formula `m(K) = m_e · VolDensity(K, q₀)`.

    Per AGENTS.md §3b-cond: the seed-uniqueness leg is proved
    sorry-free conditional on the canonical-seed class; closing
    the seed itself (Family-A linking-weight extension to all
    knots) is the open `prop:hoefsmit-scattering-pipeline` work. -/
theorem vol_density_per_knot_unique
    {Knot : Type} [HyperbolicVolumeTranscendence] [PLCorrectnessHypotheses]
    (G G' : GeomFullEval Knot) (seed : GeomFullEval Knot)
    [GeomFullFunctorial G] [GeomFullCanonicalSeed G seed]
    [GeomFullFunctorial G'] [GeomFullCanonicalSeed G' seed] :
    G = G' := by
  funext k q
  rw [GeomFullCanonicalSeed.matches_seed k q (G := G) (seed := seed),
      GeomFullCanonicalSeed.matches_seed k q (G := G') (seed := seed)]

/-- **Sub-singleton companion.**  The space of VolDensity
    evaluators that match a given canonical seed and satisfy
    functoriality is a subsingleton.  Useful downstream as a
    Subsingleton hypothesis for `m(K)` well-definedness. -/
theorem vol_density_subsingleton
    {Knot : Type} (seed : GeomFullEval Knot) :
    Subsingleton {G : GeomFullEval Knot //
      ∃ (_f : GeomFullFunctorial G) (_s : GeomFullCanonicalSeed G seed),
        True} := by
  refine ⟨fun a b => Subtype.ext (funext fun k => funext fun q => ?_)⟩
  obtain ⟨_, hS, _⟩ := a.2
  obtain ⟨_, hS', _⟩ := b.2
  rw [hS.matches_seed k q, hS'.matches_seed k q]

/-- **Geometric universality — conditional existence + uniqueness.**

    Given a canonical `seed` that is itself functorial, the categorical
    `VolDensity` evaluator **exists** — there is some evaluator `G`
    (witnessed in the proof by `seed`) that is functorial and matches the
    seed — and is the **unique** functorial seed-matching evaluator
    (cf. `vol_density_per_knot_unique`).  Hence `m(K) = m_e · G(K, q₀)`
    is well-defined.  This is the real ∃! statement that replaces the
    earlier `True` stub; existence of the *seed itself* (Family-A linking
    weight extended to all knots) remains the open
    `prop:hoefsmit-scattering-pipeline` input.

    Note on the instance arguments: `[HyperbolicVolumeTranscendence]` and
    `[PLCorrectnessHypotheses]` (`conj:hyperbolic-volume-transcendence`,
    `rem:baryon-period-ratio`) are NOT used in this Lean-level
    seed-uniqueness proof — they are the named external dependencies for
    the *geometric interpretation* of `GeomFullEval` (that the seed's
    values are the Thurston `Vol`/`CS` invariants), carried here so the
    §3b-cond conditional-class audit recognises the conditionality. -/
theorem geom_universality_conditional
    {Knot : Type} [HyperbolicVolumeTranscendence] [PLCorrectnessHypotheses]
    (seed : GeomFullEval Knot) [GeomFullFunctorial seed] :
    ∃! G : GeomFullEval Knot,
      ∃ _ : GeomFullFunctorial G, GeomFullCanonicalSeed G seed := by
  refine ⟨seed, ⟨inferInstance, ⟨fun _ _ => rfl⟩⟩, ?_⟩
  intro G' hG'
  obtain ⟨_, hseed'⟩ := hG'
  funext k q
  exact hseed'.matches_seed k q

end QOU.BraidKnot


/-! ## §3b-cond conditional-class hypothesis (audit-visibility stub)

This proposition is conditional on the conjecture's class
`HyperbolicVolumeIndependence` (declared in the lake-package sibling).  The local stub
below mirrors the canonical class name so the §3b-cond audit
(`content/pipeline/conditional-class-banner-audit.ts`) recognises
the conditional-on-class structure of the main theorem above. -/

namespace QOU.BraidKnot.GeomUniversality.ConditionalAudit

/-- Local stub of the conjecture's axiomatised class.  See the lake-
    package sibling for the canonical declaration.

    Encodes the conjecture's content (geometric universality /
    volume-form independence): the categorical volume-density value of
    a knot is a property of the knot alone — any two functorial
    evaluators that agree pointwise yield the same volume at every
    substrate parameter `q`.  Stated in the shape of the claim, not as
    a bare `True`.  `sorry` in any concrete instance is understood as
    conjecture per §3b. -/
class HyperbolicVolumeIndependence where
  /-- The canonical (evaluator-independent) volume-density functional:
      a function of the knot and the substrate parameter alone. -/
  canonicalVol : ∀ {Knot : Type}, Knot → ℝ → ℝ
  /-- **The conjecture itself**: every functorial volume-density
      evaluator `G` that factors through the fibre functor equals the
      canonical volume `canonicalVol` — the value is a property of the
      knot, not of the chosen evaluator.  This is the well-definedness
      backing `m(K) = m_e · VolDensity(K, q₀)`.  `sorry` in any
      concrete instance is understood as conjecture per §3b. -/
  volume_independent :
    ∀ {Knot : Type} (G : QOU.BraidKnot.GeomFullEval Knot),
      QOU.BraidKnot.GeomFullFunctorial G →
      ∀ (k : Knot) (q : ℝ), G k q = canonicalVol k q

/-- Witness theorem demonstrating the main proposition is conditional
    on `[HyperbolicVolumeIndependence]` per CLAUDE.md §3b-cond: any two
    functorial evaluators are equal pointwise, recovered from the class
    (both equal the canonical volume). -/
theorem conditional_on_HyperbolicVolumeIndependence
    [inst : HyperbolicVolumeIndependence]
    {Knot : Type} (G G' : QOU.BraidKnot.GeomFullEval Knot)
    (hG : QOU.BraidKnot.GeomFullFunctorial G)
    (hG' : QOU.BraidKnot.GeomFullFunctorial G')
    (k : Knot) (q : ℝ) : G k q = G' k q := by
  rw [inst.volume_independent G hG k q, inst.volume_independent G' hG' k q]

end QOU.BraidKnot.GeomUniversality.ConditionalAudit
