---
# qkhc
title: 'Q_β kernel hunt — Stage C (fibre-level Habiro/recurrence kernel for c_k)'
status: in_progress
type: task
priority: normal
created_at: 2026-06-16T02:14:00Z
updated_at: 2026-06-16T02:14:00Z
parent: qz9k
---

## Goal

Continue the Q_β kernel hunt into **Stage C**. Target: a **fibre-level**
Habiro element / recurrence kernel $F(q)\in$ Habiro ring whose archimedean
evaluation at the substrate $q_0$ reproduces the precision-ladder coefficients
$c_k$ in $Q_\beta = Q_{\text{base}}\cdot\prod_k (1 + c_k u^k)$,
$u = b\,\hbar_q^2 \approx 0.00852$.

## Corpus state (session start)

Master ledger: [`docs/coordination/1ppq-qbeta.md`](../docs/coordination/1ppq-qbeta.md).
Stage B is defined in
[`docs/scope/2026-06-04-hoefsmit-stage-b-per-block-tbeta-scope.md`](../docs/scope/2026-06-04-hoefsmit-stage-b-per-block-tbeta-scope.md).
Relevant audits:
- `docs/audits/2026-05-30-qbeta-recursive-pair-rules-and-habiro-pde.md`
- `docs/audits/2026-06-04-qbeta-1ppq-keystone-exact-construction-recipe.md`

(Background Explore agent reconstructing Stage A/B exactly + the refuted-mechanism
list + canonical scripts; results to be folded in before Stage C is fixed.)

## Discipline (read before any wire/un-wire)

- `c_2 = -1` PROVED Taylor-exact; `c_3` is a q_0-dependent **NEAR-MATCH**
  (NOT Taylor-exact) — settled 5×, flip-flop history in the ledger. `c_4..c_7`
  are §3b-cond classes (PR #1587). Report TIERED, never binary.
- **Fibre vs observable**: the c_k live in the fibre (formal q, possibly
  complex). Do NOT hunt a real closed form `c_3 = f(q_0_real)` — already known
  to fail. Hunt a fibre element whose evaluation at each anchor gives that
  anchor's c_3 (parallels α_EM `[2]_q·(1-h²α)`, PR #1511).
- Do NOT repeat already-refuted mechanisms (#1..#7+; e.g. Li_2^q × spectral
  combiner = mech #7, refuted PR #1609).

## Plan (formalize-first)

1. Pin Stage A and Stage B definitions precisely (from the scope doc) so
   Stage C is the genuine next increment, not a re-run.
2. Tabulate the refuted kernel mechanisms; pick the most promising UNTRIED
   structural angle (q-Lommel 3-term recurrence is the current candidate per
   beans v3po/vwpi — verify).
3. Formalize the invariant the kernel must satisfy (parity / bar-symmetry /
   recurrence order) to prune the class before any wide PSLQ-style scan.
4. Run only the survivors; report tiered.

## Acceptance

A scoped Stage-C definition + at least one formalize-first pruning result
(kills or constrains a kernel sub-class), recorded in the ledger with tiered
status. NO production wire/un-wire flip without ledger + tiered justification.
