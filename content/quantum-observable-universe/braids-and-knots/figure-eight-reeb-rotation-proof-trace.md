**Proof (continued).**

**Step 2: Determinant of the knot operator.** Since each generator has eigenvalue product $q \cdot (-q^{-1}) = -1$, we get $\det \sigma_1 = \det \sigma_2 = -1$ and $\det \sigma_2^{-1} = -1$. Hence for $A = \sigma_1 \sigma_2^{-1}$ and $M_{4_1} = A^2$,

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
