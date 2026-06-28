Dual to the $q$-exponential ([$q$-exponential](#def:q-exponential))
is its categorical inverse.  A *primitive* of the $q$-shuffle Hopf
algebra $\mathcal{H}_q$ is an element $p$ satisfying

$$
  \Delta_q(p) = p \otimes 1 + 1 \otimes p,
  \qquad
  \epsilon(p) = 0.
$$

Primitives form a Lie algebra $\mathrm{Prim}(\mathcal{H}_q) \subseteq \mathcal{H}_q$ under
the $q$-commutator, and they are exactly the *infinitesimal* data of
grouplikes: the Milnor--Moore theorem identifies $\mathrm{Prim}(\mathcal{H}_q)$
with the tangent space at $1 \in G(\mathcal{H}_q)$.

**$q$-Logarithm.**  The **$q$-logarithm** is the unique primitive
$\log_q \in \mathrm{Prim}(\mathcal{H}_q)$ such that

$$
  \log_q \circ \exp_q \;=\; \mathrm{id}
  \qquad\text{(in the formal-power-series PROP).}
$$

Equivalently, $\log_q$ and $\exp_q$ form an *adjoint pair*

$$
  \log_q \;\dashv\; \exp_q
  \qquad
  \bigl(\mathrm{Prim}(\mathcal{H}_q), [\cdot,\cdot]_q\bigr)
  \;\rightleftarrows\;
  \bigl(G(\mathcal{H}_q), \cdot\bigr)
$$

between the Lie algebra of primitives and the group of grouplikes.
This is the Hopf-algebraic shadow of the Lie-theoretic exponential
$\mathfrak{g} \to G$.

```tex
\begin{equation}\label{eq:q-log-adjunction}
\begin{tikzcd}[row sep=2.5em, column sep=4em]
  \mathrm{Prim}(\mathcal{H}_q)
    \ar[r, bend left=15, "\exp_q"]
    \ar[r, phantom, "\dashv"]
  & G(\mathcal{H}_q)
    \ar[l, bend left=15, "\log_q"]
\end{tikzcd}
\end{equation}
```

**Universal property.**  $\log_q$ is the left adjoint of the
functor *grouplike-of* from primitives to grouplikes.  For any
Hopf-algebra morphism $\Phi \colon \mathcal{H}_q \to K$ sending grouplikes to
grouplikes and primitives to primitives,

$$
  \Phi(\log_q g) \;=\; \log_K \Phi(g)
  \qquad\forall  g \in G(\mathcal{H}_q),
$$

so $\log_q$ is *natural* in the Hopf algebra.
