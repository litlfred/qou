**Interpretive remark.**
The
[crystal-graph realisation](#conj:crystal-graph-realization) of Hecke
normal forms together with the
[confinement–grading correspondence](#conj:confinement-grading-correspondence)
admit a sharper computational reading: every observable extracted by
the Observation Frame $\tau$ is determined by its image at the
**crystal limit** $q \to 0$ and transported back to the generic
fibre [$\mathcal{S}_p$](#def:exceptional-divisor) along the flat
$q$-connection.

**Mechanism.**
At the crystal limit $q \to 0$ the cyclotomic KLR module category
$\mathcal{K}_n$ \cite{khovanovlauda2009, brundankleshchev2009}
degenerates to its associated graded — the Kashiwara crystal
$\mathrm{Cryst}(\mathfrak{sl}_n)$ \cite{kashiwara1991}. The
crystal carries no quantum corrections: edges are decorated only by
Kashiwara operators $\tilde{e}_i, \tilde{f}_i$ and weights are
integer-graded. The graded Euler characteristic
$\tau(M) = \sum_d (-1)^d \dim_R M_d$ that defines the
[cemetery group](#def:cemetery-group) is invariant under the flat
transport from the special fibre at $q = 0$ to a generic fibre
$\mathcal{S}_p$ at $q = q_0$:

$$
  \tau\bigl(\mathfrak{M}_K\bigr)\big|_{q = q_0}
  \;=\;
  \tau\bigl(\mathfrak{M}_K\bigr)\big|_{q \to 0},
$$

so any Laurent polynomial $P_K^{(k)}(q)$ extracted at level $k$ from
the crystal traversal lifts uniquely to the generic fibre via the
$\mathbb{Z}$-grading of the
[GB spectral sequence](#prop:gb-spectral-sequence).

**Consequence for the engine.**
The Gröbner–Shirshov reduction engine is therefore allowed to
operate entirely on the finite, discrete crystal graph at $q = 0$ —
no resolution of overlapping S-polynomials at the generic fibre is
required. The crystal-limit values pull back to the physically
relevant $q_0$ along the flat connection, and the cemetery filter of
[cemetery-group emergence](#conj:cemetery-group-emergence) acts
identically on both sides. This is the structural reason the
engine can replace continuous polynomial term-rewriting with
graph traversal without loss of information at the generic fibre.
