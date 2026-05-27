**Theorem.**
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe
with gauge group $G = \mathrm{Aut}^{\otimes}(\tau)$ of dimension
$d = \dim G$. Then:

**(a)** The classical limit obstruction
([classical limit obstruction](#def:classical-limit-obstruction))
is one-dimensional:

$$
\dim_k \mathrm{Obs}(\mathbf{C}, q \to 1)
=  \dim_k HH^2(\mathcal{U}_q, \mathrm{Ad})
=  1.
$$

**(b)** The unique obstruction class is the image of the Euler
characteristic under the trace map:

$$
\mathrm{Obs}(\mathbf{C}, q \to 1)
 \cong  k,
\qquad
[\phi_1] \mapsto \chi(A) \in R.
$$

**(c)** The obstruction vanishes at Kummer level $n$ iff
$n \mid \chi(A)$:

$$
\kappa_0 \bmod n = 0
\quad\Longleftrightarrow\quad
n \mid \chi(A).
$$

**Contrast with a general QU.**

See [Table 1](#tbl:qou-obstruction-reduction-table1-data).

*Proof of (a).* Three ingredients combine:

**Step 1: Observability kills $HH^0$.**
The QOU axiom $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$
([observability](#def:quantum-observable-universe)) is the statement

$$
HH^0(\mathcal{U}_q, \mathrm{Ad}) = \mathrm{Ad}^G = 0.
$$

The adjoint representation of a semisimple group has no invariant
vectors (equivalently: $\mathfrak{g}$ has trivial center).

**Step 2: Frobenius duality relates $HH^0$ and $HH^d$.**
The Frobenius--Hopf self-duality $A \cong A^\vee$
(the non-degenerate pairing from
[Frobenius--Hopf data](#def:frobenius-hopf-substrate)) induces a
Poincare duality on Hochschild cohomology
\cite{yekutieli2010}:

$$
HH^n(\mathcal{U}_q, \mathrm{Ad})
 \cong 
HH^{d-n}(\mathcal{U}_q, \mathrm{Ad})^\vee,
\qquad d = \dim G.
$$

This is the Van den Bergh duality for Frobenius algebras:
the dualizing bimodule is trivialized by the Frobenius form
$\lambda : A \to \mathbf{1}$.

**Step 3: Dimension count for $G = \mathrm{SU}(2)$.**
With $d = \dim \mathrm{SU}(2) = 3$:

See [Table 2](#tbl:qou-obstruction-reduction-table2-data).

The key: $HH^2 \cong (HH^{d-2})^\vee = (HH^1)^\vee$. The
outer derivation space is one-dimensional because the Lusztig
integral form $\mathcal{U}^{\mathbb{Z}}_q(\mathfrak{su}(2))$
is a **one-parameter** family — $q$ itself is the unique
deformation direction. There are no other independent deformation
parameters (this is a theorem of Drinfeld: the quantized
enveloping algebra is the unique deformation of
$\mathcal{U}(\mathfrak{g})$ for simple $\mathfrak{g}$).

Therefore $HH^2 \cong k$: the obstruction space is
one-dimensional. $\square$

*Proof of (b).*
The HKR comparison map sends the generator of $HH^2$ to the
Euler class $\kappa_0 = e(\xi) \in H^2(\mathcal{S}, \mathcal{B})$,
whose trace is $\chi(A)$
([QU-to-QOU theorem](#thm:qu-to-qou), item 2).
Since $HH^2 \cong k$ is one-dimensional, the entire obstruction
is determined by the single scalar $\chi(A)$. $\square$

*Proof of (c).*
This is the Kummer specialisation
([Kummer](#prop:ns-kummer-specialisation)): $\kappa_0 \bmod n = 0$
in $H^2(\mathcal{S}, \mathbb{G}_m) / nH^2(\mathcal{S}, \mathbb{G}_m)$
iff $n$ divides the trace $\chi(A)$. Equivalently, the motivic
Galois character $\chi^{\mathrm{mot}}_A$ is non-trivial at every
finite place $p \nmid \chi(A)$
([motivic perpetual obstruction](#prop:motivic-perpetual-obstruction)). $\square$

**The obstruction as a function on $\mathbb{P}^1$.**

The obstruction $\chi(A) \bmod n$ varies over the Kummer tower
$\{\mu_n\}_{n \geq 1}$ inside $\mathbb{G}_m \hookrightarrow \mathbb{P}^1$:

$$
\mathrm{obs}(n) :=
\begin{cases}
0 & \text{if } n \mid \chi(A), \\
\chi(A) \bmod n & \text{otherwise.}
\end{cases}
$$

For the Descartes universe with $\chi(A) = -6$:

See [Table 3](#tbl:qou-obstruction-reduction-table3-data).

The obstruction **vanishes at only finitely many levels**
(the divisors of $|\chi(A)| = 6$, namely $\{1, 2, 3, 6\}$)
and **persists at all levels $n$ with $\gcd(n, 6) \neq n$** —
in particular at all primes $> 3$.

**Physical consequence:** the classical limit $q \to 1$ must
pass through infinitely many Kummer levels where the
obstruction is nonzero. The density of non-vanishing levels
in the Kummer tower is

$$
\delta
=  1 - \frac{|\{n : n \mid 6\}|}{N}
\xrightarrow{N \to \infty} 1.
$$

In the limit: the obstruction is nonzero at density-$1$ set
of levels. The classical limit cannot avoid the obstruction.

**The three millennium problems as specializations.**
Each millennium problem is a property $\mathcal{P}$ that holds
unconditionally at the $q$-scale, with obstruction class
$[\mathcal{P}] \in \mathrm{Obs}(\mathbf{C}, q \to 1) \cong k$.
In the QOU, the single obstruction scalar controls all three:

See [Table 4](#tbl:qou-obstruction-reduction-table4-data).

All three obstructions are **images of the same class**
$\chi(A) \in HH^2 \cong k$ under different evaluation maps:

- **RH**: evaluate $\chi(A)$ on the spectral localization
 map $HH^2 \to H^2(\mathrm{Spec}(\xi_q))$
- **NS**: evaluate $\chi(A)$ on the collision restriction
 map $HH^2 \to H^2(\Sigma, \mathcal{B}|_\Sigma)$
- **BSD**: evaluate $\chi(A)$ on the elliptic restriction
 map $HH^2 \to H^2(\mathcal{E}_q, \mathcal{B}|_{\mathcal{E}_q})$

The one-dimensionality of $HH^2$ means these three evaluations
are **proportional**: there is a single real number (the Euler
characteristic $\chi(A) = -6$) that controls whether all three
millennium problems persist through the classical limit.

**Corollary.** If any one of the three millennium problems is
resolved (in either direction), the resolution constrains the
other two. Specifically: if the classical limit functor
$\mathcal{L}$ preserves the property $\mathcal{P}$ for one
problem, then the same functor either preserves or violates
$\mathcal{P}$ for the other two — the mechanism is the same,
only the evaluation map differs.
