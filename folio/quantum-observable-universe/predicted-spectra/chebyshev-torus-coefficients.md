The torus knot $T_{2,n}$ is the closure of $\sigma^n$ in $H_2(q)$.
Its **crossing coefficients** $(c_n, d_n)$ in the $2 \times 2$
transfer matrix satisfy the **Chebyshev recurrence**:

$$
  \boxed{
    c_n = U_{n-1}(\tfrac{q - q^{-1}}{2}),
    \qquad
    d_n = -\frac{c_n \cdot qs_q}{1 + c_n}
  }
$$

where $U_k$ is the Chebyshev polynomial of the second kind and
$s_q = q^{1/2} - q^{-1/2}$.

Equivalently, from the matrix power
$T(1,0)^n = \bigl(\begin{smallmatrix} a_n & c_n \\ c_n & d_n \end{smallmatrix}\bigr)$:

$$
  c_1 = 1, \quad d_1 = 0
  \qquad\text{(bare crossing)}
$$

$$
  c_{n+1} = c_n(q - q^{-1}) + c_n + d_n, \qquad
  d_{n+1} = c_n
$$
