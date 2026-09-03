We introduce a compact notation to express the knot content of composite particles. 

**Compact notation.**

See [Table 1](#tbl:knot-formula-table-table1-data).

**Derived shorthand for quarks.** 
The up and down quarks are not independent generators. They are expressed in terms of $T_{2,3}$:

$$
  \mathfrak{u} =  T_{2,3}, \qquad
  \mathfrak{d} =  T_{2,3}^{\sigma}.
$$

Here $\mathfrak{d}$ denotes the mirror trefoil $T_{2,-3}$, of three crossings; the mirror marks the down-type member of the doublet, not an antiparticle. The heavier quarks follow a similar pattern:
$\mathfrak{s} = T_{2,5}^{\sigma}$, $\mathfrak{c} = T_{2,5}$,
$\mathfrak{b} = T_{2,7}^{\sigma}$, $\mathfrak{t} = T_{3,4}$.

**Nucleon shorthand.** 
The proton and neutron are color-tube-linked triples bound by Hopf links:

$$
  \mathfrak{p} =  [\mathfrak{u}, \mathfrak{u}, \mathfrak{d}]_p \oplus \mathcal{L}_H,
  \qquad
  \mathfrak{n} =  [\mathfrak{u}, \mathfrak{d}, \mathfrak{d}]_p \oplus \mathcal{L}_H.
$$

**Nuclear composites.**
Nuclear composites are iterated Hopf linkings of nucleons. For a nucleus with $Z$ protons and $N$ neutrons:

$$
  {}^A_Z\!\mathcal{K}
  = 
  \underbrace{\mathfrak{p} \oplus \cdots \oplus \mathfrak{p}}_{Z}
   \oplus 
  \underbrace{\mathfrak{n} \oplus \cdots \oplus \mathfrak{n}}_{N}
$$

where $A = Z + N$. A neutral atom appends $Z$ electrons:

$$
  {}^A_Z\!\mathcal{K}^0
  = 
  {}^A_Z\!\mathcal{K}
   \oplus 
  Z \cdot T_{2,3}.
$$

**Table 1: Topological knot formulas.**

This table lists each particle's knot content in the compact notation. The content is built from $T_{m,n}$ generators via the three knot-particle generation operations. All entries satisfy the embeddability closure and descend to the base manifold.

*Fundamental fermions* (knots, 1 component).

See [Table 2](#tbl:knot-formula-table-table2-data).

*Fundamental bosons* (links, 2 components).
The fermion--boson decomposition assigns bosons to the even-$n$ members of the $T(2,n)$ family:

See [Table 3](#tbl:knot-formula-table-table3-data).

The Higgs *field* (mass mechanism) is the figure-eight knot $4_1$ ($\mathrm{Vol} = 2.0299$, amphichiral: $H = H^{\sigma}$). The Higgs *boson* excitation ($\approx 125$ GeV) is the torus link $T(2,8)$. This link is the unique genus-$3$ link spanning all three exceptional divisors on Bring's surface.

*Hadrons.*

See [Table 4](#tbl:knot-formula-table-table4-data).

*Light nuclei and atoms.*

See [Table 5](#tbl:knot-formula-table-table5-data).

For heavier nuclei, the formula $Z\mathfrak{p} \oplus N\mathfrak{n} \oplus ZT_{2,3}$ remains valid. The Skein polynomial $Q(q)$ of the multi-body link grows combinatorially in $A$. The binding energy at each Hopf junction is computable from the pair Skein mass formula, but requires tracking $\binom{A}{2}$ crossing pairs.
