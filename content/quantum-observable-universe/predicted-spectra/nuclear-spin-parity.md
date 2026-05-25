**The nuclear spin quantum number $J$ is integral when $A$ is even
and half-integral when $A$ is odd.**

This is a topological consequence of the braid representation:
each nucleon is a spin-$\tfrac{1}{2}$ fermion (a single-component
knot), and the tensor product of $A$ such representations has
spin parity determined by $A \bmod 2$.

**Proposition.**
*Let $\mathcal{N}(Z, N)$ be a nucleus with mass number $A = Z + N$.
Then the total angular momentum $J$ satisfies:*

$$
  J \in \mathbb{Z} \quad \Longleftrightarrow \quad A \in 2\mathbb{Z}
$$

$$
  J \in \mathbb{Z} + \tfrac{1}{2} \quad \Longleftrightarrow \quad A \in 2\mathbb{Z} + 1
$$

*Proof.*
Each nucleon — proton $\mathfrak{p} = \mathcal{B}_3(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})$ or
neutron $\mathfrak{n} = \mathcal{B}_3(\mathfrak{u}, \mathfrak{d}, \mathfrak{d})$ — is a knot
(single-component link closure of the Borromean braid).
By the fermion-boson correspondence
([fermions are knots](#prop:fermion-boson-knot-link)), knots
carry half-integral spin and links carry integral spin.

The nuclear link $\mathcal{N}(Z, N)$ is a satellite of $A$
Borromean knots joined by Hopf links.  In the $\mathrm{SU}_q(2)$
representation theory, the tensor product of $A$ spin-$\tfrac{1}{2}$
representations decomposes as:

$$
  \left(\tfrac{1}{2}\right)^{\otimes A}
  = 
  \bigoplus_{J = J_{\min}}^{A/2} V_J^{\oplus m_J}
$$

where $J_{\min} = 0$ if $A$ is even and $J_{\min} = \tfrac{1}{2}$
if $A$ is odd.  Every summand $V_J$ has the same parity
($J \bmod 1$) as $A/2 \bmod 1$.  This is a standard result in
$\mathrm{SU}_q(2)$ representation theory and holds for all
$q > 0$ — the $q$-deformation does not change the spin
parity of tensor products.

Explicitly: the $q$-Clebsch--Gordan decomposition
$V_{1/2} \otimes V_J = V_{J+1/2} \oplus V_{J-1/2}$ (for $J \geq 1/2$)
adds $\tfrac{1}{2}$ at each step, so after $A$ tensor factors
the spin parity equals $A/2 \bmod 1$.  $\square$

**The braid group perspective.**

In the braid group $B_A$, the writhe $w(\beta)$ of a braid word
$\beta$ (sum of crossing signs) has parity:

$$
  w(\beta) \equiv \binom{A}{2} \pmod{2}
$$

for the standard nuclear braid representative (all pairs
crossing once).  The writhe parity determines the statistics:

- $w$ even $\Leftrightarrow$ bosonic statistics $\Leftrightarrow$
  $J \in \mathbb{Z}$
- $w$ odd $\Leftrightarrow$ fermionic statistics $\Leftrightarrow$
  $J \in \mathbb{Z} + \tfrac{1}{2}$

Since $\binom{A}{2} = A(A-1)/2$, this is even iff $A \equiv 0$
or $1 \pmod{4}$.  But the spin-statistics theorem in the $q$-deformed
setting follows directly from the representation theory above,
without reference to writhe.

**The Jones--Wenzl projector.**

In the Temperley--Lieb algebra $TL_A(\delta)$ with
$\delta = -(q^{1/2} + q^{-1/2})$, the Jones--Wenzl projector
$p_A$ projects onto the highest-weight irreducible representation
$V_{A/2}$.  The spin of the ground state is determined by
the embedding of the nuclear link in the TL algebra and the
action of $p_A$.

For ${}^{14}\mathrm{N}$ ($A = 14$, even): the ground state has
$J = 1$ (experimentally observed by molecular band spectroscopy).
The Jones--Wenzl projector $p_{14}$ projects onto $V_7$, but the
nuclear link's embedding selects the $J = 1$ subrepresentation
via the coupling pattern of 7 protons and 7 neutrons.

**Key examples.**

See [Table](#tbl:nuclear-spin-parity-table-data).

The ${}^{14}\mathrm{N}$ case is historically significant:
its integer spin ($J = 1$) was incompatible with the pre-1932
proton-electron nuclear model (which would give $A = 14$
protons and 7 electrons $= 21$ fermions, hence half-integer
spin).  The resolution — neutrons as spin-$\tfrac{1}{2}$
neutral particles — gives $A = 14$ nucleons, hence integer spin.

In the Descartes framework, this is automatic: both the proton
$\mathcal{B}_3(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})$ and the neutron $\mathcal{B}_3(\mathfrak{u}, \mathfrak{d}, \mathfrak{d})$
are spin-$\tfrac{1}{2}$ knots (same Borromean topology, different
quark colouring), and $14$ half-integer spins couple to integer
total spin.
