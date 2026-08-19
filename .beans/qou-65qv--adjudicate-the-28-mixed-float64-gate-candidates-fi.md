---
# qou-65qv
title: Adjudicate the 28 mixed-float64 gate candidates; fix true positives; flip to blocking
status: in-progress
type: task
priority: normal
created_at: 2026-08-19T11:51:09Z
updated_at: 2026-08-19T12:21:17Z
---

## 2026-08-19 — 28 -> 16, PR #5292

**Two producers fixed at source, both with measured A/B:**
- `qbeta_hoefsmit_chi_cross_anchor_stability_probe` — a 49-digit bare FLOAT
  literal for Q_PROTON (17 good digits presented as 25); `delta_q` wrong from
  the 9th significant digit via cancellation.
- `rho_k_full_via_wenzl_lr` — discarded its own declared 50-dps q0 three lines
  later. `tr_M_q0_mp30dps` carried 9-15 good digits depending on atom, worse
  than the float64 floor because the symbolic chi AMPLIFIES the q0 error.
  Required building hecke-tr-m-wenzl-lr (48s); without it the consumer is inert
  and the fix was unverifiable (first run: 0/4 atoms).

**Three DETECTOR false-positive classes fixed** (the tool's fault, not the
corpus's): int()/round() clear taint; a format-spec sink is display; bare
.trace()/.sum() no longer imply numpy (sympy Matrix carries them too).

**Six rows marked float64-intentional** — timings, the representability test in
_shortest_repr, an exact quarter-integer exponent.

**One row BLOCKED and deliberately not landed:**
`qbeta_habiro_taylor_investigation`. The float() fix is right, but re-running
the producer regenerates its witness convention C -> D. That belongs to
qou-cds1 (three active arcs), not to a float64 drain.

**Gate stays ADVISORY.** Flipping to blocking needs the residual 16 verdicted,
and one of them is not mine to verdict.
