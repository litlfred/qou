---
# qou-23dn
title: 'The bond decline is CHARGE-BEARING and the nn/pp ratio crosses 1: pure-neutron chain measured at A=2,3,4'
status: completed
type: task
priority: normal
created_at: 2026-08-31T04:36:07Z
updated_at: 2026-08-31T10:26:30Z
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


## RETRACTION 2026-08-31 — "pp saturates" is WRONG, and Lean proves why

`QOU.MassTheory.MarginalRatioExtensivity` (7 declarations, lean-direct exit 0,
0 sorry, 0 axiom beyond propext/Classical.choice/Quot.sound).

I wrote, in a merged PR body and in a probe, that a ratio sequence rising
monotonically toward 1 from below is *"the signature of a marginal bond
converging to a NONZERO limit — saturation rather than collapse."*

**That is false.** `ratio_rising_to_one_insufficient` exhibits the
counterexample: `r_k = (k+1)/(k+2)` is strictly increasing, lies strictly in
`(0,1)`, has `1 - r_k = 1/(k+2) -> 0`, and its partial products are **exactly
`1/(n+1)`** — which go to zero. Rising-to-1 is NECESSARY, not SUFFICIENT.

### And the corpus already had the answer

`docs/audits/2026-06-02-binding-intensive-vs-extensive-derivation.md`:
*"`B = E_0*Delta tr_M` is an **intensive** observable: `|tr_M|` is a bounded
trace, and its free-atom difference saturates"*. My `B_tot = E0*(S_off - S_on)`
IS that difference. `card_large_marginals_le` turns a bounded total into "at
most `M/eps` marginals can reach `eps`", so a nonzero limit is excluded
outright.

**Corrected picture: BOTH species collapse, at wildly different rates** — not
"pp saturates, nn collapses". pp merely collapses so slowly that four points
cannot see it, which is exactly what a `1 - r ~ c/k` tail looks like.

A corpus-grep on the *claim shape* ("is the total bounded?") rather than on the
topic would have caught this before the PR body went out.

### What survives

The **nn** half is now STRONGER, not weaker: a scope-(b) exclusion with a named
invariant. `prod_le_pow_of_le` — ratios uniformly `<= c` force partial products
`<= c^n`. The measured nn ratios are all `<= 0.387`, so the collapse is
geometric and unconditional.

### The measured gap sums

    pp   sum (1 - r_k) over measured terms = 0.3002   (tail unbounded -> OPEN)
    nn   sum (1 - r_k) over measured terms = 1.9318   (already > 1)
