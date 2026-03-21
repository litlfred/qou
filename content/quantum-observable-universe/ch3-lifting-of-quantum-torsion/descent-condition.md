Let $(\mathcal{C}, A, \omega)$ be a quantum observable universe and let
$\{A_n\}_{n \geq 0}$ be its recursive brane tower; let $q$ denote the substrate parameter.  With Yekutieli
triples $(x^{(n)}, g^{(n)}, a^{(n)})$
([Definition](#def:yekutieli-triple)) and let
$A_\infty = \sum_{n,i} c_{n,i}\, \alpha_{n,i}$
([Remark](#rem:distributional-connection)) be the distributional
connection.  Then the global consistency of $A_\infty$ is equivalent to
the satisfaction of the *twisted $2$-cocycle condition*: for every
triple intersection $U_i \cap U_j \cap U_k$,

```tex
\begin{equation}\label{eq:twisted-2-cocycle}
  d\!\left(g_{ijk}^{(n)}\right)
  \;=\;
  a_{ij}^{(n)} \cdot g_{ijk}^{(n)} \cdot \left(a_{jk}^{(n)}\right)^{-1},
\end{equation}
```

where
$g_{ijk}^{(n)} = g_{ij}^{(n)} \cdot g_{jk}^{(n)} \cdot (g_{ik}^{(n)})^{-1}$
is the Cech $1$-cocycle deviation at level $n$,
$d(g_{ijk}^{(n)})$ denotes the Cech coboundary
(the failure of the $1$-cocycle condition), and
$a_{ij}^{(n)}, a_{jk}^{(n)} \in \mathcal{O}_M^{\times}$ are the
$2$-morphisms (quantum deformation feedback from $\mathrm{SU}_{q_n}(2)$).

Equivalently, the obstruction class $\kappa_n$
([Definition](#def:quantum-characteristic-classes)) is the cohomology
class of the twisted $2$-cocycle
$[a_{ij}^{(n)} \cdot (\cdot) \cdot (a_{jk}^{(n)})^{-1}]$ in
$H^2(M,\, \mathcal{O}_M^{\times})$.

---

Let $\{U_i\}$ be a good cover trivialising the tower.  On
$U_i \cap U_j$ the gauge transition function $g_{ij}^{(n)}$ patches
the connection $A_n$:
$$
  A_n|_{U_j} \;=\; g_{ij}^{(n)} \cdot A_n|_{U_i} \cdot
  (g_{ij}^{(n)})^{-1} + (g_{ij}^{(n)})^{-1}\, dg_{ij}^{(n)}.
$$
On a triple overlap $U_i \cap U_j \cap U_k$, the ordinary cocycle
condition $g_{ij}^{(n)} \cdot g_{jk}^{(n)} = g_{ik}^{(n)}$ holds if and
only if the connection $A_n$ is globally well-defined at level $n$ with
no twist.  The passage from level $n$ to level $n{+}1$ via the central
extension $\mathfrak{G}_{n+1} \to \mathfrak{G}_n$ introduces the
$2$-morphism twist: the transition functions at level $n{+}1$ are related
to those at level $n$ by
$$
  g_{ij}^{(n+1)} \;=\; a_{ij}^{(n)} \cdot g_{ij}^{(n)},
$$
where $a_{ij}^{(n)} \in \mathcal{O}_M^{\times}$ is the local lift datum
([Definition](#def:yekutieli-triple)).  Computing the cocycle deviation
at level $n{+}1$:

```tex
\begin{align*}
  g_{ijk}^{(n+1)}
  &= g_{ij}^{(n+1)} \cdot g_{jk}^{(n+1)} \cdot (g_{ik}^{(n+1)})^{-1} \\
  &= (a_{ij}^{(n)} \cdot g_{ij}^{(n)}) \cdot (a_{jk}^{(n)} \cdot g_{jk}^{(n)})
     \cdot (a_{ik}^{(n)} \cdot g_{ik}^{(n)})^{-1}.
\end{align*}
```

Since $a_{ij}^{(n)}$ is central (it lies in the band
$\mathcal{O}_M^{\times}$ of the gerbe), the gauge factors commute past
the $a$-factors, giving
$$
  g_{ijk}^{(n+1)}
  \;=\;
  a_{ij}^{(n)} \cdot a_{jk}^{(n)} \cdot (a_{ik}^{(n)})^{-1}
  \cdot g_{ijk}^{(n)}.
$$
The distributional connection $A_\infty$ is globally consistent if and
only if $g_{ijk}^{(n+1)} = 0$ for all $n$ in the Cech cohomology,
which requires
$$
  d(g_{ijk}^{(n)})
  \;=\;
  a_{ij}^{(n)} \cdot g_{ijk}^{(n)} \cdot (a_{jk}^{(n)})^{-1},
$$
where the left-hand side is the Cech coboundary
$\delta^2(g^{(n)})_{ijk}$ and the right-hand side is the twisted
conjugation by the $2$-morphisms.  The class of this twisted $2$-cocycle
in $H^2(M,\, \mathcal{O}_M^{\times})$ is precisely the obstruction
class $\kappa_n$ of
[Definition](#def:quantum-characteristic-classes): it vanishes if and
only if the cocycle deviation at level $n$ can be absorbed by the
$2$-morphism data, i.e. the lift from $\mathfrak{G}_n$ to
$\mathfrak{G}_{n+1}$ is unobstructed.

By \cite[Theorem 1.7]{yekutieli2010}, this is equivalent to the
vanishing of the Yekutieli obstruction class, closing the circle with
the lifting criterion ([Proposition](#prop:yekutieli-lifting)).
