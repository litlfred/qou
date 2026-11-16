---
# b9cj
title: 'UMBRELLA: open conjectures (formal mathematics only)'
status: in-progress
type: milestone
priority: normal
created_at: 2026-07-05T13:20:00Z
updated_at: 2026-11-16T21:22:30Z
---

Ledger of all 23 open §3b conjecture-class Lean carriers (`instance : X := sorry`) across the QOU lean tree. Per AGENTS.md §3b/§1a these are HONEST conjecture placeholders — the `sorry` IS the conjecture, not missing proof; filling with a fabricated instance is an audit-dodge. Beans below track each for status/backing; famous-open encodings (RH/BSD/Collatz/…) are aspirational and NOT action items to 'prove'. Corpus also has ~153 conj: content-block labels (58 already bean-referenced); this epic scopes the open LEAN carriers specifically. One child bean per carrier.

- `BorelZagierQouVolumes` — folio/quantum-observable-universe/lean/QOU/Archimedean/BorelZagierQouVolumes.lean:45 — framework/substrate §3b carrier
- `BringFigureEightDepth2Witness` — folio/quantum-observable-universe/lean/QOU/BraidKnot/BringFigureEightDepth2Witness.lean:39 — framework/substrate §3b carrier
- `BringTrilogDepth3Witness` — folio/quantum-observable-universe/lean/QOU/BraidKnot/BringTrilogDepth3Witness.lean:114 — framework/substrate §3b carrier
- `ClassicalRiemannHypothesis` — folio/quantum-observable-universe/lean/QOU/BraidKnot/ClassicalRiemannHypothesis.lean:43 — famous-open (aspirational §3b encoding)
- `ConfinementNfStructureForcing` — folio/quantum-observable-universe/lean/QOU/BraidKnot/ConfinementNfStructureForcing.lean:47 — framework/substrate §3b carrier
- `DiophantineBirthday` — folio/quantum-observable-universe/lean/QOU/AppendixSurreals/DiophantineBirthday.lean:50 — **NOT famous-open (corrected 2026-09-03)**: the block itself says in bold *"this should not be recorded as an open conjecture. Roth proved it in 1955. What is missing is a formalisation, not a proof."* The separation follows from Thue–Siegel–Roth, which Mathlib does not carry (searching for "Roth's theorem" finds the unrelated additive-combinatorics result). The carrier is content-bearing with no instance and encodes only the unhedged algebraic half, deliberately — see its header. Status: unformalised, not unproved.
- `He4DemandClosure` — folio/quantum-observable-universe/lean/QOU/Interactions/NuclearOperatorRegimes.lean:141 — framework/substrate §3b carrier
- `LocalInfinitesimalField` — folio/quantum-observable-universe/lean/QOU/AppendixSurreals/LocalInfinitesimalField.lean:49 — framework/substrate §3b carrier
- `QBirchSwinnertonDyer` — folio/quantum-observable-universe/lean/QOU/AppendixSurreals/QBirchSwinnertonDyer.lean:49 — famous-open (aspirational §3b encoding)
- `QCollatz` — folio/quantum-observable-universe/lean/QOU/AppendixSurreals/QCollatz.lean:39 — famous-open (aspirational §3b encoding)
- `QouInfraDischargesGoncharovZeta5` — folio/quantum-observable-universe/lean/QOU/AppendixSurreals/QouInfraDischargesGoncharovZeta5.lean:45 — famous-open (aspirational §3b encoding)
- `QouPNeqNp` — folio/quantum-observable-universe/lean/QOU/Information/QouPNeqNp.lean:55 — framework/substrate §3b carrier
- `SingleVolumeIrrationality` — folio/quantum-observable-universe/lean/QOU/Archimedean/SingleVolumeIrrationality.lean:50 — famous-open (aspirational §3b encoding)
- `SpectralNormalForm` — folio/quantum-observable-universe/lean/QOU/AppendixSurreals/SpectralNormalForm.lean:49 — framework/substrate §3b carrier
- `TorusKnotMass` — folio/quantum-observable-universe/lean/QOU/BraidKnot/TorusKnotMass.lean:123 — framework/substrate §3b carrier
- `TwoFiltrationBridge` — folio/quantum-observable-universe/lean/QOU/BraidKnot/TwoFiltrationBridge.lean:69 — framework/substrate §3b carrier
- `archimedean_agreement` — folio/quantum-observable-universe/lean/QOU/BraidKnot/HabiroResidueSumEquivalence/archimedean_agreement.lean:39 — framework/substrate §3b carrier
- `jet_convergence_classical_limit` — folio/quantum-observable-universe/lean/QOU/BraidKnot/jet_convergence_classical_limit.lean:44 — framework/substrate §3b carrier
- `jet_filtered_knot_factor` — folio/quantum-observable-universe/lean/QOU/BraidKnot/jet_filtered_knot_factor.lean:67 — framework/substrate §3b carrier
- `q_gl_classical_limit` — folio/quantum-observable-universe/lean/QOU/QGeometricLanglands/q_gl_classical_limit.lean:50 — framework/substrate §3b carrier
- `q_gl_fiber_functor` — folio/quantum-observable-universe/lean/QOU/QGeometricLanglands/q_gl_fiber_functor.lean:39 — framework/substrate §3b carrier
- `q_gl_kummer_filtration` — folio/quantum-observable-universe/lean/QOU/QGeometricLanglands/q_gl_kummer_filtration.lean:47 — framework/substrate §3b carrier
- `q_oper_hecke` — folio/quantum-observable-universe/lean/QOU/QGeometricLanglands/q_oper_hecke.lean:45 — framework/substrate §3b carrier



---
**Hygiene pass 2026-08-01 (PR #4489, branch claude/b9cj-conjecture-carrier-hygiene-2026-08-01).**
Classified all 23 carriers: **14 genuine** (content-bearing, verified no change), **3 fixed** (cj421 ConfinementNf + cj118 QBSD: residual=0 → content-bearing; cj8c jet_convergence: removed fabricated laundering instance), **6 needs-owner** (cj46f SpectralNormalForm, cj52 LocalInfinitesimalField, cj1b7 DiophantineBirthday — real claim not faithfully encodable without inventing; cj27e BringFig8, cj434 archimedean_agreement, cj4df QouInfraGoncharov — Habiro-dilog/polylog frontier owned by other agents, deferred). NO instances fabricated. Full per-carrier table: docs/audits/2026-08-01-b9cj-conjecture-carrier-hygiene.md



## Reorganisation 2026-10-04

Umbrella for every open FORMAL conjecture, one epic per family. Owner ruling 2026-10-04: blocks that state a physical identification are routed to the L2 programme or the SM milestone, so no formal family inherits an empirical premise. Register of 182 conjecture blocks (108 formal, 74 identification) measured 2026-10-04.

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.

### Round 51 Update (PR #8206)
- [x] Devacuified `qou-zzhw`, `qou-1vu3`, `qou-w61k`, `qou-sz98`, `qou-00c5` in PR #8206 (`aecfe3f528c442bfb5e105f53d801fa139604119`).
