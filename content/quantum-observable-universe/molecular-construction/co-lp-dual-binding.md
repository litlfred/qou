**Proposition (conditional on [`conj:q-integer-mass-formula`](#conj:q-integer-mass-formula)).**
*For $CO$ the covalent-bond-selection LP selects an active set of cardinality $2$, corresponding to two orthogonal orbital channels $\sigma \perp \pi$. Each channel acts independently. A third dative channel (an oxygen lone pair donated to carbon) completes the observed triple bond, giving a total bond order of $3$ and making $CO$ isoelectronic with $\mathrm{N_2}$.*

A multiple bond consists of independent covalent channels rather than one stacked chain of shared pairs. Each channel forms a reduced $4$-strand $[\mathfrak{p}_A,\, e_B,\, e_A,\, \mathfrak{p}_B]$ braid in its own orthogonal orbital ($\sigma$ axial, $\pi_x, \pi_y$ transverse). Because distinct orbitals are orthogonal, electrons in different channels avoid $e$–$e$ crossings. The channels bind additively. The $\sigma$ channel binds at $:val[sigma_channel_eV]{precision=4, witness=computations/co-bond-order-active-set.witness.json}$.

Modelling the shared pairs as a single interleaved $(2k{+}2)$-strand chain yields an active set of cardinality $1$ ([witness `co-bond-order-active-set`](computations/co-bond-order-active-set.witness.json)). The subsequent pairs anti-bind due to accumulated $e$–$e$ repulsion. The triple bond requires the orthogonal decomposition.

The bond-selection LP ranges over the orthogonal channels:

$$
  \max_{x} \; \sum_{i \in \{\sigma,\, \pi_x,\, \pi_y\}} b_i\, x_i
  \quad\text{s.t.}\quad
  \sum_i x_i \le V_{CO}, \quad 0 \le x_i \le 1,
$$

where each channel binds $b_i > 0$ and $V_{CO}$ is the valence budget. The cardinality of the active set equals the bond order.

For $CO$, the covalent budget derives from the octet valence ($V_A = 10 - Z_A$). The LP ceiling $N_{\dim} = 3$ reflects the three spatial dimensions (one $\sigma$, two $\pi$), capping the $p$-block bond order at three. The LP computes active-set cardinalities $(\mathrm{O_2}, \mathrm{N_2}, \mathrm{CO}) = (2, 3, 2)$. The pure-covalent count for $\mathrm{CO}$ yields $2$. We include the dative channel as a separate addition to recover the total bond order of $3$. 

This model treats channels as equal independent copies, overestimating the total energy pending a lateral-$\pi$ overlap reduction. The observed dissociation energy $D_0(CO) \approx :val[observed_D0_CO_eV]{precision=4, witness=computations/co-bond-order-active-set.witness.json}$ is the strongest diatomic bond, consistent with three occupied channels. $\mathrm{CO}$ and $\mathrm{N_2}$ carry three shared orthogonal channels with identical Hecke-algebra structure.

