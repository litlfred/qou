<!-- FILE_START: co2-computation-intro.md -->
With heteronuclear bonding in place we add a third atom. Carbon dioxide $CO_2$ as a molecular braid (def) couples a central carbon to two oxygens, each via a shared electron pair on the molecular Hecke strands. The LP dual selects linear $O{=}C{=}O$ geometry (prop) shows that the optimum places the two $C{=}O$ trefoils on opposite sides of the central strand, and VSEPR molecular geometry from $\Phi_1$ minimisation (rem) reads this configuration as the braid-theoretic origin of the VSEPR rule. The linear triatomic case isolates molecular geometry as a consequence of $\Phi_1$ minimisation, independent of bond order.

_(draft.)_
<!-- FILE_END: co2-computation-intro.md -->

<!-- FILE_START: co2-molecular-braid.md -->
**Definition.**
**Carbon dioxide** *$CO_2$ is the molecular braid of one carbon atom
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
<!-- FILE_END: co2-molecular-braid.md -->

<!-- FILE_START: co2-linear-geometry-and-d0.md -->
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
<!-- FILE_END: co2-linear-geometry-and-d0.md -->

<!-- FILE_START: co2-lp-dual-binding.md -->
**Proposition (conditional on [`conj:q-integer-mass-formula`](#conj:q-integer-mass-formula)).**
*The LP dual of the $CO_2$ molecular braid selects the symmetric
linear arrangement O=C=O with two double bonds as the ground
state, minimising $\Phi_1$ over all possible:*

1. *Bond order assignments: $(k_1, k_2)$ with $k_1 + k_2 \leq 4$
   (carbon's valence)*
2. *Electron-bond assignments: which electrons are shared with
   which oxygen*
3. *Strand orderings: permutations of 66 strands*

*The LP dual has three shadow prices:*

- *$y_{\sigma}$: value of each $\sigma$-bond shared pair*
- *$y_{\pi}$: value of each $\pi$-bond shared pair*
- *$y_{\mathrm{sym}}$: value of symmetric bond placement
  (equal bonds to both oxygens)*

*The symmetric double-bond configuration $(k_1, k_2) = (2, 2)$
wins over asymmetric alternatives $(3, 1)$ or $(1, 3)$ because:*

- *Each double bond contributes 4 attractive crossings*
- *The symmetric arrangement minimises $O_1$-$O_2$
  repulsion (protons are maximally separated)*
- *The asymmetric $(3, 1)$ configuration wastes one of
  oxygen's valence sites and places more electron density
  on one side, increasing $e$-$e$ repulsion*
<!-- FILE_END: co2-lp-dual-binding.md -->

<!-- FILE_START: co2-vsepr-and-per-bond-energy.md -->
*This is the braid-theoretic origin of **VSEPR geometry**:
electron-pair repulsion minimisation is literally $\Phi_1$
minimisation over strand orderings, and the LP dual formalises
the repulsion-minimisation principle as a linear program.*

*The binding energy per C=O bond should be compared with:*
- *$CO$ triple bond: $\approx :val[observed_D0_CO_eV]{precision=4, witness=computations/co-bond-order-active-set.witness.json} \;\mathrm{eV}$ (3 bonds)*
- *$CO_2$ double bond: $\approx :val[d0_co2_double_ev]{precision=3, witness=computations/molecular-experimental-refs.witness.json} \;\mathrm{eV}$ (2 bonds)*
- *The per-bond energy decreases with bond order as expected:
  $11.09/3 \approx 3.70$ vs $8.28/2 \approx 4.14 \;\mathrm{eV}$
  per shared pair.*
<!-- FILE_END: co2-vsepr-and-per-bond-energy.md -->

<!-- FILE_START: co2-double-bond-symmetry.md -->
*The LP dual for $CO_2$ provides a categorical derivation of
VSEPR (Valence Shell Electron Pair Repulsion) theory.  The key
correspondence is:*

| VSEPR concept | Braid framework |
|:-------------|:---------------|
| Electron pair repulsion | $ee$ crossing ($\sigma$, $q$-eigenvalue) increases $\Phi_1$ |
| Bond pair vs lone pair | Shared trefoil (2 attractive crossings) vs retained trefoil (1 attractive crossing) |
| Geometric arrangement | Strand ordering in $H_{N}(q)$ |
| Energy minimisation | $\Phi_1$ minimisation via LP dual |

*For $CO_2$:*
- *2 bond pairs (double bonds), 0 lone pairs on C*
- *VSEPR predicts: linear, 180$^\circ$ bond angle*
- *LP dual confirms: placing $O_1$ and $O_2$ on opposite sides
  of $C$ in the strand ordering minimises the $O$-$O$
  proton repulsion crossings*

*For $H_2O$ (future computation):*
- *2 bond pairs (single bonds), 2 lone pairs on O*
- *VSEPR predicts: bent, $\approx 104.5^\circ$*
- *LP dual should show: lone pairs force the two H's into
  a non-symmetric strand arrangement*

*The braid framework is more fundamental than VSEPR because it
derives geometric preferences from the Hecke algebra structure
rather than postulating repulsion rules.  Bond angles emerge as
properties of the optimal strand ordering, not input parameters.*
<!-- FILE_END: co2-double-bond-symmetry.md -->

