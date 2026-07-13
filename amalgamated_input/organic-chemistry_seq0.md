<!-- FILE_START: covalent-bonding-intro.md -->
Where metallic bonding shares residual sub-links across an entire lattice, molecular chemistry localises the sharing between two atoms. We make this precise as a **covalent bond** of order $k$: a shared sub-Hopf link of $k$ trefoils simultaneously linked to one open site in each partner. We read off single, double, and triple bonds as $k = 1, 2, 3$. Each increment in bond order adds one shared trefoil, so higher bond order registers as additional rigidity. The explicit crossing-energy formula is stated in the covalent-bond definition.

We close the section by partitioning carbon's electron cloud into a closed $1s^2$ pair and a residual sub-link of size four. This four-site residual link is exactly half-filling of the second shell's capacity. This places carbon at the maximally covalent midpoint of the metallic-character spectrum.
<!-- FILE_END: covalent-bonding-intro.md -->

<!-- FILE_START: covalent-bond-types.md -->
**Definition.**
Let $\mathcal{A}_1$ and $\mathcal{A}_2$ be atoms with residual sub-links $R_1$ and $R_2$. A **covalent bond** of order $k$ is a shared sub-Hopf link

$$
  B_k(R_1, R_2)
  = 
  \underbrace{T_{2,3} \oplus \cdots \oplus T_{2,3}}_{k \text{ shared trefoils}}
$$

where each shared trefoil is simultaneously Hopf-linked to one open site in $R_1$ and one open site in $R_2$. The integer $k$ is the **bond order**:

| Bond order $k$ | Chemical name | Shared trefoils | Linking sites consumed |
|:-:|---|:-:|:-:|
| 1 | Single bond | 1 | 1 per atom |
| 2 | Double bond | 2 | 2 per atom |
| 3 | Triple bond | 3 | 3 per atom |

The crossing energy of the bond is

$$
  E_{\mathrm{bond}}(k)
  = 
  k \cdot \mathfrak{E}_{\mathrm{cross}}(T(2,2))
  + 
  \binom{k}{2}  \Delta E_{\mathrm{inter}},
$$

where $T(2,2)$ is the Hopf link. The first term accounts for $k$ individual Hopf links, and the second for inter-link interactions within the shared sub-link. Higher bond order increases both binding strength and rigidity: a triple bond is stronger and stiffer than a single bond because the three shared trefoils form a closed sub-link that resists Reidemeister moves.
<!-- FILE_END: covalent-bond-types.md -->

<!-- FILE_START: carbon-valence.md -->
Carbon ($p = 6$) has electron cloud $6 \cdot T_{2,3}$ partitioned as

$$
  \mathcal{E}_{\mathrm{C}}
  = 
  \underbrace{T_{2,3} \oplus T_{2,3}}_{\text{closed } 1s^2}
   \oplus 
  \underbrace{T_{2,3} \oplus T_{2,3} \oplus T_{2,3} \oplus T_{2,3}}_{\text{residual } R,  |R| = 4}.
$$

The second shell has capacity $2 \cdot 2^2 = 8$, so the residual sub-link $R$ occupies exactly half the available linking sites: $|R| / 2n^2 = 4/8 = 1/2$.

This **half-filling** makes carbon unique among the light elements:

1. **Maximal bonding capacity**: 4 open linking sites. More than any other period-2 element.
2. **Symmetric energy landscape**: adding a trefoil and removing a trefoil cost comparable crossing energy. Carbon shares electrons via covalent bonds.
3. **Chain-forming ability**: with 4 sites, carbon can bond to two neighbours while retaining 2 sites for branching. This is the topological origin of organic chemistry's combinatorial richness.

The residual linking number $\lambda(R) = 4$ places carbon in the middle of the metallic character spectrum. It is neither metallic nor inert, but maximally covalent.
<!-- FILE_END: carbon-valence.md -->

