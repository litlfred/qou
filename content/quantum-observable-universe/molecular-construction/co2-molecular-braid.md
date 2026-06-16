*Lean sibling: archimedean specialisation over $\mathbb{R}$ (CLAUDE.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Definition.**
*Carbon dioxide $CO_2$ is the molecular braid of one carbon atom
$C(6, 6)$ and two oxygen atoms $O_1(8, 8)$, $O_2(8, 8)$, with
two double bonds (O=C=O).*

### Stage 1: Constituent atoms

- *Carbon: $\mathcal{A}_C \in H_{18}(q)$, valence 4*
- *Oxygen 1: $\mathcal{A}_{O_1} \in H_{24}(q)$, valence 2*
- *Oxygen 2: $\mathcal{A}_{O_2} \in H_{24}(q)$, valence 2*

### Stage 2: Molecular assembly in $H_{66}(q)$

*Total strands: $18 + 24 + 24 = 66$.  The two double bonds
consume all 4 of carbon's valence electrons (2 per bond) and
all 2 valence electrons of each oxygen (2 per bond):*

- *C=O$_1$ bond (order 2): 1 $\sigma$ pair + 1 $\pi$ pair*
- *C=O$_2$ bond (order 2): 1 $\sigma$ pair + 1 $\pi$ pair*

*Carbon's 4 valence electrons are split equally: 2 shared with
$O_1$ and 2 shared with $O_2$.  No lone pairs on carbon.*

### Stage 3: Iterative construction

1. *Start with $\mathcal{A}_C$ in NF*
2. *Assemble $\mathcal{A}_{O_1}$: embed, apply inter-atomic
   crossings, apply 2 covalent bond operators (4 attractive
   $\sigma^{-1}$ crossings), reduce to NF*
3. *Assemble $\mathcal{A}_{O_2}$: embed, apply inter-atomic
   crossings (including $O_1$-$O_2$ interactions), apply 2
   covalent bond operators, reduce to NF*

*The key computational question: does the LP dual produce the
**linear** geometry O=C=O, or could a bent geometry be lower
in $\Phi_1$?*

*In the braid framework, linearity emerges when the optimal
strand ordering places $O_1$ and $O_2$ on opposite sides of $C$
— maximising the distance (number of intervening strands)
between the two oxygens' repulsive $\mathfrak{p}$-$\mathfrak{p}$
crossings.  The LP dual selects:*

$$
  [\ldots O_1 \ldots, \ldots C \ldots, \ldots O_2 \ldots]
$$

*with the interleaved covalent electrons mediating each C=O bond,
rather than:*

$$
  [\ldots C \ldots, \ldots O_1 \ldots, \ldots O_2 \ldots]
$$

*which would place the two oxygens adjacent (more repulsion).*

*The observed $CO_2$ structure is linear with $D_0 \approx
16.56 \;\mathrm{eV}$ (total of both C=O bonds, each
$\approx :val[d0_co2_double_ev]{precision=3, witness=computations/molecular-experimental-refs.witness.json} \;\mathrm{eV}$).*
