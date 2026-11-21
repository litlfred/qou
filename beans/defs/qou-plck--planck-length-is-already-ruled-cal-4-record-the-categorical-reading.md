---
# qou-plck
title: 'Planck length: already ruled a CAL-4 violation in the corpus — the live reading is categorical, not metric'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-06T10:56:11Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-ddmn
---

ANSWERED IN THE CORPUS, both halves, found by corpus-grep path 2:

1. FORBIDDEN AS AN INPUT.
   folio/quantum-observable-universe/braids-and-knots/meridian-exceptional-divisor-note.md:9
   "Identifying the computational tick with the Planck time would pin the
   substrate at m_Planck, i.e. introduce Newton's constant G — an input outside
   the three-calibration weak sector. That is a fourth calibration and a
   substrate-scale derivation, which the framework does not undertake."
   Also blocked by the 2026-08-02 FOREVER GATE on substrate-q_0 derivation.

2. THE ADMISSIBLE READING IS ALREADY WRITTEN.
   folio/quantum-observable-universe/brings-surface/approach-to-exceptional-divisor.md:3
   "'Below Planck scale' in QOU is a CATEGORICAL statement, not a metric one.
   The relevant geometry switches from the base M to the fibre S_p."
   And observations/g-q-closed-form.md carries G in PLANCK UNITS as a
   dimensionless q-rational (G_Planck = 1), i.e. as a RATIO, which is the only
   way a gravitational scale is allowed in.

SO: l_P may enter only as a dimensionless ratio derived from (m_e, D_beta,
D_pi); it may never be an input, and it may not be used to pin the substrate.
Open sub-question worth one paragraph, not a tranche: is the fibre S_p (the
exceptional divisor) the right "sub-Planck" object to attach a triangulation
to? That is a question about the CATEGORICAL statement above, and needs no
new dimensional constant.

## RECORDED 2026-09-06 — both halves written up; one sub-question STAYS OPEN

docs/audits/2026-09-06-universal-triangulation-ep-route-assessment.md §5 carries
both halves with their content-block citations. NOT closed: the open
sub-question -- whether the fibre S_p (the exceptional divisor) is the right
object to attach a decomposition to -- is a question about the categorical
"below Planck scale" statement and is unresolved. AGENTS.md 13a: recording that
something is open is not closing it.

## 2026-09-06 SELF-CORRECTION — Planck length is NOT a calibration

Owner: "plank length is not a calibration.. written symbolic in q". Correct, and
this bean's own title is now wrong. I generalised meridian-exceptional-divisor-
note into a prohibition on the Planck length as such; that note forbids something
narrower -- pinning the SUBSTRATE at m_Planck, i.e. importing SI G as an input
that fixes q0. Writing ell_P(q) is a different move and is already done here.

MEASURED (planck_symbolic_in_q_probe, 8/8), from the corpus's own q-forms
hbar_q = (q-1)/q, c_q = 1/(q-1), G_q = q^2/(q-1)^4:
  G in Planck units = G_q*(hbar_q/c_q)^2 = 1 IDENTICALLY (exact rational
    function -- verifies g-q-closed-form.md's own assertion)
  ell_P = sqrt(hbar_q G_q / c_q^3) = sqrt(q)
  m_P   = sqrt(hbar_q c_q / G_q)   = (q-1)^2 / q^(3/2)
  t_P   = sqrt(hbar_q G_q / c_q^5) = sqrt(q)*|q-1|
Each is a function of q ALONE -- no m_e, no CODATA, no SI G. Not calibrations.

NEW FINDING, recorded not resolved: THREE inequivalent objects carry the name
"Planck length" here.
  normalised total (discrete-planck-step)  hbar_q * q/(q-1) = 1      -> 1
  per-step share   (p5-counterexample)     (q-1)/q = hbar_q          -> 0.09908
  dimensional      (derived; NO corpus block carries it)  sqrt(q)    -> 1.05356
The corpus already separates the first two explicitly. Share vs dimensional
differ by 10.633x at the proton q0. Which one a given block MEANS is an author
question. STAYS OPEN.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8462, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21 — physics-scope re-check on main 2ae54ab40 (bean-drain sibling, issue #8810)

Unchanged. The three-objects-named-Planck-length question is an author question; no edit proposed. Audit: `docs/audits/2026-11-21-physics-claim-scope-recheck.md` on branch `claude/physics-scope-audit-2026-11-21` (4df574c79).

## 2026-11-21 — superseded-premise check (owner instruction 2026-11-21, physics-scope sibling)

Checked against `docs/coordination/owner-rulings.md` on main: no superseded premise found (L± photon, virtual photons, pre-Nov-15 γγ letters, T(2,n_s), convention C, one-term trace, trefoil-as-electron, c₂ = −1, χ₍₂,₁₎ = 2 − h⁴, fitted α/CODATA in proofs, project memory).
