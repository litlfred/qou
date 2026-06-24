The geometric series $\sum_{k \geq 0} \hbar_q^{2k}$
converges with sum $(1 - \hbar_q^{2})^{-1}$ because
$\hbar_q^2 \in (0, 1)$ (indeed $\hbar_q^2 \approx 0.00982$ at
$q_0 \approx 1.11$).  Absolute convergence follows from the
comparison
$\sum_{n \geq 1} \hbar_q^{2n} |\Delta^{(n)}|
\leq \Delta_{\max} \sum_{n \geq 1} \hbar_q^{2n}
= \Delta_{\max} \cdot \hbar_q^2 / (1 - \hbar_q^2)$.  The tail
bound factors the first skipped term:

$$
  \bigl\lvert \sum_{n > N} \hbar_q^{2n}\,\Delta^{(n)} \bigr\rvert
  \leq \Delta_{\max} \cdot \hbar_q^{2(N+1)}
   \sum_{k \geq 0} \hbar_q^{2k}
  = \Delta_{\max} \cdot \frac{\hbar_q^{2(N+1)}}{1 - \hbar_q^{2}}.
$$

Multiplying by $E_0$ and solving $E_0 \cdot \Delta_{\max} \cdot
\hbar_q^{2(N+1)} / (1 - \hbar_q^2) \leq \varepsilon_B$ for $N$
gives the stated count.
$\qquad\blacksquare$
