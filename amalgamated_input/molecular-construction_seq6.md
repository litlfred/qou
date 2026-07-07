<!-- FILE_START: ch4-computation-intro.md -->
Methane raises the coordination number from two to four. Methane $CH_4$ as a molecular braid (def) joins a central carbon to four hydrogens by four shared trefoils on the molecular strand set. The $S_4$-symmetric strand ordering minimises $\Phi_1$ for $CH_4$ (prop) shows that among all ways of arranging the four bond strands, the LP cost is minimised by configurations invariant under $S_4$, and tetrahedral geometry as $S_4$ symmetry of the LP dual (rem) reads this $S_4$ symmetry as the $109.5^\circ$ tetrahedral bond angle. The same $\Phi_1$ minimisation that produced linear $CO_2$ in §5 now selects the tetrahedral geometry of $CH_4$.

_(draft.)_
<!-- FILE_END: ch4-computation-intro.md -->

<!-- FILE_START: ch4-molecular-braid.md -->
**Definition.**
**Methane** *$CH_4$ is the molecular braid of one carbon atom
$C(6, 6)$ and four hydrogen atoms $H_1, H_2, H_3, H_4$,
each sharing one electron pair (four single bonds).*

### Stage 1: Constituent atoms

- *Carbon: $\mathcal{A}_C \in H_{18}(q)$, valence 4*
- *Hydrogen $H_k$: $\mathcal{A}_{H_k} \in H_2(q)$, valence 1,
 for $k = 1, 2, 3, 4$*

### Stage 2: Molecular assembly in $H_{26}(q)$

*Total strands: $18 + 4 \times 2 = 26$. Each of carbon's
4 valence electrons is shared with one hydrogen, forming 4
single C--H bonds. Each bond contributes 2 attractive
$\sigma^{-1}$ crossings.*

### Stage 3: Iterative construction

1. *Start with $\mathcal{A}_C$ in NF*
2. *Assemble $H_1$: embed in $H_{20}(q)$, apply inter-atomic
 crossings, apply 1 covalent bond operator (2 attractive
 crossings), reduce to NF*
3. *Assemble $H_2$: embed in $H_{22}(q)$, reduce to NF*
4. *Assemble $H_3$: embed in $H_{24}(q)$, reduce to NF*
5. *Assemble $H_4$: embed in $H_{26}(q)$, reduce to NF*

*The construction order ($H_1$ first, then $H_2$, etc.) should
not affect the final NF (confluence), but affects intermediate
complexity. The LP dual optimises the assembly ordering to
minimise intermediate word count.*
<!-- FILE_END: ch4-molecular-braid.md -->

<!-- FILE_START: ch4-tetrahedral-from-phi1.md -->
### Tetrahedral symmetry

*The LP dual selects a strand ordering with $S_4$ symmetry
(permuting the four hydrogens). In the optimal ordering, the
four H atoms are distributed **symmetrically** around carbon's
strands, maximising the inter-hydrogen distance (number of
intervening strands). This is the braid-theoretic origin of
the tetrahedral geometry of methane.*

*The $H$-$H$ interactions are:*
- *$\mathfrak{p}_{H_i}\mathfrak{p}_{H_j}$: EM repulsion ($\sigma$)*
- *$e_{H_i} e_{H_j}$: EM repulsion ($\sigma$)*
- *$\mathfrak{p}_{H_i} e_{H_j}$: EM attraction ($\sigma^{-1}$) —
 but this is a **non-bonding** attraction (no shared pair)*

*Minimising $\Phi_1$ over strand orderings accordingly distributes
the 4 H atoms to maximise separation of repulsive crossings,
producing the $S_4$-symmetric (tetrahedral) arrangement.*

*The observed C--H bond dissociation energy is
$D_0 \approx 4.48 \;\mathrm{eV}$ per bond (total
atomisation energy $\approx 17.9 \;\mathrm{eV}$).*
<!-- FILE_END: ch4-tetrahedral-from-phi1.md -->

<!-- FILE_START: ch4-lp-dual-binding.md -->
**Proposition (conditional on [`conj:q-integer-mass-formula`](#conj:q-integer-mass-formula)).**
*The LP dual of the $CH_4$ molecular braid in $H_{26}(q)$
selects the $S_4$-symmetric strand ordering as the ground state.
The four C--H bond energies are equal by symmetry.*

*The LP dual for $CH_4$ has the structure:*

$$
  \min_{\pi \in S_{26}} \; \Phi_1(\mathcal{M}(C, H_1, H_2, H_3, H_4; \pi))
$$

*The $S_4$ symmetry of the optimum means:*
1. *Each C--H bond has the same traced volume $\hat{V}_b$*
2. *Each H--H repulsion has the same $\Phi_1$ penalty*
3. *The total binding energy is exactly $4 \times \mathfrak{E}_{\mathrm{bind}}^{CH}$*

*The LP dual shadow prices:*
- *$y_{CH}$: marginal value of one C--H bond = single-bond
  dissociation energy*
- *$y_{HH}$: repulsion penalty per H--H pair (6 pairs total)*
- *$y_{\mathrm{sym}}$: symmetry premium — the $S_4$-symmetric
  arrangement is lower in $\Phi_1$ than any asymmetric alternative*

*The symmetry premium $y_{\mathrm{sym}} > 0$ is the
braid-theoretic origin of the **regular tetrahedron**:
breaking $S_4$ symmetry (e.g., compressing one H--C--H angle)
costs $\Phi_1$ through increased H--H repulsion.*
<!-- FILE_END: ch4-lp-dual-binding.md -->

<!-- FILE_START: ch4-tetrahedral-symmetry.md -->
*Methane's tetrahedral geometry ($109.5^\circ$ bond angles) is
a direct consequence of $\Phi_1$ minimisation.  In the
26-strand braid, the optimal ordering distributes the four
H atoms equidistant from each other in strand space, which
corresponds to the vertices of a regular tetrahedron in
physical space.*

*The computation establishes the mapping:*

| Braid quantity | Physical quantity |
|:-------------|:----------------|
| Strand separation between H atoms | H--C--H bond angle |
| $\Phi_1$ penalty per H--H pair | Steric repulsion energy |
| $S_4$ orbit of optimal ordering | Tetrahedral symmetry group $T_d$ |
| Breaking $S_4$ (asymmetric ordering) | Jahn--Teller distortion |

*For comparison, the same construction for $NH_3$ (nitrogen
+ 3 hydrogens) should give $C_{3v}$ symmetry with a lone pair
occupying the 4th tetrahedral site — producing the observed
pyramidal geometry with bond angles $\approx 107.8^\circ$.
The lone pair acts as a "phantom hydrogen" in the strand
ordering, occupying space but contributing no bonding
crossings.*

*This establishes the computational programme: every small
molecule's geometry is determined by the LP dual of its
molecular braid, with no geometric input required.*
<!-- FILE_END: ch4-tetrahedral-symmetry.md -->

