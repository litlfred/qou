**Proof (continued).**

**Step 4: The trace lies strictly between $-2$ and $2$ on the golden interval.** Write $\varphi = (1 + \sqrt{5})/2$ for the golden ratio. Two exact factorizations control the boundary values:

$$
\mathrm{tr}(M_{4_1}) + 2 = \bigl(q^{2} - 1 + q^{-2}\bigr)^{2},
\qquad
\mathrm{tr}(M_{4_1}) - 2 = \frac{(q^{2} - q - 1)(q^{2} + q - 1)(q^{2} - q + 1)(q^{2} + q + 1)}{q^{4}},
$$

both verified by expanding. The base $q^{2} - 1 + q^{-2}$ never vanishes for real $q$ (its numerator $q^{4} - q^{2} + 1$ has non-real roots $q^{2} = (1 \pm i\sqrt{3})/2$), so $\mathrm{tr}(M_{4_1}) + 2 > 0$ for every real $q \neq 0$. In the second factorization the cyclotomic factors $q^{2} - q + 1$ and $q^{2} + q + 1$ are positive for all real $q$ (negative discriminants), while for $\varphi^{-1} < q < \varphi$ the golden factors have opposite signs: $q^{2} + q - 1 > 0$ (its positive root is $\varphi^{-1}$) and $q^{2} - q - 1 < 0$ (its positive root is $\varphi$). Hence $\mathrm{tr}(M_{4_1}) - 2 < 0$ on the golden interval, and combining,

$$
\bigl|\mathrm{tr}(M_{4_1})\bigr| \;<\; 2
\qquad \text{for } \varphi^{-1} < q < \varphi .
$$

This interval contains the classical point $q = 1$ and the substrate regime.

**Step 5: Unit-modulus eigenvalues.** $M_{4_1}$ is a real $2 \times 2$ matrix with $\det M_{4_1} = 1$ and real trace $t = \mathrm{tr}(M_{4_1})$, so its eigenvalues are the roots of $\lambda^{2} - t\lambda + 1 = 0$. By Step 4 the discriminant $t^{2} - 4$ is strictly negative on the golden interval, so the roots form a complex-conjugate pair $\lambda_{4_1} = e^{\pm i\theta}$ with

$$
|\lambda_{4_1}|^{2} = \lambda \bar{\lambda} = \det M_{4_1} = 1,
\qquad
2\cos\theta = \mathrm{tr}(M_{4_1}).
$$

This proves the unit-modulus claim, with the rotation angle determined by the closed-form trace of Step 3. At $q = 1$ the trace is $-1$, so $\theta = 2\pi/3$ exactly (the eigenvalues are the primitive cube roots of unity); at the substrate value of $q$ the angle evaluates to $\theta \approx 117.09^{\circ}$. The eigenvalue degenerates to $\lambda = 1$ ($\theta = 0$) exactly at the golden endpoints $q \in \{\varphi^{-1}, \varphi\}$, where $\mathrm{tr}(M_{4_1}) = 2$, and the boundary value $\theta = \pi$ is never attained on the real axis since $\mathrm{tr}(M_{4_1}) + 2$ is a nonzero square. $\square$
