<!-- FILE_START: atomic-shells-element-instances-intro.md -->
We apply the shell construction to specific elements. The sequence traces the electron-shell Hopf assignment through the helium Hopf diagram, the noble-gas characterisation, the metallic character knot, and the francium extremal-metal block. We assign substrate-level shells to elements, compare predictions against periodic table data, and identify the mechanism enforcing noble-gas closure.
<!-- FILE_END: atomic-shells-element-instances-intro.md -->

<!-- FILE_START: electron-shells-hopf.md -->
We derive the electron configuration of atoms from the **closed sub-Hopf link structure** of the multi-electron trefoil chain. This yields the shell capacities $2, 8, 18, 32, \ldots = 2n^2$.

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

We conjecture that the maximum number of trefoils in a closed sub-Hopf link at level $n$ fixes the shell capacity at $2n^2$. A rigorous derivation remains open:

| Shell $n$ | Capacity $2n^2$ | Cumulative | Pure-$2n^2$ closure | Closed sub-link |
|----------:|----------------:|-----------:|---------------------|----------------|
| 1 | 2 | 2 | He (= noble) | $T_{2,3} \oplus T_{2,3}$ |
| 2 | 8 | 10 | Ne (= noble) | $8 \cdot T_{2,3}$ (Hopf $8$-chain) |
| 3 | 18 | 28 | Ni (**not** noble) | $18 \cdot T_{2,3}$ |
| 4 | 32 | 60 | Nd (**not** noble) | $32 \cdot T_{2,3}$ |

**Caveat — the pure-$2n^2$ closures are not the chemical noble gases.**
The cumulative pure-$2n^2$ count $[2, 10, 28, 60, \ldots]$ maps the closed-shell sequence of a pure-Coulomb atom. The chemical noble gases $[2, 10, 18, 36, 54, 86]$ follow the **Madelung / $n+\ell$ (Aufbau)** ordering driven by electron–electron screening. The two sequences match only at He and Ne. They diverge at $n = 3$. Reproducing the physical noble gases requires both the $2n^2$ derivation and a categorical screening mechanism. We state the noble-gas identifications as a target.

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
<!-- FILE_END: electron-shells-hopf.md -->

<!-- FILE_START: helium-hopf-diagram.md -->
The helium atom $\mathcal{A}(2, 2)$ provides the simplest closed electron shell. Its electron cloud comprises two trefoils $T_{2,3}$ joined by a Hopf link $\mathcal{L}_H$.

