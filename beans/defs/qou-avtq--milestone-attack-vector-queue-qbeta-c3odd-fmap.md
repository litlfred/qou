---
# qou-avtq
title: 'MILESTONE: attack-vector queue (Q_beta / c3^odd / f-map)'
status: todo
type: epic
priority: high
created_at: 2026-08-26T04:22:51Z
updated_at: 2026-11-15T13:30:00Z
parent: qou-10v9
---

Ordered queue of every attack vector surfaced by the 2026-08-26 three-gap
assessment. Order is my judgement and is meant to be overruled.

| # | bean | state |
|---|---|---|
| 1 | `qou-avt1` counit->trace transport | RUN 2026-08-26 -> **overshoots ~300x**, scope-(a). Live residue: the G2 form clash (affine in w vs the asserted cosine). |
| 2 | `qou-avt4` f-map keystone ledger stale since 2026-07-11 | **DONE 2026-08-26** — banner + 7 log rows; historical sections kept. Cheap, docs-only, but it is the entry point for the whole f-map programme so a stale one costs a session. |
| 3 | `qou-avt2` general-n per-block Hecke characters (Halverson-Ram / Jing-Liu) | STARTED -> its premise check surfaced `qou-avt5`. Build the general-n tool only after avt5 settles WHICH element the per-block characters belong to. |
| 3b | `qou-avt5` two H_3 n-minus-p elements differ 39% at q0 | **SETTLED 2026-08-26.** chi_block_* VERIFIED against the exhibited words; eps(Delta) is an asserted polynomial with no element. Q_A rests on the asserted one. Next: exhibit the single-wrap element. |
| 4 | `qou-avt3` c3^odd | BLOCKED UPSTREAM by design. Not well-posed until (H1) is derived or dropped. Do not start it. |
| - | `qou-ximf` Xi_k cyclotomic family | **RETRACTED** 2026-08-26 -- collapses to a function of h. |

| 3c | `qou-avt6` no typed-crossing word difference has counit epsNPq | **PROVED scope-(b) 2026-08-26** via a norm argument in Z[sqrt2] at the silver ratio. Forces a fork: either the prose describing Delta is wrong, or epsNPq is. Owner call. |

## What the queue has established so far, as one sentence

Three independent routes into the Q_beta residual have now been closed by
measurement rather than opinion -- the Xi_k weight moments (collapse to h), the
k-cycle Hecke traces (Markov forces z^{k-1}), and the counit->trace transport
(overshoots ~300x) -- and all three failures point the same way: **ce is not
reachable from the trace/weight structure, and the surviving suspect is the
axiomatised cosine.**

## Standing discipline for everything in this queue

ce is resolved to 1.45% (68.8 sigma) by sigma(Q_beta)/Q_beta. Any identification
quoted tighter than that is arithmetic, not measurement. Pre-state gates before
running; a candidate found by search is a fit however good it looks.



## Reorganisation 2026-10-04

Now the epic for P1.QB under PROGRAM: L2 at 1 ppQ (mass and binding accuracy).


## 2026-10-10 — verification sweep: every child re-checked against evidence (owner: "cleanup, status updated, validate if attack options closed vs open based on actual evidence (noting some numeric probes could be wrong)")

**The queue table at the top of this bean is stale** (it lists avt1–avt6 as of 2026-08-26). This section is the current state.

**Method.** Six read-only verification agents, one per cluster, each in its own scratch worktree at `main` `77695711d2`. Every child's claim was traced to a witness, probe, Lean file or later bean. Probes were re-run only where cheap and decisive; ~45 re-runs in total, almost all reproduced their recorded numbers. A "closed" verdict required a proof, an exact computation, or a numeric result that reproduces and whose precision exceeds the gap it decides. **Convention-C numbers were not counted as evidence about convention-D claims.**

