---
# qcz19
title: 'Front B (cycle exclusion): period-4 word-elimination + q-Steiner bound'
status: in-progress
type: task
priority: medium
tags:
    - reorg-2026-10-04
created_at: 2026-07-31T20:00:00Z
updated_at: 2026-10-04T15:26:07Z
parent: qcz14
---

Period-1/2/3 cycle exclusion proved (word-elimination via linear_combination).
- B1 (tractable): extend to PERIOD 4 — each primitive parity word (EEEO, EEOO,
  EOOO, EOEO up to rotation) pins the cycle value to a non-unit coeff in Z[q^pm1].
  Mechanical linear_combination per word. Does NOT generalize (words explode).
- B2 (hard): the q-Steiner / Simons-de Weger height bound D_w ∤ n_w for ALL
  admissible w — the general result; needs a valuation/height invariant D_w
  carries that n_w cannot match. Formalize-first: find the invariant before scan.
Census (<=period 18) is negative evidence only. Anti-laundering: (a)/(b) scope.

STALE-REFRESH 2026-08-29. B1 LANDED: AppendixSurreals/collatz_period4.lean proves all four primitive period-4 words (EEEO, EEOO, EOEO, EOOO) sorry-free by linear_combination. B2 (q-Steiner) is PARTLY landed and stronger than this bean anticipated: collatz_one_odd_family.lean supplies the reusable engine no_cycle_of_q_one_height (a cycle forcing D*P=n dies if phi(D) does not divide phi(n) at any q=1 evaluation phi : R -> Z) and closes TWO INFINITE families with it -- qcollatz_no_one_odd_cycle (E^{k-1}O, all k>=3) and qcollatz_no_adj_tail_cycle (the whole adjacent-tail family E^{k-m}O^m whenever 2*3^m < 2^k). So the 'height invariant D_w carries that n_w cannot match' that B2 asked to FIND has been found: it is the q=1 height. What is still missing is its GENERAL-WORD form -- every landed forcing lemma is per-word or adjacent-tail-only; there is no theorem for an arbitrary parity word. That is the live chip, opened as qou-gwrd. Re-status: B1 done, B2 partially done + successor bean.

## Round 68 Progress
- Addressed in PR litlfred/qou#8436 (`2d8b265bb4efb67d3e22c86c7d7605f3f1bb60ad`): de-vacuified with non-tautological substantive theorems, 0 sorry/axiom, 0 static audit findings, and 80-dps 2-commit witness.


## 2026-11-21T12:17:51Z — every cycle classified, sorry-free (pnp-collatz drain, https://claude.ai/code/session_01Qmmkt4pcG1jyT27PJvFyQ3)

Superseded-premise check (owner request 2026-11-21): none used; pure algebra over ℤ[q^{±1}].

Branch `claude/qcollatz-cycle-classification-2026-11-21` (commit `532c188f3`) adds `QOU/AppendixSurreals/collatz_cycle_classification.lean`. `laurent_cycle_classification` proves that every periodic orbit of the Skein–Collatz map on `LaurentPolynomial ℤ` starts at `0`, `-q⁻²` (the odd fixed point), `q⁻¹` or `1+q⁻¹` (the fundamental cycle). There is no positivity hypothesis, no real-q evaluation, and no restriction on the parity word. Proof by end-coefficient invariants:
- `ord ≤ -2`: an even step lowers the second-lowest coefficient by the lowest one and an odd step fixes it ⇒ no even step ⇒ affine all-odd fixed point.
- `ord ≥ 0`: evaluation at `q=0` adds 1 per odd step ⇒ no odd step ⇒ 0.
- `ord = -1`: the same count on the reversed polynomial.
`lean -DautoImplicit=false` exit 0, no warnings; `#print axioms` = [propext, Classical.choice, Quot.sound].

Scope: the formal ring ℤ[q^{±1}] only; says nothing about `reaches_cycle` or about classical Collatz. The PR awaits owner approval (math-repo rule). Mark completed when it merges.

**For this bean:** B2 (the general-word q-Steiner bound) is no longer needed as a separate result. The general-word statement is proved by a different invariant (end coefficients, not the q=1 height).
