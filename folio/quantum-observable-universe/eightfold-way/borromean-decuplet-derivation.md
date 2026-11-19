*The baryon decuplet --- the $10$-dimensional fully symmetric channel
of the Schur--Weyl decomposition $V^{\otimes 3}$ --- is realized by
the Borromean baryon ([borromean baryon](#def:borromean-baryon)) with
symmetric quark content.*

The Schur--Weyl decomposition at $N = 3$, $n = 3$ assigns the
partition $\lambda = (3)$ to the fully symmetric subspace of
$V^{\otimes 3}$, which has dimension $\binom{N+n-1}{n} = \binom{5}{3}
= 10$.  The $10$ states correspond to the $10$ elements of the weight
diagram, a triangle with vertices at $(3,0,0)$, $(0,3,0)$, $(0,0,3)$ in
quark-count coordinates $(n_u, n_d, n_s)$ --- that is, the corners
$\Delta^{++}\ (uuu)$, $\Delta^{-}\ (ddd)$ and $\Omega^{-}\ (sss)$.  The
remaining seven states fill the edges and the centre, with
$\Sigma^{*0}\ (uds)$ at the centre:

| State | Content | $I_3$ | $Y$ |
|---|---|---|---|
| $\Delta^{++}$ | $uuu$ | $+3/2$ | $+1$ |
| $\Delta^{+}$ | $uud$ | $+1/2$ | $+1$ |
| $\Delta^{0}$ | $udd$ | $-1/2$ | $+1$ |
| $\Delta^{-}$ | $ddd$ | $-3/2$ | $+1$ |
| $\Sigma^{*+}$ | $uus$ | $+1$ | $0$ |
| $\Sigma^{*0}$ | $uds$ | $0$ | $0$ |
| $\Sigma^{*-}$ | $dds$ | $-1$ | $0$ |
| $\Xi^{*0}$ | $uss$ | $+1/2$ | $-1$ |
| $\Xi^{*-}$ | $dss$ | $-1/2$ | $-1$ |
| $\Omega^{-}$ | $sss$ | $0$ | $-2$ |

**Borromean realization.**
Each decuplet state is a Borromean baryon: three quark-unknots joined
by the Borromean link $\mathcal{B}_3$.  The symmetric partition
$\lambda = (3)$ corresponds to the Hecke symmetrizer
$e_{(3)} = \sum_{\sigma \in S_3} T_\sigma$, which --- once normalized ---
projects onto the subspace where all three strands are interchangeable.
The normalization is not bookkeeping: $e_{(3)}$ satisfies
$e_{(3)}^2 = c\, e_{(3)}$ with $c = \sum_{\sigma \in S_3} q^{\ell(\sigma)}$,
equal to $|S_3| = 6$ in the classical limit, so $e_{(3)}$ is idempotent
only after division by $c$ and the symmetric channel is identifiable with
$\mathrm{Sym}^3$ only where $c$ is invertible.  In characteristic $2$ or
$3$ it is not, and the identification fails.

**Scope of the Borromean symmetry input.**
The Borromean link carries an $S_3$ symmetry permuting its three
components, so it is a *consistent* carrier for the symmetric channel.
It does not, however, *select* that channel: the octet $(2,1)$ and the
singlet $(1^3)$ live on the same three strands and are equally available
to the same link.  Brunnian-ness --- that removing any one component
frees the other two --- is a statement about sublink triviality, and no
argument in this framework connects it to the Young-symmetriser
decomposition of $V^{\otimes 3}$.  The channel
selection is carried entirely by the Hecke projector rather than by the
topology.

**Missing ingredient: spin and colour.**
The physical decuplet is spin-$3/2$, and what forces the *flavour*-symmetric
channel for it is the requirement that the total wavefunction be
antisymmetric once colour is included: with colour antisymmetric and
spin symmetric, flavour must be symmetric.  This chapter derives neither
the spin factor nor the colour antisymmetry, so the identification
$\lambda = (3) \leftrightarrow$ decuplet is at present a *matching of
dimensions and weights* rather than a derivation of the spin--flavour--colour
selection rule.  This is recorded as an open item in
[the open-problems section](#sec:eightfold-open-problems).

**Octet versus decuplet.**
The mixed partition $\lambda = (2,1)$ gives the $8$-dimensional
baryon octet (proton, neutron, $\Sigma$, $\Lambda$, $\Xi$), whose weight
diagram and its degeneracy are treated in
[the octet proposition](#prop:baryon-octet-decomposition).  The
antisymmetric partition $\lambda = (1^3)$ gives the singlet.  The
distinction between octet and decuplet is entirely carried by the
Hecke module: the $S^{(3)}$ projector (one-dimensional) selects the
decuplet, while the $S^{(2,1)}$ projector (two-dimensional) selects
the octet.

**Conditional on $N = 3$.**
As with all eightfold-way content, this derivation is conditional on
the flavor fundamental being three-dimensional
([eightfold-way multiplets via quantum Schur--Weyl duality](#prop:schur-weyl-eightfold)).  At $N = 2$, the
symmetric partition $(3)$ yields only a $4$-dimensional spin-$3/2$
quadruplet rather than a decuplet.
