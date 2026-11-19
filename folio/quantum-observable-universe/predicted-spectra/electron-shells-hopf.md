The electron configuration of atoms follows from the **closed sub-Hopf link structure** of the multi-electron trefoil chain, yielding the shell capacities $2, 8, 18, 32, \ldots = 2n^2$.

**The electron link.**

A neutral atom with $Z$ protons binds $Z$ electrons. Each electron forms a trefoil $T_{2,3}$. The stable atom takes the form:

$$
  \mathcal{A}(p, n)
  = 
  \underbrace{Z\mathfrak{p} \oplus N\mathfrak{n}}_{\text{nucleus}}
   \oplus 
  \underbrace{p \cdot T_{2,3}}_{\text{electron cloud}}.
$$

The electron cloud $p \cdot T_{2,3}$ forms a chain of $p$ trefoils bound by Hopf links. An **electron shell** defines a maximal closed sub-Hopf link of this chain. It forms a subset $S$ of trefoils such that $\bigbowtie_{i \in S} T_{2,3}$ splits from the remaining chain.

**First example: helium ($p = 2$, $n = 2$).**

The helium electron cloud $T_{2,3} \oplus T_{2,3}$ forms a Hopf link of two trefoils. This pair acts as a **closed sub-link**. It rejects a third trefoil unless the linking number increases. The two electrons fill the $1s$ shell.

Topological closure makes helium a noble gas. A third electron (lithium) forces a new sub-link. This weakly couples to the first to form the $2s$ shell.

**Shell capacities from sub-link closure.**

Conjecturally, the maximum number of trefoils in a closed sub-Hopf link at level $n$ fixes the shell capacity at $2n^2$, though a link-theoretic proof of that capacity bound is unestablished:

| Shell $n$ | Capacity $2n^2$ | Cumulative | Pure-$2n^2$ closure | Closed sub-link |
|----------:|----------------:|-----------:|---------------------|----------------|
| 1 | 2 | 2 | He (= noble) | $T_{2,3} \oplus T_{2,3}$ |
| 2 | 8 | 10 | Ne (= noble) | $8 \cdot T_{2,3}$ (Hopf $8$-chain) |
| 3 | 18 | 28 | Ni (**not** noble) | $18 \cdot T_{2,3}$ |
| 4 | 32 | 60 | Nd (**not** noble) | $32 \cdot T_{2,3}$ |

**Caveat — the pure-$2n^2$ closures are not the chemical noble gases.**
The cumulative pure-$2n^2$ count $[2, 10, 28, 60, \ldots]$ maps the closed-shell sequence of a pure-Coulomb atom. The chemical noble gases $[2, 10, 18, 36, 54, 86]$ follow the **Madelung / $n+\ell$ (Aufbau)** ordering driven by electron–electron screening. The two sequences match only at He and Ne. They diverge at $n = 3$. Reproducing the physical noble gases requires both the $2n^2$ derivation and a categorical screening mechanism; the noble-gas identifications serve accordingly as a target.

The noble gases (He, Ne, Ar, Kr, Xe, Rn) define atoms whose electron cloud reduces to a **union of closed sub-links**. Every electron belongs to a complete shell.

**Photon absorption as a knot operation.**

A photon absorption event promotes a single electron between sub-Hopf links. The knot picture models this process:

1. **Incoming photon**: A wavefront ([wavefront propagation](#rem:wavefront-propagation)) carries energy $E = h\nu$ specified by the categorical Lagrangian ([categorical Lagrangian](#def:categorical-lagrangian)).
2. **Absorption**: The photon energy opens a crossing in the electron sub-Hopf link. This elevates the trefoil to an outer sub-link. This step corresponds to a **single crossing change** in the Skein relation.
3. **Emission**: The electron decays. The crossing closes. The system re-emits a photon of identical energy.

Crossing changes that preserve the topological type of the remaining sub-links dictate the selection rules.

**Maximal shell number from stability.**

The stability of the electron–hadron interaction bounds the number of electron shells. The outermost trefoil must remain Hopf-linked to the nucleus. Fluid dynamics models this via the vortex capture radius.

The ionization energy of the outermost electron scales as:

$$
  E_{\mathrm{ion}}  \propto 
  \frac{\mathfrak{E}_{\mathrm{cross}}(\text{electron--nucleus link})}{n^2}
$$

where $n$ denotes the shell number. The atom ionizes when $E_{\mathrm{ion}}$ drops below the thermal energy $k_B T$. This threshold sets a maximum shell number $n_{\max}$ determined by the nuclear charge $p$ and the ambient temperature.

**Open problems.**

1. **Shell capacity derivation**: Prove that the maximum number of trefoils in a closed sub-Hopf link at level $n$ strictly equals $2n^2$.
2. **Photon energy**: Derive the photon energy $E = h\nu$ from the categorical action. The wavefront equation supplies propagation. The frequency $\nu$ should match the winding number of the wavefront around the Reeb flow.
3. **Selection rules**: Identify the permitted Skein operations on the electron link. These recover the dipole selection rules $\Delta \ell = \pm 1$.
4. **Orbital shapes**: Match electron orbitals to the topological types of the sub-Hopf link. The angular momentum quantum number $\ell$ acts as the Seifert surface genus.
5. **Noble gas stability**: Prove that atoms whose electron cloud decomposes into a union of closed sub-links achieve maximal ionization energy in each period. The crossing energy of a complete sub-link must represent a local maximum.
