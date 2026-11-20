---
# qou-x631
title: Prove the Δ_λ covariance kernel Cov_Planch(f^λ,Σc²)≤0
status: todo
type: feature
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-18T19:55:42Z
updated_at: 2026-11-20T16:06:50Z
parent: b9cj
---

## Goal                                                                     
                                                                            
Prove cov(k) = Σ_{λ⊢k} (f^λ)³ (Σ_□c(□)² − C(k,2)) ≤ 0 (⇔                    
T₃(k)=Σ_λ(f^λ)²χ^λ(3-cyc) ≤ 0 ⇔ Cov_Planch(f^λ, Σc²) ≤ 0) — the sole open   
input of the Δ_λ super-exp growth bound (WstdSuperExpBound.lean, via        
DeltaLambdaDReduction.D_of_T3_nonpos, sorry-free). Growth bound ⇒ k(A)=O(log
A) (GAP-A-3). Carried as YoungDiagramKernel.covariance_kernel_conjecture    
(§3b                                                                        
open).                                                                      
                                                                            
## Status                                                                   
                                                                            
• **Phase 0 (done, #3939/#3959/#3998):** reduction (D)→kernel; free-cumulant
framing Σ̂₃=R₄+R₂,                                                           
E_Planch[R₄]=−k; sorry-free Lean reduction; verified k≤40; faithful Lean    
statement.                                                                  
• **Phase 1 (done, #4008):** eliminated (1) holonomic recurrence (not P-    
recursive, k≤28);                                                           
(2) β-monotonicity (E_β[C₂] increases 4→5).                                 
• **Phase 2 (done, THIS branch):** eliminated (3) sub-family sign-          
definiteness (two-row flips + at                                            
k=6, hook at k=4); (4) Murnaghan–Nakayama peeling                           
(B(ν)=Σ_{λ/ν=BS₃}(−1)^ht(f^λ)² first >0 at the                              
self-conjugate staircase ν=(3,2,1), k=9); (5) no tabulated closed form (both |
T₃|,|cov| OEIS-absent                                                       
through k=18). Pinned R₄=3ω₃−k affine (not a new lever), Lean-carried sorry-
free (r4WeightedSum_eq).                                                    
• **Phase 3 (open):** Śniady genus expansion on the (f^λ)³-biased measure.  
Obstruction: f^λ is the                                                     
exponential DIMENSION, not a bounded character ratio ⇒ Kerov-               
CLT/Ivanov–Olshanski not direct.                                            
                                                                            
## Coordination                                                             
                                                                            
• DEPENDS on Specht/S_n Lean epic sp00 + #4110/#4114/#4126 for any Lean     
proof of the kernel.                                                        
• Feeds Δ_λ vector V5 of keystone map #4058; growth bound = GAP-A-3         
magnitude leg behind binding                                                
B_gate work (#4132/#4135/#4136).                                            
• Phase-3 lead: RSK form T₃=Σ_{w∈S_k}χ^{sh(w)}(3-cycle) + Śniady genus      
expansion; or a bespoke                                                     
second-moment identity for Cov_Planch(f^λ, Σ_3).                            

---

## Independent numerical cross-check (2026-08-15, session claude/lake-eviction-guard-rhok-drain)

A from-scratch implementation — partitions, hook-length `f^λ`, and `χ^λ(3-cyc)` by
Murnaghan–Nakayama over beta-numbers, exact integers throughout, sharing no code with the
epic's own producers — **reproduces T₃(k) < 0 for every k in 3..22**:

    k= 3  -2            k=10  -19676288           k=17  -3739005858421579852
    k= 4  -2            k=11  -536156728          k=18  -221652176124179610176
    k= 5  -16           k=12  -15073599368        k=19  -14586861263905671449384
    k= 6  -260          k=13  -506810488304       k=20  -1105899474864697741281712
    k= 7  -2336         k=14  -22172234503696     k=21  -95873425397284134999878528
    k= 8  -28792        k=15  -1192602485739392   k=22  -8966772758189897492158683680
    k= 9  -632972       k=16  -66317362326945680

This is a **weaker range** than the epic's own k ≤ 40 and adds no new mathematics; its only
value is that it is a second, independent code path agreeing with the first, so a bug in the
original verification would have to be reproduced coincidentally. Recording it because the
sign of T₃ is load-bearing for the whole epic.

**No new approach.** The route this session was building toward — FKG/Harris on the dominance
lattice, via the observation that E_Planch[Σc²] = C(k,2) exactly — is already recorded AND
ELIMINATED in docs/audits/2026-07-24-covariance-kernel-interval-fkg-reframing.md, which
carries the k=8 log-supermodularity counterexample (λ=(4,2,1,1), μ=(3,3,2): 3780 > 3136) and
the correction that C₂ and Σ ln h are U-shaped rather than dominance-monotone. Reached the
same wall from a different direction and stopped at it; the corpus-grep checklist is what
caught that this was a closed item rather than an open one.

## 2026-09-08 coordination: same kernel as qou-k5r5, qou-o6ov, qou-za3q, qou-omr7

Audit docs/audits/2026-09-08-l2-1ppq-research-program-gaps.md §6.3 item 1 / §7.3 C2: `k5r5` (99 commits, 08-21 → 09-08) and `o6ov` (99 commits, 08-30 → 09-05) both work the odd-moment / Magnus `tr(ρ_λ Ω₂)` kernel, and before this note there were **zero** cross-citations among k5r5 / o6ov / x631 / za3q / omr7 (measured 2026-09-08 by grepping each body for the other four ids). Shared ledger: epic `qou-x631`, now parent of the other four. Roles — x631: epic, Cov_Planch(f^λ, Σc²) ≤ 0 / T₃(k) kernel; k5r5: M₁ > 0 (first odd moment), all-n proof OPEN, identity Lean-proved; o6ov: does |tr(ρ_λ Ω₂)|/dim decay in b across the ≤2-row column (open mathematics, rescoped 2026-09-05, PR #6822); za3q: Magnus-Ω₂ probes use the Plancherel weight y_λ, 91 % of their work on shapes tr_M annihilates; omr7: Magnus probes' d_q was the hook product, weight inverted (4 files, PR #6442). Statuses are unchanged by this note; a result landing on any of the five should be cited in the other four.
(x631 is the shared ledger; the four are its children as of this note.)


## Cross-citation from qou-za3q (2026-09-11): the A=4 Magnus sign is measured

Per the 2026-09-08 coordination note on qou-za3q ("a result landing on any of the
five should be cited in the other four"), this is such a result.

`he4_magnus_omega2_sign_sparse_probe.py`, 77/77 partitions of H_12, max dim 7700,
28661s:

    P_total(A=4) = 34.1260272853576529271380692762741452981457684651471317452205
    sign = +1    control (rho = I) = 0.0 vanishes    33+/42-    sign_flip_vs_A3 = False

Sign map across the light nuclei: A2 = -1, A3 = +1, A4 = +1. There is exactly ONE
sign change in A = 2,3,4 and it sits between the deuteron and the triton, NOT at
the alpha particle.

Load-bearing for anyone reading the older framing: the he4 probe's docstring
asserted "A=3: P<0, NO flip vs A=2" and that premise had propagated into its
GENERATED VERDICT string. It is false — A=3 is +2.4701927, confirmed by the
committed witness and a fresh 30/30 re-run. Fixed under qou-rfhj. If any of the
five beans reasons from "negative through the deuteron and triton", that premise
is stale.

scope-(a): a dimensionless SIGN datum. NOT a MeV (the Delta_lambda magnitude gate
is open and untouched), NOT a physical binding-sign assertion (qou-v7ro / #6077,
cited not re-derived). The total is a weighted sum of mixed-sign terms (33+/42-).



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-11 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.



Former title (before 2026-10-04, when this became a story under a programme epic): EPIC: prove the Δ_λ covariance kernel Cov_Planch(f^λ,Σc²)≤0


## Round 82 Execution Note (2026-11-17T10:13:44Z)

- **Status**: `in-progress` (PR awaiting merge; no unilateral closure).
- **PR**: [`litlfred/qou#8294`](https://github.com/litlfred/qou/pull/8294) (`feat/qou-b9cj-ck2w-k5r5-ndt5-x3iv-x631`, HEAD `22907bca8b5dd626221c15ea2658a1f14545c5be`).
- **Lean Module**: `folio/quantum-observable-universe/lean/QOU/QBeta/PretzelSymmetryAdaptedGradingAndSubstrateBranchBrick.lean` (wired into `QOU.lean`, compiled with Lean 4.24.0, 0 findings across all 7 static Lean audits).
- **80-dps Probe & Witness**: `computations/probes/pretzel_symmetry_adapted_grading_and_substrate_branch_brick_probe.py` & `computations/probes/pretzel-symmetry-adapted-grading-and-substrate-branch-brick.witness.json` (`scriptCommitSha = caec3a2639d9338bfaf9aa9d455a0ab97b427071`, `scriptHash = 428700c5c7bd`, `outputHash = 27ee54e84b99cf035202cc1272490bd167d1f4ad8e861ae3bd043848cca760e3`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8294, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

**Review before closing:** a main commit subject names this bean with a closing word (2026-07-25: "attack(deltalambda covariance qou-x631): PROVED even hook-power moment positivity"). The work may be partly or fully done. Read the bean before you close it.
