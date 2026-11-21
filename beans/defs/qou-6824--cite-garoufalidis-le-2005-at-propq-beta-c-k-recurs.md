---
# qou-6824
title: Cite [garoufalidis-le-2005] at prop:q-beta-c-k-recursion-from-habiro-q-difference
status: completed
pr: 8283
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:34:56Z
updated_at: 2026-11-21T12:54:01Z
parent: qou-1qhv
---

The recurrence-minimality assumption used by computations/probes/qlift_routeC_homogenized_factor_probe.py has no counterpart in the paper layer. Cite it at the block stating the Habiro q-difference recursion so the assumption is visible at the proposition, not only in a probe docstring.

**From the source**
- Abstract / Thm 1 — The colored Jones function of a knot is q-holonomic: it satisfies a finite set of linear q-difference recursions with polynomial coefficients.
  Use here: Supplies the existence-and-minimality frame the q-lift Route C probe already assumes when it certifies an order-2 inhomogeneous recurrence; a content block stating that recursion should carry it.

Source: `library/0309214v3/0309214v3.pdf` (`garoufalidis-le-2005`)
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

## Round 56 Implementation Progress (PR #8283)
- **Status:** `in-progress` (per no-unilateral-closure policy)
- **PR:** https://github.com/litlfred/qou/pull/8283 (head `f53a095b5ee34373c44ef4b0b400e85b12af4c1c`, Commit 1 `0e2f86d58bac8f2f07854f3515aabf15d9779cd3`)
- **Lean 4 Module & Theorems:** `QOU/QBeta/StokesDTBpsHolomorphicBlockAndQHolonomicRecurrence.lean` (`garoufalidis_le_q_holonomic_inhomogeneous_homogenisation` citing `[garoufalidis-le-2005]`)
- **80-dps Witness:** `computations/probes/round56-mellor-melvin-bws0-stokes-dt-qholonomic.witness.json` (`scriptHash: d98411981e4d`, `allPassed: true`, `0` raw `float64`)

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8283, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21 — cite-intake drain (wave 1)

Verdict: **done** (commit `f15966fc86a`, branch `claude/cite-intake-drain-2026-11-21`, PR #8818, issue #8814). GL2005 Thm1 cited with scope; F not shown colored-Jones; c_k ladder itself is C-frame/off ruled base (not touched)

Superseded-premise check: the edited text was read against `docs/coordination/owner-rulings.md` (photon 1+φ₀σ₀+φ₁σ₁+φ₀₁σ₀σ₁⁻¹; electron σ₀σ₁σ₀ with Hopf closure; up quark an unknot strand; two-term Lagrangian trace; T(2,n_s) withdrawn; no virtual photons). None of these forms is asserted or relied on in the cited sentences. The c_k ladder this block feeds is convention-C frame and off the ruled z_D base (qou-cds1); the added sentence is about the recursion hypothesis only and does not use the ladder values.

Status stays in-progress until PR #8818 merges.

## 2026-11-21 — PR #8818 merged

The cite-intake work above landed on main. Status set to completed.
