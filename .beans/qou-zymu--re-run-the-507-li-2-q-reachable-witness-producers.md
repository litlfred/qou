---
# qou-zymu
title: Re-run the 507 li_2_q-reachable witness producers after the max_k truncation fix
status: in-progress
type: task
created_at: 2026-08-23T13:03:00Z
updated_at: 2026-08-23T13:03:00Z
---

`li_2_q` had `max_k=2000` while its own convergence needs 7,083 terms at the
brane tower's largest argument. It returned silently, so every consumer got a
value correct to ~21 digits while believing it had 70. Fixed in 935c11c33
(closed-form dispatch at |z| = 1/q, max_k raised, non-convergence now raises).

**Every witness computed before that fix is suspect at digit ~22.** That includes
the 563 regenerated in a0ee2ac5e, which used the truncated series.

## Scope — measured, not guessed

An import-graph scan (transitive closure out from `_li_2_q_util`, flat-namespace
bare-name resolution):

    modules transitively reaching li_2_q : 641
      of which are witness producers      : 528
      already re-run post-fix             :  21
      NOT yet re-run                      : 507

**528 is an upper bound, not the affected count.** It is *import* reachability:
anything importing `mass_at_3A_proper` inherits the edge whether or not it ever
calls `li_2_q`. The direct-caller set is ~25. The true affected set lies between,
and the only way to establish it is to re-run and diff — a producer is affected
iff its witness payload actually moves.

## Known affected so far

- `pentagon-reduction-li2q.witness.json` — moved at digit ~22, exactly the
  predicted truncation error.
- Of 23 direct consumers re-run, only **2** changed a real value. So the
  proportion affected is low; the tail matters because it includes proton-mass
  paths (`derive_m_p_hecke_full_tower_50dps.py`, `m_p_m_e_li2q.py`).

## Method

Re-run, then keep ONLY witnesses whose payload changed substantively — revert
provenance/timestamp-only churn rather than commit it. Two hard-won guards:

1. **Timeout must exceed the slowest producer.** A 45s cap gutted five witnesses
   mid-write; `chi-numpy-dtype-fix-benchmark` alone runs 408s.
2. **`witness_shape_guard.py` is the safety net** — a gutted witness scores zero
   raw floats, which the raw-float64 ratchet reads as a perfect drain.

## Not to be silenced

Producers whose output carries raw float64 must be fixed at the producer before
their witnesses land (three were, in dd4ac1494 — and that surfaced both casimir
producers computing at a float64 `q` wrong beyond digit 16).
