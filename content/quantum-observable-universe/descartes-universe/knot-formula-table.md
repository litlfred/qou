To express the knot content of composite particles compactly, we
introduce the following shorthand.

**Compact notation.**

| Symbol | Meaning |
|--------|---------|
| $T_{m,n}$ | Torus knot generator (winding numbers $m, n$) |
| $T(2,n)$ | Torus link ($n$ even) or knot ($n$ odd) |
| $\bowtie$ | Hopf linking on exceptional divisor $\mathcal{S}_c$ |
| $[\cdot,\cdot,\cdot]_p$ | Color-tube linking through $(r,g,b)$ fibers |
| $\sigma$ | Skein crossing change (transmutation) |
| $K^{\sigma}$ | Mirror (antiparticle) of knot $K$ |
| $N \cdot K$ | $N$ copies of knot $K$ in a multi-component link |

**Derived shorthand for quarks.** The up and down quarks are not
independent generators but are expressed in terms of $T_{2,3}$:

$$
  \mathfrak{u} =  T_{2,3}, \qquad
  \mathfrak{d} =  T_{2,3}^{\sigma}.
$$

Here $\mathfrak{d}$ denotes the three-twist knot $5_2$, a Skein
descendant of the trefoil.  Similarly for the heavier quarks:
$\mathfrak{s} = T_{2,5}^{\sigma}$, $\mathfrak{c} = T_{2,7}$,
$\mathfrak{b} = T_{2,5}$, $\mathfrak{t} = T_{3,4}$.

**Nucleon shorthand.** The proton and neutron are color-tube-linked
triples bound by Hopf links:

$$
  \mathfrak{p} =  [\mathfrak{u}, \mathfrak{u}, \mathfrak{d}]_p \bowtie \mathcal{L}_H,
  \qquad
  \mathfrak{n} =  [\mathfrak{u}, \mathfrak{d}, \mathfrak{d}]_p \bowtie \mathcal{L}_H.
$$

**Nuclear composites** are iterated Hopf linkings of nucleons.
For a nucleus with $Z$ protons and $N$ neutrons:

$$
  {}^A_Z\!\mathcal{K}
  = 
  \underbrace{\mathfrak{p} \bowtie \cdots \bowtie \mathfrak{p}}_{Z}
   \bowtie 
  \underbrace{\mathfrak{n} \bowtie \cdots \bowtie \mathfrak{n}}_{N}
$$

where $A = Z + N$.  A neutral atom appends $Z$ electrons:

$$
  {}^A_Z\!\mathcal{K}^0
  = 
  {}^A_Z\!\mathcal{K}
   \bowtie 
  Z \cdot T_{2,3}.
$$

**Table 1: Topological knot formulas.**

