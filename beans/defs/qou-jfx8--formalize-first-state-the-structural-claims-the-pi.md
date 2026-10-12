---
# qou-jfx8
title: 'Formalize-first: state the structural claims the picture needs (shadow prices as directions of entanglement history; phase-space measure from the dual; relative Reeb angle as a jet-level datum) as Lean scaffolds or conjecture classes before any probe'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-16T00:47:53Z
updated_at: 2026-10-12T18:38:16Z
parent: qou-v2om
---

## 2026-09-16 — derived half landed; conjecture half held for the owner

LANDED: content/quantum-observable-universe/lean/QOU/MassTheory/BlockMeasureFromFrobeniusPairing.lean — FrobeniusPairingData (trM = Σ y χ, χ(1)=dim, trM 1 = 1); blockMass_sum_eq_one; trM_eq_expectation; trM_le_of_normalised_le / le_trM_of_le_normalised (needs IsProbability, a HYPOTHESIS — positivity of convention-D y_λ is measured n=3..12, not proved at general n); entangledSupp + trM_eq_of_entangledSupp_empty + bindingForm_eq_zero_of_entangledSupp_empty (ℝ section); charSupp/level + level_one_eq_top + level_le_level_one. lean-direct -DautoImplicit=false -s 65536 exit 0, no warnings; #print axioms: propext, Classical.choice, Quot.sound on all seven. Registered in QOU.lean.

HELD (not committed): a primary conjecture class RelativeReebDatum for the owner's relative-angle datum — Lean text in the analysis doc §8 O3. Reason: §3b-tax needs content-bearing fields and the content is exactly what is undefined; owner's rule against speculative code. Also held: any Möbius-energy objective (O4) until qou-99qc pins classicalLimitConst.

Probe: computations/probes/deuteron_block_measure_entangled_support_probe.py (6/6, committed inputs only, weight_family declared). Bean stays in-progress per rule 13a (the picture's structural claims are open).


Correction (same hour): the ℝ theorem bindingForm_eq_zero_of_entangledSupp_empty lives in the §7c companion QOU/MassTheory/BlockMeasureBindingFormArchimedean.lean, not in the generic file — check-sidecars flagged the mixed file and it was split before commit.



## 2026-09-16 — owner: 'formalize and work on RelativeReebDatum conjecture class'

Owner clarification (verbatim gist): the relative Reeb angle between two knots 'is supposed to be the evaluation/trace of the substrate phase space at the point'. That is explicit consent for the held class. Branch claude/lr-a3-reeb-datum-composition-program-2026-09-16 from main 1a5059cffb; committing RelativeReebDatum as a content-bearing primary conjecture class (no instance), with derived consequences as theorems taking the class as hypothesis.



## 2026-09-16 — RelativeReebDatum committed (class, no instance)

QOU/MassTheory/RelativeReebDatum.lean: class over BranchingData ℝ A₁ A₁ A Λ₁ Λ₁ Λ with lightCone, compose, Entangled; clauses compose_eq (a ⋈ b = (a⊗b)·lightCone), lightCone_of_not_entangled (= 1), trM_lightCone_mem (∈ [−1,1]); phaseSpace (block vector of the light cone), relAngle := arccos ∘ trM ∘ lightCone; proved sum_phaseSpace and the four no-shared-history consequences (composite = free product, trace factorises, bindingForm 0, relAngle 0). Probe relative_reeb_datum_trace_angle_probe.py (7/7): trace-level candidate θ = arccos(∏(z_D+d)) defined and monotone (D 59.45°, 3He 71.86°, T 78.16°, 4He 82.78°); block-level ratio NOT definable (|χ_atom/χ_free| > 1 on T (5,4), 3He (9),(5,4)). Roast: on the only defined candidate the angle is the binding form under cos θ = exp(−B/α) — redundant. Stays in-progress (rule 13a: lightCone is data, the conjecture is open); options doc §8 O2/O5.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-16 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-10-12 — owner reformulation: segment collision (replaces the light-cone reading)

Owner: only ONE braid segment from each particle meets at p on the exceptional divisor; history enters as the categorical trace of the γγ tower; incoming angle = relative minimum of local rotational energy (O'Hara + Bring), starting the Reeb/geodesic flow (cf. qou-rydq: the Bring cone link is UT(Σ₄), so the Reeb flow is the geodesic flow of Σ₄ and an incoming direction at p is a point of UT(Σ₄)).

Landed (Lean `QOU/MassTheory/SegmentCollisionDatum.lean`, lean-direct exit 0 with -DautoImplicit=false, 14 theorems, axioms propext/Classical.choice/Quot.sound only; probe `computations/probes/segment_collision_probe.py`, 9/9):

- **A. Single-segment marginal is UNIVERSAL** (conditional on DisjointBlockMultiplicative, itself conditional on TowerSpan): tr(a·(α+βσ+γσ⁻¹)·b) = (α+βz+γz⁻)·tr a·tr b. Measured on p, n, core × p, n, σ³ in H₆: ratios (1, z_D, z_D−h) to 4e-50. So the "unknown initial photonic state" provably drops out — but so does everything else: a single-segment collision CANNOT separate particles of equal trace (`bridge_cannot_separate`).
- **Dichotomy**: a two-segment probe (σ₁σ₂, one strand into a's history) is NOT universal: p 1.2441, n 1.4706, core 0.3801 (depends on a only).
- **B. Channels**: Sym (q⁴+q²+1)/(q²+1)² = 0.75270, Alt q²/(q²+1)² = 0.24730 — exactly y_(2), y_(1,1) at n = 2; both live.
- **C. Local O'Hara cross term is chirality-blind** (θ↦π−θ and d↦−d, both proved); a reflection-symmetric energy with a unique minimiser selects θ = π/2 (proved). Measured min at π/2 for ℓ/d ∈ {0.5,2,10,50}; log coefficient → 2π/sin θ.
- **D. `SegmentCollisionDatum` class, no instance**: θ* = π/2 whenever the Bring term is achiral. Any σ-vs-σ⁻¹ selection must come from a chiral Bring term. Note: `isMin` is unused by that theorem (only uniqueness is).

Promising? Partly. The localisation is clean and the history-forgetting is a theorem, but it makes the single-segment collision blind to which particles collide, and O'Hara alone picks the achiral perpendicular angle. Live directions: (i) widen the collision window to k segments from each (k = 2 already sees history), (ii) derive a chiral Bring term on UT(Σ₄). Status stays todo: open conjecture class.
