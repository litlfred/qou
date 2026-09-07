---
# qou-zunl
title: 'chi producer scaling wall: chi_lambda_via_gp_hoefsmit / matrix_m_mpfr explode with strand count n (214x / 679x per +3 strands) — profile, exploit symmetry + symbolic forms, unblock the ⁵Li/⁶Li chi caches (takes over #7083 qou-k54t / qou-d9wf)'
status: in-progress
type: task
priority: normal
created_at: 2026-09-07T18:25:54Z
updated_at: 2026-09-07T18:28:16Z
parent: qou-vyvt
---

Takes over #7083 (branch claude/rag-document-ingestion-options-orasrw, session ended awaiting a decision A–D on three assertions). Measured there: chi_lambda_via_gp_hoefsmit per-λ cost n=6/9/12 = 1.2 ms / 26.4 ms / 5646 ms (23× then 214×); batched matrix_m_mpfr 0.3 / 15.3 / 10386 ms (51× then 679×); word length grows only 1.34× per step, so the driver is n (basis expansion braid_to_hecke_with_avg grows with |S_n| reachable set), not the word. ⁵Li (n=15, 176 λ) did not finish 40 partitions in 3h35m; ⁶Li is n=18. Owner ask (verbatim): 'Investigate why slow — can we optimize / get rid of bottlenecks / use symmetry / use symbolic forms?' Related: qou-sv7h (binding compute cannot scale), qou-d9wf (docstring says cost independent of dim). Deliverable: a profile that names the bottleneck, a faster route (symmetry: bar / conjugation / Murnaghan–Nakayama; symbolic: Laurent in q then evaluate), and the ⁵Li/⁶Li caches regenerated on the borromean word if feasible — which dissolves #7083's A–D question.
