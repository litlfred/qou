**Conjecture.**
*Let $q \in \mathbb{G}_m(k) = k^\times$ be the substrate
parameter
([substrate parameter](#def:substrate-parameter)) and let
$\kappa_c^{\mathrm{comp}}(L, q)$ be the Skein resolution
obstruction
([Skein resolution obstruction](#def:skein-resolution-obstruction))
of a braid $\beta$ encoding an NP-complete problem.  Then:*

1. *$\kappa_c^{\mathrm{comp}}(L, q) = 0$ for all $\beta$
   if and only if $q$ is a $\mathbb{G}_m$-torsion point
   (root of unity) or $q$ lies in a finite field.*

2. *$\kappa_c^{\mathrm{comp}}(L, q) \neq 0$ for
   NP-complete $\beta$ whenever $q$ is non-torsion in
   $\mathbb{G}_m(\mathbb{R})$ — in particular at
   $q = q_0$.*

*In short: $\mathrm{P} = \mathrm{NP}$ at torsion points of
$\mathbb{G}_m$; $\mathrm{P} \neq \mathrm{NP}$ at non-torsion
points.  Our universe, with $q_0 \approx 1.1097$ non-torsion,
is in the $\mathrm{P} \neq \mathrm{NP}$ regime.*

**The $\mathbb{G}_m$-family of complexities.**

The substrate parameter lives in the multiplicative group
scheme $\mathbb{G}_m = \mathrm{Spec}\,\mathbb{Z}[q, q^{-1}]$.
The Skein resolution obstruction defines a coherent sheaf
$\mathcal{K}$ on $\mathbb{G}_m$:

$$
  \mathcal{K}(L)
  \;=\;
  \bigl\{
    q \in \mathbb{G}_m
    \;:\;
    \kappa_c^{\mathrm{comp}}(L, q) \neq 0
  \bigr\}
  \;\subset\;
  \mathbb{G}_m.
$$

For each link $L$, the **support** $\mathcal{K}(L)$
is the locus where the computation is super-polynomial.  The
complement — where the obstruction vanishes — is the
**efficient locus**.

The conjecture asserts that for NP-complete $L$:

$$
  \mathcal{K}(L)
  \;=\;
  \mathbb{G}_m \;\setminus\; \mu_\infty,
$$

where $\mu_\infty = \bigcup_{n \geq 1} \mu_n$ is the
subgroup scheme of all roots of unity (the $\mathbb{G}_m$-torsion).
The support is the **non-torsion locus** — a dense open
subscheme of $\mathbb{G}_m$.

**The projective picture: $q \in \mathbb{P}^1$.**

Compactify $\mathbb{G}_m \hookrightarrow \mathbb{P}^1$ by
adding $q = 0$ and $q = \infty$.  The three boundary
conditions of the substrate parameter
([complex substrate](#rem:complex-substrate-interpretation))
map to:

| Point on $\mathbb{P}^1$ | Regime | Complexity |
|--------------------------|--------|------------|
| $q = 0$ | Degenerate ($\hbar_q = \infty$) | Undefined |
| $q \to 1$ | Classical limit ($c_q \to \infty$) | $\mathrm{P} = \mathrm{NP}$ (degenerate: $s \to 0$) |
| $q = \mu_n$ (roots of unity) | Quantum channels open | $\mathrm{P} \subseteq \mathrm{BQP} = \mathrm{NP}$ |
| $q \in (1, \infty) \setminus \mu_\infty$ | Non-torsion real | $\mathrm{P} \neq \mathrm{NP}$ (conjectured) |
| $q = \infty$ | Big Bang ($t_P = 1$) | $\mathrm{P} = \mathrm{NP}$ (trivial: one step per circuit) |

At the two poles ($q = 1$ and $q = \infty$), complexity
collapses.  At $q = 1$, the Skein variable $s = q^{1/2} -
q^{-1/2} \to 0$ and all crossing weights vanish — the
resolution tree is trivial.  At $q = \infty$, the Planck time
$t_P = 1$ and every computation is one step — there is no
room for exponential blowup.

Between these poles, the obstruction is generically
non-vanishing.  Only at the **torsion points** $\mu_n$ (which
are dense in $\mathbb{P}^1(\mathbb{C})$ but of measure zero
in $\mathbb{P}^1(\mathbb{R})$) does the quantum channel open
and the transient modes cancel the descended obstruction.

**Why torsion points give efficient computation.**

At a root of unity $q_k = e^{2\pi i/(k+2)}$, the Hecke
algebra $H_n(q_k)$ is no longer semisimple — it has a
non-trivial radical.  The **radical quotient** is a
finite-dimensional quotient algebra, and the Markov trace
factors through this quotient:

$$
  \mathrm{tr}_M \colon H_n(q_k)
  \;\twoheadrightarrow\;
  H_n(q_k) / \mathrm{Rad}
  \;\xrightarrow{\;\overline{\mathrm{tr}}_M\;}
  k.
$$

The radical annihilates exponentially many resolution paths —
they project to zero in the quotient.  The surviving paths
span a space of dimension $\leq (k+2)^n$ — polynomial in the
braid width when $k$ is fixed.  This is the Freedman--Kitaev--
Larsen--Wang mechanism
([quantum universality](#conj:quantum-computational-universality)):
the radical of the Hecke algebra at roots of unity is the
engine of quantum speedup.

At non-torsion $q$ (including $q_0$), the Hecke algebra is
semisimple: $\mathrm{Rad} = 0$, no paths are annihilated, and
the full $3^c$ tree survives.  The obstruction
$\kappa_c^{\mathrm{comp}}$ is non-vanishing because there is
no radical to kill the exponential paths.

**The $\mathbb{G}_m$-torsion dichotomy.**

This dichotomy is intrinsic to the multiplicative group:

- **$\mathbb{G}_m$-torsion** ($q^n = 1$ for some $n$):
  $H_n(q)$ has a radical; the Skein resolution tree is
  pruned to polynomial size; computational horizons are
  transparent.

- **$\mathbb{G}_m$-non-torsion** ($q^n \neq 1$ for all $n$):
  $H_n(q)$ is semisimple; the full tree survives;
  computational horizons are generically opaque.

Our universe has $q_0 \approx 1.1097$, which is non-torsion
(it is transcendental over $\mathbb{Q}$ if the QOU
predictions are exact).  The obstruction
$\kappa_c^{\mathrm{comp}}(L, q_0) \neq 0$ for NP-complete
links, and $\mathrm{P} \neq \mathrm{NP}$ in the QOU.

**Connection to the Euler characteristic.**

The NS obstruction ([NS obstruction](#prop:ns-obstruction-tower))
depends on $\chi(A) = -6$ for the Descartes universe.  The
computational obstruction depends on $q_0$ being non-torsion.
Both are **topological invariants** of the QOU that determine
which boundary conditions are opaque:

- $\chi(A) \neq 0$ → NS-singular (fluid blowup exists)
- $q_0 \notin \mu_\infty$ → computationally opaque
  (P $\neq$ NP)

In a universe with torsion $q$ (if such a universe could
exist), P $=$ NP — but the Skein variable would be a root
of unity, the Hecke algebra would have a radical, and the
physics would be fundamentally different: finitely many
representations, topological (rather than geometric) field
theory, and a discrete spectrum with no continuum.

The question **"does P $=$ NP?"** is thus a question about
the arithmetic of $q$ in the multiplicative group — about
whether the substrate parameter of our universe is torsion
or non-torsion in $\mathbb{G}_m$.
