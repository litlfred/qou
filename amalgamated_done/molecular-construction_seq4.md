<!-- FILE_START: co-computation-intro.md -->
Carbon monoxide is the first heteronuclear test of the template. Carbon monoxide $CO$ as a molecular braid joins the $(6,6)$ carbon braid to the $(8,8)$ oxygen braid with three shared electron pairs on a common strand set. The LP dual selects the triple bond as optimal for $CO$. It shows that the LP-optimal sharing pattern is the triple bond. We extract the $CO$ triple bond energy from the Wedderburn invariants. Heteronuclear bonding requires no new machinery, only the asymmetric strand counts of the two atomic factors.
<!-- FILE_END: co-computation-intro.md -->

<!-- FILE_START: co-molecular-braid.md -->
**Definition.**
**Carbon monoxide** *$CO$ is the molecular braid of a carbon atom $C(6, 6)$ and an oxygen atom $O(8, 8)$ sharing three electron pairs (triple bond).*

### Stage 1: Build the constituent atoms

*Carbon: $Z = 6$, $N = 6$, $A = 12$. The [atomic braid](#def:atomic-braid) $\mathcal{A}_C \in H_{18}(q)$ has 18 strands (12 nucleons + 6 electrons). Electron configuration $1s^2 2s^2 2p^2$: four valence electrons in the $n = 2$ shell.*

*Oxygen: $Z = 8$, $N = 8$, $A = 16$. The atomic braid $\mathcal{A}_O \in H_{24}(q)$ has 24 strands (16 nucleons + 8 electrons). Configuration $1s^2 2s^2 2p^4$: two open valence sites, two lone pairs.*

### Stage 2: Molecular assembly in $H_{42}(q)$

*The molecular braid lives in $H_{42}(q)$ ($18 + 24 = 42$ strands). The triple bond involves 3 shared electron pairs (6 electrons total participating in covalent bonding):*

- *1 $\sigma$ bond: one shared pair along the C--O axis*
- *2 $\pi$ bonds: two shared pairs perpendicular to the axis*

*In the braid framework:*
- *$\sigma$ bond: one electron from C and one from O occupy adjacent strand positions, each with two $\sigma^{-1}$ crossings (one to each nucleus)*
- *$\pi$ bonds: two additional shared pairs, each mediating between carbon's $2p$ shell and oxygen's $2p$ shell*

*After assembly:*
- *Carbon retains: 2 core electrons ($1s^2$) + 1 lone pair = 4 non-bonding electrons*
- *Oxygen retains: 2 core electrons ($1s^2$) + 1 lone pair = 4 non-bonding electrons*
- *Shared: 6 electrons (3 pairs) in covalent channels*

### Stage 3: Iterative construction

*The iterative constructor builds the molecular braid in steps:*

1. *Start with $\mathcal{A}_C$ (pre-computed, already in NF).*
2. *Embed $\mathcal{A}_O$ into the extended algebra.*
3. *Apply inter-atomic nucleon crossings (all identity except $\mathfrak{p}_C$--$\mathfrak{p}_O$ repulsion: 48 generator pairs).*
4. *Apply covalent bond operators: 3 shared pairs $\times$ 2 crossings each = 6 attractive $\sigma^{-1}$ crossings.*
5. *Gröbner--Shirshov reduce to normal form at each step.*

*The LP dual optimises the assignment of which 3 of carbon's 4 valence electrons are shared (and which 2 of oxygen's valence electrons are shared) by minimising $\Phi_1$ over all possible electron-bond assignments.*
<!-- FILE_END: co-molecular-braid.md -->

