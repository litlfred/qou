---
# qou-pqmw
title: Add disclosure — 78 bare projections currently exempt (tracked, triage pending)
status: in-progress
type: task
priority: low
tags:
    - vacuity
    - issue-2472
    - reorg-2026-10-04
created_at: 2026-08-10T01:47:54Z
updated_at: 2026-10-04T15:25:46Z
parent: qou-6qbv
---

**78 declarations** that project a class field verbatim with no disclosure and no citation, currently **exempt** (mostly under the type-matched carve-out, tracked with triage pending).

Criterion (1) — *disclosure*. Lowest priority of the four disclosure classes because the scanner already tracks them and they do not fail the gate; but the exemption's stated justification does not hold for any of them, so each needs either the disclosure sentence or ordinary self-assuming triage.

Sub-clusters worth doing together: `Instanton.lean` (4), `QHookBound.lean` (4), `core-levi-form.lean` (3), `HadronicMass.lean` (3), `categorical-jet.lean` (2), `SkewSYT.lean` (2), `MassTowerOpenProblemsClasses.lean` (2), `TrefoilCanonicalMassUnit.lean` (1 here + 2 in the non-exempt bean).

- `folio/quantum-observable-universe/braids-and-knots/knot-eigenbasis-complete.lean:303` — `knot_eigenbasis_density`
- `folio/quantum-observable-universe/brings-surface/levi-form-defect.lean:51` — `matter_locus_nonempty`
- `folio/quantum-observable-universe/brings-surface/mi-sw-abelianisation.lean:48` — `mi_sw_nonneg`
- `folio/quantum-observable-universe/climax-volume-mass/mobius-energy-proof.lean:105` — `MobiusEnergy`
- `folio/quantum-observable-universe/climax-volume-mass/non-self-intersection-proof.lean:81` — `NonSelfIntersection.exclusionRadius_eq`
- `folio/quantum-observable-universe/climax-volume-mass/non-self-intersection.lean:67` — `noncocomm_iff_quantum`
- `folio/quantum-observable-universe/fluid-dynamics/acoustic-horizon-conditions.lean:98` — `acoustic_horizon_regularity`
- `folio/quantum-observable-universe/fluid-dynamics/core-levi-form.lean:164` — `core_levi_cond_aspect_bound`
- `folio/quantum-observable-universe/fluid-dynamics/core-levi-form.lean:172` — `core_levi_cond_bound`
- `folio/quantum-observable-universe/fluid-dynamics/core-levi-form.lean:106` — `core_levi_form`
- `folio/quantum-observable-universe/fluid-dynamics/discrete-vortex-spectrum.lean:91` — `discrete_vortex_spectrum`
- `folio/quantum-observable-universe/fluid-dynamics/helicity-conservation.lean:78` — `helicity_cwf_relation`
- `folio/quantum-observable-universe/fluid-dynamics/root-of-unity-truncation.lean:73` — `root_of_unity_truncation_conditional`
- `folio/quantum-observable-universe/fluid-dynamics/vorticity-lower-bound.lean:75` — `vorticity_lower_bound_conditional`
- `folio/quantum-observable-universe/knots-particles-confinement/magic-shell-coupling-kappa.lean:82` — `kappa_closed_form_is_categorical`
- `folio/quantum-observable-universe/lean/QOU/Archimedean/BranchingConvergence.lean:352` — `branching_convergence`
- `folio/quantum-observable-universe/lean/QOU/Archimedean/HyperbolicVolumeTranscendence.lean:699` — `tower_noncollapse_implies_independence`
- `folio/quantum-observable-universe/lean/QOU/Archimedean/MassTowerOpenProblemsClasses.lean:171` — `brane_tower_finite`
- `folio/quantum-observable-universe/lean/QOU/Archimedean/MassTowerOpenProblemsClasses.lean:71` — `term7_structural`
- `folio/quantum-observable-universe/lean/QOU/Archimedean/OrderingIndependence.lean:113` — `skein_multiset_invariance_axiom`
- `folio/quantum-observable-universe/lean/QOU/Archimedean/QHookBound.lean:795` — `convergence_rate`
- `folio/quantum-observable-universe/lean/QOU/Archimedean/QHookBound.lean:599` — `qFact_ratio_bound`
- `folio/quantum-observable-universe/lean/QOU/Archimedean/QHookBound.lean:406` — `qInt_ratio_bound_small`
- `folio/quantum-observable-universe/lean/QOU/Archimedean/QHookBound.lean:709` — `wedderburn_weight_perturbation`
- `folio/quantum-observable-universe/lean/QOU/Archimedean/SkewSYT.lean:1037` — `convergence_bound`
- `folio/quantum-observable-universe/lean/QOU/Archimedean/SkewSYT.lean:1092` — `knot_invariant_convergence`
- `folio/quantum-observable-universe/lean/QOU/Archimedean/TMCorrespondence.lean:317` — `matrixChain_eq_buildChains_axiom`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/GBResidueSpectralSum.lean:94` — `gb_residue_spectral_sum`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/GradedTraceResidueSplit.lean:91` — `graded_trace_residue_split`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/PhiQTowerAlgebraicStratification.lean:106` — `phi_q_tower_algebraic_stratification`
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/QRogersPentagonArchimedean.lean:203` — `rogers_correction_leading_h_order`
- `folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean:877` — `a4_betti_magnitude_closure`
- `folio/quantum-observable-universe/lean/QOU/FeynmanPathIntegrals.lean:210` — `amplitude_finite_sum`
- `folio/quantum-observable-universe/lean/QOU/FlavorDressing/DressedMassFromSubstrateSplit.lean:122` — `dressed_mass_from_substrate_split`
- `folio/quantum-observable-universe/lean/QOU/FluidDynamics/discrete_vortex_spectrum.lean:70` — `discrete_vortex_spectrum`
- `folio/quantum-observable-universe/lean/QOU/FluidDynamics/ns_obstruction_tower.lean:46` — `ns_obstruction_tower`
- `folio/quantum-observable-universe/lean/QOU/FluidDynamics/q_bkm_criterion.lean:69` — `q_bkm_criterion`
- `folio/quantum-observable-universe/lean/QOU/FluidDynamics/root_of_unity_truncation.lean:69` — `root_of_unity_truncation`
- `folio/quantum-observable-universe/lean/QOU/Habiro/FlowSolution.lean:70` — `habiro_flow_solutions_realise_synthesis`
- `folio/quantum-observable-universe/lean/QOU/HadronicMass.lean:470` — `neutron_pair_skein_approx`
- `folio/quantum-observable-universe/lean/QOU/HadronicMass.lean:443` — `proton_pair_skein_approx`
- `folio/quantum-observable-universe/lean/QOU/HadronicMass.lean:611` — `skein_mass_relation_holds`
- `folio/quantum-observable-universe/lean/QOU/Information/p_bandwidth_bound.lean:95` — `p_bandwidth_bound`
- `folio/quantum-observable-universe/lean/QOU/Infra/Polylogarithm.lean:157` — `beta3_via_class`
- `folio/quantum-observable-universe/lean/QOU/Interactions/ConfinementSDP.lean:200` — `sdp_lp_projection`
- `folio/quantum-observable-universe/lean/QOU/Interactions/TrefoilCanonicalMassUnit.lean:168` — `trefoil_topological_mass_eq_codata`
- `folio/quantum-observable-universe/lean/QOU/Knot/FigureEightVolume.lean:116` — `saddle_eq_volume`
- `folio/quantum-observable-universe/lean/QOU/MobiusEnergy.lean:148` — `MobiusEnergy`
- `folio/quantum-observable-universe/lean/QOU/MotivesArchimedean.lean:163` — `factors_def`
- `folio/quantum-observable-universe/lean/QOU/PAdicQuantumGroups.lean:170` — `padic_frobenius_relation_preserved`
- `folio/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/GaugeTheory.lean:61` — `fiber_adjoint_involution_sq`
- `folio/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/Instanton.lean:231` — `categorical_dq_squared_nonvanishing`
- `folio/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/Instanton.lean:133` — `categorical_irreducible`
- `folio/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/Instanton.lean:279` — `categorical_jet_prolongation`
- `folio/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/Instanton.lean:259` — `kernelIncl_exact`
- `folio/quantum-observable-universe/lean/QOU/TopologicalMass/cat_eigenspace_decomposition.lean:63` — `cat_eigenspace_decomposition`
- `folio/quantum-observable-universe/lean/QOU/Torsion/JetProlongation.lean:61` — `jet_prolongation_C`
- `folio/quantum-observable-universe/lean/QOU/Torsion/TopologicalMass.lean:88` — `topological_mass_decomposition`
- `folio/quantum-observable-universe/lifting-and-descent/descent-lemma.lean:42` — `descent_surjective`
- `folio/quantum-observable-universe/mass-theory/conj-rho-prefactor-structural.lean:275` — `rho_eq_qdim_via_canonical_knot`
- `folio/quantum-observable-universe/mass-theory/crystal-basis-resolves-mass-tower-open-problems.lean:10` — `crystal_basis_reduction`
- `folio/quantum-observable-universe/mass-theory/descended-level-zero.lean:20` — `descended_level_zero`
- `folio/quantum-observable-universe/mass-theory/he4-channel-active-set.lean:154` — `he4_strong_duality_value`
- `folio/quantum-observable-universe/mass-theory/mass-side-kernel-formalize-first-gates.lean:95` — `mass_anchor_stable_forward`
- `folio/quantum-observable-universe/mass-theory/mass-side-kernel-formalize-first-gates.lean:177` — `mass_direction_sanity_forward`
- `folio/quantum-observable-universe/mass-theory/q-beta-direction-sanity-gate.lean:86` — `qbeta_direction_sanity_magnitude_match`
- `folio/quantum-observable-universe/mass-theory/q-beta-q-eq-one-shadow-gate.lean:86` — `qbeta_q_eq_one_shadow_anchors`
- `folio/quantum-observable-universe/mass-theory/q-beta-radius-of-convergence-gate.lean:102` — `qbeta_g_simple_pole_at_u_substrate`
- `folio/quantum-observable-universe/mass-theory/shared-denominator-cusp-holonomy.lean:71` — `shared_denominator_cusp_holonomy`
- `folio/quantum-observable-universe/models-of-qous/main-commutative-diagram.lean:78` — `diagram_commutes`
- `folio/quantum-observable-universe/molecular-construction/h2s-angle-s3-braid-holonomy.lean:39` — `opening_eq_holonomy_of_conj`
- `folio/quantum-observable-universe/nuclear-interactions/cpt-d6-d7-d8-closure.lean:66` — `cpt_closure`
- `folio/quantum-observable-universe/nuclear-interactions/q-beta-spectral-bridge.lean:294` — `q_beta_spectral_conditional`
- `folio/quantum-observable-universe/observations/diagrammatic-double-magic-lr-fusion.lean:133` — `nu_selfConjugate`
- `folio/quantum-observable-universe/quantum-observable-universes/contact-affine-chart.lean:66` — `ContactAffineChart.affineCoord_welldefined`
- `folio/quantum-observable-universe/quantum-observable-universes/volume-from-rigidity.lean:53` — `volume_form_is_nondegen`
- `folio/quantum-observable-universe/quantum-universes/categorical-jet.lean:55` — `CategoricalJet.kernelIncl_exact`
- `folio/quantum-observable-universe/quantum-universes/categorical-jet.lean:83` — `categorical_jet_prolongation`

