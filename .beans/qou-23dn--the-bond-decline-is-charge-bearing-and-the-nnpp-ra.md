---
# qou-23dn
title: 'The bond decline is CHARGE-BEARING and the nn/pp ratio crosses 1: pure-neutron chain measured at A=2,3,4'
status: completed
type: task
priority: normal
created_at: 2026-08-31T04:36:07Z
updated_at: 2026-08-31T04:36:33Z
---

## Measured 2026-08-31 — `computations/probes/bond_marginal_and_neutron_chain_probe.py` (6/6)

Follow-on to `qou-gcmn` (answered, #6336). Two things that probe left open.

### 1. The AVERAGE understated the decline; the MARGINAL is what moves

`B_tot(A)/(A-1)` is a running mean. The marginal bond `dB(A) = B_tot(A) - B_tot(A-1)`
is what an assembly model needs, and it moves much faster:

    chain   A   avg/bond    marginal   marg vs A=2
       pp   2   2.128361    2.128361      1.000
       pp   3   1.966343    1.804324      0.848
       pp   4   1.851586    1.622072      0.762
       nn   2   2.435585    2.435585      1.000
       nn   3   1.688377    0.941169      0.386
       nn   4   1.240832    0.345741      0.142

pp: average drops 13.0 %, marginal drops **23.79 %** by A=4.
nn: average drops 49.05 %, marginal drops **85.8 %**.

The 13.0 % figure reported in #6336 is correct as an average and understates
the underlying quantity by ~1.8x.

### 2. The decline is CHARGE-BEARING — the cheap explanation is excluded

`atom_canonical_crossings(A,0)` vs `(0,A)`: same 23/35/47 crossings, same A-1
bonds toggled by `include_inter`, **identical** `averaged` counts, and the whole
difference is a one-for-one `sigma <-> sigma_inv` trade (the p->sigma,
n->sigma_inv identification, measured rather than assumed).

    max |pp_rel - nn_rel| = 0.3605   against a 0.01 "same profile" threshold

So the decline is NOT a normalisation artifact of tracing longer chains. Same
trace, same strand count, same bond count, and the species move apart by a
third of their own scale.

### 3. The nn/pp ratio CROSSES 1 inside the measured range

    nn/pp = 1.1443 at A=2,  0.6701 at A=4

The nn bond starts stronger and ends weaker. **A single multiplicative charge
factor cannot change side of 1**, so whatever separates the species is itself
A-dependent. Observed, not extrapolated.

### Scope (a)

Pure single-species chains are not nuclei; no pn bond and no mixed chain is
measured. `B_nn` has no committed twin so its absolute value is unanchored --
only the pp leg is validated (reproduces `B_pp_strong_MeV` exactly at A=2).
Three points; no asymptotic law claimed and no extrapolation to the A=39 end of
the mirror series. Whether the nn marginal changes SIGN is not determined.
