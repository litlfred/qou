---
# qcz8
title: 'Attack B: full nontrivial-cycle exclusion (affine A≠1 case)'
status: completed
type: task
priority: medium
tags:
    - reorg-2026-10-04
created_at: 2026-07-24T16:46:17Z
updated_at: 2026-11-21T13:17:00Z
parent: qcz14
---

Goal: no periodic orbit with holonomy A = [3]_q^{ko}/[2]_q^k ≠ 1 other than
the fundamental cycle. Census shows none through period 18 (negative evidence).

Routes:
B1. CYCLE-VALUE INTEGRALITY OBSTRUCTION. A period-k word w has candidate
    P0 = n_k / D_w with D_w = [2]_q^k - [3]_q^{ko} in Z[q^±1] (see
    balanced-holonomy note + census). Show D_w ∤ n_k for all admissible w
    (except the fundamental). q-analog of classical cycle-value bounds
    (Steiner / Simons-de Weger). Lean/compute: bound the [2]_q-adic and
    degree valuations of n_k vs D_w. Formalize-first: is there a valuation
    invariant that D_w carries but n_k cannot match?
B2. POSITIVITY + PARITY-WORD CONSISTENCY. Even if D_w | n_k, P0 must (i) be
    in the positive cone and (ii) have actual parity word = w. Show the
    joint constraint is unsatisfiable for A≠1. The census's exact-Laurent
    machinery (computations/qcollatz_cycle_census.py) already tests this —
    extend to a proof of the obstruction, not just enumeration.
B3. DOMAIN-STABILITY CONSTRAINT. A genuine cycle is domain-stable; combine
    the D∞ characterization (qcz7 A1) with integrality (B1) to squeeze out
    A≠1 candidates.

Deliverable: a proved exclusion for a sub-family (e.g. bounded ko, or
A<1 contractive words) OR an honest wall. Do NOT write 'REFUTED/excluded'
in durable artifacts without the (a)/(b) scope classification.

PROGRESS (period-1 case CLOSED): qcollatz_odd_fixed_point (odd fixed pt forces q^2 P = -1) + qcollatz_neg_qinv_sq_is_odd_fixed (-qinv^2 is that fixed pt), both sorry-free. => the ONLY odd-branch fixed point is -q^-2 (negative), no POSITIVE fixed point exists; fundamental cycle is genuinely 2-periodic. Still open: period>=2 affine cycles (B1 integrality obstruction).

PERIOD-1 CLOSED (odd fixed pt -q^-2, even fixed pt 0, neither positive). WALL: period>=2 affine exclusion = q-analog Steiner/Simons-de Weger cycle-value bound (needs height/valuation input). Census (<=period 18) is negative evidence only. Documented in the 2026-07-18 audit.

PERIOD-2 CLOSED: qcollatz_period2_eveneven (EE => q(q+2)P=0 => P=0), _oddodd (OO => (q^2+2q+2)(P-P1)=0 => P=P1, degenerates), _evenodd (EO => q*P1=1 => P1=q^-1, the fundamental). Only positive 2-cycle is {q^-1,1+q^-1}. Sorry-free. Period>=3 still open (q-Steiner).



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-07-24 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## Round 69 Update (2026-11-18T11:37:12Z)
- Addressed in PR `litlfred/qou#8454` (HEAD `23a754272622fa31774e4f5d1455018224c86d36`, C1 `bcdf148ad3ef8ce5d5b1c640e65680b5b11b62b6`).


## 2026-11-21T12:17:51Z — every cycle classified, sorry-free (pnp-collatz drain, https://claude.ai/code/session_01Qmmkt4pcG1jyT27PJvFyQ3)

Superseded-premise check (owner request 2026-11-21): none used; pure algebra over ℤ[q^{±1}].

Branch `claude/qcollatz-cycle-classification-2026-11-21` (commit `532c188f3`) adds `QOU/AppendixSurreals/collatz_cycle_classification.lean`. `laurent_cycle_classification` proves that every periodic orbit of the Skein–Collatz map on `LaurentPolynomial ℤ` starts at `0`, `-q⁻²` (the odd fixed point), `q⁻¹` or `1+q⁻¹` (the fundamental cycle). There is no positivity hypothesis, no real-q evaluation, and no restriction on the parity word. Proof by end-coefficient invariants:
- `ord ≤ -2`: an even step lowers the second-lowest coefficient by the lowest one and an odd step fixes it ⇒ no even step ⇒ affine all-odd fixed point.
- `ord ≥ 0`: evaluation at `q=0` adds 1 per odd step ⇒ no odd step ⇒ 0.
- `ord = -1`: the same count on the reversed polynomial.
`lean -DautoImplicit=false` exit 0, no warnings; `#print axioms` = [propext, Classical.choice, Quot.sound].

Scope: the formal ring ℤ[q^{±1}] only; says nothing about `reaches_cycle` or about classical Collatz. The PR awaits owner approval (math-repo rule). Mark completed when it merges.

**For this bean:** B1/B2/B3 are all superseded by a full classification. The affine (A≠1) nontrivial-cycle exclusion holds for every word, so this bean's goal is met once the PR merges.

2026-11-21: PR #8846 MERGED. QOU.AppendixSurreals.CollatzCycleClassification.laurent_cycle_classification (sorry-free, standard axioms) classifies every cycle of the Skein-Collatz map on Z[q^±1]: only 0, -q^-2 and the fundamental cycle {q^-1, 1+q^-1}. Convergence/divergence stays open (not claimed).