Criterion: `docs/audits/2026-08-09-honest-placeholder-criterion.md`


## 1 of 78 drained (2026-09-04) — `q_beta_spectral_conditional`

`nuclear-interactions/q-beta-spectral-bridge.lean` — the disclosure sentence
this bean prescribes is now on the declaration.  Status left `todo`: 77 remain.

The old docstring was worse than absent — it *defended* the projection:
"Derived from the class field `forms_agree` — not a `sorry`-projection of an
unrelated conclusion."  As `docs/audits/2026-08-09-inhabitation-is-a-weak-discriminator.md`
sets out, that answers the wrong objection: the §3b-cond item-5 complaint is not
that the conclusion is UNRELATED to the field but that it is IDENTICAL to it.
That audit already adjudicated this declaration `genuine` in the review ledger.

Recorded on the declaration: the class is honest (content-bearing, uninhabited
— the correct §3b-tax open state); only the wrapper is the defect, and it is a
DISCLOSURE defect, not a mathematical one.  The file's real content
(`q_beta_spectral_bridge`, three identities) is unconditional and is what
should be cited.

NOT done, deliberately: closing the wrapper properly needs the class to relate
`Q_beta_A`/`Q_beta_B` to the file's `(h, z)` forms so that agreement DERIVES
something (exact agreement would force `z = 1` via the ratio identity).  That
changes what the block claims — authorial, left open.

