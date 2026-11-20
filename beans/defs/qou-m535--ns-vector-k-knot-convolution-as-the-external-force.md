---
# qou-m535
title: 'NS vector K: knot convolution (#) as the external force — forced-NS reformulation via ILP/SDP operator selection'
status: todo
type: task
priority: normal
created_at: 2026-10-12T21:00:36Z
updated_at: 2026-11-20T08:32:31Z
parent: qou-vo9t
---

Owner idea (2026-10-12): treat knot convolution # (see the sibling ILP/SDP operator-selection work) as the external FORCE f, making the corpus's NS question a forced one, closer to the reported OpenAI construction (Fefferman C/D). Assess honestly.

## 2026-10-12 — assessment (audit `docs/audits/2026-10-12-ns-vector-k-knot-convolution-force.md`)

Verdict: (d) as stated. A narrow conditional (a) can be stated but adds nothing beyond the analytic construction.

- **What "#"/"convolution"/"ILP" are.** `#` is connected sum (`knot-notation-convention.md:13`). The convolution is `*_q` on the depth × knot-cell bi-filtration (`hq-bi-filtration.md:15-20,50`), which is depth-0 algebraic and has no space or time. The dual-bearing operator-selection LP is PROVED degenerate: optimum 0, `y0*=0`, non-unique minimiser (`operator-selection-lp.md:34-56`). The finite knot-operator ILP picks one word by length plus a `|tr_M|` tiebreaker (`qbeta_knot_operator_ilp_ohara_cost_probe.py:6-9,53-56`). It outputs no scale, amplitude or time.
- **No knot/braid → vector-field dictionary exists in the corpus.** `braid-fluid` is an interpretive remark, and q-NS has no forcing term. The literature dictionaries (Enciso–Peralta-Salas, Enciso–Lucà–Peralta-Salas, Etnyre–Ghrist) point toward regularity: viscous NS changes knot type smoothly.
- **The analytic core, derived.** `f ∈ C^∞` with level-k pieces at frequency λ_k forces the amplitudes `a_k = O(λ_k^{-m})` for every m. The force can only seed the cascade; all the content is in amplification and error control. Choosing knot-labelled seeds because the flow blows up is selection against the target, unless the smoothness of `f` is proved, and a label neither adds nor discharges that obligation.
- **Coexistence.** A forced (C)/(D) result neither implies nor is implied by (A)/(B). If ever added, it would go in a separate "forced problem" remark that leaves NS(A) untouched.
- **Recommendation (judgement).** Do not add content now. Optional cheap step: a Lean lemma on the smooth-forcing amplitude budget (audit §5c). Stays open per rule 13a.


**2026-11-20T08:32:31Z — owner-approved status change (coordinator session_01VQDpPdnjTBLBcPi6D5gj61, PR #8542 batch C):** in-progress → todo. Open conjecture: stale claim released; never to be completed while the conjecture is open (AGENTS rule 13a).
