---
# qou-oflu
title: 'DRAIN (inherited, blocks every PR''s 4b gate): raw-float64 NEW on cross-check-trM-1ppb.witness.json (tolerance_1ppQ_exact_methods, tolerance_peel_float_check); float64-padding on nastokes-multigen-cluster-additivity 835, threerow-qcross-trend 126, nastokes-orbit-symmetric-readout 98, alpha-k-jones-markov-h12 91, threerow-crossing-a-dependence 82. Fix at producer, never baseline'
status: completed
type: bug
priority: normal
created_at: 2026-08-10T02:46:37Z
updated_at: 2026-08-10T19:37:03Z
---

DRAIN (inherited, blocks every PR's §4b gate): the raw-float64 ratchet was red
on main and every open PR inherited it. Fix at the producer, never baseline.

## Closed — but mostly by other agents

The three NEW dirty witnesses measured on `e162c74c` were
`kappa-shell8-excess-convention` (25), `charm-composite-volume` (15) and
`charm-mass-tower` (10). Note this **corrects the list this bean was opened
with**: the float64-*padding* offenders it named (nastokes-multigen 835,
threerow-qcross 126, …) were already NEW 0, and `cross-check-trM-1ppb` was not
among the current offenders either.

`NEW dirty` is now **0**. Three agents converged on it within a few hours:

| witness | drained by |
|---|---|
| kappa-shell8 | main `7733a5ed` (six kappa witnesses at once) |
| charm-mass-tower | main `a4ffc29bf` |
| charm-composite-volume | main `a4ffc29bf` |

My own drains of all three were written and then superseded mid-rebase. That
overlap was not wasted: `a4ffc29bf` independently found the *same* defect I had
in charm-mass-tower — the truncated `q0 = 1.10998` — which is two agents
reaching one wrong literal from different directions.

## What the drains left behind — PR #4945

String-construction stops the float64; it does not make a rounded literal
accurate. Both surviving defects were hand-typed constants wrapped in `mpf`:

  kappa-shell8     `mp.mpf("0.51099895000")` — CODATA m_e truncated to 9 s.f.
                   → `codata_constants.M_E_MEV` = 0.51099895069
  charm-composite  `mpf("938.272")` → `M_P_MEV_VALIDATION`

Only m_e moves anything measurable: kappa −1.07042412344526659 →
−1.07042412489065622, **1.35e-9** relative. Attribution measured, not assumed —
f64 arithmetic vs mpf on the *same* inputs is 5.06e-16, so the arithmetic was
never the problem. This is the hidden-CODATA-literal class (`qou-46ke`) reached
from the float64 side.

## Two findings that outlive this bean

1. **A witness whose producer cannot reproduce it passed the ratchet.** At
   `eab6edc0` the kappa producer raised
   `TypeError: unsupported format string passed to mpf.__format__` before its
   `json.dump` — making the constants mpf broke `print(f"{k:.7f}")`. So the
   committed witness could not have been that script's output. Verified by
   running main verbatim, not inferred. A later commit fixed the crash. The
   general hole stands: **the ratchet reads witnesses and never runs
   producers**, so "drained" and "reproducible" are independent properties and
   only one of them is checked.

2. **A drain can move a number from one gate's red to the other's.** After
   `7733a5ed`, the float64-padding ratchet went NEW 0 → **35**, all in
   `kappa-coulomb-reconciliation` and `kappa-mirror-split-shell-test`. The
   values written are exact binary64 expansions padded to 50 decimals
   (`1.43996521992482051643946761032566428184509277343750…` for a number that
   is really `1.4399652199248205`). Raw-float64 green, padding red, same
   numbers. Belongs to that arc; recorded here so it is not lost.

## Still red, owned elsewhere

`a-K-via-lp-dual-full` 395 → 867 (raw-float64 REGRESSED 1), inherited from
`1086edca`. #4929 independently confirmed it is not a precision regression —
more LP rows solve — and draining it needs a breaking corpus-wide contract
change. `qou-ftuv` / #4929 carry it.
