This remark records the derivation behind the [$CO$ LP-dual binding proposition](#prop:co-lp-dual-binding): why the multiple bond decomposes into orthogonal channels, why a single-chain model fails, and how the active-set cardinality reproduces the bond order.

## Orthogonal channels, not one chain

A multiple bond is not one braid chain made "tighter" by stacking shared pairs into a common orbital. Each bond is an independent covalent channel — the reduced $4$-strand $[\mathfrak{p}_A,\, e_B,\, e_A,\, \mathfrak{p}_B]$ channel of [$H_2$](#prop:h2-lp-dual-binding) — sitting in its own orthogonal orbital ($\sigma$ head-on, $\pi_x, \pi_y$ lateral). Because distinct orbitals are orthogonal, electrons in different channels share no $e$–$e$ crossing. The channels bind independently and additively. The single $\sigma$ channel binds at ${{ qou.computations.co-bond-order-active-set.data.sigma_channel_eV | precision: 4 }}\;\text{eV}$ (the $H_2$-scale covalent channel).

## Failure of a single chain

Modelling the shared pairs as one interleaved $(2k{+}2)$-strand chain is computationally refuted. Only the first ($\sigma$) pair binds. The second and third pairs anti-bind because forcing every bonding electron into one orbital accumulates $e$–$e$ repulsion — the braid-model expression of orbital exclusion. The bond-selection LP on that single-chain model has an active set of cardinality $1$, not $3$ ([witness `co-bond-order-active-set`](../../../computations/co-bond-order-active-set.witness.json)). The triple bond requires the orthogonal decomposition. A "decreasing-but-positive marginal in one chain" does not occur.

## Bond order is occupied orthogonal channels

The bond-selection LP ranges over the orthogonal channels:

$$
  \max_{x} \; \sum_{i \in \{\sigma,\, \pi_x,\, \pi_y\}} b_i\, x_i
  \quad\text{s.t.}\quad
  \sum_i x_i \le V_{CO}, \quad 0 \le x_i \le 1,
$$

with each channel binding $b_i > 0$ and $V_{CO}$ the shared valence budget. Its active set (the occupied orthogonal channels) has cardinality equal to the bond order. This is the molecular instance of the bond order $=$ LP active-set cardinality identity.

For $CO$, the covalent budget is fixed by the octet valence of carbon ([carbon valence](#rem:carbon-valence)) and oxygen, derived ab initio below. An oxygen lone pair donated to carbon enters separately as a dative channel, not as a covalent LP term.

The orthogonal-channel LP $\max_x \sum_i b_i x_i$ subject to $\sum_i x_i \le \min(N_{\dim}, V)$ is computed for the diatomic series (witness `co-bond-order-active-set`), with the valence budget $V$ derived ab initio from the octet rule ($V_A = 10 - Z_A$ for second-row atoms: $\mathrm{C}=4$, $\mathrm{N}=3$, $\mathrm{O}=2$). The LP returns active-set cardinalities $(\mathrm{O_2}, \mathrm{N_2}, \mathrm{CO}) = (2, 3, 2)$. For $\mathrm{O_2}$ and $\mathrm{N_2}$ this equals the observed bond order. For $\mathrm{CO}$ the covalent active-set is $2$. The observed triple bond includes one dative bond (an oxygen lone pair donated to carbon). This makes $\mathrm{CO}$ isoelectronic with $\mathrm{N_2}$. The covalent count yields $2$, and the dative channel is a named addition. The ceiling is $N_{\dim} = 3$: physical space $\mathbb{R}^3$ admits at most three mutually-orthogonal directions (one axial $\sigma$, two transverse $\pi$). No $p$-block bond exceeds order three. The active set is capped by the spatial dimension.

Two limitations remain. (i) The covalent valence derives from $Z$ (octet rule), but $\mathrm{CO}$'s dative third bond is a named channel, not derived. (ii) The channels are modelled as equal independent copies, which overbinds the total energy ($3\,b_\sigma$ versus the observed $D_0$) pending a lateral-$\pi$ overlap reduction. The cardinality result holds; the energy is an upper bound.

The observed dissociation energy $D_0(CO) \approx {{ qou.computations.co-bond-order-active-set.data.observed_D0_CO_eV | precision: 4 }}\;\text{eV}$ is consistent with three occupied channels. $CO$ is isoelectronic with $\mathrm{N_2}$. Both carry three shared orthogonal channels with the same Hecke-algebra structure.
