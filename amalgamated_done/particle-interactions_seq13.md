<!-- FILE_START: skein-particle-generation-intro.md -->
Hadrons factorise uniquely into knot constituents under the relation algebra. A single family of fundamental strands—the torus knots $T_{m,n}$—generates every hadron under the Skein-relation moves. The resulting dictionary identifies each torus generator with a physical particle. We read the mass directly from the linking number and constituent volume.

This section builds the constructive hierarchy. We exhibit $T_{m,n}$ as the generating family for the hadron monoid. The mass functional on a Skein resolution splits the mass into a topological linking term and an additive constituent volume. This structure assigns a physical colour-tube reading to the constituents. The $q$-Schur--Weyl functor identifies each generator with a physical particle. The resulting dictionary tabulates the matches: torus knots and Hopf links to fundamental fermions, Borromean composites to baryons. A visual inventory collects the small-crossing knots with their braid words and assignments. We then use this correspondence to lift the dictionary to a bundle of state spaces over the brane manifold.

_(draft.)_
<!-- FILE_END: skein-particle-generation-intro.md -->

<!-- FILE_START: atomic-braid.md -->
**Definition.**
*The **atomic braid** of a neutral atom $(Z, N)$ is the element of $H_{A+Z}(q)$ obtained by assembling $Z$ protons, $N$ neutrons, and $Z$ electrons into a single Hecke algebra with $A + Z$ strands, where $A = Z + N$. The crossing coefficients are:*

