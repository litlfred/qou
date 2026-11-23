**Proof.** Throughout, $h = q - q^{-1}$ denotes the Hecke amplitude and $[2]_q = q + q^{-1}$, $[3]_q = q^2 + 1 + q^{-2}$ the balanced quantum integers, with $q > 0$ real.

**Step 1: The seminormal matrices on $V_{(2,1)}$.** In the Hoefsmit seminormal basis of the two-dimensional representation $V_{(2,1)}$ of $H_3(q)$, the first generator is diagonal,

$$
\sigma_1 = \begin{pmatrix} q & 0 \\ 0 & -q^{-1} \end{pmatrix},
$$

and the second generator is the real symmetric matrix

$$
\sigma_2 = \begin{pmatrix} a & b \\ b & c \end{pmatrix},
\qquad
a = \frac{q - q^{-1}}{1 - q^{4}},
\qquad
c = \frac{q - q^{-1}}{1 - q^{-4}},
\qquad
b^2 = \frac{[3]_q}{[2]_q^2},
$$

with $b > 0$; the off-diagonal entry is the binding amplitude of [the Hoefsmit proposition](#prop:hoefsmit-binding-amplitude). These entries satisfy the two seminormal identities

$$
a + c
= h \cdot \frac{(1 - q^{-4}) + (1 - q^{4})}{(1-q^{4})(1-q^{-4})}
= h,
\qquad
a c
= \frac{h^2}{2 - q^{4} - q^{-4}}
= \frac{-h^2}{(q^{2} - q^{-2})^{2}}
= \frac{-1}{[2]_q^2},
$$

so that $\det \sigma_2 = ac - b^2 = -\bigl(1 + [3]_q\bigr)/[2]_q^2 = -[2]_q^2/[2]_q^2 = -1$ and $\mathrm{tr}\,\sigma_2 = h$: both generators have the Hecke eigenvalues $q$ and $-q^{-1}$. These are Hoefsmit's seminormal matrices for the standard representation, with diagonal entries indexed by the axial distances $\pm 2$ of the two standard tableaux of shape $(2,1)$; they satisfy the braid relation $\sigma_1\sigma_2\sigma_1 = \sigma_2\sigma_1\sigma_2$ by the seminormal construction \cite{hoefsmit1974,wenzl1988c}.

**Step 2: Determinant of the knot operator.** Since each generator has eigenvalue product $q \cdot (-q^{-1}) = -1$, it follows that $\det \sigma_1 = \det \sigma_2 = -1$ and $\det \sigma_2^{-1} = -1$. Hence for $A = \sigma_1 \sigma_2^{-1}$ and $M_{4_1} = A^2$,

$$
\det A = (-1)(-1) = 1,
\qquad
\det M_{4_1} = 1 .
$$

**Step 3: Trace of the knot operator.** The Hecke relation $\sigma_2^2 = h\sigma_2 + 1$ gives $\sigma_2^{-1} = \sigma_2 - h$, so

$$
\mathrm{tr}(A) = \mathrm{tr}(\sigma_1 \sigma_2) - h\,\mathrm{tr}(\sigma_1).
$$

Because $\sigma_1$ is diagonal, only the diagonal entries of $\sigma_2$ contribute to the first term:

$$
\mathrm{tr}(\sigma_1\sigma_2)
= q\,a - q^{-1} c
= h \left( \frac{q}{1 - q^{4}} - \frac{q^{-1}}{1 - q^{-4}} \right)
= h \cdot \frac{q + q^{3}}{1 - q^{4}}
= \frac{(q - q^{-1})\, q}{1 - q^{2}}
= -1,
$$

using $q^{-1}/(1 - q^{-4}) = -q^{3}/(1 - q^{4})$ and $1 - q^4 = (1-q^2)(1+q^2)$. With $\mathrm{tr}(\sigma_1) = q - q^{-1} = h$ this yields

$$
\mathrm{tr}(A) = -1 - h^2 = 1 - q^{2} - q^{-2},
$$

and therefore, by the Cayley--Hamilton identity $\mathrm{tr}(A^2) = \mathrm{tr}(A)^2 - 2\det A$ for $2 \times 2$ matrices,

$$
\mathrm{tr}(M_{4_1})
= \bigl(1 - q^{2} - q^{-2}\bigr)^{2} - 2
= q^{4} - 2q^{2} + 1 - 2q^{-2} + q^{-4}.
$$

At the classical point $q = 1$ this equals $-1$, and it is a smooth function of $q$ on $q > 0$.

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

This proves the unit-modulus claim, with the rotation angle determined by the closed-form trace of Step 3. At $q = 1$ the trace is $-1$, so $\theta = 2\pi/3$ exactly (the eigenvalues are the primitive cube roots of unity); at the substrate value of $q$ the angle evaluates to $\theta \approx 117.09^{\circ}$. The eigenvalue degenerates to $\lambda = 1$ ($\theta = 0$) exactly at the golden endpoints $q \in \{\varphi^{-1}, \varphi\}$, where $\mathrm{tr}(M_{4_1}) = 2$, and the boundary value $\theta = \pi$ is never attained on the real axis since $\mathrm{tr}(M_{4_1}) + 2$ is a nonzero square. Outside the golden interval, for $q > \varphi$ or $0 < q < \varphi^{-1}$, the two golden factors in Step 4 have the same sign, so $t - 2 > 0$; the discriminant $t^2 - 4$ is then positive, the roots of $\lambda^2 - t\lambda + 1$ are real, distinct and positive with product $1$, and neither has modulus $1$. $\square$
