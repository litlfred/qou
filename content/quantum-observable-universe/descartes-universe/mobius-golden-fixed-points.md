**Proposition.**
The Möbius transformation $f(q) = (4-q)/(4q+3)$ arising from the
leading coefficients of the color-tube cubic has fixed points
$q_+ = 1/\varphi$ and $q_- = -\varphi$, where $\varphi = (1+\sqrt{5})/2$
is the golden ratio.

*Proof.*
Setting $f(q) = q$ gives $(4-q) = q(4q+3)$, hence $4q^2 + 4q - 4 = 0$,
or equivalently

$$
q^2 + q - 1 = 0.
$$

The quadratic formula yields

$$
q = \frac{-1 \pm \sqrt{5}}{2}.
$$

Since $\varphi = (1+\sqrt{5})/2$, the roots are $q_+ = (-1+\sqrt{5})/2 = 1/\varphi$
and $q_- = (-1-\sqrt{5})/2 = -\varphi$.  The polynomial $q^2 + q - 1$ is the
minimal polynomial of $1/\varphi$ over $\mathbb{Q}$.

The Möbius matrix $M = \bigl(\begin{smallmatrix} -1 & 4 \\ 4 & 3 \end{smallmatrix}\bigr)$
has determinant $\det M = -3 - 16 = -19$ (prime, orientation-reversing),
trace $\operatorname{tr} M = 2$, characteristic polynomial $\lambda^2 - 2\lambda - 19$,
and eigenvalues $1 \pm 2\sqrt{5} = 4\varphi - 1$ and $3 - 4\varphi$. $\square$

The matrix entries $\{-1, 4; 4, 3\}$ derive from the binomial
structure of the color-tube cubic
([color-tube cubic](#rem:color-tube-cubic)):
$4 = \binom{4}{1}$ is the leading $z$-coefficient of the $c^2$ term,
$3$ is the degree of the cubic, and the sign comes from the numerator
$4 - q = -(q - 4)$.
