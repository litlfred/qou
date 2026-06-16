---
# cbnf
title: 'Categorical binding wiring (NO fitting) — derive (1+q)/2, not a 7th Δ_λ ansatz'
status: in_progress
type: task
priority: normal
created_at: 2026-06-16T02:14:00Z
updated_at: 2026-06-16T02:14:00Z
parent: qz9k
---

## Goal

Advance the **categorical** wiring of the per-isotope binding formula
$$ B(K) \;=\; m_e \sum_\lambda y_\lambda\, \chi^\lambda\, \Delta_\lambda $$
**without fitting**. Per STATUS.md (`Δ_λ closure / Option-E`): the deuteron is
CLOSED; the A=3 mirror pair sits at a 0.11% near-match where a factor
**(1+q)/2 is NOT yet derived**. The genuine open piece is deriving that factor
**categorically** — not by a new fit.

## Corpus state (session start)

Master ledger: [`docs/coordination/option-e.md`](../docs/coordination/option-e.md).
Gating context: [`docs/audits/2026-05-18-delta-lambda-gating-context.md`](../docs/audits/2026-05-18-delta-lambda-gating-context.md).
Mass-table wireup: `docs/workplans/2026-06-03-per-knot-mass-table-wireup-workplan.md`.
Appendix contract: `content/quantum-observable-universe/appendix-mass-binding-algorithms/`.

(Background Explore agent mapping exact wired-vs-exploratory state, the 6 failed
ansätze, GAP-A-3/A-4, and the appendix alg: blocks; results to be folded in.)

## Discipline (this is the whole point of the bean)

- **SIX Δ_λ closure ansätze have ALL FAILED on the deuteron** (Frobenius
  co-Casimir, Demazure-fibre, LP-Plancherel, LP-Frobenius, crystal-graph,
  augmented Markov). **Do NOT propose a seventh fit-based ansatz** — the
  three-calibration review will catch it.
- Productive (non-fitting) directions only: **GAP-A-3 / GAP-A-4** (categorical
  brane-tower level selection / ρ general rule) and **Option E** (Kashiwara
  crystal). The (1+q)/2 must emerge from one of these as a structural identity.
- Any operator-selection/LP compute MUST emit primal AND dual
  (`y0_star`, `y_star`, `active_set`, `duality_gap`) via
  `folio-assistant/computations/lp_dual_solver.py`.
- Any binding/Δ_λ compute change MUST sync the matching `alg:` block under
  `appendix-mass-binding-algorithms/` in the same PR.

## Plan (formalize-first)

1. Pin exact wiring state: which Δ_λ/binding forms feed the canonical
   dashboard vs which are exploratory.
2. Pin the (1+q)/2 context: exactly what it multiplies in the A=3 mirror pair
   and why a categorical derivation is missing.
3. Identify the structural invariant (brane-tower level / crystal weight) that
   could FORCE (1+q)/2 — formalize it; if it forces a different factor, that's
   a refutation, recorded tiered.
4. Wire only a derived identity (never a fit); keep appendix + dual in sync.

## Acceptance

Either (a) a categorical derivation (or tight structural constraint) of the
(1+q)/2 A=3 factor wired with appendix+dual sync; or (b) a formalize-first
refutation narrowing the candidate structure. NO 7th fit-ansatz, NO CAL-4.
