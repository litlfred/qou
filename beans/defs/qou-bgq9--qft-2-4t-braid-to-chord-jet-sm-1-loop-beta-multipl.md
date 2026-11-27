---
# qou-bgq9
title: 'QFT-2 (math): 4T relations and the braid-to-chord-diagram jet (Drinfeld–Kohno / Kontsevich)'
status: in-progress
type: task
priority: critical
created_at: 2026-11-19T16:48:44Z
updated_at: 2026-11-22T22:05:00Z
parent: qou-3fjn
---

`QOU/StandardModel/InfraredQFTSubsumptionAndPartonMoments.lean` (`935` lines, wired in `QOU.lean`) + `qft_subsumption_gm2_alphas_and_dis_probe.py` (`47875996083d`) — Red-Team PASS.

## Reopened (owner instruction 2026-11-20, via W12)
This bean was set to completed by local commits on `cat/cat-harness/beans` (e223ed1 / 4fcd2cb / 89bb5e0, 2026-11-19, `litlfred@fenugreek.home`, no session trailer). The Lean / probe / witness files its resolution names are not on main, on any branch, or in any PR found by the bean id (measured 2026-11-20). See GAP bean qou-w12g.

## 2026-11-21 — physics-scope re-check on main 2ae54ab40 (bean-drain sibling, issue #8810)

Re-checked on main: the Lean/probe files this bean's resolution text names are absent (`git ls-files | grep <stem>` = 0). The epic's vocabulary has 0 hits in the folio (Cutkosky, Bern–Kosower, Callan–Gross, Herm₂, 41/10, Machacek, Larin). Two further scope problems independent of the missing files: (1) the title puts empirical comparisons inside formal targets; (2) Feynman perturbation theory sums over virtual quanta, which the owner ruling of 2026-11-21 (no virtual photons) excludes. Disposition (re-scope to math-only / scrap / leave) is on an owner card. Audit: `docs/audits/2026-11-21-physics-claim-scope-recheck.md` on branch `claude/physics-scope-audit-2026-11-21` (4df574c79).

## 2026-11-21 — superseded-premise check (owner instruction 2026-11-21, physics-scope sibling)

Superseded basis found: Feynman perturbation theory relies on virtual quanta, excluded by the 2026-11-21 ruling (no virtual photons), and the title's targets are CODATA/PDG comparisons. Do not work this bean on that basis; disposition on the owner card (re-scope to math-only / scrap / leave).

## 2026-11-21 — RE-SCOPED to math only (owner card "Re-scope to math only", 12:09Z; issue #8810)

Previous title: 'QFT-2: 4T Braid-to-Chord Jet, SM 1-Loop Beta Multiplicities (7, 19/6, -41/10), (g-2)_e Pin Audit & DIS Valence Moments'

Target: the 4T relations among chord diagrams and the associated graded of the braid group algebra (pure braids, Drinfeld–Kohno) as the target of the braid-to-chord jet. Dropped: SM 1-loop β multiplicities (defined by loops), (g−2)_e pin audit (CODATA comparison, virtual photons), DIS valence moments.

## 2026-11-22 — wave-2 applicability review (thread "Build ribbon categories and QFT math cores")

**Verdict: APPLIES.** Math-only target, no retired premise.

Partial: `QOU/QFTMath/InfinitesimalPureBraid.lean` on `claude/qft-math-cores-2026-11-22` (df504460b) proves the Drinfeld–Kohno relations for transpositions in k[Sₙ] for every n (hence for every permutation representation). Still open: Kohno's theorem (𝔱ₙ = associated graded of ℤ[PBₙ]) and the link from the near relation to `QOU.KnotTheory.Vassiliev.FourTermRelation`.

## 2026-11-27 — the 4T encoding collapses 𝒜ₙ (thread "Derive hypercharge and gauge structure", PR litlfred/qou#9729)

`BraidKnotOctonion/Vassiliev/FourTermEncodingCollapse.lean` (0 sorry) proves that with `fourTermRelator D i j` imposed for all adjacent transpositions, `relationsSubmodule = ⊤` and every `WeightSystem R (k+1)` is 0 whenever 2 is a unit (the relator at i = j is 2·(one slide); slides generate Perm; 1T then kills every diagram). The true 𝒜₂/ℚ is 1-dimensional. Next: replace the encoding with Bar-Natan's 4T (shared definition, needs owner OK), then the near relation → 4T link. Kohno's theorem not attempted. Associator thread confirmed it is not touching this.

## 2026-11-27 (later) — Bar-Natan 4T in place (owner card "Yes, replace it in this thread"; PR #9729)

`FourTermRelation.lean` now encodes Bar-Natan's 4T (re-insertion via `gapPerm`, slides across both ends of a chord cancel, all rotations). The old relator survives as `slideRelator` in `FourTermEncodingCollapse.lean` with its collapse proof. `FourTermDegreeTwo.lean` shows that the crossed diagram survives in degree 2 and that a non-zero weight system exists. Still open: matching Bar-Natan in degree ≥ 3 as a theorem, linking the near relation [t_ij, t_ik+t_jk]=0 to this 4T via closure, and Kohno's theorem.
