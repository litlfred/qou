---
# cbnf
title: Categorical binding wiring (NO fitting) — derive (1+q)/2, not a 7th Δ_λ ansatz
status: completed
type: task
priority: normal
created_at: 2026-06-16T02:14:00Z
updated_at: 2026-06-21T19:39:07Z
parent: qz9k
---

## Result (2026-06-16) — state pinned + non-fit direction sharpened; pending human close

Finding delivered:
[`docs/audits/2026-06-16-categorical-binding-wiring-state-and-no-fit-direction.md`](../docs/audits/2026-06-16-categorical-binding-wiring-state-and-no-fit-direction.md).

- **Wired vs exploratory pinned:** B_sym + B_magic + LP/SDP dual = production;
  B_lin/B_qCLT + Option-E v9 (1+q)/2 = exploratory.
- **(1+q)/2 is a REFUTED near-match** (PR #1707): "0.11%" was a stale muon-anchor
  literal; at canonical q₀ it's +0.12% sign-flipped; 4 structural hypotheses killed;
  only "matches" are tautologies. Stays un-wired, A=3 OPEN, **no v10 ansatz**. So this
  bean does NOT re-attempt (1+q)/2.
- **Non-fit direction = GAP-A-3** two-layer factorization Δ_λ(K)=A(K)·P_λ(K), A(K)
  already derived (Phase-4 ≤2.5%), P_λ open (color/spin/normalization channels).
- **Grounded structural observation (value-add):** since tr_M(β)=Σ_λ y_λ χ^λ(β)
  (Frobenius), P_λ≡1 recovers A(K)·tr_M(β_K) exactly ⇒ P_λ is the per-partition
  **deviation of binding from the flat mass/trace distribution**. Gives the §4 probe a
  free baseline + a bar-even (λ↔λᵀ) admissibility constraint.
- **No probe run** — §4 needs canonical χ^λ(β_D) at q₀ (same infra blocker as Hoefsmit
  Stage B; no pyhecke_native) + plethystic-content wiring. Next step on infra-enabled
  session. Appendix-sync contract recorded.

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
  `computations/lp_dual_solver.py`.
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

TRIAGE VERDICT (2026-06-20, "wire now?", session intelligent-pasteur): NOT-YET — nothing wireable. (1+q)/2 confirmed a REFUTED near-match (+0.12% at canonical q0; only tautological [2]_q/2 / (q+1)/2 "match", all independent objects miss 18–90%; docs/audits/2026-06-02-option-e-derive-1plusq-over-2.md, ledger docs/coordination/option-e.md "TESTED → NEAR-MATCH (fit)"). Stays un-wired per the Δ_λ gate; NOT a v10 ansatz. Currently WIRED in production: B_sym (log-trace), B_magic (⁴He), LP/SDP dual contract. The genuine non-fit direction = GAP-A-3 factorization Δ_λ(K)=A(K)·P_λ(K) with A(K) derived (≤2.5%, zero-param) and P_λ(K) OPEN (brane-tower content count). Per bean g3pl that probe is "already run/exhausted; converges on conj:s5-so3-fiber-action". Infra (pyhecke_native χ^λ at q0 + plethystic multiplicity) is buildable per bean pyhk, but P_λ is the OPEN MATH — it reduces to the s5-so3 q-closure (bean s5bb). So: not wireable this session; bottleneck is the s5-so3 keystone, not infra.
