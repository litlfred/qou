**Proposition (symbolic Hoefsmit Gram on $H_3(q)$).** *Let $u = \sqrt{q}$ with $u > 0$. On the 6-element NF basis, the Hoefsmit-seminormal Gram matrix $G(q)$ has exact Laurent polynomial entries. Then:*
1. *$G(q)$ is symmetric: $G[i,j] = G[j,i]$ for all $i, j$.*
2. *$G[0,0] = 1$.*
3. *$\det G(q) \neq 0$ for $q > 0,\ q \neq 1$.*

## Numerical evaluation at the substrate

Sympy-computed symbolic entries match the $q_0 \approx 1.110$ empirical values to a maximum absolute difference $\approx 2.1 \times 10^{-16}$. The determinant at $u_0 = \sqrt{q_0}$ is $\approx -0.189$. This includes one negative eigenvalue $\approx -0.855$, which shows that Frobenius positivity applies a non-trivial constraint.

## Role in the framework

This proposition replaces the Phase 1a empirical Gram matrix with categorical closed-form entries. Downstream consumers can now rely on proven structural properties. The remaining $\det \neq 0$ proof reduces the Phase 1 workstream to a symbolic-determinant computation.
