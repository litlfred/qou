*Let $K$ be a commutative semiring satisfying the strong rank condition
(every field qualifies), let $V = Ku \oplus Kd$ be free on two generators
$u, d$, and let $\mathrm{Sym}^3 V$ be the space of homogeneous forms of
degree $3$ in $u, d$ over $K$.  Then $\dim_K \mathrm{Sym}^3 V = 4$.  Assign
to a monomial $u^{n_u} d^{n_d}$ the label $2I_3 = n_u - n_d$.  On the four
monomials of degree $3$ this label takes exactly the values $3, 1, -1, -3$,
it is odd at every monomial, and distinct monomials carry distinct labels.*

**The model term.**  The two variables are the two quark flavours of the
single-fibre tower, $u$ with $I_3 = +\tfrac12$ and $d$ with $I_3 = -\tfrac12$,
and $\mathrm{Sym}^3 V$ is the fully symmetric channel, partition $\lambda = (3)$, of the
Schur--Weyl decomposition of $V^{\otimes 3}$ at $N = 2$
([Proposition](#prop:schur-weyl-eightfold)).  Its four basis monomials are
named the **$\Delta$ quartet**:

| State | Monomial | $(n_u, n_d)$ | $2I_3$ |
|---|---|---|---|
| $\Delta^{++}$ | $u^3$ | $(3, 0)$ | $+3$ |
| $\Delta^{+}$ | $u^2 d$ | $(2, 1)$ | $+1$ |
| $\Delta^{0}$ | $u d^2$ | $(1, 2)$ | $-1$ |
| $\Delta^{-}$ | $d^3$ | $(0, 3)$ | $-3$ |

The label is stated as the doubled value $2I_3$ so that every statement stays
in $\mathbb{Z}$ and no division is performed.

**Proof.**  The dimension is the stars-and-bars count: the degree-$n$ forms in
$N$ variables are exactly the polynomials supported on the exponent vectors of
total degree $n$, and these are in bijection with the multisets of size $n$
drawn from $N$ flavours, so $\dim_K = \binom{N+n-1}{n}$.  At $N = 2$, $n = 3$
this is $\binom{4}{3} = 4$.  For the labelling, every exponent vector of
degree $3$ satisfies $n_u + n_d = 3$, so $2I_3 = 3 - 2n_d$ with
$n_d \in \{0, 1, 2, 3\}$.  This gives the four values $3, 1, -1, -3$, each
attained by $u^{3-k} d^{k}$ for $k = 0, 1, 2, 3$.  Each value is odd because
$n_u + n_d$ is odd.  Two vectors with the same $2I_3$ and the same total
degree have the same $n_u$ and the same $n_d$, so the label is injective. $\square$

**What the labelling adds to the count.**  The dimension alone says only that
the symmetric channel has four basis vectors.  Attainment and closure fix the
value set of $2I_3$ as exactly $\{3, 1, -1, -3\}$, the weight set of isospin
$\tfrac32$.  Injectivity makes the four vectors four *distinctly labelled*
states.

**Scope.**  The statement concerns weights only.  It constructs no action of
the isospin group and no raising or lowering operators, and it makes no
statement about spin, mass or any experimental quantity.  It is not conditional
on $N = 3$: unlike the decuplet
([Proposition](#prop:borromean-decuplet)), whose corner $\Omega^{-}$ requires a
third flavour, the quartet lives entirely at $N = 2$.  The oddness of $2I_3$
depends on the degree: at even degree the same construction gives even
values.
