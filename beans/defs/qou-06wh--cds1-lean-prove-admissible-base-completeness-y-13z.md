---
# qou-06wh
title: 'cds1: Lean-prove admissible-base completeness — y_(1^3)(z) has exactly two roots {q, z_D}, net excluded'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - verify-build
created_at: 2026-08-28T20:42:25Z
updated_at: 2026-10-04T15:30:48Z
---

## DONE (PR #5925) — completeness Lean-proved, sorry-free

Lean file QOU/QBeta/ConventionDAdmissibleRoots.lean, lean-direct EXIT=0, no
sorry/admit/native_decide/axiom.

Extracted the exact (1^3)-weight at n=3 from the corpus Markov-character solve:
  y_(1^3)(z) = q^2 * N(q,z) / (q^4+q^2+1),  N=(q^2+1)z^2-(2q^3+q)z+q^4
and it factors over ANY CommRing:
  N(q,z) = (z-q)*((q^2+1)z - q^3)   [denom = (q^2+1)(q^4+q^2+1), never 0 over R]

Theorems: wtNumer_factor (ring), wtNumer_eq_zero_iff, second_root_eq_zD,
admissible_markov_param_iff (COMPLETENESS: roots exactly {q, z_D}),
one_not_root (z=1 = net excluded on 1<q, q<plastic ~1.4656), capstone
conventionD_base_completeness.

Hardens qou-99qc's SYMPY-measured completeness (bracket probe 15/15) into a
theorem. Distinct from #5897 (element identity) and #5337 (capped correction);
intent posted on both. Cited input: N is the (1^3)-weight numerator; the
algebra is proved. Nothing wired.



## Summary of Changes

Closed 2026-10-04 in the work-plan reorganisation: the work has landed on main. Evidence: 84489c2f56 "Lean-prove convention-D base admissibility is closed at two roots {q,z_D}" + 4e9afefa14; §4.1 cites ConventionDAdmissibleRoots.lean sorry-free; previously stalled (last activity 2026-08-29); 2 



## Verify by build (2026-10-04)

Closed on 'sorry-free on main' evidence, but the cited declaration could not be matched automatically to a file that a CI Lake target is known to compile (orphan census 2026-10-04: only 654 of 1,309 lean.refs resolve into the compiled library; ugb and fred2005 are separate required packages). Confirm with a build and `#print axioms`; reopen if it does not compile.
