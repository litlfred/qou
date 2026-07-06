Jones polynomials are the bridge between the finite-field model of
this section and the categorical machinery of
[Chapter](#chap:path-integrals-braiding).  We sketch the
correspondence here; the systematic theory lives in the braid
chapter.

The fusion category $\mathrm{Rep}_{\mathbb{F}_p}(\mathrm{SU}_q(2))$
carries a canonical $R$-matrix coming from the universal $R$-matrix
of $U_q(\mathfrak{sl}_2)$ specialised at a primitive $\ell$-th root
of unity in $\overline{\mathbb{F}_p}$.  This $R$-matrix turns the
fundamental representation $V$ into a braided object: the braid
group $B_n$ acts on $V^{\otimes n}$, and the Markov trace produces
a knot invariant which, after the standard Reshetikhin–Turaev
normalisation, is the Jones polynomial $J_K(q) \in
\mathbb{Z}[q^{\pm 1/2}]$ specialised mod $p$.

The interaction with the substrate parameter $q$ is direct: the
crossing number of a knot diagram tracks the number of $R$-matrix
applications, so $J_K(q)$ is a polynomial of degree at most the
crossing number, with coefficients controlled by the Hecke
algebra structure constants
([Chapter](#chap:path-integrals-braiding)).  At a root of unity
$q = \zeta_\ell$, divisibility patterns of $J_K(q)$ encode the
modular-Hecke combinatorics of [the modular Markov-trace conventions](#tm-notation).

In the $\pp$-adic / Witt-vector lift of the substrate parameter
([Witt-vector lift](#rem:witt-lift-qou)), the Jones polynomial is
recovered by reducing the lifted $R$-matrix mod $\pp$; the
modular Jones invariant agrees with the characteristic-zero one
where both make sense, and in this sense the finite-field model
and the archimedean model both produce the same knot-theoretic
output.  The detailed development, including the Markov trace
realisation and the connection between Jones polynomials and the
mass formula, lives in
[the topological mass formula](#prop:topological-mass-formula).
