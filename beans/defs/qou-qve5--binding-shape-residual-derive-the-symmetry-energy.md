---
# qou-qve5
title: 'Binding SHAPE residual: derive the symmetry-energy term of the additive log law from the bond graph — isospin coefficient has the wrong sign (κ=+2(q₀−1)=+0.22 vs data ≈ −0.15); formalize-first, no fit (gm4q / qou-brng / 1ppQ reanalysis §5 item 3)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-07T18:26:48Z
updated_at: 2026-10-04T15:12:00Z
parent: qou-v2om
---

Owner 2026-09-07: 'fixing binding where most of the gap is shape'. State (docs/audits/2026-09-04-binding-law-options-decision-frame.md, 2026-09-05-binding-law-arc-synthesis.md, 2026-09-07-1ppq-reanalysis §2b/§5.3): additive law B = E₀·log(tr_M(free)/tr_M(atom)) adopted (Option B); scale freedom 0.99 %, residual band 22.5 % — shape residual is 22.7× the scale freedom. Joint fit of the residual shape gives symmetry : surface : Coulomb ≈ 3 : 1.8 : 1, symmetry energy leads (corr −0.804 vs surface −0.178). Derived isospin coefficient κ = +2(q₀−1) = +0.2200 has the WRONG SIGN (data ≈ −0.15); layout-free bond counting (1.181) beats every isospin-resolved variant. Lean already: QOU/Hecke/SymmetrySignAmGm.lean (symmetry sign is AM-vs-GM; equal-weight p–n bond always wrong-signed; crossing weight 1/(q²+1) < ½), BindingExtensivity.lean, CoordinationSaturation, ChainBondOrderDependence, BodyOrderRecurrenceDepth, MayerThreeBodySign. Pruned: complete graph, linear chain, per-block Δ_λ reweighting (qou-bmz8 ℓ¹ ceiling). Task: formalize-first — what edge set / bond weighting does the braid geometry FORCE, and does it produce a negative-signed (N−Z)² term with no new constant? Anti-fit: the SEMF coefficients are targets to check against, never to search on. Honest negative is a result.



2026-09-08 (branch claude/binding-shape-symmetry-term-edge-set-2026-09-07): formalize-first result landed. QOU/Hecke/BondCutSymmetry.lean (generic ring/ordered field, 15 theorems) + QOU/Hecke/BondCutSymmetryLogBound.lean (ℝ, −ln b letters, 5 theorems; §7c split) (20 theorems, lean-direct -DautoImplicit=false exit 0 against restored lake-cache/qou-v4-24-0, #print axioms = propext/Classical.choice/Quot.sound only, no sorryAx). Cut identity: B = (e_pp d_P + e_nn d_N)/2 + delta.n_pn for ANY graph/colouring — the whole layout dependence is the p–n cut times delta = e_pn − (e_pp+e_nn)/2. Constant cut (every segregated layout, the A−1 chain) ⇒ affine in (Z,N), no (N−Z)² at all; well-mixed cut n_pn = kZN/A ⇒ exactly one symmetry term a_A^eff = E₀·delta·k/4, SEMF sign iff delta > 0. Two invariants exclude the class (scope-(b), proved): (1) convex interface bounds delta ≤ 2 ln q = 0.2087 for every w∈[0,1] ⇒ a_A^eff ≤ (k/2)E₀ ln q = 0.44 MeV (k=2) … 2.65 MeV (k=12) vs a_A ≈ 23.7 — an order of magnitude short even with the sign flipped; (2) positivity: e = −ln b > 0 and counts ≥ 0 ⇒ B ≥ 0 at pure neutron matter, while SEMF a_A > a_V gives (a_V−a_A)A < 0 — no non-negative bond count on any graph with any interface agrees. O(ℏ²) question: deformation miss (q²−1)/(2(q²+1)) = 0.0520 ≥ ℏ_q/2 = 0.0495 (first order), flavour tilt +0.00034 pushes AWAY from the crossing; a second-order flip needs coefficient ≥ 1/(2ℏ_q) = 5.05. Probe computations/qbeta/qbeta_bond_cut_symmetry_shape_probe.py (14/14, mpmath 40 dps, proton pin). Corpus delta = −0.02176, a_A^eff(corpus) = −0.046k MeV. HONEST NEGATIVE: the braid geometry does not force an edge set producing a negative-signed (N−Z)² term of SEMF size; the symmetry energy (and neutron-matter unbinding) needs a term outside the pair-additive positive bond-count class — same object as the extensive-term frontier (qou-brng). Bean stays OPEN: the positive target (what supplies it) is unclosed.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-08 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress Update (Round 67 — PR #8279)
- **Status**: `in-progress` (per active rule: no unilateral `qou` bean closures).
- **PR**: [`litlfred/qou#8279`](https://github.com/litlfred/qou/pull/8279) (branch `feat/round67-diproton-coordination-markov-cut-parity-43c1`, Commit 1 `cfebb01621939a34b7b6881f7cb1f8c1de011515`, Commit 2 / Head `6ad7f37ff2f830c6b6b24c3e111bd408c518e8e6`).
- **Lean 4 Artifact**: `folio/quantum-observable-universe/lean/QOU/Hecke/BondCutSymmetry.lean (`bondSum_mirror_diff_cut_invariant`)` (0 sorry, 0 findings across all 6 static vacuity audits).
- **80-dps Witness**: `computations/probes/diproton_coordination_markov_cut_parity_probe.py` (`scriptHash: 54f10b23e4d2`) + `test/results/witnesses/diproton-coordination-markov-cut-parity.witness.json` (`allPassed: true`).
