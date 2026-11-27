The Gram matrix $G$ over $H_3(q)$ has a characteristic polynomial whose eigenvalue crossings are controlled by the discriminant of the Hecke relation $(T - q)(T + q^{-1}) = 0$. The smallest eigenvalue $\lambda_{\min}(\mathrm{G}(q))$ is continuous in $q$. At the Markov parameter $z = q^3/(q^2+1)$, the **bilinear** pairing $\mathrm{tr}_M(b_i b_j)$ carries one negative eigenvalue, $\lambda_{\min}(q_0) = -0.75270211$ (with a one-dimensional radical from $y_{(1^3)} = 0$), whereas on the **star** pairing $\mathrm{tr}_M(b_i b_j^*)$ the form is positive semidefinite with signature $(5,0,1)$. Any sign claim here must name which pairing it means.

Write $T_q$ in the NF basis. The target-flip amplitude $P_{7,6}(q)$ determines the off-diagonal mass component. The diagonal $P_{7,7}(q)$ determines the Wedderburn weight of the standard channel ([Toffoli transfer matrix](#prop:toffoli-transfer-matrix)). Positivity of $G\vec{t}(q)$ therefore reduces to the positivity of the product $P_{7,7}(q) \cdot W_{\mathrm{std}}(q)$ with the appropriate sign from the off-diagonal amplitude.

**Open step — the second half of the reduction is underived.** The derived off-diagonal amplitude is
$$
  P_{7,6}(q) \;=\; -\frac{(q-1)(q+1)(q^6+q^4+2q^2+1)}{2q(q^2+1)^2}
$$
([Toffoli transfer matrix](#prop:toffoli-transfer-matrix)). The reduction above is asserted in a single clause and the part that carries the weight — *"with the appropriate sign from"* the off-diagonal amplitude — is not derived: nothing states what that sign must be, or why. The first factor satisfies $P_{7,7}(q)\,W_{\mathrm{std}}(q) > 0$ for all $q > 0$; the second is open.

Solving $P_{7,7}(q) = 0$ on $(0,\infty)$: the numerator is $q^3(q^4+1)$, whose only real zero is $q = 0$, so the derived diagonal **has no positive zero**.

Solving $P_{7,6}(q) = 0$ on $(0,\infty)$: the factor $(q-1)$ gives $q = 1$; the factor $(q+1)$ has no positive root; and $q^6 + q^4 + 2q^2 + 1 > 0$ for every real $q$. So $q = 1$ is the **only** positive zero.

For $q > 1$: $P_{7,7}(q) > 0$ but $P_{7,6}(q) < 0$, since the sextic factor is positive and the sign is carried by $-(q-1)(q+1)$. The Wedderburn weights $W_{\mathrm{sym}} = W_{\mathrm{alt}} = q^2/(q^4 + 4q^2 + 1)$ and $W_{\mathrm{std}} = (q^2+1)^2/(q^4 + 4q^2 + 1)$ are strictly positive. So the sign pattern on the physical regime is **mixed**, not uniformly positive: the amplitudes of the derived family are not all of the same sign. Whether linear reduction preserves feasibility under a mixed pattern is the open step above; item 4 of the proposition evaluates $G\vec t(q_0)$ directly instead.

For $0 < q < 1$: $P_{7,6}(q) > 0$. The sign reversal of the off-diagonal amplitude occurs at $q = 1$ and nowhere else.

The boundedness of shadow prices is not a consequence of LP duality ([LP-dual stability](#prop:lp-dual-stability) states only feasibility and strong duality). The bound used here is the one recorded in the [confinement reading](#rem:lp-dual-stability-confinement-reading): the dual norm $|y^*|$ bounded by the primal norm times the Gram condition number $\kappa(\mathrm{G}(q)) = \lambda_{\max}(G)/|\lambda_{\min}(G)|$. **Open step (Gram singularity).** At $z = q^3/(q^2+1)$ the Markov–Gram form is singular ($y_{(1^3)} = 0$), so the ratio $\lambda_{\max}/|\lambda_{\min}|$ is not a finite condition number on the full six-dimensional normal-form span. Moreover, at $q_0$, $P_{7,7}(q_0) \approx 0.6912 > 0$ whereas $P_{7,6}(q_0) \approx -0.1438 < 0$. Closing the shadow-price bound requires passing to the quotient by the radical, and closing the amplitude step requires deriving the off-diagonal sign relation. $\square$

**Physical consequence.**
The aether parameter $q_0 \approx 1.110$ sits on the $q > 1$ side of the single threshold $q = 1$, where the diagonal amplitudes are positive and $P_{7,6}(q_0)$ is negative.
