---
# qou-8p1c
title: 'qou-8pl1/c: period-matrix route (Bring vs Klein) — parked until qou-8p1e drops a premise; infra requirements recorded'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-colour
created_at: 2026-08-07T00:00:00Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-8lxd
blocked_by:
    - qou-8p1e
---

Parent: `qou-8pl1`. The decisive route, and the expensive one.

## The computation

Compute the period matrix of the pinched Bring surface's normalization and match
it against the Klein quartic's known period matrix (equivalently, compare points
in the genus-3 Siegel upper half-space modulo Sp(6,Z)). This SETTLES the
conjecture either way — confirm or refute — where the discrete invariants of
`qou-8p1b` can only ever give necessary conditions.

## Infra status in this sandbox (probed 2026-08-07) — BLOCKED

| package | status |
|---|---|
| `sympy` | **installs** (1.14.0 via pip) — symbolic only, no period machinery |
| `numpy` | absent, not installed by pip in this environment |
| `scipy` | absent |
| `abelfunctions` | **not on PyPI at all** — GitHub-only (`abelfunctions/abelfunctions`), and it requires numpy + scipy + Cython |
| `sage` | absent; not pip-installable |

So the period route **cannot run here as-is**. Do not attempt it without first
resolving the stack.

## What would unblock it

Roughly in increasing order of effort:

1. Get `numpy` + `scipy` installed, then clone `abelfunctions` from GitHub
   (egress to github.com is available) and build its Cython extensions.
   `abelfunctions` computes Riemann matrices of plane algebraic curves directly,
   which is exactly the primitive needed.
2. A Sage environment (Docker or conda). Sage has
   `RiemannSurface` / `period_matrix` natively and would make this a short
   script, but installing Sage in this sandbox is a project in itself.
3. Hand-roll it: numerical integration of a basis of holomorphic differentials
   over a homology basis. Feasible in mpmath (which IS available) but the
   homology-basis bookkeeping for a pinched genus-4 → genus-3 degeneration is
   error-prone and is really what `abelfunctions` exists to handle.

## Recommendation

**Do `qou-8p1a` and `qou-8p1b` first.** They need no stack, and if the
competitor set turns out to be small and a cheap discrete invariant separates
it, the period computation may never be necessary. Only escalate here if the
discrete invariants prove insufficient.


---

## NOT THE BOTTLENECK (2026-08-07, from `qou-8p1a`)

`qou-8p1a` closed: the S_4 datum admits an infinite pencil of genus-3 curves.
So the blocked numpy/scipy/sage infra recorded above is **not what is holding
`qou-8pl1` up**.  Even with a working period-matrix stack, computing periods of
two hand-picked curves cannot close an argument whose organising datum is this
weak.  Deprioritise until `qou-8p1b` has been re-scoped to an invariant the
pinch determines; the infra requirements below stay recorded for whenever the
route is genuinely needed.

## Infra blocker is STALE — numpy/scipy/sympy do install (2026-08-07)

Correcting the recorded requirement, not reviving the route. In this
sandbox `pip install mpmath numpy scipy sympy` all succeed (numpy 2.4.6,
scipy 1.17.1, sympy 1.14.0); `litlfred/folio-assistant` also clones and
`bun install`s cleanly. So the "numpy, scipy, sage all absent" note above
is no longer accurate for the first two.

This does **not** change the deprioritisation. qou-8p1a's infinite-pencil
result is the reason this is parked, and that is unaffected by tooling.
`sage` and `abelfunctions` remain genuinely unavailable (abelfunctions is
GitHub-only and needs Cython).

Recorded so the next agent re-tests rather than inheriting a stale blocker
— the same trap that had `rho_k_co_casimir_extended` written off as
unverifiable for want of scipy when scipy installs fine.


---

## RECORDED BLOCKER IS FALSE (2026-08-07)

This bean says the period-matrix route is blocked because numpy/scipy/sage are
absent. **`cbefd99be3` on main established that numpy and scipy install fine**
in a fresh container — the recorded blocker is stale and was never verified
against a working install.

It does not matter for priority: the route is deprioritised anyway (there is no
shortlist of candidate targets left to compare, per `qou-8p1a`). But the bean
should not sit there asserting a false infrastructure claim that a future agent
might trust.

## 2026-10-10: retitled and gated on `qou-8p1e`

The old title said "BLOCKED on infra". This body has already corrected that twice:
numpy and scipy install, and only `sage` and `abelfunctions` are unavailable. The real
reason the route is parked is substantive. `qou-8pl1` records a scope-(b) exclusion of
the Bring→Klein degeneration under the chapter's three premises
(`computations/s4_marked_pair_obstruction.py`). A period-matrix comparison only matters
once `qou-8p1e` decides which premise (H1, H2 or H3) to drop. So this bean is now
`blocked_by: qou-8p1e`, and the title says why. Nothing is closed: `8pl1`'s
conjecture is deliberately left open.

## Round 67 Update (PR #8242)
- Formalized in `OctonionComplexStructureAntiFitBudgetFinkelsteinZ6PeriodMatrixTorelliAndDetanglerBand.lean` and verified via 80-dps `mpmath` witness in PR #8242.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8242, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
