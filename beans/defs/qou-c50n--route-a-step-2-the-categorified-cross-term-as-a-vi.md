---
# qou-c50n
title: 'Route A step 2: the categorified cross term as a VIRTUAL Soergel object — KL-basis decomposition of the two n=4 Bott–Samelson words (Elias–Williamson) and the Markov trace on indecomposables'
status: completed
type: task
priority: normal
created_at: 2026-09-06T04:14:58Z
updated_at: 2026-09-06T04:14:59Z
parent: qou-2akx
---

(Re-created 2026-09-06: the first file for this bean minted the ID qou-s82c, which collided with an existing bean 'unify the two yekutieli-triple modules'; that duplicate file is removed and this is the live carrier.)

## 2026-09-06 — DONE, 12/12: interleaving_cross_term_soergel_kl_probe.py (witness q0-independent; merged via #6891 as 0b84dfb9a0 → main 6f0c7c34f0)

Exact, sympy over Q(v) (framework q = Soergel v; T_s = v·g_s; C'_s = g_s + q⁻¹):
- KL polynomials of S_4 by the KL recursion; P_{e,3412} = P_{e,4231} = 1+q_H, all other P_{e,w} = 1; nonneg + degree bound.
- Bott–Samelson objects (Soergel categorification + Elias–Williamson): sequential word = (v+v⁻¹)²·C'_{s0s1s2} — four shifted copies of ONE indecomposable; interleaved word = C'_{3421 (4-cycle, ℓ=5)} + C'_{2413} + C'_{3214}, multiplicity 1 each. No shared summand.
- Rouquier classes ∏T_s (the braid words; HHH(Rouquier) = HOMFLY-PT homology) expanded in the KL basis with SIGNED coefficients (top term v⁵·C'_{3421}); v⁻⁵·tr_M reproduces I(q), S(q); v⁻⁵·tr_M([int]−[seq]) = Δ(q) EXACTLY.

VERDICT: Δ is the Markov trace of an intrinsic virtual Soergel object — the categorification route A wanted, with no chain map; the categorical name of 'interleaving' is the length-5 indecomposable of the 4-cycle. OPEN: whether the binding functional can see that summand — a nucleus must be an interleaved word class first (qou-5vhf).
