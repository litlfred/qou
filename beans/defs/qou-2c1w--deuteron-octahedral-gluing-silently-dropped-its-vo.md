---
# qou-2c1w
title: deuteron_octahedral_gluing silently dropped its Vol=0 assertion when snappy is absent, keeping allPassed=True
status: completed
type: task
priority: normal
created_at: 2026-09-04T03:21:41Z
updated_at: 2026-09-04T03:22:26Z
---

## Fixed 2026-09-04 in `deuteron_octahedral_gluing_probe.py` (guard added)

Found by re-running the producer during the q0-label drain (bean qou-9ugp).

    HEAD  allPassed=True  n=3
          True  reciprocal_pairing_exact
          True  meridian_map_verified
          True  deuteron_is_torus_knot_vol_zero      <-- gone below
    NOW   allPassed=True  n=2
          True  reciprocal_pairing_exact
          True  meridian_map_verified

The producer wrapped the third assertion in `if have_snappy:` with no `else`.
snappy is absent by default in a fresh container, so a re-run emitted a
two-assertion witness -- and `allPassed` stayed **True**, so a consumer reading
that field could not tell a check had gone missing.

The check that vanishes is the one that matters: `deuteron_is_torus_knot_vol_zero`
is the `Vol = 0` verification underpinning **owner ruling A (2026-08-29)** --
"the deuteron knot is the canonical braid closure (trefoil / Hopf, Vol = 0); the
deuteron binding is NOT a hyperbolic-volume term". A snappy-less re-run by any
later agent would have quietly removed the evidence for a standing ruling while
reporting success.

**Fix**: the `else` branch now REFUSES -- prints why on stdout (a stderr-only
harness would not see it) and returns 2, writing nothing. Following
`low_isotope_mass_table` and `qbeta_braid_nf_sdp_offset_probe`, which refuse
by design for the same reason. Verified: exit 2, no witness written, the
committed witness restored untouched from HEAD.

**Consequence for this branch**: the q0_convention label refresh for
`deuteron-octahedral-gluing.witness.json` is BLOCKED on snappy in this
container. The producer source is already correct (it says "experimental/proton
pin, read by name from q_parameter.Q_50_DIGIT_STR"); only its committed witness
still carries the stale `muon-canonical` string. `pip install snappy` and re-run
clears it. Shipping the degraded witness to fix a label would have been the
worse trade.

**Generalisable**: `allPassed` is computed over the assertions PRESENT, so it
cannot detect an assertion that was never added. An assertion behind an
`if <dependency>:` with no `else` is invisible to it by construction. Worth a
sweep for the same shape elsewhere -- not done here.
