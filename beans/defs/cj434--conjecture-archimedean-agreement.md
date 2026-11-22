---
# cj434
title: 'Conjecture carrier: archimedean_agreement (archimedean_agreement.lean) — §3b, framework/substrate §3b carrier'
status: in-progress
type: task
priority: low
tags:
    - reorg-2026-10-04
created_at: 2026-07-05T13:20:00Z
updated_at: 2026-11-22T21:58:00Z
parent: qou-j5ch
---

§3b conjecture-class Lean carrier `instance : archimedean_agreement := sorry` at folio/quantum-observable-universe/lean/QOU/BraidKnot/HabiroResidueSumEquivalence/archimedean_agreement.lean:39. The sorry IS the conjecture (per AGENTS.md §3b) — do NOT fabricate an instance (audit-dodge). Category: framework/substrate §3b carrier. Track backing/derivation status; advance only via genuine derivation or owner-directed reframing. Parent: b9cj.

## Progress Update (2026-11-18 — Round 66, PR #8415)

- Added conditional interval enclosure (`eval_mem_interval`), zero-tolerance exactness (`eval_eq_of_zero_tolerance`), pipeline symmetry (`symm_agree`), and tolerance monotonicity (`mono_tolerance`) in `QOU/BraidKnot/HabiroResidueSumEquivalence/archimedean_agreement.lean` (PR litlfred/qou#8415).

## 2026-11-22T21:58:00Z: applicability review — APPLIES

Owner instruction 2026-11-22 ("reviewed for applicability ... critical analysis"). Checked against docs/coordination/owner-rulings.md on origin/main, git log since the bean's last update, and the state of every PR it cites. The generic carrier is word-independent and compares two internal evaluations, so the absolute-mass ruling (qou-exam) does not bite. FLAG for the sibling block, not this bean: conj:gs-archimedean-agreement-residue records 2.1225825095 for the proton word T_w(Z=1,N=0) at u0 = sqrt(q0) without naming the Markov z or the q0 pin, and it predates both the 2026-11-15 supersession of the single-crossing atom letters and the 2026-11-22 ruling that selects beta_Bor = (s0 s1^-1)^3 by energy minimisation. That value should not be cited until recomputed or scoped. #8415 open, unmerged.
