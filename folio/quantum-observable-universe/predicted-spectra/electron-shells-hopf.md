The electron configuration of atoms is derived from the **closed sub-Hopf link structure** of the multi-electron chain. This yields the shell capacities $2, 8, 18, 32, \ldots = 2n^2$.

**The electron link.**

A neutral atom with $Z$ protons binds $Z$ electrons, each the word $e^- = \sigma_0\sigma_1\sigma_0$. The stable atom takes the form:

$$
  \mathcal{A}(p, n)
  = 
  \underbrace{Z\mathfrak{p} \oplus N\mathfrak{n}}_{\text{nucleus}}
   \oplus 
  \underbrace{p \cdot e^-}_{\text{electron cloud}}.
$$

The electron cloud $p \cdot e^-$ forms a chain of $p$ electrons bound by Hopf links. An **electron shell** defines a maximal closed sub-Hopf link of this chain. It forms a subset $S$ of electrons such that $\bigbowtie_{i \in S} e^-_i$ splits from the remaining chain. Each electron is the word $e^- = \sigma_0\sigma_1\sigma_0 \in B_3$ ([electron knot](#def:electron-knot)), and its closure is itself a Hopf link with two components. So a sub-Hopf link here counts electrons, not link components, and the linking number between two electrons needs a choice of one component of each. That choice is not fixed in the corpus.

**First example: helium ($p = 2$, $n = 2$).**

The helium electron cloud $e^- \oplus e^-$ forms a Hopf link of two electrons. This pair acts as a **closed sub-link**. It rejects a third electron unless the linking number increases. The two electrons fill the $1s$ shell.

Topological closure makes helium a noble gas. A third electron (lithium) forces a new sub-link. This weakly couples to the first to form the $2s$ shell.

**Shell capacities from sub-link closure.**

The conjecture is that the maximum number of electrons in a closed sub-Hopf link at level $n$ fixes the shell capacity at $2n^2$. A rigorous derivation remains open:

| Shell $n$ | Capacity $2n^2$ | Cumulative | Pure-$2n^2$ closure | Closed sub-link |
|----------:|----------------:|-----------:|---------------------|----------------|
| 1 | 2 | 2 | He (= noble) | $e^- \oplus e^-$ |
| 2 | 8 | 10 | Ne (= noble) | $8 \cdot e^-$ (Hopf $8$-chain) |
| 3 | 18 | 28 | Ni (**not** noble) | $18 \cdot e^-$ |
| 4 | 32 | 60 | Nd (**not** noble) | $32 \cdot e^-$ |

**Caveat — the pure-$2n^2$ closures are not the chemical noble gases.**
The cumulative pure-$2n^2$ count $[2, 10, 28, 60, \ldots]$ maps the closed-shell sequence of a pure-Coulomb atom. The chemical noble gases $[2, 10, 18, 36, 54, 86]$ follow the **Madelung / $n+\ell$ (Aufbau)** ordering driven by electron–electron screening. The two sequences match only at He and Ne. They diverge at $n = 3$. Reproducing the physical noble gases requires both the $2n^2$ derivation and a categorical screening mechanism. The noble-gas identifications are stated as a target.

The noble gases (He, Ne, Ar, Kr, Xe, Rn) define atoms whose electron cloud reduces to a **union of closed sub-links**. Every electron belongs to a complete shell.

**Photon absorption as a knot operation.**

A photon absorption event promotes a single electron between sub-Hopf links. The knot picture models this process:

1. **Incoming photon**: A wavefront ([wavefront propagation](#rem:wavefront-propagation)) carries energy $E = h\nu$ specified by the categorical Lagrangian ([categorical Lagrangian](#def:categorical-lagrangian)).
2. **Absorption**: The [photon](#def:photon) adds a strand-adding curl to the electron word, $e_n \mapsto e_n\sigma_{n+1}$. This is a Markov stabilisation, so the closure stays the Hopf link while the level rises by one ([shell--writhe correspondence](#conj:hydrogen-shell-writhe)). How this curl moves the electron to an outer sub-link is not re-derived.
3. **Emission**: The electron decays. The curl is removed. The system re-emits a photon of identical energy.

Curls that preserve the topological type of the remaining sub-links dictate the selection rules.

**Maximal shell number from stability.**

The stability of the electron–hadron interaction bounds the number of electron shells. The outermost electron must remain Hopf-linked to the nucleus. Fluid dynamics models this via the vortex capture radius.

The ionization energy of the outermost electron scales as:

$$
  E_{\mathrm{ion}}  \propto 
  \frac{\mathfrak{E}_{\mathrm{cross}}(\text{electron--nucleus link})}{n^2}
$$

where $n$ denotes the shell number. The atom ionizes when $E_{\mathrm{ion}}$ drops below the thermal energy $k_B T$. This threshold sets a maximum shell number $n_{\max}$ determined by the nuclear charge $p$ and the ambient temperature.

**Open problems.**

1. **Shell capacity derivation**: Prove that the maximum number of electrons in a closed sub-Hopf link at level $n$ strictly equals $2n^2$.
2. **Photon energy**: Derive the photon energy $E = h\nu$ from the categorical action. The wavefront equation supplies propagation. The frequency $\nu$ should match the winding number of the wavefront around the Reeb flow.
3. **Selection rules**: Identify the permitted Skein operations on the electron link. These recover the dipole selection rules $\Delta \ell = \pm 1$.
4. **Orbital shapes**: Match electron orbitals to the topological types of the sub-Hopf link. The angular momentum quantum number $\ell$ acts as the Seifert surface genus.
5. **Noble gas stability**: Prove that atoms whose electron cloud decomposes into a union of closed sub-links achieve maximal ionization energy in each period. The crossing energy of a complete sub-link must represent a local maximum.
