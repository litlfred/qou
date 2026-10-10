---
# qou-65qv
title: Adjudicate the 28 mixed-float64 gate candidates; fix true positives; flip to blocking
status: completed
type: task
priority: normal
created_at: 2026-08-19T11:51:09Z
updated_at: 2026-08-19T13:23:51Z
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


## COMPLETED 2026-08-19 — merged 2c5776834a (PR #5292)

28 -> 3, gate flipped to BLOCKING at baseline 3. Verified on main: gate is
blocking, baseline reads 3, all producer fixes present.

Eight producers fixed at source. Best two: a 49-digit bare FLOAT literal in
the cross-anchor PRECISION-STABILITY probe (delta_q wrong from the 9th
significant digit via cancellation), and rho_k discarding its own declared
50-dps q0 three lines later (tr_M_q0_mp30dps carrying as few as NINE good
digits -- worse than the float64 floor, because the symbolic chi amplifies
the q0 error).

Two PRE-EXISTING bugs fixed because the work was otherwise unverifiable:
proton_residual_rootcause crashed on main (mpf.__format__), and
PhiQ_euler_mpfr returns mpc for an mpf argument (Im == 0.0 exactly).

Four DETECTOR false-positive classes fixed before spending verdicts on real
rows. Sharpest: mpf(str(<=17-digit literal)) round-trips exactly, which is
also precisely why Q_PROTON's 49 digits do NOT -- same syntax, opposite
verdict, decided by digit count.

Nine rows marked float64-intentional with reasons. Three BLOCKED on qou-cds1
(re-running qbeta_habiro_taylor regenerates its witness convention C -> D).

INHERITED RED left standing, not silenced: raw-float64 ratchet fails on
gswz_epsm_m3_one_two_relation_closure.witness.json, byte-identical to main's
copy and absent from a baseline identical to main's -- main is red on that
gate. Belongs to the gswz-epsm arc.
