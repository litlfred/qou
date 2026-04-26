
Write $a = q^{-1}$ and $b = 1 - q^{-1}$, so $d_q = ad + b\pi_V d$.
Then

```tex
\begin{align*}
  d_q^2
  &= (ad + b\pi_V d)(ad + b\pi_V d) \\
  &= a^2\underbrace{d^2}_{= 0}
     + ab(d \circ \pi_V d + \pi_V d \circ d)
     + b^2\underbrace{\pi_V d \circ \pi_V d}_{= 0}.
\end{align*}
```

The first term vanishes because $d^2 = 0$ in the non-commutative
de Rham complex.  The last term vanishes because $\pi_V$ is the projection onto the
vertical (weight-$1$) summand of the Reeb decomposition
$\Omega^k(A) = \Omega^k_H(A) \oplus \varTheta_A \wedge \Omega^{k-1}_H(A)$:
the exterior derivative $d$ applied to a vertical form produces a form
whose vertical component has weight $\geq 2$ in $\varTheta_A$, but the
contact distribution forces $\varTheta_A \wedge \varTheta_A = 0$
(since $\varTheta_A$ is a $1$-form), so $\pi_V(d(\pi_V\alpha)) = 0$.
For the middle term, we first establish the key commutation relation.
Since $\pi_V$ is the projection onto the non-zero-weight summand of
the $T$-action on $\Omega^k(A)$, and $d$ is the universal derivation,
the commutator $[d, \pi_V] = d \circ \pi_V - \pi_V \circ d$ measures
how much $d$ fails to preserve the weight grading. On a weight-$n$
form $\alpha_n$, we have $d\alpha_n = (d\alpha_n)_H + (d\alpha_n)_V$;
the weight-shift arises from the Lie derivative along $\xi$ (the
generator of $T$), giving

$$
  [d, \pi_V]\alpha = \mathcal{L}_\xi(\alpha) - \pi_V(\mathcal{L}_\xi(\alpha))
  = \pi_H(\mathcal{L}_\xi\alpha).
$$

Since $\pi_H + \pi_V = \mathrm{id}$ and
$\mathcal{L}_\xi = \iota_\xi \circ d + d \circ \iota_\xi$
(Cartan's formula), the middle term simplifies:
$d(\pi_V d\alpha) + \pi_V d(d\alpha) = \omega_V \wedge_q [\xi, \alpha]$
where $\omega_V = d(\pi_V(d1_A)) \in \Omega^2(A)$ is the curvature
of the weight projection — a canonical $2$-form measuring the failure
of the horizontal distribution to be integrable.
