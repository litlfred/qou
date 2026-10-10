---
# qou-18s7
title: 'Run the six S-polynomial computations against the concrete q-Serre rules: discharge or refute qSerre_is_gs_basis'
status: completed
type: task
priority: normal
created_at: 2026-08-10T11:58:04Z
updated_at: 2026-08-10T12:09:11Z
---


---

## 2026-08-10 — done: the five-rule system is NOT a GS basis

`qSerre_is_gs_basis` was false of the five explicit rules. Producer:
[`computations/qserre_gs_basis_check.py`](../computations/qserre_gs_basis_check.py)
→ `qserre-gs-basis-check.witness.json`. Exact arithmetic over `ℚ(q)`.

### The docstring's overlap list was wrong

It named six "S-polynomial computations". Three of them — `(1,3)`, `(1,4)`,
`(3,4)` — are **not ambiguities at all**: those pairs share a *first* letter,
and an overlap needs a proper **suffix** of one leading word to equal a proper
**prefix** of the other. It also recorded `(2,3)` as "no overlap", and `(2,3)`
is one of the two that **fail**.

### What the check actually finds

**Five-rule system: 5 ambiguities, 2 unresolved** — both decisive, each pair of
reducts genuinely irreducible (so this is non-confluence, not a strategy
artifact):

| ambiguity | word | one way | the other |
|---|---|---|---|
| R2/R3 | `K⁻¹ K E_+` | `E_+` | `q²·K⁻¹ E_+ K` |
| R2/R4 | `K⁻¹ K E_-` | `E_-` | `q⁻²·K⁻¹ E_- K` |

Same gap twice: nothing rewrites `K⁻¹` past `E_±`, so `K⁻¹ E_± K` is stuck.
Both are true identities in `U_q(sl₂)` (`E_+ = q²K⁻¹E_+K` follows from
`KE_+ = q²E_+K`), so the algebra is fine — the *presentation* was incomplete.

**Seven-rule system** (adding `K⁻¹E_+ → q⁻²E_+K⁻¹`, `K⁻¹E_- → q²E_-K⁻¹`):
**8 ambiguities, all resolve.**

### Landed

* the two missing rules, with `qSerre_lm_6/7` and monicity proved;
* `SU2Gen.rank` corrected **again** — the new rules impose
  `rank K_inv > rank E_+` and `rank K_inv > rank E_-`, which the qou-ix9e
  ranking violated. Now `E_- < E_+ < K_inv < K`, satisfying all five
  orientation constraints, each checked by a `qSerre_lm_*` theorem;
* the axiom's overlap analysis replaced with the computed one, and the axiom
  restated of the seven-rule system.

### Status of `qSerre_is_gs_basis` now

Still an axiom, but its content changed: it is now a claim about the
**completed** system, and the critical-pair check **passes**. That is
verified-but-not-formalised — better than the unverified state qou-ix9e left it
in, worse than a theorem. Formalising the eight resolutions removes it.

### Tally

Four claims in this file examined by making them checkable; **three were false**
(`normal_form_exists`, `pbw_monomials_are_normal_forms`, `qSerre_is_gs_basis`),
plus two ranking errors. The pattern is consistent: every one of them was
protected by opacity, and failed as soon as something could check it.
