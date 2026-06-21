*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Definition.**
*Carbon monoxide $CO$ is the molecular braid of a carbon atom
$C(6, 6)$ and an oxygen atom $O(8, 8)$ sharing three electron
pairs (triple bond).*

### Stage 1: Build the constituent atoms

*Carbon: $Z = 6$, $N = 6$, $A = 12$.  The
[atomic braid](#def:atomic-braid) $\mathcal{A}_C \in H_{18}(q)$
has 18 strands (12 nucleons + 6 electrons).  Electron
configuration $1s^2 2s^2 2p^2$: four valence electrons in the
$n = 2$ shell.*

*Oxygen: $Z = 8$, $N = 8$, $A = 16$.  The atomic braid
$\mathcal{A}_O \in H_{24}(q)$ has 24 strands (16 nucleons +
8 electrons).  Configuration $1s^2 2s^2 2p^4$: two open valence
sites, two lone pairs.*

### Stage 2: Molecular assembly in $H_{42}(q)$

*The molecular braid lives in $H_{42}(q)$ ($18 + 24 = 42$ strands).
The triple bond involves 3 shared electron pairs — 6 electrons
total participating in covalent bonding:*

- *1 $\sigma$ bond: one shared pair along the C--O axis*
- *2 $\pi$ bonds: two shared pairs perpendicular to the axis*

*In the braid framework:*
- *$\sigma$ bond: one electron from C and one from O occupy
  adjacent strand positions, each with two $\sigma^{-1}$
  crossings (one to each nucleus)*
- *$\pi$ bonds: two additional shared pairs, each mediating
  between carbon's $2p$ shell and oxygen's $2p$ shell*

*After assembly:*
- *Carbon retains: 2 core electrons ($1s^2$) + 1 lone pair = 4
  non-bonding electrons*
- *Oxygen retains: 2 core electrons ($1s^2$) + 1 lone pair = 4
  non-bonding electrons*
- *Shared: 6 electrons (3 pairs) in covalent channels*

### Stage 3: Iterative construction

*The iterative constructor builds the molecular braid in steps:*

1. *Start with $\mathcal{A}_C$ (pre-computed, already in NF)*
2. *Embed $\mathcal{A}_O$ into the extended algebra*
3. *Apply inter-atomic nucleon crossings (all identity except
   $\mathfrak{p}_C$--$\mathfrak{p}_O$ repulsion: 48 generator pairs)*
4. *Apply covalent bond operators: 3 shared pairs $\times$ 2
   crossings each = 6 attractive $\sigma^{-1}$ crossings*
5. *Gröbner--Shirshov reduce to normal form at each step*

*The LP dual optimises the assignment of which 3 of carbon's
4 valence electrons are shared (and which 2 of oxygen's valence
electrons are shared) by minimising $\Phi_1$ over all possible
electron-bond assignments.*
