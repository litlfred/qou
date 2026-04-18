**Definition.**
*Water $\mathrm{H}_2\mathrm{O}$ is the molecular braid of two
hydrogen atoms $H_1(1,0)$, $H_2(1,0)$ and one oxygen atom
$O(8,8)$ sharing two electron pairs, with two lone pairs retained
on the oxygen vertex.*

### Stage 1: Constituent atoms

- *Hydrogen: $Z = 1$, $N = 0$, $A = 1$.  Each
  [atomic braid](#def:atomic-braid) $\mathcal{A}_{H_i} \in H_2(q)$
  has 2 strands (1 proton + 1 electron).  Configuration $1s^1$:
  one valence electron, one open linking site.*
- *Oxygen: $Z = 8$, $N = 8$, $A = 16$.  $\mathcal{A}_O \in H_{24}(q)$
  has 24 strands (8 protons + 8 neutrons + 8 electrons).
  Configuration $1s^2 2s^2 2p^4$: two open valence sites and two
  lone pairs in the $n = 2$ shell.*

### Stage 2: Molecular assembly in $H_{28}(q)$

*Total strands: $2 + 2 + 24 = 28$.  Each O–H bond is a single
shared pair; the two remaining $2p$ electron pairs on O do not
participate in bonding:*

- *O–$H_1$ bond: 1 $\sigma$ pair (1 shared electron from $H_1$
  and 1 from O)*
- *O–$H_2$ bond: 1 $\sigma$ pair (1 shared electron from $H_2$
  and 1 from O)*
- *O lone pairs: 2 pairs in the $2s$ / $2p_z$ channels — each
  pair is a trefoil loop on the oxygen vertex that participates
  in neither covalent bond*

*After assembly:*
- *Each hydrogen retains: 0 core electrons, 0 lone electrons;
  both $H$ electrons are shared*
- *Oxygen retains: 2 core electrons ($1s^2$) + 4 lone-pair
  electrons (2 pairs) = 6 non-bonding electrons*
- *Shared: 4 electrons (2 pairs) in the two O–H covalent
  channels*

### Stage 3: Iterative construction

*The iterative constructor builds the braid in three steps:*

1. *Start with $\mathcal{A}_O$ (pre-computed, in NF).*
2. *Embed $\mathcal{A}_{H_1}$ into the extended algebra.  Apply
   inter-atomic nucleon crossings ($\mathfrak{p}_O$–$\mathfrak{p}_{H_1}$
   and $\mathfrak{n}_O$–$\mathfrak{p}_{H_1}$, all identity except
   O-proton–H-proton repulsion).  Apply the single O–$H_1$
   covalent bond operator: 1 shared pair $\times$ 2 crossings =
   2 attractive $\sigma^{-1}$ crossings.  Reduce to NF.*
3. *Embed $\mathcal{A}_{H_2}$.  Apply inter-atomic crossings
   (including $H_1$–$H_2$ repulsion, which is non-trivial because
   both protons now reside on $O$).  Apply the O–$H_2$ covalent
   bond operator (2 more attractive $\sigma^{-1}$ crossings).
   Reduce to NF.*

*The LP dual determines (a) which two of oxygen's four $2p$
valence electrons are placed in bonding channels (and which two
stay as a lone pair), and (b) the strand ordering that places
$H_1$ and $H_2$ on different sides of the oxygen vertex rather
than adjacent to each other — see
[H₂O bent geometry](#rem:h2o-bent-geometry).*