**Counts (103 children):** OPEN 31, DONE 26, EVIDENCE-UNRELIABLE 12, SUPERSEDED 11, BLOCKED 8, DUPLICATE 6, CLOSED-REFUTED 6, CLOSED-PROVED 3. Status moves: 30 → `completed`, 17 → `scrapped` (each with its reason; nothing deleted), the rest unchanged. Four children (`54g5`, `g3mz`, `ox7y`, `cds1`) were edited today by the `qou-d8c7` session (issue #7547); their statuses are respected.

**What the evidence says, across clusters.**
1. **No committed `c_k` value is a convention-D value.** Every ladder number is convention C. The "D" figures (`c₃ ≈ −974`, implied `c₂ ≈ −9.3`) are hybrids, a z-swap on the retired base. `qou-cds1`'s 2026-10-10 entries add that `c₂…c₅` are z-free and therefore identical under D, so "re-derive under D" has nothing to re-derive at k ≥ 2.
2. **On the ruled base the ladder is excluded for every phase** (`LadderFactorBound`, `LadderUniformBound`), so the chain `iagg ← cds1 ← pdix` is broken: α cannot unblock it. **No admissible element or functional supplies the factor 1.759.** The functional side is closed exactly by `χ_(2,1)(Δ_S) = 0`. The element side reaches at most 1.362 if "no gluon" covers the γγ words, a ruling question recorded open on `qou-cds1`.
3. **Several "measured" facts rest on numbers that do not support them:**
   - **The muon/proton sign flip `S_μ > 0 > S_p`:** the canonical witness records `sign_flip_resolved=False`, with S uncertainty ±1.262, 126× the muon value. It uses convention-C extractions and a superseded CODATA-2018 muon value.
   - **The "hypersensitivity" slope (~2e6):** this is the c₃ extraction's own `1/u³` factor, matched to 3e-5, not geometry.
4. **The A_ω arc:**
   - **The "4₁ DT spectrum {3,4}" misreads GGM.** Eqs (96)/(98) are 5₂ data; 4₁ is eq (60), which carries only 3.
   - **"A_ω = 3 is the Stokes symmetry constant" holds by construction.** `S₁₂+S₂₁ = 3S₁₁` holds for any symmetric middle matrix.
   - **`mass-theory/aomega-fourone-dt-count.md` overstates GGM.** It says they "proved peacock Conjecture 3"; they prove Conjectures 4 and 5.
5. **Red or stale probes, beyond those named in individual beans:**
   - The failed-assertion audit reports 104 new offenders.
   - `qbeta_ck_qholonomic_recurrence_test.py` exits 0 with `allPassed false`, and prints hard-coded verdict prose its computation no longer produces.
   - The committed chirality witness (`durationMs 44`) matches no recorded run.

| child | verdict | status |
|---|---|---|
| `aciw` | BLOCKED | `todo` → `todo` |
| `cjo1` | BLOCKED | `todo` → `todo` |
| `qou-avt3` | BLOCKED | `todo` → `todo` |
| `qou-iagg` | BLOCKED | `todo` → `todo` |
| `qou-qb8e` | BLOCKED | `todo` → `todo` |
| `qou-qb8g` | BLOCKED | `todo` → `todo` |
| `qou-qu2t` | BLOCKED | `todo` → `todo` |
| `qou-s077` | BLOCKED | `todo` → `todo` |
| `qou-0e2p` | CLOSED-PROVED | `todo` → `completed` |
| `qou-kc21im` | CLOSED-PROVED | `todo` → `completed` |
| `qou-p7n5` | CLOSED-PROVED | `todo` → `completed` |
| `qou-4kr1` | CLOSED-REFUTED | `todo` → `completed` |
| `qou-avt1` | CLOSED-REFUTED | `todo` → `completed` |
| `qou-f5xq` | CLOSED-REFUTED | `todo` → `completed` |
| `qou-i2ir` | CLOSED-REFUTED | `todo` → `completed` |
| `qou-rt0a` | CLOSED-REFUTED | `completed` → `completed` |
| `qou-rwhj` | CLOSED-REFUTED | `todo` → `completed` |
| `ciei` | DONE | `todo` → `completed` |
| `qou-52sn` | DONE | `completed` → `completed` |
| `qou-54g5` | DONE | `completed` → `completed` |
| `qou-5nyg` | DONE | `todo` → `completed` |
| `qou-5s01` | DONE | `todo` → `completed` |
| `qou-66f2` | DONE | `todo` → `completed` |
| `qou-8j0d` | DONE | `todo` → `completed` |
| `qou-bvgw` | DONE | `todo` → `completed` |
| `qou-c66b` | DONE | `todo` → `completed` |
| `qou-cg1b` | DONE | `todo` → `completed` |
| `qou-ckwt` | DONE | `todo` → `completed` |
| `qou-floy` | DONE | `todo` → `completed` |
| `qou-g3mz` | DONE | `scrapped` → `scrapped` |
| `qou-iax1` | DONE | `todo` → `completed` |
| `qou-khue` | DONE | `todo` → `completed` |
| `qou-ls7l` | DONE | `todo` → `completed` |
| `qou-ox7y` | DONE | `todo` → `todo` |
| `qou-s6b9` | DONE | `todo` → `completed` |
| `qou-u14x` | DONE | `todo` → `completed` |
| `qou-u7hi` | DONE | `todo` → `completed` |
| `qou-v6wz` | DONE | `todo` → `completed` |
| `qou-vbw1` | DONE | `todo` → `completed` |
| `qou-w1j9` | DONE | `todo` → `completed` |
| `qou-w2q7` | DONE | `todo` → `completed` |
| `qou-xyk3` | DONE | `todo` → `completed` |
| `qou-zezz` | DONE | `todo` → `completed` |
| `qou-0pym` | DUPLICATE | `todo` → `scrapped` |
| `qou-gjs2` | DUPLICATE | `todo` → `scrapped` |
| `qou-ledr` | DUPLICATE | `todo` → `scrapped` |
| `qou-mcus` | DUPLICATE | `todo` → `scrapped` |
| `qou-wwme` | DUPLICATE | `todo` → `scrapped` |
| `qou-zol3` | DUPLICATE | `todo` → `scrapped` |
| `kehn` | EVIDENCE-UNRELIABLE | `todo` → `todo` |
| `qou-4kgh` | EVIDENCE-UNRELIABLE | `todo` → `todo` |
| `qou-5u0i` | EVIDENCE-UNRELIABLE | `todo` → `todo` |
| `qou-avra` | EVIDENCE-UNRELIABLE | `todo` → `todo` |
| `qou-dbau` | EVIDENCE-UNRELIABLE | `todo` → `todo` |
| `qou-dvlt` | EVIDENCE-UNRELIABLE | `todo` → `todo` |
| `qou-fgte` | EVIDENCE-UNRELIABLE | `todo` → `todo` |
| `qou-qmnb` | EVIDENCE-UNRELIABLE | `todo` → `todo` |
| `qou-x581` | EVIDENCE-UNRELIABLE | `todo` → `todo` |
| `qou-yh67` | EVIDENCE-UNRELIABLE | `todo` → `todo` |
| `qou-zuk4` | EVIDENCE-UNRELIABLE | `todo` → `todo` |
| `zqtv` | EVIDENCE-UNRELIABLE | `todo` → `todo` |
| `n920` | OPEN | `todo` → `todo` |
| `qou-0e66` | OPEN | `todo` → `todo` |
| `qou-0xe1` | OPEN | `todo` → `todo` |
| `qou-0ylf` | OPEN | `todo` → `todo` |
| `qou-11l4` | OPEN | `todo` → `todo` |
| `qou-3ent` | OPEN | `todo` → `todo` |
| `qou-5wuz` | OPEN | `todo` → `todo` |
| `qou-6tdg` | OPEN | `todo` → `todo` |
| `qou-8ex3` | OPEN | `todo` → `todo` |
| `qou-8vt2` | OPEN | `todo` → `todo` |
| `qou-a613` | OPEN | `todo` → `todo` |
| `qou-ae6l` | OPEN | `todo` → `todo` |
| `qou-ay84` | OPEN | `todo` → `todo` |
| `qou-cds1` | OPEN | `in-progress` → `in-progress` |
| `qou-dq2q` | OPEN | `todo` → `todo` |
| `qou-dt14` | OPEN | `todo` → `todo` |
| `qou-dtd3` | OPEN | `todo` → `todo` |
| `qou-esx7` | OPEN | `todo` → `todo` |
| `qou-l15q` | OPEN | `todo` → `todo` |
| `qou-my68` | OPEN | `todo` → `todo` |
| `qou-n2cl` | OPEN | `todo` → `todo` |
| `qou-pdix` | OPEN | `in-progress` → `in-progress` |
| `qou-q05m` | OPEN | `todo` → `todo` |
| `qou-sglq` | OPEN | `todo` → `todo` |
| `qou-t39x` | OPEN | `todo` → `todo` |
| `qou-tv6l` | OPEN | `todo` → `todo` |
| `qou-uabo` | OPEN | `todo` → `todo` |
| `qou-v4ux` | OPEN | `todo` → `todo` |
| `qou-vr3q` | OPEN | `todo` → `todo` |
| `qou-xijb` | OPEN | `todo` → `todo` |
| `qou-ztod` | OPEN | `todo` → `todo` |
| `qou-3s30` | SUPERSEDED | `todo` → `scrapped` |
| `qou-5843` | SUPERSEDED | `todo` → `scrapped` |
| `qou-68ge` | SUPERSEDED | `todo` → `scrapped` |
| `qou-82w7` | SUPERSEDED | `todo` → `scrapped` |
| `qou-goc9` | SUPERSEDED | `todo` → `scrapped` |
| `qou-iyj5` | SUPERSEDED | `todo` → `scrapped` |
| `qou-k8w9` | SUPERSEDED | `todo` → `scrapped` |
| `qou-mogm` | SUPERSEDED | `todo` → `scrapped` |
| `qou-nlbj` | SUPERSEDED | `todo` → `scrapped` |
| `qou-qsme` | SUPERSEDED | `todo` → `scrapped` |
| `qou-xzrj` | SUPERSEDED | `todo` → `scrapped` |

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.
