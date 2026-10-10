---
# qou-0xe1
title: 'GAP: qbeta_5two_chirality_state_integral hangs in z_state_integral at G1 (pre-dates the qou-9ugp re-pin)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T00:26:33Z
updated_at: 2026-10-10T08:30:00Z
parent: qou-avtq
---

MEASURED 2026-09-04 (bean qou-9ugp, probes/ tranche).

`computations/probes/qbeta_5two_chirality_state_integral_probe.py` does not
complete. It prints its banner and the `[G1]` header, then blocks forever at
line 114:

    quad41 = z_state_integral(mp.mpf(1), 2, 1)

killed by its own 3000 s timeout with no traceback and no witness written.

THIS PRE-DATES THE RE-PIN, and that is measured rather than assumed. The
unmodified HEAD producer, run in the same container, hangs at the IDENTICAL
line and produces a BYTE-IDENTICAL 283-byte log (exit 124 at a 240 s cap).
So the q0 re-pin landed on this branch is not what broke it, and reverting the
re-pin would not fix it.

Consequence for the tranche: the `.py` re-pin is committed (it is correct and
needed -- both legs were literals, the muon one the retired pin A), and
`qbeta-5two-chirality-state-integral.witness.json` is deliberately LEFT AT
HEAD. Its committed payload is whatever the last successful run produced, at
an unknown date, and this container cannot reproduce it.

What to look at: `z_state_integral(b=1, n=2, k=1)` -- the 4_1 quadrature that
G1 checks against the Garoufalidis-Kashaev closed form. Either the integrand
has acquired a non-convergent branch or mpmath's `quad` is not terminating on
its contour. Note the probe's own comparison target `exact41` is computed in
closed form and returns instantly, so the defect is confined to the quadrature.

Not a q0 question. Filed separately so the anchor drain is not blocked on it.


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: OPEN.** Still reproduces on main 2026-10-10: G1 does not finish within 300 s (see verdict6.md for the long run). qou-he82 recorded a full 1424 s pass on 2026-08-10, so the likely cause is a slowdown (mpmath 1.3→1.4.1, or `set_compute_dps` raising the working precision), not a mathematical non-convergence. The committed witness cannot be reproduced and records no q0Anchor, so nothing should cite it until G1 runs again.

Evidence: `computations/probes/qbeta_5two_chirality_state_integral_probe.py`: `timeout 300 python3 …` → exit 124, stuck after `[G1] 4₁ quadrature at b=1 …` (line 114, `z_state_integral(mp.mpf(1),2,1)`). See the long-run row under "Probes re-run" for the 2700 s attempt. Contradicting record: `qou-he82` (2026-08-10) says the same probe ran 5/5 PASS in 1424 s (G1 rel err 1.097e-19). Committed witness `qbeta-5two-chirality-state-integral.witness.json`: `computedAt 2026-07-18`, `durationMs 44`, `allPassed true`, mpmath 1.3.0, `compute_dps 70`, **no `q0Anchor`** (listed in `computations/q0-anchor-missing-baseline.json`). The container now has mpmath 1.4.1.

Status: `todo` → `todo` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.
