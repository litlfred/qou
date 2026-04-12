The formal proof chain of this paper lives entirely in
$\mathbb{Z}[q, q^{-1}]$ --- the Laurent polynomial
[ground ring](#def:quantum-planck-constant) --- and never invokes
real-number arithmetic.  Hyperbolic volumes enter only through the
specialisation $\iota \colon q \mapsto q_0$, where they appear as
computed invariants verified to $10^{-14}$ precision via SnapPy.

The [topological mass formula](#prop:topological-mass-formula)
$\mathfrak{m}(K) = \mathrm{Vol}(K)/\hbar_q^2$ mixes Laurent polynomials
in $q$ with hyperbolic volumes, but the categorical derivation
--- Hecke algebra, Skein relations, Gr\"obner--Shirshov normal forms,
transfer matrices --- is purely algebraic over $\mathbb{Z}[q, q^{-1}]$
and does not require knowing whether $\mathrm{Vol}(K)$ is transcendental,
algebraic, or even irrational.

The [algebraic independence
conjecture](#conj:hyperbolic-volume-transcendence) is therefore a
statement about the number-theoretic richness of the physical coefficient
ring, not a prerequisite for any result in this paper.  If it fails
--- that is, if some polynomial relation holds among the volumes ---
the mass predictions and categorical structure are unaffected; only the
algebraic structure of the coefficient ring would be simpler than
expected.  Conversely, whether the specialisation map $\iota$ is
injective on the extended ring
$\mathbb{Q}[q, q^{-1}][\mathrm{Vol}(4_1), \mathrm{Vol}(5_2),
\mathrm{Vol}(\mathcal{B}_3)]$ is precisely the content of the
conjecture.
