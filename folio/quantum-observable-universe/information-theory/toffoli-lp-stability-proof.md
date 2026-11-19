*Proof.*
The Gram matrix $G$ over $H_3(q)$ has a characteristic polynomial whose eigenvalue crossings are controlled by the discriminant of the Hecke relation $(T - q)(T + q^{-1}) = 0$. Its smallest eigenvalue $\lambda_{\min}(\mathrm{G}(q))$ is continuous in $q$, and its signature depends on which pairing is chosen: under the canonical convention $z_D = q^3/(q^2+1)$, the **bilinear** pairing $\mathrm{tr}_M(b_i b_j)$ carries one negative eigenvalue ($\lambda_{\min}(q_0) = -0.75270211$) and a one-dimensional radical, whereas the **star** pairing $\mathrm{tr}_M(b_i b_j^*)$ is positive semidefinite with signature $(5,0,1)$. Any spectral sign statement must therefore specify the pairing.

Write $T_q$ in the normal-form basis. The target-flip amplitude $P_{7,6}(q)$ determines the off-diagonal component, while the diagonal $P_{7,7}(q)$ determines the Wedderburn weight of the standard channel ([Toffoli transfer matrix](#prop:toffoli-transfer-matrix)), where
$$
  P_{7,6}(q) \;=\; -\frac{(q-1)(q+1)(q^6+q^4+2q^2+1)}{2q(q^2+1)^2}.
$$
While $P_{7,7}(q)\,W_{\mathrm{std}}(q) > 0$ holds for every $q > 0$, a single-product reduction of $G\vec{t}(q) \geq 0$ to $P_{7,7}(q)\,W_{\mathrm{std}}(q)$ times a sign factor from $P_{7,6}(q)$ does not close on its own; as shown in the proposition, the exact cone constraint is quadratic rather than monomial in the amplitudes.

Solving $P_{7,7}(q) = 0$ on $(0,\infty)$: the numerator is $q^3(q^4+1)$, whose only real zero is $q = 0$, so the derived diagonal **has no positive zero** (whereas the golden-ratio value $q_\star = 1/\varphi^2 = (3-\sqrt5)/2 \approx 0.382$ is a root only of the alternative convention-$C$ diagonal $(q + q^{1/2} - 1)/(q+1)$).

Solving $P_{7,6}(q) = 0$ on $(0,\infty)$: the factor $(q-1)$ gives $q = 1$; the factor $(q+1)$ has no positive root; and $q^6 + q^4 + 2q^2 + 1 > 0$ for every real $q$. Thus $q = 1$ is the **only** positive zero (the value $q_\Phi \approx 0.4656$ was a root of the cubic factor $q^{3/2} + q^{1/2} - 1$ of $\Phi$ and corresponds to no zero of the derived amplitudes).

For $q > 1$: $P_{7,7}(q) > 0$ whereas $P_{7,6}(q) < 0$, since the sextic factor is positive and the sign is carried by $-(q-1)(q+1)$. The Wedderburn weights $W_{\mathrm{sym}} = W_{\mathrm{alt}} = q^2/(q^4 + 4q^2 + 1)$ and $W_{\mathrm{std}} = (q^2+1)^2/(q^4 + 4q^2 + 1)$ are strictly positive. The sign pattern on $q > 1$ is therefore **mixed** rather than uniformly positive, and LP feasibility at $q_0$ is established instead by direct evaluation of $G\vec{t}(q_0) > 0$.

For $0 < q < 1$: $P_{7,6}(q) > 0$. The sign reversal of the off-diagonal amplitude occurs at $q = 1$ and nowhere else on $(0,\infty)$.

On any non-degenerate subspace, LP duality ([LP-dual stability](#prop:lp-dual-stability)) bounds the dual norm $|y^*|$ by the primal norm times the condition number $\kappa(\mathrm{G}(q)) = \lambda_{\max}(G)/|\lambda_{\min}(G)|$. Because the Markov–Gram form under convention $D$ is singular on the full six-dimensional normal-form span, closing the shadow-price bound requires descending to the quotient by its radical. $\square$

**Regime at the aether parameter.**
The aether parameter $q_0 \approx 1.110$ lies on the $q > 1$ side of the unique operator threshold $q = 1$, where the diagonal amplitudes are strictly positive ($P_{7,7}(q_0) \approx 0.6912$) and $P_{7,6}(q_0) \approx -0.1438$ is negative. Well-definedness of the $q$-GoL ([q-Game of Life](#prop:q-game-of-life)) rests on $P_{7,7}(q) > 0$ and $P_{7,6}(q) \neq 0$ rather than on uniform amplitude positivity or on an aether threshold at $q_\star$.
