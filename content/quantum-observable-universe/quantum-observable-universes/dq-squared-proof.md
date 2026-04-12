
Write $a = q^{-1}$ and $b = 1 - q^{-1}$, so $a + b = 1$. Then

```tex
\begin{align*}
  d_q^2\alpha
  &= d_q\bigl(ad\alpha + b\theta \wedge \mathcal{L}_\xi\alpha\bigr) \\
  &= a^2d^2\alpha
     + abd(\theta \wedge \mathcal{L}_\xi\alpha)
     + ab\theta \wedge \mathcal{L}_\xid\alpha
     + b^2\theta \wedge \mathcal{L}_\xi(\theta \wedge \mathcal{L}_\xi\alpha).
\end{align*}
```

The first term vanishes since $d^2 = 0$. The second expands as
$abd\theta \wedge \mathcal{L}_\xi\alpha - ab\theta \wedge d\mathcal{L}_\xi\alpha$.
The third term cancels the second's negative part because
$[d, \mathcal{L}_\xi] = 0$ implies
$\theta \wedge \mathcal{L}_\xid\alpha = \theta \wedge d\mathcal{L}_\xi\alpha$.
For the fourth term, the Reeb field satisfies
$\mathcal{L}_\xi\theta = 0$ (since $\iota_\xi d\theta = 0$ and $\theta(\xi)=1$), so
$\mathcal{L}_\xi(\theta \wedge \mathcal{L}_\xi\alpha) = \theta \wedge \mathcal{L}_\xi^2\alpha$;
the factor $\theta \wedge \theta = 0$ in $b^2\theta \wedge \theta \wedge \mathcal{L}_\xi^2\alpha$ kills this term. Hence
$d_q^2\alpha = abd\theta \wedge \mathcal{L}_\xi\alpha$.
