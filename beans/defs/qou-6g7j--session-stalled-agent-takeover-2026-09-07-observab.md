---
# qou-6g7j
title: 'Session: stalled-agent takeover 2026-09-07 — observable C, #7092 coboundary, Z-resolved b3, REV Σβ, SandwichReduces'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-07T18:06:39Z
updated_at: 2026-10-04T15:11:33Z
---

Branch claude/stalled-agents-em-linking-jilmbv. Owner instruction 2026-09-07: several agents stalled; bean up, take up their work, dispatch agents, consolidate toward L2 with the binding gap read as SHAPE (PR #7005: 5.81 digits of b3 resolution lost to the mirror convention, none to experiment; qou-hok7: REV_n is a free energy over partition shapes).

Stale-branch measurement at session start (age of head commit, 30 open PRs): 11 branches < 65 min (live), 19 idle > 3 h (657 min to 10896 min). Takeover targets are the four pasted arcs plus #7005, not the long-idle tail.


2026-09-11T21:00Z: merge queues 1–3 done (11 PRs merged). Fronts settled: m6gp (obs C, ΔVol≡0), zmat (σ_b coboundary yes/σ_a no), tbk7 (Z-resolved b3 negative), 0ie7 (REV_n=Θ(√n)), fq1i (sym-group tower witness). Parked pending owner: dgpz (Option B), l99f (absolute volume). #7121 merged; branch restarted from main 5408f53d2bc for follow-ups.


### 2026-09-12T05:50Z — next-front results (both chosen by the six-path corpus-grep of the connected 3-body term)

- **qou-rwhv / PR #7198 — YES, the partition function exists, and it REVERSES the 2026-08-30 sign reading.** The corpus b3 of the multiplicative assembly is exactly −φᵀ₃ of a hard-core lattice gas on the nucleon sites (grand canonical over sub-clusters of one fixed nucleus; pair weights = interface-letter traces pp 0.61269 / pn 0.50823 / nn 0.40363 at the proton pin, convention D; tr_M(atom)/tr_M(free) = ∏μ to 2.5e-60 on the live word). Ursell alternation ⇒ b3 < 0 for EVERY bond triple, no 2/3 threshold; the 08-30 'restore (−1)^{n−1}' is the same expansion at negative activity (per-case dispatch). Magnitudes, zero parameters, sign wrong: −1.2277 MeV (³H) vs AME +1.8081; −0.7973 (³He) vs +1.0443. Identity is n ≤ 3 only (b4 = −φᵀ₄ − three perfect matchings). Scope (b), invariant = alternation on (0,1). Lean UrsellPartitionFunctionB3.lean sorry-free (13 decls, lean-direct exit 0); probe 11/11; MayerThreeBodySign docstring re-scoped (corpus-derived). AGENTS.md bullet-4 rewording proposed in the PR body — OWNER decision.
- **qou-m8f3 / PR #7200 — NO at A ≤ 4, scope (b).** The trace's dominant summand is the one-row block [3A] for all ten typed clusters (runner-up ≤ 0.754); its character is a ring homomorphism so the log-weight is exactly chain-edge additive (7.4e-51): b3(ppn) = b3(pnn) = −b2(pn), mirror pair opposite signs. Stops at ⁶Li (two-row [15,3]) — scope (a) for A ≥ 6. Secondary binding-sum argmax gives right-sign b3 at 0.56×/0.72× but wrong-sign b4 and an N−Z artefact — reported, NOT wired. Lean OneRowBlockLetterProduct.lean verified by the parent (exit 0, propext/Quot.sound); probe 14/14.

Net for the goal (L2 binding shape): the Mayer/Ursell vocabulary is now CLOSED on this arc with a proved invariant, and the dominant-summand channel is closed at A ≤ 4. The extensive term's live remainder narrows to: A ≥ 6 two-row dominant blocks, classes B/D of qou-brng, an attractive channel (letter trace > 1 — none in the production word), or a non-Mayer assembly.


2026-09-12T11:55Z: queue 5 merged (#7200, #7198, #7201 — 17 PRs total). AGENTS.md Extensive-term bullet 4 now carries the owner-adopted Mayer-sign wording (73f8cdc7444). Live front: qou-vn6h / PR #7211 (two-row dominant block at A ≥ 6, agent a762e6fbc053f8e04) — first probe run 14/16 with ⁶Li cache round-trip (1e-40) and ⁷Li Ursell round-trip (1e-50) failing; agent re-running, tolerances are to be root-caused not loosened. Remaining doors after it: classes B/D of qou-brng, non-pairwise-generated object, distinguishable components (qou-lq6k).


### 2026-09-12T12:20Z — A ≥ 6 front answered (qou-vn6h, PR #7211, head 1e02a8ed7b9)

YES the one-row letter-product argument of #7200 stops: from A = 5 the trace's dominant summand is a two-row block ([12,3] at A=5, [15,3] at A=6, [18,3]/[15,6] at A=7) and its log-weight carries connected many-edge terms — `mixedSpectrum_not_rightLetterMultiplicative` (sorry-free; parent re-verified lean-direct exit 0 against Mathlib oleans, no sorry) + 32-subset Möbius cumulants at ⁶Li (non-local pp–nn pair cumulant 22× the adjacent one). NO it is not the extensive term: the connected content is anti-binding, −3.50 MeV at ⁶Li and −3.62 MeV at ⁷Li against AME shortfalls of +23.5 / +27.8, and the dominant summand's B/A grows linearly (no plateau). Scope (b) for "the letter-product argument extends", (a) for the physics. Probe 21/21 (672 s), 60 dps, proton pin, convention D. Audit `docs/audits/2026-09-12-two-row-dominant-block-a6.md`. Found on the way: the only committed ⁶Li per-partition cache is the sign-only wire (qou-sgv5) and differs from the live word by up to 3.3e3 in χ; `chi_all_lambda_any` pins dps=50 regardless of ambient mp.dps (TRAP added to compute-precision-auditor memory).

Net for the goal: every order-zero channel of the trace (Mayer/Ursell pairwise, one-row dominant summand at A ≤ 4, two-row dominant summand at A = 5–7, attractive-bond class B) now has a measured or proved answer, and none supplies the extensive positive term. Live: class D (the tower) — dispatched as qou-zlra (sign convention the type-2 pair-convolution quadratic hangs on).


### 2026-09-12T12:36Z — queue 6 merged (#7211, #7217, #7219); 20 PRs across six queues

| PR | note |
|---|---|
| #7211 (A >= 6 two-row dominant block, qou-vn6h) | merged 12:33Z, head 0951b1acee9 on main; parent cherry-verified 0 unmerged |
| #7217 (queue-5 ledger beans) | merged 12:34Z |
| #7219 (merge-coordinator memory, queue 5) | merged 12:36Z, main tip 9af91480d79 |

Coordinator a8e6ef7440ea877d5 hit a session rate limit after the three merges; nothing was left half-done (all three verified with `git cherry origin/main origin/<branch>` by the parent). Branch restarted from main 9af91480d79.

### 2026-09-12T12:35Z — class D answered (qou-zlra, PR #7223)

**The `+c_k / -c_k` sign question is EMPTY for the functional the corpus actually uses.** Every binding law in the corpus is a LOGARITHM of a trace, and for any product-additive functional (`log`, `-log`, `a*log`) the type-two pair convolution `sum_{i<j} b_i b_j` -- the term that carries `(N-Z)^2` -- is absent, for BOTH signs. It is present in the bare product for either sign, but no corpus artifact reads *binding* as a bare Vassiliev coefficient: the one bare binding law (`Q_beta * Delta tr`) was refuted 2026-09-05, and the surviving bare `|tr_M|` readings are MASS functionals. So `qou-oooq`'s valley belonged to the product under an assumed sign; `+c_2` makes it a hill; the log removes it. Sharper: the functional the owner ruled in FOR EXTENSIVITY ("log is the unique multiplicative->additive map") is, by the same theorem, the one that cannot carry a two-bond correlation at type two.

Lean `QOU/Mass/GradedBindingFunctionalPairTerm.lean` (generic CommRing; formal log over Field + NeZero 2): `prod_c2`, `e2_append`, `two_mul_e2_census`, `additive_census`, `neg_additive`/`smul_additive`, `logJet_c2_prod`, `logJet_c2_census`. Parent re-verified lean-direct (`-DautoImplicit=false -s 65536`) exit 0, 0 `sorry`, seven `#print axioms` on propext / Classical.choice / Quot.sound only. Probe 21/21, 44 s, dps 70, proton pin, convention D, exact `Fraction` h-series, no float64: 2nd difference in Z of `[h^2] prod` = 4 at every A = 3..12, of `[h^2](+/-log)` = 0; `c_2/c_0 = (N-Z)^2/2 + (5-A)/8` reproduced exactly; valley scan -- live law endpoint at every A, `-c_2/c_0` interior max at N=Z, `+c_2/c_0` a hill. `qou-eqwg`'s open question ANSWERED: transfer matrices on one generator COMMUTE exactly, so "non-commutativity inside a generator" is empty.

**Collision found, not resolved (no functional picked by its numbers):** the corpus carries two inequivalent log readings -- log of the Markov-weighted TOTAL trace (bond-additive on the chain) vs `unified-iterative-correction`'s weighted sum of PER-BLOCK logs. A single Wedderburn block is not multiplicative even on the chain. The production UIC scan exceeded 300 s/atom and is left as the one open measurement on `qou-zlra`; it is the only corpus functional outside the additive class, so it is the one place a type-two two-bond correlation could still live.

Net: classes A, B, C of `qou-brng` are closed or narrowed by proved invariants, and class D is narrowed to the per-block log. `qou-brng` stays OPEN (rule 13a).



## Summary of Changes

Session log closed 2026-10-04 (owner decision 2): open children were reparented to programme epics and prose follow-ups extracted as their own beans. Kept as a record, not deleted.
