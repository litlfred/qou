
Write $a = q^{-1}$ and $b = 1 - q^{-1}$, so $d_q = a\,d + b\,\pi_V d$.
Then

```tex
\begin{align*}
  d_q^2
  &= (a\,d + b\,\pi_V d)(a\,d + b\,\pi_V d) \\
  &= a^2\,\underbrace{d^2}_{= 0}
     + ab\,(d \circ \pi_V d + \pi_V d \circ d)
     + b^2\,\underbrace{\pi_V d \circ \pi_V d}_{= 0}.
\end{align*}
```

The first term vanishes because $d^2 = 0$ in the non-commutative
de Rham complex.  The last term vanishes because $\pi_V$ is the projection onto the
vertical (weight-$1$) summand of the Reeb decomposition
$\Omega^k(A) = \Omega^k_H(A) \oplus \theta_A \wedge \Omega^{k-1}_H(A)$:
the exterior derivative $d$ applied to a vertical form produces a form
whose vertical component has weight $\geq 2$ in $\theta_A$, but the
contact distribution forces $\theta_A \wedge \theta_A = 0$
(since $\theta_A$ is a $1$-form), so $\pi_V(d(\pi_V\alpha)) = 0$.
The middle term simplifies:
$d(\pi_V d\,\alpha) + \pi_V d(d\,\alpha) = \omega_V \wedge_q [\xi, \alpha]$
where $\omega_V = \pi_V(d^2_{\text{total}})$ represents the curvature
of the weight projection, and the commutator with $\xi$ arises
from $[d, \pi_V] = [\xi, {-}]$ on the graded pieces.
