Beyond the grouplike $\exp_q$ ([$q$-exponential](#def\:q-exponential))
and its primitive inverse $\log_q$
([$q$-logarithm](#def\:q-logarithm)), the $q$-shuffle Hopf algebra
$\mathcal{H}_q$ admits a canonical *level-2* element — the $q$-dilogarithm —
obtained by iterating the primitive structure once.

**Iterated-primitive definition.** A *level-$k$ primitive* of $\mathcal{H}_q$
is an element $p_k \in \mathcal{H}_q^{\otimes k}$ satisfying the shuffle
recursion

$$
  \Delta_q(p_k) \;=\; p_k \otimes 1 + 1 \otimes p_k + \sum_{i=1}^{k-1}
    p_i \otimes p_{k-i},
$$

with $p_0 = 1$ and $p_1 = \log_q$. The solution space at each level
is one-dimensional (up to primitives of lower levels). The
**$q$-dilogarithm** is the unique level-2 primitive

$$
  \mathrm{Li}_2^q \;\in\; \mathcal{H}_q^{\otimes 2}
$$

normalised by the *pentagon identity* (below).

**Pentagon identity.** The $q$-dilogarithm satisfies the five-term
relation

$$
  \mathrm{Li}_2^q(y) + \mathrm{Li}_2^q(x)
  \;=\;
  \mathrm{Li}_2^q(xy) + \mathrm{Li}_2^q\!\left(\frac{x(1-y)}{1-xy}\right)
  + \mathrm{Li}_2^q\!\left(\frac{y(1-x)}{1-xy}\right),
$$

which is the Hopf-algebraic avatar of the *pentagon axiom* for the
:refterm[monoidal category]{#monoidal-category} $\mathbf{C}$. This identity characterises
$\mathrm{Li}_2^q$ up to a scalar — it is the unique level-2 primitive
compatible with the monoidal associator $\alpha_{X,Y,Z}$.

```tex
\begin{equation}\label{eq:q-dilog-pentagon}
\begin{tikzcd}[row sep=2.5em, column sep=2em]
  (X \otimes Y) \otimes (Z \otimes W)
    \ar[r, "\alpha"]
    \ar[d, "\alpha \otimes \mathrm{id}"']
  &  X \otimes (Y \otimes (Z \otimes W))
    \ar[d, "\mathrm{id} \otimes \alpha"]
  \\
  ((X \otimes Y) \otimes Z) \otimes W
    \ar[r, "\alpha"']
  &  X \otimes ((Y \otimes Z) \otimes W)
\end{tikzcd}
\qquad
\leftrightarrow
\qquad
\mathrm{Li}_2^q\text{-pentagon}
\end{equation}
```
