---
# qou-j6f9
title: GAP HeckeCoset top-generator bubble reduction (spanning half dim H_n = n!)
status: completed
type: task
priority: normal
tags:
    - lean
created_at: 2026-08-11T11:19:12Z
updated_at: 2026-08-14T16:32:15Z
blocking:
    - qou-uoal
---

content/quantum-observable-universe/lean/QOU/SchurWeyl/HeckeCoset.lean gen_mul_span_mem: the i<m case (i = j.castSucc, absorbed via heckeIncl) is sorry-free; only the top generator (i = Fin.last m) is a Ref'd sorry (~line 215). Deep spanning half of Iwahori-Hecke basis thm: push sigma_m through descending coset reps r_j = descProd m j back into Sum_k heckeIncl(H_m) r_j via quadratic/braid relations. Template: 12 explicit HeckeDim3.gen_mul_mem reductions at n=3. Refs mathas1999 Ch1, geckpfeiffer2000 s4.4. Closing it makes span_cosetFam_eq_top + finrank_le_factorial fully sorry-free. PR 5004.
