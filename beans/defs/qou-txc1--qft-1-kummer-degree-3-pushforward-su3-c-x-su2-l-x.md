---
# qou-txc1
title: 'QFT-1 (math): S(U(3)×U(2)) ≅ (SU(3)×SU(2)×U(1))/Z₆ and sin²θ_W = 3/8 as a hypercharge trace ratio; Bring pushforward producing the embedding as a conjecture'
status: in-progress
type: task
priority: high
created_at: 2026-11-19T16:48:44Z
updated_at: 2026-11-24T03:35:27Z
parent: qou-3fjn
---

`QOU/StandardModel/BringPushforwardAndGaugeGroupUnification.lean` (`1,274` lines, wired in `QOU.lean`) + `su3_su2_u1_pushforward_and_weinberg_probe.py` (`9761c2ea0edd`) — Red-Team PASS.

## Reopened (owner instruction 2026-11-20, via W12)
This bean was set to completed by local commits on `cat/cat-harness/beans` (e223ed1 / 4fcd2cb / 89bb5e0, 2026-11-19, `litlfred@fenugreek.home`, no session trailer). The Lean / probe / witness files its resolution names are not on main, on any branch, or in any PR found by the bean id (measured 2026-11-20). See GAP bean qou-w12g.

## 2026-11-21 — physics-scope re-check on main 2ae54ab40 (bean-drain sibling, issue #8810)

Re-checked on main: the Lean/probe files this bean's resolution text names are absent (`git ls-files | grep <stem>` = 0). The epic's vocabulary has 0 hits in the folio (Cutkosky, Bern–Kosower, Callan–Gross, Herm₂, 41/10, Machacek, Larin). Two further scope problems independent of the missing files: (1) the title puts empirical comparisons inside formal targets; (2) Feynman perturbation theory sums over virtual quanta, which the owner ruling of 2026-11-21 (no virtual photons) excludes. Disposition (re-scope to math-only / scrap / leave) is on an owner card. Audit: `docs/audits/2026-11-21-physics-claim-scope-recheck.md` on branch `claude/physics-scope-audit-2026-11-21` (4df574c79).

## 2026-11-21 — superseded-premise check (owner instruction 2026-11-21, physics-scope sibling)

Superseded basis found: Feynman perturbation theory relies on virtual quanta, excluded by the 2026-11-21 ruling (no virtual photons), and the title's targets are CODATA/PDG comparisons. Do not work this bean on that basis; disposition on the owner card (re-scope to math-only / scrap / leave).

## 2026-11-21 — RE-SCOPED to math only (owner card "Re-scope to math only", 12:09Z; issue #8810)

Previous title: 'QFT-1: Kummer Degree-3 Pushforward SU(3)_c x SU(2)_L x U(1)_Y / Z_6 & UV sin^2(theta_W) = 3/8'

Target: (a) the group isomorphism S(U(3)×U(2)) ≅ (SU(3)×SU(2)×U(1))/Z₆; (b) for the standard embedding in SU(5), the trace ratio Tr(T₃²)/Tr(Q²) = 3/8 on the 5̄ ⊕ 10, as representation theory. (c) 'the Kummer degree-3 pushforward on Bring's surface yields this embedding' is the QOU content and is stated as a conjecture. No running, no comparison with measured sin²θ_W.

## 2026-11-22 — wave-2 applicability review (thread "Build ribbon categories and QFT math cores")

**Verdict: RESCOPE / NEEDS-OWNER.** Part (b), the 3/8 trace ratio on 5̄⊕10, fixes the hypercharge normalisation by the SM charge assignment; under the 2026-11-22 ruling (quark charges derived, not adopted) and with U(1)_em grading owned by PR #9123, it should be restated as a statement about the commutant of su(3)⊕su(2) in su(5) with the normalisation left as a parameter. Part (a) (S(U(3)×U(2)) ≅ (SU(3)×SU(2)×U(1))/Z₆) is pure group theory and APPLIES.

Not worked this pass (boundary with the charge threads). Part (a) is the next math-only step.

Parts (a) & (b) proved sorry-free in Su3Su2U1Z6GroupAndCommutant.lean (83a784c4bdd); Part (c) isolated in BringKummerSU5EmbeddingHypothesis.

## 2026-11-27 — status check (thread "Derive hypercharge and gauge structure")

Parts (a) and (b) are on main in `QOU/StandardModel/Su3Su2U1Z6GroupAndCommutant.lean` (0 sorry; imported via `EightfoldWay/NeutralLeptonFixesCharges`), so the 2026-11-20 file-loss reopening is resolved for them. PR litlfred/qou#9729 adds that the SU(5) charge pattern feeding (b) is itself forced by anomaly freedom, and that 3/8 ⇔ one neutral lepton on any anomaly-free chiral solution. Part (c) (Bring Kummer pushforward produces the embedding) stays open in `BringKummerSU5EmbeddingHypothesis`.

## 2026-11-27 (round 2) — part (c) carrier is satisfied by α = 1/6 (PR #9754)

`QOU/StandardModel/BringKummerCarrierVacuity.lean`: `bringKummerCarrier_satisfied` builds `BringKummerSU5EmbeddingHypothesis K` from the constant 1/6. The fields never mention Bring's curve. Real content of (c): Bring's degree-3 Kummer pushforward realises the flavour fundamental W of `FlavouredQuantumObservableUniverse` (bean qou-j3w6, flavour W thread). Given V, W the embedding, commutant and α = ±1/6 are proved. χ = −6 thread caution: H¹(M₀) = 2W₄ has no A₅-equivariant 3 ⊕ 2. Owner card on whether to retire the carrier and re-point (c) at qou-j3w6.


## 2026-11-27T22:15Z — part (c) carrier retired (PR #9754, commit 2564f59c7)
Carl card 21:53Z "Retire carrier, link to flavour W". BringKummerSU5EmbeddingHypothesis and BringKummerCarrierVacuity.lean removed (satisfied by alpha=1/6). Part (c) = substrate supplies W (qou-j3w6); alpha^2=1/36 then follows from neutral_lepton_iff_three_eighths. Note chi=-6 thread: Bring H^1 = 2W_4 has no A5-equivariant 3+2.
