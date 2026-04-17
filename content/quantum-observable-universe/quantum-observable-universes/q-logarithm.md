Dual to the $q$-exponential ([$q$-exponential](#def:q-exponential))
is its categorical inverse.  A *primitive* of the $q$-shuffle Hopf
algebra $H_q$ is an element $p$ satisfying

$$
  \Delta_q(p) = p \otimes 1 + 1 \otimes p,
  \qquad
  \epsilon(p) = 0.
$$

Primitives form a Lie algebra $\mathrm{Prim}(H_q) \subseteq H_q$ under
the $q$-commutator, and they are exactly the *infinitesimal* data of
grouplikes: the Milnor--Moore theorem identifies $\mathrm{Prim}(H_q)$
with the tangent space at $1 \in G(H_q)$.

**$q$-Logarithm.**  The *$q$-logarithm* is the unique primitive
$\log_q \in \mathrm{Prim}(H_q)$ such that

$$
  \log_q \circ \exp_q \;=\; \mathrm{id}
  \qquad\text{(in the formal-power-series PROP).}
$$

Equivalently, $\log_q$ and $\exp_q$ form an *adjoint pair*

$$
  \log_q \;\dashv\; \exp_q
  \qquad
  \bigl(\mathrm{Prim}(H_q), [\cdot,\cdot]_q\bigr)
  \;\rightleftarrows\;
  \bigl(G(H_q), \cdot\bigr)
$$

between the Lie algebra of primitives and the group of grouplikes.
This is the Hopf-algebraic shadow of the Lie-theoretic exponential
$\mathfrak{g} \to G$.

```tex
\begin{equation}\label{eq:q-log-adjunction}
\begin{tikzcd}[row sep=2.5em, column sep=4em]
  \mathrm{Prim}(H_q)
    \ar[r, bend left=15, "\exp_q"]
    \ar[r, phantom, "\dashv"]
  & G(H_q)
    \ar[l, bend left=15, "\log_q"]
\end{tikzcd}
\end{equation}
```

**Universal property.**  $\log_q$ is the left adjoint of the
functor *grouplike-of* from primitives to grouplikes.  For any
Hopf-algebra morphism $\Phi \colon H_q \to K$ sending grouplikes to
grouplikes and primitives to primitives,

$$
  \Phi(\log_q g) \;=\; \log_K \Phi(g)
  \qquad\forall  g \in G(H_q),
$$

so $\log_q$ is *natural* in the Hopf algebra.

**Base-ring independence.**  The adjoint pair $(\log_q, \exp_q)$ lives
in the universal setting of Hopf algebras — no convergence is
required.  Over $\mathbb{F}_p$ the $\log_q$ of a grouplike is still
a well-defined primitive, even when the series representation fails
([finite-field obstruction](#rem:q-exp-finite-field-obstruction)).

**Archimedean realisation.**  Over $\mathbb{C}$ the adjoint pair
$(\log_q, \exp_q)$ is represented by the convergent series

$$
  \log_q(1 + x) \;=\; \sum_{n \ge 1} \frac{(-1)^{n-1}  x^n}{[n]_q}
$$

(a corollary of the Taylor expansion of $\exp_q$; cf.
[Taylor series of $\exp_q$](#prop:q-exponential-taylor)).

**Physical meaning.**  The Reeb-flow holonomy between two substrate
slices $q_1 < q_2$ is a grouplike element; its $q$-logarithm is the
infinitesimal generator of the flow on $\mathrm{Prim}(H_q)$.  Hence
$\log_q$ measures *cosmological displacement* in Hopf-algebraic
units — the analogue of a "time rapidity" on the substrate side.
