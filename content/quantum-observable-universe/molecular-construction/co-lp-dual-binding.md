**Proposition (conditional on [`conj:q-integer-mass-formula`](#conj:q-integer-mass-formula)).**
*For $CO$ the covalent-bond-selection LP selects an active set of
cardinality $2$ — two **orthogonal orbital channels** $\sigma \perp \pi$,
each an independent covalent channel rather than one accumulating chain of
shared pairs. The observed triple bond is completed by a third, **dative**
channel (an oxygen lone pair donated to carbon), giving total bond order
$3$ and making $CO$ isoelectronic with $\mathrm{N_2}$.*

## Orthogonal channels, not one chain

A multiple bond is **not** one braid chain made "tighter" by stacking
shared pairs into a common orbital.  Each bond is an independent covalent
channel — the reduced $4$-strand
$[\mathfrak{p}_A,\, e_B,\, e_A,\, \mathfrak{p}_B]$ channel of
[$H_2$](#prop:h2-lp-dual-binding) — sitting in its own **orthogonal
orbital** ($\sigma$ head-on, $\pi_x, \pi_y$ lateral).  Because distinct
orbitals are orthogonal, electrons in different channels share **no**
$e$–$e$ crossing, so the channels bind independently and additively.  The
single $\sigma$ channel binds at
$:val[sigma_channel_eV]{precision=4, witness=computations/co-bond-order-active-set.witness.json}$
(the $H_2$-scale covalent channel).

## Why a single chain fails (computational refutation)

Modelling the shared pairs as one interleaved $(2k{+}2)$-strand chain is
**refuted by computation**: only the first ($\sigma$) pair binds, while
the second and third pairs **anti-bind**, because forcing every bonding
electron into one orbital accumulates $e$–$e$ repulsion — the braid-model
expression of orbital exclusion.  The bond-selection LP on that
single-chain model has an active set of cardinality $1$, not $3$
([witness `co-bond-order-active-set`](computations/co-bond-order-active-set.witness.json)).
The triple bond therefore *requires* the orthogonal decomposition; a
"decreasing-but-positive marginal in one chain" does not occur.

## Bond order = occupied orthogonal channels

The bond-selection LP ranges over the orthogonal channels:

$$
  \max_{x} \; \sum_{i \in \{\sigma,\, \pi_x,\, \pi_y\}} b_i\, x_i
  \quad\text{s.t.}\quad
  \sum_i x_i \le V_{CO}, \quad 0 \le x_i \le 1,
$$

with each channel binding $b_i > 0$ and $V_{CO}$ the shared valence/site
budget.  Its **active set** — the occupied orthogonal channels — has
cardinality equal to the bond order.  This is the molecular instance of
the *bond order $=$ LP active-set cardinality* identity.

For $CO$ the covalent budget is fixed by the octet valence of carbon
([carbon valence](#rem:carbon-valence)) and oxygen, derived ab initio
below; an oxygen lone pair donated to carbon enters separately as a dative
channel, not as a covalent LP term.

The orthogonal-channel LP $\max_x \sum_i b_i x_i$ subject to
$\sum_i x_i \le \min(N_{\dim}, V)$ is **computed** for the diatomic
series (witness `co-bond-order-active-set`), with the valence budget $V$
**derived ab initio** from the octet rule ($V_A = 10 - Z_A$ for
second-row atoms: $\mathrm{C}=4$, $\mathrm{N}=3$, $\mathrm{O}=2$ — no
longer an input).  The LP returns active-set cardinalities
$(\mathrm{O_2}, \mathrm{N_2}, \mathrm{CO}) = (2, 3, 2)$.  For
$\mathrm{O_2}$ and $\mathrm{N_2}$ this **equals the observed bond order
with no input**.  For $\mathrm{CO}$ the covalent active-set is $2$; the
observed triple bond includes one **dative** bond (an oxygen lone pair
donated to carbon), which is precisely why $\mathrm{CO}$ is isoelectronic
with $\mathrm{N_2}$ — the pure-covalent count correctly yields $2$, and
the dative channel is a named addition, not a fitted $3$.  The
**non-circular** ceiling is $N_{\dim} = 3$: physical space
$\mathbb{R}^3$ admits at most three mutually-orthogonal directions (one
axial $\sigma$, two transverse $\pi$), so **no $p$-block bond exceeds
order three** — the active set is capped by the spatial dimension, not a
fitted parameter.

*Two honest limitations remain.* (i) The covalent valence is now derived
from $Z$ (octet rule), but $\mathrm{CO}$'s dative third bond is not yet
derived — it is added as a named channel. (ii) The channels are modelled
as equal independent copies, which overbinds the total energy
($3\,b_\sigma$ versus the observed $D_0$) pending a lateral-$\pi$ overlap
reduction: the **cardinality** result is robust, the **energy** is not.

The observed dissociation energy
$D_0(CO) \approx :val[observed_D0_CO_eV]{precision=4, witness=computations/co-bond-order-active-set.witness.json}$
is the strongest diatomic bond, consistent with three occupied channels.
$CO$ is isoelectronic with $\mathrm{N_2}$: both carry three shared
orthogonal channels with the same Hecke-algebra structure in their
covalent channels.
