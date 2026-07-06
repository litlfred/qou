Let $\mathcal{H}_q$ be the $q$-shuffle Hopf algebra of a quantum observable
universe with coproduct $\Delta_q$, counit $\epsilon$, antipode $S_q$,
and $q$-Jackson derivative $D_q$.  A *grouplike* of $\mathcal{H}_q$ is an
element $g \in \mathcal{H}_q$ satisfying

$$
  \Delta_q(g) = g \otimes g,
  \qquad
  \epsilon(g) = 1.
$$

Grouplikes form a group $G(\mathcal{H}_q) \subseteq \mathcal{H}_q$ under multiplication:
they are the characters of the coalgebra structure.

**$q$-Exponential.**  The *$q$-exponential* is the unique grouplike
$\exp_q \in G(\mathcal{H}_q)$ satisfying the categorical flow equation

$$
  D_q  \exp_q  =  \exp_q,
  \qquad
  \exp_q(0) = 1.
$$

Equivalently, $\exp_q$ is the unique element of $\mathcal{H}_q$ with
$\mathcal{L}_q^{-1}[(1 - s)_q^{-1}] = \exp_q$, where $\mathcal{L}_q$ is
the categorical Laplace transform
([categorical Laplace transform](#def:categorical-laplace)).