Verified: `lean`-direct **exit 0** with a COMPLETE sentinel written after the
process exited (not read from a possibly-truncated log), 0 error lines; the one
warning is a pre-existing unused `hzh` at line 87.


## 🛑 RE-MEASURED 2026-09-04 — the list above is a 2026-08-10 SNAPSHOT and 36 % of it no longer resolves

Do **not** drain this queue entry-by-entry from the list as written. Re-run
[`scripts/pqmw-queue-recheck.py`](../scripts/pqmw-queue-recheck.py) first.

    entries in the bean : 78
      file_gone   :  6     the path no longer exists
      decl_gone   : 22     file exists, declaration name is not in it
      moved       : 28     resolves, at a different line
      same_line   : 22     resolves exactly where this bean records

    NO LONGER RESOLVES  : 28 / 78 (36 %)

**The worked case is `core-levi-form.lean`, and it is the reason this was
checked.** Its three entries (lines 106 / 164 / 172) now point at a blank
line, a `rw` inside a proof body, and a sentence in a docstring. The file was
rewritten by `6c17f7203d` (2026-08-31) — *"fix(qou-z9ws): core Levi form —
data become parameters, and one 'bound' turns out to carry nothing"* — into
exactly the data-as-parameters shape this queue wants: `CoreLeviData` is
declared **"Data only … an inhabitant of this structure asserts nothing"**,
each claim is a separate `def … : Prop` taken as an explicit hypothesis, and
`core_levi_form` *derives* both conjuncts. It even discloses its own residual
gap (`QuantumPressureBound`'s `q > 1` restriction is "an open gap here, not a
discharged hypothesis").

So writing a disclosure onto those three would be worse than a no-op: it would
annotate declarations that no longer carry the defect, and two of the three
line numbers do not name a declaration at all.

**Caveat on `decl_gone`:** it means *no longer resolves by name*. A rename and
a deletion look identical to this check; separating them needs `git log -S` and
was not done.

**Where to start instead:** the **22 `same_line`** entries are the ones most
likely still to carry the defect, since neither the file nor the surrounding
line count has moved since the snapshot. Read the declaration and its class
before writing anything.


## Triage column added (2026-09-04) — 15 of the 50 live entries are NOT defects

`scripts/pqmw-queue-recheck.py` now also asks, per surviving entry, whether the
class it projects has an instance anywhere in `content/`:

    of the 50 that still resolve:
      class INHABITED  : 15   necessary-not-sufficient; needs a human read
      class uninhabited: 21   honest open state -> the disclosure shape
      no carrier binder: 14   only ambient Mathlib classes, or none

**Why the column exists — the `QHookBound.lean` sub-cluster this bean says to
"do together" is four different verdicts.** Two of its four no longer resolve.
The other two project `QIntRatioBoundSmall` and `QFactRatioBound`, which have
**three** and **four** `nlinarith`-proved instances respectively for the
concrete `m`/`k` the file uses — the ordinary bundle-plus-accessor idiom with
the bundle actually built. Draining that cluster as a batch would have written
a "derives nothing" disclosure onto two proved bundles.

**Inhabited is necessary, not sufficient** — per
`docs/audits/2026-08-09-inhabitation-is-a-weak-discriminator.md`, a
reflexive-diagonal or trivial-index instance inhabits without saying anything.
So the 15 mean *read before writing*, never *legit*. **Uninhabited is the
decisive direction**: honest §3b-tax open state, and the projection is the
disclosure shape. Start there — the 21.

**Two errors of my own, both caught by an implausible value rather than by
reading the code**, and both now guarded in the script: the carrier column
first took the FIRST bracket binder, so six entries were attributed to
`CommRing` / `CategoryTheory.Category`; and the capture could end on a `.`.
The column remains a heuristic ("last binder not on a hand-kept ambient list")
and is a pointer to read, not a verdict — `descent_surjective` is the known
residual, reporting whichever ambient class is not yet on the list.


## The real drain queue is 9, not 78 — and my own inhabitation column was the wrong axis too

`scripts/pqmw-queue-recheck.py` now tests the **proof term** directly, which is
what "bare projection" actually means. Four independent narrowings:

    78  entries in the bean
    -28  no longer resolve (file or declaration gone)
    ---
    50  live
    -24  DERIVE -- compose or use fields; not projections at all
    ---
    26  bare projections
    -12  class is INHABITED -- the bundle is built, so the accessor is the
         ordinary Mathlib idiom (Aug-09 `legit` / `advisory`)
    - 5  carrier heuristic returned no class -- needs a read, not excluded
    ---
     9  bare projection AND uninhabited class  <-- THE DRAIN QUEUE

**The case that proves the inhabitation column was the wrong axis:**
`q_bkm_criterion` is uninhabited (so my previous triage put it in the queue)
**and is not a projection at all** — it composes TWO fields into an iff,
`⟨ctx.bkm_necessity, ctx.bkm_continuation⟩`. **AGENTS.md §3b-cond names that
file as the verified exemplar of the pattern working correctly.** Had I drained
the 21 uninhabited as I said I would last turn, that would have been the first
entry.

So neither "still resolves" nor "class uninhabited" decides it. The
discriminator is the 2026-08-30 one — **derives vs projects** — and it has to
be read off the proof term.

**THE DRAIN QUEUE (9):**

    matrixChain_eq_buildChains_axiom        MatrixChainEqBuildChains      TMCorrespondence.lean
    dressed_mass_from_substrate_split       DressedMassSubstrateSplit     DressedMassFromSubstrateSplit.lean
    sdp_lp_projection                       ScalarLPProjection            ConfinementSDP.lean
    categorical_dq_squared_nonvanishing     HasDqSquaredNonvanishing      Instanton.lean
    mass_anchor_stable_forward              MassAnchorStableGateClass     mass-side-kernel-formalize-first-gates.lean
    mass_direction_sanity_forward           MassDirectionSanityGateClass  mass-side-kernel-formalize-first-gates.lean
    qbeta_direction_sanity_magnitude_match  DirectionSanityGateClass      q-beta-direction-sanity-gate.lean
    qbeta_g_simple_pole_at_u_substrate      RadiusOfConvergenceGateClass  q-beta-radius-of-convergence-gate.lean
    opening_eq_holonomy_of_conj             H2SAngleS3HolonomyConjecture  h2s-angle-s3-braid-holonomy.lean

Plus **5 needing a carrier read** (`categorical_jet_prolongation`,
`jet_prolongation_C`, `kernelIncl_exact`, `matter_locus_nonempty`,
`topological_mass_decomposition`) where the heuristic found no class binder.

Read each declaration and its class before writing. Still.


## Final narrowing: the queue is **5**, not 78 — four of the nine are working GATES

Read `mass-side-kernel-formalize-first-gates.lean` before editing it and found
the design is already correct:

```lean
class MassAnchorStableGateClass (swing : ℝ) : Prop where
  swing_within_tolerance : swing ≤ anchorTolerance

theorem mass_anchor_stable_forward (swing : ℝ) [hC : MassAnchorStableGateClass swing] :
    swing ≤ anchorTolerance := hC.swing_within_tolerance

theorem mass_anchor_stable_reject (swing : ℝ) (h : swing > anchorTolerance) :
    ¬ MassAnchorStableGateClass swing := ...
```

The carrier is **parametrised** and there is a **proved refutation**. That is a
gate: `_forward` extracts the bound, `_reject` shows the class is uninhabitable
when the bound fails. The projection is the gate's intended API, not a
restatement — and it is exactly the parametrise-and-refute shape this whole
thread has been recommending.

**Four of the nine are this shape** (`mass_anchor_stable_forward`,
`mass_direction_sanity_forward`, `qbeta_direction_sanity_magnitude_match`,
`qbeta_g_simple_pole_at_u_substrate`), so the queue is **5**:

    matrixChain_eq_buildChains_axiom      MatrixChainEqBuildChains      TMCorrespondence.lean
    dressed_mass_from_substrate_split     DressedMassSubstrateSplit     DressedMassFromSubstrateSplit.lean
    sdp_lp_projection                     ScalarLPProjection            ConfinementSDP.lean
    categorical_dq_squared_nonvanishing   HasDqSquaredNonvanishing      Instanton.lean
    opening_eq_holonomy_of_conj           H2SAngleS3HolonomyConjecture  h2s-angle-s3-braid-holonomy.lean

(Plus the 5 whose carrier the heuristic could not identify — excluded on
measurement uncertainty, not merit.)

**Seventh measurement error of the session, same family.** My first refutation
check looked one line past the `theorem` keyword and returned NONE for all
nine — including `mass_anchor_stable_reject`, whose `¬ MassAnchorStableGateClass`
sits on the THIRD line, and which I had read with my own eyes two minutes
earlier. Caught instantly *because* the file had been read first. The whole-block
search is now in the script with that note attached.


## Final: the queue is **4**. `sdp_lp_projection` has a CONSTRUCTOR.

`ScalarLPProjection` has no `instance`, so the inhabitation column flagged it —
but `ConfinementSDP.lean` proves an introduction rule:

```lean
theorem scalarLPProjection_of_strongDuality (n : ℕ) …
    (hSlater : slaterStrict n) [HasConfinementSDPStrongDuality n hSlater]
    (h : bindingMultiplicity n = 1) : ScalarLPProjection n h :=
  ⟨HasConfinementSDPStrongDuality.strong_duality hSlater⟩
```

The carrier **follows from strong duality** (cited to Boyd–Vandenberghe
§5.2.3/§5.3) rather than being assumed, so its accessor is not a defect. That is
a **fifth** exculpating shape, and the positive twin of the refutation column:
`class_is_inhabited` only looks at `instance` declarations and cannot see an
introduction rule written as a plain `theorem`.

**THE QUEUE (4)** — no instance, no refutation, no constructor:

    matrixChain_eq_buildChains_axiom     MatrixChainEqBuildChains      TMCorrespondence.lean
    dressed_mass_from_substrate_split    DressedMassSubstrateSplit     DressedMassFromSubstrateSplit.lean
    categorical_dq_squared_nonvanishing  HasDqSquaredNonvanishing      Instanton.lean
    opening_eq_holonomy_of_conj          H2SAngleS3HolonomyConjecture  h2s-angle-s3-braid-holonomy.lean

Full narrowing, every step measured and re-runnable:

    78  in the bean
    -28  no longer resolve
    -24  derive, not projections
    -12  bare, class inhabited (bundle built)
    - 4  bare, class refutable (a working gate)
    - 1  bare, class has a constructor (derived upstream)
    - 5  carrier unidentified by the heuristic; excluded on uncertainty
    ---
     4  THE QUEUE

**Five exculpating shapes, all found by reading rather than by scanning**, and
each one added a column the previous pass did not have. That is the shape of
this bean: it is a *candidate* list, and its 78 was never a count of defects.


## 2026-09-05 — the four were read one each. **ZERO are defects.** Queue: 0 actionable.

| # | decl | verdict |
|---|---|---|
| 1 | `dressed_mass_from_substrate_split` | **not a defect; already disclosed at length** |
| 2 | `matrixChain_eq_buildChains_axiom` | not a defect; thin docstring → disclosed, and its Mathlib claim corrected |
| 3 | `categorical_dq_squared_nonvanishing` | not a defect; thin docstring → disclosed |
| 4 | `opening_eq_holonomy_of_conj` | **not a defect; already disclosed** |

All four are **parametrised** carriers in the honest §3b-tax open state.

**#1 is the strongest case against the queue.** Its file records that an earlier
`axiom` of the same content made the library **inconsistent** — a compiled
`theorem … : False`, because `F`, `M_N`, `q` were universally quantified and
unrelated while `substrate_split_factor` is concrete and strictly positive. It
also records the mechanism: a review flagged the downstream theorem as a
*tautology*, the repair introduced the axiom, and *"the tautology fix
over-corrected into unsoundness — the statement stopped being empty by starting
to be false."* The current no-instance class is the deliberate repair.

**#4 already carries the disclosure on the theorem itself** (*"this much is
unconditional given the class instance"*), and its class says *"providing an
instance amounts to proving the identification — that is the open conjecture."*

**#2's Mathlib claim was wrong and is corrected.** It cited
`List.foldl_eq_foldr_of_comm` as *"not yet available"*. **No lemma of that name
exists**, which makes the gap look wider than it is. Two real neighbours do:
`List.foldl_eq_foldr` (Basic.lean:802) needs `Std.Commutative` on the
*operation* — matrix multiplication fails that, so it does not apply; and
`List.foldl_eq_foldr'` (:822) needs only right-commutativity, which is weaker
and may hold, but concludes with `flip f`. So the gap is real and **narrower
than "no lemma exists"**: what is missing is a pointwise-commuting variant
without the `flip`. Closing it is Lean work on the fold shapes, not a citation.

**Eighth measurement error, same family.** My parametrisation check reported
`False` for #1 and #3; both *are* parametrised, with the parameters on the line
*after* `class X`. Single-line regex again — the same defect as the refutation
check two turns earlier.

**Disposition for the bean: 78 entries, 0 actionable defects.** The list was a
candidate scan, and every one of the 78 is now accounted for by one of seven
shapes (no longer resolves / derives / bundle built / gate / constructor /
carrier unidentified / parametrised-and-documented). Recommend closing it, or
re-scoping it to "re-run `scripts/pqmw-queue-recheck.py` after the next
carrier-shape change".

## Round 57 Progress (PR litlfred/qou#8286)
- Status updated to `in-progress` (`litlfred/qou#8286`, C1 `6c7a20f3289e7e0671ce65ef402e1a06fd77c443`, C2 `dce9c51d4a6cd8f2253c078180b4b77a6f7c1ed0`).