<!-- FILE_START: co-lp-dual-binding.md -->
**Proposition (conditional on [`conj:q-integer-mass-formula`](#conj:q-integer-mass-formula)).**
*For $CO$ the covalent-bond-selection LP selects an active set of cardinality $2$ — two **orthogonal orbital channels** $\sigma \perp \pi$, each an independent covalent channel rather than one accumulating chain of shared pairs. The observed triple bond is completed by a third, **dative** channel (an oxygen lone pair donated to carbon), giving total bond order $3$ and making $CO$ isoelectronic with $\mathrm{N_2}$.*

## Orthogonal channels, not one chain

A multiple bond is not one braid chain made "tighter" by stacking shared pairs into a common orbital. Each bond is an independent covalent channel — the reduced $4$-strand $[\mathfrak{p}_A,\, e_B,\, e_A,\, \mathfrak{p}_B]$ channel of [$H_2$](#prop:h2-lp-dual-binding) — sitting in its own orthogonal orbital ($\sigma$ head-on, $\pi_x, \pi_y$ lateral). Because distinct orbitals are orthogonal, electrons in different channels share no $e$–$e$ crossing. The channels bind independently and additively. The single $\sigma$ channel binds at $:val[sigma_channel_eV]{precision=4, witness=computations/co-bond-order-active-set.witness.json}$ (the $H_2$-scale covalent channel).

## Failure of a single chain

Modelling the shared pairs as one interleaved $(2k{+}2)$-strand chain is computationally refuted. Only the first ($\sigma$) pair binds. The second and third pairs anti-bind because forcing every bonding electron into one orbital accumulates $e$–$e$ repulsion — the braid-model expression of orbital exclusion. The bond-selection LP on that single-chain model has an active set of cardinality $1$, not $3$ ([witness `co-bond-order-active-set`](computations/co-bond-order-active-set.witness.json)). The triple bond requires the orthogonal decomposition. A "decreasing-but-positive marginal in one chain" does not occur.

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

The observed dissociation energy $D_0(CO) \approx :val[observed_D0_CO_eV]{precision=4, witness=computations/co-bond-order-active-set.witness.json}$ is consistent with three occupied channels. $CO$ is isoelectronic with $\mathrm{N_2}$. Both carry three shared orthogonal channels with the same Hecke-algebra structure.
<!-- FILE_END: co-lp-dual-binding.md -->

<!-- FILE_START: embeddable-knot-operator.md -->
**Definition.**
*An **embeddable knot operator** is a knot operator $K$ together with an embedding of its braid into the ambient $3$-manifold, carrying an **overlap weight** $w \in (0, 1]$ determined by the embedding direction relative to the bond axis. Its **binding contribution** is*

$$
  \mathfrak{E}(K) = \mathfrak{E}_0(K)\, w ,
$$

*where $\mathfrak{E}_0(K)$ is the un-embedded channel binding.*

### Axial vs transverse channels

*The embedding direction sorts operators into two classes by their angle to the bond axis:*

- ***Axial*** *($\sigma$-type): the braid runs along the bond axis. Head-on overlap is maximal, so $w = 1$.*
- ***Transverse*** *($\pi$-type): the braid lies in the plane transverse to the bond axis. Lateral overlap is smaller, so $w = w_\perp < 1$.*

*The weight $w_\perp$ is the transverse/axial overlap ratio, fixed per system.*

### Composite binding

*The binding of a composite is the overlap-weighted sum*

$$
  \mathfrak{E}\Bigl(\textstyle\bigcup_i K_i\Bigr) = \sum_i \mathfrak{E}_0(K_i)\, w_i .
$$

*An order-$k$ bond is one axial $\sigma$ channel and $k-1$ transverse $\pi$ channels, with total binding $\mathfrak{E}_0\,\bigl(1 + (k-1)\,w_\perp\bigr)$ (Lean: `multipleBond_binding`).*
<!-- FILE_END: embeddable-knot-operator.md -->

<!-- FILE_START: bond-order-le-three.md -->
**Proposition.**
*Each bond channel embeds as a direction in the ambient $3$-space, with distinct channels mutually orthogonal. Orthogonal nonzero vectors are linearly independent, so their number cannot exceed $\dim_{\mathbb{R}} \mathbb{R}^3 = 3$. At most three mutually-orthogonal channels embed — one axial $\sigma$ and two transverse $\pi$. The bond order is bounded by the spatial dimension. No $p$-block bond exceeds order three.*

This bound is formalised in Lean as `orthogonal_channels_le_dim` (pairwise-orthogonal nonzero vectors in a space of finrank $3$ number at most $3$).
<!-- FILE_END: bond-order-le-three.md -->

<!-- FILE_START: embeddable-cardinality-vs-energy.md -->
*Overlap weighting changes only the energy, never the channel count. Every channel with $w > 0$ is occupied, so the active-set cardinality (the bond order of [the CO LP dual](#prop:co-lp-dual-binding)) is independent of the weights (Lean: `multipleBond_length`). The equal-channel model ($w \equiv 1$) overbinds: for the $\sigma + 2\pi$ triple bond it gives $1.42\times$ the observed $D_0(\mathrm{N_2})$. A lateral weight $w_\perp \in [0.3, 0.7]$ brackets it (witness `embeddable-knot-operator`).*
<!-- FILE_END: embeddable-cardinality-vs-energy.md -->

<!-- FILE_START: co-triple-bond-energy.md -->
*The CO bond energy decomposes into three Wedderburn channels:*

$$
  \mathfrak{E}_{\mathrm{bind}}(CO) = \alpha \sum_{i \in \mathrm{bonds}}
  \ln\lvert \hat{V}_i^{\mathrm{full}} \rvert
$$

*where the sum runs over all 6 covalent-channel generators (3 bonds $\times$ 2 crossings each). The full traced volume includes symmetric, standard, and alternating representations:*

$$
  \hat{V}_i^{\mathrm{full}} =
  w_{\mathrm{sym}} \lambda_i^{\mathrm{sym}} +
  w_{\mathrm{std}} \hat{V}_i^{\mathrm{std}} +
  w_{\mathrm{alt}} \lambda_i^{\mathrm{alt}}
$$

*For the triple bond:*
- *$\sigma$ bond generators: eigenvalue products from the head-on overlap of $2s/2p_z$ orbitals.*
- *$\pi$ bond generators: eigenvalue products from lateral overlap of $2p_x$ and $2p_y$ orbitals.*
- *The $\sigma$ bond contributes the largest $|\hat{V}|$ (strong overlap). The $\pi$ bonds contribute smaller $|\hat{V}|$ (weaker lateral overlap).*

*The computation requires assembling the 42-strand transfer matrix chain. We perform this iteratively, reducing to NF at each step. The witness file `co-molecular-binding.witness.json` records:*
- *$\Phi_1$ for isolated C and O atoms.*
- *$\Phi_1$ for the CO molecular braid at each bond order $k = 1, 2, 3$.*
- *The LP dual shadow prices $y_1, y_2, y_3$.*
- *Comparison with observed $D_0 \approx :val[observed_D0_CO_eV]{precision=4, witness=computations/co-bond-order-active-set.witness.json} \;\mathrm{eV}$.*
<!-- FILE_END: co-triple-bond-energy.md -->