The table lists each particle's knot content in the compact
notation, built from $T_{m,n}$ generators via the three operations
([knot-particle generation](#def:knot-particle-generation)).  All
entries satisfy the embeddability closure
([embeddability closure](#thm:embeddability-closure)) and descend
to the base manifold.

*Fundamental fermions* (knots, 1 component).

| Particle | Symbol | Knot formula | $g$ | Crossings |
|----------|--------|-------------|:---:|:---------:|
| Photon | $\gamma$ | $\mathbf{1}_{B_4}$ (4-strand id; closure $= 4 \cdot 0_1$) | $0$ | $0$ |
| Neutrino | $\nu$ | $T_{1,0} = 0_1$ (1-strand) | $0$ | $0$ |
| Electron | $e^-$ | $T_{2,3}$ | $1$ | $3$ |
| Muon | $\mu^-$ | $T_{2,5}$ | $2$ | $5$ |
| Tau | $\tau^-$ | $T_{2,7}$ | $3$ | $7$ |
| Up quark | $\mathfrak{u}$ | $T_{2,3}$ | $1$ | $3$ |
| Down quark | $\mathfrak{d}$ | $T_{2,3}^{\sigma}$ | $1$ | $3$ |
| Strange quark | $\mathfrak{s}$ | $T_{2,5}^{\sigma}$ | $2$ | $5$ |
| Charm quark | $\mathfrak{c}$ | $T_{2,7}$ | $3$ | $7$ |
| Bottom quark | $\mathfrak{b}$ | $T_{2,5}$ | $2$ | $5$ |
| Hopf${}^2$ color binding | $\mathfrak{t}$ | $T_{3,4}$ | $3$ | $8$ | *(force carrier sector $H^{0,1}$; "top quark" label deprecated)* |

*Fundamental bosons* (links, 2 components).
The fermion--boson decomposition
([fermions are knots, bosons are links](#prop:fermion-boson-knot-link))
assigns bosons to the even-$n$ members of the $T(2,n)$ family:

| Particle | Symbol | Link formula | Components | Crossings |
|----------|--------|-------------|:----------:|:---------:|
| Gluon | $g$ | $T(2,2)$ (Hopf link) | $2$ | $2$ |
| $W$ boson | $W^{\pm}$ | $T(2,4)$ | $2$ | $4$ |
| $Z$ boson | $Z^0$ | $T(2,6)$ | $2$ | $6$ |
| Higgs boson | $H$ | $T(2,8)$ | $2$ | $8$ |

The Higgs *field* (mass mechanism) is the figure-eight knot
$4_1$ ($\mathrm{Vol} = 2.0299$, amphichiral: $H = H^{\sigma}$).
The Higgs *boson* excitation ($\approx 125$ GeV) is the torus
link $T(2,8)$, the unique genus-$3$ link spanning all three
exceptional divisors on Bring's surface
([Higgs as $T(2,8)$](#conj:higgs-t28)).

*Hadrons.*

| Particle | Symbol | Knot formula |
|----------|--------|-------------|
| Proton | $\mathfrak{p}$ | $[\mathfrak{u}, \mathfrak{u}, \mathfrak{d}]_p \bowtie \mathcal{L}_H$ |
| Neutron | $\mathfrak{n}$ | $[\mathfrak{u}, \mathfrak{d}, \mathfrak{d}]_p \bowtie \mathcal{L}_H$ |
| $\pi^+$ | | $\mathfrak{u} \bowtie \mathfrak{d}^{\sigma}$ |
| $\pi^0$ | | $(\mathfrak{u} \bowtie \mathfrak{u}^{\sigma} + \mathfrak{d} \bowtie \mathfrak{d}^{\sigma})/\!\sqrt{2}$ |
| $K^+$ | | $\mathfrak{u} \bowtie \mathfrak{s}^{\sigma}$ |
| $\Lambda$ | | $[\mathfrak{u}, \mathfrak{d}, \mathfrak{s}]_p \bowtie \mathcal{L}_H$ |
| $\Sigma^+$ | | $[\mathfrak{u}, \mathfrak{u}, \mathfrak{s}]_p \bowtie \mathcal{L}_H$ |

*Light nuclei and atoms.*

| Nucleus | $A$ | $Z$ | Knot formula |
|---------|-----|-----|-------------|
| Hydrogen | $1$ | $1$ | $\mathfrak{p} \bowtie T_{2,3}$ |
| Deuterium | $2$ | $1$ | $\mathfrak{p} \bowtie \mathfrak{n} \bowtie T_{2,3}$ |
| Helium-3 | $3$ | $2$ | $2\mathfrak{p} \bowtie \mathfrak{n} \bowtie 2T_{2,3}$ |
| Helium-4 | $4$ | $2$ | $2\mathfrak{p} \bowtie 2\mathfrak{n} \bowtie 2T_{2,3}$ |
| Lithium-7 | $7$ | $3$ | $3\mathfrak{p} \bowtie 4\mathfrak{n} \bowtie 3T_{2,3}$ |
| Carbon-12 | $12$ | $6$ | $6\mathfrak{p} \bowtie 6\mathfrak{n} \bowtie 6T_{2,3}$ |
| Oxygen-16 | $16$ | $8$ | $8\mathfrak{p} \bowtie 8\mathfrak{n} \bowtie 8T_{2,3}$ |
| Iron-56 | $56$ | $26$ | $26\mathfrak{p} \bowtie 30\mathfrak{n} \bowtie 26T_{2,3}$ |

For heavier nuclei the formula $Z\mathfrak{p} \bowtie N\mathfrak{n} \bowtie ZT_{2,3}$ remains valid, but the Skein polynomial $Q(q)$
of the multi-body link grows combinatorially in $A$.  The binding
energy at each Hopf junction is computable in principle from the
pair Skein mass formula
([terminal resolution](#prop:terminal-resolution)) but requires
tracking $\binom{A}{2}$ crossing pairs.