See [Table 1](#tbl:atomic-braid-table1-data).

*The **ground-state ordering** is determined by:*

1. *Nuclear ordering: minimize $\Phi_1$ over all permutations of $Z$ protons and $N$ neutrons.*
2. *Electron insertion: greedily insert each of $Z$ electrons at the position minimizing $\Phi_1$.*

*The greedy insertion produces **ep pairs**: each electron sits immediately before its proton. The $\mathfrak{n}e = \mathrm{id}$ crossing means electrons pass through neutrons without generating Hecke generators.*

*For hydrogen ($A = 1$): the bare $[e, \mathfrak{p}]$ braid is LP-unstable. The $\mathfrak{p}e$ crossing uses the $\mathcal{B}_3$-dressed eigenvalues $(q^5, -q^{-5})$ instead of the bare $(q^{-1}, -q)$.*
<!-- FILE_END: atomic-braid.md -->

<!-- FILE_START: knot-particle-generation.md -->
**Definition.**
*The particle spectrum is generated from a finite set of torus knot generators $T_{m,n}$ (with $\gcd(m,n) = 1$) embedded in the standard torus $\mathbb{T}^2 \subset S^3$, together with two linking operations that act on the exceptional divisor and the color-tube fibration. The **torus knot generators** are the family*

$$
  \mathcal{G} =  \bigl\{ T_{m,n}  \big| 
  \gcd(m,n) = 1, m < n,
  m + n \leq N(\chi) \bigr\},
$$

*where $T_{m,n}$ winds $m$ times around the meridian and $n$ times around the longitude of $\mathbb{T}^2$, and $N(\chi)$ is a cutoff determined by the Euler characteristic of the Frobenius--Hopf object.* For the Descartes universe with $\chi(A) = -6$, the bound is $N(-6) = 9$, admitting:

See [Table](#tbl:knot-particle-generation-table-data).

We reserve $q$ for the substrate parameter and $p$ for base points. The winding indices are always $(m,n)$.
<!-- FILE_END: knot-particle-generation.md -->

<!-- FILE_START: knot-particle-generation-consequences.md -->
The fermion--boson decomposition extends the generator set to the even-$n$ torus links, which represent bosons. These include the $T(2,2)$ gluon, the $T(2,4)$ $W$ boson, the $T(2,6)$ $Z$ boson, and the $T(2,8)$ Higgs boson. These are two-component links with $\gcd(2,n) = 2$, carrying integer spin.

All torus knots have zero hyperbolic volume. They are satellite knots, not hyperbolic. Consequently, their bare mass under the topological mass formula vanishes:

$$
  \mathcal{M}_{\mathrm{bare}}(T_{m,n}) = 
  \frac{\mathrm{Vol}(T_{m,n})}{\hbar_q^{2}} =  0.
$$

Mass arises entirely through the linking operations: Hopf linking on the exceptional divisor, color-tube threading, and Skein crossing changes.

**Presentation of the particle Skein module.**
The Skein module admits the presentation

$$
  \mathrm{Sk}_q(\mathbf{C}) = 
  \mathbb{Z}[q^{\pm 1}]\bigl\langle
    \mathcal{G},
    \mathcal{L}_{\mathrm{Hopf}},
    \ell_c
  \bigr\rangle
  \Big/
  \bigl(
    qL_+ - q^{-1}L_- - (q^{1/2} - q^{-1/2})L_0
  \bigr),
$$

where $\mathcal{G}$ is the torus knot generator set. The quotient applies the HOMFLY-PT Skein relation at every crossing. Every particle in the knot--particle dictionary is a word in this presentation.
<!-- FILE_END: knot-particle-generation-consequences.md -->

<!-- FILE_START: skein-particle-generation-knot-particle-generation-intro.md -->
This sub-section formalises the categorical knot-particle correspondence. Every confined particle acts as a categorical knot. Every categorical knot generates a particle via the substrate-flow. The dictionary tabulates this correspondence across the lepton, meson, and nucleon sectors. The closing visual inventory and binding-knot tables fix the substrate-level reference set used in subsequent chapters.
<!-- FILE_END: skein-particle-generation-knot-particle-generation-intro.md -->

<!-- FILE_START: knot-particle-generation-interpretation.md -->
**Operation 1: Hopf linking on the exceptional divisor.**
Let $\mathcal{S}_c \cong \mathbb{P}^1(\mathbb{C}) \cong S^2$ be the exceptional divisor at a blow-up point $c$. The Hopf fibration $S^3 \to S^2 \cong \mathcal{S}_c$ makes the Hopf link $\mathcal{L}_{\mathrm{Hopf}}$ the canonical linking on $\mathcal{S}_c$. Given two generators $T_{m_1,n_1}$ and $T_{m_2,n_2}$, their **Hopf linking** is

$$
  \ell_H  \colon 
  T_{m_1,n_1}, T_{m_2,n_2}
   \longmapsto 
  T_{m_1,n_1} \mathbin{\cup_{\mathrm{Hopf}}} T_{m_2,n_2},
$$

producing a two-component link in $S^3$ fibered over $\mathcal{S}_c$. This is the colorless $U(1)$ binding operation:

- **Degree 0**: A single unknot $T_{1,0}$ sits on $\mathcal{S}_c$ with trivial braiding, corresponding to the neutrino at rest.
- **Degree 1**: An excited unknot $T_{1,0}$ at Reeb degree $\deg\alpha_V = 1$ acquires a unit of vertical charge.
- **Linking**: Two such unknots Hopf-link on $\mathcal{S}_c$, producing the simplest non-trivial bound state. The Hopf link contributes a binding energy $\mathcal{M}(\mathcal{L}_{\mathrm{Hopf}})$ invisible to the $\mathbb{P}^1(\mathbb{C})$ base but detectable via the Skein polynomial.

Iterating Hopf linking builds the leptonic and mesonic sectors.

**Operation 2: Color-tube threading.**
The three color tubes $(r, g, b) = (w_2 - z, w_3 - z, w_4 - z)$ from Bring's surface provide a second linking operation. Given three generators $T_{m_1,n_1}$, $T_{m_2,n_2}$, $T_{m_3,n_3}$, their **color-tube linking** threads each knot through one of the three chiral fibers:

$$
  \ell_c  \colon 
  T_{m_1,n_1}, T_{m_2,n_2}, T_{m_3,n_3}
   \longmapsto 
  T_{m_1,n_1} \mathbin{\cup_r} T_{m_2,n_2}
  \mathbin{\cup_g} T_{m_3,n_3}.
$$

The $S_3 \subset S_5$ permutation symmetry of the color coordinates ensures this linking is invariant under color permutations. This reproduces the $\mathrm{SU}(3)$ color confinement condition. Only color-singlet combinations produce observable hadrons.

**Operation 3: Skein crossing change.**
The $q$-deformed Skein relation at a crossing

$$
  q  L_+ -  q^{-1} L_-
  =  (q^{1/2} - q^{-1/2}) L_0
$$

acts as a transmutation operation. Resolving or introducing crossings in a linked configuration converts torus topologies into hyperbolic ones. The figure-eight knot $4_1$ (muon) is not a generator. It arises from a crossing change on a linked trefoil pair:

$$
  T_{2,3} \mathbin{\cup_{\mathrm{Hopf}}} T_{2,3}
  \xrightarrow{\sigma}
  4_1 +  \text{(Skein remainder)}.
$$

The muon is a Skein excitation of the electron.
<!-- FILE_END: knot-particle-generation-interpretation.md -->

<!-- FILE_START: knot-particle-correspondence.md -->
**Proposition.**
*Let $V = V_{1/2}$ be the fundamental representation of $\mathcal{U}_q(\mathfrak{su}(2))$. Let $B_n$ act faithfully on $V^{\otimes n}$ via the $R$-matrix braiding. By $q$-Schur--Weyl duality, $V^{\otimes n}$ decomposes into irreducible summands labeled by partitions $\lambda \vdash n$.*

*The Markov trace on $H_n(R, q)$ assigns a knot type $K_\lambda$ (the closure of any braid representative) to each irreducible summand. This establishes a bijection between irreducible summands of $V^{\otimes n}$ under the Iwahori--Hecke algebra $H_n(R, q)$ and knot/link types arising as closures of $n$-strand braids.*

*In particular, each localized knot $(p, K)$ in a bundle corresponds to a unique irreducible summand. Hadrons correspond to tensor products of such summands bound by Hopf links.*
<!-- FILE_END: knot-particle-correspondence.md -->

<!-- FILE_START: knot-particle-dictionary.md -->
The localized knot framework assigns a topological identity to each fundamental particle. This dictionary is derived from the categorical braiding on $V = V_{1/2}$. The $R$-matrix of $\mathcal{U}_q(\mathfrak{su}(2))$ endows $V^{\otimes n}$ with a faithful $B_n$-action. The $q$-Schur--Weyl duality decomposes $V^{\otimes n}$ into irreducible summands labelled by partitions $\lambda \vdash n$. By Alexander's theorem, every oriented knot is the closure of a braid $\beta \in B_n$. The Markov trace on the Iwahori--Hecke algebra $H_n(R, q)$ identifies each irreducible summand with a knot type.

**Fermion--boson principle.**
In the $T(2,n)$ torus family on the Bring's surface, the number of connected components is $\gcd(2,n)$. **Fermions** ($n$ odd) are knots (1 component, half-integer spin). **Bosons** ($n$ even) are links (2 components, integer spin). Quarks are Borromean-linked unknots in the exceptional divisor.

**Table 1: Fermion sector** (knots, 1 component).

See [Table 1](#tbl:knot-particle-dictionary-table1-data).

**Table 2: Boson sector** (links, 2 components).

See [Table 2](#tbl:knot-particle-dictionary-table2-data).

**Table 3: Derived knots and mass mechanism.**

See [Table 3](#tbl:knot-particle-dictionary-table3-data).

**Table 4: Quark sector** (on the exceptional divisor).

Each quark is an **unknot** ($0_1$) within the Borromean braid $\mathcal{B}_3$. Up vs down flavour is encoded by crossing orientation ($\sigma$ vs $\sigma^{-1}$), not knot type. The table below shows which lepton's torus knot each quark descends from on the exceptional divisor. This is a descent relationship, not the quark's own knot type:

See [Table 4](#tbl:knot-particle-dictionary-table4-data).

**Precision data.** All torus knots have zero hyperbolic volume ($\mathrm{Vol} = 0$), so their bare mass vanishes. Mass arises entirely from crossing energy $\mathfrak{E}_{\times}(q) = \tfrac{1}{2}(q - q^{-1})$ at each self-crossing and from Hopf linking. The figure-eight knot ($4_1$) is the unique amphichiral knot driving the mass mechanism, with $\mathrm{Vol}(4_1) = 2.0299$. Jones polynomial values at $q = q_0 = 1.109978595554181\ldots$ (50 dps) are listed for the building-block knots.

In a bundle initial condition $\mathcal{S}_0$, each entry $(p_i, K_i)$ is one row of this dictionary placed at a specific point on $\mathbb{P}(V)$.
<!-- FILE_END: knot-particle-dictionary.md -->

<!-- FILE_START: binding-knots-visual-inventory.md -->
**Remark (visual inventory of binding knots).**

This block collects diagrams for the knots and links that act as binding operators across the QOU framework. Each entry shows the standard diagram (TikZ), its braid word in $B_n$, and its entry point in the binding pipeline. For per-particle context, see the knot-particle dictionary.

## Trivial: the unknot

The unknot $0_1 = T_{1,0}$ is a single unknotted circle — the trivial element of every braid group. It carries zero crossings. Hence it has zero $q$-deformed crossing energy, $\mathfrak{E}_\times(q) = \frac{1}{2}(q - q^{-1}) \cdot 0 = 0$, and its bare mass vanishes. It plays two disjoint roles:

1. **Neutrino $\nu$**: a single unknot in $H_1(q)$. Its mass arises entirely from Reeb-divisor coupling, not from the knot itself.
2. **Each quark inside the Borromean baryon**: the three strands of $\mathcal{B}_3$ are individually unknotted. Only their joint closure is non-trivial.

```tex
\begin{tikzpicture}[scale=1, line width=1.2pt]
  \draw[->, >=Latex] (0:0.9) arc (0:355:0.9);
  \node at (0, 0) {\small $0_1$};
  \node at (1.6, 0) {$\equiv$};
  \node at (3.0, 0) {$\beta = \mathbf{1} \in B_1$};
\end{tikzpicture}
```

## Hopf link (the "bowtie")

The Hopf link $L2a1 = T(2, 2)$ is the simplest non-trivial link: two circles linked once. Its braid word $\sigma_0 \sigma_1 \in B_3$ closes to two interlocked loops, giving a "bowtie" silhouette when drawn flat with a single crossing per loop. This is the categorical identity of the **gluon** (strong-force mediator).

```tex
\begin{tikzpicture}[scale=1, line width=1.2pt]
  % left ring
  \draw[->, >=Latex] (-0.6, 0) circle (0.6);
  % right ring (overlapping)
  \draw[white, line width=4pt]
    (0.6, 0) ++(165:0.6) arc (165:195:0.6);
  \draw[->, >=Latex] (0.6, 0) circle (0.6);
  \node at (0, -1.2) {\small $L2a1 = T(2,2)$};
  \node at (3.4, 0) {$\beta = \sigma_0 \sigma_1 \in B_3$};
\end{tikzpicture}
```

The full torus-link family $T(2, 2k)$ supplies the electroweak bosons: $T(2,2)$ gluon, $T(2,4)$ $W$, $T(2,6)$ $Z$, $T(2,8)$ Higgs.

## Trefoil $3_1 = T(2,3)$

The trefoil knot is the simplest non-trivial knot, and the canonical **electron** identity. Its braid word $\sigma_0\sigma_1\sigma_0 \in B_3$ closes to a 3-cusp shape with three over/under crossings. The crossing energy $3 \cdot \mathfrak{E}_\times(q) = \frac{3}{2}(q - q^{-1})$ fixes the leptonic mass quantum.

```tex
\begin{tikzpicture}[scale=0.9, line width=1.2pt]
  % three-fold-symmetric trefoil schematic
  \foreach \a in {0, 120, 240} {
    \draw[rotate=\a]
      (0:1.0) .. controls (40:1.4) and (80:1.4) .. (120:1.0);
  }
  \node at (0, 0) {\small $3_1$};
  \node at (3.0, 0) {$\beta = \sigma_0\sigma_1\sigma_0$};
\end{tikzpicture}
```

The torus-knot family $T(2, 2k+1)$ extends to the muon $T(2,5)$, tau $T(2,7)$, and beyond.

## Figure-eight $4_1$ — the mass mechanism

The figure-eight $4_1$ is the smallest hyperbolic knot ($\mathrm{Vol}(4_1) \approx 2.0299$, the CAL-2 calibration anchor). Its braid word is $\sigma_0\sigma_1^{-1}\sigma_0\sigma_1^{-1} \in B_3$. The alternating positive/negative crossings give amphichirality $4_1 \cong 4_1^{\,\text{mirror}}$ (invariance under $q \mapsto q^{-1}$). This property selects $4_1$ as the **Higgs / mass mechanism**.

```tex
\begin{tikzpicture}[scale=0.9, line width=1.2pt]
  \draw (-1.2, 0)
    .. controls (-1.5, 1.0) and (-0.4, 1.4) .. (0.0, 0.6)
    .. controls (0.4, -0.2) and (-0.4, -0.2) .. (0.0, -0.6)
    .. controls (0.4, -1.4) and (1.5, -1.0) .. (1.2, 0)
    .. controls (1.0, 1.0) and (-1.0, 1.0) .. (-1.2, 0);
  \node at (-1.8, 0) {\small $4_1$};
  \node at (3.5, 0)
    {$\beta = \sigma_0\sigma_1^{-1}\sigma_0\sigma_1^{-1}$};
\end{tikzpicture}
```

## Borromean rings $\mathcal{B}_3 = 6^3_2$

The Borromean rings are three mutually linked circles such that removing any one frees the other two — no two are individually linked. The braid word is $\mathcal{B}_3 = \sigma_0\sigma_1\sigma_2\sigma_0\sigma_1\sigma_2 \in B_4$. The hyperbolic volume is $\mathrm{Vol}(\mathcal{B}_3) = 8G$ (twice the volume of a regular ideal octahedron, where $G$ is Catalan's constant). This provides the **three-quark confinement** identity for the proton, neutron, and $^4$He nucleus, and sets the binding-energy scale $\alpha = m_e \cdot 8G \approx 3.7445$ MeV.

```tex
\begin{tikzpicture}[scale=0.85, line width=1.2pt]
  % three circles arranged at 120° offsets
  \def\R{0.85}
  \def\d{0.55}
  \draw[red!70!black] (0, \d) circle (\R);
  \draw[green!50!black] ({-\d*0.866}, {-\d*0.5}) circle (\R);
  \draw[blue!70!black] ({\d*0.866}, {-\d*0.5}) circle (\R);
  \node at (0, -2.0) {\small $6^3_2 = \mathcal{B}_3$};
  \node at (4.7, 0)
    {$\beta = \sigma_0\sigma_1\sigma_2\sigma_0\sigma_1\sigma_2$};
\end{tikzpicture}
```

(The schematic above shows the three rings overlapping; the actual over/under crossing pattern alternates so that no two rings are individually linked. See KnotInfo entry $L6a4$ — also known as the three-component Brunnian link.)

## Cross-reference table

See [Table 1](#tbl:binding-knots-visual-inventory-table1-data).

## Higher-order links (in mass-table-ppb pipeline)

The zero-parameter Kashaev law $B = \rho_F \cdot \mathrm{Vol}_{\mathrm{hyp}}(K)$ uses additional hyperbolic knots and links that do not yet have visualizations here:

See [Table 2](#tbl:binding-knots-visual-inventory-table2-data).

These are flagged `census-assigned` in the pipeline. This indicates the assignment was selected via census search to match AME binding energies, rather than derived from first principles.
<!-- FILE_END: binding-knots-visual-inventory.md -->
