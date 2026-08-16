---
# qou-x631
title: 'EPIC: prove the Δ_λ covariance kernel Cov_Planch(f^λ,Σc²)≤0'
status: in-progress
type: milestone
priority: normal
created_at: 2026-07-18T19:55:42Z
updated_at: 2026-08-15T23:07:07Z
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