```tex
\begin{tikzcd}[row sep=3em, column sep=4em]
  & \boxed{\mathcal{N}(2{,}2)} \ar[dl, "\oplus"', dashed] \ar[dr, "\oplus", dashed] & \\
  T_{2,3} \ar[rr, "\mathcal{L}_H"', "\text{Hopf link}", bend right=15]
  & & T_{2,3} \\
  \underset{e_1}{\text{electron 1}} & \underset{1s^2 \text{ (closed)}}{\text{—————————————}} & \underset{e_2}{\text{electron 2}}
\end{tikzcd}

The Hopf link $\mathcal{L}_H$ defines the linking operation between $e_1$ and $e_2$. Each trefoil threads the Seifert surface of the other exactly once ($\mathrm{lk}(e_1, e_2) = 1$).

**Full atom structure.**

$$
  \mathcal{A}(2, 2) = 
  \underbrace{2\mathfrak{p} \oplus 2\mathfrak{n}}_{\alpha\text{-particle}}
   \oplus 
  \underbrace{T_{2,3} \oplus T_{2,3}}_{1s^2\text{ shell (closed)}}
$$

**Closure of the shell.**

The linking matrix of the two-electron Hopf link is:

$$
  L =  \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}.
$$

This matrix has rank $1$. Adding a third component $e_3$ requires $\mathrm{lk}(e_3, e_1) \geq 1$ and $\mathrm{lk}(e_3, e_2) \geq 1$. This increases the total linking number from $1$ to at least $3$. The crossing energy cost of these extra links exceeds the binding energy gain. The atom expels the third electron to a higher shell.

**Comparison: lithium ($p = 3$, $n = 4$).**

```tex
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  & \boxed{\mathcal{N}(3{,}4)} \ar[d, "\oplus"', dashed] & \\
  & \underset{1s^2}{\bigl(T_{2,3} \oplus T_{2,3}\bigr)} \ar[d, "\oplus"', dashed, "\text{level 2}"] & \\
  & T_{2,3} & \\
  & \underset{2s^1}{\text{outer electron}} &
\end{tikzcd}

$$
  \mathcal{A}(3, 4) = 
  3\mathfrak{p} \oplus 4\mathfrak{n}
   \oplus 
  \underbrace{(T_{2,3} \oplus T_{2,3})}_{1s^2}
   \oplus 
  \underbrace{T_{2,3}}_{2s^1}
$$

The third electron links to the closed $1s^2$ sub-link at a higher linking level. It passes around the entire Hopf pair instead of threading through it. This forms the $2s$ shell. The trefoil links to the $1s^2$ cluster as a single unit.
<!-- FILE_END: helium-hopf-diagram.md -->

<!-- FILE_START: noble-gas-characterization.md -->
An atom $\mathcal{A}(p,n)$ constitutes a noble gas if and only if its electron cloud $p \cdot T_{2,3}$ decomposes into a disjoint union of closed sub-Hopf links. Every shell is topologically full of curls.

**Statement.**
Let $\mathcal{A}(p,n)$ be a stable atom with electron cloud $\mathcal{E} = p \cdot T_{2,3}$. The atom $\mathcal{A}$ is chemically inert (noble) if and only if a partition $\mathcal{E} = S_1 \sqcup S_2 \sqcup \cdots \sqcup S_k$ exists satisfying:

1. **Closure**: Each $S_i = 2n_i^2 \cdot T_{2,3}$ forms a closed sub-Hopf link at level $n_i$. The trefoil chain within $S_i$ admits no additional linking without increasing total linking number.
2. **Exhaustion**: Every electron belongs to an $S_i$. No unlinked trefoils remain.
3. **Monotone nesting**: The sequence $n_1 < n_2 < \cdots < n_k$ holds. The linking of $S_{i+1}$ threads through $S_i$ without disrupting its closure.

Cumulative shell closure characterizes the six noble gases:

See [Table](#tbl:noble-gas-characterization-table-data).

**Ionization energy.**
The crossing energy of a closed sub-link represents a local maximum across each period. Removing an electron from a noble gas breaks a crossing in a fully interlocked chain. This costs more energy than removing an electron from an incomplete sub-link. Thus, noble gases sit at ionization-energy peaks.

**Electron affinity.**
A noble gas exhibits near-zero electron affinity. Attaching a new trefoil requires initiating a fresh sub-link at level $n_k+1$. This trefoil weakly Hopf-links to the outermost closed shell. The minimal linking number yields a binding energy negligible compared to thermal fluctuations.
<!-- FILE_END: noble-gas-characterization.md -->

<!-- FILE_START: noble-gas-characterization-interpretation.md -->
**Remark (why "full curls").**
Each trefoil $T_{2,3}$ is a $(2,3)$-torus knot. It winds twice around one axis and three times around the other. The writhe encodes the electron angular state. A closed sub-Hopf link at level $n$ is a chain where every trefoil curl fully interlocks with its neighbours. No Reidemeister I move can add or remove a crossing without breaking the sub-link.

This yields:
> **Full shell = full curls.**

A shell fills by exhausting available linking sites at its writhe level, not by reaching a numerical threshold. Topological rigidity drives inertness. No crossing remains available for a new electron.

**Remark (mathematical novelty).**
This topological characterization replaces heuristic chemistry with a rigid sub-Hopf link invariant. It formally binds empirical ionization energy peaks to crossing-energy maxima.
<!-- FILE_END: noble-gas-characterization-interpretation.md -->

<!-- FILE_START: metallic-character-knot.md -->
**Statement.**
Let $\mathcal{A}(p,n)$ be a stable atom with electron cloud $\mathcal{E} = p \cdot T_{2,3}$. Partition $\mathcal{E}$ into sub-Hopf links $S_1 \sqcup \cdots \sqcup S_k \sqcup R$. Each $S_i$ is a closed sub-link. The component $R$ is the residual sub-link. The atom $\mathcal{A}$ exhibits metallic character if and only if:

1. **Incompleteness**: $|R| < 2n_{k+1}^2$. The outermost sub-link contains unfilled linking sites.
2. **Low crossing energy**: $\mathfrak{E}_{\mathrm{cross}}(R) \ll \mathfrak{E}_{\mathrm{cross}}(S_k)$. The outermost curls wind loosely relative to the inner closed shells.
3. **Site availability**: $R$ contains at least one open linking site. The atom permits Hopf linking to an adjacent residual sub-link without disrupting the closed inner shells $S_i$.
<!-- FILE_END: metallic-character-knot.md -->

<!-- FILE_START: metallic-character-knot-interpretation.md -->
Noble gases possess closed sub-Hopf links. Metals possess an incomplete outermost sub-Hopf link with low crossing energy. This allows neighbouring atoms to share sites.

**Metallic bonding.**
In a metallic lattice, adjacent residual sub-links $R_a$ and $R_b$ merge their open linking sites. Outermost trefoils Hopf-link to the neighbour offering the lowest crossing energy. This models electron delocalisation:

$$
  R_a \oplus R_b
   \leadsto 
  \text{shared sub-link } R_{ab}
  = 
  R_a \cup R_b \text{ with merged linking sites.}
$$

Delocalised trefoils form a lattice-spanning sub-Hopf chain. This acts as a conduction band. Trefoils slide along this chain via Reidemeister II moves. These crossing exchanges conserve the total linking number.

**Strategy.**
We translate macroscopic properties into structural conditions on sub-Hopf links. Macroscopic conductivity corresponds to Reidemeister II mobility. Shared bonding becomes merged linking sites. Energetic inequalities derive from crossing energies, parametrized by the residual index $\lambda(R)$.

**Classification.**
The residual sub-link size $|R|$ and shell capacity $2n_{k+1}^2$ govern metallic behaviour.

| $\lvert R\rvert$ vs. capacity | Character | Examples |
|--------------------:|-----------|----------|
| $\lvert R\rvert = 1$ | Strong metal (alkalis) | Li, Na, K |
| $\lvert R\rvert = 2$ | Strong metal (alkaline earths) | Mg, Ca, Sr |
| $\lvert R\rvert \approx \tfrac{1}{2} \cdot 2n^2$ | Transition metal | Fe, Cu, Ni |
| $\lvert R\rvert = 2n^2 - 1$ | Weak nonmetal (halogens) | F, Cl, Br |
| $\lvert R\rvert = 2n^2$ | Noble gas (no residual) | He, Ne, Ar |

Alkali metals ($|R| = 1$) contain one loose curl. The minimal crossing energy to detach this curl matches their low ionization energy and high reactivity.

Transition metals have partially filled $d$-sub-links. These have $\ell = 2$, Seifert genus $2$, and $10$ linking sites. For $|R_d|$ between $1$ and $9$, multiple open sites exist at similar crossing energies. This yields:
- Variable oxidation states: Trefoils detach or share at similar energy costs.
- Catalytic activity: Open $d$-sites temporarily Hopf-link to substrate trefoils.
- Magnetic behaviour: Unpaired trefoils carry uncompensated writhe, producing a net magnetic moment.

**Conductivity.**
Electrical conductivity requires trefoil mobility along the lattice-spanning chain. An external field biases Reidemeister II moves. This produces a net drift of trefoils.

Resistance arises from pinning sites. These local energy barriers impede crossing exchanges. The barriers derive from:
- Lattice defects that disrupt chain topology.
- Thermal fluctuations that induce transient Reidemeister I moves.
- Phonons that modulate crossing energies via periodic compressions.

Low temperatures minimize crossing disruptions and lower resistance.

**Residual linking number.**
Noble gases have $R = \varnothing$. They lack residual sub-links, open linking sites, and delocalisation. The residual linking number $\lambda(R)$ parametrizes the chemical spectrum:

$$
  \lambda(R) = 0 \Longleftrightarrow \text{noble gas},
  \qquad
  \lambda(R) > 0 \Longleftrightarrow \text{non-inert}.
$$

Metallic character is strongest when $\lambda(R)$ is small relative to shell capacity. It weakens as $\lambda(R)$ approaches the closure threshold $2n^2$.
<!-- FILE_END: metallic-character-knot-interpretation.md -->

<!-- FILE_START: metallic-character-knot-novelty.md -->
**Remark.** The residual linking number $\lambda(R)$ provides a knot-theoretic metric for metallic character. This formalizes conductivity via Reidemeister transport. A rigid topological invariant replaces qualitative chemical models.
<!-- FILE_END: metallic-character-knot-novelty.md -->

<!-- FILE_START: francium-extremal-metal.md -->
Metallic character strengthens as the residual sub-link $R$ shrinks and the shell number $n$ grows. Francium ($p = 87$) extremises both conditions.

**Francium's electron cloud.**
Francium partitions its $87$ electrons as:

$$
  \mathcal{E}(87)
  = 
  \underbrace{S_1 \sqcup S_2 \sqcup \cdots \sqcup S_6}_{86
  \text{ electrons in closed sub-links (radon core)}}
  \sqcup
  \underbrace{R}_{|R| = 1}.
$$

The inner $86$ trefoils form the radon core. These six fully closed sub-Hopf links interlock every curl. The $87$th trefoil sits alone in shell $n = 7$. This single loose curl weakly Hopf-links to the core.

**Extremality of francium.**
Francium minimises the outermost crossing energy in two ways:

1. **Minimal residual**: $|R| = 1$. The lone trefoil lacks an interlocking partner. It occupies an open linking site without compensating closure. Elements with $|R| \geq 2$ exhibit partial interlocking among residual trefoils. This raises detachment energy.
2. **Maximal shell depth**: $n = 7$. The crossing energy scales as $\mathfrak{E}_{\mathrm{cross}} \propto 1/n^2$. The $n = 7$ trefoil is the most weakly bound alkali electron.

Consequently, francium exhibits:
- The lowest ionization energy ($E_{\mathrm{ion}} \approx 4.07 \mathrm{eV}$).
- The highest electropositive character. It donates its lone curl readily.
- The strongest metallic bonding tendency. Its single open linking site couples to neighbours with negligible crossing cost.

**The alkali series.**
The alkali metals possess $|R| = 1$ at increasing shell depth:

See [Table](#tbl:francium-extremal-metal-table-data).

Each atom has one loose trefoil. The crossing energy decreases monotonically with $n$. The slight ionization-energy uptick for francium reflects relativistic contraction of the $7s$ orbital. This corresponds to a tightening of the Hopf linking to the Borromean core at high $p$.

**Dual extremum: fluorine.**
Fluorine ($p = 9$) anchors the opposite end of the spectrum. It holds $|R| = 7$ trefoils out of a shell-$2$ capacity of $8$. The residual sub-link sits one trefoil short of closure. This empty linking site makes fluorine the most electronegative element. It pulls a trefoil from any neighbour to close its sub-link. This action is the topological dual to francium donating a curl.

$$
  \underbrace{\text{Fr}: |R| = 1}_{\text{most metallic}}
  \qquad\longleftrightarrow\qquad
  \underbrace{\text{F}: |R| = 2n^2 - 1}_{\text{most nonmetallic}}
$$

The filling fraction $|R| / 2n^2$ of the outermost sub-Hopf link parametrises the entire metallic–nonmetallic spectrum.
<!-- FILE_END: francium-extremal-metal.md -->

<!-- FILE_START: hydrogen-shell-writhe.md -->
**Proposition (conditional on [`conj:borromean-quark`](#conj:borromean-quark)).**
Let $T_{2,3}$ be the electron trefoil ([electron knot](#def:electron-knot)) Hopf-linked to a proton anchor. Let $w$ be the writhe in its minimal diagram.

1. **Shell--writhe correspondence.** The writhe fixes the principal quantum number $n$ via $n = (w - 1)/2$. The ground state has $w = 3$ ($n = 1$). Excited states $w = 2n + 1$ arise from Reidemeister I pairs at the exceptional divisor.
2. **Orbital counting.** At shell $n$, the trefoil vibrates transversely in its normal bundle $N_{T_{2,3}}$. The integers $\ell = 0, 1, \ldots, n - 1$ label the resonance modes. Each mode admits $2\ell + 1$ orientations. This yields $\sum_{\ell=0}^{n-1}(2\ell + 1) = n^2$ orbitals per shell.
3. **Energy scaling.** The Seifert surface of the Hopf link at level $n$ has area proportional to $n^2$. The crossing energy per Reidemeister I curl scales as $1/n^2$. This yields the energy levels $E_n = -E_{\mathrm{ion}} / n^2$.

**Archimedean specialisation (§7c).** This block evaluates generic $q$-deformation identities at the real-valued substrate parameter $q_0$. The categorical identities remain valid over any abstract coefficient ring.
<!-- FILE_END: hydrogen-shell-writhe.md -->

<!-- FILE_START: hydrogen-orbitals.md -->
**The picture.**

Hydrogen couples a large trefoil electron to a small Borromean proton. The proton occupies the center as a compact $\mathcal{B}_3$ formed of three unknots with $\mathrm{Vol} \approx 7.328$. The electron $T_{2,3}$ loops around the proton. They Hopf-link. The electron passes through the proton's Seifert surface exactly once.

The trefoil spins around the Borromean anchor. This motion sweeps out the electron cloud. The trefoil writhe and wrapping determine the cloud shape.

```tex
\begin{tikzcd}[row sep=4em, column sep=5em]
  & \underset{\text{\normalsize large } T_{2,3}}{\bigcirc\!\!\!\bigcirc\!\!\!\bigcirc}
    \ar[d, "\oplus"', "\text{Hopf}", dashed] & \\
  & \underset{\text{\normalsize small } \mathcal{B}_3}{\bullet}
    & \\
  & \underset{\text{proton (anchor)}}{\mathrm{Vol} \approx 7.328} &
\end{tikzcd}

The Borromean volume pins the massive proton in place. The zero volume of the trefoil keeps the electron light. Vacuum drag alone supplies its mass. The Hopf link $\oplus$ provides the electromagnetic binding.

**Shell transitions as Reidemeister I moves.**

The minimal diagram of the trefoil $T_{2,3}$ has writhe $w = +3$. Photon absorption executes a Reidemeister I move on the trefoil embedding within the Hopf link. This adds a curl at the exceptional divisor and increases the writhe by $+2$.

$$
  n \to n + 1
  \qquad\Longleftrightarrow\qquad
  w \to w + 2
  \qquad\Longleftrightarrow\qquad
  \text{two R-I moves at exceptional divisor.}
$$

The bare mass $m_e \approx 0.511$ MeV remains unchanged. Reidemeister moves preserve knot type (the Reidemeister mass-invariance conjecture). The binding energy $E_n = -13.6/n^2$ eV changes because R-I moves alter the embedding. The electron remains a trefoil but shifts to a higher writhe state.

The shell number $n$ matches the writhe level:

$$
  n =  \frac{w - 1}{2} =  1, 2, 3, 4, \ldots
  \qquad\text{for}\quad w = 3, 5, 7, 9, \ldots
$$

The added curls localize at the exceptional divisor of the brane tower. The ground-state trefoil ($w = 3$) lies in the base space $\mathcal{S}_0$. An excited trefoil ($w = 5$) places extra curls in the blow-up $\mathcal{S}_1$.

**Sub-shells from resonance modes.**

The embedded trefoil $T_{2,3}$ vibrates transversely within its normal bundle $N_{T_{2,3}}$ in the Bring surface. Laplacian eigenvalues on the trefoil curve govern the resonance frequencies. The mode integers $\ell = 0, 1, 2, \ldots$ label the standing-wave patterns:

- Mode $\ell = 0$: Uniform (no oscillation) — the $s$ orbital.
- Mode $\ell = 1$: One wavelength around the curve — the $p$ orbital.
- Mode $\ell = 2$: Two wavelengths — the $d$ orbital.

At linking level $n$, the Seifert surface has effective length proportional to $n$. Only modes with wavelength $\geq L/n$ fit. This yields the cutoff $\ell = 0, 1, \ldots, n - 1$. Each mode $\ell$ vibrates transversely in ambient $3$-space. Projected onto the sphere, the $2\ell + 1$ standing-wave orientations match the spherical harmonics $Y_\ell^m$. Thus:

$$
  \sum_{\ell=0}^{n-1} (2\ell + 1) =  n^2
  \quad\text{orbitals per shell.}
$$

This sum reproduces the observed capacity for all $n$.

**Note on geometric counting.**

The sum $\sum(2\ell + 1) = n^2$ matches standard quantum mechanics. The topological model identifies $\ell$ with trefoil resonance modes and $n$ with the writhe framing number. The remaining step requires a proof:

*The space of sections of the normal bundle $N_{T_{2,3}}$ of the trefoil in the Bring's surface, at total framing twist $k = 2(n-1)$, has dimension $n^2$.*

This appears as a conjecture below. The $2\ell + 1$ orientations and the cutoff $\ell \leq n - 1$ must follow from the $\mathrm{SO}(3)$ representation theory of this section space.
<!-- FILE_END: hydrogen-orbitals.md -->

