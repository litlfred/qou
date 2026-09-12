---
# qou-juz3
title: 'Infra: Markov trace uniqueness + Wenzl embedding'
status: completed
type: task
priority: normal
created_at: 2026-08-04T01:39:43Z
updated_at: 2026-09-12T12:04:28Z
---

Blocks: prop_rigid_monoidal_structural_gap_invariance (1), markov_trace_recursive_reducer (1), delta_q_decoration (1). Need Jones Markov-trace uniqueness [jones1985] + Wenzl block decomposition [wenzl1988].


## SUPERSEDED 2026-09-12 — what this bean asks for is already proved

This bean (2026-08-04) reads *"Need Jones Markov-trace uniqueness [jones1985] +
Wenzl block decomposition"*. Both halves are now held:

* **Uniqueness:** `QOU.SchurWeyl.HeckeCoset.markovTrace_unique`
  (`MarkovTraceUnique.lean:103`), sorry-free, general `z`, generic `CommRing`.
* **The weight identification at z_D:** `eq_wtrace_of_markov`
  (`MarkovTraceInstance.lean:191`) — every Markov trace at `q^3/(q^2+1)` is the
  Ocneanu-weighted seminormal trace, i.e. the Frobenius decomposition
  `Σ_ν ocneanuWeight · tr ρ_ν`.
* **Classical source, and it is NOT jones1985:** the held copy is Chlouveraki
  HDR **Theorem 6.20** (`library/hdr/sections/sec-025-knot-invariants.md`,
  `[chlouveraki2016-hdr]`), `d = 1` case. `jones1987` and `wenzl1988` are
  *registered but NOT ingested*, so this bean's intended citation was never
  actually available — the HDR is, and suffices.

Carriers that closed it: `qou-smtg` (completed 2026-09-03) and `qou-4a68`
(completed 2026-08-24, PR #5705).

Completing as **mechanical** under AGENTS.md 13a: the subject is not an open
conjecture, it is a need-statement whose need is met, and closing it removes a
stale 'open' that a future corpus-grep would read as work remaining.
