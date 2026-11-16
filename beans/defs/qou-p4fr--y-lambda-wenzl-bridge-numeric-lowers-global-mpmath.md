---
# qou-p4fr
title: y_lambda_wenzl_bridge_numeric lowers global mpmath precision and never restores it
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-13T09:21:45Z
updated_at: 2026-11-16T19:56:39Z
parent: qou-9nnz
---


## The defect

`computations/y_lambda_wenzl_bridge.py` — the impl behind
`y_lambda_wenzl_bridge_numeric(partition, q_val, dps=50)` assigns
**`mp.mp.dps = dps` globally and never restores it** (7 such assignments in
that module). A caller working at higher precision that passes a literal
`dps=50` therefore has its working precision silently lowered for everything
that follows the call.

## How it surfaced — it destroyed a finite difference

Writing `magnus_omega2_markov_stabilisation_probe.py` (bean `qou-gba1`) at
`mp.mp.dps = 140` with `dps=50` at the call site, the probe's germ

    A_g = q·(∂_q σ_g)·σ_g⁻¹,   central difference at EPS = 1e-50

lost every significant digit — a 1e-50 difference cannot survive at 50 dps.

**It failed loudly only by luck of good design.** That probe validates the
differentiated-Hecke identity `σσ' + σ'σ = h'σ + hσ'` per generator and
asserted on shape (5,1). A caller without such a check would have got quietly
wrong digits and a witness that looked fine. That is the whole argument for
fixing it at the source rather than at the call sites.

## Blast radius, measured

15 call sites pass a literal `dps=50`, 10 pass `dps=dps`, 4 pass `dps=mp.mp.dps`,
1 each `dps=DPS` / `dps=80`. Of the 15 literals, **exactly one** works above
50 dps — `computations/y_lambda_at_q0_cache.py` at 60 — and it already guards
with `with mp.workdps(60):` and wants 50 for serialisation. **So there is no
live victim today.** This is a latent trap, not an outage.

## The fix

Wrap the impl body in `with mp.workdps(dps):` so the caller's precision is
restored on exit. Strictly safer in one direction: it can only *preserve* a
caller's precision where today it lowers it.

**The risk to check before landing it** is the mirror case — a caller that
depends on the side effect, i.e. that calls the bridge and then relies on
`mp.mp.dps` having become 50 afterwards. Grep for a bridge call followed by
mpmath work with no explicit dps set in between. If any exists, fix that
caller in the same change; do not leave the side effect in place for it.

Regenerate every witness whose producer passes a literal `dps` below its own
working precision and diff the numerics — the point of the change is that some
digits may move, and they should be *checked*, not assumed unchanged.

## Interim

Warned in the entry point's docstring (2026-09-13) with the incident and the
`dps=mp.mp.dps` guidance, since that is where the next person looks. The
warning is not the fix.

## Progress Update (Round 50 — PR #8178)

- Wrapped `_wenzl_norm_numeric_cached`, `_y_lambda_wenzl_bridge_numeric_impl`, `chi_lambda_mpmath`, `markov_m3_sum_numeric`, `markov_trace_lhs_numeric`, and `markov_trace_target_numeric` in `computations/y_lambda_wenzl_bridge.py` with `with mp.workdps(dps):` so calling them at a lower `dps` restores the caller's ambient working precision on exit; added `--self-test`.
- PR: https://github.com/litlfred/qou/pull/8178 (`6465362ef2e7902778c4f8796f81286e3aeb81bc`)
