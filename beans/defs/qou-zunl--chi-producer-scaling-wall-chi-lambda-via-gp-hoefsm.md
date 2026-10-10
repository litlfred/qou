---
# qou-zunl
title: 'chi producer scaling wall: chi_lambda_via_gp_hoefsmit / matrix_m_mpfr explode with strand count n (214x / 679x per +3 strands) — profile, exploit symmetry + symbolic forms, unblock the ⁵Li/⁶Li chi caches (takes over #7083 qou-k54t / qou-d9wf)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-07T18:25:54Z
updated_at: 2026-10-04T15:12:06Z
parent: qou-5vkl
---

Takes over #7083 (branch claude/rag-document-ingestion-options-orasrw, session ended awaiting a decision A–D on three assertions). Measured there: chi_lambda_via_gp_hoefsmit per-λ cost n=6/9/12 = 1.2 ms / 26.4 ms / 5646 ms (23× then 214×); batched matrix_m_mpfr 0.3 / 15.3 / 10386 ms (51× then 679×); word length grows only 1.34× per step, so the driver is n (basis expansion braid_to_hecke_with_avg grows with |S_n| reachable set), not the word. ⁵Li (n=15, 176 λ) did not finish 40 partitions in 3h35m; ⁶Li is n=18. Owner ask (verbatim): 'Investigate why slow — can we optimize / get rid of bottlenecks / use symmetry / use symbolic forms?' Related: qou-sv7h (binding compute cannot scale), qou-d9wf (docstring says cost independent of dim). Deliverable: a profile that names the bottleneck, a faster route (symmetry: bar / conjugation / Murnaghan–Nakayama; symbolic: Laurent in q then evaluate), and the ⁵Li/⁶Li caches regenerated on the borromean word if feasible — which dissolves #7083's A–D question.

## 2026-09-08 ~04:20Z — DONE on PR #7160 (branch claude/chi-scaling-wall-symmetry-symbolic-2026-09-07, 4 commits, head 681ce3a8e77). The agent could not see this bean (branch-only) and minted qou-s7ld on its branch; qou-s7ld is the live carrier, this bean is its ledger twin.

Verdict: the wall is the minimal-length reduction inside chi_q_via_gp (>99 % at n=12: 7385 ms vs 62 ms expansion+Hoefsmit vs <1 ms seminormal), NOT dim V_λ and NOT the T_w expansion (support is exactly 6^A). Level-local path-sum computations/chi_path_sum_seminormal.py: χ^λ(T_β) = Σ_{T∈SYT(λ)} Π_j ⟨T|F_j|T⟩, dim-free; ⁵Li 2.5 s (176 λ), ⁶Li 8.5 s (385 λ), cross-checked ≤1.2e-49 vs the Rust seminormal kernel. Second finding: D/T/³He/⁵Li/⁶Li matrix-m caches on main were on the pre-2026-09-05 GROUPED word (only ⁴He was borromean); all five regenerated on the borromean word (D/T/³He in revertible 9917730f17f). NOT re-run: four deltalambda/ consumers (delta_lambda_empirical_tabulation, carrier_table_convention_d_rederivation, li6_h18_amplification_discriminator_probe, carrier_saturation_mechanism_probe) — their witnesses are now stale. Open: reduction complexity class; level-locality of unified_iterative_correction words (qou-sv7h) — same identity would apply.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-08 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
