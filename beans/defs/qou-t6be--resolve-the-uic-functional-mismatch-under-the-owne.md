---
# qou-t6be
title: Resolve the UIC functional mismatch under the owner's Lean-provability criterion
status: completed
type: task
priority: normal
created_at: 2026-09-12T20:22:13Z
updated_at: 2026-09-12T20:22:48Z
---

## Owner ruling, 2026-09-12, verbatim

> **"resolve functionals ... what lean provable"**

The authorisation to resolve what PR #7230 (bean `qou-zlra`) deliberately left
open, plus the criterion: the functional the corpus keeps is the one that is
**Lean-provable**, not the one with better numbers.

## What was resolved, and what decided it

PR #7237, branch `claude/uic-functional-resolution-2026-09-12`.
Audit: `docs/audits/2026-09-12-uic-functional-resolution.md`.

**The discriminator.** `prop:unified-iterative-correction`'s summand reads the
trace only through `ln|tr|`, so it is EVEN in the trace; the producer's Pass-2
gate reads `sign(tr)`, which evenness has destroyed. Proved sorry-free in
`QOU.MassTheory.UICFunctionalSelection.gate_not_a_function_of_displayed_data`
and `UICLogSummandEven.logRatio_even`; measured in
`computations/probes/uic_functional_resolution_probe.py` (16/16) — flipping
every trace's sign leaves the ungated total BIT-IDENTICAL and moves the gated
one `-0.0895596831 -> -0.3226525092` (2H). **So the block's formula could not
denote the producer's functional, whatever the physics.** Something had to move.

**Four divergences, all resolved against the CONTENT SIDE; the producer is
untouched and no number moves.**

1. `u_lambda` as "Frobenius positivity LP shadow price" — refuted on BOTH
   readings. Net-constraint dual provably 0 (`y_0_eq_zero_of_radical`,
   sorry-free); Frobenius duals of that LP are `e_0` (`qou-8na1`); and the
   partition-indexed solve `prop:mass-coefficient-shadow-price:22-28` allows is
   `(1,1,0)` at H_3 against the producer's measured
   `(0, 0.166953658774, 0)`. The upstream block was already corrected on
   2026-08-25 / 2026-09-05 (PR #6752) and this one was left behind.
2. The q-Laplacian resolvent `rho_lambda(s_*)` was absent from the block.
   **This was the BIGGER divergence and PR #7230 ranked it the lesser one:**
   deleting it moves the gated total 4.1208754x (A=2) and 9.8660639x (A=4),
   against the gate's own 4.6026535x / 3.4030381x.
3. "sums these strictly over all lambda" did not describe the gated sum.
4. **Found by qa-sweep, not by the analysis:** the block's own `.lean` sibling
   `stepDelta` carries `m_e * H_q * w_lambda` — a THIRD scale, matching neither
   the producer's superseded Kerov nor its live resolvent one, omitting
   `y_lambda` entirely. Added `qResolvent`, `stepDeltaResolvent`,
   `stepDeltaResolvent_eq_partition`, `unified_telescope_resolvent`
   (sorry-free); kept `stepDelta` with a docstring saying what it is.

## What the criterion did NOT settle, and is NOT closed

**Whether the gate belongs in the physics.** The criterion establishes the gate
is UNDERIVED and its stated justification FALSE — genuine complementary
slackness makes "tight" mean `tr = 0`, under which the functional collapses to
`(sum c_lambda) * f(0)` and reads nothing about the atom (`uicGated_cs_eq`),
and 0 of 10 active blocks sit at `tr = 0`. It does NOT establish the gate is
wrong: a rule can be right for a reason other than the one given (scope-(a) vs
scope-(b)). Dropping it would move every binding number by 3.4-4.6x on an
argument that only refutes a justification, so it ASKS. Not asked here, because
the honest statement — "the gate is what runs, and it is asserted" — is
available without taking the decision. Stays with `qou-sv7h` / `qou-brng`, both
OPEN.

## A precision finding, reported and NOT acted on

`q_laplacian_eigenvalue` accumulates `casimir_sum = 0.0` in float64
(`hecke_core_legacy.py:292`) and `S_REEB_PLANCK` is float64 (`:520`), so every
`C_lambda_resolvent_MeV` carries a float64-limited resolvent. Measured against
an mpf recomputation at `mp.dps = 70`, the worst relative gap over the ten
active blocks is **2.54432e-16** at `lambda = (2)`. That is the FLOOR of float64
arithmetic, so it bounds the damage at ~1e-16 and **cannot** distinguish
correctly-rounded from slightly-wrong — it is not evidence the path is harmless.
Fixing it moves every binding number in the corpus; out of scope for a
resolution PR. **This bean is completed for the RESOLUTION; the float64
resolvent is the one mechanical leftover** and belongs to whoever takes the
NO-FLOAT64 drain.

## Gates

`lean`-direct exit 0 on all three `.lean` (`-DautoImplicit=false -s 65536`),
`#print axioms` clean on all sixteen declarations, no `sorryAx`.
`precision-gates.sh --changed` exit 0 with ZERO hits on the new files (the
eleven contended audit witnesses reverted per `qou-v0t8`). `run-validate`
against pinned platform `df28d02`: Valid, 2 pre-existing issues in other blocks.
`qa-sweep --only render-math-mode-envelope`: 0 findings. Full render-QA grep
battery all-pass (one pre-existing markdown-list-hijack line found and fixed).
