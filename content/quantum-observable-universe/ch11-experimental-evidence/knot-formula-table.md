To express the knot content of composite particles compactly, we
introduce the following shorthand.

**Compact notation.**

| Symbol | Meaning |
|--------|---------|
| $T_{m,n}$ | Torus knot generator (winding numbers $m, n$) |
| $\bowtie$ | Hopf linking on exceptional divisor $E_c$ |
| $[\cdot,\cdot,\cdot]_c$ | Color-tube linking through $(r,g,b)$ fibers |
| $\sigma$ | Skein crossing change (transmutation) |
| $\overline{K}$ | Mirror (antiparticle) of knot $K$ |
| $N \cdot K$ | $N$ copies of knot $K$ in a multi-component link |

**Derived shorthand for quarks.** The up and down quarks are not
independent generators but are expressed in terms of $T_{2,3}$:

$$
  u \;=\; T_{2,3}, \qquad
  d \;=\; \sigma(T_{2,3}).
$$

Here $d$ denotes the three-twist knot $5_2$, a Skein descendant of
the trefoil.  Similarly for the heavier quarks:
$s = \sigma(T_{2,5})$, $c = T_{2,7}$,
$b = T_{2,5}$, $t = T_{3,4}$.

**Nucleon shorthand.** The proton and neutron are color-tube-linked
triples bound by Hopf links:

$$
  \mathfrak{p} \;=\; [u, u, d]_c \bowtie \mathcal{L}_H,
  \qquad
  \mathfrak{n} \;=\; [u, d, d]_c \bowtie \mathcal{L}_H.
$$

**Nuclear composites** are iterated Hopf linkings of nucleons.
For a nucleus with $Z$ protons and $N$ neutrons:

$$
  {}^A_Z\!\mathcal{K}
  \;=\;
  \underbrace{\mathfrak{p} \bowtie \cdots \bowtie \mathfrak{p}}_{Z}
  \;\bowtie\;
  \underbrace{\mathfrak{n} \bowtie \cdots \bowtie \mathfrak{n}}_{N}
$$

where $A = Z + N$.  A neutral atom appends $Z$ electrons:

$$
  {}^A_Z\!\mathcal{K}^0
  \;=\;
  {}^A_Z\!\mathcal{K}
  \;\bowtie\;
  Z \cdot T_{2,3}.
$$

**Table 1: Topological knot formulas.**

The table lists each particle's knot content in the compact
notation, built from $T_{m,n}$ generators via the three operations
([knot-particle generation](#def:knot-particle-generation)).  All
entries satisfy the embeddability closure
([embeddability closure](#thm:embeddability-closure)) and descend
to the base manifold.

*Fundamental particles.*

| Particle | Symbol | Knot formula | $g$ |
|----------|--------|-------------|-----|
| Photon | $\gamma$ | $\varnothing$ (point) | $0$ |
| Neutrino | $\nu$ | $T_{1,0}$ | $0$ |
| Electron | $e^-$ | $T_{2,3}$ | $1$ |
| Muon | $\mu^-$ | $\sigma(T_{2,3} \bowtie T_{2,3})$ | $1$ |
| Tau | $\tau^-$ | $T_{2,5} \bowtie T_{1,0}$ | $2$ |
| Up quark | $u$ | $T_{2,3}$ | $1$ |
| Down quark | $d$ | $\sigma(T_{2,3})$ | $1$ |
| Strange quark | $s$ | $\sigma(T_{2,5})$ | $1$ |
| Charm quark | $c$ | $T_{2,7}$ | $3$ |
| Bottom quark | $b$ | $T_{2,5}$ | $2$ |
| Top quark | $t$ | $T_{3,4}$ | $3$ |

*Hadrons.*

| Particle | Symbol | Knot formula |
|----------|--------|-------------|
| Proton | $\mathfrak{p}$ | $[u, u, d]_c \bowtie \mathcal{L}_H$ |
| Neutron | $\mathfrak{n}$ | $[u, d, d]_c \bowtie \mathcal{L}_H$ |
| $\pi^+$ | | $u \bowtie \overline{d}$ |
| $\pi^0$ | | $(u \bowtie \overline{u} + d \bowtie \overline{d})/\!\sqrt{2}$ |
| $K^+$ | | $u \bowtie \overline{s}$ |
| $\Lambda$ | | $[u, d, s]_c \bowtie \mathcal{L}_H$ |
| $\Sigma^+$ | | $[u, u, s]_c \bowtie \mathcal{L}_H$ |

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

For heavier nuclei the formula $Z\mathfrak{p} \bowtie N\mathfrak{n}
\bowtie ZT_{2,3}$ remains valid, but the Skein polynomial $Q(q)$
of the multi-body link grows combinatorially in $A$.  The binding
energy at each Hopf junction is computable in principle from the
pair Skein mass formula
([terminal resolution](#prop:terminal-resolution)) but requires
tracking $\binom{A}{2}$ crossing pairs.
