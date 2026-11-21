---
# qou-4ocd
title: 'q-Steiner clustered residue: exclude the finite bounded-run words per k_odd (the remaining open frontier after genNoCycle_of_lead closed the spread regime)'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T14:25:28Z
updated_at: 2026-11-21T13:17:00Z
parent: qcz14
---

---

## 2026-09-08 — NOT closeable: this bean IS the open frontier. Read for the completion-candidate queue.

`scripts/bean-completion-candidates.py` flags this on `644595a0a8b`,
*"chore(beans): bean qou-4ocd — q-Steiner clustered residue (open frontier after
spread closed)"*. That is the commit that **created** this bean, not one that
completed it — cause 2/queue-creation, the same false-positive shape recorded on
`qou-ub6p` in this drain.

The title is the status: `genNoCycle_of_lead` closed the **spread** regime; what
this bean carries is the **clustered residue** — excluding the finite
bounded-run words per `k_odd` — which is open. AGENTS.md rule 13a applies
directly: the subject is open mathematics, so it stays `todo` until that
mathematics closes, not until its openness is written down.

Body is otherwise empty; anyone picking this up starts from `genNoCycle_of_lead`
and the spread-regime argument.


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

**For this bean:** the clustered bounded-run residue is covered: the classification needs no spread/clustered split and no q=1 height bound. This bean can be completed when the PR merges.

2026-11-21: PR #8846 MERGED. QOU.AppendixSurreals.CollatzCycleClassification.laurent_cycle_classification (sorry-free, standard axioms) classifies every cycle of the Skein-Collatz map on Z[q^±1]: only 0, -q^-2 and the fundamental cycle {q^-1, 1+q^-1}. Convergence/divergence stays open (not claimed).
