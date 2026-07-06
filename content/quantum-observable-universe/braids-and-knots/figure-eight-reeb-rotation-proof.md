**Proof sketch.** The Hoefsmit seminormal matrix $\sigma_i$ on $V_{(2,1)}$ has eigenvalues $q$ and $-q^{-1}$. It satisfies the characteristic equation $\sigma^2 = h\sigma + 1$. The inverse $\sigma^{-1} = \sigma - h$ has eigenvalues $q^{-1}$ and $-q$. These have the same absolute values, since $|q| = |q^{-1}|$ and $|{-q^{-1}}| = |{-q}|$.

The alternating product $\sigma_1\sigma_2^{-1}$ composes a generator with its partner's inverse. On the $2 \times 2$ Hoefsmit block:

- The diagonal entries are $a_\rho$ and $a_{-\rho}$. These satisfy $a_\rho + a_{-\rho} = h$ and $a_\rho \cdot a_{-\rho} = -(b^2 - 1) = -[3]_q/[2]_q^2 + 1 = -1/[2]_q^2$.
- The determinant is $\det(\sigma_i) = a_\rho a_{-\rho} - b^2 = -1$. This matches the eigenvalue product $q \cdot (-q^{-1}) = -1$.

We compute $\det(M_{4_1}) = (\det\sigma_1)^2 (\det\sigma_2^{-1})^2 = (-1)^2 \cdot (-1)^{-2} = 1$. The trace $\mathrm{tr}(M_{4_1})$ is real because the braid is a word in Hermitian-conjugate pairs. Since the determinant is 1 and the trace is real, the eigenvalues are complex conjugates on the unit circle. $\square$
